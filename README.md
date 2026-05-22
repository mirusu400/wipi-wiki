# WIPI Wiki

WIPI 1.2.1 (한국 무선 인터넷 표준 플랫폼) 개발자용 위키.

원본 규격서 PDF 와 JavaDoc HTML 을 Markdown 으로 변환해 검색 가능한 정적 사이트로
배포합니다.

- **사이트**: <https://mirusu400.github.io/wipi-wiki/>
- **소스 (PDF)**: 무선 인터넷 표준화 포럼, *모바일 표준 플랫폼 규격 V1.2.1* (2003)
  - https://archive.org/details/wipi-c-emulator-1.2.2.0
- **소스 (JavaDoc HTML)**: WIPI 1.1.1 / CLDC 1.1 / MIDP 2.0 한국어 JavaDoc
  - WIPI 1.1.1: https://archive.org/details/aroma-wipi-emulator-v1.1.1.8
  - CIDC 1.1: http://jcp.org/aboutJava/communityprocess/final/jsr139/index.html
  - MIDP 2.0: http://jcp.org/aboutJava/communityprocess/final/jsr118/index.html


## 구조

```
wipi-wiki/
├── docs/                # 사이트 콘텐츠 (Markdown)
│   ├── index.md
│   ├── overview/        # 1~3장
│   ├── hal/             # 4장 - HAL
│   ├── c-api/           # 5.1장 - WIPI-C
│   ├── java-api/        # 5.2장 - WIPI-Java (JavaDoc 기반, 135 classes)
│   └── appendix/        # 6, 7장
├── scripts/
│   ├── convert_javadoc.py   # JavaDoc HTML → Markdown
│   ├── extract_pdf.py       # PDF → 섹션별 Markdown
│   └── build_llms_txt.py    # llms.txt / llms-full.txt 생성
├── mkdocs.yml
├── requirements.txt
└── .github/workflows/deploy.yml
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

## 배포

`main` 브랜치에 push 하면 `.github/workflows/deploy.yml` 이 자동으로:

1. `mkdocs build --strict`
2. `scripts/build_llms_txt.py` 로 `site/llms.txt`, `site/llms-full.txt` 생성
3. GitHub Pages 로 배포

GitHub repo 의 *Settings → Pages → Build and deployment → Source* 를
**GitHub Actions** 로 설정해야 합니다.

## 기여

각 페이지 우측 상단의 연필 아이콘으로 GitHub 편집 화면으로 이동할 수 있습니다.

## 라이선스

원본 규격서의 저작권은 무선 인터넷 표준화 포럼에 있습니다. 본 저장소는 학술적 ·
기술 문서 참조 목적의 재구성이며, 원본을 인용할 때는 출처를 명시해 주세요.
