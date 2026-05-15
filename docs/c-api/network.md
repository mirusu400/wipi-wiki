# 5.1.5. NETWORK

TCP/IP 인터넷 통신에 관련된 모듈이다. 인터넷 접근, TCP/UDP 소켓, HTTP 연결에 관련된 API 들이 포함된다.

모든 네트웍 I/O 관련 API 는 넌블로킹(nonblocking)이며 I/O 상에서 발생하는 이벤트를 받기위해서는 콜백함수를 등록해야한다.

어플리케이션은 `MC_netConnect()` 를 호출하여 인터넷 접근이 허용된 후부터 모든 소켓 관련 API 를 통해 데이터 통신이 가능해 진다. `MC_netSocketClose()` 를 통해 인터넷 접근이 종료된 이후에는 모든 소켓 API 가 `M_E_NOTCONN` 에러를 리턴하며, 소켓에 등록된 모든 콜백 함수는 삭제되어 불리지 않게 된다. `MC_netConnect()` 를 통한 인터넷 접근은 어플리케이션 단위로 이루어져야 하며 한 어플리케이션의 인터넷 접근은 다른 어플리케이션에 영향을 주지 않는다. 예를 들어 한 어플리케이션에서 `MC_netConnect()` 로 인터넷에 접근이 가능해 진다 하더라도 다른 어플리케 이션에서 인터넷연결을 하려면 `MC_netConnect()` 을 호출하여 인터넷 접근을 시도 해야한다.

플랫폼은 TCP 와 UDP 소켓을 지원한다. TCP 서버소켓 지원은 선택사항이며 클라이 언트 기능은 필수사항이다. TCP 소켓과 UDP 소켓은 동시에 여러개를 지원할 수 있 지만 동시에 지원할 수 있는 개수는 해당 플랫폼마다 다르다. 만일 `MC_netSocket()` 이 `M_E_NOSPACE` 를 리턴하면 더이상 소켓을 열 수 없다는 뜻이다. `MC_netClose()` 함수를 호출하여 인터넷 접근을 종료하면 응용프로그램에서 네트웍 API 로 등록한 모든 콜백함수는 호출되지 않으며 플랫폼은 응용프로그램에서 생성 한 모든 소켓을 종료한다.

**참고 항목**

없음

### MC_AF_INET

**프로토타입**

```c
#define MC_AF_INET 2
```

**설명**

인터넷 도메인임을 가르키는 상수로 값은 2 이다.

### MC_SOCKET_STREAM

**프로토타입**

```c
#define MC_SOCKET_STREAM 1
```

**설명**

TCP 소켓 타입을 지정하는 값으로 1 이다

### MC_SOCKET_DGRAM

**프로토타입**

```c
#define MC_SOCKET_DGRAM 2
```

**설명**

UDP 소켓 타입을 지정하는 값으로 2 이다

### NETCONNECTCB

**설명**

함수 `MC_netConnect` 에 등록하는 콜백함수.

**프로토타입**

```c
typedef void (*NETCONNECTCB)(M_Int32 error, void *param)
```

**매개 변수**

- `error` - 성공: 0, 실패: `M_E_ERROR`
- `param` - `MC_netConnect()` 호출시에 넘겨주는 콜백 매개변수

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MC_netConnect`

### NETSOCKCONNECTCB

**설명**

함수 MC_netConnect 에 등록하는 콜백함수

**프로토타입**

```c
typedef void (*NETSOCKCONNECTCB)(M_Int32 fd, M_Int32 error, void *param)
```

**매개 변수**

- `fd` - 소켓 식별자
- `error` - 0 : 성공, 실패: `M_E_ERROR`
- `param` - `MC_netSocketConnect()` 호출 시에 넘겨주눈 콜백 매개변수

**반환 값**

없음

**부작용**

없음

**참고 항목**


## MC_netSocketConnect

### NETSOCKACCEPTCB

**설명**

함수 `MC_netSocketAccept` 에 등록하는 콜백함수

**프로토타입**

```c
typedef void (*NETSOCKACCEPTCB)(M_Int32 sd, M_Int32 fd, M_Int32 error, void *param)
```

**매개 변수**

- `sd` - 서버소켓 식별자
- `fd` - 클라이언트와 연결된 소켓 식별자 error – 0 : 성공, 실패: M_E_ERROR
- `param` - `MC_netSocketAccept()` 호출 시에 넘겨주는 콜백 매개변수

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MC_netSocketAccept`

### NETSOCKREADCB

**설명**

함수 `MC_netSetReadCB` 에 등록하는 콜백함수

**프로토타입**

```c
typedef void (*NETSOCKREADCB)(M_Int32 fd, M_Int32 error, void *param)
```

**매개 변수**

- `fd` - 소켓 식별자
- `error` - 0 : 성공, 실패: `M_E_ERROR`
- `param` - `MC_netSetReadCB()` 호출시 넘겨주는 콜백 매개변수

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MC_netSetReadCB`

### NETSOCKWRITECB

**설명**

함수 `MC_netSetWriteCB` 에 등록하는 콜백함수

**프로토타입**

```c
typedef void (*NETSOCKWRITECB)(M_Int32 fd, M_Int32 error, void *param)
```

**매개 변수**

- `fd` - 소켓 식별자
- `error` - 성공: 0, 실패: `M_E_ERROR`
- `param` - `MC_netSetWriteCB()` 호출시 넘겨주는 콜백 매개변수

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MC_netSetWriteCB`

