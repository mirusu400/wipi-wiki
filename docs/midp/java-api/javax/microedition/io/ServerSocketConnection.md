# Interface ServerSocketConnection

`package javax.microedition.io`

```
   // Create the server listening socket for port 1234 
   ServerSocketConnection scn = (ServerSocketConnection)
                            Connector.open("socket://:1234");
   // Wait for a connection.
   SocketConnection sc = (SocketConnection) scn.acceptAndOpen();
   // Set application specific hints on the socket.
   sc.setSocketOption(DELAY, 0);
   sc.setSocketOption(LINGER, 0);
   sc.setSocketOption(KEEPALIVE, 0);
   sc.setSocketOption(RCVBUF, 128);
   sc.setSocketOption(SNDBUF, 128);
   // Get the input stream of the connection.
   DataInputStream is = sc.openDataInputStream();
   // Get the output stream of the connection.
   DataOutputStream os = sc.openDataOutputStream();
   // Read the input data.
   String result = is.readUTF();
   // Echo the data back to the sender.
   os.writeUTF(result);
   // Close everything.
   is.close();
   os.close();
   sc.close();
   scn.close();
   ..
```

## 설명

**Since:**
- MIDP 2.0

## 메서드 요약

- `String getLocalAddress ()` — 소켓이 바운드되는 로컬 주소를 가져옵니다.
- `int getLocalPort ()` — 이 소켓이 바운드되는 로컬 포트를 반환합니다.

## 메서드 상세

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
- ``SocketConnection``

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
- ``SocketConnection``
