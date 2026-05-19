---
title: "Class PrintStream"
---

`package java.io`

```text
java.lang.Object
  |
  +--java.io.OutputStream
        |
        +--java.io.PrintStream
```

## 설명

**extends OutputStream:**

다른 출력스트림에 새로운 라인 값을 덧붙여 출력하기 등 값 출력에 대한 여러 
 부가적인 기능을 덧붙이는 출력스트림이다.

## 생성자 요약

- PrintStream ( OutputStream out) 새로운 출력스트림을 생성함니다.

## 메서드 요약

- `boolean checkError ()` — 출력 스트림이 오류상태 인지 여부를 구한다.
- `void close ()` — 출력스트림을 닫는다.
- `void flush ()` — 출력된 정보 중 중간 버퍼에 남아있는 내용을 모두 실제로 출력한다.
- `void print (boolean b)` — boolean형 값을 출력한다.
- `void print (char c)` — 한 문자를 출력한다.
- `void print (char[] s)` — 문자배열을 출력한다.
- `void print (int i)` — 정수값을 출력한다.
- `void print (long l)` — long값을 출력한다.
- `void print ( Object obj)` — 특정 객체에 대한 정보를 출력한다.
- `void print ( String s)` — 문자열을 출력한다.
- `void println ()` — 새로운 라인 문자를 출력한다.
- `void println (boolean x)` — boolean형 값을 출력한다.이어서 새로운 라인 문자를 출력한다.
- `void println (char x)` — 한 문자를 출력한다.이어서 새로운 라인 문자를 출력한다.
- `void println (char[] x)` — 문자배열을 출력한다.이어서 새로운 라인 문자를 출력한다.
- `void println (int x)` — 정수값을 출력한다.이어서 새로운 라인 문자를 출력한다.
- `void println (long x)` — long값을 출력한다.이어서 새로운 라인 문자를 출력한다.
- `void println ( Object x)` — 특정 객체에 대한 정보를 출력한다.이어서 새로운 라인 문자를 출력한다.
- `void println ( String x)` — 문자열을 출력한다.이어서 새로운 라인 문자를 출력한다.
- `protected  void setError ()` — 출력스트림이 오류상태임을 설정한다.
- `void write (byte[] buf, int off, int len)` — 바이트배열을 출력한다.
- `void write (int b)` — 특정 바이트를 출력한다.

## 생성자 상세

### PrintStream

```java
public PrintStream(OutputStream out)
```

**Parameters:**
- `out` - 실제 출력할 출력스트림.

### flush

```java
public void flush()
```

**Overrides:**
- `flush` in class `OutputStream`
- Following copied from class: `java.io.OutputStream`

**Throws:**
- `IOException` -

### close

```java
public void close()
```

**Overrides:**
- `close` in class `OutputStream`
- Following copied from class: `java.io.OutputStream`

**Throws:**
- `IOException` -

### checkError

```java
public boolean checkError()
```

**Returns:**
- 오류상태이면 true 아니면 false

### setError

```java
protected void setError()
```

- 출력스트림이 오류상태임을 설정한다.

### write

```java
public void write(int b)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 출력할 정수값.

### write

```java
public void write(byte[] buf,
                  int off,
                  int len)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 출력할 바이트 갯수.

### print

```java
public void print(boolean b)
```

**Parameters:**
- `b` - 출력할 boolean형 변수.

### print

```java
public void print(char c)
```

**Parameters:**
- `c` - 출력할 문자.

### print

```java
public void print(int i)
```

**Parameters:**
- `i` - 출력할 정수값.

### print

```java
public void print(long l)
```

**Parameters:**
- `l` - 출력할 long값.

### print

```java
public void print(char[] s)
```

**Parameters:**
- `s` - 출력할 문자배열.

### print

```java
public void print(String s)
```

**Parameters:**
- `s` - 출력할 문자열.

### print

```java
public void print(Object obj)
```

**Parameters:**
- `obj` - 출력할 객체.

### println

```java
public void println()
```

- 새로운 라인 문자를 출력한다.

### println

```java
public void println(boolean x)
```

**Parameters:**
- `x` - 출력할 boolean형 변수.

### println

```java
public void println(char x)
```

**Parameters:**
- `x` - 출력할 문자.

### println

```java
public void println(int x)
```

**Parameters:**
- `x` - 출력할 정수값.

### println

```java
public void println(long x)
```

**Parameters:**
- `x` - 출력할 long값.

### println

```java
public void println(char[] x)
```

**Parameters:**
- `x` - 출력할 문자배열.

### println

```java
public void println(String x)
```

**Parameters:**
- `x` - 출력할 문자열.

### println

```java
public void println(Object x)
```

**Parameters:**
- `x` - 출력할 객체.## 메서드 상세

### flush

```java
public void flush()
```

**Overrides:**
- `flush` in class `OutputStream`
- Following copied from class: `java.io.OutputStream`

**Throws:**
- `IOException` -

### close

```java
public void close()
```

**Overrides:**
- `close` in class `OutputStream`
- Following copied from class: `java.io.OutputStream`

**Throws:**
- `IOException` -

### checkError

```java
public boolean checkError()
```

**Returns:**
- 오류상태이면 true 아니면 false

### setError

```java
protected void setError()
```

- 출력스트림이 오류상태임을 설정한다.

### write

```java
public void write(int b)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 출력할 정수값.

### write

```java
public void write(byte[] buf,
                  int off,
                  int len)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 출력할 바이트 갯수.

### print

```java
public void print(boolean b)
```

**Parameters:**
- `b` - 출력할 boolean형 변수.

### print

```java
public void print(char c)
```

**Parameters:**
- `c` - 출력할 문자.

### print

```java
public void print(int i)
```

**Parameters:**
- `i` - 출력할 정수값.

### print

```java
public void print(long l)
```

**Parameters:**
- `l` - 출력할 long값.

### print

```java
public void print(char[] s)
```

**Parameters:**
- `s` - 출력할 문자배열.

### print

```java
public void print(String s)
```

**Parameters:**
- `s` - 출력할 문자열.

### print

```java
public void print(Object obj)
```

**Parameters:**
- `obj` - 출력할 객체.

### println

```java
public void println()
```

- 새로운 라인 문자를 출력한다.

### println

```java
public void println(boolean x)
```

**Parameters:**
- `x` - 출력할 boolean형 변수.

### println

```java
public void println(char x)
```

**Parameters:**
- `x` - 출력할 문자.

### println

```java
public void println(int x)
```

**Parameters:**
- `x` - 출력할 정수값.

### println

```java
public void println(long x)
```

**Parameters:**
- `x` - 출력할 long값.

### println

```java
public void println(char[] x)
```

**Parameters:**
- `x` - 출력할 문자배열.

### println

```java
public void println(String x)
```

**Parameters:**
- `x` - 출력할 문자열.

### println

```java
public void println(Object x)
```

**Parameters:**
- `x` - 출력할 객체.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
