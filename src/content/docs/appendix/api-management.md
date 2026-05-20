---
title: "7.2. API 추가/삭제 기능 관련 API"
---

API 추가 및 삭제 기능은 선택적으로 제공할 수 있다. 이 기능을 제공하고자 하면, 다 음의 규격에따라 지원되어야 한다.

## 7.2.1. C API

### MC_knlMExecute

**프로토타입**

```c
M_Int32 MC_knlMExecute(char* symName, int parmCnt, ...)
```

**설명**

프로그램에 설치된 프로그램을 실행시킨다.

프로그램 내부에 존재하는 프로그램을 실행시키므로 같은 보안레벨을 가진다. 이 기능은 프로그램이 큰 경우, 여러 프로그램으로 나누어 부분(partial) 로딩함으로써 프로그램 로딩속도를 향상시키고 오버레이(overlay)형태로 플랫폼이 지원하는 힙보다 큰 프로그램을 실행시킬 수 있다. 그 외의 동작은 `MC_knlCExecute()`기능과 일치한다.

**매개 변수**

- `symName` - [in] 프로그램 개발시 개발자가 부여한 심볼릭(symbolic)이름
- `parmCnt` - [in] 이 매개변수뒤에 연속해서 전달할 매개변수 수

**반환 값**

성공

- 생성된 프로그램 ID

실패

- `M_E_ACCESS` - 만기일이 지났거나, 접근 권한이 없는 경우
- `M_E_NOMEMORY` – 메모리가 부족한 경우
- `M_E_INVALID` - 전달한 매개변수가 잘못된 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlLoad

**프로토타입**

```c
M_Int32 MC_knlLoad(char* execName, int parmCnt, ...)
```

**설명**

플랫폼에 설치된 동적로딩라이브러리를 로딩한다.

만기일이 지났거나 기타, 접근이 허락되지 않으면 에러값을 반환한다. 이 함수는 넌블라킹(non-blocking)함수이다. 프로그램이 라이브러리를 로딩하면 같은 메모리 공간에 존재하고 바로 라이브러리 함수를 불러 사용할 수 있다. 서로 다른 프로그램이 같은 라이브러리를 로딩하면 라이브러리는 한번만 로딩되고 공유된다. 라이 브러리는 명시적으로 해제될 수 없고, 해당 라이브러리를 사용하는 모든 프로그램 이 종료되면 자동으로 종료된다.

**매개 변수**

- `execName` - [in] 실행시킬 프로그램의 이름, `MC_knlGetExecNames()`에 의해 구해진다.

- `parmCnt` - [in] 이 매개변수뒤에 연속해서 전달할 매개변수 수

**반환 값**

성공

- 생성된 프로그램 ID

실패

- `M_E_ACCESS` - 만기일이 지났거나, 접근 권한이 없는 경우
- `M_E_NOMEMORY` – 메모리가 부족한 경우
- `M_E_INVALID` - 전달한 매개변수가 잘못된 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlMLoad

**프로토타입**

```c
M_Int32 MC_knlMLoad(char* symName, int parmCnt, ...)
```

**설명**

프로그램에 설치된 동적로딩라이브러리를 로딩한다.

프로그램 내부에 존재하는 라이브러리이므로 다른 프로그램과 공유될 수 없다. 이 기능은 프로그램이 큰 경우, 여러 라이브러리로 나누어 부분(partial) 로딩함으로 서 프로그램 로딩속도를 향상시키는데 사용할 수 있다. 그 외의 동작은 `MC_knlLoad()`기능과 일치한다.

**매개 변수**

- `symName` - [in] 프로그램 개발시 개발자가 부여한 심볼릭(symbolic)이름
- `parmCnt` - [in] 이 매개변수뒤에 연속해서 전달할 매개변수 수

**반환 값**

성공

- 생성된 프로그램 ID

실패

- `M_E_ACCESS` - 만기일이 지났거나, 접근 권한이 없는 경우
- `M_E_NOMEMORY` – 메모리가 부족한 경우
- `M_E_INVALID` - 전달한 매개변수가 잘못된 경우

**부작용**

없음

**참고 항목**

없음

## 7.2.2. 자바 API

### mExecute

```Java
public static int mExecute(java.lang.String symName, java.lang.String[] args)
```

프로그램에 설치된 프로그램을 실행시킵니다. 프로그램 내부에 존재하는 프로그램을 실행시키므로 같은 보안레벨을 가집니다. 이 기능은 프로그램이 큰 경우, 여러 프로그 램으로 나누어 부분(partial) 로딩함으로서 프로그램 로딩속도를 향상시키고 오버레이 (overlay)형태로 플랫폼이 지원하는 힙보다 큰 프로그램을 실행시킬 수 있읍니다. 그 외의 동작은 execute()기능과 일치합니다.

**Parameters**

- `symName` - 프로그램 개발시 개발자가 부여한 심볼릭(symbolic)이름
- `args` - `Main method()`로 전달될 매개변수

**Returns**

성공이면 살행된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

### load

```java
public static int load(java.lang.String execName, java.lang.String[] args)
```

플랫폼에 설치된 동적로딩라이브러리를 로딩합니다. 만기일이 지났거나 기타, 접근이 허락되지 않으면 에러값을 반환합니다. 이 함수는 넌블라킹(non-blocking)함수입니다.

프로그램이 라이브러리를 로딩하면 같은 메모리공간에 존재하고 바로 라이브러리함수 를 불러 사용할 수 있읍니다. 서로 다른 프로그램이 같은 라이브러리를 로딩하면 라이 브러리는 한번만 로딩되고 공유됩니다. 라이브러리는 명시적으로 해제될 수 없고, 해 당 라이브러리를 사용하는 모든 프로그램이 종료되면 자동으로 종료됩니다.

**Parameters**:

- `execName` - 실행시킬 프로그램의 이름, `getExecNames()`함수에 의해 구해진다.
- `args` - `Main method()`로 전달될 parameter

**Returns**

성공이면 load된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

**See Also**

`getExecNames(String prgName, String version, String vendor)`

### mLoad

```java
public static int mLoad(java.lang.String symName, java.lang.String[] args)
```

프로그램에 설치된 동적로딩라이브러리를 로딩합니다. 프로그램 내부에 존재하는 라이 브러리이므로 다른 프로그램과 공유될 수 없읍니다. 이 기능은 프로그램이 큰 경우, 여러 라이브러리로 나누어 부분(partial) 로딩함으로서 프로그램 로딩속도를 향상시키 는데 사용할 수 있읍니다. 그 외의 동작은 load()기능과 일치합니다.

**Parameters**

- `symName` - 프로그램 개발시 개발자가 부여한 심볼릭(symbolic)이름
- `args` - `Main method()`로 전달될 parameter

**Returns**

성공이면 load된 프로그램의 프로그램ID 반환, 실패하면 음수 반환
