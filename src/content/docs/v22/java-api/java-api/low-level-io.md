---
title: "2.2.2. 저수준 입출력"
---

Interface HttpSocket public interface HttpSocket HTTP 연결에 관련된 소켓 인터페이스이다. 필드 상세 설명

#### HEAD

public static final java.lang.String HEAD HTTP Head 요청 메쏘드 이다. 값은 "HEAD" 이다.

#### GET

public static final java.lang.String GET HTTP Get 요청 메쏘드 이다. 값은 "GET" 이다.

#### POST

public static final java.lang.String POST HTTP Post 요청 메쏘드 이다. 값은 "POST" 이다.

#### TRACE

public static final java.lang.String TRACE HTTP Trace 요청 메쏘드 이다. 값은 "TRACE" 이다.

#### PUT

public static final java.lang.String PUT HTTP Put 요청 메쏘드 이다. 값은 "PUT" 이다.

#### DELETE

public static final java.lang.String DELETE HTTP Delete 요청 메쏘드 이다. 값은 "DELETE" 이다.

#### OPTIONS

public static final java.lang.String OPTIONS HTTP Options 요청 메쏘드 이다. 값은 "OPTIONS" 이다.

#### CONNECT

public static final java.lang.String CONNECT HTTP Connect 요청 메쏘드 이다. 값은 "CONNECT" 이다.

#### HTTP_OK

public static final int HTTP_OK 서버응답코드 OK 이다. 값은 200 이다.

#### HTTP_CREATED

public static final int HTTP_CREATED 서버응답코드 CREATED 이다. 값은 201 이다.

#### HTTP_ACCEPTED

public static final int HTTP_ACCEPTED 서버응답코드 ACCEPTED 이다. 값은 202 이다.

#### HTTP_NON_AUTHORITATIVE

public static final int HTTP_NON_AUTHORITATIVE 서버응답코드 NOT AUTHORITATIVE 이다. 값은 203 이다.

#### HTTP_NO_CONTENT

public static final int HTTP_NO_CONTENT 서버응답코드 NO CONTENT 이다. 값은 204 이다.

#### HTTP_RESET_CONTENT

public static final int HTTP_RESET_CONTENT 서버응답코드 RESET CONTENT 이다. 값은 205 이다.

#### HTTP_PARTIAL_CONTENT

public static final int HTTP_PARTIAL_CONTENT 서버응답코드 PARTIAL CONTENT 이다. 값은 206 이다.

#### HTTP_MULTIPLE_CHOICE

public static final int HTTP_MULTIPLE_CHOICE 서버응답코드 MULTIPLE CHOICE 이다. 값은 300 이다.

#### HTTP_MOVED_PERMANENTLY

public static final int HTTP_MOVED_PERMANENTLY 서버응답코드 MOVED PETMANENTLY 이다. 값은 301 이다.

#### HTTP_MOVED_TEMPORARILY

public static final int HTTP_MOVED_TEMPORARILY 서버응답코드 MOVED TEMPORARILY 이다. 값은 302 이다.

#### HTTP_SEE_OTHER

public static final int HTTP_SEE_OTHER 서버응답코드 SEE OTHER 이다. 값은 303 이다.

#### HTTP_NOT_MODIFIED

public static final int HTTP_NOT_MODIFIED 서버응답코드 NOT MODIFIED 이다. 값은 304 이다.

#### HTTP_USE_PROXY

public static final int HTTP_USE_PROXY 서버응답코드 USE PROXY 이다. 값은 305 이다.

#### HTTP_BAD_REQ

public static final int HTTP_BAD_REQ 서버응답코드 BAD REQUEST 이다. 값은 400 이다.

#### HTTP_UNAUTHORIZED

public static final int HTTP_UNAUTHORIZED 서버응답코드 UNAUTHORIZED 이다. 값은 401 이다.

#### HTTP_PAYMENT_REQUIRED

