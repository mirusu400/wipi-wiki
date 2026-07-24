---
title: WIPI 2.2.0
description: WIPI 2.2.0 모바일 표준 플랫폼 규격 위키
---

**WIPI 2.2.0** (TTAK.KO-06.0036/R6, 2008년 12월)은 모바일 표준 플랫폼 규격의 최종 개정판입니다.

## 규격 구성

| 편 | 내용 | 설명 |
|---|---|---|
| [제1편](/wipi-wiki/v22/overview/introduction/) | 규격 구조 및 기능 | 서론, 개념적 구조, 주요 기능 규격, 참조문헌 |
| [제2편](/wipi-wiki/v22/hal/types/) | HAL API | 하드웨어 추상화 계층 (18개 섹션) |
| [제3편](/wipi-wiki/v22/c-api/kernel/) | C API | 필수 C API (16개 섹션 + 표준 C 라이브러리) |
| [제4편](/wipi-wiki/v22/java-api/kernel/) | Java API | 필수 Java API (MSF/MSP 기반) |
| [제5편](/wipi-wiki/v22/optional/dynamic-api/) | 선택 규격 | 동적 API, VGI |
| [부속서](/wipi-wiki/v22/appendix/api-interop/) | 부속서 | API 혼용 기준, 보안 정책, 에러 코드, 예제, wCard |

## v1.2.1 대비 주요 변경사항

- **Generic I/O**: HAL/C API/Java API에 Generic I/O 규격 추가
- **단말 리소스**: 단말 리소스 관리 API 추가
- **SMS**: HAL/C API/Java API에 SMS 지원 추가
- **보안통신**: C API에 보안통신 규격 추가
- **부가 장치 제어**: C API/Java API에 부가 장치 제어 추가
- **수학 연산**: C API에 수학 연산 함수 추가
- **VGI**: 선택 규격으로 VGI (Vector Graphics Interface) 추가
- **wCard**: 부속서에 wCard 규격 추가
