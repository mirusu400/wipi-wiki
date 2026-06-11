---
title: "C API"
---

WIPI-C 응용프로그래밍 인터페이스. 응용프로그램이 플랫폼 위에서 사용할 수 있는
C 언어 API 들을 정의합니다. 함수는 `MC_` 접두사를 갖습니다 (예: `MC_knlCalloc`,
`MC_grpDrawLine`).

| 절 | 항목 | 내용 |
|---|---|---|
| 5.1.1 | [커널](kernel) | 메모리 할당, 타이머, 프로세스 |
| 5.1.2 | [그래픽](graphics) | 2D 드로잉, 이미지 |
| 5.1.3 | [데이터베이스](database) | 응용프로그램 저장소 |
| 5.1.4 | [파일시스템](filesystem) | 파일/디렉토리 입출력 |
| 5.1.5 | [NETWORK](network) | 소켓, HTTP |
| 5.1.6 | [매체 처리기](media) | 미디어 클립 재생 |
| 5.1.7 | [SERIAL](serial) | 시리얼 통신 |
| 5.1.8 | [PHONE](phone) | 전화 발신 |
| 5.1.9 | [MISC](misc) | 메뉴, 알람 등 |
| 5.1.10 | [UTILITY](utility) | 문자열, 변환 |
| 5.1.11 | [UI Components](ui-components) | 위젯, 컴포넌트 |
| 5.1.12 | [표준 C 라이브러리](c-stdlib) | 지원 표준 C 함수 목록 |

## 5.1 C API

Clet 에서 사용할 수 있는 모든 API를 정의 한다. Clet은 다음의 함수를 모두 구현해야 한다. 플랫폼이 필요한 경우 각종 이벤트에 따라 해당 함수를 불러 준다. 

### handleCletEvent 

```c
void CletHandleEvent(int type, int param1, int param2) 
```
이벤트를 처리하는 함수이다. type에는 1 항에 정의된 이벤트가 올 수 있다. param1과 param2는 type의 값에 따라서 달라진다.

| 이벤트 (type) | 설명 | 사용되는 변수 |
|---|---|---|
| `MV_KEY_PRESS_EVENT` | 키가 눌렸을 때 발생되는 이벤트 | `param1` = 키 코드 값<br>`param2` = 0 |
| `MV_KEY_REPEAT_EVENT` | 키가 계속 눌려 있는 상태일 때 특정 시간마다 반복적으로 발생되는 이벤트 | `param1` = 키 코드 값<br>`param2` = 0 |
| `MV_KEY_RELEASE_EVENT` | 키가 떼어졌을 때 발생되는 이벤트 | `param1` = 키 코드 값<br>`param2` = 0 |
| `MV_CHILD_APP_START_EVENT` | 현재 응용 프로그램이 수행시킨 자식 프로그램이 시작되었음을 알려주는 이벤트 | `param1` = 생성된 자식 프로그램의 식별자<br>`param2` = 0 |
| `MV_CHILD_APP_DESTROY_EVENT` | 현재 응용 프로그램이 수행시킨 자식 프로그램이 종료되었음을 알려주는 이벤트 | `param1` = 생성된 자식 프로그램의 식별자<br>`param2` = 프로그램의 종료 코드 |
| `MV_USER_EVENT` | 사용자 이벤트 | `param1` = 사용자 지정 값<br>`param2` = 사용자 지정 값 |

