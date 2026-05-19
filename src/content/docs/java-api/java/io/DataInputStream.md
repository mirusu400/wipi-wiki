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

바이트 정보를 읽어서 다른 타입의 정보로 변환할 수 있도록 
 만든 입력스트림 클래스.

## 필드 요약

- `protected InputStream in` — 실제 바이트 정보를 읽어올 입력 스트림.

## 생성자 요약

- DataInputStream ( InputStream in) 새로운 객체를 만든다.

## 메서드 요약

- `int available ()` — 입력 스트림에서 읽을 수 있는 정보량을 구한다.
- `void close ()` — 입력 스트림을 닫는다.
- `void mark (int readlimit)` — 입력 스트림에 mark정보를 설정한다.
- `boolean markSupported ()` — 입력 스트림이 mark기능을 지원하는지 여부를 구한다.
- `int read ()` — 한 바이트를 읽는다.
- `int read (byte[] b)` — 바이트 배열로 읽어 들인다.
- `int read (byte[] b, int off, int len)` — 바이트 배열 일부분으로 읽어 들인다.
- `boolean readBoolean ()` — 입력 스트림에서 한 바이트를 읽은 뒤 0이 아니면 true 0이면 false를 리턴한다.
- `byte readByte ()` — 입력 스트림에서 한 바이트를 읽는다.
- `char readChar ()` — 입력 스트림에서 char형 정보를 읽는다.
- `double readDouble ()`
- `float readFloat ()`
- `void readFully (byte[] b)` — 바이트 배열로 읽어 들인다. read와 다른 점은 바이트 배열이 다 차기 전에 입력받을 정보가 없어지면 EOFException을 발생한다는 점이다.
- `void readFully (byte[] b, int off, int len)` — 바이트 배열 일부분으로 읽어 들인다. read와 다른 점은 원하는 양만큼 읽기 전에 입력받을 정보가 없어지면 EOFException을 발생한다는 점이다.
- `int readInt ()` — 입력 스트림에서 정수형 정보를 읽는다.
- `long readLong ()` — 입력 스트림에서 Long형 정보를 읽는다.
- `short readShort ()` — 입력 스트림에서 두 바이트를 읽는다.
- `int readUnsignedByte ()` — 입력 스트림에서 한 바이트를 읽고 unsigned 바이트로 처리해 정수형 정보로 변환 후 리턴한다.
- `int readUnsignedShort ()` — 입력 스트림에서 두 바이트를 읽고 unsigned short로 처리해 정수형 정보로 변환 후 리턴한다.
- `String readUTF ()` — 입력 스트림에서 UTF형식 정보를 읽어 문자열을 만들어 리턴한다.
- `static String readUTF ( DataInput in)` — 특정 입력 스트림에서 UTF형식 정보를 읽어 문자열을 만들어 리턴한다.
- `void reset ()` — 입력 스트림의 읽는 위치를 mark정보에 설정된 위치로 변경한다.
- `long skip (long n)` — 입력 스트림에서 정보를 읽지 않고 건너뛴다.
- `int skipBytes (int n)` — 입력 스트림에서 정보를 읽지 않고 건너뛴다.

## 필드 상세

### in

```java
protected InputStream in
```

- 실제 바이트 정보를 읽어올 입력 스트림.

### DataInputStream

```java
public DataInputStream(InputStream in)
```

**Parameters:**
- `in` - 실제 바이트 정보를 읽어올 입력 스트림.

### read

```java
public int read()
         throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Returns:**
- 읽은 바이트 정보.

**Throws:**
- `IOException` -

### read

```java
public final int read(byte[] b)
               throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `b` - 읽은 정보가 저장될 바이트 배열.

**Returns:**
- 실제 읽은 바이트 수, 읽은 바이트가 없으면 -1.

**Throws:**
- `IOException` -

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
- `len` - 읽을 바이트 수.

**Returns:**
- 실제 읽은 바이트 수, 읽은 바이트가 없으면 -1.

**Throws:**
- `IOException` -

### readFully

```java
public final void readFully(byte[] b)
                     throws IOException
```

**Specified by:**
- `readFully` in interface `DataInput`

**Parameters:**
- `b` - 읽은 정보가 저장될 바이트 배열.

**Throws:**
- `EOFException` - 읽을 량을 채우지 못할  발생.

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
- `len` - 읽을 바이트 수.

**Throws:**
- `IOException` -

