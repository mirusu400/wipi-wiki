# Interface DataOutput

`package java.io`

```
public void write(int b)
           throws IOException
```

## 설명

**Parameters:**
- `b` - 기록되는 바이트

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

**Parameters:**
- `b` - 데이터

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

**Parameters:**
- `len` - 기록할 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeBoolean

**Parameters:**
- `v` - 기록되는 부울

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeByte

**Parameters:**
- `v` - 기록되는 바이트 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeShort

**Parameters:**
- `v` - 기록되는 `short` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeChar

**Parameters:**
- `v` - 기록되는 `char` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeInt

**Parameters:**
- `v` - 기록되는 `int` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeLong

**Parameters:**
- `v` - 기록되는 `long` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeFloat

**Parameters:**
- `v` - 기록되는 `float` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

### writeDouble

**Parameters:**
- `v` - 기록되는 `double` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

### writeChars

**Parameters:**
- `s` - 기록되는 문자열 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeUTF

**Parameters:**
- `s` - 기록되는 문자열 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 메서드 요약

- `void write (byte[] b)` — 배열 b 의 모든 바이트를 출력 스트림에 씁니다.
- `void write (byte[] b, int off, int len)` — 배열 b 의 len 바이트를 출력 스트림에 씁니다.
- `void write (int b)` — 인자 b 의 하위 8비트를 출력 스트림에 씁니다.
- `void writeBoolean (boolean v)` — boolean 값을 이 출력 스트림에 씁니다.
- `void writeByte (int v)` — 인자 v 의 하위 8비트를 출력 스트림에 씁니다.
- `void writeChar (int v)` — 2바이트로 이루어진 char 값을 출력 스트림에 씁니다.
- `void writeChars ( String s)` — s 문자열의 모든 문자를 순서대로 문자당 2바이트씩 출력 스트림에 씁니다.
- `void writeDouble (double v)` — 8바이트로 이루어진 double 값을 출력 스트림에 씁니다.
- `void writeFloat (float v)` — 4바이트로 이루어진 float 값을 출력 스트림에 씁니다.
- `void writeInt (int v)` — 4바이트로 이루어진 int 값을 출력 스트림에 씁니다.
- `void writeLong (long v)` — 4바이트로 이루어진 long 값을 출력 스트림에 씁니다.
- `void writeShort (int v)` — 인자 값을 나타내기 위해 2바이트를 출력 스트림에 씁니다.
- `void writeUTF ( String s)` — 2바이트의 길이 정보를 출력 스트림에 쓰고 그 다음에 s 문자열에 있는 모든 문자의 Java로 수정된 UTF 표현이 나옵니다.

## 메서드 상세

### write

```java
public void write(int b)
           throws IOException
```

**Parameters:**
- `b` - 기록되는 바이트

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(byte[] b)
           throws IOException
```

**Parameters:**
- `b` - 데이터

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(byte[] b,
                  int off,
                  int len)
           throws IOException
```

**Parameters:**
- `len` - 기록할 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeBoolean

```java
public void writeBoolean(boolean v)
                  throws IOException
```

**Parameters:**
- `v` - 기록되는 부울

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeByte

```java
public void writeByte(int v)
               throws IOException
```

**Parameters:**
- `v` - 기록되는 바이트 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeShort

```java
public void writeShort(int v)
                throws IOException
```

**Parameters:**
- `v` - 기록되는 `short` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeChar

```java
public void writeChar(int v)
               throws IOException
```

**Parameters:**
- `v` - 기록되는 `char` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeInt

```java
public void writeInt(int v)
              throws IOException
```

**Parameters:**
- `v` - 기록되는 `int` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeLong

```java
public void writeLong(long v)
               throws IOException
```

**Parameters:**
- `v` - 기록되는 `long` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeFloat

```java
public void writeFloat(float v)
                throws IOException
```

**Parameters:**
- `v` - 기록되는 `float` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

### writeDouble

```java
public void writeDouble(double v)
                 throws IOException
```

**Parameters:**
- `v` - 기록되는 `double` 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**Since:**
- CLDC 1.1

### writeChars

```java
public void writeChars(String s)
                throws IOException
```

**Parameters:**
- `s` - 기록되는 문자열 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### writeUTF

```java
public void writeUTF(String s)
              throws IOException
```

**Parameters:**
- `s` - 기록되는 문자열 값

**Throws:**
- `IOException` - I/O 오류가 발생한 경우
