# Interface DataInput

`package java.io`

```text
public void readFully(byte[] b)
               throws IOException
```

## 설명

**Parameters:**
- `b` - 읽은 정보를 저장할 배열.

**Throws:**
- `IOException` -

### readFully

**Parameters:**
- `len` - 읽을 정보 갯수.

**Throws:**
- `IOException` -

### skipBytes

**Parameters:**
- `n` - 건너 뛸 갯수.

**Returns:**
- 실제로 건너 뛴 갯수.

**Throws:**
- `IOException` -

### readBoolean

**Returns:**
- boolean 값.

**Throws:**
- `IOException` -

### readByte

**Returns:**
- 읽은 한 signed 바이트.

**Throws:**
- `IOException` -

### readUnsignedByte

**Returns:**
- 읽은 한 unsigned 바이트가 변환된 정수값.

**Throws:**
- `IOException` -

### readShort

**Returns:**
- 읽은 signed short형 정보.

**Throws:**
- `IOException` -

### readUnsignedShort

**Returns:**
- 읽은 두 unsigned short가 변환된 정수값.

**Throws:**
- `IOException` -

### readChar

**Returns:**
- 읽은 char형 정보.

**Throws:**
- `IOException` -

### readInt

**Returns:**
- 읽은 정수형 정보.

**Throws:**
- `IOException` -

### readLong

**Returns:**
- 읽은 Long형 정보.

**Throws:**
- `IOException` -

### readFloat

### readDouble

### readUTF

**Returns:**
- 문자열.

**Throws:**
- `IOException` -## 메서드 요약

- `boolean readBoolean ()` — 입력 스트림에서 한 바이트를 읽은 뒤 0이 아니면 true 0이면 false를 리턴한다.
- `byte readByte ()` — 입력 스트림에서 한 바이트를 읽는다.
- `char readChar ()` — 입력 스트림에서 char형 정보를 읽는다.
- `double readDouble ()`
- `float readFloat ()`
- `void readFully (byte[] b)` — 바이트 배열로 정보를 읽는다.
- `void readFully (byte[] b, int off, int len)` — 바이트 배열 일부분으로 정보를 읽는다.
- `int readInt ()` — 입력 스트림에서 정수형 정보를 읽는다.
- `long readLong ()` — 입력 스트림에서 Long형 정보를 읽는다.
- `short readShort ()` — 입력 스트림에서 두 바이트를 읽는다.
- `int readUnsignedByte ()` — 입력 스트림에서 한 바이트를 읽고 unsigned 바이트로 처리해 정수형 정보로 변환 후 리턴한다.
- `int readUnsignedShort ()` — 입력 스트림에서 두 바이트를 읽고 unsigned short로 처리해 정수형 정보로 변환 후 리턴한다.
- `String readUTF ()` — 입력 스트림에서 UTF형식 정보를 읽어 문자열을 만들어 리턴한다.
- `int skipBytes (int n)` — 입력 스트림에서 정보를 읽지 않고 건너뛴다.

## 메서드 상세

### readFully

```java
public void readFully(byte[] b)
               throws IOException
```

**Parameters:**
- `b` - 읽은 정보를 저장할 배열.

**Throws:**
- `IOException` -

### readFully

```java
public void readFully(byte[] b,
                      int off,
                      int len)
               throws IOException
```

**Parameters:**
- `len` - 읽을 정보 갯수.

**Throws:**
- `IOException` -

### skipBytes

```java
public int skipBytes(int n)
              throws IOException
```

**Parameters:**
- `n` - 건너 뛸 갯수.

**Returns:**
- 실제로 건너 뛴 갯수.

**Throws:**
- `IOException` -

### readBoolean

```java
public boolean readBoolean()
                    throws IOException
```

**Returns:**
- boolean 값.

**Throws:**
- `IOException` -

### readByte

```java
public byte readByte()
              throws IOException
```

**Returns:**
- 읽은 한 signed 바이트.

**Throws:**
- `IOException` -

### readUnsignedByte

```java
public int readUnsignedByte()
                     throws IOException
```

**Returns:**
- 읽은 한 unsigned 바이트가 변환된 정수값.

**Throws:**
- `IOException` -

### readShort

```java
public short readShort()
                throws IOException
```

**Returns:**
- 읽은 signed short형 정보.

**Throws:**
- `IOException` -

### readUnsignedShort

```java
public int readUnsignedShort()
                      throws IOException
```

**Returns:**
- 읽은 두 unsigned short가 변환된 정수값.

**Throws:**
- `IOException` -

### readChar

```java
public char readChar()
              throws IOException
```

**Returns:**
- 읽은 char형 정보.

**Throws:**
- `IOException` -

### readInt

```java
public int readInt()
            throws IOException
```

**Returns:**
- 읽은 정수형 정보.

**Throws:**
- `IOException` -

### readLong

```java
public long readLong()
              throws IOException
```

**Returns:**
- 읽은 Long형 정보.

**Throws:**
- `IOException` -

### readFloat

```java
public float readFloat()
                throws IOException
```

### readDouble

```java
public double readDouble()
                  throws IOException
```

### readUTF

```java
public String readUTF()
               throws IOException
```

**Returns:**
- 문자열.

**Throws:**
- `IOException` -

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