### skipBytes

```java
public final int skipBytes(int n)
                    throws IOException
```

**Specified by:**
- `skipBytes` in interface `DataInput`

**Parameters:**
- `n` - 건너 뛸 갯수.

**Returns:**
- 실제로 건너 뛴 갯수.

**Throws:**
- `IOException` -

### mark

```java
public void mark(int readlimit)
```

**Overrides:**
- `mark` in class `InputStream`

### reset

```java
public void reset()
           throws IOException
```

**Overrides:**
- `reset` in class `InputStream`

**Throws:**
- `IOException` -

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 지원하면 true 아니면 false.

### readBoolean

```java
public final boolean readBoolean()
                          throws IOException
```

**Specified by:**
- `readBoolean` in interface `DataInput`

**Returns:**
- boolean 값.

**Throws:**
- `IOException` -

### readByte

```java
public final byte readByte()
                    throws IOException
```

**Specified by:**
- `readByte` in interface `DataInput`

**Returns:**
- 읽은 한 signed 바이트.

**Throws:**
- `IOException` -

### readUnsignedByte

```java
public final int readUnsignedByte()
                           throws IOException
```

**Specified by:**
- `readUnsignedByte` in interface `DataInput`

**Returns:**
- 읽은 한 unsigned 바이트가 변환된 정수값.

**Throws:**
- `IOException` -

### readChar

```java
public final char readChar()
                    throws IOException
```

**Specified by:**
- `readChar` in interface `DataInput`

**Returns:**
- 읽은 char형 정보.

**Throws:**
- `EOFException` - 2바이트를 읽을 수 없을 때 발생.

### readShort

```java
public final short readShort()
                      throws IOException
```

**Specified by:**
- `readShort` in interface `DataInput`

**Returns:**
- 읽은 signed short형 정보.

**Throws:**
- `EOFException` - 2바이트를 읽을 수 없을 때 발생.

### readUnsignedShort

```java
public final int readUnsignedShort()
                            throws IOException
```

**Specified by:**
- `readUnsignedShort` in interface `DataInput`

**Returns:**
- 읽은 두 unsigned short가 변환된 정수값.

**Throws:**
- `EOFException` - 2바이트를 읽을 수 없을 때 발생.

### readInt

```java
public final int readInt()
                  throws IOException
```

**Specified by:**
- `readInt` in interface `DataInput`

**Returns:**
- 읽은 정수형 정보.

**Throws:**
- `EOFException` - 4바이트를 읽을 수 없을 때 발생.

### readLong

```java
public final long readLong()
                    throws IOException
```

**Specified by:**
- `readLong` in interface `DataInput`

**Returns:**
- 읽은 Long형 정보.

**Throws:**
- `EOFException` - 8바이트를 읽을 수 없을 때 발생.

### readFloat

```java
public final float readFloat()
                      throws IOException
```

**Specified by:**
- `readFloat` in interface `DataInput`

### readDouble

```java
public final double readDouble()
                        throws IOException
```

**Specified by:**
- `readDouble` in interface `DataInput`

### readUTF

```java
public final String readUTF()
                     throws IOException
```

**Specified by:**
- `readUTF` in interface `DataInput`

**Returns:**
- 문자열.

**Throws:**
- `IOException` -

### readUTF

```java
public static final String readUTF(DataInput in)
                            throws IOException
```

**Parameters:**
- `in` - UTF형식 정보를 읽어들일 입력 스트림.

**Returns:**
- 문자열.

**Throws:**
- `IOException` -

### available

```java
public int available()
              throws IOException
```

**Overrides:**
- `taInput.html#readUTF()">readUTF` in interface `DataInput`

**Returns:**
- 臾몄

## 생성자 상세

### DataInputStream

```java
public DataInputStream(InputStream in)
```

**Parameters:**
- `in` - 실제 바이트 정보를 읽어올 입력 스트림.

### read

```java
public int read()
         throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Returns:**
- 읽은 바이트 정보.

**Throws:**
- `IOException` -

### read

```java
public final int read(byte[] b)
               throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `b` - 읽은 정보가 저장될 바이트 배열.

**Returns:**
- 실제 읽은 바이트 수, 읽은 바이트가 없으면 -1.

**Throws:**
- `IOException` -

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
- `len` - 읽을 바이트 수.

**Returns:**
- 실제 읽은 바이트 수, 읽은 바이트가 없으면 -1.

