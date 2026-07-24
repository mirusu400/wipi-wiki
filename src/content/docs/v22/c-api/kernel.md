---
title: "2.1. 커널"
---

#### 커널 인터페이스 API

동적 메모리 할당/해제, 프로그램의 생성/종료, 타이머, 시스템 정보, 공유 메모리에 관한 API 를 제공한다.

#### 메모리 관리

메모리의 효율적인 관리를 위하여 메모리의 고정(static)할당과, 동적(dynamic)할당을 지원한다. 또한 동적으로 할당된 메모리는 컴팩션(compaction)을 지원할 수 있다. 고 정 할당되는 메모리는 프로그램 로딩 시 메모리에 할당되며, 프로그램 수행 중에는 해제될 수 없고, 프로그램 종료 시에 자동으로 해제된다. 동적 할당되는 메모리는 프 로그램 수행 중에 `MC_knlAlloc()` 또는 `MC_knlCalloc()` API에 의해 할당되며, 수행 중 에 `MC_knlFree()` API를 통해 해제할 수 있다. 프로그램 종료 시 해제되지 않은 메모 리는 플랫폼이 자동으로 해제한다. 컴팩션(compaction)은 동적 메모리 할당 시 할당 할 미사용 메모리가 없으면 자동으로 일어난다. 동적으로 할당되는 메모리는 메모리 식별자(ID)이며 사용자는 컴팩션(compaction)이 일어날 수 있는 곳에서는 메모리식별 자에서 포인터를 다시 구해와서 사용해야 한다. 컴팩션(compaction)은 동적 메모리 할당 시 할당할 미사용 메모리가 없는 경우와, `MC_knlGetFreeMemory()` API를 부를 때만 일어난다. 이외의 API에서 컴팩션(compaction)이 일어나는 경우는 해당 API내 부에서 메모리를 동적으로 할당하는 경우이다. 내부적으로 메모리를 동적으로 할당 하는 API는 각 API의 부작용 항목을 참조한다. 플랫폼 API중에는 입력으로 간접 (indirect)버퍼를 요구하는 API들이 있다. 이런 API들은 주로 내부적으로 동적할당을 사용하여 컴팩션이 일어날 수 있는 API들이다. 간접버퍼(메모리식별자와 같음)는 동적 할당된 버퍼와, `DECLARE_INDIRECTBUF`()로 선언된 고정 할당된 버퍼를 말한다. `DECLARE_INDIRECTBUF`()로 선언된 버퍼는 동 적 할당된 버퍼와 같은 구조를 가지지만 실제로는 고정 할당된다.

```c
typedef struct _IndirectBuf {
INDIRECT_BUF_HEAD;
char buf[1024]
} IndirectBuf;
char staticBuf[256]; // 고정(static)할당 buffer
char imageBuf[1024];
```

`DECLARE_INDIRECTBUF`(IndirectBuf, idBuf);

```c
void startClet() {
M_Byte* dynamicBuf;
M_Uint32 mBufID;
M_Int32 freeMemorySize;
strcpy(staticBuf, "this is testing...\n");
MC_knlPrintk("%s", staticBuf);
mBufID = MC_knlCalloc(256); // mBufID는 메모리식별자
dynamicBuf = MC_GETDPTR(mBufID); // 메모리식별자에서 포인터를 구해옴
strcpy(dynamicBuf, "this is testing...\n");
MC_knlPrintk("%s", dynamicBuf);
freeMemorySize = MC_knlGetFreeMemory();// 컴팩션(compaction)이 일어남
dynamicBuf = MC_GETDPTR(mBufID);
// 컴팩션(compaction)이 일어 날 수 있으므로
// 메모리식별자에서 다시 포인터를 구해옴
MC_knlPrintk("%s", dynamicBuf);
MC_knlFree(mBufID);
...
if ( (rID = MC_knlGetResourceID("test.gif", &rSize)) < 0 ) {
MC_knlPrintk(resource not found\n");
...
}
mBufID = MC_knlCalloc(rSize); // 동적할당을 이용한 리소스 얻기
MC_knlGetResource(rID, mBufID, rSize);
dynamicBuf = MC_GETDPTR(mBufID);
memcpy(imageBuf, dynamicBuf, rSize);
...
MC_knlGetResource(rID, &idBuf, rSize);
// DECLARE_INDIRECTBUF()로 할당된 간접버퍼를 통한 리소스 얻기
memcpy(imageBuf, idBuf.buf, rSize);
...
}
```

#### 프로그램 관리

다중 프로그램 수행을 지원한다. 각 프로그램은 독립적인 메모리/실행 공간을 가진다. 플랫폼은 여러 개의 프로그램을 동시에 실행할 수 있고 가능한 한 자신 이외의 프로 그램 자원을 접근(access)할 수 없게 해야 한다. 프로그램간의 통신은 event와 공유 메모리를 사용한다. 프로그램은 자기자신을 생성시킨 프로그램과 부모/자식간의 관계 를 가진다. 응용 프로그램 관리자는 최상위 부모가 되고, 여기서부터 자식 프로그램 이 수행된다. 자식 프로그램은 부모 프로그램을 강제로 종료시킬 수 없고, 부모는 자 식을 강제로 종료시킬 수 있다. 또한 부모 프로그램이 종료되면 자식프로그램들은 자동으로 종료된다. 플랫폼은 오버레이(overlay)기능을 제공할 수 있다.. 프로그램 개발자는 플랫폼에서 제공하는 heap보다 큰 프로그램을 실행시킬 수 있다. 오버레이 기능을 이용하기 위 하여 플랫폼 개발환경에서는 프로그램 개발자가 큰 프로그램을 여러 개의 작은 프로 그램으로 나누어 컴파일하고, 이것을 묶어서 플랫폼에 하나의 프로그램으로 설치할 수 있는 환경을 제공해야 한다. 또한 프로그램 개발자가 큰 프로그램을 여러 작은 프로그램으로 나눌 때, 작은 프로그램마다 심볼릭(symbolic)이름을 정의 할 수 있어 야 한다. 플랫폼은 오버레이방식으로 작은 프로그램을 로딩할 때, 프로그램 식별자로 이 심볼릭(symbolic)이름을 사용한다. 동적 로딩 라이브러리를 지원한다. 플랫폼은 플랫폼에 추가할 API를 라이브러리로 만들고, 여러 프로그램이 공유하여 사용할 수 있는 기능을 제공한다.

