---
title: "Class DataInputStream"
---

`package java.io`

```text
java.lang.Object
  |
  +--java.io.InputStream
        |
        +--java.io.DataInputStream
```

## 설명

**All Implemented Interfaces:**
- `DataInput`

**implements DataInput:**

데이터 입력 스트림은 
 응용 프로그램이 시스템에 독립적인 방법으로 
 기본 입력 스트림에서 프리미티브 Java 데이터 유형을 읽을 수 있도록 합니다. 
 응용 프로그램은 데이터 출력 스트림을 사용하여 나중에 데이터 입력 스트림이 읽을 수 있도록 데이터를 씁니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``DataOutputStream``

## 필드 요약

- `protected InputStream in` — 입력 스트림

## 생성자 요약

- DataInputStream ( InputStream in) DataInputStream 을 만들고, 
 나중에 사용할 수 있도록 그 인자인 입력 스트림 in 을 저장합니다.

## 메서드 요약

- `int available ()` — 차단되지 않고 이 입력 스트림에서 읽을 수 있는 바이트 수를 반환합니다.
- `void close ()` — 이 입력 스트림을 닫고 스트림과 연결된 시스템 자원을 해제합니다.
- `void mark (int readlimit)` — 이 입력 스트림에서의 현재 위치를 표시합니다.
- `boolean markSupported ()` — 이 입력 스트림이 mark 및 reset 메소드를 지원하는지 테스트합니다.
- `int read ()` — 이 입력 스트림에서 다음 바이트의 데이터를 읽습니다.
- `int read (byte[] b)` — DataInput 의 read 메소드 일반 계약을 참조하십시오.
- `int read (byte[] b, int off, int len)` — 이 입력 스트림에서 최대 len 바이트의 데이터를 바이트 배열로 읽어 옵니다.
- `boolean readBoolean ()` — DataInput 의 readBoolean 메소드 일반 계약을 참조하십시오.
- `byte readByte ()` — DataInput 의 readByte 메소드 일반 계약을 참조하십시오.
- `char readChar ()` — DataInput 의 readChar 메소드 일반 계약을 참조하십시오.
- `double readDouble ()` — DataInput 의 readDouble 메소드 일반 계약을 참조하십시오.
- `float readFloat ()` — DataInput 의 readFloat 메소드 일반 계약을 참조하십시오.
- `void readFully (byte[] b)` — DataInput 의 readFully 메소드 일반 계약을 참조하십시오.
- `void readFully (byte[] b, int off, int len)` — DataInput 의 readFully 메소드 일반 계약을 참조하십시오.
- `int readInt ()` — DataInput 의 readInt 메소드 일반 계약을 참조하십시오.
- `long readLong ()` — DataInput 의 readLong 메소드 일반 계약을 참조하십시오.
- `short readShort ()` — DataInput 의 readShort 메소드 일반 계약을 참조하십시오.
- `int readUnsignedByte ()` — DataInput 의 readUnsignedByte 메소드 일반 계약을 참조하십시오.
- `int readUnsignedShort ()` — DataInput 의 readUnsignedShort 메소드 일반 계약을 참조하십시오.
- `String readUTF ()` — DataInput 의 readUTF 메소드 일반 계약을 참조하십시오.
- `static String readUTF ( DataInput in)` — 스트림 in 에서 Java로 수정된 UTF-8 형식으로 인코딩된 유니코드 문자열의 표현을 읽습니다.
- `void reset ()` — 이 입력 스트림에서 mark 메소드를 마지막으로 호출했을 때의 위치에 다시 스트림을 놓습니다.
- `long skip (long n)` — 입력 스트림에서 n 바이트의 데이터를 건너뛰어 무시합니다.
- `int skipBytes (int n)` — DataInput 의 skipBytes 메소드 일반 계약을 참조하십시오.

## 필드 상세

### in

```java
protected InputStream in
```

- 입력 스트림

### DataInputStream

```java
public DataInputStream(InputStream in)
```

- `DataInputStream`을 만들고, 
 나중에 사용할 수 있도록 그 인자인 입력 스트림 
 `in`을 저장합니다.

**Parameters:**
- `in` - 입력 스트림

### read

```java
public int read()
         throws IOException
```

**Specified by:**
- `read` in class `InputStream`

**Returns:**
- 다음 바이트의 데이터 또는 스트림의 끝에 도달한 경우
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public final int read(byte[] b)
               throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `b` - 데이터를 읽어들이는 버퍼

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 또는 
 스트림의 끝에 도달하여 더 이상 데이터가 없는 경우
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``InputStream.read(byte[], int, int)``

### read

