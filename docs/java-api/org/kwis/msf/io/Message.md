# Class Message

`package org.kwis.msf.io`

```text
java.lang.Object
  |
  +--org.kwis.msf.io.Message
```

## 설명

**extends Object:**

소켓으로 전송할 수 있는 메세지를 정의한 클래스이다.

## 생성자 요약

- Message (byte[] data) 단말로부터 메세지를 읽어들인 버퍼 Object를 생성한다.
- Message ( String addr,
 byte[] data) 소켓으로 전송할 메세지를 생성한다.
- Message ( String addr,
 byte[] data,
 int off,
 int len) 소켓으로 전송할 메세지를 생성한다.

## 메서드 요약

- `String getAddress ()` — 메세지의 주소를 리턴한다.
- `int getAddressInt ()` — 메세지의 주소를 정수형으로 리턴한다.
- `byte getClassification ()` — 메세지의 상태를 리턴한다.
- `byte[] getData ()` — 메세지 버퍼를 리턴한다.
- `Date getDate ()` — 메세지의 전송시간을 리턴한다.
- `byte getIndex ()` — 메세지 인덱스를 리턴한다.
- `int getLength ()` — 메세지 길이를 리턴한다.
- `int getOffset ()` — 메세지 버퍼의 오프셋을 리턴한다.
- `int getTeleServiceID ()` — 메세지의 텔리서비스 ID를 리턴한다.
- `void setAddress ( String addr)` — 메세지의 주소를 설정한다.
- `void setAddressInt (int addr)` — 메세지의 정수형 주소값을 지정한다.
- `void setClassification (byte newClassification)` — 메세지의 상태를 설정한다.
- `void setDate ( Date date)` — 메세지 전송시간을 설정한다.
- `void setIndex (byte newIndex)` — 메세지의 인덱스를 설정한다.
- `int setLength (int val)` — 메세지 길이를 설정한다.
- `int setOffset (int val)` — 메세지 버퍼의 오프셋을 설정한다.
- `void setTeleServiceID (int newTeleServiceID)` — 메세지의 텔리서비스 ID를 설정한다.

## 생성자 상세

### Message

```java
public Message(byte[] data)
```

- 단말로부터 메세지를 읽어들인 버퍼 Object를 생성한다.

### Message

```java
public Message(String addr,
               byte[] data)
```

**Parameters:**
- `data` - 메세지 내용

### Message

```java
public Message(String addr,
               byte[] data,
               int off,
               int len)
```

**Parameters:**
- `len` - 메세지 버퍼의 길이

### getIndex

```java
public byte getIndex()
```

**Returns:**
- 메세지 인덱스

### setIndex

```java
public void setIndex(byte newIndex)
```

- 메세지의 인덱스를 설정한다.

### getTeleServiceID

```java
public int getTeleServiceID()
```

**Returns:**
- 텔리서비스 ID

### setTeleServiceID

```java
public void setTeleServiceID(int newTeleServiceID)
```

- 메세지의 텔리서비스 ID를 설정한다.

### getClassification

```java
public byte getClassification()
```

- 메세지의 상태를 리턴한다.

### setClassification

```java
public void setClassification(byte newClassification)
```

- 메세지의 상태를 설정한다.(Local Object에 대해서만 사용가능)

### getData

```java
public byte[] getData()
```

**Returns:**
- 메세지 버퍼

### getLength

```java
public int getLength()
```

**Returns:**
- 메세지 길이

### setLength

```java
public int setLength(int val)
```

**Parameters:**
- `val` - 메세지 길이

**Returns:**
- 설정된 길이

### getOffset

```java
public int getOffset()
```

**Returns:**
- 메세지 버퍼의 오프셋

### setOffset

```java
public int setOffset(int val)
```

**Returns:**
- 설정된 오프셋

### getAddress

```java
public String getAddress()
```

**Returns:**
- 메세지 주소

### setAddress

```java
public void setAddress(String addr)
```

**Parameters:**
- `addr` - 메세지 주소

### getAddressInt

```java
public int getAddressInt()
```

**Returns:**
- 정수형 주소값

### setAddressInt

```java
public void setAddressInt(int addr)
```

**Parameters:**
- `addr` - 정수형 주소값

### getDate

```java
public Date getDate()
```

**Returns:**
- 성공: 메세지 전송시간, 실패: 전송시간을 알 수 없을 경우 null

### setDate

```java
public void setDate(Date date)
```

**Parameters:**
- `date` - java.util.Date 형의 전송시간## 메서드 상세

### getIndex

```java
public byte getIndex()
```

**Returns:**
- 메세지 인덱스

### setIndex

```java
public void setIndex(byte newIndex)
```

- 메세지의 인덱스를 설정한다.

### getTeleServiceID

```java
public int getTeleServiceID()
```

**Returns:**
- 텔리서비스 ID

### setTeleServiceID

```java
public void setTeleServiceID(int newTeleServiceID)
```

- 메세지의 텔리서비스 ID를 설정한다.

### getClassification

```java
public byte getClassification()
```

- 메세지의 상태를 리턴한다.

### setClassification

```java
public void setClassification(byte newClassification)
```

- 메세지의 상태를 설정한다.(Local Object에 대해서만 사용가능)

### getData

```java
public byte[] getData()
```

**Returns:**
- 메세지 버퍼

### getLength

```java
public int getLength()
```

**Returns:**
- 메세지 길이

### setLength

```java
public int setLength(int val)
```

**Parameters:**
- `val` - 메세지 길이

**Returns:**
- 설정된 길이

### getOffset

```java
public int getOffset()
```

**Returns:**
- 메세지 버퍼의 오프셋

### setOffset

```java
public int setOffset(int val)
```

**Returns:**
- 설정된 오프셋

### getAddress

```java
public String getAddress()
```

**Returns:**
- 메세지 주소

### setAddress

```java
public void setAddress(String addr)
```

**Parameters:**
- `addr` - 메세지 주소

### getAddressInt

```java
public int getAddressInt()
```

**Returns:**
- 정수형 주소값

### setAddressInt

```java
public void setAddressInt(int addr)
```

**Parameters:**
- `addr` - 정수형 주소값

### getDate

```java
public Date getDate()
```

**Returns:**
- 성공: 메세지 전송시간, 실패: 전송시간을 알 수 없을 경우 null

### setDate

```java
public void setDate(Date date)
```

**Parameters:**
- `date` - java.util.Date 형의 전송시간

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