#### 공유메모리

프로그램간에 자료공유는 공유메모리를 이용한다. 공유메모리는 공유 메모리 이름을 키로 하여 복수개를 생성할 수 있다. 공유메모리는 사용하는 모든 프로그램이 종료 되면 자동으로 해제된다.

#### 기타

여러 개의 타이머를 지원한다. 타이머를 설정한 프로그램이 타이머가 해제되기 전에 종료되면 해제되지 않은 타이머도 자동으로 해제된다. 단말기 번호, ESN등 각종 시 스템정보를 읽어오는 API를 제공한다.

#### 버퍼할당

언급이 없을 경우, 플랫폼의 모든 API는 버퍼가 필요할 때 호출자(caller)가 버퍼를 할당하여 매개변수로 전달한다.. 호출 받는 API안에서 메모리버퍼가 할당되어 반환 할 경우에는 각API에 명확히 언급된다.

#### MC_knlGetSystemProperty 함수 Command 추가

Command 비고 “IODEVICES” 지원하는 I/O device의 문자열, 여러 개일 경우 “,”로 구분함 지원 되는 device가 없으면 M_E_NOTSUP를 반환 문자열 device “IrDA” IrDA 장치 “Camera” 카메라 장치 “1ChipCard” 1Chip용 IC 카드 장치 “Bluetooth” 블루투스 장치 디바이스가 미리 정의된 문자열을 지원할 시에는 정의된 문자열을 반환하고, 그렇지 않을 경우에는 벤더나 이통사에서 정의하여 확장 한다. “DEFAULTVOLUM 단말기가 제공하는 시스템 볼륨 문자열 E” 단말기가 제공하는 시스템 볼륨 카테고리 문자열, 여러 개일 경우 “,” 로 구분함. 지원되는 시스템 볼륨 카테고리가 존재하지 않으면 `M_E_NOTSUP` 에러값을 반환함 문자열 기능 GENERAL 일반적인 application에서 사용되는 특성을 갖는 다. VOICE 음성의 재생/녹음 특성을 갖는다. RING 착신 벨 특성을 갖는다. 예를 들어 현재 착신 벨 이 진동으로 되어 있다면, play 시 소리가 나지 않 고 진동이 발생한다. 별도의 멜로디용 speaker가 따로 있다면 이를 통해 소리가 발생한다. 즉, 단말 기에 전화가 왔을 때의 특성 그대로 행동 한다. KEY 키 톤의 특성을 갖는다. MESSAGE SMS message 도착 경고음 특성을 갖는다. ALARM 알람 경고음 특성을 갖는다. ALERT No service, low battery 각종 경고음 특성을 갖는 다. MMEDIA TCM2, AOD, VOD 재생시 사용되는 특성을 갖는 다. GAME 게임 시 재생되는 특성을 갖는다. OEM 위에서 정의되지 않은 음량에 대한 설정 시 사용 한다. “REGISTRABLEST `MC_termResRegister()` 함수를 통하여 단말의 IDLE 상태에 설정이 ATUS_IDLE” 허용된 단말 리소스 그룹 목록을 반환함 여러 개일 경우 “,”로 구 분함 “REGISTRABLEST `MC_termResRegister()` 함수를 통하여 단말의 INCOMING 상태에 ATUS_INCOMING” 설정이 허용된 단말 리소스 그룹 목록을 반환함 여러 개일 경우 “,”로 구분함 “REGISTRABLEST `MC_termResRegister()` 함수를 통하여 단말의 POWERON 상태에 ATUS_POWERON” 설정이 허용된 단말 리소스 그룹 목록을 반환함 여러 개일 경우 “,”로 구분함 “REGISTRABLEST `MC_termResRegister()` 함수를 통하여 단말의 POWEROFF 상태에 ATUS_POWEROFF 설정이 허용된 단말 리소스 그룹 목록을 반환함 여러 개일 경우 ” “,”로 구분함 “REGISTRABLEST `MC_termResRegister()` 함수를 통하여 단말의 BROWSERON 상태 ATUS_BROWSERO 에 설정이 허용된 단말 리소스 그룹 목록을 반환함 여러 개일 경 N” 우 “,”로 구분함 “REGISTRABLEST `MC_termResRegister()` 함수를 통하여 단말의 BROWSEROFF 상태 ATUS_BROWSERO 에 설정이 허용된 단말 리소스 그룹 목록을 반환함 여러 개일 경 FF” 우 “,”로 구분함 “SUPPORTGLOCK 단말 리소스 그룹 중 그룹 Lock을 지원하는 리소스 그룹의 목록을 ” 반환함. 여러 개일 경우 “,”로 구분함 “SUPPORTPLOCK 단말 리소스 그룹 중 개별 리소스 Lock을 지원하는 리소스 그룹의 ” 목록을 반환함. 여러 개일 경우 “,”로 구분함 "NOTDELGROUP" 리소스의 삭제를 허용하지 않는 단말리소스 그룹 목록을 반환함. 여러 개 일 경우 ","로 구분함

### MC_PRGTYPE_JAVAAPP

**프로토타입**

```c
#define MC_PRGTYPE_JAVAAPP
```

**설명**

자바 애플리케이션. 1로 정의 되어있다.

### MC_PRGTYPE_CAPP

**프로토타입**

```c
#define MC_PRGTYPE_CAPP
```

**설명**

C 애플리케이션. 2로 정의 되어있다.

### MC_PRGTYPE_CDLL

**프로토타입**

```c
#define MC_PRGTYPE_CDLL
```

