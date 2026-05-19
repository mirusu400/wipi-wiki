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

자바에서 지원하는 타입 객체를 바이트 스트림으로 변환해 출력할 수 있도록
 만든 출력 스트림 클래스.

## 필드 요약

- `protected OutputStream out` — 실제 출력할 출력스트림.
- `protected  int written` — out로 출력한 바이트 갯수.

## 생성자 요약

- DataOutputStream ( OutputStream out) 새로운 객체를 만든다.

## 메서드 요약

- `void close ()` — 출력 스트림을 닫는다.
- `void flush ()` — 중간 버퍼에 남아있는 정보들을 실제 출력하도록 한다.
- `void write (byte[] buf, int offset, int len)` — 바이트 배열의 일부분을 출력한다.
- `void write (int b)` — 매개변수로 받은 변수 값 중 상위 24비트는 버리고 나머지 8비트만 출력한다.
- `void writeBoolean (boolean b)` — 매개변수 값이 true이면 1 false이면 0을 출력한다.
- `void writeByte (int b)` — 매개변수로 받은 변수 값 중 상위 24비트는 버리고 나머지 8비트만 출력한다.
- `void writeChar (int c)` — 매개변수로 받은 변수 값 중 상위 16비트는 버리고 8~15비트까지 출력하고 이어 하위 8비트를 출력한다.
- `void writeChars ( String s)` — 문자열을 구성하는 문자들을 인덱스 0 부터 차례대로 출력한다.
- `void writeDouble (double v)`
- `void writeFloat (float v)`
- `void writeInt (int i)` — 매개변수로 받은 변수 값 중 상위 8비트부터 차례대로 8비트 단위로 출력한다.
- `void writeLong (long l)` — 매개변수로 받은 변수 값 중 상위 8비트부터 차례대로 8비트 단위로 출력한다.
- `void writeShort (int s)` — 매개변수로 받은 변수 값 중 상위 16비트는 버리고 8~15비트까지 출력하고 이어 하위 8비트를 출력한다.
- `void writeUTF ( String s)` — 문자열을 UTF형식으로 바꿔 출력한다.

## 필드 상세

### written

```java
protected int written
```

- out로 출력한 바이트 갯수.

### out

```java
protected OutputStream out
```

- 실제 출력할 출력스트림.

### DataOutputStream

```java
public DataOutputStream(OutputStream out)
```

**Parameters:**
- `out` - 실제 바이트 정보가 출력될 출력 스트림.

### write

```java
public void write(int b)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 출력할 정보.

**Throws:**
- `IOException` -

### write

```java
public void write(byte[] buf,
                  int offset,
                  int len)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 출력할 갯수.

**Throws:**
- `IOException` -

### flush

```java
public void flush()
           throws IOException
```

**Overrides:**
- `flush` in class `OutputStream`
- Following copied from class: `java.io.OutputStream`

**Throws:**
- `IOException` -

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `OutputStream`

**Throws:**
- `IOException` -

### writeBoolean

```java
public final void writeBoolean(boolean b)
                        throws IOException
```

**Specified by:**
- `writeBoolean` in interface `DataOutput`

**Parameters:**
- `b` - 출력할 boolean변수.

**Throws:**
- `IOException` -

### writeByte

```java
public final void writeByte(int b)
                     throws IOException
```

**Specified by:**
- `writeByte` in interface `DataOutput`

**Parameters:**
- `b` - 출력할 정보.

**Throws:**
- `IOException` -

### writeShort

```java
public final void writeShort(int s)
                      throws IOException
```

**Specified by:**
- `writeShort` in interface `DataOutput`

**Parameters:**
- `s` - 출력할 정보.

**Throws:**
- `IOException` -

### writeChar

```java
public final void writeChar(int c)
                     throws IOException
```

**Specified by:**
- `writeChar` in interface `DataOutput`

**Parameters:**
- `c` - 출력할 정보.

**Throws:**
- `IOException` -

### writeInt

```java
public final void writeInt(int i)
                    throws IOException
```

**Specified by:**
- `writeInt` in interface `DataOutput`

**Parameters:**
- `i` - 출력할 정보.

**Throws:**
- `IOException` -

### writeLong

```java
public final void writeLong(long l)
                     throws IOException
```

**Specified by:**
- `writeLong` in interface `DataOutput`

**Parameters:**
- `l` - 출력할 정보.

**Throws:**
- `IOException` -

### writeFloat

```java
public final void writeFloat(float v)
                      throws IOException
```

**Specified by:**
- `writeFloat` in interface `DataOutput`

### writeDouble

```java
public final void writeDouble(double v)
                       throws IOException
```

**Specified by:**
- `writeDouble` in interface `DataOutput`

### writeChars

```java
public final void writeChars(String s)
                      throws IOException
```

**Specified by:**
- `writeChars` in interface `DataOutput`

**Parameters:**
- `s` - 출력할 문자열.

**Throws:**
- `IOException` -

### writeUTF

```java
public final void writeUTF(String s)
                    throws IOException
```

**Specified by:**
- `writeUTF` in interface `DataOutput`

**Parameters:**
- `str` - 출력할 문자열.

**Throws:**
- `IOException` -## 생성자 상세

### DataOutputStream

```java
public DataOutputStream(OutputStream out)
```

**Parameters:**
- `out` - 실제 바이트 정보가 출력될 출력 스트림.

### write

