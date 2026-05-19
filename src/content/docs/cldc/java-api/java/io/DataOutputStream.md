---
title: "Class DataOutputStream"
---

`package java.io`

```text
java.lang.Object
  |
  +--java.io.OutputStream
        |
        +--java.io.DataOutputStream
```

## 설명

**All Implemented Interfaces:**
- `DataOutput`

**implements DataOutput:**

데이터 출력 스트림은 응용 프로그램이 이식 가능한 방법으로 
 프리미티브 Java 데이터 유형을 출력 스트림에 쓸 수 있도록 합니다. 
 그런 다음 응용 프로그램은 데이터 입력 스트림을 사용하여 다시 데이터를 읽어올 수 있습니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``DataInputStream``

## 필드 요약

- `protected OutputStream out` — 출력 스트림

## 생성자 요약

- DataOutputStream ( OutputStream out) 새로운 데이터 출력 스트림을 만들어 지정된 
 기본 출력 스트림에 데이터를 씁니다.

## 메서드 요약

- `void close ()` — 이 출력 스트림을 닫고 스트림과 연결된 모든 시스템 자원을 해제합니다.
- `void flush ()` — 이 데이터 출력 스트림을 플러시합니다.
- `void write (byte[] b, int off, int len)` — off 오프셋에서 시작하여 지정된 바이트 배열의 len 바이트를 기본 출력 스트림에 씁니다.
- `void write (int b)` — 지정된 바이트(인자 b 의 하위 8비트)를 기본 출력 스트림에 씁니다.
- `void writeBoolean (boolean v)` — boolean 을 1바이트 값으로 기본 출력 스트림에 씁니다.
- `void writeByte (int v)` — byte 를 1바이트 값으로 기본 출력 스트림에 씁니다.
- `void writeChar (int v)` — char 를 2바이트 값으로 기본 출력 스트림에 상위 바이트부터 씁니다.
- `void writeChars ( String s)` — 문자열을 문자 시퀀스로 기본 출력 스트림에 씁니다.
- `void writeDouble (double v)` — Double 클래스의 doubleToLongBits 메소드를 사용하여 double 인자를 long 으로 변환한 다음, long 값을 8바이트로 기본 출력 스트림에 씁니다.
- `void writeFloat (float v)` — Float 클래스의 floatToIntBits 메소드를 사용하여 float 인자를 int 로 변환한 다음, int 값을 4바이트로 기본 출력 스트림에 씁니다.
- `void writeInt (int v)` — int 를 4바이트로 기본 출력 스트림에 상위 바이트부터 씁니다.
- `void writeLong (long v)` — long 을 8바이트로 기본 출력 스트림에 상위 바이트부터 씁니다.
- `void writeShort (int v)` — short 를 2바이트로 기본 출력 스트림에 상위 바이트부터 씁니다.
- `void writeUTF ( String str)` — 시스템 독립적인 방법으로 utf-8 인코딩을 사용하여 문자열을 기본 출력 스트림에 씁니다.

## 필드 상세

### out

```java
protected OutputStream out
```

- 출력 스트림

### DataOutputStream

```java
public DataOutputStream(OutputStream out)
```

- 새로운 데이터 출력 스트림을 만들어 지정된 
 기본 출력 스트림에 데이터를 씁니다.

**Parameters:**
- `out` - 기본 출력 스트림, 추후 사용을 위해 
 저장

### write

```java
public void write(int b)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Specified by:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 기록되는 `byte`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 기록할 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### flush

```java
public void flush()
           throws IOException
```

**Overrides:**
- `flush` in class `OutputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `OutputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeBoolean

```java
public final void writeBoolean(boolean v)
                        throws IOException
```

**Specified by:**
- `writeBoolean` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `boolean` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeByte

```java
public final void writeByte(int v)
                     throws IOException
```

**Specified by:**
- `writeByte` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `byte` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeShort

```java
public final void writeShort(int v)
                      throws IOException
```

**Specified by:**
- `writeShort` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `short`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeChar

```java
public final void writeChar(int v)
                     throws IOException
```

**Specified by:**
- `writeChar` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `char` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeInt

```java
public final void writeInt(int v)
                    throws IOException
```

**Specified by:**
- `writeInt` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `int`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeLong

```java
public final void writeLong(long v)
                     throws IOException
```

**Specified by:**
- `writeLong` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `long`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeFloat

```java
public final void writeFloat(float v)
                      throws IOException
```

**Specified by:**
- `writeFloat` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `float` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``Float.floatToIntBits(float)``

### writeDouble

```java
public final void writeDouble(double v)
                       throws IOException
