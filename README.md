# WIPI Wiki

WIPI 1.2.1 (한국 무선 인터넷 표준 플랫폼) 개발자용 위키.

원본 규격서 PDF 와 JavaDoc HTML 을 Markdown 으로 변환해 검색 가능한 정적 사이트로
배포합니다.

- **사이트**: <https://mirusu400.github.io/wipi-wiki/>
- **소스 (PDF)**: 무선 인터넷 표준화 포럼, *모바일 표준 플랫폼 규격 V1.2.1* (2003)
- **소스 (JavaDoc HTML)**: WIPI 1.1.1 / CLDC 1.1 / MIDP 2.0 한국어 JavaDoc — 원본은
  각 표준 규격에 동봉되어 배포된 자료. 본 레포에는 변환 결과 Markdown 만 포함

## 구조

```
wipi-wiki/
├── docs/                # 사이트 콘텐츠 (Markdown)
│   ├── index.md
│   ├── overview/        # 1~3장
│   ├── hal/             # 4장 — HAL
│   ├── c-api/           # 5.1장 — WIPI-C
│   ├── java-api/        # 5.2장 — WIPI-Java (JavaDoc 기반, 135 classes)
│   └── appendix/        # 6, 7장
├── scripts/
│   ├── convert_javadoc.py   # JavaDoc HTML → Markdown
│   ├── extract_pdf.py       # PDF → 섹션별 Markdown
│   └── build_llms_txt.py    # llms.txt / llms-full.txt 생성
├── mkdocs.yml
├── requirements.txt
├── .github/workflows/deploy.yml
└── vendor/              # gitignored — 원본 PDF / JavaDoc clone
```

## 로컬 빌드

```bash
# 1) Python 의존성
pip install -r requirements.txt

# 2) 개발 서버 (http://127.0.0.1:8000)
mkdocs serve

# 3) 정적 빌드 + strict 모드로 깨진 링크 점검
mkdocs build --strict
```

## 원본 소스 재준비

기본적으로 `docs/` 의 변환 결과만 커밋되어 있습니다. 변환을 다시 돌리려면 원본을
받아야 합니다.

```bash
# PDF: vendor/WIPI V1.2.1_final(ST1.2.1).pdf 로 직접 배치

# JavaDoc HTML: 표준 규격에 동봉된 원본 JavaDoc 디렉토리를 아래 경로에 배치
#   vendor/wipi_api_1_1_1/        (WIPI 1.1.1 Java API)
#   vendor/cldc-1_1-fr-spec-ko/   (CLDC 1.1 — Appendix2-javadocs.zip 풀어둘 것)
#   vendor/midpng-javadoc-final/  (MIDP 2.0)
```

## 변환 스크립트

```bash
# JavaDoc → docs/java-api/ (WIPI), docs/cldc/java-api/, docs/midp/java-api/
python3 scripts/convert_javadoc.py vendor/wipi_api_1_1_1            docs/java-api
python3 scripts/convert_javadoc.py vendor/cldc-1_1-fr-spec-ko/javadocs docs/cldc/java-api
python3 scripts/convert_javadoc.py vendor/midpng-javadoc-final/javadoc docs/midp/java-api

# PDF → docs/{overview,hal,c-api,appendix}/
python3 scripts/extract_pdf.py \
    "vendor/WIPI V1.2.1_final(ST1.2.1).pdf" \
    docs/

# llms.txt (mkdocs build 후 site/ 에 생성)
mkdocs build
python3 scripts/build_llms_txt.py site
```

`extract_pdf.py` 는 `pdfplumber` (내부에 pdfminer.six 포함) 를 사용하기 때문에
poppler-data 같은 시스템 패키지 설치가 필요하지 않습니다.

## 배포

`main` 브랜치에 push 하면 `.github/workflows/deploy.yml` 이 자동으로:

1. `mkdocs build --strict`
2. `scripts/build_llms_txt.py` 로 `site/llms.txt`, `site/llms-full.txt` 생성
3. GitHub Pages 로 배포

GitHub repo 의 *Settings → Pages → Build and deployment → Source* 를
**GitHub Actions** 로 설정해야 합니다.

## 기여

각 페이지 우측 상단의 연필 아이콘으로 GitHub 편집 화면으로 이동할 수 있습니다.
변환 스크립트 버그 수정도 환영합니다 (`CLAUDE.md` 의 "알려진 마이너 이슈" 참고).

## 라이선스

원본 규격서의 저작권은 무선 인터넷 표준화 포럼에 있습니다. 본 저장소는 학술적 ·
기술 문서 참조 목적의 재구성이며, 원본을 인용할 때는 출처를 명시해 주세요.