**설명**

C 동적 로딩 라이브러리, 3로 정의 되어있다.

### MC_PRGTYPE_JAVADLL

**프로토타입**

```c
#define MC_PRGTYPE_JAVADLL
```

**설명**

자바 동적 로딩 라이브러리, 4로 정의 되어있다.

### MC_PRGTYPE_JAVASYSDLL

**프로토타입**

```c
#define MC_PRGTYPE_JAVASYSDLL
```

**설명**

자바 시스템 라이브러리, 5로 정의 되어있다.

### MC_DIR_SYS_READ_REQ_MASK

**프로토타입**

```c
#define MC_DIR_SYS_READ_REQ_MASK
```

**설명**

system directory read가능. 0x01로 정의 되어있다.

### MC_DIR_SYS_WRITE_REQ_MASK

**프로토타입**

```c
#define MC_DIR_SYS_WRITE_REQ_MASK
```

**설명**

system directory write가능. 0x02로 정의 되어있다.

### MC_DIR_SHARED_READ_REQ_MASK

**프로토타입**

```c
#define MC_DIR_SHARED_READ_REQ_MASK
```

**설명**

shared directory read가능. 0x04로 정의 되어있다.

### MC_DIR_SHARED_WRITE_REQ_MASK

**프로토타입**

```c
#define MC_DIR_SHARED_WRITE_REQ_MASK
```

**설명**

shared directory write가능. 0x08로 정의 되어있다.

### MC_NETWORK_ACCESS_REQ_MASK

**프로토타입**

```c
#define MC_NETWORK_ACCESS_REQ_MASK
```

**설명**

network API사용 가능. 0x10으로 정의 되어있다.

### MC_SERIAL_ACCESS_REQ_MASK

**프로토타입**

```c
#define MC_SERIAL_ACCESS_REQ_MASK
```

**설명**

serial API사용 가능. 0x20으로 정의 되어있다.

### MC_SYSTEM1_ACCESS_REQ_MASK

**프로토타입**

```c
#define MC_SYSTEM1_ACCESS_REQ_MASK
```

**설명**

system group1에 속한 API사용가능(system group1에 속할 API들은 각 이통사가 정 의) . 0x40으로 정의 되어있다.

### MC_SYSTEM2_ACCESS_REQ_MASK

**프로토타입**

```c
#define MC_SYSTEM2_ACCESS_REQ_MASK
```

**설명**

system group2에 속한 API사용가능(system group2에 속할 API들은 각 이통사가 정 의) . 0x80으로 정의 되어있다.

### MC_GETDPTR

**프로토타입**

```c
#define MC_GETDPTR(mID)
```

**설명**

메모리식별자에서 포인터를 구한다. `MC_knlAlloc()` 또는 `MC_knlCalloc`()에서 할당한 메모리식별자에서 실제로 사용할 포 인터를 구한다.

**매개 변수**

- `mID` - 메모리식별자

**반환 값**

포인터

### DECLARE_INDIRECTBUF

**프로토타입**

```c
#define DECLARE_INDIRECTBUF(typeName, var)
```

**설명**

고정할당으로 간접버퍼(메모리식별자)를 할당한다. 버퍼를 할당하기 위하여는 먼저, 할당할 버퍼의 타입을 아래와 같은 형태로 정의 한 다.

```c
typedef struct type_name {
INDIRECT_BUF_HEAD; // 간접버퍼할당을 위해 플랫폼에서 제공하는 매크로
char buf[1024]; // 사용자가 원하는 크기의 버퍼 설정
};
```

**매개 변수**

- `typeName` - 사용자가 선언한 타입선언의 이름
- `var` - 간접버퍼로 선언할 변수명

**반환 값**

포인터

**참고 항목**

사용법은 kernel overview의 예제 참조

### MCTimer

**프로토타입**

```c
typedef struct _MTimer MCTimer
```

**설명**

타이머 설정에 사용되는 구조체형 선언

**참고 항목**

`MC_knlDefTimer`, `MC_knlSetTimer`, `MC_knlUnsetTimer`

### TIMERCB

**프로토타입**

```c
typedef void (*TIMERCB)(MCTimer *tm, void* parm)
```

**설명**

`MC_knlDefTimer`()에 등록하는 콜백함수이다. 설정한 타이머가 만료되면 불린다.

**매개 변수**

- `tm` - 타이머 설정 시 타이머 구조체 포인터
- `parm` - 타이머 설정 시 전달한 매개변수

**참고 항목**

`MC_knlDefTimer`

### MC_knlPrintk

**프로토타입**

```c
M_Int32 MC_knlPrintk(M_Char* format, ...)
```

**설명**

format string을 stdout으로 출력한다. “ISO/IEC 9899:1999(E) -- Programming Languages – C” 의 printf 규격을 따른다.

**부작용**

없음

**참고 항목**

없음

### MC_knlSprintk

**프로토타입**

```c
M_Int32 MC_knlSprintk(M_Char* buf, M_Char* format, ...)
```

**설명**

format string을 buf로 출력한다. “ISO/IEC 9899:1999(E) -- Programming Languages – C” 의 sprintf 규격을 따른다.

**부작용**

없음

**참고 항목**

없음

### MC_knlGetExecNames

**프로토타입**

```c
M_Int32 MC_knlGetExecNames(M_Char* prgName, M_Char* version,
M_Char* vendor, M_Char* buf, M_Int32 bufSize)
```

**설명**

플랫폼에 설치된 어플리케이션 중 prgName(프로그램이름), version, vendor와 일치하 는 어플리케이션 식별이름을 반환한다. 매개변수가 NULL인 경우에는 아무것이나 일 치한다는 뜻 이다. 예를 들어 prgName, version, vendor가 모두 NULL인경 우, 플랫폼 에 설치된 모든 프로그램의 이름을 반환한다. 반환되는 이름은 null로 끝나는 문자열 의 리스트이다. 예로서 두 개의 일치하는 프로그램이 있을 경우 예)"/1/1.jar,3\0/2/2.jar,2\0" 와 같이 buf에 저장되어 반환될 수 있다.

