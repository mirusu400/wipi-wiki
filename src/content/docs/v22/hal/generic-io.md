---
title: "2.9. Generic I/O"
---

## 2.9.1. 개요

#### 용어정의

IrDA 적외선 통신을 위한 장치를 말한다. 1Chip 단말을 이용한 전자 결재 시 인증 등에 필요한 개인 정보를 저장하는 IC 카드를 말한다. UICC(Universal IC Card) WCDMA 단말에서 각종 단말 정보를 저장하고 관리하기 위한 용도의 카드로, 1Chip 기능도 포함되어 있다.

#### 개요

Generic I/O는 향후 추가되는 I/O 장치에 대해서 어플리케이션 레벨에서 별도의 API 추가 없이 확장이 가능하도록 하기 위해 마련된 규격이다. HAL에서는 각 I/O 장치의 기본 오퍼레이션에 대한 함수를 작성하고 이를 플랫폼에 등록한다. 어플리케이션에서는 장치의 타입에 따라서 플랫폼에 등록된 해당 장치의 함수를 호출하여 장치를 제어한다. 단말기에서 지원 가능한 장치의 종류는 `MH_sysGetInformation` ()의 command로 “IODEVICES”를 이용해서 반환받을 수 있도록 해 주어야 한다.

#### 함수 기능 및 목록

> **<표 2-9-1> 함수 기능 및 목록**

