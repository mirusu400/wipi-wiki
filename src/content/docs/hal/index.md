---
title: "HAL 규격"
---

**HAL (Handset Adaptation Layer)** 은 단말기 기본 소프트웨어 위에 모바일 표준 플랫폼이
요구하는 함수들을 정의한 추상화 계층입니다. 모든 함수는 `MH_` 접두사를 갖습니다.

| 절 | 항목 | 내용 |
|---|---|---|
| 4.1 | [Type Definition](types/) | `M_Int32` 등 기본 타입 정의 |
| 4.2 | [플랫폼이 제공하는 API](platform-api/) | 플랫폼 → 단말 SW 호출 |
| 4.3 | [System](system/) | 디버그 출력, 시스템 정보 |
| 4.4 | [CALL](call/) | 전화 발신 / 종료 |
| 4.5 | [HandSet Device](handset/) | 진동, LED, 배터리 |
| 4.6 | [네트워크](network/) | TCP/IP 소켓 |
| 4.7 | [Serial](serial/) | 시리얼 통신 |
| 4.8 | [MEDIA](media/) | 사운드, 비디오 |
| 4.9 | [TIME](time/) | 시각, 타이머 |
| 4.10 | [UTILITY](utility/) | 문자셋 변환 |
| 4.11 | [FILE](file/) | 파일 입출력 |
| 4.12 | [InputMethod](input-method/) | 한글 입력기 |
| 4.13 | [Font](font/) | 폰트 렌더링 |
| 4.14 | [Frame Buffer](frame-buffer/) | 프레임 버퍼 |
| 4.15 | [Virtual Key](virtual-key/) | 가상 키 매핑 |