**매개 변수**

- `prgName` - [in] 프로그램 이름
- `version` - [in] 버전
- `vendor` - [in] 제작사
- `buf` - [out] null로 끝나는 문자열의 list
- `bufSize` - [in] buf의 크기

**반환 값**

성공

해당되는 프로그램의 count
실패

- `M_E_SHORTBUF` - buf가 작아 해당되는 이름을 모두 반환하지 못하는 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlExecute

**프로토타입**

```c
M_Int32 MC_knlExecute(M_Char* execName, M_Int32 parmCnt, ...)
```

**설명**

플랫폼에 설치된 java/C/C++프로그램을 실행시킨다 만기일이 지났거나 기타, 접근이 허락되지 않으면 에러값을 반환한다. 이 함수는 넌 블라킹(non-blocking)함수이다. 프로그램이 죽게 되면, MV_CHILD_APP_DESTROY_EVENT를 응용프로그램 관리자와 죽는 프로그램의 부 모 프로그램에게 보내게 된다. 실행된 프로그램은 다른 프로그램과 서로 다른 메모 리 공간에 존재하게 되고, event와 공유메모리를 통하여만 데이타를 주고 받을 수 있 다. 매개변수 전달: 프로그램은 자신이 실행시킨 자식프로그램에게 필요한 정보를 전달 할 수 있다. 전달할 매개변수는 문자열이어야만 한다. C 부모 프로그램 ... `MC_knlExecute`("execName", 4, "this parm1", "20", "this parm3", "40"); ... 실행된 프로그램이 C/C++ 자식 프로그램인 경우

```c
void startClet(int argc, char* args[]) {
args[0]; // 프로그램 이름(플랫폼이 전달함)
args[1]; // "this parm1" 이 들어가 있음
args[2]; // "20" 이 들어가 있음
args[3]; // "this parm3" 이 들어가 있음
args[4]; // "40" 이 들어가 있음
}
```

실행된 프로그램이 Java 자식 프로그램인 경우 public static void main(String[] args) {

```c
int argsLen = args.length; // 5임
args[0]; // " 프로그램 이름(플랫폼이 전달함)
```

args[1]; // "this parm1" 이 들어가 있음 args[2]; // "20" 이 들어가 있음 args[3]; // "this parm3" 이 들어가 있음 args[4]; // "40" 이 들어가 있음 }

**매개 변수**

- `execName` - [in] 실행시킬 프로그램의 이름, `MC_knlGetExecNames`()에 의해 구해진다.
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

### MC_knlExit

**프로토타입**

```c
void MC_knlExit(M_Int32 exitCode)
```

**설명**

프로그램을 종료한다. 실제 종료시점은 이 함수가 불리는 시점이 아니라, 이 함수에 서 return되고, 이벤트 핸들러를 빠져나간 시점에서 종료가 일어난다. 그러므로 `MC_knlExit`()를 호출한 이후에는 바로 return해야 한다. `MC_knlExit`()를 통하여 프로그 램이 종료되게 되면 부모 프로그램과, 응용 프로그램 관리자에게 MV_CHILD_APP_DESTROY_EVENT(exitCode는 이벤트 매개변수로 전달)를 보내게 된다. 프로그램 종료 시 해제되지 않은 자원들은 플랫폼에서 자동으로 해제한다. 아래의 예는 프로그램 A가 프로그램 B를 실행시키고 프로그램 B가 exitCode 27로 종료하는 예제이다. program A

```c
void handleCletEvent(int type, int parm1, int parm2)
switch(type) {
case MV_CHILD_APP_DESTROY_EVENT :
knlPrintk("exit code %d\n", param1); // 27을 출력함
break;
case XXX :
...
execute("B", ...);
...
break;
}
```

... } program B

```c
void handleCletEvent(int type, int parm1, int parm2) {
...
if ( xxx ) {
MC_knlExit(27);
return
}
}
```

**매개 변수**

- `exitCode` - [in] 종료 값

**부작용**

없음

**참고 항목**

없음

### MC_knlProgramStop

**프로토타입**

```c
M_Int32 MC_knlProgramStop(M_Int32 prgID)
```

**설명**

수행중인 다른 응용 프로그램을 강제로 종료시킨다. 동적 로딩 라이브러리는 강제로 해제될 수 없고, 동적 로딩 라이브러리를 사용하는 모든 응용프로그램이 종료되면 자동으로 종료된다. 부모프로그램은 종료시킬 수 없고, 자식프로그램만 종료시킬 수 있다.

**매개 변수**

- `prgID` - [in] 종료시킬 프로그램 식별자

**반환 값**

성공

실패

- `M_E_ACCESS` - 부모 프로그램 종료를 시도한 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlGetCurProgramID

**프로토타입**

```c
M_Int32 MC_knlGetCurProgramID()
```

**설명**

현재 수행되고 있는 자기 자신의 프로그램 식별자를 얻어 온다.

**반환 값**

프로그램 식별자

**부작용**

없음

**참고 항목**

없음

### MC_knlGetParentProgramID

**프로토타입**

```c
M_Int32 MC_knlGetParentProgramID()
```

**설명**

현재 수행되고 있는 프로그램의 부모 프로그램 식별자를 얻어 온다.

**반환 값**

프로그램 식별자

**부작용**

없음

**참고 항목**

없음

### MC_knlGeAppManagerID

**프로토타입**

```c
M_Int32 MC_knlGetAppManagerID()
```

**설명**

응용프로그램 관리자의 프로그램 ID를 구한다.

**반환 값**

프로그램 식별자

**부작용**

없음

**참고 항목**

없음

### MC_knlGetProgramInfo

**프로토타입**

```c
M_Int32 MC_knlGetProgramInfo(M_Int32* buf, M_Int32 bufSize)
```

**설명**

