---
title: "2.9. Generic I/O"
---

## 2.9.1. 개요

#### 용어정의

IrDA 적외선 통신을 위한 장치를 말한다. 1Chip 단말을 이용한 전자 결재 시 인증 등에 필요한 개인 정보를 저장하는 IC 카드를 말 한다. UICC(Universal IC Card) WCDMA 단말에서 각종 단말 정보를 저장하고 관리하기 위한 용도의 카드로, 1Chip 기능도 포함되어 있다.

#### 개요

단말기에 장착되는 일반적인 장치를 다루기 위한 API를 제공한다. 향후 추가되는 모 든 I/O장치에 대해서 별도의 API의 추가 없이 제어가 가능하다. 어플리케이션에서는 장치의 이름에 의해 그에 해당 장치를 open하면 그 이후 장치 식별자에 의해 모든 제어가 가능하다. 단말기에서 지원 가능한 장치의 종류는 `MC_knlGetSystemProperty`()에 의해 얻어오며 command로 “IODEVICES”를 사용한다.

#### 함수 기능 및 목록

기 능 목 록 `MC_ioDevOpen` 장치 open/close `MC_ioDevClose` `MC_ioDevRead` 데이터 통신 `MC_ioDevWrite` 장치 제어 `MC_ioDevControl` `MC_ioDevSetOpenCB` 콜백 등록 `MC_ioDevSetReadCB` `MC_ioDevSetReadCB`

#### 지원 I/O 장치 및 기능

현재 규격화되어 지원하는 I/O 장치에는 IrDA, Camera와 1-chip 장치를 포함한다. 현재 지원하는 장치에 대한 API 및 기능은 다음과 같다. IrDA I/O 장치명 API 기능 `MC_ioDevOpen` IrDA 장치 초기화 장치 연결 성공, 타임아웃, 연결 `MC_ioDevSetOpenCB` 종료 등을 알기 위한 콜백 등록 `MC_ioDevClose` IrDA 장치 종료 `MC_ioDevRead` IrDA를 통한 데이터 read “IrDA” `MC_ioDevSetReadCB` 데이터 수신에 관한 콜백 등록 `MC_ioDevWrite` IrDA를 통한 데이터 write `MC_ioDevSetWriteCB` 데이터 송신에 관한 콜백 등록 “SETOPCODE” `MC_ioDevControl` IrDA 전송 방식 설정 1-Chip I/O 장치명 API 기능 `MC_ioDevOpen` 1Chip 장치 초기화 1Chip Card 통신 중에 발생할 `MC_ioDevSetOpenCB` 수 있는 에러 상황을 알기 위한 콜백 등록 `MC_ioDevClose` 1Chip 장치 종료 `MC_ioDevRead` 1Chip 장치를 통한 데이터 read “1ChipCard” `MC_ioDevSetReadCB` 데이터 수신시 콜백 등록 `MC_ioDevWrite` 1Chip 장치를 통한 데이터 write `MC_ioDevSetWriteCB` 데이터 송신시 콜백 등록 “GETSTATUS”- IC 카드의 존재 여부 `MC_ioDevControl` “GETCHANNEL” - 논리적인 채 널 번호 얻기

#### MC_ioDevControl()의 command 별 제어 정보

IrDA command Parameter param1 “SETOPCODE” [in] “SETMETHOD” 문자열 :IrDA의 전송 방식 설정 param2 [in] “OBEXPUT”, “OBEXGET” 문자열 중 하나 1-Chip command Parameter param1 [in] 버퍼 포인터 “GETSTATUS” [out] “exist”, “noexist” 문자열 중 하나 :IC Card의 삽입 여부 조사 param2 [in] 버퍼의 크기 param1 “GETCHANNEL” [in] 정수형 포인터 :현재 할당된 UICC의 논리 [out] 채널 번호 적인 채널 번호 얻기 param2 [in] `NULL`

#### DEVOPENCB

**프로토타입**

```c
typedef void (*DEVOPENCB)(M_Int32 fd, M_Int32 error, void *param)
```

**설명**