public static final int HTTP_PAYMENT_REQUIRED 서버응답코드 PAYMENT REQUIRED 이다. 값은 402 이다.

#### HTTP_FORBIDDEN

public static final int HTTP_FORBIDDEN 서버응답코드 FORBIDDEN 이다. 값은 403 이다.

#### HTTP_NOT_FOUND

public static final int HTTP_NOT_FOUND 서버응답코드 NOT FOUND 이다. 값은 404 이다.

#### HTTP_METHOD_NOT_ALLOWED

public static final int HTTP_METHOD_NOT_ALLOWED 서버응답코드 METHOD NOT ALLOWED 이다. 값은 405 이다.

#### HTTP_NOT_ACCEPTABLE

public static final int HTTP_NOT_ACCEPTABLE 서버응답코드 NOT ACCEPTABLE 이다. 값은 406 이다.

#### HTTP_PROXY_AUTHENTICATION_REQUIRED

public static final int HTTP_PROXY_AUTHENTICATION_REQUIRED 서버응답코드 PROXY AUTHENTICATION REQUITRED 이다. 값은 407 이다.

#### HTTP_REQ_TIMEOUT

public static final int HTTP_REQ_TIMEOUT 서버응답코드 REQUEST TIMEOUT 이다. 값은 408 이다.

#### HTTP_CONFLICT

public static final int HTTP_CONFLICT 서버응답코드 CONFLICT 이다. 값은 409 이다.

#### HTTP_GONE

public static final int HTTP_GONE 서버응답코드 GONE 이다. 값은 410 이다.

#### HTTP_LENGTH_REQUIRED

public static final int HTTP_LENGTH_REQUIRED 서버응답코드 LENGTH REQUIRED 이다. 값은 411 이다.

#### HTTP_PRECONDITION_FAILED

public static final int HTTP_PRECONDITION_FAILED 서버응답코드 PRECONDITION FAILED 이다. 값은 412 이다.

#### HTTP_ENTITY_TOO_LARGE

public static final int HTTP_ENTITY_TOO_LARGE 서버응답코드 TOO LARGE 이다. 값은 413 이다.

#### HTTP_REQ_TOO_LONG

public static final int HTTP_REQ_TOO_LONG 서버응답코드 REQUEST TOO LONG 이다. 값은 414 이다.

#### HTTP_UNSUPPORTED_TYPE

public static final int HTTP_UNSUPPORTED_TYPE 서버응답코드 UNSUPPORTED TYPE 이다. 값은 415 이다.

#### HTTP_REQ_RANGE

public static final int HTTP_REQ_RANGE 서버응답코드 REQUEST RANGE NOT SATISFIABLE이다. 값은 416 이다.

#### HTTP_EXPECT_FAIL

public static final int HTTP_EXPECT_FAIL 서버응답코드 EXPECTATION FAILED 이다. 값은 417 이다.

#### HTTP_SERVER_ERR

public static final int HTTP_SERVER_ERR 서버응답코드 INTERNAL SERVER ERROR 이다. 값은 500 이다.

#### HTTP_NOT_IMPL

public static final int HTTP_NOT_IMPL 서버응답코드 NOT IMPLEMENTED 이다. 값은 501 이다.

#### HTTP_BAD_GATEWAY

public static final int HTTP_BAD_GATEWAY 서버응답코드 BAD GATEWAY 이다. 값은 502 이다.

#### HTTP_UNAVAILABLE

public static final int HTTP_UNAVAILABLE 서버응답코드 UNAVAILABLE 이다. 값은 503 이다.

#### HTTP_GATEWAY_TIMEOUT

public static final int HTTP_GATEWAY_TIMEOUT 서버응답코드 GATEWAY TIMEOUT 이다. 값은 504 이다.

#### HTTP_VERSION

public static final int HTTP_VERSION 서버응답코드 VERSION NOT SUPPORTED 이다. 값은 505 이다. 메쏘드 상세 설명

#### close