```java
public final int read(byte[] b,
                      int off,
                      int len)
               throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `len` - 읽는 최대 바이트 수

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 또는 
 스트림의 끝에 도달하여 더 이상 데이터가 없는 경우 
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``InputStream.read()``

### readFully

```java
public final void readFully(byte[] b)
                     throws IOException
```

**Specified by:**
- `readFully` in interface `DataInput`

**Parameters:**
- `b` - 데이터를 읽어들이는 버퍼

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readFully

```java
public final void readFully(byte[] b,
                            int off,
                            int len)
                     throws IOException
```

**Specified by:**
- `readFully` in interface `DataInput`

**Parameters:**
- `len` - 읽을 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### skipBytes

```java
public final int skipBytes(int n)
                    throws IOException
```

**Specified by:**
- `skipBytes` in interface `DataInput`

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readBoolean

```java
public final boolean readBoolean()
                          throws IOException
```

**Specified by:**
- `readBoolean` in interface `DataInput`

**Returns:**
- 읽은 `boolean` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readByte

```java
public final byte readByte()
                    throws IOException
```

**Specified by:**
- `readByte` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 바이트(부호 있는 
 8비트 `byte`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readUnsignedByte

```java
public final int readUnsignedByte()
                           throws IOException
```

**Specified by:**
- `readUnsignedByte` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 바이트
 (부호 없는 8비트 숫자)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readShort

```java
public final short readShort()
                      throws IOException
```

**Specified by:**
- `readShort` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 2바이트
 (부호 있는 16비트 숫자)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readUnsignedShort

```java
public final int readUnsignedShort()
                            throws IOException
```

**Specified by:**
- `readUnsignedShort` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 2바이트
 (부호 없는 16비트 정수)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readChar

```java
public final char readChar()
                    throws IOException
```

**Specified by:**
- `readChar` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 2바이트
 (유니코드 문자)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readInt

```java
public final int readInt()
                  throws IOException
```

**Specified by:**
- `readInt` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 4바이트
 (`int`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readLong

```java
public final long readLong()
                    throws IOException
```

**Specified by:**
- `readLong` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 8바이트
 (`long`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readFloat

```java
public final float readFloat()
                      throws IOException
```

**Specified by:**
- `readFloat` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 4바이트
 (`float`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``readInt()``, 
``Float.intBitsToFloat(int)``

### readDouble

```java
public final double readDouble()
                        throws IOException
```

**Specified by:**
- `readDouble` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 8바이트
 (`double`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``readLong()``, 
``Double.longBitsToDouble(long)``

### readUTF

```java
public final String readUTF()
                     throws IOException
```

**Specified by:**
- `readUTF` in interface `DataInput`

**Returns:**
- 유니코드 문자열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``readUTF(java.io.DataInput)``

### readUTF

```java
public static final String readUTF(DataInput in)
                            throws IOException
```

**Parameters:**
- `in` - 데이터 입력 스트림

**Returns:**
- 유니코드 문자열

**Throws:**
- `UTFDataFormatException` - 바이트가 유니코드 문자열의 
 유효한 UTF-8 인코딩을 나타내지 않는 경우

**See Also:**
- ``readUnsignedShort()``

### skip

```java
public long skip(long n)
          throws IOException
```

**Overrides:**
- `skip` in class `InputStream`

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### available

```java
public int available()
              throws IOException
```

**Overrides:**
- `available` in class `InputStream`

**Returns:**
- 차단되지 않고 입력 스트림에서 
 읽을 수 있는 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `InputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### mark

```java
public void mark(int readlimit)
```

**Overrides:**
- `mark` in class `InputStream`

**Parameters:**
- `readlimit` - 표시 위치가 무효화될 때까지 읽을 수 있는 
 최대 바이트 수 한계

**See Also:**
- ``InputStream.reset()``

### reset

```java
public void reset()
           throws IOException
```

**Overrides:**
- `reset` in class `InputStream`

**Throws:**
- `IOException` - 스트림이 표시되어 있지 않거나 
 표시가 무효화된 경우

**See Also:**
- ``InputStream.mark(int)``, 
``IOException``

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 이 입력 유형이 `mark` 및 
 `reset` 메소드를 지원하면 
 `true`, 지원하지 않으면 `false`

**See Also:**
- ``InputStream.mark(int)``, 
``InputStream.reset()``

## 생성자 상세

### DataInputStream

```java
public DataInputStream(InputStream in)
```

- `DataInputStream`을 만들고, 
 나중에 사용할 수 있도록 그 인자인 입력 스트림 
 `in`을 저장합니다.

**Parameters:**
- `in` - 입력 스트림

### read

```java
public int read()
         throws IOException
```

**Specified by:**
- `read` in class `InputStream`

