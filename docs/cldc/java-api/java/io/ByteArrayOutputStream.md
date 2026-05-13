# Class ByteArrayOutputStream

`package java.io`

```
java.lang.Object
  |
  +--java.io.OutputStream
        |
        +--java.io.ByteArrayOutputStream
```

## 설명

**extends OutputStream:**

이 클래스는 데이터를 바이트 배열에 쓰는 
 출력 스트림을 구현합니다. 
 데이터를 버퍼에 쓰면 버퍼가 자동으로 커집니다. 
 데이터는 `toByteArray()`와 
 `toString()`을 사용하여 검색할 수 있습니다.

**Since:**
- JDK1.0, CLDC 1.0

## 필드 요약

- `protected  byte[] buf` — 데이터가 저장되는 버퍼
- `protected  int count` — 버퍼에 있는 유효 바이트 수

## 생성자 요약

- ByteArrayOutputStream () 새로운 바이트 배열 출력 스트림을 만듭니다.
- ByteArrayOutputStream (int size) 지정된 크기(바이트)의 버퍼 용량을 가진 
 새로운 바이트 배열 출력 스트림을 만듭니다.

## 메서드 요약

- `void close ()` — 이 출력 스트림을 닫고 스트림과 연결된 시스템 자원을 해제합니다.
- `void reset ()` — 출력 스트림에 현재 축적된 모든 출력이 삭제되도록 바이트 배열 출력 스트림의 count 필드를 0으로 재설정합니다.
- `int size ()` — 버퍼의 현재 크기를 반환합니다.
- `byte[] toByteArray ()` — 새로 할당된 바이트 배열을 만듭니다.
- `String toString ()` — 플랫폼의 기본 문자 인코딩에 따라 바이트를 문자로 변환하여 버퍼 내용을 문자열로 변환합니다.
- `void write (byte[] b, int off, int len)` — off 오프셋에서 시작하여 지정된 바이트 배열의 len 바이트를 이 바이트 배열 출력 스트림에 씁니다.
- `void write (int b)` — 지정된 바이트를 이 바이트 배열 출력 스트림에 씁니다.

## 필드 상세

### buf

```java
protected byte[] buf
```

- 데이터가 저장되는 버퍼

### count

```java
protected int count
```

- 버퍼에 있는 유효 바이트 수

### ByteArrayOutputStream

```java
public ByteArrayOutputStream()
```

- 새로운 바이트 배열 출력 스트림을 만듭니다.
 초기 버퍼 용량은 32바이트지만 필요한 경우 크기가 증가합니다.

### ByteArrayOutputStream

```java
public ByteArrayOutputStream(int size)
```

- 지정된 크기(바이트)의 버퍼 용량을 가진 
 새로운 바이트 배열 출력 스트림을 만듭니다.

**Parameters:**
- `size` - 초기 크기

**Throws:**
- `IllegalArgumentException` - 크기가 음수인 경우

### write

```java
public void write(int b)
```

**Specified by:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 기록되는 바이트

### write

```java
public void write(byte[] b,
                  int off,
                  int len)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 기록할 바이트 수

### reset

```java
public void reset()
```

**See Also:**
- ``ByteArrayInputStream.count``

### toByteArray

```java
public byte[] toByteArray()
```

**Returns:**
- 이 출력 스트림의 현재 내용(바이트 배열)

**See Also:**
- ``size()``

### size

```java
public int size()
```

**Returns:**
- 이 출력 스트림의 유효 바이트 수인 `count` 
 필드 값

**See Also:**
- ``count``

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 버퍼 내용이 변환된 문자열

**Since:**
- JDK1.1

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `OutputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 생성자 상세

### ByteArrayOutputStream

```java
public ByteArrayOutputStream()
```

- 새로운 바이트 배열 출력 스트림을 만듭니다.
 초기 버퍼 용량은 32바이트지만 필요한 경우 크기가 증가합니다.

### ByteArrayOutputStream

```java
public ByteArrayOutputStream(int size)
```

- 지정된 크기(바이트)의 버퍼 용량을 가진 
 새로운 바이트 배열 출력 스트림을 만듭니다.

**Parameters:**
- `size` - 초기 크기

**Throws:**
- `IllegalArgumentException` - 크기가 음수인 경우

### write

```java
public void write(int b)
```

**Specified by:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 기록되는 바이트

### write

```java
public void write(byte[] b,
                  int off,
                  int len)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 기록할 바이트 수

### reset

```java
public void reset()
```

**See Also:**
- ``ByteArrayInputStream.count``

### toByteArray

```java
public byte[] toByteArray()
```

**Returns:**
- 이 출력 스트림의 현재 내용(바이트 배열)

**See Also:**
- ``size()``

### size

```java
public int size()
```

**Returns:**
- 이 출력 스트림의 유효 바이트 수인 `count` 
 필드 값

**See Also:**
- ``count``

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 버퍼 내용이 변환된 문자열

**Since:**
- JDK1.1

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `OutputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 메서드 상세

### write

```java
public void write(int b)
```

**Specified by:**
- `write` in class `OutputStream`

**Parameters:**
- `b` - 기록되는 바이트

### write

```java
public void write(byte[] b,
                  int off,
                  int len)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `len` - 기록할 바이트 수

### reset

```java
public void reset()
```

**See Also:**
- ``ByteArrayInputStream.count``

### toByteArray

```java
public byte[] toByteArray()
```

**Returns:**
- 이 출력 스트림의 현재 내용(바이트 배열)

**See Also:**
- ``size()``

### size

```java
public int size()
```

**Returns:**
- 이 출력 스트림의 유효 바이트 수인 `count` 
 필드 값

**See Also:**
- ``count``

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 버퍼 내용이 변환된 문자열

**Since:**
- JDK1.1

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `OutputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우
