---
title: "Interface HttpConnection"
---

`package javax.microedition.io`

```text
     void getViaStreamConnection(String url) throws IOException {
         StreamConnection c = null;
         InputStream s = null;
         try {
             c = (StreamConnection)Connector.open(url);
             s = c.openInputStream();
             int ch;
             while ((ch = s.read()) != -1) {
                 ...
             }
         } finally {
             if (s != null)
                 s.close();
             if (c != null)
                 c.close();
         }
     }
```

## 설명

**ContentConnection 사용 예**

`ContentConnection`을 사용하여 단순히 URL을 읽기만 하며 
HTTP 고유의 동작은 필요 없거나 사용되지 않습니다.

`Connector.open`을 사용하여 URL을 열고 
`ContentConnection`이 반환됩니다. 
`ContentConnection`은 길이를 제공할 수도 있습니다. 
길이를 사용할 수 있으면 길이를 사용하여 대량으로 데이터를 읽습니다. 
`ContentConnection`에서 
`InputStream`이 열립니다. 
EOF(-1)까지 모든 문자를 읽는 데 사용됩니다. 
예외가 발생하면 연결과 스트림이 닫힙니다.

**HttpConnection 사용 예**

`HttpConnection`을 사용하여 HTTP 헤더와 데이터를 읽습니다.

`Connector.open`을 사용하여 URL을 열고 
`HttpConnection`이 반환됩니다. 
HTTP 헤더를 읽고 처리합니다. 
길이를 사용할 수 있으면 길이를 사용하여 대량으로 데이터를 읽습니다. 
`HttpConnection`에서 
`InputStream`이 열립니다. 
EOF(-1)까지 모든 문자를 읽는 데 사용됩니다. 
예외가 발생하면 연결과 스트림이 닫힙니다.

**POST 및 HttpConnection 사용 예**

일부 헤더와 내용이 포함된 요청을 서버에 게시하고 
헤더와 내용을 처리합니다.

`Connector.open`을 사용하여 URL을 열고
 `HttpConnection`이 반환됩니다. 
요청 메소드는 POST와 요청 헤더 집합으로 설정됩니다. 
단순한 명령을 작성하고 플러시합니다. 
HTTP 헤더를 읽고 처리합니다. 
길이를 사용할 수 있으면 길이를 사용하여 대량으로 데이터를 읽습니다. 
`HttpConnection`에서 
`InputStream`이 열립니다.
EOF(-1)까지 모든 문자를 읽는 데 사용됩니다. 
예외가 발생하면 연결과 스트림이 닫힙니다.

**커넥터에 대한 단순한 스트림 메소드**

주의: `Connector` 클래스는 
지정된 URL에 대한 
입력 또는 출력 스트림을 직접 검색하기 위한 
다음과 같은 편리한 메소드를 정의합니다.

- ` InputStream openInputStream(String url) `
- ` DataInputStream openDataInputStream(String url) `
- ` OutputStream openOutputStream(String url) `
- ` DataOutputStream openDataOutputStream(String url) `

이러한 메소드를 사용할 경우 특정 제한이 수반됩니다. 
실제 연결에 대한 참조가 아닌 
연결의 입력 또는 출력 스트림에 대한 
참조만 가져올 수 있습니다. 
연결에 대한 참조를 가져올 수 없으므로 연결을 직접 조작하거나 
쿼리할 수 없으며 다음 메소드를 호출할 수 없게 됩니다.

- ` getRequestMethod() `
- ` setRequestMethod() `
- ` getRequestProperty() `
- ` setRequestProperty() `
- ` getLength() `
- ` getType() `
- ` getEncoding() `
- ` getHeaderField() `
- ` getResponseCode() `
- ` getResponseMessage() `
- ` getHeaderFieldInt`
- ` getHeaderFieldDate`
- ` getExpiration`
- ` getDate`
- ` getLastModified`
- ` getHeaderField`
- ` getHeaderFieldKey`

**Since:**
- MIDP 1.0

## 필드 요약