**Returns:**
- 다음 바이트의 데이터 또는 스트림의 끝에 도달한 경우
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public final int read(byte[] b)
               throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `b` - 데이터를 읽어들이는 버퍼

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 또는 
 스트림의 끝에 도달하여 더 이상 데이터가 없는 경우
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``InputStream.read(byte[], int, int)``

### read

```java
public final int read(byte[] b,
                      int off,
                      int len)
               throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `len` - 읽는 최대 바이트 수

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 또는 
 스트림의 끝에 도달하여 더 이상 데이터가 없는 경우 
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``InputStream.read()``

### readFully

```java
public final void readFully(byte[] b)
                     throws IOException
```

**Specified by:**
- `readFully` in interface `DataInput`

**Parameters:**
- `b` - 데이터를 읽어들이는 버퍼

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readFully

```java
public final void readFully(byte[] b,
                            int off,
                            int len)
                     throws IOException
```

**Specified by:**
- `readFully` in interface `DataInput`

**Parameters:**
- `len` - 읽을 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### skipBytes

```java
public final int skipBytes(int n)
                    throws IOException
```

**Specified by:**
- `skipBytes` in interface `DataInput`

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readBoolean

```java
public final boolean readBoolean()
                          throws IOException
```

**Specified by:**
- `readBoolean` in interface `DataInput`

**Returns:**
- 읽은 `boolean` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readByte

```java
public final byte readByte()
                    throws IOException
```

**Specified by:**
- `readByte` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 바이트(부호 있는 
 8비트 `byte`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readUnsignedByte

```java
public final int readUnsignedByte()
                           throws IOException
```

**Specified by:**
- `readUnsignedByte` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 바이트
 (부호 없는 8비트 숫자)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readShort

```java
public final short readShort()
                      throws IOException
```

**Specified by:**
- `readShort` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 2바이트
 (부호 있는 16비트 숫자)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readUnsignedShort

```java
public final int readUnsignedShort()
                            throws IOException
```

**Specified by:**
- `readUnsignedShort` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 2바이트
 (부호 없는 16비트 정수)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readChar

```java
public final char readChar()
                    throws IOException
```

**Specified by:**
- `readChar` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 2바이트
 (유니코드 문자)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readInt

```java
public final int readInt()
                  throws IOException
```

**Specified by:**
- `readInt` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 4바이트
 (`int`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readLong

```java
public final long readLong()
                    throws IOException
```

**Specified by:**
- `readLong` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 8바이트
 (`long`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readFloat

```java
public final float readFloat()
                      throws IOException
```

**Specified by:**
- `readFloat` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 4바이트
 (`float`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``readInt()``, 
``Float.intBitsToFloat(int)``

### readDouble

```java
public final double readDouble()
                        throws IOException
```

**Specified by:**
- `readDouble` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 8바이트
 (`double`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``readLong()``, 
``Double.longBitsToDouble(long)``

### readUTF

```java
public final String readUTF()
                     throws IOException
```

**Specified by:**
- `readUTF` in interface `DataInput`

**Returns:**
- 유니코드 문자열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``readUTF(java.io.DataInput)``

### readUTF

```java
public static final String readUTF(DataInput in)
                            throws IOException
```

**Parameters:**
- `in` - 데이터 입력 스트림

**Returns:**
- 유니코드 문자열

**Throws:**
- `UTFDataFormatException` - 바이트가 유니코드 문자열의 
 유효한 UTF-8 인코딩을 나타내지 않는 경우

**See Also:**
- ``readUnsignedShort()``

### skip

```java
public long skip(long n)
          throws IOException
```

**Overrides:**
- `skip` in class `InputStream`

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### available

```java
public int available()
              throws IOException
```

**Overrides:**
- `available` in class `InputStream`

**Returns:**
- 차단되지 않고 입력 스트림에서 
 읽을 수 있는 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `InputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### mark

```java
public void mark(int readlimit)
```

**Overrides:**
- `mark` in class `InputStream`

**Parameters:**
- `readlimit` - 표시 위치가 무효화될 때까지 읽을 수 있는 
 최대 바이트 수 한계

**See Also:**
- ``InputStream.reset()``

### reset

```java
public void reset()
           throws IOException
```

**Overrides:**
- `reset` in class `InputStream`

**Throws:**
- `IOException` - 스트림이 표시되어 있지 않거나 
 표시가 무효화된 경우

**See Also:**
- ``InputStream.mark(int)``, 
``IOException``

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 이 입력 유형이 `mark` 및 
 `reset` 메소드를 지원하면 
 `true`, 지원하지 않으면 `false`

**See Also:**
- ``InputStream.mark(int)``, 
``InputStream.reset()``

## 메서드 상세

### read

```java
public int read()
         throws IOException
```

**Specified by:**
- `read` in class `InputStream`

