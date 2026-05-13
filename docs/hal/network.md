# 4.6. 네트워크

TCP/IP 인터넷 통신을 지원하는 함수들을 정의한 것이다.

플랫폼은 TCP/IP 인터넷 통신을 위해 단일한 네트웍 인터페이스를 지원한다. 플 랫폼은 MH_netConnect() 함수를 호출하여 인터넷 사용이 가능해 진 후부터 소켓 관련 API 를 통해 인터넷으로 데이터 통신이 가능하게 해야 한다. 플랫폼이 MH_netClose() 를 호출한 이후에는 어떠한 소켓 API 를 통해서도 인터넷을 통한 데이터 통신이 불가능하도록 해야 한다. 플랫폼은 MH_netClose() 가 불릴 때 네 트웍을 사용하는 소켓이 모두 종료되어 있어야 함을 권고한다.

네트웍의 특성상 네트워크 API 를 호출한 후 상당시간 블로킹(blocking)할 경우에 그 시간 동안 플랫폼이 정지하는 현상이 발생 할 수 있으므로, 네트워크 API 는 MH_netClose() 와 MH_netSocketClose() 를 제외하고 모두 논블로킹(NonBlocking) 함수로 구현 되어야 한다. MH_netClose() 와 MH_netSocketClose() 가 블로킹 이 라 함은 이 함수를 호출한 후에 이 함수호출에 관련한 이벤트가 플랫폼에 전달되 지 않는다는 것을 의미한다.

네트웍 API 를 호출하고 I/O 이벤트가 발생하면 이 이벤트 관련 정보가 플랫폼에 전달되어야 하는데 이때 호출하는 함수는 MH_pltEvent() 이며 매개변수로 MH_NETWORK_EVENT와 MH_NetEvent 타입의 데이터가 전달된다

- 관련 자료형
```c
//인터넷 도메인임을 가르키는 상수. 값은 2
#define MH_AF_INET 2
//TCP/UDP 소켓을 구분하는 상수
typedef enum MH_SOCKET_TYPE{
MH_SOCKET_STREAM =1, // TCP SOCKET
MH_SOCKET_DGRAM // UDP SOCKET
} MH_SOCKET_TYPE;
//네트웍 이벤트
typedef enum MH_SUB_NETWORK_EVENT {
MH_NETEV_NETWORK_OPEN = 0x01, // 네트웍 연결 이벤트
MH_NETEV_NETWORK_CLOSE = 0x02, // 네트웍 종료 이벤트
MH_NETEV_SOCKET_CONNECT = 0x04, // SOCKET 연결이벤트
MH_NETEV_SOCKET_CLOSE = 0x08, // SOCKET 종료 이벤트
MH_NETEV_SOCKET_READ = 0x10, // SOCKET READ 이벤트
MH_NETEV_SOCKET_WRITE = 0x20, // SOCKET WRITE 이벤트
} MH_SUB_NETWORK_EVENT;
//네트웍 이벤트를 전달하는 구조체
typedef struct MH_NetEvent{
M_Int32 fd; // 소켓 식별자
M_Int32 event; //발생된 event, MH_SUB_NETWORK_EVENT
값
} MH_NetEvent;
```

### MH_netConnect

**설명**

인터넷 접근을 시도한다. 반환 값이 M_E_WOULDBLOCK 일 경우에는 논블로킹 (NonBlocking)으로 인터넷 접근이 가능하게 되었다는 것을 의미한다. 인터넷 접근 이 가능하게 되었을 경우는 MH_NETEV_NETWORK_OPEN 이벤트를 플랫폼에 전달해야 한다.어떠한 이유로든 인터넷 접근이 불가능하게 되면 MH_NETEV_NETWORK_CLOSE 이 벤트를 플랫폼으로 전달 해야 한다.

**프로토타입**

```c
M_Int32 MH_netConnect (void)
```

**매개 변수**

없음

**반환 값**

성공 실패 M_E_WOULDBLOCK –인터넷 접근이 가능하게 될 때까지 기다릴 필요가 있을 경우 M_E_INPROGRESS –인터넷 접근 시도 중인 경우 M_E_ISCONN –이미 인터넷 접근이 가능하게 되어 있는 경우 M_E_ERROR - 인터넷 접근 종료 중이거나 기타 이유로 실패할 경우

**부작용**

없음.

**참고 항목**

없음

### MH_netClose

**설명**