public void close() throws java.io.IOException HTTP 소켓을 닫다. 이미 닫힌 소켓에 대해서는 아무런 액션을 취하지 않는다. Throws java.io.IOException 소켓을 닫는데 실패한 경우

#### getInputStream

public java.io.InputStream getInputStream() throws java.io.IOException InputStream 을 반환한다.

**반환 값**

InputStream Throws java.io.IOException InputStream을 얻는데 실패한 경우 getOutputStream public java.io.OutputStream getOutputStream() throws java.io.IOException OutputStream 을 반환한다.

**반환 값**

OutputStream Throws java.io.IOException OutputStream을 얻는데 실패한 경우 getURL public java.lang.String getURL() URL 을 반환한다.

**반환 값**

URL 문자열 getProtocol public java.lang.String getProtocol() URL 의 프로토콜 부분을 반환한다.

**반환 값**

프로토콜 문자열 getHost public java.lang.String getHost() URL 의 호스트 부분을 반환한다.

**반환 값**

호스트 문자열 getFile public java.lang.String getFile() URL 의 파일 부분을 반환한다.

**반환 값**

파일 문자열 getRef public java.lang.String getRef() URL 의 anchor 부분을 반환한다.

**반환 값**

anchor 문자열 getQuery public java.lang.String getQuery() URL 의 query 부분을 반환한다.

**반환 값**

query 문자열 getPort public int getPort() URL 의 포트 부분을 반환한다.

**반환 값**

정수형의 포트번호 getRequestMethod public java.lang.String getRequestMethod() 요청 메쏘드를 반환한다.

**반환 값**

요청 메쏘드 문자열 setRequestMethod public void setRequestMethod(java.lang.String method) throws java.io.IOException 요청 메쏘드를 설정한다.

**매개 변수**

- `method` - 요청 메쏘드 문자열 Throws java.io.IOException 요청 메쏘드 설정에 실패한 경우 getRequestProperty
- `public` - java.lang.String getRequestProperty(java.lang.String key) 매개변수 key 에 해당하는 request property 값을 반환한다.

**매개 변수**

- `key` - request header 이름

**반환 값**

request property 값 setRequestProperty public void setRequestProperty(java.lang.String key, ava.lang.String value) request property 를 설정한다.

**매개 변수**

- `key` - request header 이름
- `value` - request property 값 getResponseCode
- `public` - int getResponseCode() throws java.io.IOException 서버의 응답코드를 반환한다.

**반환 값**

정수 응답코드 Throws java.io.IOException 응답코드를 알 수 없을 경우 getResponseMessage public java.lang.String getResponseMessage() throws java.io.IOException 서버의 응답메세지를 반환한다. 서버로 부터의 응답이 다음과 같을 때 HTTP/1.0 200 OK HTTP/1.0 404 Not Found 응답메세지는 "OK" 와 "Not Found" 를 각각 반환한다.

**반환 값**

응답메세지 Throws java.io.IOException 응답 메세지를 알 수 없을 경우 getLength public long getLength() 수신한 컨텐트의 길이를 바이트 단위로 반환한다.

**반환 값**

수신한 컨텐트의 길이 getType public java.lang.String getType() 수신한 컨텐트의 타입을 반환한다.

**반환 값**

컨텐트 타입 문자열 getEncoding public java.lang.String getEncoding() 수신한 컨텐트의 인코딩을 반환한다. 서버로부터의 응답헤더중 "content-encoding" 에 해당하는 값을 반환한다.

**반환 값**

컨텐트 인코딩 문자열 getExpiration public long getExpiration() 컨텐트의 만료일을 반환한다.

**반환 값**

- 1970년 1월 1일 GMT 기준시로부터의 시간(초단위)
getDate public long getDate() 컨텐트의 작성일을 반환한다.

**반환 값**

- 1970년 1월 1일 GMT 기준시로부터의 시간(초 단위)
getLastModified public long getLastModified() 컨텐트의 최근 수정시간을 반환한다.

**반환 값**

