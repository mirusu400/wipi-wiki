---
title: "Interface SecureConnection"
---

`package javax.microedition.io`

```text
   SecureConnection sc = (SecureConnection)
                         Connector.open("ssl://host.com:79");
   SecurityInfo info = sc.getSecurityInfo();
   boolean isTLS = (info.getProtocolName().equals("TLS"));
 
   sc.setSocketOption(SocketConnection.LINGER, 5);
   InputStream is  = sc.openInputStream();
   OutputStream os = sc.openOutputStream();
   os.write("\r\n".getBytes());
   int ch = 0;
   while(ch != -1) {
       ch = is.read();
   }
   is.close();
   os.close();
   sc.close();
```

## 설명

**Since:**
- MIDP 2.0

## 필드 요약

## 메서드 요약

- `SecurityInfo getSecurityInfo ()` — 열린 연결과 관련된 보안 정보를 반환합니다.

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