### NETHOSTADDRCB

**설명**

`MC_netGetHostAddr()` 로 등록하는 콜백함수. 성공하면 addr 로 -1 이 아닌 IP 주소값이 전달된다. 이 주소값은 네트웍 바이트 순서(network byte ordering)이다.

**프로토타입**

```c
typedef void (*NETHOSTADDRCB)(M_Int32 addr, void *param)
```

**매개 변수**

- `addr` - IP 주소
- `param` - `MC_netGetHostAddr()` 호출 시에 넘겨주는 콜백 매개변수

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MC_netGetHostAddr`

### NETHTTPCB

**설명**

`MC_netHttpConnect()` 에 등록하는 콜백함수. 이 함수는 HTTP 서버로 부터 응답을 받거나 통신상의 에러가 발생하면 불리는 콜백함수이다. 서버로부터 응답을 받을 받았을 경우 서버응답 중 HTTP 헤더 필드 부분의 파싱(parsing)이 끝나는 시점이 이 함수가 불리는 시점이다. 따라서 이 함수가 불린 이후에야 다음 함수들이 정상적으로 동작한다.

```c
MC_netHttpGetResponseCode(), MC_netHttpGetResponseMessage(), MC_netHttpGetHeaderField(), MC_netHttpGetLength(), MC_netHttpGetType(), MC_netHttpGetEncoding()
```

또한 서버가 전송하는 컨텐츠는 이 함수로 전달되는 매개변수 sd 소켓 식별자를 통해서 읽을 수 있다. 서버가 전송하는 컨텐츠가 없을 경우 이 소켓 식별자는 -1 이 전달된다. 이 소켓 식별자가 -1 이 아닐 경우 소켓은 이미 서버와 연결된 상태이므로 `MC_netSocketConnect()` 를 호출할 필요가 없다. `MC_netHttpClose()` 가 불리면 앞에서 언급한 소켓 식별자가 무의미 해지며 이 소켓을 통한 모든 I/O 가 시 도가 실패로 돌아 간다. 이 함수로 전달되는 error 가 `M_E_ERROR` 일 경우 통신상 의 문제가 발생한 것으로 위에 열거한 함수들은 모두 `M_E_ERROR` 를 리턴한다.

**프로토타입**

```c
typedef  void  (*NETHTTPCB)(M_Int32 fd,  M_Int32 sd, M_Int32 error, void *param)
```

**매개 변수**

- `fd` - HTTP 식별자 sd – 소켓 식별자
- `error` - 성공: 0, 실패: `M_E_ERROR`
- `param` - `MC_netHttpConnect()` 호출시에 넘겨주는 콜백 매개변수

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netConnect

**설명**

인터넷 접근을 시도한다.

소켓을 사용하기 전에 이 함수가 불려 인터넷 접근이 가능해 져야만 소켓을 통한 TCP/IP 통신이 가능해 진다. 이 함수는 어플리케이션 별로 불려야 하는 함수다. 즉 다른 어플리케이션이 이 함수를 호출하여 인터넷 접근이 허용되어 있다 하더라 도 현재 어플리케이션이 이 함수를 호출하지 않으면 소켓을 사용할 수 없다. 이 함수가 0 을 리턴할 경우 등록하는 콜백함수를 통해 연결이 성공했는지 실패했는 지 여부를 알려준다. 이 함수를 사용하는 어플리케이션이 이미 함수를 호출하였거 나 다른 어플리케이션에서 인터넷 접근을 시도 중일 경우 `M_E_INPROGRESS` 를 리턴 하며, 이 함수를 호출하는 어플리케이션을 위한 인터넷 접근이 이미 허용되어 있 으면 에러 값 `M_E_ISCONN` 이 리턴된다. 이 함수가 에러 값을 리턴할 경우에는 이 함수로 등록하는 콜백이 불리지 않는다.

**프로토타입**

```c
M_Int32 MC_net Connect(NETCONNECTCB cb, void *param)
```

**매개 변수**

- `cb` - 접근에 성공하거나 실패할 경우 불려지는 콜백함수

**반환 값**

성공

- 0

실패

- `M_E_INPROGRESS` – 이 어플리케이션이 혹은 다른 어플리케이션이 인터넷 접근을 시도하고 있는 경우
- `M_E_ISCONN` – 이 어플리케이션이 이미 인터넷 접근이 허용된 경우
- `M_E_ERROR` – 기타 에러가 발생했을 경우

**부작용**

없음

**참고 항목**

없음

### MC_netClose

**설명**

인터넷 접근을 종료한다.

이 함수를 부르면 모든 인터넷 통신이 불가능하게 된다. 따라서 이 함수가 불릴 때 어플리케이션 내에 종료되지 않는 소켓이 존재한다면 자동으로 종료되며, `MC_netHttpOpen()` 으로 생성되는 HTTP 식별자도 종료된다. 더불어 네트웍 API 로 등록하는 모든 콜백함수는 호출되지 않는다. 또한 이 함수는 어플리케이션별로 불려지는 함수이어서 이 함수가 불리고 난 뒤에 소켓을 사용하는 다른 어플리케이션에 영향을 주지 않는다.

**프로토타입**

```c
void MC_netClose(void)
```

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MC_netSocket

**설명**

TCP 혹은 UDP 통신을 위한 소켓을 생성한다. 이 함수가 불리기 전에 먼저 `MC_netConnect()` 함수로 인터넷 접근에 성공해야 한다.

**프로토타입**

```c
M_Int32 MC_netSocket(M_Int32 domain, M_Int32 type)
```

**매개 변수**

- `domain` - 통신 도메인으로 인터넷 소켓일 경우 AF_INET 임
- `type` - `MC_SOCKET_STREAM` 혹은 `MC_SOCKET_DGRAM`

**반환 값**

성공

- 소켓 식별자

실패

- `M_E_NOTSUP` – domain 혹은 type 이 지원하지 않는 값을 경우
- `M_E_NOTCONN` - 인터넷 접근이 허용되지 않은 경우
- `M_E_NOSPACE` – 더 이상 소켓을 생성할 수 없을 경우
- `M_E_ERROR` – 기타 에러

**부작용**

없음

**참고 항목**

없음


### MC_netSocketConnect

**설명**

TCP 소켓으로 서버와 연결을 시도한다.

파라메타로 들어가는 IP 주소(addr) 과 포트번호(port) 는 네트웍 바이트 순서 (network byte ordering) 이어야 한다. 이 함수로 등록하는 콜백함수가 NULL 일 경우 이 함수는 `M_E_INVALID` 를 리턴하며 아무 역할도 하지 않는다. 이 함수가 0 을 리턴할 경우 콜백으로 등록된 함수가 불린다. 이 함수로 등록하는 콜백함수가 불리기 전에 `MC_netSocketClose()` 가 호출되면 콜백함수는 호출되지 않는다.

**프로토타입**

```c
M_Int32 MC_netSocketConnect(M_Int32 fd, M_Int32 addr, M_Int16 port, NETSOCKCONNECTCB cb, void *param)
```

**매개 변수**

- `fd` - 소켓 식별자
- `addr` - 서버의 주소
- `port` - 서버의 포트번호
- `cb` - 연결에 성공하거나 실패할 경우 불리는 콜백함수
- `param` – 콜백함수가 불릴 때 전달되는 값

**반환 값**

성공

- 0

실패

- `M_E_NOTSUP` – 이 함수를 지원하지 않는 소켓일 경우
- `M_E_BADFD` - 유효하지 않는 소켓 식별자
- `M_E_NOTCONN` - 인터넷 접근이 불가능한 경우
- `M_E_ISCONN` - 이미 연결되어 있는 경우
- `M_E_INPROGRESS` - 연결 작업이 이미 진행 중인
- `M_E_INVALID` – 주소가 잘 못된 경우나 콜백함수가 NULL 일 경우
- `M_E_ERROR` – 기타 에러

**부작용**

없음

**참고 항목**

`MC_netSocketClose`

### MC_netSocketWrite

**설명**

TCP 소켓으로 데이터를 보낸다.

이 함수가 `M_E_WOULDBLOCK` 을 리턴하면 시스템 내부 요인으로 지금 데이타를 전송 할 수 없다는 뜻이다. 이 경우 `MC_netSetWriteCB()` 로 등록한 콜백함수 내에서 다시 이 함수를 불러 데이터를 전송한다. 콜백내에서 부른 이 함수는 `M_E_WOULDBLOCK` 을 리턴할 수 있다.

**프로토타입**

```c
M_Int32 MC_netSocketWrite(M_Int32 fd, M_Byte* buf, M_Int32 len)
```

**매개 변수**

- `fd` - 소켓 식별자
- `buf` - 데이터의 버퍼
- `len` - 보낼 데이터의 길이

**반환 값**

성공

- 보낸 데이터 길이(0 이상의 값)

실패

- `M_E_WODULDBLOCK` - 시스템 내부요인으로 당장 데이터를 전송할 수 없는 경우
- `M_E_BADFD` - 유효하지 않는 소켓 식별자
- `M_E_NOTCONN` – 서버와 소켓 연결이 끊기거나 인터넷 접근이 불가능한 경우
- `M_E_INVALID` – 버퍼나 버퍼길이가 잘 못된 경우

**부작용**

없음

**참고 항목**

`MC_netSocketWriteNETSOCKWRITECB`


### MC_netSocketRead

**설명**

TCP 소켓을 통해 데이터를 읽어 온다.

이 함수가 `M_E_WOULDBLOCK` 을 리턴하면 시스템 내부 요인으로 지금 데이타를 읽을 수 없다는 뜻이다. 이 경우 `MC_netSetReadCB()` 로 등록하는 콜백함수 내에서 다시 이 함수를 불러 데이터를 읽는다. 콜백내에서 부른 이함수는 다시 `M_E_WOULDBLOCK` 을 리턴할 수 있다.

**프로토타입**

```c
M_Int32 MC_netSocketRead(M_Int32 fd, M_Byte* buf, M_Int32 len)
```

**매개 변수**

- `fd` - 소켓 식별자
- `buf` - 데이터의 버퍼
- `len` - 읽을 데이터의 길이

**반환 값**

성공

- 읽은 데이타 길이(0 이상의 값으로 0)

실패

- `M_E_WOULDBLOCK` - 데이터가 도착하지 않아 지금 읽을 수 없는 경우
- `M_E_NOTCONN` – 서버와 소켓 연결이 끊기거나 인터넷 접근이 불가능한 경우
- `M_E_BADFD` - 소켓 식별자가 유효하지 않은 경우
- `M_E_INVALID` – 버퍼나 버퍼길이가 잘못된 경우

**부작용**

없음

**참고 항목**

`MC_netSetReadCB`

### MC_netSocketClose

**설명**

소켓을 종료한다. 이 함수를 부르기 전에 `MC_netClose()` 을 불러 인터넷 접근을 종료한 경우에는 이미 소켓이 종료된 상태이지만 이 함수는 성공을 리턴한다. 이 함수가 불리면 소켓에 등록된 모든 콜백함수는 삭제되며 콜백은 불리지 않는다.

**프로토타입**

```c
M_Int32 MC_netSocketClose(M_Int32 fd)
```

**매개 변수**

`fd` - 소켓 식별자

**반환 값**

성공

- 0

실패

- `M_E_BADFD` - 유효하지 않은 소켓 식별자인 경우

**부작용**

없음

**참고 항목**

`MC_netClose`

### MC_netSocketBind

**설명**

특정 포트를 소켓에 지정한다.

**프로토타입**

```c
M_Int32 MC_netSocketBind(M_Int32 fd, M_Uint32 addr, M_Uint16 port)
```

**매개 변수**

- `fd` - 소켓 식별자
- `port` - 로컬 포트번호. 네트웍 바이트 순서(network byte ordering)이다.

**반환 값**

성공

- 0

실패

- `M_E_INVALID` - 이미 특정포트가 다른 소켓을 위해 지정되어 있는 경우
- `M_E_NOTCONN` - 인터넷 접근이 불가능한 경우
- `M_E_BADFD` - 유효하지 않은 소켓 식별자인 경우

**부작용**

없음

**참고 항목**

없음


### MC_netGetMaxPacketLength

**설명**

UDP 를 통해 보낼 수 있는 패킷의 최대길이를 리턴한다.

**프로토타입**

```c
M_Int32 MC_netGetMaxPacketLength(void)
```

**반환 값**

패킷의 최대 길이

**부작용**

없음

**참고 항목**

없음


### MC_netSocketSendTo 

**설명**

UDP 소켓을 통해 데이타를 보낸다.

전송하는 데이타 길이는 `MC_netGetMaxPacketLength()` 가 리턴하는 값을 초과할 수 없다. 파라메타로 들어가는 IP 주소(addr) 과 포트번호(port) 는 네트웍 바이트 순서 (network byte ordering) 이어야 한다. 이 함수가 `M_E_WOULDBLOCK` 을 리턴하 면 시스템 내부 요인으로 지금 데이타를 전송할 수 없다는 뜻이다. 이 경우 `MC_netSetWriteCB()`로 등록하는 콜백함수 내에서 다시 이 함수를 불러 데이터를 전송한다. 콜백내에서 부른 이함수는 다시 `M_E_WOULDBLOCK` 을 리턴할 수 있다.

**프로토타입**

```c
M_Int32 MC_netSocketSendTo(M_Int32 fd, M_Byte* buf, M_Int32 len, M_Uint32 addr, M_Uint16 port)
```

**매개 변수**

- `fd` - 소켓 식별자
- `buf` - 데이터의 버퍼
- `len` - 데이터의 길이
- `addr` - 상대방 IP 주소. 네트웍 바이트 순서(network byte ordering)이다.
- `port` - 상대방 포트번호. 네트웍 바이트 순서(network byte ordering)이다.

**반환 값**

성공

- 보낸 데이타 길이(0 이상의 값)

실패

- `M_E_NOTSUP` – 소켓이 이 함수를 지원하지 않는 경우
- `M_E_WODULDBLOCK` - 시스템 내부요인으로 지금 당장 데이터를 전송할 수 없는 경우
- `M_E_BADFD` - 유효하지 않는 소켓 식별자
- `M_E_NOTCONN` - 인터넷 접근이 불가능한 경우
- `M_E_INVALID` – 주소 혹은 버퍼나 버퍼 길이가 잘 못 된 경우

**부작용**

없음

**참고 항목**

`MC_netGetMaxPacketLength`, `MC_netSetWriteCB`

### MC_netSocketRcvFrom

**설명**

UDP 소켓을 통해 데이타를 읽어 온다.

데이타를 전송한 상대방의 IP 주소와 포트번호는 각각 addr 와 port 에 저장된다. 상대방의 IP 주소와 포트번호는 모두 네트웍 바이트 순서(network byte ordering) 이다. 이 함수가 `M_E_WOULDBLOCK` 을 리턴하면 시스템 내부 요인으로 지금 데이타를 읽을 수 없다는 뜻이다. 이 경우 `MC_netSetReadCB()` 로 등록하는 콜백함수 내에서 다시 이 함수를 불러 데이터를 읽는다. 콜백내에서 부른 이 함수는 다시 `M_E_WOULDBLOCK` 을 리턴할 수 있다.

**프로토타입**

```c
M_Int32 MC_netSocketRcvFrom(M_Int32 fd, M_Byte* buf, M_Int32 len, M_Uint32* addr, M_Uint16* port)
```

**매개 변수**

- `fd` - 소켓 식별자 buf - 데이터의 버퍼
- `len` - 읽을 데이터의 길이
- `addr` - 상대방 IP 주소가 저장될 버퍼. 네트웍 바이트 순서(network byte ordering)이다.
- `port` - 상대방 포트번호가 저장될 버퍼. 네트웍 바이트 순서(network byte ordering)이다.

**반환 값**

성공

- 읽은 데이타 길이(0 이상의 값)

실패

- `M_E_WODULDBLOCK` - 도착한 데이터가 없어 지금 당장 데이터를 읽을 수 없는 경우
- `M_E_BADFD` - 유효하지 않는 소켓 식별자
- `M_E_NOTCONN` - 인터넷 접근이 불가능한 경우
- `M_E_INVALID` – 데이터 버퍼나 버퍼길이 혹은 상대방 IP 와 포트가 저장될 버퍼가 잘못된 경우

**부작용**

없음

**참고 항목**

`MC_netSetReadCB`

### MC_netGetHostAddr

**설명**

네트웍 호스트이름에 해당하는 IP 주소를 얻는다. 이 함수가 에러를 리턴하는 경우를 제외하고 IP 주소를 얻었거나 실패한 경우에 등록한 콜백함수가 불린다. 매개변수 dnsserver 가 -1 일 경우 `MC_knlGetSystemProperty()` 함수가 리턴하는 도 메인 네임 서버에 접속하여 IP 주소를 구한다.

**프로토타입**

```c
M_Int32 MC_netGetHostAddr(M_Int32 dnsserver, M_Byte *hostname, NETHOSTADDRCB cb, void *param)
```

**매개 변수**

- `dnsserver` – 도메인 네임 서버 IP 주소
- `hostname` –호스트 이름
- `cb` – 호스트 이름에 해당하는 IP 주소를 얻게 되면 호출되는 콜백함수
- `param` – 콜백함수가 호출될 때 전달되는 매개변수

**반환 값**

성공

- 0

실패

- `M_E_INVALID` – 등록하는 콜백함수가 NULL 이거나 매개변수 dnsserver 가 0 혹은 매개변수 hostname 이 NULL 일 경우
- `M_E_ERROR` – 기타 에러

**부작용**

없음

**참고 항목**

`MC_knlGetSystemProperty`

### MC_netSocketAccept

**설명**

TCP 서버 소켓이 클라이언트와 연결된 소켓을 리턴한다. 이 함수가 불리기 전에 `MC_netSocketBind()` 로 로컬 포트를 지정해야 한다. 이 함수가 `M_E_WOULDBLOCK` 을 리턴하면 클라이언트와 연결된 소켓이 생기면 등록하는 콜백함수가 불린다. 이 함수가 `M_E_WOULDBLOCK` 이외의 에러 값을 리턴하면 이 함수는 역할도 하지 않는다.

**프로토타입**

```c
M_Int32 MC_netSocketAccept(M_Int32 fd. NETSOCKACCEPTCB cb, void *param)
```

**매개 변수**

- `fd` – TCP 서버 소켓 식별자
- `cb` – 콜백 함수
- `param` – 콜백함수가 호출될 때 전달되는 매개변수

**반환 값**

성공

- 클라이언트와 연결된 소켓 식별자

실패

- `M_E_INVALID` – 콜백함수가 NULL 일 경우
- `M_E_WOULDBLOCK` – 지금 클라이언트와 연결된 소켓이 없을 경우
- `M_E_NOTSUP` – 이 함수를 지원하지 않는 소켓일 경우
- `M_E_BADFD` – 잘못된 식별자일 경우
- `M_E_NOTCONN` – 인터넷 접근이 불가능한 경우
- `M_E_ERROR` - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MC_netSetReadCB

**설명**

소켓으로부터 데이터를 읽을 수 있는 시점에서 불리는 콜백함수를 지정한다. `MC_netSocketRead()` 나 `MC_netSocketRcvFrom()` 이 `M_E_WOULDBLOCK` 을 리턴할 경우 에만 이 함수로 등록된 콜백이 불린다. 여기서 지정하는 콜백함수는 한번만 불린다. 따라서 데이터를 읽을 수 있는 시점에서 콜백함수이 다시 불리게 하려면 다시 이 함수를 호출하여 콜백을 등록해야 한다. 또한 콜백함수가 불리기 전에 이 함수를 부르면 이전 콜백함수는 새로운 콜백함수로 대체된다. 만약 콜백함수가 NULL 이면 이전에 등록한 콜백함수를 제거하는 역할을 한다. 또한 이 함수가 호출되었 을 때 소켓으로부터 데이터를 읽을 수 있으면 콜백함수가 불린다.

**프로토타입**

```c
M_Int32 MC_netSetReadCB(M_Int32 fd, NETSOCKREADCB cb, void *param)
```

**매개 변수**

- `fd` - 소켓 식별자
- `cb` – 콜백함수
- `param` - 콜백함수가 불릴 때 전달되는 콜백 매개변수

**반환 값**

성공

- 0

실패

- `M_E_NOTCONN` –인터넷 접근이 불가능한 경우
- `M_E_BADF` - 소켓 식별자가 잘못 되었을 경우

**부작용**

없음

**참고 항목**

없음

### MC_netSetWriteCB

**설명**

소켓으로 데이터를 전송할 수 있는 시점에서 불리는 콜백함수를 지정한다. `MC_netSocketWrite()` 나 `MC_netSocketSendTo()` 가 `M_E_WOULDBLOCK` 을 리턴할 경우 에만 이 함수로 등록한 콜백이 불린다. 여기서 지정하는 콜백함수는 한번만 불린 다. 따라서 데이터를 전송할 수 있는 시점에서 콜백함수이 다시 불리게 하려면 다 시 이 함수를 호출하여 콜백을 등록해야 한다. 또한 콜백함수가 불리기 전에 이 함수를 부르면 이전 콜백함수는 새로운 콜백함수로 대체된다. 만약 콜백함수가 NULL 이면 이전에 등록한 콜백함수를 제거하는 역할을 한다. 또한 이 함수가 호출 되었을 때 소켓을 통해 데이터를 전송할 수 있으면 콜백함수가 불린다.

**프로토타입**

```c
M_Int32 MC_netSetWriteCB(M_Int32 fd, NETSOCKWRITECB cb, void *param)
```

**매개 변수**

- `fd` - 소켓 식별자
- `cb` – 콜백함수
- `param` - 콜백함수가 불릴 때 전달되는 콜백 매개변수

**반환 값**

성공

- 0

실패

- `M_E_NOTCONN` – 인터넷 접근이 불가능한 경우
- `M_E_BADF` - 소켓 식별자가 잘못 되었을 경우

**부작용**

없음

**참고 항목**

없음

### MC_netHttpOpen

**설명**

HTTP 식별자를 생성한다. 이 함수로 HTTP 연결 식별자를 생성한 후에 다음 함수 들을 호출하여 필요한 값들을 설정하거나 읽어온다. URL 문자열에 HTTP 서버의 IP 주소가 명시되어 있지 않으면 도메인 네임 서버로부터 IP 주소를 구해오게된다. 이때 사용하는 도메인 네임 서버의 IP 주소는 MC_knlGetSystemProperty() 를 통해 얻을 수 있다.

```c
MC_netHttpSetRequestMethod(), MC_netHttpGetRequestMethod(), MC_netHttpSetRequestProperty(), MC_netHttpGetRequestProperty(), MC_netHttpSetProxy(), MC_netHttpGetProxy().
```

**프로토타입**

```c
M_Int32 MC_netHttpOpen(M_Byte* url)
```

**매개 변수**

- `url` - "http://" 로 시작하는 URL 문자열

**반환 값**

성공

- HTTP 식별자

실패

- `M_E_INVALID` – URL 문자열이 잘 못 된 경우
- `M_E_NOSPACE` - 더 이상 HTTP 식별자를 생성할 수 없을 때
- `M_E_NOTCONN` - 인터넷 접근이 허용되어 있지 않은 경우
- `M_E_ERROR` – 기타 에러


**부작용**

없음

**참고 항목**

`MC_knlGetSystemProperty`, `MC_netHttpSetRequestMethod`, `MC_netHttpGetRequestMethod`, `MC_netHttpSetRequestProperty`, `MC_netHttpGetRequestProperty`, `MC_netHttpSetProxy`, `MC_netHttpGetProxy`

### MC_netHttpConnect

**설명**

서버와 HTTP 연결을 시도한다. `MC_netHttpOpen()` 함수가 불려도 실제 서버와 HTTP 연결을 맺지 않고 이 함수가 불려야만 연결을 시도한다. 연결에 성공하거나 실패했을 경우 등록하는 콜백함수가 불린다. 이 함수가 불린 이후에는 다음 함수 들은 `M_E_ERROR` 를 리턴한다.

```c
MC_netHttpSetRequestMethod(), MC_netHttpGetRequestMethod(), MC_netHttpSetRequestProperty(), MC_netHttpGetRequestProperty(), MC_netHttpSetProxy(), MC_netHttpGetProxy().
```

**프로토타입**

```c
M_Int32 MC_netHttpConnect(M_Int32 fd, NETHTTPCB cb, void *param)
```

**매개 변수**

- `fd` - HTTP 연결 식별자
- `cb` – 콜백함수
- `param` - 콜백함수가 호출될 때 전달되는 매개변수

**반환 값**

성공

- 0

실패

- `M_E_BADFD` - 잘못된 식별자
- `M_E_NOTCONN` - 인터넷 접근이 불가능해진 경우
- `M_E_INPROGRESS` – HTTP 서버에 이미 연결 시도 중인 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpSetRequestMethod`, `MC_netHttpGetRequestMethod`, `MC_netHttpSetRequestProperty`, `MC_netHttpGetRequestProperty`, `MC_netHttpSetProxy`, `MC_netHttpGetProxy`