현재 동작중인 프로그램에 대한 정보를 얻는다. 반환값은 현재 동작중인 프로그램의 수를 나타내고, buf 배열에는 프로그램 ID, 프로그램 type이 쌍으로 온다. 예를 들어 buf[0] 이 1 이고 buf[1]가 MC_PRGTYPE_JAVADLL일 경우, 프로그램 ID가 1인 프로 그램의 타입이 java application DLL이라는 것을 나타낸다. 따라서 배열의 크기는 프 로그램 수의 2배가 된다.

**매개 변수**

- `buf` - [out] 구해진 프로그램 타입이 반환될 버퍼
- `bufSize` - [in] 전달되는 버퍼 크기

**반환 값**

성공

동작중인 프로그램 수
실패

- `M_E_SHORTBUF` - 버퍼가 작아 모두 반환하지 못하는 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlGetAccessLevel

**프로토타입**

```c
M_Int32 MC_knlGetAccessLevel()
```

**설명**

프로그램의 접근 수준을 구한다. 반환 값의 각 비트(bit)는 현재 프로그램이 접근할 수 있는 API들의 종류를 나타낸다. 각 비트(bit)의 의미는 `MC_DIR_SYS_READ_REQ_MASK`, `MC_DIR_SYS_WRITE_REQ_MASK`, `MC_DIR_SHARED_READ_REQ_MASK`, `MC_DIR_SHARED_WRITE_REQ_MASK`, `MC_NETWORK_ACCESS_REQ_MASK`, `MC_SERIAL_ACCESS_REQ_MASK`, `MC_SYSTEM1_ACCESS_REQ_MASK`, `MC_SYSTEM2_ACCESS_REQ_MASK` 마스크 값에 따른다.

**반환 값**

접근수준(각 마스크값의 OR값)

**부작용**

없음

**참고 항목**

없음

### MC_knlGetProgramName

**프로토타입**

```c
M_Int32 MC_knlGetProgramName(M_Char* nameBuf, M_Int32 bufSize)
```

**설명**

현재 수행되고 있는 자기 자신의 프로그램 이름을 구한다. 구해지는 이름은 ADF 파 일에 기술된 이름이다.

**매개 변수**

- `nameBuf` - [out] 구해진 이름이 반환될 버퍼
- `bufSize` - [in] namebuf size

**반환 값**

성공

실패

- `M_E_SHORTBUF` - 버퍼가 작아 이름을 모두 반환하지 못하는 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlCreateSharedBuf

**프로토타입**

```c
M_Uint32 MC_knlCreateSharedBuf(const M_Char* name, M_Int32 size)
```

**설명**

공유 버퍼를 생성한다. 공유 버퍼는 프로그램간에 자료를 공유할 수 있도록 한다. 생 성된 버퍼는 이 버퍼를 사용하는 모든 프로그램이 종료되면 자동으로 삭제된다.

**매개 변수**

- `name` - [in] 공유버퍼의 이름. Null 문자로 끝난다.
- `size` - [in] 생성시킬 버퍼의 크기

**반환 값**

성공

생성된 간접버퍼(메모리식별자)
실패

- 0 같은 이름의 공유버퍼가 존재하거나 메모리가
부족한 경우

**부작용**

공유버퍼 생성시 메모리가 부족하면 컴팩션이 일어날 수 있다.

**참고 항목**

없음

### MC_knlDestroyShareBuf

**프로토타입**

```c
M_Int32 MC_knlDestroySharedBuf(M_Uint32 buf)
```

**설명**

생성된 공유버퍼를 파괴한다.

**매개 변수**

- `buf` - [in] 공유 간접버퍼(메모리식별자)

**반환 값**

성공

실패

- `M_E_INVALID` - 공유버퍼의 메모리식별자가 존재하지 않을 경우
- `M_E_ERROR` - 기타 이유로 공유버퍼를 파괴할 수 없을 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlGetSharedBuf

**프로토타입**

```c
M_Uint32 MC_knlGetSharedBuf(const M_char* name)
```

**설명**

name 문자열로 생성된 공유 버퍼를 얻어 온다.

**매개 변수**

- `name` - [in] 공유버퍼의 이름. Null 문자로 끝난다.

**반환 값**

성공

공유 간접버퍼(메모리식별자)
실패

- 0 설정된 공유버퍼가 없는 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlGetSharedBufSize

**프로토타입**

```c
M_Int32 MC_knlGetSharedBufSize(M_Uint32 buf)
```

**설명**

공유 버퍼 크기를 얻어 온다.

**매개 변수**

- `buf` - [in] 공유 간접버퍼(메모리식별자). `MC_knlCreateSharedBuf`()나 `MC_knlGetSharedBuf()` 함수의 반환값이다.

**반환 값**

성공

공유버퍼 크기
실패

- -1 - 설정된 공유버퍼가 없는 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlResizeSharedBuf

**프로토타입**

```c
M_Uint32 MC_knlResizeSharedBuf(M_Uint32 buf, M_Int32 size)
```

**설명**

공유버퍼의 크기를 변경한다.

**매개 변수**

- `buf` - [in] 공유 간접버퍼(메모리식별자)
- `size` - [in] 생성할 공유버퍼 크기

**반환 값**

성공

크기가 변경된 공유 간접버퍼(메모리식별자)
실패


**부작용**

공유버퍼 크기변경 시 메모리가 부족하면 컴팩션이 일어날 수 있다

**참고 항목**

없음

### MC_knlAlloc

**프로토타입**

```c
M_Uint32 MC_knlAlloc(M_Int32 size)
```

**설명**

힙에서 요청하는 크기만큼의 메모리를 할당한다. 할당된 메모리는 `MC_knlFree`()에서 해제해 주어야 재사용된다. 할당된 메모리를 프로그램 종료 시까지 해제하지 않으면 프로그램 종료 시 플랫폼에서 자동으로 해제한다. 할당된 메모리는 메모리 식별자로 사용시 `MC_GETDPTR`()를 이용하여 포인터를 구해와 사용해야 한다. 메모리 상에서 소비된 메모리 크기는 동적 메모리 관리에 필요한 크기까지 포함된다.