- `static String GET` — HTTP Get 메소드
- `static String HEAD` — HTTP Head 메소드
- `static int HTTP_ACCEPTED` — 202: 요청 처리가 승인되었지만 처리가 완료되지 않았습니다.
- `static int HTTP_BAD_GATEWAY` — 502: 게이트웨이나 프록시로 작동하는 서버가 요청 이행 중에 액세스한 업스트림 서버로부터 유효하지 않은 응답을 받았습니다.
- `static int HTTP_BAD_METHOD` — 405: Request-Line에 지정된 메소드를 Request-URI로 식별된 자원에 사용할 수 없습니다.
- `static int HTTP_BAD_REQUEST` — 400: 잘못된 형식의 구문 때문에 서버에서 요청을 이해할 수 없습니다.
- `static int HTTP_CLIENT_TIMEOUT` — 408: 클라이언트가 서버 대기 시간 내에 요청하지 못했습니다.
- `static int HTTP_CONFLICT` — 409: 요청이 자원의 현재 상태와 충돌하므로 요청을 완료할 수 없습니다.
- `static int HTTP_CREATED` — 201: 요청이 이행되었으며 그 결과 새로운 자원이 만들어졌습니다.
- `static int HTTP_ENTITY_TOO_LARGE` — 413: 서버에서 처리할 수 있는 것보다 요청 엔티티가 더 크므로 서버가 요청 처리를 거부합니다.
- `static int HTTP_EXPECT_FAILED` — 417: 서버가 Expect 요청 헤더 필드에 지정된 기대를 충족시킬 수 없거나, 서버가 프록시인 경우 다음 경유 서버에서 요청을 충족시킬 수 없다는 확실한 증거가 있습니다.
- `static int HTTP_FORBIDDEN` — 403: 서버가 요청을 이해했지만 이행하기를 거부합니다.
- `static int HTTP_GATEWAY_TIMEOUT` — 504: 게이트웨이나 프록시로 작동하는 서버가 요청 완료 중에 액세스한 URI 또는 다른 보조 서버에 의해 지정된 업스트림 서버로부터 적절한 응답을 받지 못했습니다.
- `static int HTTP_GONE` — 410: 요청된 자원은 서버에서 더 이상 사용할 수 없으며 전달 주소를 알 수 없습니다.
- `static int HTTP_INTERNAL_ERROR` — 500: 서버에서 예상치 못한 조건을 발견하여 요청을 이행하지 못했습니다.
- `static int HTTP_LENGTH_REQUIRED` — 411: 서버에서 Content- Length가 정의되지 않은 요청을 거부합니다.
- `static int HTTP_MOVED_PERM` — 301: 요청된 자원에 새로운 영구 URL이 할당되었으며 이 자원에 대한 이후 참조는 반환된 URI 중 하나를 사용하는 것이 좋습니다.
- `static int HTTP_MOVED_TEMP` — 302: 요청된 자원이 일시적으로 다른 URI에 있습니다.
- `static int HTTP_MULT_CHOICE` — 300: 요청된 자원이 각각 특정 위치를 가진 표현 집합 중 하나에 일치하며, 사용자가 원하는 표현을 선택하고 요청을 해당 위치로 리디렉션할 수 있도록 에이전트 구동 협상 정보가 제공됩니다.
- `static int HTTP_NO_CONTENT` — 204: 서버에서 요청을 이행했지만 entity-body를 반환할 필요가 없으며 업데이트된 meta-information을 반환할 수도 있습니다.
- `static int HTTP_NOT_ACCEPTABLE` — 406: 요청에 의해 식별된 자원이 요청 시 전송된 승인 헤더에 따라 승인할 수 없는 내용이 포함된 응답 엔티티만 생성할 수 있습니다.
- `static int HTTP_NOT_AUTHORITATIVE` — 203: entity-header에 반환된 meta-information은 원본 서버에서 사용할 수 있는 정의 집합이 아닙니다.
- `static int HTTP_NOT_FOUND` — 404: 서버에서 Request-URI에 일치하는 항목을 찾지 못했습니다.
- `static int HTTP_NOT_IMPLEMENTED` — 501: 서버에서 요청 이행에 필요한 기능을 지원하지 않습니다.
- `static int HTTP_NOT_MODIFIED` — 304: 클라이언트가 조건부 GET 요청을 수행했으며 액세스가 허용되었지만 문서를 수정하지 않은 경우 서버는 이 상태 코드로 응답하는 것이 좋습니다.
- `static int HTTP_OK` — 200: 요청이 성공했습니다.
- `static int HTTP_PARTIAL` — 206: 서버에서 자원에 대한 부분 GET 요청을 이행했습니다.
- `static int HTTP_PAYMENT_REQUIRED` — 402: 이 코드는 이후 사용을 위해 예약됩니다.
- `static int HTTP_PRECON_FAILED` — 412: 하나 이상의 요청 헤더 필드에 지정된 사전 조건을 서버에서 테스트한 결과 false로 평가되었습니다.
- `static int HTTP_PROXY_AUTH` — 407: 이 코드는 401 (Unauthorized)와 유사하지만 클라이언트가 먼저 프록시를 사용하여 자신을 인증해야 함을 나타냅니다.
- `static int HTTP_REQ_TOO_LONG` — 414: Request-URI가 서버에서 해석할 수 있는 것보다 길어서 서버가 요청 처리를 거부합니다.
- `static int HTTP_RESET` — 205: 서버에서 요청을 이행했으며 사용자 에이전트는 요청을 보내게 한 문서 보기를 재설정하는 것이 좋습니다.
- `static int HTTP_SEE_OTHER` — 303: 요청에 대한 응답은 다른 URI에서 찾을 수 있으며 해당 자원에 대한 GET 메소드를 사용하여 검색하는 것이 좋습니다.
- `static int HTTP_TEMP_REDIRECT` — 307: 요청된 자원이 일시적으로 다른 URI에 있습니다.
- `static int HTTP_UNAUTHORIZED` — 401: 요청에 사용자 인증이 필요합니다.
- `static int HTTP_UNAVAILABLE` — 503: 일시적 오버로드 또는 유지 보수로 인해 현재 서버에서 요청을 처리할 수 없습니다.
- `static int HTTP_UNSUPPORTED_RANGE` — 416: 요청에 Range 요청 헤더 필드가 포함되어 있지만 이 필드의 범위 지정자 값 중에 선택한 자원의 현재 범위와 겹치는 값이 없으며 요청에 If-Range 요청 헤더 필드가 포함되어 있지 않으면 서버에서 이 상태 코드로 응답하는 것이 좋습니다.
- `static int HTTP_UNSUPPORTED_TYPE` — 415: 요청 엔티티가 요청된 메소드의 요청 자원에서 지원하지 않는 형식이므로 서버에서 요청 처리를 거부합니다.
- `static int HTTP_USE_PROXY` — 305: 요청된 자원은 Location 필드에 지정된 프록시를 통해 액세스해야 합니다.
- `static int HTTP_VERSION` — 505: 서버에서 요청 메시지에 사용된 HTTP 프로토콜 버전을 지원하지 않거나 지원을 거부합니다.
- `static String POST` — HTTP Post 메소드

