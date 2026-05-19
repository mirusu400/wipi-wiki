---
title: "Class OutputStream"
---

`package java.io`

```text
java.lang.Object
  |
  +--java.io.OutputStream
```

## 설명

**Direct Known Subclasses:**
- `ByteArrayOutputStream`, `DataOutputStream`, `PrintStream`

**extends Object:**

이 추상 클래스는 바이트 출력 스트림을 나타내는 
모든 클래스의 수퍼 클래스입니다. 
출력 스트림은 출력 바이트를 받아서 싱크로 보냅니다.

`OutputStream`의 서브 클래스를 정의할 필요가 있는 
응용 프로그램은 항상 최소 1바이트 이상의 출력을 쓰는 
메소드를 제공해야 합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``ByteArrayOutputStream``, 
``DataOutputStream``, 
``InputStream``, 
``write(int)``

## 생성자 요약

- OutputStream ()

## 메서드 요약

- `void close ()` — 이 출력 스트림을 닫고 스트림과 연결된 시스템 자원을 해제합니다.
- `void flush ()` — 이 출력 스트림을 플러시하고 버퍼된 출력 바이트를 모두 씁니다.
- `void write (byte[] b)` — 지정된 바이트 배열의 b.length 바이트를 이 출력 스트림에 씁니다.
- `void write (byte[] b, int off, int len)` — off 오프셋에서 시작하여 지정된 바이트 배열의 len 바이트를 이 출력 스트림에 씁니다.
- `abstract  void write (int b)` — 지정된 바이트를 이 출력 스트림에 씁니다.

## 생성자 상세

### OutputStream

```java
public OutputStream()
```

### write

```java
public abstract void write(int b)
                    throws IOException
```

**Parameters:**
- `b` - `byte`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우 
 특히 출력 스트림이 닫힌 경우 `IOException`이 
 발생합니다.

### write

```java
public void write(byte[] b)
           throws IOException
```

**Parameters:**
- `b` - 데이터

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``write(byte[], int, int)``

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
 특히 출력 스트림이 닫힌 경우 
 `IOException`이 발생합니다.

### flush

```java
public void flush()
           throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 메서드 상세

### write

```java
public abstract void write(int b)
                    throws IOException
```

**Parameters:**
- `b` - `byte`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우 
 특히 출력 스트림이 닫힌 경우 `IOException`이 
 발생합니다.

### write

```java
public void write(byte[] b)
           throws IOException
```

**Parameters:**
- `b` - 데이터

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``write(byte[], int, int)``

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
 특히 출력 스트림이 닫힌 경우 
 `IOException`이 발생합니다.

### flush

```java
public void flush()
           throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우