함수 MC_ioDevSetOpenCB에 등록하는 콜백 함수. 해당 장치가 non-blocking으로 동 작할 경우 장치 연결의 성공 여부나 비정상적인 종료에 대한 이벤트가 발생하는 시 점에서 불린다.

**매개 변수**

- `fd` - 장치 식별자
- `error` - 성공 0 실패 `M_E_DEVCLOSE`(종료 이벤트 발생시), `M_E_TIMEOUT`(타임아웃 발생시), `M_E_ERROR`(연결 실패시)
- `param` - 콜백 함수를 등록할 때 설정하는 콜백 매개 변수

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MC_ioDevSetReadCB`

#### DEVREADCB

**프로토타입**

```c
typedef void (*DEVREADCB)(M_Int32 fd, M_Int32 error, void *param)
```

**설명**

함수 MC_ioDevSetReadCB에 등록하는 콜백 함수. 해당 장치가 non-blocking으로 동 작할 경우 장치가 데이터를 읽을 수 있는 시점에서 불린다.

**매개 변수**

- `fd` - 장치 식별자
- `error` - 성공 0 실패 `M_E_ERROR`
- `param` - 콜백 함수를 등록할 때 설정하는 콜백 매개 변수

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MC_ioDevSetReadCB`

#### DEVWRITECB

**프로토타입**

```c
typedef void (*DEVWRITECB)(M_Int32 fd, M_Int32 error, void *param)
```

**설명**

함수 MC_ioDevSetWriteCB에 등록하는 콜백 함수. 해당 장치가 non-blocking으로 동 작하는 경우 장치가 데이터를 전송할 수 있을 경우 불린다.

**매개 변수**

- `fd` - 장치 식별자
- `error` - 성공: 0, 실패: `M_E_ERROR`
- `param` - 콜백 함수를 등록할 때 설정하는 콜백 매개 변수

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MC_ioDevSetWriteCB`

### MC_ioDevOpen

**프로토타입**

```c
M_Int32 MC_ioDevOpen(M_Char *devname, M_Uint16 devnum, void *param)
```

**설명**

장치를 열고 초기화한다. 지원하는 장치의 이름 및 장치의 개수는 `MC_knlGetSystemProperty()` 함수의 매개 변수로 “IODEVICES”를 전달해서 얻어올 수 있다. 물리적으로 구분되어져야 하는 동 일한 I/O 장치가 두 개 이상일 경우에는 매개 변수로 전달되는 devnum에 의해 구별 한다. 예를 들어 IrDA 장치가 두 개일 경우 첫번째 장치는 “0”번, 두번째 장치는 “1” 번이 된다.

**매개 변수**

- `devname` - [in] 장치의 이름
- `devnum` - [in] 장치의 번호
- `param` - [in] 장치 open 시 넘겨줄 파라미터

**반환 값**

성공

장치 식별자
실패

- `M_E_NOTSUP` - 해당 장치를 지원하지 않는 경우
- `M_E_ISCONN` - 해당 장치가 이미 열려 있는 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_knlGetSystemProperty`

### MC_ioDevSetOpenCB

**프로토타입**

```c
M_Int32 MC_ioDevSetOpenCB(M_Int32 fd, DEVOPENCB cb, void *param)
```

**설명**

Non-blocking I/O 장치의 경우 장치 연결의 성공 여부나 비정상적인 종료에 대한 이 벤트를 전달받기 위한 콜백 함수를 등록한다. 콜백 함수가 불리면 매개 변수 param 값이 콜백 함수 API로 전달된다. 이 함수가 에러를 반환하면 콜백 함수는 불리지 않 는다.

**매개 변수**

- `fd` - [in] I/O 장치 식별자
- `cb` - [in] 콜백 함수
- `param` - [in] 콜백 함수가 불릴 때 전달되는 값

**반환 값**

성공

실패

- `M_E_BADFD` - 잘못된 식별자
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevClose

**프로토타입**

```c
M_Int32 MC_ioDevClose(M_Int32 fd)
```

**설명**

장치의 사용을 종료한다. Non-blocking I/O 장치의 경우 장치에 등록되어 있던 모든 콜백 함수는 삭제되어 불리지 않게 된다.

**매개 변수**