## 메서드 요약

- `long getDate ()` — date 헤더 필드 값을 반환합니다.
- `long getExpiration ()` — expires 헤더 필드 값을 반환합니다.
- `String getFile ()` — HttpConnection 의 URL에서 파일 부분을 반환합니다.
- `String getHeaderField (int n)` — 색인으로 헤더 필드 값을 가져옵니다.
- `String getHeaderField ( String name)` — 명명된 헤더 필드 값을 반환합니다.
- `long getHeaderFieldDate ( String name, long def)` — 날짜로 구문 분석된 명명된 필드 값을 반환합니다.
- `int getHeaderFieldInt ( String name, int def)` — 숫자로 구문 분석된 명명된 필드 값을 반환합니다.
- `String getHeaderFieldKey (int n)` — 색인으로 헤더 필드 키를 가져옵니다.
- `String getHost ()` — HttpConnection 의 URL에 지정된 호스트 정보(예: 호스트 이름 또는 IPv4 주소)를 반환합니다.
- `long getLastModified ()` — last-modified 헤더 필드 값을 반환합니다.
- `int getPort ()` — 이 HttpConnection 에 대한 URL의 네트워크 포트 번호를 반환합니다.
- `String getProtocol ()` — HttpConnection 의 URL에 지정된 프로토콜 이름(예: http 또는 https)을 반환합니다.
- `String getQuery ()` — HttpConnection 의 URL에서 쿼리 부분을 반환합니다.
- `String getRef ()` — HttpConnection 의 URL에서 참조 부분을 반환합니다.
- `String getRequestMethod ()` — 현재 요청 메소드(예: HEAD, GET, POST)를 가져옵니다.
- `String getRequestProperty ( String key)` — 이 연결의 명명된 일반 요청 등록 정보 값을 반환합니다.
- `int getResponseCode ()` — HTTP 응답 상태 코드를 반환하며, 응답을 다음과 같이 구문 분석합니다.
- `String getResponseMessage ()` — 응답 코드와 함께 서버에서 반환된 HTTP 응답 메시지를 가져옵니다.
- `String getURL ()` — 이 연결에 대한 URL의 문자열 표현을 반환합니다.
- `void setRequestMethod ( String method)` — URL 요청 메소드를 다음 중 하나로 설정합니다.
- `void setRequestProperty ( String key, String value)` — 일반 요청 등록 정보를 설정합니다.

