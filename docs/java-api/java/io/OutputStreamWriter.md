# Class OutputStreamWriter

`package java.io`

```text
java.lang.Object
  |
  +--java.io.Writer
        |
        +--java.io.OutputStreamWriter
```

## 설명

**extends Writer:**

Unicode로 된 내부 문자열을 KSC5601과 같은 형식의 문자열로
 변환하여 출력하는 출력 스트림이다.

Fields inherited from class java.io. Writer lock

Constructor Summary OutputStreamWriter ( OutputStream out) 새로운 출력스트림을 생성한다. OutputStreamWriter ( OutputStream out, String encoding_scheme) 새로운 출력스트림을 생성한다.

Method Summary void close () 출력스트림을 닫는다. void flush () 출력된 정보 중 중간 버퍼에 남아있는 내용을 모두 실제로 출력한다. void write (char c) 한 문자를 출력한다. void write (char[] buf,
 int offset,
 int len) 문자배열을 출력한다. void write (int c) 정수형 값을 출력한다. void write ( String str,
 int offset,
 int len) 문자열을 출력한다.

Methods inherited from class java.io. Writer write , write

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , toString , wait , wait , wait

Constructor Detail

### OutputStreamWriter

**Parameters:**
- `out` - 인코딩된 문자열이 실제 출력될 스트림.

### OutputStreamWriter

**Parameters:**
- `encoding_scheme` - 인코딩 방식

**Throws:**
- `UnsupportedEncodingException` - 지원하지 않는 인코딩 방식.

Method Detail

### close

**Overrides:**
- `close` in class `Writer`

**Throws:**
- `IOException` -

### flush

**Overrides:**
- `flush` in class `Writer`

**Throws:**
- `IOException` -

### write

**Parameters:**
- `c` - 출력할 문자열.

**Throws:**
- `IOException` -

### write

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `c` - 출력할 정수 값.

**Throws:**
- `IOException` -

### write

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -

### write

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -## 생성자 요약

- OutputStreamWriter ( OutputStream out) 새로운 출력스트림을 생성한다.
- OutputStreamWriter ( OutputStream out, String encoding_scheme) 새로운 출력스트림을 생성한다.

## 메서드 요약

- `void close ()` — 출력스트림을 닫는다.
- `void flush ()` — 출력된 정보 중 중간 버퍼에 남아있는 내용을 모두 실제로 출력한다.
- `void write (char c)` — 한 문자를 출력한다.
- `void write (char[] buf, int offset, int len)` — 문자배열을 출력한다.
- `void write (int c)` — 정수형 값을 출력한다.
- `void write ( String str, int offset, int len)` — 문자열을 출력한다.

## 생성자 상세

### OutputStreamWriter

```java
public OutputStreamWriter(OutputStream out)
```

**Parameters:**
- `out` - 인코딩된 문자열이 실제 출력될 스트림.

### OutputStreamWriter

```java
public OutputStreamWriter(OutputStream out,
                          String encoding_scheme)
                   throws UnsupportedEncodingException
```

**Parameters:**
- `encoding_scheme` - 인코딩 방식

**Throws:**
- `UnsupportedEncodingException` - 지원하지 않는 인코딩 방식.

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `Writer`

**Throws:**
- `IOException` -

### flush

```java
public void flush()
           throws IOException
```

**Overrides:**
- `flush` in class `Writer`

**Throws:**
- `IOException` -

### write

```java
public void write(char c)
           throws IOException
```

**Parameters:**
- `c` - 출력할 문자열.

**Throws:**
- `IOException` -

### write

```java
public void write(int c)
           throws IOException
```

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `c` - 출력할 정수 값.

**Throws:**
- `IOException` -

### write

```java
public void write(char[] buf,
                  int offset,
                  int len)
           throws IOException
```

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -

### write

```java
public void write(String str,
                  int offset,
                  int len)
           throws IOException
```

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -## 메서드 상세

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `Writer`

**Throws:**
- `IOException` -

### flush

```java
public void flush()
           throws IOException
```

**Overrides:**
- `flush` in class `Writer`

**Throws:**
- `IOException` -

### write

```java
public void write(char c)
           throws IOException
```

**Parameters:**
- `c` - 출력할 문자열.

**Throws:**
- `IOException` -

### write

```java
public void write(int c)
           throws IOException
```

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `c` - 출력할 정수 값.

**Throws:**
- `IOException` -

### write

```java
public void write(char[] buf,
                  int offset,
                  int len)
           throws IOException
```

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -

### write

```java
public void write(String str,
                  int offset,
                  int len)
           throws IOException
```

**Overrides:**
- `write` in class `Writer`

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
