---
title: "WIPI Wiki"
---

**WIPI 1.2.1** (Wireless Internet Platform for Interoperability) — 2000년대 한국의 피처폰
모바일 표준 플랫폼 규격을 검색 가능한 형태로 정리한 개발자용 레퍼런스입니다.

원본 규격은 무선 인터넷 표준화 포럼 모바일 플랫폼 분과가 작성한
**모바일 표준 플랫폼 규격 V1.2.1** PDF (2003) 와 동시기 배포된 JavaDoc HTML을 기준으로 합니다.

---

## 무엇이 정리되어 있나

| 영역 | 내용 |
|---|---|
| [개요](overview/) | 플랫폼의 목적·범위, 개념적 구조, 단말기 권장 사양 |
| [HAL 규격](hal/) | Handset Adaptation Layer — 단말기 추상화 계층 함수 정의 |
| [C API](c-api/) | WIPI-C 응용프로그래밍 인터페이스 (커널, 그래픽, 네트워크, DB, UI 등) |
| [Java API](java-api/) | WIPI Java (MSF / MSP) 패키지·클래스 레퍼런스 (135 classes) |
| [부속서](appendix/) | EUC-KR 확장, 보안 API, 미디어 확장, 참조 문헌 |

---

## 빠른 진입점

- `MC_*` 로 시작하는 함수가 궁금하다 → [C API](c-api/)
- `MH_*` 로 시작하는 함수가 궁금하다 → [HAL 규격](hal/)
- `org.kwis.*` 클래스가 궁금하다 → [Java API](java-api/)
- 전체 규격서 PDF가 필요하다 → 원본은 무선 인터넷 표준화 포럼 자료를 참조

---

## LLM 친화 진입점

이 사이트는 LLM (Claude, ChatGPT 등) 이 직접 참조하기 좋도록 다음 파일을 함께 배포합니다.

- [`/llms.txt`](llms.txt) — 페이지 인덱스 (요약 + 절대 URL)
- [`/llms-full.txt`](llms-full.txt) — 전체 콘텐츠를 한 파일로 concat

[llmstxt.org](https://llmstxt.org/) 표준을 따릅니다.

---

## 기여 / 이슈

각 페이지 우측 상단의 연필 아이콘으로 GitHub 편집으로 바로 이동할 수 있습니다.
저장소: <https://github.com/mirusu400/wipi-wiki>