## 필드 상세

### HEAD

```java
public static final String HEAD
```

**See Also:**
- `Constant Field Values`

### GET

```java
public static final String GET
```

**See Also:**
- `Constant Field Values`

### POST

```java
public static final String POST
```

**See Also:**
- `Constant Field Values`

### HTTP_OK

```java
public static final int HTTP_OK
```

**See Also:**
- `Constant Field Values`

### HTTP_CREATED

```java
public static final int HTTP_CREATED
```

**See Also:**
- `Constant Field Values`

### HTTP_ACCEPTED

```java
public static final int HTTP_ACCEPTED
```

**See Also:**
- `Constant Field Values`

### HTTP_NOT_AUTHORITATIVE

```java
public static final int HTTP_NOT_AUTHORITATIVE
```

**See Also:**
- `Constant Field Values`

### HTTP_NO_CONTENT

```java
public static final int HTTP_NO_CONTENT
```

**See Also:**
- `Constant Field Values`

### HTTP_RESET

```java
public static final int HTTP_RESET
```

**See Also:**
- `Constant Field Values`

### HTTP_PARTIAL

```java
public static final int HTTP_PARTIAL
```

**See Also:**
- `Constant Field Values`

### HTTP_MULT_CHOICE

```java
public static final int HTTP_MULT_CHOICE
```

**See Also:**
- `Constant Field Values`

### HTTP_MOVED_PERM

```java
public static final int HTTP_MOVED_PERM
```

**See Also:**
- `Constant Field Values`

### HTTP_MOVED_TEMP

```java
public static final int HTTP_MOVED_TEMP
```

**See Also:**
- `Constant Field Values`

### HTTP_SEE_OTHER

```java
public static final int HTTP_SEE_OTHER
```

**See Also:**
- `Constant Field Values`

### HTTP_NOT_MODIFIED

```java
public static final int HTTP_NOT_MODIFIED
```

**See Also:**
- `Constant Field Values`

### HTTP_USE_PROXY

```java
public static final int HTTP_USE_PROXY
```

**See Also:**
- `Constant Field Values`

### HTTP_TEMP_REDIRECT

```java
public static final int HTTP_TEMP_REDIRECT
```

**See Also:**
- `Constant Field Values`

### HTTP_BAD_REQUEST

```java
public static final int HTTP_BAD_REQUEST
```

**See Also:**
- `Constant Field Values`

### HTTP_UNAUTHORIZED

```java
public static final int HTTP_UNAUTHORIZED
```

**See Also:**
- `Constant Field Values`

### HTTP_PAYMENT_REQUIRED

```java
public static final int HTTP_PAYMENT_REQUIRED
```

**See Also:**
- `Constant Field Values`

### HTTP_FORBIDDEN

```java
public static final int HTTP_FORBIDDEN
```

**See Also:**
- `Constant Field Values`

### HTTP_NOT_FOUND

```java
public static final int HTTP_NOT_FOUND
```

**See Also:**
- `Constant Field Values`

### HTTP_BAD_METHOD

```java
public static final int HTTP_BAD_METHOD
```

**See Also:**
- `Constant Field Values`

### HTTP_NOT_ACCEPTABLE

```java
public static final int HTTP_NOT_ACCEPTABLE
```

**See Also:**
- `Constant Field Values`

### HTTP_PROXY_AUTH

```java
public static final int HTTP_PROXY_AUTH
```

**See Also:**
- `Constant Field Values`

### HTTP_CLIENT_TIMEOUT

```java
public static final int HTTP_CLIENT_TIMEOUT
```

**See Also:**
- `Constant Field Values`