### MC_netHttpSetRequestMethod

**설명**

HTTP 요청 메쏘드(Request Method)를 설정한다. 요청 메쏘드는 "GET", "POST", "HEAD" 가 될 수 있다. 메쏘드가 "POST" 일 경우 전송할 메세지를 함께 명시해야 한다. 이 함수가 `MC_netHttpConnect()` 함수 이후에 불리면 `M_E_ERROR` 를 리턴한다.

**프로토타입**

```c
M_Int32 MC_netHttpSetRequestMethod(M_Int32 fd, M_Byte *method, M_Byte *msg, M_Int32 msglen)
```

**매개 변수**

- `fd` - HTTP 식별자
- `method` - 요청 메쏘드 문자열
- `msg` - 요청 메쏘드가 "POST" 일 경우 전송할 메시지
- `msglen` - 메세지 길이

**반환 값**

성공

- 0

실패

- `M_E_BADFD` - 잘 못된 식별
- `M_E_INVALID` - 인식할 수 없는 요청 메쏘드일 경우나 POST 메쏘드 설정시 잘 못된 메시지일 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpGetRequestMethod

**설명**

HTTP 요청 메쏘드(Request Method)를 복사해 온다. `MC_netHttpSetRequestMethod()` 로 요청 메쏘드를 설정하지 않았다면 디폴트로 "GET" 이 복사된다. 매개변수 buf 에 저장되는 요청 메쏘드 문자열의 마지막에는 NULL 문자가 포함되며 리턴하는 길이는 NULL 문자를 제외한 문자열의 길이다. 이 함수가 `MC_netHttpConnect()` 함수 이후에 불리면 `M_E_ERROR` 를 리턴한다.