```

**Specified by:**
- `writeDouble` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `double` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``Double.doubleToLongBits(double)``

### writeChars

```java
public final void writeChars(String s)
                      throws IOException
```

**Specified by:**
- `writeChars` in interface `DataOutput`

**Parameters:**
- `s` - 기록되는 `String` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``writeChar(int)``

### writeUTF

```java
public final void writeUTF(String str)
                    throws IOException
```

**Specified by:**
- `writeUTF` in interface `DataOutput`

**Parameters:**
- `str` - 기록되는 문자열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 생성자 상세

### DataOutputStream

```java
public DataOutputStream(OutputStream out)
```

- 새로운 데이터 출력 스트림을 만들어 지정된 
 기본 출력 스트림에 데이터를 씁니다.

**Parameters:**
- `out` - 기본 출력 스트림, 추후 사용을 위해 
 저장

### write

```java
public void write(int b)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Specified by:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 기록되는 `byte`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 기록할 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### flush

```java
public void flush()
           throws IOException
```

**Overrides:**
- `flush` in class `OutputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `OutputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeBoolean

```java
public final void writeBoolean(boolean v)
                        throws IOException
```

**Specified by:**
- `writeBoolean` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `boolean` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeByte

```java
public final void writeByte(int v)
                     throws IOException
```

**Specified by:**
- `writeByte` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `byte` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeShort

```java
public final void writeShort(int v)
                      throws IOException
```

**Specified by:**
- `writeShort` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `short`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeChar

```java
public final void writeChar(int v)
                     throws IOException
```

**Specified by:**
- `writeChar` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `char` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeInt

```java
public final void writeInt(int v)
                    throws IOException
```

**Specified by:**
- `writeInt` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `int`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeLong

```java
public final void writeLong(long v)
                     throws IOException
```

**Specified by:**
- `writeLong` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `long`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeFloat

```java
public final void writeFloat(float v)
                      throws IOException
```

**Specified by:**
- `writeFloat` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `float` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``Float.floatToIntBits(float)``

### writeDouble

```java
public final void writeDouble(double v)
                       throws IOException
```

**Specified by:**
- `writeDouble` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `double` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``Double.doubleToLongBits(double)``

### writeChars

```java
public final void writeChars(String s)
                      throws IOException
```

**Specified by:**
- `writeChars` in interface `DataOutput`

**Parameters:**
- `s` - 기록되는 `String` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``writeChar(int)``

### writeUTF

```java
public final void writeUTF(String str)
                    throws IOException
```

**Specified by:**
- `writeUTF` in interface `DataOutput`

**Parameters:**
- `str` - 기록되는 문자열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 메서드 상세

### write

```java
public void write(int b)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Specified by:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 기록되는 `byte`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 기록할 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### flush

```java
public void flush()
           throws IOException
```

**Overrides:**
- `flush` in class `OutputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `OutputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeBoolean

```java
public final void writeBoolean(boolean v)
                        throws IOException
```

**Specified by:**
- `writeBoolean` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `boolean` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeByte

```java
public final void writeByte(int v)
                     throws IOException
```

**Specified by:**
- `writeByte` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `byte` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeShort

```java
public final void writeShort(int v)
                      throws IOException
```

**Specified by:**
- `writeShort` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `short`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeChar

```java
public final void writeChar(int v)
                     throws IOException
```

**Specified by:**
- `writeChar` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `char` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeInt

```java
public final void writeInt(int v)
                    throws IOException
```

**Specified by:**
- `writeInt` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `int`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeLong

```java
public final void writeLong(long v)
                     throws IOException
```

**Specified by:**
- `writeLong` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `long`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeFloat

```java
public final void writeFloat(float v)
                      throws IOException
```

**Specified by:**
- `writeFloat` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `float` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``Float.floatToIntBits(float)``

### writeDouble

```java
public final void writeDouble(double v)
                       throws IOException
```

**Specified by:**
- `writeDouble` in interface `DataOutput`

**Parameters:**
- `v` - 기록되는 `double` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``Double.doubleToLongBits(double)``

### writeChars

```java
public final void writeChars(String s)
                      throws IOException
```

**Specified by:**
- `writeChars` in interface `DataOutput`

**Parameters:**
- `s` - 기록되는 `String` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``writeChar(int)``

### writeUTF

```java
public final void writeUTF(String str)
                    throws IOException
```

**Specified by:**
- `writeUTF` in interface `DataOutput`

**Parameters:**
- `str` - 기록되는 문자열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우