**Throws:**
- `IOException` -

### readFully

```java
public final void readFully(byte[] b)
                     throws IOException
```

**Specified by:**
- `readFully` in interface `DataInput`

**Parameters:**
- `b` - 읽은 정보가 저장될 바이트 배열.

**Throws:**
- `EOFException` - 읽을 량을 채우지 못할  발생.

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
- `len` - 읽을 바이트 수.

**Throws:**
- `IOException` -

### skipBytes

```java
public final int skipBytes(int n)
                    throws IOException
```

**Specified by:**
- `skipBytes` in interface `DataInput`

**Parameters:**
- `n` - 건너 뛸 갯수.

**Returns:**
- 실제로 건너 뛴 갯수.

**Throws:**
- `IOException` -

### mark

```java
public void mark(int readlimit)
```

**Overrides:**
- `mark` in class `InputStream`

### reset

```java
public void reset()
           throws IOException
```

**Overrides:**
- `reset` in class `InputStream`

**Throws:**
- `IOException` -

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 지원하면 true 아니면 false.

### readBoolean

```java
public final boolean readBoolean()
                          throws IOException
```

**Specified by:**
- `readBoolean` in interface `DataInput`

**Returns:**
- boolean 값.

**Throws:**
- `IOException` -

### readByte

```java
public final byte readByte()
                    throws IOException
```

**Specified by:**
- `readByte` in interface `DataInput`

**Returns:**
- 읽은 한 signed 바이트.

**Throws:**
- `IOException` -

### readUnsignedByte

```java
public final int readUnsignedByte()
                           throws IOException
```

**Specified by:**
- `readUnsignedByte` in interface `DataInput`

**Returns:**
- 읽은 한 unsigned 바이트가 변환된 정수값.

**Throws:**
- `IOException` -

### readChar

```java
public final char readChar()
                    throws IOException
```

**Specified by:**
- `readChar` in interface `DataInput`

**Returns:**
- 읽은 char형 정보.

**Throws:**
- `EOFException` - 2바이트를 읽을 수 없을 때 발생.

### readShort

```java
public final short readShort()
                      throws IOException
```

**Specified by:**
- `readShort` in interface `DataInput`

**Returns:**
- 읽은 signed short형 정보.

**Throws:**
- `EOFException` - 2바이트를 읽을 수 없을 때 발생.

### readUnsignedShort

```java
public final int readUnsignedShort()
                            throws IOException
```

**Specified by:**
- `readUnsignedShort` in interface `DataInput`

**Returns:**
- 읽은 두 unsigned short가 변환된 정수값.

**Throws:**
- `EOFException` - 2바이트를 읽을 수 없을 때 발생.

### readInt

```java
public final int readInt()
                  throws IOException
```

**Specified by:**
- `readInt` in interface `DataInput`

**Returns:**
- 읽은 정수형 정보.

**Throws:**
- `EOFException` - 4바이트를 읽을 수 없을 때 발생.

### readLong

```java
public final long readLong()
                    throws IOException
```

**Specified by:**
- `readLong` in interface `DataInput`

**Returns:**
- 읽은 Long형 정보.

**Throws:**
- `EOFException` - 8바이트를 읽을 수 없을 때 발생.

### readFloat

```java
public final float readFloat()
                      throws IOException
```

**Specified by:**
- `readFloat` in interface `DataInput`

### readDouble

```java
public final double readDouble()
                        throws IOException
```

**Specified by:**
- `readDouble` in interface `DataInput`

### readUTF

```java
public final String readUTF()
                     throws IOException
```

**Specified by:**
- `readUTF` in interface `DataInput`

**Returns:**
- 문자열.

**Throws:**
- `IOException` -

### readUTF

```java
public static final String readUTF(DataInput in)
                            throws IOException
```

**Parameters:**
- `in` - UTF형식 정보를 읽어들일 입력 스트림.

**Returns:**
- 문자열.

**Throws:**
- `IOException` -

### available

```java
public int available()
              throws IOException
```

**Overrides:**
- `taInput.html#readUTF()">readUTF` in interface `DataInput`

**Returns:**
- 臾몄

## 메서드 상세

### read

```java
public int read()
         throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Returns:**
- 읽은 바이트 정보.

**Throws:**
- `IOException` -

### read

```java
public final int read(byte[] b)
               throws IOException
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `b` - 읽은 정보가 저장될 바이트 배열.

