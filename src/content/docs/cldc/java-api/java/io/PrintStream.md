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

`PrintStream`은 다양한 데이터 값 표현의 
편리한 인쇄 기능 등을 다른 출력 스트림에 추가합니다. 
다른 두 가지 기능도 제공합니다. 
다른 출력 스트림과 달리 `PrintStream`은 
`IOException`을 발생시키지 않습니다. 
예외적인 상황이 발생하면 `checkError` 메소드를 통해 테스트할 수 있는 내부 플래그만 설정됩니다.

`PrintStream`에서 인쇄하는 모든 문자는 
플랫폼의 기본 문자 인코딩을 사용하여 바이트로 변환됩니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- PrintStream ( OutputStream out) 새로운 인쇄 스트림을 만듭니다.

## 메서드 요약

- `boolean checkError ()` — 스트림을 플러시하고 오류 상태를 확인합니다.
- `void close ()` — 스트림을 닫습니다.
- `void flush ()` — 스트림을 플러시합니다.
- `void print (boolean b)` — 부울 값을 인쇄합니다.
- `void print (char c)` — 문자를 인쇄합니다.
- `void print (char[] s)` — 문자 배열을 인쇄합니다.
- `void print (double d)` — 배정도 부동 소수점 숫자를 인쇄합니다.
- `void print (float f)` — 부동 소수점 숫자를 인쇄합니다.
- `void print (int i)` — 정수를 인쇄합니다.
- `void print (long l)` — long 정수를 인쇄합니다.
- `void print ( Object obj)` — 객체를 인쇄합니다.
- `void print ( String s)` — 문자열을 인쇄합니다.
- `void println ()` — 행 구분자 문자열을 기록하여 현재 행을 종료합니다.
- `void println (boolean x)` — 부울을 인쇄하고 행을 종료합니다.
- `void println (char x)` — 문자를 인쇄하고 행을 종료합니다.
- `void println (char[] x)` — 문자 배열을 인쇄하고 행을 종료합니다.
- `void println (double x)` — double을 인쇄하고 행을 종료합니다.
- `void println (float x)` — float를 인쇄하고 행을 종료합니다.
- `void println (int x)` — 정수를 인쇄하고 행을 종료합니다.
- `void println (long x)` — long을 인쇄하고 행을 종료합니다.
- `void println ( Object x)` — 객체를 인쇄하고 행을 종료합니다.
- `void println ( String x)` — 문자열을 인쇄하고 행을 종료합니다.
- `protected  void setError ()` — 스트림의 오류 상태를 true 로 설정합니다.
- `void write (byte[] buf, int off, int len)` — off 오프셋에서 시작하여 지정된 바이트 배열의 len 바이트를 이 스트림에 씁니다.
- `void write (int b)` — 지정된 바이트를 이 스트림에 씁니다.

## 생성자 상세

### PrintStream

```java
public PrintStream(OutputStream out)
```

- 새로운 인쇄 스트림을 만듭니다. 이 스트림은 자동으로 플러시되지 않습니다.

**Parameters:**
- `out` - 값과 객체가 인쇄되는 
 출력 스트림

### flush

```java
public void flush()
```

**Overrides:**
- `flush` in class `OutputStream`

**See Also:**
- ``OutputStream.flush()``

### close

```java
public void close()
```

**Overrides:**
- `close` in class `OutputStream`

**See Also:**
- ``OutputStream.close()``

### checkError

```java
public boolean checkError()
```

**Returns:**
- 이 스트림에서 
 `IOException`이 발생하거나 
 `setError` 메소드가 호출된 경우에만 true

### setError

```java
protected void setError()
```

**Since:**
- JDK1.1

### write

```java
public void write(int b)
```

**Specified by:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 기록되는 바이트

**See Also:**
- ``print(char)``, 
``println(char)``

### write