**매개 변수**

- `size` - [in] 할당을 요청하는 크기(byte단위)

**반환 값**

성공

할당된 메모리 식별자
실패


**부작용**

메모리가 부족하면 컴팩션이 일어날 수 있다

**참고 항목**

없음

### MC_knlCalloc

**프로토타입**

```c
M_Uint32 MC_knlCalloc(M_Int32 size)
```

**설명**

힙에서 요청하는 크기만큼의 메모리를 할당한다. 할당되는 영역은 0으로 초기화된다. 할당된 메모리는 `MC_knlFree`()에서 해제해 주어야 재사용된다. 할당된 메모리를 프 로그램 종료 시까지 해제하지 않으면 프로그램 종료 시 플랫폼에서 자동으로 해제한 다. 할당된 메모리는 메모리 식별자로 사용시 `MC_GETDPTR`()를 이용하여 포인터를 구해와 사용해야 한다. 메모리 상에서 소비된 메모리 크기는 동적메모리 관리에 필 요한 크기까지 포함된다.

**매개 변수**

- `size` - [in] 할당을 요청하는 크기(byte단위)

**반환 값**

성공

할당된 메모리 식별자
실패


**부작용**

메모리가 부족하면 컴팩션이 일어날 수 있다

**참고 항목**

없음

### MC_knlFree

**프로토타입**

```c
void MC_knlFree(M_Uint32 mID)
```

**설명**

`MC_knlCalloc`()으로 할당한 메모리를 해제한다. 할당되지 않은 메모리를 해제하려고 하면 안 된다. 스택에 남아있는 메모리는 해제 대상에서 제외될 수 있다.

**매개 변수**

- `mID` - [in] 해제할 메모리 식별자

**부작용**

없음

**참고 항목**

없음

### MC_knlGetTotalMemory

**프로토타입**

```c
M_Int32 MC_knlGetTotalMemory()
```

**설명**

total메모리를 구한다.

**반환 값**

total메모리(byte단위)

**부작용**

없음

**참고 항목**

없음

### MC_knlGetFreeMemory

**프로토타입**

```c
M_Int32 MC_knlGetFreeMemory()
```

**설명**

free메모리를 구한다. 컴팩션을 수행하고 free메모리를 구해 반환한다. 명시적으로 메 모리 컴팩션이 필요한 경우, 이 함수를 이용한다

**반환 값**

free메모리(byte단위)

**부작용**

없음

**참고 항목**

없음

### MC_knlDefTimer

**프로토타입**

```c
void MC_knlDefTimer(MCTimer* tm, TIMERCB cb)
```

**설명**

타이머를 초기화하고 콜백함수를 등록한다. 타이머가 만료되면 등록된 콜백함수가 호출된다. 콜백함수가 호출될 때 `MC_knlSetTimer`()에서 설정한 타이머구조체 포인터와 매개변 수가 전달된다. MCTimer tm;

```c
void TimerCb(MCTimer* ptm, void* parm) {
MC_knlPrintk("timer occur %d\n", parm);
MC_knlSetTimer(ptm, 1000L, (int)param+1);
}
void startClet(int argc, char* argv[]) {
MC_knlPrintk("start Clet!!!\n");
MC_knlDefTimer(&tm, TimerCb);
MC_knlSetTimer(&tm, 1000L, 0x1234);
}
```

**매개 변수**

- `tm` - [in] 초기화할 타이머 구조체 포인터
- `cb` - [in] 타이머 콜백함수

**부작용**

없음

**참고 항목**

없음

### MC_knlSetTimer

**프로토타입**

```c
M_Int32 MC_knlSetTimer(MCTimer* tm, M_Int64 timeout, void* parm)
```

**설명**

타이머를 설정한다. 타이머가 만료되면 `MC_knlDefTimer`()에서 설정한 콜백함수가 불린다. 만료되지 않은 타이머가 남은 상태에서 프로그램이 종료하면, 남은 타이머들은 자동으로 해제된다. 만료되지 않은 타이머를 이 함수를 통해서 재 정의하면 오류가 발생한다. 만일 만료 되지 않은 타이머를 재 정의하기 위해서는 `MC_knlUnsetTimer`()를 호출한 후에 이 함수를 다시 호출한다. 타이머는 플랫폼하단의 운영체제에서 지원하는 타이머 resolution과 타이머 만료 시 다른 태스크가 수행될 경우 어느 정도의 오차는 발생할 수 있다.

**매개 변수**

- `tm` - [in] 타이머 구조체 포인터
- `timeout` - [in] millisecond단위
- `parm` - [in] 타이머가 만료되었을 때 콜백함수에 전달될 매개변수

**반환 값**

성공

실패

- `M_E_EXIST` - 기존에 설정된 타이머가 만료되지 않고 존재 하는 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlUnsetTimer

**프로토타입**

```c
void MC_knlUnsetTimer(MCTimer* tm)
```

**설명**

설정된 타이머를 취소한다. 타이머가 설정되지 않았을 때는 무시된다.

**매개 변수**

- `tm` - [in] 타이머 구조체 포인터

**부작용**

없음

**참고 항목**

없음

### MC_knlCurrentTime

**프로토타입**

```c
M_Int64 MC_knlCurrentTime()
```

**설명**

현재의 시간을 구한다. 단위는 millisecond이다.

**반환 값**

- 1970년1월1일0시0분0초를 기준으로 현재시간까지의 millisecond

**부작용**

없음

**참고 항목**

없음

### MC_knlGetSystemProperty

**프로토타입**

```c
M_Int32 MC_knlGetSystemProperty(M_Char* id, M_Char* rtnBuf, M_Int32 bufSize)
```

**설명**