**Returns:**
- 실제 읽은 바이트 수, 읽은 바이트가 없으면 -1.

**Throws:**
- `IOException` -

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
- `len` - 읽을 바이트 수.

**Returns:**
- 실제 읽은 바이트 수, 읽은 바이트가 없으면 -1.

**Throws:**
- `IOException` -

### readFully

```java
public final void readFully(byte[] b)
                     throws IOException
```

**Specified by:**
- `readFully` in interface `DataInput`

**Parameters:**
- `b` - 읽은 정보가 저장될 바이트 배열.

**Throws:**
- `EOFException` - 읽을 량을 채우지 못할  발생.

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
- `len` - 읽을 바이트 수.

**Throws:**
- `IOException` -

### skipBytes

```java
public final int skipBytes(int n)
                    throws IOException
```

**Specified by:**
- `skipBytes` in interface `DataInput`

**Parameters:**
- `n` - 건너 뛸 갯수.

**Returns:**
- 실제로 건너 뛴 갯수.

**Throws:**
- `IOException` -

### mark

```java
public void mark(int readlimit)
```

**Overrides:**
- `mark` in class `InputStream`

### reset

```java
public void reset()
           throws IOException
```

**Overrides:**
- `reset` in class `InputStream`

**Throws:**
- `IOException` -

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 지원하면 true 아니면 false.

### readBoolean

```java
public final boolean readBoolean()
                          throws IOException
```

**Specified by:**
- `readBoolean` in interface `DataInput`

**Returns:**
- boolean 값.

**Throws:**
- `IOException` -

### readByte

```java
public final byte readByte()
                    throws IOException
```

**Specified by:**
- `readByte` in interface `DataInput`

**Returns:**
- 읽은 한 signed 바이트.

**Throws:**
- `IOException` -

### readUnsignedByte

```java
public final int readUnsignedByte()
                           throws IOException
```

**Specified by:**
- `readUnsignedByte` in interface `DataInput`

**Returns:**
- 읽은 한 unsigned 바이트가 변환된 정수값.

**Throws:**
- `IOException` -

### readChar

```java
public final char readChar()
                    throws IOException
```

**Specified by:**
- `readChar` in interface `DataInput`

**Returns:**
- 읽은 char형 정보.

**Throws:**
- `EOFException` - 2바이트를 읽을 수 없을 때 발생.

### readShort

```java
public final short readShort()
                      throws IOException
```

**Specified by:**
- `readShort` in interface `DataInput`

**Returns:**
- 읽은 signed short형 정보.

**Throws:**
- `EOFException` - 2바이트를 읽을 수 없을 때 발생.

### readUnsignedShort

```java
public final int readUnsignedShort()
                            throws IOException
```

**Specified by:**
- `readUnsignedShort` in interface `DataInput`

**Returns:**
- 읽은 두 unsigned short가 변환된 정수값.

**Throws:**
- `EOFException` - 2바이트를 읽을 수 없을 때 발생.

### readInt

```java
public final int readInt()
                  throws IOException
```

**Specified by:**
- `readInt` in interface `DataInput`

**Returns:**
- 읽은 정수형 정보.

**Throws:**
- `EOFException` - 4바이트를 읽을 수 없을 때 발생.

### readLong

```java
public final long readLong()
                    throws IOException
```

**Specified by:**
- `readLong` in interface `DataInput`

**Returns:**
- 읽은 Long형 정보.

**Throws:**
- `EOFException` - 8바이트를 읽을 수 없을 때 발생.

### readFloat

```java
public final float readFloat()
                      throws IOException
```

**Specified by:**
- `readFloat` in interface `DataInput`

### readDouble

```java
public final double readDouble()
                        throws IOException
```

**Specified by:**
- `readDouble` in interface `DataInput`

### readUTF

```java
public final String readUTF()
                     throws IOException
```

**Specified by:**
- `readUTF` in interface `DataInput`

**Returns:**
- 문자열.

**Throws:**
- `IOException` -

### readUTF

```java
public static final String readUTF(DataInput in)
                            throws IOException
```

**Parameters:**
- `in` - UTF형식 정보를 읽어들일 입력 스트림.

**Returns:**
- 문자열.

**Throws:**
- `IOException` -

### available

```java
public int available()
              throws IOException
```

**Overrides:**
- `taInput.html#readUTF()">readUTF` in interface `DataInput`

**Returns:**
- 臾몄