**프로토타입**

```c
M_Int32 MC_netHttpGetRequestMethod(M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**매개 변수**

- `fd` - HTTP 식별자
- `buf` - 요청 메쏘드를 저장할 버퍼
- `len` - 버퍼의 길이

**반환 값**

성공

- 버퍼에 저장된 요청 메쏘드 문자열의 길이

실패

- `M_E_BADFD` - 잘 못된 식별자
- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘 못 된 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpSetRequestProperty

**설명**

HTTP 요청특성(Request Property)을 설정한다. 이 함수가 `MC_netHttpConnect()` 함수 이후에 불리면 `M_E_ERROR` 를 리턴한다

**프로토타입**

```c
M_Int32 MC_netHttpSetRequestProperty(M_Int32 fd, M_Byte *key, M_Byte *value)
```

**매개 변수**

- `fd` - HTTP 식별자
- `key` - 요청 특성 이름
- `value` - 특성 값

**반환 값**

성공

- 0

실패

- `M_E_BADFD` - 잘 못된 식별자
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpGetRequestProperty 

**설명**

HTTP 요청특성(Request Property) 을 복사해 온다. 요청 특성 이름에 해당하는 값이 설정되어 있지 않았거나 이 함수가 `MC_netHttpConnect()` 함수 이후에 불리면 `M_E_ERROR` 를 리턴한다.

**프로토타입**

```c
M_Int32 MC_netHttpGetRequestProperty(M_Int32 fd, M_Byte *key, M_Byte *buf, M_Int32 len)
```

**매개 변수**

- `fd` - HTTP 식별자
- `key` - 요청 특성 이름
- `buf` - 값이 저장될 버퍼
- `len` - 버퍼 길이

**반환 값**

성공

- 복사된 특성값의 길이

실패

- `M_E_BADFD` - 잘못된 식별자
- `M_E_INVALID` - 버퍼나 버퍼길이가 잘 못 된 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpSetProxy

**설명**

프락시를 설정한다. 이 함수가 `MC_netHttpConnect()` 함수 이후에 불리면 `M_E_ERROR` 를 리턴한다.

**프로토타입**

```c
M_Int32 MC_netHttpSetProxy(M_Int32 fd, M_Int32 proxyhost, M_Int16 proxyport)
```

**매개 변수**

- `fd` - HTTP 식별자
- `proxyhost` - 프락시 호스트 IP 주소. 값은 네트웍 바이트 순서(network byte ordering)이다.
- `proxyport` - 프락시 포트 번호. 값은 네트웍 바이트 순서(network byte ordering)이다

**반환 값**

성공

- 0

실패

- `M_E_BADFD` - 잘 못된 식별자
- `M_E_INVALID` – proxyhost 가 0 이거나 -1 일 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpGetProxy

**설명**

프락시 호스트와 포트를 복사해 온다. 프락시를 지정하지 않았거나 이 함수가 `MC_netHttpConnect()` 함수 이후에 불리면 `M_E_ERROR` 를 리턴한다

**프로토타입**

```c
M_Int32 MC_netHttpGetProxy(M_Int32 fd, M_Int32 *proxyhost, M_Int16 *proxyport)
```

**매개 변수**

- `fd` - HTTP 식별자
- `proxyhost` - 프락시 호스트 값이 저장될 버퍼. 값은 네트웍 바이트 순서(network byte ordering)로 저장된다.
- `proxyport` - 프락시 포트 번호 값이 저장될 버퍼. 값은 네트웍 바이트 순서 (network byte ordering)로 저장된다.

**반환 값**

성공

- 0

실패

- `M_E_BADFD` - 잘 못된 식별자
- `M_E_INVALID` - 매개변수 proxyhost 나 proxyport 가 NULL 일 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpGetResponseCode

**설명**

HTTP 서버의 응답코드를 리턴한다. 서버로 부터의 응답이 다음과 같을 때

```
HTTP/1.0 200 OK
HTTP/1.0 404 Not Found
```

응답 코드는 각각 200, 400 이 된다. 이 함수가 `MC_netHttpConnect()` 에서 설정하는 콜백함수가 불리기 전에 불리면 `M_E_ERROR` 를 리턴한다.

**프로토타입**

```c
M_Int32 MC_netHttpGetResponseCode(M_Int32 fd)
```

**매개 변수**

- `fd` - HTTP 식별자

**반환 값**

성공

- 응답코드

실패

- `M_E_BADFD` - 잘못된 식별자
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpGetResponseMessage

**설명**

HTTP 서버의 응답메세지를 복사해 온다. 서버로 부터의 응답이 다음과 같을 때

```
HTTP/1.0 200 OK
HTTP/1.0 404 Not Found
```

응답메세지는 "OK" 와 "Not Found" 가 된다. 이 함수가 `MC_netHttpConnect()` 에서 설정하는 콜백함수가 불리기 전에 불리면 `M_E_ERROR` 를 리턴한다.

**프로토타입**

```c
M_Int32 MC_netHttpGetResponseMessage(M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**매개 변수**

- `fd` - HTTP 식별자
- `buf` - 응답 메세지가 저장될 버퍼 len 버퍼 길이

**반환 값**

성공

- 복사된 메세지 길이

실패

- `M_E_BADFD` - 잘 못된 식별자
- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘 못 된 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpGetHeaderField

**설명**

HTTP 서버의 응답중 헤더 값을 복사해 온다. 이 함수가 `MC_netHttpConnect()` 에서 설정하는 콜백함수가 불리기 전에 불리면 `M_E_ERROR` 를 리턴한다.

**프로토타입**

```c
M_Int32 MC_netHttpGetHeaderField(M_Int32 fd, M_Byte *name, M_Byte *buf, M_Int32 len)
```

**매개 변수**

- `fd` - HTTP 식별자
- `name` - 헤더 이름
- `buf` - 헤더 값이 저장될 버퍼
- `len` - 버퍼 길이

**반환 값**

성공

- 복사된 헤더 값 길이

실패

- `M_E_BADFD` - 잘 못된 식별자
- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘 못 된 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpGetLength

**설명**

컨텐츠의 길이를 리턴한다. 이 함수가 `MC_netHttpConnect()` 에서 설정하는 콜백함 수가 불리기 전에 불리면 `M_E_ERROR` 를 리턴한다

**프로토타입**

```c
M_Int32 MC_netHttpGetLength(M_Int32 fd)
```

**매개 변수**

- `fd` - HTTP 식별자

**반환 값**

성공

- 컨텐츠 길이

실패

- `M_E_BADFD` - 잘 못된 식별자
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpGetType

**설명**

컨텐츠의 타입 문자열을 복사해 온다. 이 함수가 `MC_netHttpConnect()` 에서 설정 하는 콜백함수가 불리기 전에 불리면 `M_E_ERROR` 를 리턴한다.

**프로토타입**

```c
M_Int32 MC_netHttpGetType(M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**매개 변수**

- `fd` - HTTP 식별자
- `buf` - 컨텐츠 타입 문자열이 복사될 버퍼
- `len` - 버퍼 길이

**반환 값**

성공

- 복사된 컨텐츠 타임 문자열 길이

실패

- `M_E_BADFD` - 잘 못된 식별자
- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘 못 된 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpGetEncoding 설명

컨텐츠의 인코딩 문자열을 복사해 온다. 이 함수가 `MC_netHttpConnect()` 에서 설정하는 콜백함수가 불리기 전에 불리면 `M_E_ERROR` 를 리턴한다.

**프로토타입**

```c
M_Int32 MC_netHttpGetEncoding(M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**매개 변수**

- `fd` - HTTP 식별자
- `buf` - 컨텐츠 인코딩 문자열 복사될 버퍼
- `len` - 버퍼 길이

**반환 값**

성공

- 복사된 컨텐츠 인코딩 문자열 길이

실패

- `M_E_BADFD` - 잘 못된 식별자
- `M_E_INVALID` - 버퍼나 버퍼 길이가 잘 못 된 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

`MC_netHttpConnect`

### MC_netHttpClose

**설명**

HTTP 연결 식별자 사용을 종료한다. 이 함수가 `MC_netHttpConnect()` 에서 설정하는 콜백함수가 불리기 전에 불리면 콜백함수는 불리지 않는다.

**프로토타입**

```c
M_Int32 MC_netHttpClose(M_Int32 fd)
```

**매개 변수**

- `fd` - HTTP 식별자

**반환 값**

성공

- 0

실패

- `M_E_BADFD` – 잘 못된 식별자

**부작용**

없음

**참고 항목**

없음


