# WIPI Wiki — Project Memory

이 파일은 **Claude Code가 이 프로젝트를 이어받기 위한 컨텍스트 메모**입니다.
모든 결정사항, 진행 상태, 남은 작업이 여기 있습니다. 새 세션을 시작하면
이 파일을 먼저 읽고, 그 다음 작업을 이어가세요.

---

## 프로젝트 목표

**WIPI 1.2.1 (한국 옛날 휴대폰 표준 플랫폼) 개발자용 위키**를 만든다.

소스는 두 가지:
1. **PDF**: `vendor/WIPI_V1_2_1_final_ST1_2_1_.pdf` (939페이지 한국어 규격서, 1.9 MB, C언어 API)
2. **JavaDoc HTML**: [nikita36078/J2ME_Docs](https://github.com/nikita36078/J2ME_Docs)의 `docs/WIPI_API_1_1_1/` 폴더, JAVA API

결과물:
- MkDocs Material 사이트 → GitHub Pages 배포
- 모든 콘텐츠가 순수 Markdown → LLM (Claude 포함)이 grep/read로 직접 참조 가능
- 사이트 전역 검색 (한국어 토크나이징 포함)
- `llms.txt` / `llms-full.txt`로 LLM 친화적 진입점 제공

---

## 핵심 결정사항 (이미 결정됨, 바꾸지 말 것)

| 항목 | 선택 | 이유 |
|---|---|---|
| 정적 사이트 생성기 | **MkDocs Material** | 한국어 무설정 지원, 레퍼런스 문서 UI에 최적, Python+MD 단순 빌드, GitHub Pages 친화 |
| 검색 | **Pagefind** (외부 통합) | MkDocs 기본 검색보다 CJK 토크나이징 우수, 100% 클라이언트 사이드 |
| 콘텐츠 포맷 | **순수 Markdown** | LLM 친화, GitHub에서도 잘 보임 |
| JavaDoc 처리 | **HTML → MD 완전 변환** | 검색 통합 위해. iframe/HTML 보존 안 함 |
| PDF 처리 | **목차 기반 섹션별 분할** | 한 파일 = 한 섹션 |
| 배포 | **GitHub Actions → gh-pages** | `mkdocs gh-deploy` 직접 하지 말 것 |
| LLM 접근 | `llms.txt` + `llms-full.txt` 표준 | [llmstxt.org](https://llmstxt.org/) |

---

## 현재 진행 상태

### ✅ 완료된 것

1. **디렉토리 스캐폴드** (아래 "디렉토리 구조" 섹션 참고)

2. **JavaDoc → Markdown 변환기**: `scripts/convert_javadoc.py`
   - 입력: `vendor/j2me_docs/docs/WIPI_API_1_1_1/` (sparse-clone)
   - 출력: `docs/java-api/`
   - **11개 패키지, 135개 클래스 변환 완료** — 이미 `docs/java-api/`에 결과물 있음
   - 처리하는 것: 클래스 설명, 상속 트리, 필드/생성자/메서드 요약, 필드/생성자/메서드 상세, Parameters/Returns 블록
   - 패키지별 인덱스 페이지(`<pkg>/index.md`)와 최상위 인덱스(`java-api/index.md`)도 자동 생성

3. **PDF 텍스트 추출 검증 완료**
   - 한국어가 `Adobe-Korea1` CID 폰트로 인코딩돼 있어 `pdftotext` 단독으로는 빈 출력
   - **반드시** `apt install poppler-data` 한 뒤 `pdftotext -layout` 사용
   - 추출 검증: `pdftotext -f 1 -l 1 vendor/WIPI_V1_2_1_final_ST1_2_1_.pdf - | head` → "모바일 표준 플랫폼 규격"이 나오면 OK

4. **프로젝트 보조 파일**: `.gitignore`, `requirements.txt`

### 🔧 알려진 마이너 이슈 (변환 결과물에 있음)

`scripts/convert_javadoc.py`는 정상 동작하지만, 다음 케이스는 미세하게 부정확:

- **다중 파라미터 메서드의 nested `<dd>`**: WIPI JavaDoc HTML이 비표준 nested `<dd>` 구조를 가질 때(예: `<dd>id...<dd>val...</dd></dd>`) 두 번째 파라미터(`val`)만 노출되고 첫 번째(`id`)가 묶여서 누락될 수 있음. 단일 파라미터/리턴 케이스는 완벽. 예시 클래스: `org.kwis.msp.handset.HandsetProperty.setSystemProperty` 메서드 상세에서 `id` 누락 확인 가능.
- **수정 방향**: `_list_to_md`에서 nested wrapper `<dd>` 안의 own-text를 추출해 별도 항목으로 추가. 또는 `<dt>` 기준으로 forward-walk하면서 다음 `<dt>` 전까지의 모든 텍스트를 한 term의 본문으로 합치는 방식으로 재작성.

### ❌ 남은 작업 (우선순위 순)

#### 1. JavaDoc 변환기 nested `<dd>` 패치
`scripts/convert_javadoc.py`의 `_list_to_md` 보강. 위 "알려진 이슈" 참고. 변환 재실행:
```bash
python3 scripts/convert_javadoc.py vendor/j2me_docs/docs/WIPI_API_1_1_1 docs/java-api
```

#### 2. PDF → Markdown 변환기 작성
파일: `scripts/extract_pdf.py`

전략:
- `pdftotext -layout` 으로 전체 텍스트 추출 (poppler-data 설치 후)
- 정규식 `^(\d+(?:\.\d+)*)\.\s+(.+)$` 로 섹션 헤더 인식
- 챕터별로 분할해 아래 파일들에 저장
- 표는 `pdfplumber`로 page-by-page 별도 추출 → Markdown 테이블로 재구성
- 그림이 있는 페이지는 `pdfimages -png -f N -l N`으로 추출 → `docs/assets/figures/`

PDF의 목차 (이미 추출해서 확인함):
```
1. 서론                     → docs/overview/introduction.md
2. 개념적 구조              → docs/overview/architecture.md
3. 플랫폼 일반 사항         → docs/overview/platform.md

4. HAL 규격
  4.1 Type Definition       → docs/hal/types.md
  4.2 플랫폼이 제공하는 API → docs/hal/platform-api.md
  4.3 System                → docs/hal/system.md
  4.4 CALL                  → docs/hal/call.md
  4.5 HandSet Device        → docs/hal/handset.md
  4.6 네트워크              → docs/hal/network.md
  4.7 Serial                → docs/hal/serial.md
  4.8 MEDIA                 → docs/hal/media.md
  4.9 TIME                  → docs/hal/time.md
  4.10 UTILITY              → docs/hal/utility.md
  4.11 FILE                 → docs/hal/file.md
  4.12 InputMethod          → docs/hal/input-method.md
  4.13 Font                 → docs/hal/font.md
  4.14 Frame Buffer         → docs/hal/frame-buffer.md
  4.15 Virtual Key          → docs/hal/virtual-key.md

5. API 규격
  5.1 C API
    5.1.1 커널              → docs/c-api/kernel.md
    5.1.2 그래픽            → docs/c-api/graphics.md
    5.1.3 데이터베이스      → docs/c-api/database.md
    5.1.4 파일시스템        → docs/c-api/filesystem.md
    5.1.5 NETWORK           → docs/c-api/network.md
    5.1.6 매체 처리기       → docs/c-api/media.md
    5.1.7 SERIAL            → docs/c-api/serial.md
    5.1.8 PHONE             → docs/c-api/phone.md
    5.1.9 MISC              → docs/c-api/misc.md
    5.1.10 UTILITY          → docs/c-api/utility.md
    5.1.11 UI Components    → docs/c-api/ui-components.md
    5.1.12 표준 C 라이브러리→ docs/c-api/c-stdlib.md
  5.2 자바 API
    → JavaDoc 변환분이 이미 docs/java-api/ 에 있음.
    PDF의 5.2 섹션은 보조 자료로 docs/java-api/_spec/ 에 따로 두거나
    스킵해도 됨 (JavaDoc이 더 풍부함). 결정은 변환 후 비교해서.

6. 참조 문헌                → docs/appendix/references.md
7. 부속서
  7.1 한국어 EUC_KR 확장    → docs/appendix/euc-kr-extended.md
  7.2 API 추가/삭제 API     → docs/appendix/api-management.md
  7.3 보안 관련 API         → docs/appendix/security.md
  7.4 Media 관련 API        → docs/appendix/media-ext.md
```

스크립트 인터페이스 권장:
```bash
python3 scripts/extract_pdf.py vendor/WIPI_V1_2_1_final_ST1_2_1_.pdf docs/
```

#### 3. `mkdocs.yml` 작성
포함할 것:
```yaml
site_name: WIPI Wiki
site_description: WIPI 1.2.1 모바일 표준 플랫폼 API 레퍼런스
site_url: https://<username>.github.io/wipi-wiki/   # 사용자 입력 필요
repo_url: https://github.com/<username>/wipi-wiki    # 사용자 입력 필요
edit_uri: edit/main/docs/

theme:
  name: material
  language: ko
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.path
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy
    - toc.follow
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      toggle:
        icon: material/weather-night
        name: 다크 모드로 전환
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      toggle:
        icon: material/weather-sunny
        name: 라이트 모드로 전환

plugins:
  - search:
      lang: ko       # MkDocs 기본 검색 (백업용). Pagefind는 빌드 후 별도 주입.
  - awesome-pages   # 디렉토리 기반 자동 nav

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.tabbed:
      alternate_style: true
  - toc:
      permalink: true

nav:
  - 홈: index.md
  - 개요:
    - overview/introduction.md
    - overview/architecture.md
    - overview/platform.md
  - HAL 규격: hal/
  - C API: c-api/
  - Java API: java-api/
  - 부속서: appendix/
```

awesome-pages 플러그인을 쓰면 각 디렉토리에 `.pages` 파일로 정렬을 지정할 수 있음. 단순하게 시작하려면 nav를 직접 명시.

#### 4. 인덱스 페이지들 작성
- `docs/index.md` — 사이트 랜딩. 뭘 다루는지 + 빠른 링크
- `docs/overview/index.md` — 1~3장 개요 모음
- `docs/hal/index.md` — HAL 카테고리 목록
- `docs/c-api/index.md` — C API 카테고리 목록
- `docs/java-api/index.md` — 이미 변환기가 생성함. 검토 후 다듬기
- `docs/appendix/index.md` — 부속서 모음

#### 5. `llms.txt` / `llms-full.txt` 생성기
파일: `scripts/build_llms_txt.py`

- `llms.txt`: 프로젝트 한 단락 소개 + 모든 페이지의 절대 URL 리스트 (사이트 빌드 후 sitemap 기준)
- `llms-full.txt`: 모든 `.md` 파일을 한 파일로 concat (헤더로 페이지 구분)

빌드 워크플로우에서 `mkdocs build` 직전에 실행해 `docs/` 안에 같이 들어가게 하거나, `site/` 빌드 후 `site/llms.txt`로 직접 출력.

#### 6. GitHub Actions 배포 워크플로우
파일: `.github/workflows/deploy.yml`

대략 이런 형태:
```yaml
name: Deploy
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install -r requirements.txt
      - run: mkdocs build --strict
      # Pagefind index
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npx -y pagefind --site site
      # llms.txt
      - run: python3 scripts/build_llms_txt.py site
      - uses: actions/upload-pages-artifact@v3
        with: { path: site }
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

#### 7. `README.md`
- 프로젝트 소개 (사용자용)
- 로컬 빌드 가이드: `pip install -r requirements.txt && mkdocs serve`
- 변환 스크립트 사용법 (vendor 준비 + 실행)
- 기여 방법

#### 8. 검증
```bash
mkdocs build --strict       # 에러 0 확인
python3 -m http.server -d site 8000   # 로컬에서 페이지 확인
```

---

## 디렉토리 구조 (현재)

```
wipi-wiki/
├── CLAUDE.md                ← 이 파일
├── .gitignore
├── requirements.txt
├── README.md                ← 작성 예정
├── mkdocs.yml               ← 작성 예정
├── docs/
│   ├── index.md             ← 작성 예정
│   ├── overview/            ← 비어있음 (PDF에서 채울 예정)
│   ├── hal/                 ← 비어있음 (PDF에서 채울 예정)
│   ├── c-api/               ← 비어있음 (PDF에서 채울 예정)
│   ├── java-api/            ✅ 135 classes 변환 완료
│   │   ├── index.md
│   │   ├── java/io/         (java.io.* 클래스들)
│   │   ├── java/lang/
│   │   ├── java/util/
│   │   └── org/kwis/...     (org.kwis.* 클래스들)
│   ├── appendix/            ← 비어있음 (PDF에서 채울 예정)
│   └── assets/
│       └── pdf/             ← 원본 PDF 호스팅 (배포 시 복사)
├── scripts/
│   ├── convert_javadoc.py   ✅ 작동 중 (마이너 패치만 남음)
│   ├── extract_pdf.py       ← 작성 예정
│   └── build_llms_txt.py    ← 작성 예정
├── .github/workflows/
│   └── deploy.yml           ← 작성 예정
└── vendor/                  (gitignore됨, 외부 소스 받는 위치)
    ├── WIPI_V1_2_1_final_ST1_2_1_.pdf
    └── j2me_docs/           (sparse-clone)
```

---

## 외부 소스 다시 받기 (Claude Code 환경 셋업)

### PDF
사용자가 `vendor/WIPI_V1_2_1_final_ST1_2_1_.pdf`로 직접 배치. 파일이 `.gitignore`되어 있어 repo에 안 들어감.

### JavaDoc HTML
```bash
mkdir -p vendor
git clone --depth 1 --filter=blob:none --sparse \
    https://github.com/nikita36078/J2ME_Docs.git vendor/j2me_docs
cd vendor/j2me_docs && git sparse-checkout set "docs/WIPI_API_1_1_1" && cd ../..
```

---

## 시스템 의존성 (셋업 한번)

```bash
# 한국어 PDF 처리에 필수 — 빼먹으면 PDF가 빈 텍스트로 추출됨
sudo apt install -y poppler-utils poppler-data

# Python 패키지
pip install -r requirements.txt
```

---

## 변환 스크립트 사용법

```bash
# JavaDoc 변환 (이미 한 번 실행되어 docs/java-api/ 채워짐)
python3 scripts/convert_javadoc.py \
    vendor/j2me_docs/docs/WIPI_API_1_1_1 \
    docs/java-api

# PDF 변환 (스크립트 작성 후)
python3 scripts/extract_pdf.py \
    vendor/WIPI_V1_2_1_final_ST1_2_1_.pdf \
    docs/

# llms.txt 빌드 (스크립트 작성 후, mkdocs build 후 실행)
python3 scripts/build_llms_txt.py site/
```

---

## 함정 / 주의사항

1. **PDF 한국어 폰트 매핑**
   `pdftotext` 단독 호출 시 `Syntax Error: Missing language pack for 'Adobe-Korea1' mapping` 에러 + 빈 출력.
   **반드시** `poppler-data` 패키지 설치 후 사용. 첫 실행 전 검증:
   ```bash
   pdftotext -f 1 -l 1 vendor/WIPI_V1_2_1_final_ST1_2_1_.pdf - | head
   # → "모바일 표준 플랫폼 규격" 같은 한국어가 보여야 OK
   ```

2. **JavaDoc HTML 비표준 구조**
   - `<a NAME="...">` 와 `<a name="...">` 대소문자 혼용. BeautifulSoup(lxml)은 자동 소문자화하므로 항상 소문자로 검색. grep 디버깅 시에는 `-i` 옵션 필수.
   - 일부 클래스에는 `method_detail`/`field_detail` 앵커 자체가 없음 (예: `org.kwis.msp.lcdui.Graphics`). 모든 앵커 존재를 가정하지 말 것.
   - `<dl>` 안에 비표준 nested `<dd>` 구조가 있을 수 있음 (위 "알려진 이슈" 참고).

3. **collapse_ws의 코드블록 보호**
   `scripts/convert_javadoc.py`의 `collapse_ws`는 fenced code block 안의 공백/개행을 그대로 보존하도록 작성되어 있음. 만약 새 정제 로직을 추가할 때 이 보호를 깨지 말 것.

4. **MkDocs `strict` 모드**
   CI에서는 `mkdocs build --strict`로 빌드 — broken link/missing nav target을 다 잡아냄. 변환기 출력에 javadoc 내부 cross-link (`Other.html#method`)가 남아있으면 strict가 fail함. 변환기는 이미 그런 링크를 plain code로 바꿔놓음. 새 콘텐츠 추가 시 주의.

5. **JavaDoc 변환기를 다시 실행하면 docs/java-api/ 가 덮어쓰여짐**
   수동 수정한 게 있으면 git에서 살려야 함.

---

## 권장 작업 순서 (Claude Code에서)

```
1. vendor/ 셋업 (PDF + JavaDoc clone)
2. apt install poppler-data  (한 번)
3. pip install -r requirements.txt
4. scripts/convert_javadoc.py 패치 → 재변환  (선택사항. 현재로도 95% 깔끔)
5. scripts/extract_pdf.py 작성 + 실행
6. mkdocs.yml + docs/index.md + 섹션별 index.md 작성
7. mkdocs serve로 로컬 확인하며 nav/링크 조정
8. scripts/build_llms_txt.py 작성
9. .github/workflows/deploy.yml 작성
10. README.md
11. 첫 push → 배포 확인
```

---

## TODO 체크리스트

- [x] 디렉토리 스캐폴드
- [x] JavaDoc 변환기 작성 + 실행 (135 classes)
- [x] PDF 한국어 추출 환경 검증
- [x] `.gitignore`, `requirements.txt`
- [x] **CLAUDE.md** (이 파일)
- [ ] JavaDoc 변환기 nested `<dd>` 패치 (선택)
- [ ] `scripts/extract_pdf.py` 작성
- [ ] PDF 전체 변환 실행
- [ ] `mkdocs.yml`
- [ ] `docs/index.md` + 섹션별 `index.md` 6개
- [ ] `scripts/build_llms_txt.py`
- [ ] `.github/workflows/deploy.yml`
- [ ] `README.md`
- [ ] 로컬 `mkdocs build --strict` 통과
- [ ] 첫 GitHub Pages 배포