- `fd` - [in] 장치 식별자

**반환 값**

성공

실패

- `M_E_BADFD` - 유효하지 않은 식별자

**부작용**

없음

**참고 항목**

없음

### MC_ioDevRead

**프로토타입**

```c
M_Int32 MC_ioDevRead(M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**설명**

I/O 장치로부터 데이터를 읽어온다.

**매개 변수**

- `fd` - [in] 장치 식별자
- `buf` - [out] 읽어 들일 데이터를 저장할 버퍼 포인터
- `len` - [in] 읽어 들일 데이터를 저장할 버퍼의 크기

**반환 값**

성공

읽은 데이터 길이
실패

- `M_E_WOULDBLOCK` - 읽을 데이터가 없을 경우
- `M_E_BADFD` - 유효하지 않은 식별자
- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘못되었을 경우

**부작용**

없음

**참고 항목**

없음

### MC_ioDevWrite

**프로토타입**

```c
M_Int32 MC_ioDevWrite(M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**설명**

I/O 장치에 데이터를 쓴다.

**매개 변수**

- `fd` - [in] 장치 식별자
- `buf` - [in] 쓸 데이터를 저장하고 있는 버퍼 포인터
- `len` - [in] 쓸 데이터를 저장하고 있는 버퍼의 크기

**반환 값**

성공

쓴 데이터 길이
실패

- `M_E_WOULDBLOCK` - 현재 데이터를 쓸 수 없는 경우
- `M_E_BADFD` - 유효하지 않은 식별자
- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘못되었을 경우

**부작용**

없음

**참고 항목**

없음

### MC_ioDevSetReadCB

**프로토타입**

```c
M_Int32 MC_ioDevSetReadCB(M_Int32 fd, DEVREADCB cb, void *param)
```

**설명**

Non-blocking I/O 장치의 경우 장치를 통해서 데이터를 읽을 수 있는 시점에서 불리 는 콜백 함수를 등록한다. 콜백 함수가 불리면 매개 변수 param값이 콜백 함수 API 로 전달된다. 등록하는 콜백 함수가 NULL일 경우 이전에 이 함수로 등록한 콜백 함 수가 삭제된다. 이 함수가 에러를 반환하면 콜백 함수는 불리지 않는다. 이 함수가 호출된 이후에 장치로부터 데이터를 읽을 수 있으면 콜백 함수가 불린다.

**매개 변수**

- `fd` - [in] I/O 장치 식별자
- `cb` - [in] 콜백 함수
- `param` - [in] 콜백 함수가 불릴 때 전달되는 값

**반환 값**

성공

실패

- `M_E_BADFD` - 잘못된 식별자
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevSetWriteCB

**프로토타입**

```c
M_Int32 MC_ioDevSetWriteCB(M_Int32 fd, DEVWRITECB cb, void *param)
```

**설명**

Non-blocking I/O 장치의 경우 해당 장치를 통해서 데이터를 전송할 수 있는 시점에 서 불리는 콜백 함수를 등록한다. 콜백 함수가 불리면 매개 변수 param값이 콜백 함 수 API로 전달된다. 등록하는 콜백 함수가 NULL일 경우 이전에 이 함수로 등록된 콜백 함수가 삭제된다. 이 함수가 에러를 반환하면 콜백 함수는 불리지 않는다. 이 함수가 호출된 이후에 장치가 데이터를 전송할 수 있으면 콜백 함수가 불린다.

**매개 변수**

- `fd` - [in] I/O 장치 식별자
- `cb` - [in] 콜백 함수
- `param` - [in] 콜백 함수가 불릴 때 전달되는 값

**반환 값**

성공

실패

- `M_E_BADFD` - 잘못된 식별자
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevControl

**프로토타입**

```c
M_Int32 MC_ioDevControl(M_Int32 fd, M_Char *cmd, void *param1, void *param2)
```

**설명**

장치에 주어진 command에 따라 해당하는 오퍼레이션을 수행한다.

**매개 변수**

- `fd` - [in] 장치 식별자
- `cmd` - [in] 장치에 수행할 오퍼레이션의 종류를 나타내는 문자열
- `param1` - [in/out] 장치의 해당 오퍼레이션에 넘겨줄 매개 변수 또는 오퍼레이션의 결과값을 저장할 버퍼 포인터
- `param2` - [in/out] 장치의 해당 오퍼레이션에 넘겨줄 매개 변수 또는 오퍼레이션의 결과값을 저장할 버퍼 포인터

**반환 값**

성공

실패

- `M_E_BADFD` - 유효하지 않은 식별자
- `M_E_INVALID` - 유효하지 않은 커맨드
- `M_E_ERROR` - command 수행에 실패했을 경우

**부작용**

없음

**참고 항목**

없음 가 IrDA 제어

### MC_ioDevOpen

**프로토타입**

```c
M_Int32 MC_ioDevOpen(M_Char *devname, M_Uint16 devnum, void *param)
```

**설명**

IrDA 장치를 초기화한다. IrDA 장치가 서버 모드로 동작할지, 클라이언트 모드로 동작할지를 설정한다. 서버 모드일 경우 지정된 시간 동안 클라이언트로부터 응답 요청을 기다리며, 클라이언트 모드일 경우 지정된 시간 동안 서버를 탐색하고 서버가 존재하는 경우 연결을 시도 한다.

**매개 변수**

- `devname` - “IrDA”를 사용한다.
- `devnum` - 첫번째 장치는 0번이고 이후 순서대로 번호를 부여한다.
- `param` - 설정하려는 모드는 아래의 `MC_IrDAMode` 구조체를 이용하여 전달한다. 서버 모드일 경우에는 aszMode에 “Server”를, 클라이언트 모드일 경우에는 aszMode에 “Client”를 넣어 전달한다. nTime은 연결을 시도할 시간을 명시한다.
- `typedef` - struct `MC_IrDAMode` {
- `M_Char` - aszMode[`MC_IRDA_MODE_LEN`]; // 모드 지정
- `M_Uint32` - nTime; // 연결 시도 시간 } `MC_IrDAMode`;

**반환 값**

성공

장치 식별자
실패

- `M_E_NOTSUP` - IrDA를 지원하지 않는 경우
- `M_E_ISCONN` - 이미 해당 장치가 연결이 되어 있는 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevSetOpenCB

**프로토타입**

```c
M_Int32 MC_ioDevSetOpenCB(M_Int32 fd, DEVOPENCB cb, void *param)
```

**설명**

IrDA 장치로부터 발생하는 연결 성공 여부나 타임아웃, 연결 종료와 같은 이벤트를 전달받기 위해서는 `MC_ioDevSetOpenCB()` API를 사용하여 콜백 함수를 등록해 주어 야 한다. 콜백 함수의 매개 변수인 error 값에는 연결 성공 시에는 0이, 타임아웃이 된 경우에는 M_E_TIMEOUT이, 연결 종료 시에는 M_E_DEVCLOSE가 전달된다. IrDA 통신 중에 전화가 걸려오는 경우와 같이 OEM의 사정에 의해서 IrDA 통신이 중지될 경우에는 M_E_OEMERROR가 전달되며 그 외 에러 상황에서는 M_E_ERROR가 전달된다. M_E_DEVCLOSE를 전달 받으면 `MC_ioDevClose`()를 호 출하여 IrDA 장치를 닫아 주어야 한다.

**매개 변수**

- `fd` - I/O 장치 식별자
- `cb` - 콜백 함수
- `param` - 콜백 함수가 불릴 때 전달되는 값

**반환 값**

성공

실패

- `M_E_BADFD` - 유효하지 않은 fd 값
- `M_E_INVALID` - 매개 변수가 잘못되었을 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevClose

**프로토타입**

```c
M_Int32 MC_ioDevClose(M_Int32 fd)
```

**설명**

IrDA 장치 사용을 종료한다.

**매개 변수**

- `fd` - I/O 장치 식별자

**반환 값**

성공

장치 식별자
실패

- `M_E_BADFD` - 유효하지 않은 fd 값
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevRead

**프로토타입**

```c
M_Int32 MC_ioDevRead(M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**설명**

IrDA 장치를 통해 설정된 모드에 따라 데이터를 수신한다. 먼저 모드가 설정되어 있 어야 한다. 그렇지 않은 경우 M_E_ERROR를 반환한다. 데이터를 바로 수신할 수 없을 경우 M_E_WOULDBLOCK을 반환하고 이 경우 `MC_ioDevSetReadCB`()에 콜백 함수를 등록하여 데이터 수신이 가능하게 될 때 콜백 함수 내에서 다시 수신을 시도 한다.

**매개 변수**

- `fd` - 장치 식별자
- `buf` - 읽어 들일 데이터를 저장할 버퍼 포인터
- `len` - 읽어 들일 데이터를 저장할 버퍼의 크기

**반환 값**

성공

읽은 데이터 크기
실패

- `M_E_BADFD` - 유효하지 않은 fd 값
- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘못되었을 경우
- `M_E_WOULDBLOCK` - 데이터를 읽거나 쓸 수 없을 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevWrite

**프로토타입**

```c
M_Int32 MC_ioDevWrite(M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**설명**

IrDA 장치를 통해 설정된 모드에 따라 데이터를 송신한다. 먼저 모드가 설정되어 있 어야 한다. 그렇지 않은 경우 M_E_ERROR를 반환한다. 데이터를 바로 송신할 수 없을 경우 M_E_WOULDBLOCK을 반환하고 이 경우MC_ioDevSetWriteCB()에 콜백 함수를 등록하여 데이터 송신이 가능하게 될 때 콜백 함수 내에서 다시 송신을 시도 한다.

**매개 변수**

- `fd` - 장치 식별자
- `buf` - 읽어 들일 데이터를 저장할 버퍼 포인터
- `len` - 읽어 들일 데이터를 저장할 버퍼의 크기

**반환 값**

성공

쓰여진 데이터 크기
실패

- `M_E_BADFD` - 유효하지 않은 fd 값
- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘못되었을 경우
- `M_E_WOULDBLOCK` - 데이터를 읽거나 쓸 수 없을 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevControl

**프로토타입**

```c
M_Int32 MC_ioDevControl(M_Int32 fd, M_Char *cmd, void *param1, void *param2)
```

**설명**

IrDA 장치를 통한 OBEX 전송 방식을 설정한다. 설정할 수 있는 방식에는 OBEX PUT(0x82)과 OBEX GET(0x83)이 있다. “SETOPCODE”를 통해 설정된 OBEX 헤더 값은 다시 `MC_ioDevControl()` API를 통해 재설정하지 않는 한 해당 전송 방식을 그 대로 유지한다. IrDA장치를 open한 후 전송 방식을 별도로 설정하지 않고 바로 write 를 수행하는 경우, OBEX GET을 default 전송 방식으로 설정하여 OBEX header를 구 성한다.

**매개 변수**

- `fd` - I/O 장치 식별자
- `cmd` - “SETOPCODE”를 사용한다.
- `param1` - “SETMETHOD”를 사용한다.
- `param2` - OBEX PUT 방식인 경우에는 “OBEXPUT”을, OBEX GET 방식인 경우에는 “OBEXGET”을 사용한다.

**반환 값**

성공

실패

- `M_E_BADFD` - 유효하지 않은 식별자
- `M_E_INVALID` - 유효하지 않은 커맨드
- `M_E_ERROR` - command 수행에 실패했을 경우

**부작용**

없음

**참고 항목**

없음 나 1Chip 제어

### MC_ioDevOpen

**프로토타입**

```c
M_Int32 MC_ioDevOpen(M_Char *devname, M_Uint16 devnum, void *param)
```

**설명**

1Chip Card를 활성화시킨다. param에 장치 리셋에 대한 응답(Answer To Reset, ATR) 을 받기 위한 버퍼와 버퍼의 길이를 전달한다.

**매개 변수**

- `devname` - “1ChipCard”를 사용한다.
- `devnum` - 첫번째 장치는 0번이고 이후 순서대로 번호를 부여한다.
- `param` - IC Card 활성화 시 전달되는 파라미터는 MC_CardOption을 이용하여 전달한다. 어플리케이션은 bATR에 버퍼를 할당하고 버퍼의 크기를 wATRLen을 통해 넘기면, bATR과 wATRLen에 응답값과 응답의 길이를 반환한다. 만약 넘긴 버퍼의 크기가 실제 응답값보다 작다면 wATRLen에 OxFFFF과 M_E_ERROR를 반환한다.
- `typedef` - struct `MC_CardOption` {
- `M_Byte` - *bATR; // ATR data pointer
- `M_Uint16` - wATRLen; // ATR data length } `MC_CardOption`

**반환 값**

성공

장치 식별자
실패

- `M_E_NODEVICE` - 카드가 삽입되어 있지 않은 경우
- `M_E_BADFORMAT` - 전송 데이터 format이 잘못된 경우
- `M_E_INVALID` - 매개 변수가 잘못된 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevClose

**프로토타입**

```c
M_Int32 MC_ioDevClose(M_Int32 fd)
```

**설명**

1Chip Card를 비활성화 시킨다.

**매개 변수**

- `fd` - I/O 장치 식별자

**반환 값**

성공

장치 식별자
실패

- `M_E_NODEVICE` - 카드가 삽입되어 있지 않은 경우
- `M_E_BADFD` - 유효하지 않은 식별자
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevRead

**프로토타입**

```c
M_Int32 MC_ioDevRead(M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**설명**

Card를 통해 데이터를 수신한다.

**매개 변수**

- `fd` - 장치 식별자
- `buf` - 읽어 들일 데이터를 저장할 버퍼 포인터
- `len` - 읽어 들일 데이터를 저장할 버퍼의 크기

**반환 값**

성공

읽은 데이터 크기
실패

- `M_E_NODEVICE` - 카드가 삽입되어 있지 않은 경우
- `M_E_BADFD` - 유효하지 않은 fd 값
- `M_E_NOTACTIVE` - 카드가 활성화가 안된 경우
- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘못되었을 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevWrite

**프로토타입**

```c
M_Int32 MC_ioDevWrite(M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**설명**

Card를 통해 데이터를 송신한다.

**매개 변수**

- `fd` - 장치 식별자
- `buf` - 읽어 들일 데이터를 저장할 버퍼 포인터
- `len` - 읽어 들일 데이터를 저장할 버퍼의 크기

**반환 값**

성공

쓰여진 데이터 크기
실패

- `M_E_BADFD` - 유효하지 않은 fd 값
- `M_E_NODEVICE` - 카드가 삽입되어 있지 않은 경우
- `M_E_BADFORMAT` - 전송 데이터 format이 잘못된 경우
- `M_E_NOTACTIVE` - 카드가 활성화가 안된 경우
- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘못되었을 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevControl

**프로토타입**

```c
M_Int32 MC_ioDevControl(M_Int32 fd, M_Char *cmd, void *param1, void *param2)
```

**설명**

IC Card의 삽입 여부를 검사한다.

**매개 변수**

- `fd` - I/O 장치 식별자
- `cmd` - “GETSTATUS”를 사용한다.
- `param1` - 문자열을 저장할 버퍼를 할당하여 전달한다. 반환되는 값은 “exist”, “noexist” 중에 하나이다.
- `param2` - 버퍼의 크기를 정수값으로 전달한다.

**반환 값**

성공

실패

- `M_E_BADFD` - 유효하지 않은 식별자
- `M_E_INVALID` - 매개 변수가 잘못된 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_ioDevControl

**프로토타입**

```c
M_Int32 MC_ioDevControl(M_Int32 fd, M_Char *cmd, void *param1, void *param2)
```

**설명**

WCDMA 단말기에 한해서 사용되며, 현재 할당된 UICC의 논리적인 채널 번호를 얻 어온다.

**매개 변수**

- `fd` - I/O 장치 식별자
- `cmd` - “GETCHANNEL”을 사용한다.
- `param1` - 정수형 포인터를 전달한다. 현재 할당된 UICC의 논리적인 채널 번호를 반환한다
- `param2` - `NULL`

**반환 값**

성공

실패

- `M_E_BADFD` - 유효하지 않은 식별자
- `M_E_INVALID` - 매개 변수가 잘못된 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음
