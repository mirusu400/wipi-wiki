# Class OutputStreamWriter

`package java.io`

```
java.lang.Object
  |
  +--java.io.Writer
        |
        +--java.io.OutputStreamWriter
```

## 설명

**extends Writer:**

OutputStreamWriter가 문자 스트림에서 바이트 스트림으로의 
브릿지 역할을 하는 경우 기록된 문자를 바이트로 변환합니다. 
사용할 인코딩을 이름으로 지정하거나 
플랫폼의 기본 인코딩을 사용할 수 있습니다.

write() 메소드를 호출할 때마다 지정된 문자에 대해 
인코딩 변환기가 호출됩니다. 
결과로 나온 바이트는 버퍼에 축적된 후 기본 출력 스트림에 기록됩니다. 
이 버퍼의 크기를 지정할 수도 있지만 기본적으로 버퍼는 대부분의 용도로 
사용할 수 있을 만큼 크게 할당되어 있습니다. 
write() 메소드로 전달된 문자는 버퍼되지 않습니다.

**Since:**
- CLDC 1.0

**See Also:**
- ``Writer``, 
``UnsupportedEncodingException``

## 필드 요약

## 생성자 요약

- OutputStreamWriter ( OutputStream os) 기본 문자 인코딩을 사용하는 OutputStreamWriter를 만듭니다.
- OutputStreamWriter ( OutputStream os, String enc) 명명된 문자 인코딩을 사용하는 OutputStreamWriter를 만듭니다.

## 메서드 요약

- `void close ()` — 스트림을 닫습니다.
- `void flush ()` — 스트림을 플러시합니다.
- `void write (char[] cbuf, int off, int len)` — 문자 배열의 일부를 씁니다.
- `void write (int c)` — 단일 문자를 씁니다.
- `void write ( String str, int off, int len)` — 문자열의 일부를 씁니다.

## 생성자 상세

### OutputStreamWriter

```java
public OutputStreamWriter(OutputStream os)
```

- 기본 문자 인코딩을 사용하는 OutputStreamWriter를 만듭니다.

**Parameters:**
- `os` - OutputStream

### OutputStreamWriter

```java
public OutputStreamWriter(OutputStream os,
                          String enc)
                   throws UnsupportedEncodingException
```

- 명명된 문자 인코딩을 사용하는 OutputStreamWriter를 만듭니다.

**Parameters:**
- `enc` - 지원되는 문자 인코딩 이름

**Throws:**
- `UnsupportedEncodingException` - 명명된 인코딩이 지원되지 않는 경우

### write

```java
public void write(int c)
           throws IOException
```

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `c` - 기록되는 문자를 지정하는 int

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(char[] cbuf,
                  int off,
                  int len)
           throws IOException
```

**Specified by:**
- `write` in class `Writer`

**Parameters:**
- `len` - 기록되는 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(String str,
                  int off,
                  int len)
           throws IOException
```

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `len` - 기록되는 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### flush

```java
public void flush()
           throws IOException
```

**Specified by:**
- `flush` in class `Writer`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Specified by:**
- `close` in class `Writer`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 메서드 상세

### write

```java
public void write(int c)
           throws IOException
```

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `c` - 기록되는 문자를 지정하는 int

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(char[] cbuf,
                  int off,
                  int len)
           throws IOException
```

**Specified by:**
- `write` in class `Writer`

**Parameters:**
- `len` - 기록되는 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(String str,
                  int off,
                  int len)
           throws IOException
```

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `len` - 기록되는 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### flush

```java
public void flush()
           throws IOException
```

**Specified by:**
- `flush` in class `Writer`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Specified by:**
- `close` in class `Writer`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우