### HTTP_CONFLICT

```java
public static final int HTTP_CONFLICT
```

**See Also:**
- `Constant Field Values`

### HTTP_GONE

```java
public static final int HTTP_GONE
```

**See Also:**
- `Constant Field Values`

### HTTP_LENGTH_REQUIRED

```java
public static final int HTTP_LENGTH_REQUIRED
```

**See Also:**
- `Constant Field Values`

### HTTP_PRECON_FAILED

```java
public static final int HTTP_PRECON_FAILED
```

**See Also:**
- `Constant Field Values`

### HTTP_ENTITY_TOO_LARGE

```java
public static final int HTTP_ENTITY_TOO_LARGE
```

**See Also:**
- `Constant Field Values`

### HTTP_REQ_TOO_LONG

```java
public static final int HTTP_REQ_TOO_LONG
```

**See Also:**
- `Constant Field Values`

### HTTP_UNSUPPORTED_TYPE

```java
public static final int HTTP_UNSUPPORTED_TYPE
```

**See Also:**
- `Constant Field Values`

### HTTP_UNSUPPORTED_RANGE

```java
public static final int HTTP_UNSUPPORTED_RANGE
```

**See Also:**
- `Constant Field Values`

### HTTP_EXPECT_FAILED

```java
public static final int HTTP_EXPECT_FAILED
```

**See Also:**
- `Constant Field Values`

### HTTP_INTERNAL_ERROR

```java
public static final int HTTP_INTERNAL_ERROR
```

**See Also:**
- `Constant Field Values`

### HTTP_NOT_IMPLEMENTED

```java
public static final int HTTP_NOT_IMPLEMENTED
```

**See Also:**
- `Constant Field Values`

### HTTP_BAD_GATEWAY

```java
public static final int HTTP_BAD_GATEWAY
```

**See Also:**
- `Constant Field Values`

### HTTP_UNAVAILABLE

```java
public static final int HTTP_UNAVAILABLE
```

**See Also:**
- `Constant Field Values`

### HTTP_GATEWAY_TIMEOUT

```java
public static final int HTTP_GATEWAY_TIMEOUT
```

**See Also:**
- `Constant Field Values`

### HTTP_VERSION

```java
public static final int HTTP_VERSION
```

**See Also:**
- `Constant Field Values`

### getURL

```java
public String getURL()
```

**Returns:**
- 이 연결에 대한 URL의 문자열 표현

### getProtocol

```java
public String getProtocol()
```

**Returns:**
- `HttpConnection`의 URL에 지정된 프로토콜

### getHost

```java
public String getHost()
```

**Returns:**
- `HttpConnection`의 
URL에 지정된 호스트 정보

### getFile

```java
public String getFile()
```

**Returns:**
- `HttpConnection`의 URL에서 파일 부분. 
파일이 없으면 `null`이 반환됩니다.

### getRef

```java
public String getRef()
```

**Returns:**
- `HttpConnection`의 URL에서 참조 부분. 
값이 없으면 `null`이 반환됩니다.

### getQuery

```java
public String getQuery()
```

**Returns:**
- `HttpConnection`의 
URL에서 쿼리 부분. 값이 없으면 
`null`이 반환됩니다.

### getPort

```java
public int getPort()
```

**Returns:**
- 이 `HttpConnection`에 대한 
URL의 네트워크 포트 번호. 
`Connector.open`에 전달된 문자열에 포트 번호가 없으면 
기본 HTTP 포트 번호(80)가 반환됩니다.

### getRequestMethod

```java
public String getRequestMethod()
```

**Returns:**
- HTTP 요청 메소드

**See Also:**
- ``setRequestMethod(java.lang.String)``

### setRequestMethod

```java
public void setRequestMethod(String method)
                      throws IOException
```

**Parameters:**
- `method` - HTTP 메소드

**Throws:**
- `IOException` - 메소드를 재설정할 수 없거나 
 요청된 메소드가 HTTP에 유효하지 않은 경우

**See Also:**
- ``getRequestMethod()``

### getRequestProperty

```java
public String getRequestProperty(String key)
```

**Parameters:**
- `key` - 요청 등록 정보를 알려주는 키워드(예:
"accept")

**Returns:**
- 이 연결의 명명된 일반 요청 등록 정보 값. 
 지정된 이름을 가진 키가 없으면 
 `null`이 반환됩니다.

