---
title: "Interface DataOutput"
---

`package java.io`

```text
public void write(int b)
           throws IOException
```

## 설명

**Parameters:**
- `b` - 출력할 정보.

**Throws:**
- `IOException` -

### write

**Parameters:**
- `b` - 출력할 바이트 배열.

**Throws:**
- `IOException` -

### write

**Parameters:**
- `len` - 출력할 갯수.

**Throws:**
- `IOException` -

### writeBoolean

**Parameters:**
- `v` - 출력할 boolean변수.

**Throws:**
- `IOException` -

### writeByte

**Parameters:**
- `v` - 출력할 정보.

**Throws:**
- `IOException` -

### writeShort

**Parameters:**
- `v` - 출력할 정보.

**Throws:**
- `IOException` -

### writeChar

**Parameters:**
- `v` - 출력할 정보.

**Throws:**
- `IOException` -

### writeInt

**Parameters:**
- `v` - 출력할 정보.

**Throws:**
- `IOException` -

### writeLong

**Parameters:**
- `v` - 출력할 정보.

**Throws:**
- `IOException` -

### writeChars

**Parameters:**
- `s` - 출력할 문자열.

**Throws:**
- `IOException` -

### writeFloat

### writeDouble

### writeUTF

**Parameters:**
- `str` - 출력할 문자열.

**Throws:**
- `IOException` -## 메서드 요약

- `void write (byte[] b)` — 바이트 배열 전체를 출력한다.
- `void write (byte[] b, int off, int len)` — 바이트 배열의 일부분을 출력한다.
- `void write (int b)` — 매개변수로 받은 변수 값 중 상위 24비트는 버리고 나머지 8비트만 출력한다.
- `void writeBoolean (boolean v)` — 매개변수 값이 true이면 1 false이면 0을 출력한다.
- `void writeByte (int v)` — 매개변수로 받은 변수 값 중 상위 24비트는 버리고 나머지 8비트만 출력한다.
- `void writeChar (int v)` — 매개변수로 받은 변수 값 중 상위 16비트는 버리고 8~15비트까지 출력하고 이어 하위 8비트를 출력한다.
- `void writeChars ( String s)` — 문자열을 구성하는 문자들을 인덱스 0 부터 차례대로 출력한다.
- `void writeDouble (double v)`
- `void writeFloat (float v)`
- `void writeInt (int v)` — 매개변수로 받은 변수 값 중 상위 8비트부터 차례대로 8비트 단위로 출력한다.
- `void writeLong (long v)` — 매개변수로 받은 변수 값 중 상위 8비트부터 차례대로 8비트 단위로 출력한다.
- `void writeShort (int v)` — 매개변수로 받은 변수 값 중 상위 16비트는 버리고 8~15비트까지 출력하고 이어 하위 8비트를 출력한다.
- `void writeUTF ( String str)` — 문자열을 UTF형식으로 바꿔 출력한다.

## 메서드 상세

### write

```java
public void write(int b)
           throws IOException
```

**Parameters:**
- `b` - 출력할 정보.

**Throws:**
- `IOException` -

### write

```java
public void write(byte[] b)
           throws IOException
```

**Parameters:**
- `b` - 출력할 바이트 배열.

**Throws:**
- `IOException` -

### write

```java
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```

**Parameters:**
- `len` - 출력할 갯수.

**Throws:**
- `IOException` -

### writeBoolean

```java
public void writeBoolean(boolean v)
                  throws IOException
```

**Parameters:**
- `v` - 출력할 boolean변수.

**Throws:**
- `IOException` -

### writeByte

```java
public void writeByte(int v)
               throws IOException
```

**Parameters:**
- `v` - 출력할 정보.

**Throws:**
- `IOException` -

### writeShort

```java
public void writeShort(int v)
                throws IOException
```

**Parameters:**
- `v` - 출력할 정보.

**Throws:**
- `IOException` -

### writeChar

```java
public void writeChar(int v)
               throws IOException
```

**Parameters:**
- `v` - 출력할 정보.

**Throws:**
- `IOException` -

### writeInt

```java
public void writeInt(int v)
              throws IOException
```

**Parameters:**
- `v` - 출력할 정보.

**Throws:**
- `IOException` -

### writeLong

```java
public void writeLong(long v)
               throws IOException
```

**Parameters:**
- `v` - 출력할 정보.

**Throws:**
- `IOException` -

### writeChars

```java
public void writeChars(String s)
                throws IOException
```

**Parameters:**
- `s` - 출력할 문자열.

**Throws:**
- `IOException` -

### writeFloat

```java
public void writeFloat(float v)
                throws IOException
```

### writeDouble

```java
public void writeDouble(double v)
                 throws IOException
```

### writeUTF

```java
public void writeUTF(String str)
              throws IOException
```

**Parameters:**
- `str` - 출력할 문자열.

**Throws:**
- `IOException` -

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