```java
public void write(int b)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 출력할 정보.

**Throws:**
- `IOException` -

### write

```java
public void write(byte[] buf,
                  int offset,
                  int len)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 출력할 갯수.

**Throws:**
- `IOException` -

### flush

```java
public void flush()
           throws IOException
```

**Overrides:**
- `flush` in class `OutputStream`
- Following copied from class: `java.io.OutputStream`

**Throws:**
- `IOException` -

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `OutputStream`

**Throws:**
- `IOException` -

### writeBoolean

```java
public final void writeBoolean(boolean b)
                        throws IOException
```

**Specified by:**
- `writeBoolean` in interface `DataOutput`

**Parameters:**
- `b` - 출력할 boolean변수.

**Throws:**
- `IOException` -

### writeByte

```java
public final void writeByte(int b)
                     throws IOException
```

**Specified by:**
- `writeByte` in interface `DataOutput`

**Parameters:**
- `b` - 출력할 정보.

**Throws:**
- `IOException` -

### writeShort

```java
public final void writeShort(int s)
                      throws IOException
```

**Specified by:**
- `writeShort` in interface `DataOutput`

**Parameters:**
- `s` - 출력할 정보.

**Throws:**
- `IOException` -

### writeChar

```java
public final void writeChar(int c)
                     throws IOException
```

**Specified by:**
- `writeChar` in interface `DataOutput`

**Parameters:**
- `c` - 출력할 정보.

**Throws:**
- `IOException` -

### writeInt

```java
public final void writeInt(int i)
                    throws IOException
```

**Specified by:**
- `writeInt` in interface `DataOutput`

**Parameters:**
- `i` - 출력할 정보.

**Throws:**
- `IOException` -

### writeLong

```java
public final void writeLong(long l)
                     throws IOException
```

**Specified by:**
- `writeLong` in interface `DataOutput`

**Parameters:**
- `l` - 출력할 정보.

**Throws:**
- `IOException` -

### writeFloat

```java
public final void writeFloat(float v)
                      throws IOException
```

**Specified by:**
- `writeFloat` in interface `DataOutput`

### writeDouble

```java
public final void writeDouble(double v)
                       throws IOException
```

**Specified by:**
- `writeDouble` in interface `DataOutput`

### writeChars

```java
public final void writeChars(String s)
                      throws IOException
```

**Specified by:**
- `writeChars` in interface `DataOutput`

**Parameters:**
- `s` - 출력할 문자열.

**Throws:**
- `IOException` -

### writeUTF

```java
public final void writeUTF(String s)
                    throws IOException
```

**Specified by:**
- `writeUTF` in interface `DataOutput`

**Parameters:**
- `str` - 출력할 문자열.

**Throws:**
- `IOException` -## 메서드 상세

### write

```java
public void write(int b)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 출력할 정보.

**Throws:**
- `IOException` -

### write

```java
public void write(byte[] buf,
                  int offset,
                  int len)
           throws IOException
```

**Specified by:**
- `write` in interface `DataOutput`

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 출력할 갯수.

**Throws:**
- `IOException` -

### flush

```java
public void flush()
           throws IOException
```

**Overrides:**
- `flush` in class `OutputStream`
- Following copied from class: `java.io.OutputStream`

**Throws:**
- `IOException` -

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `OutputStream`

**Throws:**
- `IOException` -

### writeBoolean

```java
public final void writeBoolean(boolean b)
                        throws IOException
```

**Specified by:**
- `writeBoolean` in interface `DataOutput`

**Parameters:**
- `b` - 출력할 boolean변수.

**Throws:**
- `IOException` -

### writeByte

```java
public final void writeByte(int b)
                     throws IOException
```

**Specified by:**
- `writeByte` in interface `DataOutput`

**Parameters:**
- `b` - 출력할 정보.

**Throws:**
- `IOException` -

### writeShort

```java
public final void writeShort(int s)
                      throws IOException
```

**Specified by:**
- `writeShort` in interface `DataOutput`

**Parameters:**
- `s` - 출력할 정보.

**Throws:**
- `IOException` -

### writeChar

```java
public final void writeChar(int c)
                     throws IOException
```

**Specified by:**
- `writeChar` in interface `DataOutput`

**Parameters:**
- `c` - 출력할 정보.

**Throws:**
- `IOException` -

### writeInt

```java
public final void writeInt(int i)
                    throws IOException
```

**Specified by:**
- `writeInt` in interface `DataOutput`

**Parameters:**
- `i` - 출력할 정보.

**Throws:**
- `IOException` -

### writeLong

```java
public final void writeLong(long l)
                     throws IOException
```

**Specified by:**
- `writeLong` in interface `DataOutput`

**Parameters:**
- `l` - 출력할 정보.

**Throws:**
- `IOException` -

### writeFloat

```java
public final void writeFloat(float v)
                      throws IOException
```

**Specified by:**
- `writeFloat` in interface `DataOutput`

### writeDouble

```java
public final void writeDouble(double v)
                       throws IOException
```

**Specified by:**
- `writeDouble` in interface `DataOutput`

### writeChars

```java
public final void writeChars(String s)
                      throws IOException
```

**Specified by:**
- `writeChars` in interface `DataOutput`

**Parameters:**
- `s` - 출력할 문자열.

**Throws:**
- `IOException` -

### writeUTF

```java
public final void writeUTF(String s)
                    throws IOException
```

**Specified by:**
- `writeUTF` in interface `DataOutput`

**Parameters:**
- `str` - 출력할 문자열.

**Throws:**
- `IOException` -

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
