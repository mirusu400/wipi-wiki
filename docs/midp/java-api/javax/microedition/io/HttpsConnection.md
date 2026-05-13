# Interface HttpsConnection

`package javax.microedition.io`

```
     void getViaHttpsConnection(String url)
            throws CertificateException, IOException {
         HttpsConnection c = null;
         InputStream is = null;
         try {
             c = (HttpsConnection)Connector.open(url);
             // Getting the InputStream ensures that the connection
             // is opened (if it was not already handled by
             // Connector.open()) and the SSL handshake is exchanged,
             // and the HTTP response headers are read.
             // These are stored until requested.
             is = c.openDataInputStream();
             if c.getResponseCode() == HttpConnection.HTTP_OK) {
                 // Get the length and process the data
                 int len = (int)c.getLength();
                 if (len > 0) {
                     byte[] data = new byte[len];
                     int actual = is.readFully(data);
                     ...
                 } else {
                     int ch;
                     while ((ch = is.read()) != -1) {
                         ...
                     }
                 }
             } else {
               ...
             }
         } finally {
             if (is != null)
                 is.close();
             if (c != null)
                 c.close();
         }
     }
```

## 필드 요약

## 메서드 요약

- `int getPort ()` — 이 HttpsConnection 에 대한 URL의 네트워크 포트 번호를 반환합니다.
- `SecurityInfo getSecurityInfo ()` — 성공적으로 열린 연결과 관련된 보안 정보를 반환합니다.

## 메서드 상세

### getSecurityInfo

```java
public SecurityInfo getSecurityInfo()
                             throws IOException
```

**Returns:**
- 열린 연결과 관련된 보안 정보

**Throws:**
- `IOException` - 임의 연결 오류가 발생한 경우

### getPort

```java
public int getPort()
```

**Specified by:**
- `getPort` in interface `HttpConnection`

**Returns:**
- 이 `HttpsConnection`에 대한 
URL의 네트워크 포트 번호. 
`Connector.open`에 전달된 문자열에 포트 번호가 없으면 
기본 HTTPS 포트 번호(443)가 반환됩니다.