**Returns:**
- 다음 바이트의 데이터 또는 스트림의 끝에 도달한 경우
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public final int read(byte[] b)
               throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `b` - 데이터를 읽어들이는 버퍼

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 또는 
 스트림의 끝에 도달하여 더 이상 데이터가 없는 경우
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``InputStream.read(byte[], int, int)``

### read

```java
public final int read(byte[] b,
                      int off,
                      int len)
               throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `len` - 읽는 최대 바이트 수

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 또는 
 스트림의 끝에 도달하여 더 이상 데이터가 없는 경우 
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``InputStream.read()``

### readFully

```java
public final void readFully(byte[] b)
                     throws IOException
```

**Specified by:**
- `readFully` in interface `DataInput`

**Parameters:**
- `b` - 데이터를 읽어들이는 버퍼

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readFully

```java
public final void readFully(byte[] b,
                            int off,
                            int len)
                     throws IOException
```

**Specified by:**
- `readFully` in interface `DataInput`

**Parameters:**
- `len` - 읽을 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### skipBytes

```java
public final int skipBytes(int n)
                    throws IOException
```

**Specified by:**
- `skipBytes` in interface `DataInput`

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readBoolean

```java
public final boolean readBoolean()
                          throws IOException
```

**Specified by:**
- `readBoolean` in interface `DataInput`

**Returns:**
- 읽은 `boolean` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readByte

```java
public final byte readByte()
                    throws IOException
```

**Specified by:**
- `readByte` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 바이트(부호 있는 
 8비트 `byte`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readUnsignedByte

```java
public final int readUnsignedByte()
                           throws IOException
```

**Specified by:**
- `readUnsignedByte` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 바이트
 (부호 없는 8비트 숫자)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readShort

```java
public final short readShort()
                      throws IOException
```

**Specified by:**
- `readShort` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 2바이트
 (부호 있는 16비트 숫자)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readUnsignedShort

```java
public final int readUnsignedShort()
                            throws IOException
```

**Specified by:**
- `readUnsignedShort` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 2바이트
 (부호 없는 16비트 정수)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readChar

```java
public final char readChar()
                    throws IOException
```

**Specified by:**
- `readChar` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 2바이트
 (유니코드 문자)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readInt

```java
public final int readInt()
                  throws IOException
```

**Specified by:**
- `readInt` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 4바이트
 (`int`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readLong

```java
public final long readLong()
                    throws IOException
```

**Specified by:**
- `readLong` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 8바이트
 (`long`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### readFloat

```java
public final float readFloat()
                      throws IOException
```

**Specified by:**
- `readFloat` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 4바이트
 (`float`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``readInt()``, 
``Float.intBitsToFloat(int)``

### readDouble

```java
public final double readDouble()
                        throws IOException
```

**Specified by:**
- `readDouble` in interface `DataInput`

**Returns:**
- 이 입력 스트림의 다음 8바이트
 (`double`)

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``readLong()``, 
``Double.longBitsToDouble(long)``

### readUTF

```java
public final String readUTF()
                     throws IOException
```

**Specified by:**
- `readUTF` in interface `DataInput`

**Returns:**
- 유니코드 문자열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``readUTF(java.io.DataInput)``

### readUTF

```java
public static final String readUTF(DataInput in)
                            throws IOException
```

**Parameters:**
- `in` - 데이터 입력 스트림

**Returns:**
- 유니코드 문자열

**Throws:**
- `UTFDataFormatException` - 바이트가 유니코드 문자열의 
 유효한 UTF-8 인코딩을 나타내지 않는 경우

**See Also:**
- ``readUnsignedShort()``

### skip

```java
public long skip(long n)
          throws IOException
```

**Overrides:**
- `skip` in class `InputStream`

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### available

```java
public int available()
              throws IOException
```

**Overrides:**
- `available` in class `InputStream`

**Returns:**
- 차단되지 않고 입력 스트림에서 
 읽을 수 있는 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `InputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### mark

```java
public void mark(int readlimit)
```

**Overrides:**
- `mark` in class `InputStream`

**Parameters:**
- `readlimit` - 표시 위치가 무효화될 때까지 읽을 수 있는 
 최대 바이트 수 한계

**See Also:**
- ``InputStream.reset()``

### reset

```java
public void reset()
           throws IOException
```

**Overrides:**
- `reset` in class `InputStream`

**Throws:**
- `IOException` - 스트림이 표시되어 있지 않거나 
 표시가 무효화된 경우

**See Also:**
- ``InputStream.mark(int)``, 
``IOException``

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 이 입력 유형이 `mark` 및 
 `reset` 메소드를 지원하면 
 `true`, 지원하지 않으면 `false`

**See Also:**
- ``InputStream.mark(int)``, 
``InputStream.reset()``