인터넷 접근을 종료 한다. 이 함수는 블로킹(blocking)함수이다. 인터넷 접근이 허용되지 않은 상태에서도 이 함수는 성공을 리턴한다. 운영체제는 플랫폼이 MH_netClose() 를 호출한 이후에는 어떠한 소켓 API 를 통해서도 인터넷을 통한 데이터 통신이 불가능하도록 해야 한다. 플랫폼은 MH_netClose() 가 불릴 때 네트 웍을 사용하는 소켓이 모두 종료되어 있는 것을 권고한다.

**프로토타입**

```c
M_Int32 MH_netClose (void)
```

**매개 변수**

없음

**반환 값**

성공 실패 M_E_INPROGRESS - 인터넷 접근 종료 중인 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음.

**참고 항목**

없음

### MH_netSocket

**설명**

소켓을 얻어 온다. 이 함수가 리턴하는 소켓 식별자는 음수가 될 수 없다.

**프로토타입**

```c
M_Int32 MH_netSocket (M_Int32 domain, M_Int32 type)
```

**매개 변수**

[in] domain 인터넷 도메인일 경우 MH_AF_INET [in] type MH_SOCKET_STREAM(TCP 소켓), MH_SOCKET_DGRAM(UDP 소

```c
켓);
```

**반환 값**

성공 소켓 식별자 실패 M_E_NOTSUP – domain 혹은 type 을 지원하지 않는 경우 M_E_NOTCONN– 인터넷 접근이 불가능한 경우.

M_E_NOSPACE– 소켓의 최대 할당 개수를 초과하여 더 이상 할당할 수 없 는 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_netSocketConnect

**설명**

TCP 소켓을 서버에 연결 한다. 반환 값이 M_E_WOULDBLOCK 일 경우에는 논블로킹 (NonBlocking)으로 소켓이 연결된다는 것을 의미하며, 소켓이 연결되었을 경우, MH_NETEV_SOCKET_CONNECT 이벤트를 플랫폼에 전달해야 한다

**프로토타입**

```c
M_Int32 MH_netSocketConnect (M_Int32 fd, M_Int32 addr, M_int16 port)
```

**매개 변수**

[in] fd 소켓 식별자 [in] addr 상대방 IP 주소로 네트웍 바이트 순서(network byte ordering)이 다.

[in] port 상대방 포트 번호로 네트웍 바이트 순서(network byte ordering) 이다

**반환 값**

성공 실패 M_E_INVALID – 주소가 0 인 경우 M_E_WODULDBLOCK – 소켓 연결이 설정될 때까지 기다려야 될 경우 M_E_NOTCONN - 인터넷 접근이 불가능해 진 경우 M_E_ISCONN - 이미 CONNECT되어 있는 경우 M_E_INPROGRESS - 서버와 연결시도 중인 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_netSocketRead

**설명**

TCP 를 통해 데이터를읽는다. 반환 값이 0 이라면 EOF(End Of File)를 의미 한다.

반환 값이 M_E_WOULDBLOCK 일 경우에는 읽어 들일 데이터가 없다는 것을 의미한 다. 이 경우 데이터를 읽을 수 있는 시점에서 MH_NETEV_SOCKET_READ 이벤트가 플 랫폼에 전달되어야 한다.

**프로토타입**

```c
M_Int32 MH_netSocketRead (M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**매개 변수**

[in] fd 소켓 식별자 [out] buf 데이터의 버퍼 포인터 [in] len 읽고자 하는 버퍼 크기

**반환 값**

성공 읽혀진 데이터 길이 실패 M_E_WOULDBLOCK – 읽어 들일 데이터가 없는 경우 M_E_NOTCONN– 소켓이 연결되지 않은 경우거나 인터넷 접근이 불가능해진 경우.

M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_netSocketWrite

**설명**

TCP 소켓을 통해 데이터를 보낸다. 반환 값이 M_E_WOULDBLOCK 일 경우에는 시스템 내부요인으로 지금 당장 데이터를 전송할 수 없다는 것을 의미한다. 이 경우 데이 터를 전송할 수 있는 시점에서 MH_NETEV_SOCKET_WRITE 이벤트가 플랫폼에 전달되 어야 한다.

**프로토타입**

```c
M_Int32 MH_netSocketWrite (M_Int32 fd, M_Byte *buf, M_Int32 len)
```

**매개 변수**

[in] fd 소켓 식별자 [in] buf 데이터의 버퍼 포인터 [in] len 데이터의 size

**반환 값**

성공 전송한 길이 실패 M_E_WODULDBLOCK –시스템 내부 요인으로 지금 당장 데이터를 전송할 수 없는 경우 M_E_NOTCONN - 소켓이 연결되지 않은 경우나인터넷 접근이 불가능해진 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_netSocketBind

**설명**

소켓에 local port를 지정한다.

**프로토타입**

```c
M_Int32 MH_netSocketBind (M_Int32 fd, M_Int16 port)
```

**매개 변수**

[in] fd 소켓 식별자 [in] port 로컬 포트번호로 네트웍 바이트 순서(network byte ordering)이 다

**반환 값**

성공 실패 M_E_INVALID - 주소나 포트가 잘 못된 경우 M_E_ISCONN - 이미 포트가 지정되어 있는 경우 M_E_NOTCONN –인터넷 연결이 불가능해진 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_netSocketSendTo

**설명**

UDP 소켓을 통해 data 를 전송한다. 반환 값이 M_E_WOULDBLOCK 일 경우에는 시스 템 내부 요인으로 지금 당장 전송할 수 없다는 것을 의미한다. 이 경우 데이터를 전송할 수 있는 시점에서 MH_NETEV_SOCKET_WRITE 이벤트가 플랫폼에 전달되어야 한다.

**프로토타입**

```c
M_Int32 MH_netSocketSendTo (
M_Int32 fd,
M_Byte *buf,
M_Int32 len,
M_Int32 addr,
M_Int16 port,
)
```

**매개 변수**

[in] fd 소켓 식별자 값 [in] buf 데이터의 버퍼 포인터 [in] len 데이터의 size [in] addr 상대방 IP 주소. 네트웍 바이트 순서(network byte ordering) [in] port 상대방 포트번호. 네트웍 바이트 순서(network byte ordering)

**반환 값**

성공 전송한 데이터 길이 실패 M_E_WOULDBLOCK – 전송할 수 있을 때 까지 기다려야 하는 경우 M_E_NOTCONN –인터넷 접근이 불가능한 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_netSocketRcvFrom

**설명**

UDP 소켓을 통해 데이터를 수신한다.반환 값이 M_E_WOULDBLOCK 일 경우에는 읽어 들일 데이터가 없다는 것을 의미한다. 이 경우 데이터를 읽을 수 있는 시점에서 MH_NETEV_SOCKET_READ 이벤트가 플랫폼에 전달되어야 한다.

**프로토타입**

```c
M_Int32 MH_netSocketRcvFrom (
M_Int32 fd,
M_Byte *buf,
M_Int32 len,
M_Int32 *addr,
M_Int16 *port
)
```

**매개 변수**

[in] fd - 소켓 식별자 값 [out] buf - 데이터의 버퍼 포인터 [in] len - 데이터의 size [out] addr 상대방 IP 주소. 네트웍 바이트 순서(network byte ordering) [out] port 상대방 포트번호. 네트웍 바이트 순서(network byte ordering)

**반환 값**

성공 수신된 데이터 길이 실패 M_E_WOULDBLOCK – 읽어 들일 데이터가 없는 경우 M_E_NOTCONN –인터넷 접근이 불가능한 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_netSocketClose

**설명**

소켓을 종료한다. 이 함수는 블로킹(blocking)함수이다.

**프로토타입**

```c
M_Int32 MH_netSocketClose (M_Int32 fd)
```

**매개 변수**

[in] fd 소켓 식별자값

**반환 값**

성공 실패 M_E_INPROGRESS – 이미 종료 중인 경우 M_E_NOTCONN –인터넷 접근이 불가능한 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_netGetMaxPacketLength

**설명**

송수신할 수 있는 UDP 패킷의 최대 길이를 얻어 온다.

**프로토타입**

```c
M_Int32 MH_netGetMaxPacketLength (void)
```

**매개 변수**

없음

**반환 값**

패킷길이

**부작용**

없음

**참고 항목**

없음

### MH_netSocketAccept

**설명**

TCP 서버 소켓이 클라이언트와 연결된 소켓을 리턴한다. 이 함수가 불리기 전에 MH_netSocketBind() 로 로컬 포트를 지정해야 한다. 이 함수가 M_E_WOULDBLOCK 을 리턴하면 나중에 클라이언트와 연결된 소켓이 생길 경우 운영체제는 플랫폼에 MH_NETEV_SOCKET_CONNECT 이벤트를 전달해야 한다. 이 함수 지원은 플랫폼 구현의 선택사항이다.

**프로토타입**

```c
M_Int32 MH_netSocketAccept (M_Int32 fd)
```

**매개 변수**

- `fd` — TCP 서버소켓 식별자
**반환 값**

성공 클라이언트와 연결된 소켓 식별자 실패 M_E_WOULDBLOCK – 클라이언트와 연결될 때 까지 기다려야 할 경우 M_E_NOTSUP – 플랫폼이 이 함수를 지원하지 않거나 이 함수를 지원하지 않는 소켓일 경우 M_E_NOTCONN –인터넷 접근이 불가능한 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음
