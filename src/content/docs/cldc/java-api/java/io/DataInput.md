---
title: "Interface DataInput"
---

`package java.io`

```text
public void readFully(byte[] b)
               throws IOException
```

## 설명

**Parameters:**
- `b` - 데이터를 읽어들이는 버퍼

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readFully

**Parameters:**
- `len` - 읽을 바이트 수를 지정하는 정수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### skipBytes

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readBoolean

**Returns:**
- 읽은 `boolean` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readByte

**Returns:**
- 읽은 8비트 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readUnsignedByte

**Returns:**
- 읽은 부호 없는 8비트 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readShort

**Returns:**
- 읽은 16비트 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readUnsignedShort

**Returns:**
- 읽은 부호 없는 16비트 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readChar

**Returns:**
- 읽은 유니코드 `char`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readInt

**Returns:**
- 읽은 `int` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readLong

**Returns:**
- 읽은 `long` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readFloat

**Returns:**
- 읽은 `float` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

### readDouble

**Returns:**
- 읽은 `double` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

### readUTF

**Returns:**
- 유니코드 문자열

**Throws:**
- `UTFDataFormatException` - 바이트가 문자열의 유효한 
 UTF-8 인코딩을 나타내지 않는 경우

## 메서드 요약

- `boolean readBoolean ()` — 1바이트의 입력을 읽어 이 바이트가 0이 아니면 true , 0이면 false 를 반환합니다.
- `byte readByte ()` — 1바이트의 입력을 읽고 반환합니다.
- `char readChar ()` — 입력 char 를 읽고 char 값을 반환합니다.
- `double readDouble ()` — 8바이트의 입력을 읽고 double 값을 반환합니다.
- `float readFloat ()` — 4바이트의 입력을 읽고 float 값을 반환합니다.
- `void readFully (byte[] b)` — 입력 스트림에서 일부 바이트를 읽어 버퍼 배열 b 에 저장합니다.
- `void readFully (byte[] b, int off, int len)` — 입력 스트림에서 len 바이트를 읽습니다.
- `int readInt ()` — 4바이트의 입력을 읽고 int 값을 반환합니다.
- `long readLong ()` — 8바이트의 입력을 읽고 long 값을 반환합니다.
- `short readShort ()` — 2바이트의 입력을 읽고 short 값을 반환합니다.
- `int readUnsignedByte ()` — 1바이트의 입력을 읽고 int 유형으로 zero-extend하여 0 에서 255 사이의 결과 값을 반환합니다.
- `int readUnsignedShort ()` — 2바이트의 입력을 읽고 int 유형으로 zero-extend하여 0 에서 65535 사이의 int 값을 반환합니다.
- `String readUTF ()` — 수정된 UTF-8 형식을 사용하여 인코딩된 문자열을 읽습니다.
- `int skipBytes (int n)` — 건너뛴 바이트를 삭제하면서 입력 스트림에서 n 바이트의 데이터를 건너뛰려고 시도합니다.

## 메서드 상세

### readFully

```java
public void readFully(byte[] b)
               throws IOException
```

**Parameters:**
- `b` - 데이터를 읽어들이는 버퍼

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readFully

```java
public void readFully(byte[] b,
                      int off,
                      int len)
               throws IOException
```

**Parameters:**
- `len` - 읽을 바이트 수를 지정하는 정수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### skipBytes

```java
public int skipBytes(int n)
              throws IOException
```

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readBoolean

```java
public boolean readBoolean()
                    throws IOException
```

**Returns:**
- 읽은 `boolean` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readByte

```java
public byte readByte()
              throws IOException
```

**Returns:**
- 읽은 8비트 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readUnsignedByte

```java
public int readUnsignedByte()
                     throws IOException
```

**Returns:**
- 읽은 부호 없는 8비트 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readShort

```java
public short readShort()
                throws IOException
```

**Returns:**
- 읽은 16비트 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readUnsignedShort

```java
public int readUnsignedShort()
                      throws IOException
```

**Returns:**
- 읽은 부호 없는 16비트 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readChar

```java
public char readChar()
              throws IOException
```

**Returns:**
- 읽은 유니코드 `char`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readInt

```java
public int readInt()
            throws IOException
```

**Returns:**
- 읽은 `int` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readLong

```java
public long readLong()
              throws IOException
```

**Returns:**
- 읽은 `long` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readFloat

```java
public float readFloat()
                throws IOException
```

**Returns:**
- 읽은 `float` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

### readDouble

```java
public double readDouble()
                  throws IOException
```

**Returns:**
- 읽은 `double` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

### readUTF

```java
public String readUTF()
               throws IOException
```

**Returns:**
- 유니코드 문자열

**Throws:**
- `UTFDataFormatException` - 바이트가 문자열의 유효한 
 UTF-8 인코딩을 나타내지 않는 경우