**See Also:**
- ``setRequestProperty(java.lang.String, java.lang.String)``

### setRequestProperty

```java
public void setRequestProperty(String key,
                               String value)
                        throws IOException
```

**Parameters:**
- `value` - 연결된 값

**Throws:**
- `IOException` - 연결 상태가 
연결됨인 경우

**See Also:**
- ``getRequestProperty(java.lang.String)``

### getResponseCode

```java
public int getResponseCode()
                    throws IOException
```

**Returns:**
- HTTP Status-Code 또는 상태 코드를 확인할 수 없는 경우 -1

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getResponseMessage

```java
public String getResponseMessage()
                          throws IOException
```

**Returns:**
- HTTP 응답 메시지 또는 `null`

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getExpiration

```java
public long getExpiration()
                   throws IOException
```

**Returns:**
- 이 URL이 참조하는 자원의 만료 날짜 또는 
 만료 날짜를 알 수 없는 경우 0. 
 값은 1970년 1월 1일 GMT 이후의 밀리초 수입니다.

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getDate

```java
public long getDate()
             throws IOException
```

**Returns:**
- URL이 참조하는 자원의 전송 날짜 또는 
 전송 날짜를 알 수 없는 경우 `0`. 
 반환된 값은 1970년 1월 1일 GMT 이후의 밀리초 수입니다.

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getLastModified

```java
public long getLastModified()
                     throws IOException
```

**Returns:**
- 이 `HttpConnection`이 참조하는 자원이 
 마지막으로 수정된 날짜 또는 
 날짜를 알 수 없는 경우 0

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getHeaderField

```java
public String getHeaderField(String name)
                      throws IOException
```

**Parameters:**
- `name` - 헤더 필드의 이름

**Returns:**
- 명명된 헤더 필드 값 또는 해당 필드가 헤더에 없는 경우 
 `null`

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getHeaderFieldInt

```java
public int getHeaderFieldInt(String name,
                             int def)
                      throws IOException
```

**Parameters:**
- `def` - 기본값

**Returns:**
- 정수로 구문 분석된 명명된 필드 값. 
 필드가 없거나 필드 형식이 잘못된 경우 
 `def` 값이 반환됩니다.

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getHeaderFieldDate

```java
public long getHeaderFieldDate(String name,
                               long def)
                        throws IOException
```

**Parameters:**
- `def` - 기본값

**Returns:**
- 날짜로 구문 분석된 필드 값. 필드가 없거나 
 필드 형식이 잘못된 경우 
 `def` 인자 값이 반환됩니다.

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getHeaderField

```java
public String getHeaderField(int n)
                      throws IOException
```

**Parameters:**
- `n` - 헤더 필드의 색인

**Returns:**
- n번째 헤더 필드 값 또는 배열 색인이 범위에서 벗어난 경우 
`null`. 
필드에 값이 없으면 빈 문자열이 반환됩니다.

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getHeaderFieldKey

```java
public String getHeaderFieldKey(int n)
                         throws IOException
```

**Parameters:**
- `n` - 헤더 필드의 색인

**Returns:**
- n번째 헤더 필드 키 또는 배열 색인이 범위에서 벗어난 경우
`null`

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

## 메서드 상세

### getURL

```java
public String getURL()
```

**Returns:**
- 이 연결에 대한 URL의 문자열 표현

### getProtocol

```java
public String getProtocol()
```

**Returns:**
- `HttpConnection`의 URL에 지정된 프로토콜

### getHost

```java
public String getHost()
```

**Returns:**
- `HttpConnection`의 
URL에 지정된 호스트 정보

### getFile

```java
public String getFile()
```

**Returns:**
- `HttpConnection`의 URL에서 파일 부분. 
파일이 없으면 `null`이 반환됩니다.

### getRef

```java
public String getRef()
```

**Returns:**
- `HttpConnection`의 URL에서 참조 부분. 
값이 없으면 `null`이 반환됩니다.

### getQuery

```java
public String getQuery()
```

**Returns:**
- `HttpConnection`의 
URL에서 쿼리 부분. 값이 없으면 
`null`이 반환됩니다.

### getPort

```java
public int getPort()
```