세부 카테고리 함수
Device Initialization `MH_ioDevInit()`
`M_Int32` (*DEVOPENFUN)(`M_Uint16` devnum, void
*param)
Device I/O
`M_Int32` (*DEVCLOSEFUN)(`M_Uint16` devnum)
`M_Int32` (*DEVREADFUN)(`M_Uint16` devnum, `M_Byte`
*buf, `M_Int32` len)
`M_Int32` (*DEVWRITEFUN)(`M_Uint16` devnum, `M_Byte`
*buf, `M_Int32` len)
`M_Int32` (*DEVCONTROLFUN)(`M_Uint16` devnum,

```c
M_Char *cmd, void *param1, void *param2)
장치 제어 오퍼레이션
```

제공되는 장치의 기본 오퍼레이션은 open, close, read, write, io control이며 io control에 명령어를 등록하여 다양한 오퍼레이션을 추가할 수 있다. HAL에서는 각 장치에 대한 open, close, read, write, io control에 대한 함수를 작성하여 `MH_IODevice` 구조체에 연결하고, `MH_pltRegIODevice()` API를 이용하여 플랫폼 에 등록한다.

#### 물리적인 장치와 논리적인 장치

I/O 장치는 특성에 따라 물리적인 장치와 논리적인 장치로 구분되어진다. 물리 적인 장치는 같은 장치 이름을 가지면서 물리적으로 구별되는 장치가 여러 개인 경우에 해당되며, 어플리케이션은 미리 약속된 장치 번호를 사용하여 원하는 장 치를 열 수 있다. 논리적인 장치는 물리적으로는 하나의 장치이지만 논리적으로 동시에 다수의 포트나 채널 등을 열 수 있는 경우를 말하며, 어플리케이션에서 는 장치 번호 구별 없이 장치를 open 하면 논리적으로 수용 가능한 장치의 수 만큼 동시에 열 수 있다. HAL에서는 장치를 등록할 때 해당 장치가 물리적인 장 치인지 논리적인 장치인지를 type 필드에 “physical” 또는 “logical”로 명시하고 동시에 open 가능한 장치의 수를 등록해 주어야 한다. 일반적으로 open 가능한 장치가 하나인 경우에는 물리적인 장치가 된다. 물리적인 장치인 경우 HAL에서 는 장치 번호에 따라 미리 약속된 장치를 열어주면 된다. 논리적인 장치인 경우 HAL에서는 장치 번호에 따라 open 가능한 포트 또는 채널 등을 열어 주고, 장 치 번호와 그에 따라 열린 포트 또는 채널에 대한 매핑 테이블을 관리하여 이후 read/write/control 등의 작동이 발생할 때 이러한 장치 번호를 통해 해당 포트 또는 채널을 제어할 수 있어야 한다.

#### 지원 I/O 장치 및 장치별 구현 함수

현재 규격화되어 지원하는 I/O 장치에는 IrDA 와 1-chip 장치를 포함한다. 이를 제외한 기타 장치들에 대해서는 해당 WSR (WIPI Specification Request) 규격서 를 참조한다. 아래 표는 현재 지원하는 I/O 장치별 OEM에서 구현해야 할 함수 및 구현 내용을 설명한다. I/O 장치 제어를 위한 DEVCONTROLFUN의 경우 구 현해야 할 명령어 이름 및 기능을 설명한다. I/O 장치명과 명령어 이름은 고정된 값이므로 제조사에서 임의로 지정할 수 없다.

> **<표 2-9-2> 지원 I/O 장치 및 장치별 구현 함수**

I/O 장치명 구현 함수 구현 내용
DEVOPENFUN IrDA 장치 초기화
DEVCLOSEFUN IrDA 장치 종료
DEVREADFUN IrDA를 통한 데이터 read
“IrDA”
DEVWRITEFUN IrDA를 통한 데이터 write
“SETOPCODE” – opcode를 통한 전송 방식
DEVCONTROLFUN
설정
DEVOPENFUN 1Chip 장치 초기화
DEVCLOSEFUN 1Chip 장치 종료
DEVREADFUN 1Chip 장치를 통한 데이터 read
“1ChipCard”
DEVWRITEFUN 1Chip 장치를 통한 데이터 write
“GETSTATUS” - IC 카드의 존재 여부
DEVCONTROLFUN
“GETCHANNEL” - 논리적인 채널 번호 얻기

## 2.9.2. 관련 자료형

### MH_IODevEvent

```c
typedef struct MH_IODevEvent {
    M_Int32 event; // 발생된 event, MH_SUB_IODEVICE_EVENT
    M_Char devname[MH_DEV_NAME_LEN]; // event가 발생한 장치 이름
    M_Uint16 devnum;
    M_Char cmd[MH_IO_COMMAND_MAX]; // 해당 컨트롤 커맨드
    M_Int32 error; // 디바이스별 추가되는 서브이벤트
    M_Uint32 param_sz; // param 사이즈
    void *param; // cmd 에 의해 요청한 데이터를 전달
} MH_IODevEvent;
```

해당 장치에 대해 시스템으로부터 이벤트가 발생했을 때 이 자료 구조를 이용하 여 플랫폼에 이벤트를 전달한다.

#### MH_SUB_IODEVICE_EVENT

```c
typedef enum MH_SUB_IODEVICE_EVENT {
    MH_IODEVICEEV_CONNECT = 0,
    MH_IODEVICEEV_READ,
    MH_IODEVICEEV_WRITE,
    MH_IODEVICEEV_CLOSE,
    MH_IODEVICEEV_TIMEOUT,
    MH_IODEVICEEV_ERROR,
    MH_IODEVICEEV_OEMERROR,
    MH_IODEVICEEV_RESPONSE
} MH_SUB_IODEVICE_EVENT;
```

해당 장치에서 발생할 수 있는 이벤트의 타입을 정의한다. MH_IODEVICEEV_CONNECT는 non-blocking 장치의 경우 상대방과의 연결 성 공 시 전달한다.


- `MH_IODEVICEEV_READ와MH_IODEVICEEV_WRITE는장치가read나write가` - 가능하게 되는 시점에 전달한다. MH_IODEVICEEV_CLOSE는 연결이 종료된 경우에 전달한다.
- `MH_IODEVICEEV_TIMEOUT는상대방과의연결을기다리는경우주어진시간` - 이 초과했을때 전달한다. MH_IODEVICEEV_ERROR는 비정상적인 오류가 발생했을 경우 전달한다.
- `MH_IODEVICEEV_OEMERROR는전화가걸려오는경우등과같이OEM에서` - 특수한 상황에 IO 장치 오퍼레이션을 강제 종료하는 경우 전달한다. `MH_IODEVICEEV_RESPONSE` 는 non-blocking 장치의 Control Command 의 처리 결과를 전달할 콜백함수를 호출하고자 할 때 전달한다.

### MH_IODevice

```c
typedef struct MH_IODevice {
    M_Char *devname;
    M_Char *devtype;
    M_Uint16 total_devnum;
    DEVOPENFUN open;
    DEVCLOSEFUN close;
    DEVREADFUN read;
    DEVWRITEFUN write;
    DEVCONTROLFUN control;
} MH_IODevice;
```

하나의 장치를 등록하기 위한 자료형이다. 하나의 장치는 장치의 이름과 장치의 타입, 장치의 총개수, 그리고 장치를 제어하기 위한 기본 오퍼레이션의 집합으로 이루어진다. 새로운 장치가 추가될 때마다 이 자료형을 적절히 초기화하고 `MH_pltRegIODevice()` 함수를 통해 플랫폼에 등록한다. 장치의 타입은 물리적인 장치인 경우에는 “physical”을 논리적인 장치인 경우에는 “logical”을 설정한다

#### DEVOPENFUN

**프로토타입**

```c
typedef M_Int32 (*DEVOPENFUN)(M_Uint16 devnum, void *param)
```

**설명**

해당 장치를 열고 초기화한다. 해당 장치가 물리적으로 여러 개 있는 경우 미리 지정 된 devnum에 의해 해당 장치를 연다. 만약 논리적으로 여러 개의 포트나 채널을 열 수 있는 경우 devnum에 따라 구별하여 장치에서 open 가능한 포트나 채널을 임의로 할당하고, devnum과 실제 할당된 포트나 채널에 대한 매핑 테이블을 별도로 관리하 여 이후 devnum에 의해 해당 포트나 채널을 제어 가능하도록 한다. 해당 장치가 non-blocking으로 동작할 경우에는 M_E_WOULDBLOCK을 반환하고, 장치가 연결되 는 시점에 `MH_IODEVICEEV_CONNECT` 이벤트를 플랫폼에 전달한다.

**매개 변수**

- `devnum` - [in] 장치 번호
- `param` - [in] 장치 오픈 시 넘겨 줄 매개 변수

**반환 값**

성공

실패

- `M_E_INVALID` - 장치이름이 잘못되었을 경우, 유효하지 않은 장치번호일 경우(0보다 작거나 지정된 장치번호 개수보다 크거나 같 을 경우),param 매개변수가 잘못된 경우이며, 디바이스 특성에 따 름
- `M_E_WOULDBLOCK` - 장치가 연결되기를 기다려야 하는 경우
- `M_E_ISCONN` - 이미 해당 장치가 열려 있는 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

#### DEVCLOSEFUN

**프로토타입**

```c
typedef M_Int32 (*DEVCLOSEFUN)(M_Uint16 devnum)
```

**설명**

해당 장치를 닫는다.

**매개 변수**

- `devnum` - [in] 장치 번호

**반환 값**

성공

실패

- `M_E_ERROR` - 장치 닫기 실패

**부작용**

없음

**참고 항목**

없음

#### DEVREADFUN

**프로토타입**

```c
typedef M_Int32 (*DEVREADFUN)(M_Uint16 devnum, M_Byte *buf, M_Int32 len)
```

**설명**

장치로부터 데이터를 읽는다. 해당 장치가 non-blocking으로 동작할 경우에는 데이터 를 읽을 수 없을 경우 M_E_WOULDBLOCK을 반환한다.

**매개 변수**

- `devnum` - [in] 장치 번호
- `buf` - [out] 읽은 데이터를 저장할 버퍼 포인터
- `len` - [in] 버퍼의 크기

**반환 값**

성공

읽은 데이터의 크기
실패

- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘못되었을 경우
- `M_E_WOULDBLOCK` - 데이터를 읽을 수 없는 경우(해당 장치가 non-blocking으로 동작할 경우에 한함)
- `M_E_ERROR` - 기타 에러 그외 장치 별 에러 값

**부작용**

없음

**참고 항목**

없음

#### DEVWRITEFUN

**프로토타입**

```c
typedef M_Int32 (*DEVWRITEFUN)(M_Uint16 devnum, M_Byte *buf, M_Int32 len)
```

**설명**

장치에 데이터를 쓴다. 해당 장치가 non-blocking으로 동작할 경우에는 데이터를 쓸 수 없을 경우 M_E_WOULDBLOCK을 반환하고, 데이터를 쓸 수 있는 시점에 `MH_IODEVICEEV_WRITE` 이벤트를 플랫폼에 전달한다.

**매개 변수**

- `devnum` - [in] 장치 번호
- `buf` - [in] 쓸 데이터를 저장된 버퍼 포인터
- `len` - [in] 버퍼의 크기

**반환 값**

성공

쓴 데이터의 크기
실패

- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘못되었을 경우
- `M_E_WOULDBLOCK` - 데이터를 쓸 수 없는 경우(해당 장치가 non -blocking으로 동작할 경우에 한함)
- `M_E_ERROR` - 기타 에러 그외 장치 별 에러 값

**부작용**

없음

**참고 항목**

없음

#### DEVCONTROLFUN

**프로토타입**

```c
typedef M_Int32 (*DEVCONTROLFUN)(M_Uint16 devnum, M_Char *cmd, void *param1, void *param2)
```

**설명**

장치를 제어한다. 장치의 open/close/read/write 기능 이외의 장치 정보를 얻어오거나 옵션을 설정하기 위해 사용된다.

**매개 변수**

- `devnum` - [in] 장치 번호
- `cmd` - [in] 장치를 제어할 명령어 문자열
- `param1` - [in/out] 제어할 값 또는 결과를 얻어오기 위한 매개 변수
- `param2` - [in/out] 제어할 값 또는 결과를 얻어오기 위한 매개 변수

**반환 값**

성공

실패

- `M_E_INVALID` - 매개 변수가 잘못된 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MH_ioDevInit

**프로토타입**

```c
M_Int32 MH_ioDevInit(void)
```

**설명**

`MH_pltRegIODevice`()를 통해 각 장치를 등록한다. 각 장치의 open/close/read/write/control 함수를 구현하여 `MH_IODevice` 구조체에 연결 한 후 `MH_ioDevInit()` 함수 내에서 호출하는 `MH_pltRegIODevice()` 함수를 이용하여 해당 장치의 `MH_IODevice` 구조체를 등록한다.

**매개 변수**

없음

**반환 값**

성공

실패

- `M_E_ERROR` - 초기화 실패

**부작용**

없음

**참고 항목**

없음 가 IrDA 제어

#### 장치 이름

“IrDA”를 사용한다.

#### 제조사 준수 사항

IrDA OBEX 규격 version 1.2 이상을 준수해야 한다. OBEX 객체 데이터 패킷을 분할하거나 조합하는 것은 단말기에서 수행된다. 이는 어플리케이션으로부터 내려 받는 OBEX body에 해당하는 data size가 단말 의 OBEX단 처리 가능 buffer size보다 클 경우와 단말에서 어플리케이션으로 전 달하는 data buffer size가 어플리케이션이 읽어 들일 수 있는 buffer size보다 클 경우를 포함한다.

#### DEVOPENFUN

**프로토타입**

```c
typedef M_Int32 (*DEVOPENFUN)(M_Uint16 devnum, void *param)
```

**설명**

매개 변수인 param에 `MH_IrDAMode` 구조체의 포인터가 전달된다. aszMode의 값이 “Server”일 경우 서버 모드로 동작하고, “Client”인 경우 클라이언트 모드로 동작한다. nTime에 명시된 시간 동안 연결을 시도한다. 연결이 성공되면 플랫폼에 `MH_IODEVICEEV_CONNECT` 이벤트를 전달하고, (nTime이 0이면 연결이 성립될때까 지 시도한다. nTime이 0으로 셋팅된 경우, 단말이 설정한 연결 최대시간 동안 연결을 시도한다.) 타임 아웃이 발생한 경우에는 `MH_IODEVICEEV_TIMEOUT` 이벤트를 전달 한다.

```c
typedef struct MH_IrDAMode {
    M_Char aszMode[MH_IRDA_MODE_LEN]; // 모드 지정
    M_Uint32 nTime; // 연결 시도 시간
} MH_IrDAMode;
```

**매개 변수**

- `devnum` - [in] 장치 번호
- `param` - [in] `MH_IrDAMode` 구조체의 포인터

**반환 값**

성공

실패

- `M_E_NOTSUP` - IrDA를 지원하지 않는 경우
- `M_E_ISCONN` - 이미 해당 장치가 연결이 되어 있는 경우
- `M_E_INVALID` - 장치이름이 잘못되었을 경우, nTime이 음수인 경우, 유효하지 않은 장치번호일 경우(0보다 작거나 지정된 장치번 호 개수보다 크거나 같을 경우),param 매개변수가 잘못된 경우이며, 디바이스 특성에 따름
- `M_E_WOULDBLOCK` - 장치가 연결되기를 기다려야 하는 경우
- `M_E_ERROR` - 기타 에러 DEVCLOSEFUN

**프로토타입**

```c
typedef M_Int32 (*DEVCLOSEFUN)(M_Uint16 devnum)
```

**설명**

IrDA 장치를 닫는다. OBEX Client인 경우 OBEX DISCONNECT(0x81)을 사용하여 Server에 접속 중지를 알 리고 OBEX Client mode session을 종료한다. 상대방의 OBEX 연결 종료로 연결이 끊 어진 경우에는 `MH_IODEVICEEV_CLOSE` 이벤트를 플랫폼에 전달하여 이 사실을 알 린다.

**매개 변수**

- `Devnum` - 장치 번호

**반환 값**

성공

실패

- `M_E_NOTSUP` - IrDA를 지원하지 않는 경우
- `M_E_ERROR` - 기타 에러 DEVREADFUN

**프로토타입**

```c
typedef M_Int32 (*DEVREADFUN)(M_Uint16 devnum, M_Byte *buf, M_Int32 len)
```

**설명**

IrDA 장치를 통해 데이터를 읽는다.

**매개 변수**

- `devnum` - [in] 장치 번호
- `buf` - [out] 읽을 데이터(OBEX body)를 저장할 버퍼 포인터
- `len` - [in] 버퍼의 크기

**반환 값**

성공

읽은 데이터 크기
실패

- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘못되었을 경우
- `M_E_ERROR` - 기타 에러 그 외 장치별 에러 값 DEVWRITEFUN

**프로토타입**

```c
typedef M_Int32 (*DEVWRITEFUN)(M_Uint16 devnum, M_Byte *buf, M_Int32 len)
```

**설명**

IrDA 장치를 통해 데이터를 쓴다.

**매개 변수**

- `devnum` - [in] 장치 번호
- `buf` - [in] 쓸 데이터(OBEX body)가 저장될 버퍼 포인터
- `len` - [in] 버퍼의 크기

**반환 값**

성공

쓰여진 데이터 크기
실패

- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘못되었을 경우
- `M_E_ERROR` - 기타 에러 그 외 장치별 에러 값 DEVCONTROLFUN

**프로토타입**

```c
typedef M_Int32 (*DEVCONTROLFUN)(M_Uint16 devnum, M_Char *cmd, void *param1, void *param2)
```

**설명**

전송 방식을 설정한다. cmd에 “SETOPCODE”를 사용한다. param1에는 어플리케이션에서 할당한 버퍼 포인터가 넘어오며 “SETMETHOD” 값이 전달된다. param2에는 어플리케이션에서 할당한 버퍼 포인터가 넘어오며 해당 포인터가 가리키 는 값은 문자열 “OBEXPUT” (0x82, OBEX PUT) 또는 “OBEXGET” (0x83, OBEX GET) 이 된다. 이 이외의 값은 M_E_INVALID로 반환한다. “SETOPCODE”를 통해 설정된 OBEX header 값은 다시 control 함수를 통해 재설정 되지 않는 한 어플리케이션이 실행 중에는 해당 opcode 값을 유지하여 전송에 적용 한다. IrDA 장치가 open된 후 control 함수로 전송 방식을 별도로 설정하지 않고 바로 write 함수가 호출되는 경우, OBEXGET을 default 전송 방식으로 설정하여 OBEX header를 구성하도록 한다.

**반환 값**

성공

실패

- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘못되었을 경우
- `M_E_ERROR` - 기타 에러 나 1-Chip IC Card 제어 장치 이름 “1ChipCard”를 사용한다. DEVOPENFUN

**프로토타입**

```c
typedef M_Int32 (*DEVOPENFUN)(M_Uint16 devnum, void *param)
```

**설명**

1Chip Card를 활성화시킨다. 매개 변수인 param에 1Chip Card의 리셋에 대한 응답 (ATR:Answer To Reset)을 전달받기 위한 `MH_CardOption` 구조체의 포인터가 전달된 다. bATR에는 응답을 받을 버퍼가 전달되고, wATRLen에는 버퍼의 크기가 전달되며, bATR과 wATRLen에 실제 응답값과 응답의 길이를 넣어 반환한다. 만약 전달된 버퍼 의 크기가 실제 응답값보다 작다면 wATRLen에 OxFFFF와 M_E_ERROR를 반환한다. WCDMA 단말기의 경우처럼 UICC에서 여러 개의 논리적인 채널을 open 가능한 경우, devnum에 따라 다른 채널을 할당해 주고, devnum과 그에 따른 채널 번호의 매핑 테 이블을 관리하여 devnum으로 해당 채널의 제어가 가능하도록 한다.

```c
typedef struct MH_CardOption {
    M_Byte *bATR; // ATR data pointer
    M_Uint16 wATRLen; // ATR data length
} MH_CardOption;
```

**반환 값**

성공

실패

- `M_E_INVALID` - 장치이름이 잘못되었을 경우, 유효하지 않은 장치번호일 경우(0보다 작거나 지정된 장치번호 개수보다 크거나 같 을 경우),param 매개변수가 잘못된 경우이며, 디바이스 특성에 따 름
- `M_E_NODEVICE` - 카드가 삽입되어 있지 않은 경우
- `M_E_BADFORMAT` - 전송 데이터 format이 잘못된 경우
- `M_E_ERROR` - 기타 에러 DEVCLOSEFUN

**프로토타입**

```c
typedef M_Int32 (*DEVCLOSEFUN)(M_Uint16 devnum)
```

**설명**

1Chip Card를 비활성화시킨다.

**반환 값**

성공

실패

- `M_E_ERROR` - 기타 에러 DEVREADFUN

**프로토타입**

```c
typedef M_Int32 (*DEVREADFUN)(M_Uint16 devnum, M_Byte *buf, M_Int32 len)
```

**설명**

1Chip Card를 통해 데이터를 읽는다. 데이터를 바로 읽을 수 없는 경우 가능하게 될 때 `MH_IODEVICEEV_READ` 이벤트를 플랫폼에 전달한다.

**반환 값**

성공

읽은 바이트 크기
실패

- `M_E_INVALID` - 매개변수가 잘못되어 있는 경우
- `M_E_NOCARD` - 카드가 삽입되어 있지 않은 경우
- `M_E_WOULDBLOCK` - 데이터를 읽을 수 없는 경우
- `M_E_BADFORMAT` - 전송 데이터 format이 잘못된 경우
- `M_E_NOTACTIVE` - 카드가 활성화가 안된 경우
- `M_E_ERROR` - 기타 에러 DEVWRITEFUN

**프로토타입**

```c
typedef M_Int32 (*DEVWRITEFUN)(M_Uint16 devnum, M_Byte *buf, M_Int32 len)
```

**설명**

1Chip Card를 통해 데이터를 쓴다. 데이터를 바로 쓸 수 없는 경우 가능하게 될때 `MH_IODEVICEEV_WRITE` 이벤트를 플랫폼에 전달한다.

**반환 값**

성공

쓴 바이트 크기
실패

- `M_E_INVALID` - 매개 변수가 잘못된 경우
- `M_E_NOCARD` - 카드가 삽입되어 있지 않은 경우
- `M_E_WOULDBLOCK` - 데이터를 쓸 수 없는 경우
- `M_E_BADFORMAT` - 전송 데이터 format이 잘못된 경우
- `M_E_NOTACTIVE` - 카드가 활성화가 안된 경우
- `M_E_ERROR` - 기타 에러 DEVCONTROLFUN

**프로토타입**

```c
typedef M_Int32 (*DEVCONTROLFUN)( M_Uint16 devnum, M_Char *cmd,
void *param1, void *param2)
```

**설명**

1Chip Card의 삽입 여부를 검사한다. cmd에 “GETSTATUS”를 사용한다. param1에는 어플리케이션에서 할당한 버퍼가 넘어오며 카드가 삽입되어 있을 경우에 는 “exist”를, 삽입되어 있지 않을 경우에는 “noexist”를 반환한다. param2에는 param1에서 넘어온 버퍼의 길이가 넘어온다

**반환 값**

성공

실패

- `M_E_INVALID` - 매개 변수가 잘못된 경우
- `M_E_ERROR` - 기타 에러 UICC의 논리적인 채널 번호 얻기 cmd에 “GETCHANNEL”을 사용한다. param1에는 정수형 포인터를 넘어온다. WCDMA 단말의 경우에 한해서 사용되며 현 재 할당된 UICC의 논리적인 채널 번호를 반환한다. param2는 무시된다.

**반환 값**

성공

실패

- `M_E_BADFORMAT` - 전송 cmd가 잘못된 경우
- `M_E_ERROR` - 기타 에러
- `M_E_INVALID` - 매개변수가 잘못된 경우
