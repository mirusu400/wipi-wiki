# Interface SocketConnection

`package javax.microedition.io`

```
   SocketConnection sc = (SocketConnection)
                         Connector.open("socket://host.com:79");
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

- `static byte DELAY` — 작은 버퍼 쓰기 지연 을 위한 소켓 옵션(0).
- `static byte KEEPALIVE` — 연결 유지 기능을 위한 소켓 옵션(2).
- `static byte LINGER` — 보류 중인 데이터 출력과의 연결을 닫기 전에 대기할 초 단위 지연 시간 을 위한 소켓 옵션(1).
- `static byte RCVBUF` — 수신 버퍼 의 크기를 위한 소켓 옵션(3).
- `static byte SNDBUF` — 전송 버퍼 의 크기를 위한 소켓 옵션(4).

## 메서드 요약

- `String getAddress ()` — 소켓이 바운드되는 원격 주소를 가져옵니다.
- `String getLocalAddress ()` — 소켓이 바운드되는 로컬 주소를 가져옵니다.
- `int getLocalPort ()` — 이 소켓이 바운드되는 로컬 포트를 반환합니다.
- `int getPort ()` — 이 소켓이 바운드되는 원격 포트를 반환합니다.
- `int getSocketOption (byte option)` — 연결에 대한 소켓 옵션을 가져옵니다.
- `void setSocketOption (byte option, int value)` — 연결에 대한 소켓 옵션을 설정합니다.

## 필드 상세

### DELAY

```java
public static final byte DELAY
```

**See Also:**
- `Constant Field Values`

### LINGER

```java
public static final byte LINGER
```

**See Also:**
- `Constant Field Values`

### KEEPALIVE

```java
public static final byte KEEPALIVE
```

**See Also:**
- `Constant Field Values`

### RCVBUF

```java
public static final byte RCVBUF
```

**See Also:**
- `Constant Field Values`

### SNDBUF

```java
public static final byte SNDBUF
```

**See Also:**
- `Constant Field Values`

### setSocketOption

```java
public void setSocketOption(byte option,
                            int value)
                     throws IllegalArgumentException,
                            IOException
```

**Parameters:**
- `value` - 지정된 옵션의 숫자 값

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``getSocketOption(byte)``

### getSocketOption

```java
public int getSocketOption(byte option)
                    throws IllegalArgumentException,
                           IOException
```

**Parameters:**
- `option` - 소켓 옵션 식별자(KEEPALIVE, LINGER, 
SNDBUF, RCVBUF 또는 DELAY)

**Returns:**
- 지정된 옵션의 숫자 값 또는 값을 
사용할 수 없는 경우 -1

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``setSocketOption(byte, int)``

### getLocalAddress

```java
public String getLocalAddress()
                       throws IOException
```

**Returns:**
- 소켓이 바운드되는 로컬 주소

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``ServerSocketConnection``

### getLocalPort

```java
public int getLocalPort()
                 throws IOException
```

**Returns:**
- 이 소켓이 연결되는 로컬 포트 번호

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``ServerSocketConnection``

### getAddress

```java
public String getAddress()
                  throws IOException
```

**Returns:**
- 소켓이 바운드되는 원격 주소

**Throws:**
- `IOException` - 연결이 닫힌 경우

### getPort

```java
public int getPort()
            throws IOException
```

**Returns:**
- 이 소켓이 연결되는 원격 포트 번호

**Throws:**
- `IOException` - 연결이 닫힌 경우

## 메서드 상세

### setSocketOption

```java
public void setSocketOption(byte option,
                            int value)
                     throws IllegalArgumentException,
                            IOException
```

**Parameters:**
- `value` - 지정된 옵션의 숫자 값

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``getSocketOption(byte)``

### getSocketOption

```java
public int getSocketOption(byte option)
                    throws IllegalArgumentException,
                           IOException
```

**Parameters:**
- `option` - 소켓 옵션 식별자(KEEPALIVE, LINGER, 
SNDBUF, RCVBUF 또는 DELAY)

**Returns:**
- 지정된 옵션의 숫자 값 또는 값을 
사용할 수 없는 경우 -1

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``setSocketOption(byte, int)``

### getLocalAddress

```java
public String getLocalAddress()
                       throws IOException
```

**Returns:**
- 소켓이 바운드되는 로컬 주소

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``ServerSocketConnection``

### getLocalPort

```java
public int getLocalPort()
                 throws IOException
```

**Returns:**
- 이 소켓이 연결되는 로컬 포트 번호

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``ServerSocketConnection``

### getAddress

```java
public String getAddress()
                  throws IOException
```

**Returns:**
- 소켓이 바운드되는 원격 주소

**Throws:**
- `IOException` - 연결이 닫힌 경우

### getPort

```java
public int getPort()
            throws IOException
```

**Returns:**
- 이 소켓이 연결되는 원격 포트 번호

**Throws:**
- `IOException` - 연결이 닫힌 경우