- 1970년 1월 1일 GMT 기준시로부터의 시간(초 단위)
getHeaderField public java.lang.String getHeaderField(java.lang.String name) 서버로부터의 응답 헤더 값을 반환한다.

**매개 변수**

- `name` - 응답 헤더

**반환 값**

응답 헤더에 해당하는 값 setProxy public void setProxy(java.lang.String host, int port) throws java.io.IOException HTTP 프락시를 지정한다.

**매개 변수**

- `host` - 프락시 호스트
- `port` - 프락시 포트 Throws java.io.IOException 프락시를 지정할 수 없을 경우 isRelocatable
- `public` - boolean isRelocatable() 컨텐츠의 위치가 옮겨져서 서버가 다른 서버로의 접속을 유도하는 경우를 알려 준다. 이 메쏘드는 서버로부터 응답코드를 수신했을 경우에만 유효하다.

**반환 값**

서버의 응답코드가 301, 302, 303 중의 하나일 경우 true 를 반환한다. relocation public HttpSocket relocation() throws java.io.IOException 컨텐츠의 위치가 옮겨져서 서버가 다른 서버로의 접속을 유도하여 다른 서버로 접속하여 새로운 HTTP 소켓을 반환한다.

**반환 값**

새로 접속한 HTTP 소켓 Throws java.io.IOException 새로 접속할 수 없을 경우 Class Message java.lang.Object | +--org.kwis.msf.io.Message public class Message extends java.lang.Object 소켓으로 전송할 수 있는 메세지를 정의한 클래스이다. Methods inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 생성자 상세 설명 Message public Message(java.lang.String addr, byte[] data) 소켓으로 전송할 메세지를 생성한다.

**매개 변수**

- `addr` - 메세지를 수신할 주소
- `data` - 메세지 내용 Message
- `public` - Message(java.lang.String addr, byte[] data, int off, int len) 소켓으로 전송할 메세지를 생성한다.

**매개 변수**

- `addr` - 메세지 주소
- `data` - 메세지 버퍼
- `off` - 메세지 버퍼의 오프셋
- `len` - 메세지 버퍼의 길이 메쏘드 상세 설명 getData
- `public` - byte[] getData() 메세지 버퍼를 반환한다.

**반환 값**

메세지 버퍼 getLength public int getLength() 메세지 버퍼의 길이를 반환한다.

**반환 값**

메세지 버퍼 길이 setLength public int setLength(int val) 메세지 길이를 설정한다. 설정하려는 길이와 getOffset() 의 반환값의 합이 getData() 가 반환하는 버퍼길이를 초과하거나 길이가 0 보다 작으면 설정되지 않고 -1을 반환한다.

**매개 변수**

- `val` - 메시지 길이

**반환 값**

설정된 길이 getOffset public int getOffset() 메세지 버퍼의 오프셋을 반환한다.

**반환 값**

메세지 버퍼의 오프셋 setOffset public int setOffset(int val) 메세지 버퍼의 오프셋을 설정한다. 설정하려는 오프셋과 getLength() 의 반환값의 합이 getData() 가 반환하는 버퍼길이를 초과하거나 오프셋이 0 보다 작거나 오프셋이 getData() 가 반환하는 버퍼길이 이상이면 설정되지 않고 -1을 반환한다.

**매개 변수**

- `val` - 오프셋

**반환 값**

설정된 오프셋 getAddress public java.lang.String getAddress() 메세지의 주소를 반환한다.

**반환 값**

메세지 주소 getAddressInt public int getAddressInt() 메세지의 정수형 주소를 반환한다.

**반환 값**

메세지 정수형 주소. getDate public java.util.Date getDate() 메시지가 전송된 시간을 반환한다.

**반환 값**

성공

메시지가 전송된 시간.
실패

전송된 시간을 모를 경우 null 을 반환 setDate public void setDate(java.util.Date date) 메시지가 전송된 시간을 설정한다.

**매개 변수**

