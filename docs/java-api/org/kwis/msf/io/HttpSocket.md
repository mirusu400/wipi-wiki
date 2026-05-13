# Interface HttpSocket

`package org.kwis.msf.io`

## 필드 요약

- `static String CONNECT` — HTTP Connect 요청 메쏘드 이다.
- `static String DELETE` — HTTP Delete 요청 메쏘드 이다.
- `static String GET` — HTTP Get 요청 메쏘드 이다.
- `static String HEAD` — HTTP Head 요청 메쏘드 이다.
- `static int HTTP_ACCEPTED` — 서버응답코드 ACCEPTED 이다.
- `static int HTTP_BAD_GATEWAY` — 서버응답코드 BAD GATEWAY 이다.
- `static int HTTP_BAD_REQ` — 서버응답코드 BAD REQUEST 이다.
- `static int HTTP_CONFLICT` — 서버응답코드 CONFLICT 이다.
- `static int HTTP_CREATED` — 서버응답코드 CREATED 이다.
- `static int HTTP_ENTITY_TOO_LARGE` — 서버응답코드 TOO LARGE 이다.
- `static int HTTP_EXPECT_FAIL` — 서버응답코드 EXPECTATION FAILED 이다.
- `static int HTTP_FORBIDDEN` — 서버응답코드 FORBIDDEN 이다.
- `static int HTTP_GATEWAY_TIMEOUT` — 서버응답코드 GATEWAY TIMEOUT 이다.
- `static int HTTP_GONE` — 서버응답코드 GONE 이다.
- `static int HTTP_LENGTH_REQUIRED` — 서버응답코드 LENGTH REQUIRED 이다.
- `static int HTTP_METHOD_NOT_ALLOWED` — 서버응답코드 METHOD NOT ALLOWED 이다.
- `static int HTTP_MOVED_PERMANENTLY` — 서버응답코드 MOVED PETMANENTLY 이다.
- `static int HTTP_MOVED_TEMPORARILY` — 서버응답코드 MOVED TEMPORARILY 이다.
- `static int HTTP_MULTIPLE_CHOICE` — 서버응답코드 MULTIPLE CHOICE 이다.
- `static int HTTP_NO_CONTENT` — 서버응답코드 NO CONTENT 이다.
- `static int HTTP_NON_AUTHORITATIVE` — 서버응답코드 NOT AUTHORITATIVE 이다.
- `static int HTTP_NOT_ACCEPTABLE` — 서버응답코드 NOT ACCEPTABLE 이다.
- `static int HTTP_NOT_FOUND` — 서버응답코드 NOT FOUND 이다.
- `static int HTTP_NOT_IMPL` — 서버응답코드 NOT IMPLEMENTED 이다.
- `static int HTTP_NOT_MODIFIED` — 서버응답코드 NOT MODIFIED 이다.
- `static int HTTP_OK` — 서버응답코드 OK 이다.
- `static int HTTP_PARTIAL_CONTENT` — 서버응답코드 PARTIAL CONTENT 이다.
- `static int HTTP_PAYMENT_REQUIRED` — 서버응답코드 PAYMENT REQUIRED 이다.
- `static int HTTP_PRECONDITION_FAILED` — 서버응답코드 PRECONDITION FAILED 이다.
- `static int HTTP_PROXY_AUTHENTICATION_REQUIRED` — 서버응답코드 PROXY AUTHENTICATION REQUITRED 이다.
- `static int HTTP_REQ_RANGE` — 서버응답코드 REQUEST RANGE NOT SATISFIABLE이다.
- `static int HTTP_REQ_TIMEOUT` — 서버응답코드 REQUEST TIMEOUT 이다.
- `static int HTTP_REQ_TOO_LONG` — 서버응답코드 REQUEST TOO LONG 이다.
- `static int HTTP_RESET_CONTENT` — 서버응답코드 RESET CONTENT 이다.
- `static int HTTP_SEE_OTHER` — 서버응답코드 SEE OTHER 이다.
- `static int HTTP_SERVER_ERR` — 서버응답코드 INTERNAL SERVER ERROR 이다.
- `static int HTTP_UNAUTHORIZED` — 서버응답코드 UNAUTHORIZED 이다.
- `static int HTTP_UNAVAILABLE` — 서버응답코드 UNAVAILABLE 이다.
- `static int HTTP_UNSUPPORTED_TYPE` — 서버응답코드 UNSUPPORTED TYPE 이다.
- `static int HTTP_USE_PROXY` — 서버응답코드 USE PROXY 이다.
- `static int HTTP_VERSION` — 서버응답코드 VERSION NOT SUPPORTED 이다.
- `static String OPTIONS` — HTTP Options 요청 메쏘드 이다.
- `static String POST` — HTTP Post 요청 메쏘드 이다.
- `static String PUT` — HTTP Put 요청 메쏘드 이다.
- `static String TRACE` — HTTP Trace 요청 메쏘드 이다.

## 메서드 요약

- `void close ()` — HTTP 소켓을 닫는다.
- `long getDate ()` — 컨텐트의 작성일을 리턴한다.
- `String getEncoding ()` — 수신한 컨텐트의 인코딩을 리턴한다.
- `long getExpiration ()` — 컨텐트의 만료일을 리턴한다.
- `String getFile ()` — URL 의 파일 부분을 리턴한다.
- `String getHeaderField ( String name)` — 서버로 부터의 응답 헤더 값을 리턴한다.
- `String getHost ()` — URL 의 호스트 부분을 리턴한다.
- `InputStream getInputStream ()` — InputStream 을 리턴한다.
- `long getLastModified ()` — 컨텐트의 최근 수정시간을 리턴한다.
- `long getLength ()` — 수신한 컨텐트의 길이를 바이트 단위로 리턴한다.
- `OutputStream getOutputStream ()` — OutputStream 을 리턴한다.
- `int getPort ()` — URL 의 포트 부분을 리턴한다.
- `String getProtocol ()` — URL 의 프로토콜 부분을 리턴한다.
- `String getQuery ()` — URL 의 query 부분을 리턴한다.
- `String getRef ()` — URL 의 anchor 부분을 리턴한다.
- `String getRequestMethod ()` — 요청 메쏘드를 리턴한다.
- `String getRequestProperty ( String key)` — 매개변수 key 에 해당하는 request property 값을 리턴한다.
- `int getResponseCode ()` — 서버의 응답코드를 리턴한다.
- `String getResponseMessage ()` — 서버의 응답메세지를 리턴한다.
- `String getType ()` — 수신한 컨텐트의 타입을 리턴한다.
- `String getURL ()` — URL 을 리턴한다.
- `boolean isRelocatable ()` — 컨텐츠의 위치가 옮겨져서 서버가 다른 서버로의 접속을 유도하는 경우를 알려 준다.
- `HttpSocket relocation ()` — 컨텐츠의 위치가 옮겨져서 서버가 다른 서버로의 접속을 유도하여 다른 서버로 접속하여 새로운 HTTP 소켓을 리턴한다.
- `void setProxy ( String host, int port)` — HTTP 프락시를 지정한다.
- `void setRequestMethod ( String method)` — 요청 메쏘드를 설정한다.
- `void setRequestProperty ( String key, String value)` — request property 를 설정한다.

## 필드 상세
