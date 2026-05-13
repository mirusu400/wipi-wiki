# Interface Socket

`package org.kwis.msf.io`

```
public InputStream getInputStream()
                           throws IOException
```

## 설명

**Returns:**
- InputStream 을 리턴한다

**Throws:**
- `IOException` - stream 소켓이 아니거나 InputStream 을 리턴하지 못할 경우

### getOutputStream

**Returns:**
- OutputStream 을 리턴한다

**Throws:**
- `IOException` - stream 소켓이 아니거나 OutputStream 을 리턴하지 못할 경우

### isStream

**Returns:**
- stream 소켓이면 true, 아니면 false

### getMessageCount

**Returns:**
- 앞으로 읽을 수 있는 메세지 갯수. 메세지 갯수를 알수 없을 경우
 
 -1을 리턴한다.

**Throws:**
- `IOException` - stream 소켓일 경우

### getMessageMaxLength

**Returns:**
- 메세지 데이타의 최대길이

**Throws:**
- `IOException` - stream 소켓일 경우

### send

**Throws:**
- `IOException` - stream 소켓이거나 메세지를 전송하지 못할 경우

### recv

**Parameters:**
- `m` - 수신된 데이타가 저장될 메세지 버퍼

**Throws:**
- `IOException` - stream 소켓이거나 메세지를 수신하지 못할 경우

### close

**Throws:**
- `IOException` - 에러 발생시

### accept

**Returns:**
- 새로 연결된 소켓

**Throws:**
- `IOException` - 서버 기능을 지원하는 소켓이 아니거나 I/O 에러가 발생할 경우## 메서드 요약

- `Socket accept ()` — 서버 기능을 지원하는 소켓이 새롭게 연결된 소켓을 리턴한다.
- `void close ()` — 소켓을 닫는다. stream 소켓일 경우 만약 getInputStream() 이나 getOutputStream() 으로 InputStream 혹은 OutputStream 을 리턴한 경우 소켓이 완전히 닫히기 위해서는 이 메쏘드와 함께 InputStream 혹은 OutputStream 의 close() 메쏘드가 불려 져야 한다.
- `InputStream getInputStream ()` — stream 소켓일 경우 InputStream 을 리턴한다.
- `int getMessageCount ()` — stream 소켓이 아닐 경우 앞으로 이 소켓으로 부터 읽을 수 있는 메세지 갯수를 알려준다.
- `int getMessageMaxLength ()` — stream 소켓이 아닐경우 한 메세지에 실을 수 있는 데이타의 최대길이를 알려준다.
- `OutputStream getOutputStream ()` — stream 소켓일 경우 OutputStream 을 리턴한다.
- `boolean isStream ()` — stream 소켓인지여부를 알려준다.
- `void recv ( Message m)` — stream 소켓이 아닐 경우 메세지를 수신한다.
- `void send ( Message m)` — stream 소켓이 아닐 경우 메세지를 전송한다.

## 메서드 상세

### getInputStream

```java
public InputStream getInputStream()
                           throws IOException
```

**Returns:**
- InputStream 을 리턴한다

**Throws:**
- `IOException` - stream 소켓이 아니거나 InputStream 을 리턴하지 못할 경우

### getOutputStream

```java
public OutputStream getOutputStream()
                             throws IOException
```

**Returns:**
- OutputStream 을 리턴한다

**Throws:**
- `IOException` - stream 소켓이 아니거나 OutputStream 을 리턴하지 못할 경우

### isStream

```java
public boolean isStream()
```

**Returns:**
- stream 소켓이면 true, 아니면 false

### getMessageCount

```java
public int getMessageCount()
                    throws IOException
```

**Returns:**
- 앞으로 읽을 수 있는 메세지 갯수. 메세지 갯수를 알수 없을 경우
 
 -1을 리턴한다.

**Throws:**
- `IOException` - stream 소켓일 경우

### getMessageMaxLength

```java
public int getMessageMaxLength()
                        throws IOException
```

**Returns:**
- 메세지 데이타의 최대길이

**Throws:**
- `IOException` - stream 소켓일 경우

### send

```java
public void send(Message m)
          throws IOException
```

**Throws:**
- `IOException` - stream 소켓이거나 메세지를 전송하지 못할 경우

### recv

```java
public void recv(Message m)
          throws IOException
```

**Parameters:**
- `m` - 수신된 데이타가 저장될 메세지 버퍼

**Throws:**
- `IOException` - stream 소켓이거나 메세지를 수신하지 못할 경우

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` - 에러 발생시

### accept

```java
public Socket accept()
              throws IOException
```

**Returns:**
- 새로 연결된 소켓

**Throws:**
- `IOException` - 서버 기능을 지원하는 소켓이 아니거나 I/O 에러가 발생할 경우

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