- `date` - 메시지가 전송된 시간. setAddressInt
- `public` - void setAddressInt(int addr) 메세지의 정수형 주소값을 지정한다. UDP 소켓으로 전송하는 메시지의 주소는 다음의 형식을 따른다. IP주소: 포트번호 예) 111.111.111.111:80

**매개 변수**

- `addr` - 정수형 주소 값
- `Class` - Network java.lang.Object | +--org.kwis.msf.io.Network
- `public` - class Network extends java.lang.Object 응용 프로그램이 TCP/IP 인터넷 통신을 하기 위한 인터넷 접근 API 를 모은 것이다. 응용 프로그램은 인터넷 접근 API 를 통해서 인터넷에 접근이 가능하게 된 후에야 TCP/IP 통신 소켓을 사용할 수 있다. TCP/IP 통신 소켓은 URL.find() 메쏘드로 생성된다. 메쏘드 상세 설명 connect
- `public` - static int connect() TCP/IP 인터넷 접근을 시도한다.

**반환 값**

현재 접근이 가능하다면 0을 돌려주고, 접근되어 있지 않은 상태에서 접근에 성공하면 1을 돌려준다. 만일 실패하면 -1을 돌려준다. disconnect public static void disconnect() TCP/IP 인터넷 접근을 종료한다. 이 함수가 호출된 후에는 TCP/IP 통신 소켓의 모든 I/O 기능이 불가능하게 된다. Class SchemeNotFoundException java.lang.Object | +--java.lang.Throwable | +--java.lang.Exception | +--java.io.IOException | +--org.kwis.msf.io.SchemeNotFoundException public class SchemeNotFoundException extends java.io.IOException Methods inherited from class java.lang.Throwable fillInStackTrace, getLocalizedMessage, getMessage, printStackTrace, printStackTrace, printStackTrace, toString Methods inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명 SchemeNotFoundException public SchemeNotFoundException() SchemeNotFoundException public SchemeNotFoundException(java.lang.String s) Interface Socket public interface Socket 플랫폼 외부와의 데이타 통신을 가능하게 하는 클래스이다. 소켓은 스트림(stream) 소켓과 그렇지 않은 소켓으로 구분된다. 스트림 소켓은 java.io.InputStream 과 java.io.OutputStream 으로 통신을 하며 스트림 소켓이 아닌 경우는 메시지(Message)형태로 통신을 한다. 스트림 소켓의 대표적인 예가 TCP 통신을 하는 소켓이고 메시지형태로 통신을 하는 소켓의 대표적인 예가 UDP 통신을 하는 소켓이다. 메쏘드 상세 설명 getInputStream public java.io.InputStream getInputStream() throws java.io.IOException 스트림 소켓일 경우 InputStream 을 반환한다.

**반환 값**

InputStream 을 반환한다 Throws java.io.IOException 스트림 소켓이 아니거나 InputStream 을 반환하지 못 할 경우 getOutputStream public java.io.OutputStream getOutputStream() throws java.io.IOException 스트림 소켓일 경우 OutputStream 을 반환한다.

**반환 값**

OutputStream 을 반환한다 Throws java.io.IOException 스트림 소켓이 아니거나 OutputStream 을 반환하지 못할 경우 isStream public boolean isStream() 스트림 소켓인지여부를 알려준다.

**반환 값**

스트림 소켓이면 true, 아니면 false getMessageCount public int getMessageCount() throws java.io.IOException 스트림 소켓이 아닐 경우 앞으로 이 소켓으로부터 읽을 수 있는 메세지 개수를 알려준다.

**반환 값**

앞으로 읽을 수 있는 메세지 개수. 메세지 개수를 알 수 없을 경우 -1을 반환한다. Throws java.io.IOException stream 소켓일 경우 getMessageMaxLength public int getMessageMaxLength() throws java.io.IOException 스트림 소켓이 아닐 경우 한 메세지에 실을 수 있는 데이타의 최대길이를 알려준다.

**반환 값**

