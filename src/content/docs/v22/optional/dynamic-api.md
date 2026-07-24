---
title: "1. 동적 API 분할 추가 및 실행"
---

동적 API의 분할 추가 및 실행기능은 선택적으로 제공할 수 있다. 이 기능을 제공하 고자 하면, 다음의 규격에 따라 지원되어야 한다.

## 1.1. C API

### MC_knlGetExecMName

**프로토타입**

```c
M_Int32 MC_knlGetExecMName(M_Char* execName, M_Char* moduleName,
M_Char* rtnBuf, M_Int32 rtnBufSize)
```

**설명**

프로그램에 설치된 프로그램 실행을 위한 이름을 구한다. 구해진 이름은 `MC_knlMExecute()`, `MC_knlMLoad`()의 패러미터로 사용된다.

**매개 변수**

- `execName` - [in] `MC_knlGetExecNames`()에서 구해진 이름
- `moduleName` - [in] jar안에 포함되어 실행시킬 모듈(module)이름
- `rtnBuf` - [out] null로 끝나는 문자열
- `rtnBufSize` - [in] rtnBuf의 크기

**반환 값**

성공

실패

- `M_E_SHORTBUF` - buf가 작아 해당되는 이름을 모두 반환하지 못하는 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlMExecute

**프로토타입**

```c
M_Int32 MC_knlMExecute(char* symName, int parmCnt, ...)
```

**설명**

프로그램에 설치된 프로그램을 실행시킨다. 프로그램 내부에 존재하는 프로그램을 실행시키므로 같은 보안레벨을 가진다. 이 기 능은 프로그램이 큰 경우, 여러 프로그램으로 나누어 부분(partial) 로딩함으로써 프로그램 로딩속도를 향상시키고 오버레이(overlay)형태로 플랫폼이 지원하는 힙보 다 큰 프로그램을 실행시킬 수 있다. 그 외의 동작은 `MC_knlExecute`()기능과 일치한 다.

**매개 변수**

- `symName` - [in] 프로그램 개발 시 개발자가 부여한 심볼릭(symbolic) 이름
- `parmCnt` - [in] 이 매개변수 뒤에 연속해서 전달할 매개변수 수

**반환 값**

성공

생성된 프로그램 ID
실패

- `M_E_ACCESS` - 만기일이 지났거나, 접근 권한이 없는 경우
- `M_E_NOMEMORY` - 메모리가 부족한 경우
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

프로그램에 설치된 동적 로딩 라이브러리를 로딩한다. 프로그램 내부에 존재하는 라이브러리이므로 다른 프로그램과 공유될 수 없다. 이 기능은 프로그램이 큰 경우, 여러 라이브러리로 나누어 부분(partial) 로딩함으로써 프로그램 로딩속도를 향상시키는데 사용할 수 있다. 그 외의 동작은 `MC_knlLoad`()기 능과 일치한다.

**매개 변수**

- `symName` - [in] 프로그램 개발 시 개발자가 부여한 심볼릭(symbolic) 이름
- `parmCnt` - [in] 이 매개변수 뒤에 연속해서 전달할 매개변수 수

**반환 값**

성공

로딩된 라이브러리 ID
실패

- `M_E_ACCESS` - 만기일이 지났거나, 접근 권한이 없는 경우
- `M_E_NOMEMORY` - 메모리가 부족한 경우
- `M_E_INVALID` - 전달한 매개변수가 잘못된 경우

**부작용**

없음

**참고 항목**

없음

## 1.2. Java API


#### getExecMName

public static String getExecMName(java.lang.String execName, java.lang.String moduleName) 프로그램에 설치된 프로그램 실행을 위한 이름을 구한다. 구해진 이름은 mExecute(), mLoad()의 패러미터로 사용된다. 예) String[] rtn; String mName; rtn = getExecNames(“mygame”, null, null); mName = getExecMName(rtn[0], “stage1.bin”); mExecute(mName, null); (*C에제 참조)

**매개 변수**

- `execName` - getExecNames()에서 구해진 이름
- `moduleName` - jar안에 포함되어 실행시킬 모듈(module)이름

**반환 값**

성공이면 플랫폼에서 사용하는 모듈(module)이름 반환, 실패하면 null 반환 mExecute public static int mExecute(java.lang.String symName, java.lang.String[] args) 프로그램에 설치된 프로그램을 실행시킨다. 프로그램 내부에 존재하는 프로그램을 실행시키므로 같은 보안레벨을 가진다. 이 기능은 프로그램이 큰 경우, 여러 프로그 램으로 나누어 부분(partial) 로딩함으로써 프로그램 로딩속도를 향상시키고 오버레 이(overlay)형태로 플랫폼이 지원하는 힙보다 큰 프로그램을 실행시킬 수 있다. 그 외의 동작은 execute()기능과 일치한다.

**매개 변수**

- `symName` - 프로그램 개발 시 개발자가 부여한 심볼릭(symbolic)이름
- `args` - Main method()로 전달될 매개변수

**반환 값**

성공이면 실행된 프로그램의 프로그램ID 반환, 실패하면 음수 반환 mLoad public static int mLoad(java.lang.String symName, java.lang.String[] args) 프로그램에 설치된 동적 로딩 라이브러리를 로딩한다. 프로그램 내부에 존재하는 라 이브러리이므로 다른 프로그램과 공유될 수 없다. 이 기능은 프로그램이 큰 경우, 여러 라이브러리로 나누어 부분(partial) 로딩함으로써 프로그램 로딩속도를 향상시 키는데 사용한다. 그 외의 동작은 load()기능과 일치한다.

**매개 변수**

- `symName` - 프로그램 개발 시 개발자가 부여한 심볼릭(symbolic)이름
- `args` - Main method()로 전달될 parameter

**반환 값**

성공이면 load된 프로그램의 프로그램ID 반환, 실패하면 음수 반환