단말기에 특화된 값을 읽어 온다. 패러미터로 올 수 있는 id문자열은 HAL문서 API중 `MH_sysGetInformation`()에서 사용하는 문자열에 준하고, 또한 각 이통사나 벤더에 따 라 추가 확장될 수 있다. "ESN", "NID", "SID", "BASELAT", "BASELONG", "CURRENTCH", "PHONENUMBER", "RSSILEVEL", "BATTERYLEVEL", "MAXSOCKETNUM", "MAXRSSILEVEL", "MAXSERIALNUM", "MAXBATTLEVEL", "MEDIADEVICES", "DNS", “VIBRATORLEVEL” , “VOLUMELEVEL”, “IODEVICES”, “DEFAULTVOLUME”, "REGISTRABLESTATUS_IDLE", "REGISTRABLESTATUS_INCOMING", "REGISTRABLESTATUS_POWERON", "REGISTRABLESTATUS_POWEROFF", "REGISTRABLESTATUS_BROWSERON", "“REGISTRABLESTATUS_BROWSEROFF", “SUPPORTGLOCK”, “SUPPORTPLOCK”, “NOTDELGROUP” 등의 id 문자열이 온다. 이것은 탑재되는 단말기에 따라 달라 질 수 있다.

**매개 변수**

- `id` - [in] 읽어 오고자 하는 문자열
- `rtnBuf` - [out] 반환 문자열이 반환되는 버퍼
- `bufSize` - [in] 반환 값이 저장될 버퍼 크기

**반환 값**

성공

실패

- `M_E_SHORTBUF` - 반환되는 문자열보다 전달한 버퍼크기가 작을 때 발생
- `M_E_INVALID` - 전달한 매개변수가 잘못되었음
- `M_E_NOTSUP` - 지원하지 않는 command 임
- `M_E_ACCESS` - 읽어 올 수 없는 단말기의 정보임

**부작용**

없음

**참고 항목**

없음

### MC_knlSetSystemProperty

**프로토타입**

```c
M_Int32 MC_knlSetSystemProperty(M_Char* id, M_Char* buf)
```

**설명**

단말기에 특화된 값을 설정 한다. 패러미터로 올 수 있는 id, buf문자열은 HAL문서 API 중 `MH_sysSetInformation`()에서 사용하는 문자열에 준하고, 또한 각 이통사나 벤 더에 따라 추가 확장될 수 있다.

**매개 변수**

- `id` - [in] 설정 하고자 하는 ID 문자열
- `buf` - [in] 설정할 문자열 버퍼

**반환 값**

성공

실패

- `M_E_INVALID` - 전달한 매개변수가 잘못된 경우
- `M_E_ACCESS` - 설정할 수 없는 정보인 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlGetResourceID

**프로토타입**

```c
M_Int32 MC_knlGetResourceID(M_Char* resourceName, M_Int32* size)
```

**설명**

프로그램과 연관된 리소스의 ID를 얻어온다

**매개 변수**

- `resourceName` - [in] 리소스 이름
- `size` - [out] 리소스 크기

**반환 값**

성공

리소스 ID
실패

- `M_E_NOENT` - : 리소스가 존재하지 않는 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlGetResource

**프로토타입**

```c
M_Int32 MC_knlGetResource(M_Int32 resourceID, M_Uint32 buf, M_Int32 bufSize)
```

**설명**

리소스 ID에 해당하는 리소스를 읽어온다.

**매개 변수**

- `resourceID` - [in] 리소스ID
- `buf` - [in] 리소스를 복사할 간접버퍼(메모리식별자)
- `bufSize` - [in] 버퍼크기

**반환 값**

성공

실패

- `M_E_SHORTBUF` - 버퍼크기가 작은 경우

**부작용**

컴팩션이 일어날 수 있음

**참고 항목**

없음

### MC_DLL_INTERFACE

**프로토타입**

```c
MC_DLL_INTERFACE(void* interface, M_Char* interfaceName, M_Int32 major,
M_Int32 minor)
```

**설명**

export할 인터페이스의 엔트리(entry)를 정의한다. 여기서 정의한 엔드리(entry)는 `MC_EXPORT_DLL_INTERFACE_LIST`()의 패러미터로 사용된다. 여기서 부여한 interfaceName, major, minor값이 `MC_knlGetDLLInterface`()에서 부합하는 인터페이스 를 찾는 검색대상으로 사용된다.

**매개 변수**

- `interface` - [in] 응용프로그램 개발자 정의 interface
- `interfaceName` - [in] 인터페이스에 부여할 이름
- `major` - [in] 인터페이스에 부여할 major버전 넘버
- `minor` - [in] 인터페이스에 부여할 minor버전 넘버 `MC_EXPORT_DLL_INTERFACE_START`(dllName), `MC_EXPORT_DLL_INTERFACE_END`

**프로토타입**

```c
MC_EXPORT_DLL_INTERFACE_START(dllName)
MC_DLL_INTERFACE()
MC_DLL_INTERFACE()
… MC_DLL_INTERFACE()
MC_EXPORT_DLL_INTERFACE_END
```

**설명**

export할 인터페이스들의 리스트를 정의한다.

**매개 변수**

- `dllName` - [in] dll이름(예, MyNetworkDLL)

### MC_DLL_INIT

**프로토타입**

```c
MC_DLL_INIT(M_Int32 (*initFunc)(void))
```

**설명**

DLL이 로딩될 때 한번 호출되어야 할 함수를 정의한다. 여기서 정의한 함수를 이용 하여 DLL개발자는 DLL이 사용되기 전 필요한 초기화를 수행할 수 있다. 선언되지 않으면, 로딩 시 초기화 함수는 불리지 않는다. `M_Int32` (*initFunc)(void)가 정상적으 로 동작하면 0을 반환하여야 하고, 음수 값이 반환되면 해당 DLL은 `MC_knlLoad`()에 서 로딩되지 않고 M_E_INIT값을 반환한다.

### MC_DLL_EXIT

**프로토타입**

```c
MC_DLL_EXIT(void (*exitFunc)(void))
```

**설명**

