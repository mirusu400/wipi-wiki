---
title: "Interface Datagram"
---

`package javax.microedition.io`

```text
    datagram = connection.newDatagram(max);
 
    // Reset prepares the datagram for writing new message.
    datagram.reset();
 
    // writeUTF automatically increases the datagram length.
    datagram.writeUTF("hello world");
 
    connection.send(datagram);
```

## 설명

데이터그램에서 읽는 예는 다음과 같습니다(단일 사용에만 해당).

위의 *length*는 `getLength`에서 반환되며 
 경우에 따라 다른 의미를 가질 수 있습니다. 보낼 때의 *length*는 
 보낼 바이트 수입니다. 받기 전의 *length*는 수신할 최대 바이트 수입니다. 
 받은 후의 *length*는 수신된 바이트 수입니다. 
 따라서 보내거나 받은 후에 데이터그램을 다시 사용하여 수신하려면 
 `setLength`를 사용하여 길이를 
 다시 최대값으로 설정해야 합니다.

를 사용하지 않고 읽으려면

메소드를 
 사용해야 합니다.

데이터그램을 다시 읽는 예는 다음과 같습니다.

**Since:**
- CLDC 1.0

## 메서드 요약

- `String getAddress ()` — 데이터그램의 주소를 가져옵니다.
- `byte[] getData ()` — 데이터 버퍼의 내용을 가져옵니다.
- `int getLength ()` — 데이터그램의 길이를 가져옵니다.
- `int getOffset ()` — 오프셋을 가져옵니다.
- `void reset ()` — read/write pointer , offset 및 length 상태 변수를 0으로 설정합니다.
- `void setAddress ( Datagram reference)` — 다른 데이터그램의 주소를 복사하여 데이터그램 주소를 설정합니다.
- `void setAddress ( String addr)` — 데이터그램 주소를 설정합니다.
- `void setData (byte[] buffer, int offset, int len)` — buffer , offset 및 length 상태 변수를 설정합니다.
- `void setLength (int len)` — length 상태 변수를 설정합니다.

## 메서드 상세

### getAddress

```java
public String getAddress()
```

**Returns:**
- 문자열 형식의 주소 또는 주소가 설정되어 있지 않으면 null

**See Also:**
- ``setAddress(java.lang.String)``

### getData

```java
public byte[] getData()
```

**Returns:**
- 데이터 버퍼(바이트 배열)

**See Also:**
- ``setData(byte[], int, int)``

### getLength

```java
public int getLength()
```

**Returns:**
- length 상태 변수

**See Also:**
- ``setLength(int)``

### getOffset

```java
public int getOffset()
```

**Returns:**
- offset 상태 변수

### setAddress

```java
public void setAddress(String addr)
                throws IOException
```

**Parameters:**
- `addr` - 새로운 대상 주소(URL)

**Throws:**
- `IOException` - 일종의 I/O 오류가 발생한 경우

**See Also:**
- ``getAddress()``

### setAddress

```java
public void setAddress(Datagram reference)
```

**Parameters:**
- `reference` - 이 데이터그램의 새로운 대상 
 주소로 복사되는 주소의 데이터그램

**Throws:**
- `IllegalArgumentException` - 주소가 유효하지 않은 경우

**See Also:**
- ``getAddress()``

### setLength

```java
public void setLength(int len)
```

**Parameters:**
- `len` - 새로운 데이터그램 길이

**Throws:**
- `IllegalArgumentException` - length 또는 length에 
 offset을 더한 값이 버퍼 범위에서 벗어나는 경우

**See Also:**
- ``getLength()``

### setData

```java
public void setData(byte[] buffer,
                    int offset,
                    int len)
```

**Parameters:**
- `len` - 버퍼의 데이터 길이

**Throws:**
- `IllegalArgumentException` - length 또는 length에 offset을 
 더한 값이 버퍼 범위에서 벗어나거나 
 버퍼 매개 변수가 유효하지 않은 경우

**See Also:**
- ``getData()``

### reset

```java
public void reset()
```

read/write pointer , offset 및 length 상태 변수를 0으로 설정합니다.