메세지 데이타의 최대길이 Throws java.io.IOException 스트림 소켓일 경우 send public void send(Message m) throws java.io.IOException 스트림 소켓이 아닐 경우 메세지를 전송한다.

**매개 변수**

- `m` - 전송할 데이터가 저장된 메시지 Throws java.io.IOException 스트림 소켓이거나 메세지를 전송하지 못할 경우 recv
- `public` - void recv(Message msg) throws java.io.IOException 스트림 소켓이 아닐 경우 메세지를 수신한다.

**매개 변수**

- `m` - 수신된 데이터를 저장할 메시지

**반환 값**

수신한 메세지 Throws java.io.IOException 스트림 소켓이거나 메세지를 수신하지 못할 경우 close public void close() throws java.io.IOException 소켓을 닫는다. 스트림 소켓일 경우 만약 getInputStream() 이나 getOutputStream() 으로 InputStream 혹은 OutputStream 을 반환한 경우 소켓이 완전히 닫히기 위해서는 이 메쏘드와 함께 InputStream 혹은 OutputStream 의 close() 메쏘드가 불려 져야 한다. Throws java.io.IOException 에러 발생시 accept public Socket accept() throws java.io.IOException 서버 기능을 지원하는 소켓이 새롭게 클라이언트와 연결된 소켓을 반환한다.

**반환 값**

새로 연결된 소켓 Throws java.io.IOException 서버 기능을 지원하는 소켓이 아니거나 I/O 에러가 발생할 경우 Class URL java.lang.Object | +--org.kwis.msf.io.URL public class URL extends java.lang.Object 플랫폼 외부와의 데이타 통신을 위해 소켓을 생성해주는 클래스이다. 모든 소켓은 URL.find() 메쏘드에 URL(RFC1738 참조) 문자열을 전달하는 방식으로 생성된다. URL 문자열의 스킴(sheme) 부분에 의해 생성되는 소켓의 성격이 구분된다. 소켓의 성격은 스트림(stream) 소켓과 그렇지 않은 것으로 나눈다. 소켓에 사용하는 URL 문자열은 <표 2-2-1-1>에 정의되어 있으며 플랫폼은 TCP 서버 URL(serversocket:// 로 시작)을 제외한 문자열에 대해 소켓(Socket)을 생성해야 한다. <표 2-2-1-1> 프로토콜별 URL 문자열 소켓 URL 문자열 예 비고 .모드: r(읽기 전용), w(쓰기 전용), rw(읽기쓰기 가능) .타임아웃: 밀리 초 단위. 0 이면 무한대 .모드와 타임아웃은 데이터 송수신 때 socket://<IP주소>:<포트번호> socket://111.111. 적용됨. [/<모드>/<타임아웃>] 111.111:80 .모드와 타임아웃이 TCP socket://111.111. 생략되면 디폴트로 serversocket://:<포트번호>[/< 111.111:80/rw/300 모드는 "rw", 타임아웃은 모드>/<타임아웃>] 0 "0”. .서버소켓(serversocket:/ / 으로 시작)일 경우 모드와 타임 아웃은 연결되는 클라이언트 소켓에 적용됨. .서버소켓을 지원하는 지 여부는 플랫폼 구현의 선택사항임 datagram://:80 .로컬 포트로 바인드. datagram://:<포트번호>[/<모 UDP datagram://:80/rw .모드와 타임아웃은 TCP 드>/<타임아웃>] /3000 소켓과 의미가 동일함. comm://0:baudrat .제어문자열은 HAL API comm://<포트번호>:<제어문자 serial e=115200,parity=n `MH_serialOpen()` 함수 열> o,size=8,flow=no 설명 참조 HTTP HTTP URL http://somehost:8 Methods inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 생성자 상세 설명 없음 메쏘드 상세 설명 find public static Socket find(java.lang.String url) throws SchemeNotFoundException 매개변수 url 에 따라 소켓을 생성한다. Throws SchemeNotFoundException 소켓을 생성하지 못할 경우