DLL이 메모리에서 해제될 때 한번 불리워야 될 함수를 정의한다. 여기서 정의한 함 수를 이용하여 DLL개발자는 DLL이 종료되기 전 필요한 조치(리소스 프리(free)등)를 할 수 있다. 선언되지 않으면 언로딩(unloading)시 종료함수는 불리지 않는다. `MC_EXPORT_DLL_START`(dllName), `MC_EXPORT_DLL_END`

**프로토타입**

```c
MC_EXPORT_DLL_START(dllName)
MC_DLL_INIT()
MC_DLL_EXIT()
MC_EXPORT_DLL_END
```

**설명**

DLL을 호출할 때 최초로 호출되는 함수와 DLL이 메모리에서 해제될 때 호출되는 함 수이다. dllName은 builtin dll과 같이 한 이미지에 여러 개의 DLL module 이 올 경우, 구분자 역할을 한다. 또한 MC_EXPORT_DLL_INTERFACE_START와 MC_EXPORT_DLL_START는 같은 파일안에 존재해야하고 같은 dllName을 사용해야 한다. 예1) `MC_EXPORT_DLL_INTERFACE_START`(test1) `MC_EXPORT_DLL_INTERFACE_END` `MC_EXPORT_DLL_START`(test1) `MC_EXPORT_DLL_END` 예2) `MC_EXPORT_DLL_INTERFACE_START`(test2) `MC_DLL_INTERFACE`(interface1, “testInterface1”, 1, 0) `MC_EXPORT_DLL_INTERFACE_END` `MC_EXPORT_DLL_START`(test2) `MC_EXPORT_DLL_END` `MC_EXPORT_DLL_INTERFACE_START`(test3) `MC_DLL_INTERFACE`(interface2, “testInterface2”, 1, 0) `MC_EXPORT_DLL_INTERFACE_END` `MC_EXPORT_DLL_START`(test3) `MC_DLL_INIT`(initFunc) `MC_EXPORT_DLL_END`

**매개 변수**

- `dllName` - [in] dll이름(예, MyNetworkDLL)

### MC_knlLoad

**프로토타입**

```c
M_Int32 MC_knlLoad(M_Char* dllLibName, M_Int32 parmCnt, ...)
```

**설명**

플랫폼에 설치된 동적링킹라이브러리(DLL)를 로딩한다. 만기일이 지났거나 기타, 접근이 허락되지 않으면 에러 값을 반환한다. 이 함수는 넌 블로킹(non-blocking)함수이다. 프로그램이 라이브러리를 로딩하면 같은 메모리공간에 존재하고 바로 라이브러리함수를 불러 사용할 수 있다. 서로 다른 프로그램이 같은 라이브러리를 로딩하면 라이브러리 등록시 설정한 값(예를 들어 ADF)에 따라 라이브 러리가 공유 될 수도 있고, 별도로 로딩 될 수도 있다. 해당 라이브러리는 라이브러 리를 로딩한 모든 프로그램이 명시적으로 `MC_knlUnload`()를 수행하거나, 사용하는 모든 프로그램이 종료되면 자동으로 종료된다.

**매개 변수**

- `dllLibName` - [in] 적재할 DLL 이름, `MC_knlGetExecNames`()에 의해 구해진다.
- `parmCnt` - [in] 이 매개변수 뒤에 연속해서 전달되는 매개변수 수

**반환 값**

성공

생성된 프로그램 ID
실패

- `M_E_ACCESS` - 만기일이 지났거나, 접근 권한이 없는 경우
- `M_E_NOMEMORY` - 메모리가 부족한 경우
- `M_E_INVALID` - 전달한 매개변수가 잘못된 경우
- `M_E_INIT` - DLL로딩 초기화중 잘못된 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlUnload

**프로토타입**

```c
M_Int32 MC_knlUnload(M_Int32 dllID)
```

**설명**

플랫폼에 로딩된 동적링킹라이브러리(DLL)와의 연결을 끊는다. 서로 다른 프로그램이 같은 라이브러리를 로딩한 경우에는 실제적인 종료는 로딩한 모든 프로그램이 `MC_knlUnload`()를 수행할 때, 맨 마지막에 수행되는 `MC_knlUnload`()에서 일어난다. 라이브러리를 로딩한 프로그램이 `MC_knlUnload`()을 수행하지 않고 종료하면 종료시 자동으로 수행된다.

**매개 변수**

- `dllID` - [in] `MC_knlLoad`()에서 구해진 ID

**반환 값**

성공

실패

- `M_E_INVALID` - 전달한 매개변수가 잘못된 경우

**부작용**

없음

**참고 항목**

없음

### MC_knlGetDLLInterface

**프로토타입**

```c
void* MC_knlGetDLLInterface(M_Char* name, M_Int32 major, M_Int32 minor,
M_Int32* rtnMajor, M_Int32* rtnMinor);
```

**설명**

로딩된 동적링킹라이브러리(DLL)에서 인터페이스를 구한다. 현재의 프로그램이 `MC_knlLoad`()로 로딩한 동적링킹라이브러리와 빌트인(built-in)된 동적링킹라이브러리중 name, major, minor에 일치하는 인터페이스를 찾아 반환한다. 실행(runtime)중 로딩한 라이브러리와 초기 설치(built-in)된 라이브러리 양쪽에 일치하 는 인터페이스가 있을 경우, 실행 중 로딩된 라이브러리를 먼저 찾는다. 실행 중 로 딩한 라이브러리들 중에 일치하는 인터페이스가 여러 개 발견될 경우에는 나중에 로 딩한 라이브러리에서 찾는다. 인터페이스는 `MC_knlLoad`()뿐만 아니라 빌트인(built-in), APM의 자동로딩, 응용프로그램 개발자 조작 등에 의해서도 로딩될 수 있다. 이럴 경우, `MC_knlLoad`()로 로딩하지 않는 DLL들도 `MC_knlGetDLLInterface`()에 의해 찾아 질 수 있다. 일치하는 조건은 아래와 같다.