```java
public void write(byte[] buf,
                  int off,
                  int len)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 기록할 바이트 수

### print

```java
public void print(boolean b)
```

**Parameters:**
- `b` - 인쇄되는 `boolean`

### print

```java
public void print(char c)
```

**Parameters:**
- `c` - 인쇄되는 `char`

### print

```java
public void print(int i)
```

**Parameters:**
- `i` - 인쇄되는 `int`

**See Also:**
- ``Integer.toString(int)``

### print

```java
public void print(long l)
```

**Parameters:**
- `l` - 인쇄되는 `long`

**See Also:**
- ``Long.toString(long)``

### print

```java
public void print(float f)
```

**Parameters:**
- `f` - 인쇄되는 `float`

**Since:**
- CLDC 1.1

**See Also:**
- ``Float.toString(float)``

### print

```java
public void print(double d)
```

**Parameters:**
- `d` - 인쇄되는 `double`

**Since:**
- CLDC 1.1

**See Also:**
- ``Double.toString(double)``

### print

```java
public void print(char[] s)
```

**Parameters:**
- `s` - 인쇄되는 문자 배열

**Throws:**
- `NullPointerException` - `s`가 `null`인 경우

### print

```java
public void print(String s)
```

**Parameters:**
- `s` - 인쇄되는 `String`

### print

```java
public void print(Object obj)
```

**Parameters:**
- `obj` - 인쇄되는 `Object`

**See Also:**
- ``Object.toString()``

### println

```java
public void println()
```

행 구분자 문자열을 기록하여 현재 행을 종료합니다. 
행 구분자 문자열은 시스템 등록 정보 line.separator 로 
정의되며 반드시 단일 개행 문자( '\n' )를 
사용할 필요는 없습니다.

### println

```java
public void println(boolean x)
```

**Parameters:**
- `x` - 인쇄되는 `boolean`

### println

```java
public void println(char x)
```

**Parameters:**
- `x` - 인쇄되는 `char`

### println

```java
public void println(int x)
```

**Parameters:**
- `x` - 인쇄되는 `int`

### println

```java
public void println(long x)
```

**Parameters:**
- `x` - 인쇄되는 `long`

### println

```java
public void println(float x)
```

**Parameters:**
- `x` - 인쇄되는 `float`

**Since:**
- CLDC 1.1

### println

```java
public void println(double x)
```

**Parameters:**
- `x` - 인쇄되는 `double`

**Since:**
- CLDC 1.1

### println

```java
public void println(char[] x)
```

**Parameters:**
- `x` - 인쇄할 문자 배열

### println

```java
public void println(String x)
```

**Parameters:**
- `x` - 인쇄되는 `String`

### println

```java
public void println(Object x)
```

**Parameters:**
- `x` - 인쇄되는 `Object`

## 메서드 상세

### flush

```java
public void flush()
```

**Overrides:**
- `flush` in class `OutputStream`

**See Also:**
- ``OutputStream.flush()``

### close

```java
public void close()
```

**Overrides:**
- `close` in class `OutputStream`

**See Also:**
- ``OutputStream.close()``

### checkError

```java
public boolean checkError()
```

**Returns:**
- 이 스트림에서 
 `IOException`이 발생하거나 
 `setError` 메소드가 호출된 경우에만 true

### setError

```java
protected void setError()
```

**Since:**
- JDK1.1

### write

```java
public void write(int b)
```

**Specified by:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 기록되는 바이트

**See Also:**
- ``print(char)``, 
``println(char)``

### write

```java
public void write(byte[] buf,
                  int off,
                  int len)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 기록할 바이트 수

### print

```java
public void print(boolean b)
```

**Parameters:**
- `b` - 인쇄되는 `boolean`

### print

```java
public void print(char c)
```

**Parameters:**
- `c` - 인쇄되는 `char`

### print

```java
public void print(int i)
```

**Parameters:**
- `i` - 인쇄되는 `int`

**See Also:**
- ``Integer.toString(int)``

### print

```java
public void print(long l)
```

**Parameters:**
- `l` - 인쇄되는 `long`

**See Also:**
- ``Long.toString(long)``

### print

```java
public void print(float f)
```

**Parameters:**
- `f` - 인쇄되는 `float`

**Since:**
- CLDC 1.1

**See Also:**
- ``Float.toString(float)``

### print

```java
public void print(double d)
```

**Parameters:**
- `d` - 인쇄되는 `double`

**Since:**
- CLDC 1.1

**See Also:**
- ``Double.toString(double)``

### print

```java
public void print(char[] s)
```

**Parameters:**
- `s` - 인쇄되는 문자 배열

**Throws:**
- `NullPointerException` - `s`가 `null`인 경우

### print

```java
public void print(String s)
```

**Parameters:**
- `s` - 인쇄되는 `String`

### print

```java
public void print(Object obj)
```

**Parameters:**
- `obj` - 인쇄되는 `Object`

**See Also:**
- ``Object.toString()``

### println

```java
public void println()
```

행 구분자 문자열을 기록하여 현재 행을 종료합니다. 
행 구분자 문자열은 시스템 등록 정보 line.separator 로 
정의되며 반드시 단일 개행 문자( '\n' )를 
사용할 필요는 없습니다.

### println

```java
public void println(boolean x)
```

**Parameters:**
- `x` - 인쇄되는 `boolean`

### println

```java
public void println(char x)
```

**Parameters:**
- `x` - 인쇄되는 `char`

### println

```java
public void println(int x)
```

**Parameters:**
- `x` - 인쇄되는 `int`

### println

```java
public void println(long x)
```

**Parameters:**
- `x` - 인쇄되는 `long`

### println

```java
public void println(float x)
```

**Parameters:**
- `x` - 인쇄되는 `float`

**Since:**
- CLDC 1.1

### println

```java
public void println(double x)
```

**Parameters:**
- `x` - 인쇄되는 `double`

**Since:**
- CLDC 1.1

### println

```java
public void println(char[] x)
```

**Parameters:**
- `x` - 인쇄할 문자 배열

### println

```java
public void println(String x)
```

**Parameters:**
- `x` - 인쇄되는 `String`

### println

```java
public void println(Object x)
```

**Parameters:**
- `x` - 인쇄되는 `Object`