**Returns:**
- 이 `HttpConnection`에 대한 
URL의 네트워크 포트 번호. 
`Connector.open`에 전달된 문자열에 포트 번호가 없으면 
기본 HTTP 포트 번호(80)가 반환됩니다.

### getRequestMethod

```java
public String getRequestMethod()
```

**Returns:**
- HTTP 요청 메소드

**See Also:**
- ``setRequestMethod(java.lang.String)``

### setRequestMethod

```java
public void setRequestMethod(String method)
                      throws IOException
```

**Parameters:**
- `method` - HTTP 메소드

**Throws:**
- `IOException` - 메소드를 재설정할 수 없거나 
 요청된 메소드가 HTTP에 유효하지 않은 경우

**See Also:**
- ``getRequestMethod()``

### getRequestProperty

```java
public String getRequestProperty(String key)
```

**Parameters:**
- `key` - 요청 등록 정보를 알려주는 키워드(예:
"accept")

**Returns:**
- 이 연결의 명명된 일반 요청 등록 정보 값. 
 지정된 이름을 가진 키가 없으면 
 `null`이 반환됩니다.

**See Also:**
- ``setRequestProperty(java.lang.String, java.lang.String)``

### setRequestProperty

```java
public void setRequestProperty(String key,
                               String value)
                        throws IOException
```

**Parameters:**
- `value` - 연결된 값

**Throws:**
- `IOException` - 연결 상태가 
연결됨인 경우

**See Also:**
- ``getRequestProperty(java.lang.String)``

### getResponseCode

```java
public int getResponseCode()
                    throws IOException
```

**Returns:**
- HTTP Status-Code 또는 상태 코드를 확인할 수 없는 경우 -1

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getResponseMessage

```java
public String getResponseMessage()
                          throws IOException
```

**Returns:**
- HTTP 응답 메시지 또는 `null`

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getExpiration

```java
public long getExpiration()
                   throws IOException
```

**Returns:**
- 이 URL이 참조하는 자원의 만료 날짜 또는 
 만료 날짜를 알 수 없는 경우 0. 
 값은 1970년 1월 1일 GMT 이후의 밀리초 수입니다.

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getDate

```java
public long getDate()
             throws IOException
```

**Returns:**
- URL이 참조하는 자원의 전송 날짜 또는 
 전송 날짜를 알 수 없는 경우 `0`. 
 반환된 값은 1970년 1월 1일 GMT 이후의 밀리초 수입니다.

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getLastModified

```java
public long getLastModified()
                     throws IOException
```

**Returns:**
- 이 `HttpConnection`이 참조하는 자원이 
 마지막으로 수정된 날짜 또는 
 날짜를 알 수 없는 경우 0

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getHeaderField

```java
public String getHeaderField(String name)
                      throws IOException
```

**Parameters:**
- `name` - 헤더 필드의 이름

**Returns:**
- 명명된 헤더 필드 값 또는 해당 필드가 헤더에 없는 경우 
 `null`

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getHeaderFieldInt

```java
public int getHeaderFieldInt(String name,
                             int def)
                      throws IOException
```

**Parameters:**
- `def` - 기본값

**Returns:**
- 정수로 구문 분석된 명명된 필드 값. 
 필드가 없거나 필드 형식이 잘못된 경우 
 `def` 값이 반환됩니다.

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getHeaderFieldDate

```java
public long getHeaderFieldDate(String name,
                               long def)
                        throws IOException
```

**Parameters:**
- `def` - 기본값

**Returns:**
- 날짜로 구문 분석된 필드 값. 필드가 없거나 
 필드 형식이 잘못된 경우 
 `def` 인자 값이 반환됩니다.

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getHeaderField

```java
public String getHeaderField(int n)
                      throws IOException
```

**Parameters:**
- `n` - 헤더 필드의 색인

**Returns:**
- n번째 헤더 필드 값 또는 배열 색인이 범위에서 벗어난 경우 
`null`. 
필드에 값이 없으면 빈 문자열이 반환됩니다.

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우

### getHeaderFieldKey

```java
public String getHeaderFieldKey(int n)
                         throws IOException
```

**Parameters:**
- `n` - 헤더 필드의 색인

**Returns:**
- n번째 헤더 필드 키 또는 배열 색인이 범위에서 벗어난 경우
`null`

**Throws:**
- `IOException` - 서버에 연결하는 동안 오류가 발생한 경우
