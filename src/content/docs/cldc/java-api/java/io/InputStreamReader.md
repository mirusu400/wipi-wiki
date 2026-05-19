---
title: "Class InputStreamReader"
---

`package java.io`

```text
java.lang.Object
  |
  +--java.io.Reader
        |
        +--java.io.InputStreamReader
```

## 설명

**extends Reader:**

InputStreamReader가 바이트 스트림에서 문자 스트림으로의 
브릿지 역할을 하는 경우 바이트를 읽어 문자로 변환합니다. 
사용할 인코딩을 이름으로 지정하거나 
플랫폼의 기본 인코딩을 사용할 수 있습니다.

InputStreamReader의 read() 메소드 중 하나를 호출할 때마다 
기본 바이트 입력 스트림에서 1바이트 이상이 읽혀질 수 있습니다. 
바이트에서 문자로의 효율적 변환을 위해 기본 스트림에서 
현재 읽기 작업에 필요한 것보다 
많은 바이트를 미리 읽을 수도 있습니다.

**Since:**
- CLDC 1.0

**See Also:**
- ``Reader``, 
``UnsupportedEncodingException``

## 필드 요약

## 생성자 요약

- InputStreamReader ( InputStream is) 기본 문자 인코딩을 사용하는 InputStreamReader를 만듭니다.
- InputStreamReader ( InputStream is, String enc) 명명된 문자 인코딩을 사용하는 InputStreamReader를 만듭니다.

## 메서드 요약

- `void close ()` — 스트림을 닫습니다.
- `void mark (int readAheadLimit)` — 스트림에서의 현재 위치를 표시합니다.
- `boolean markSupported ()` — 이 스트림이 mark() 작업을 지원하는지 알려줍니다.
- `int read ()` — 단일 문자를 읽습니다.
- `int read (char[] cbuf, int off, int len)` — 문자를 배열의 일부로 읽어 옵니다.
- `boolean ready ()` — 이 스트림을 읽을 준비가 되었는지 알려줍니다.
- `void reset ()` — 스트림을 재설정합니다.
- `long skip (long n)` — 문자를 건너뜁니다.

## 생성자 상세

### InputStreamReader

```java
public InputStreamReader(InputStream is)
```

- 기본 문자 인코딩을 사용하는 InputStreamReader를 만듭니다.

**Parameters:**
- `is` - InputStream

### InputStreamReader

```java
public InputStreamReader(InputStream is,
                         String enc)
                  throws UnsupportedEncodingException
```

- 명명된 문자 인코딩을 사용하는 InputStreamReader를 만듭니다.

**Parameters:**
- `enc` - 지원되는 문자 인코딩 이름

**Throws:**
- `UnsupportedEncodingException` - 명명된 인코딩이 지원되지 않는 경우

### read

```java
public int read()
         throws IOException
```

**Overrides:**
- `read` in class `Reader`

**Returns:**
- 읽은 문자 또는 스트림의 끝에 
 도달한 경우 -1

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public int read(char[] cbuf,
                int off,
                int len)
         throws IOException
```

**Specified by:**
- `read` in class `Reader`

**Parameters:**
- `len` - 읽을 최대 문자 수

**Returns:**
- 읽은 문자 수 또는 스트림의 끝에 
 도달한 경우 -1

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### skip

```java
public long skip(long n)
          throws IOException
```

**Overrides:**
- `skip` in class `Reader`

**Parameters:**
- `n` - 건너뛸 문자 수

**Returns:**
- 실제로 건너뛴 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### ready

```java
public boolean ready()
              throws IOException
```

**Overrides:**
- `ready` in class `Reader`

**Returns:**
- 다음 read()가 입력을 위해 차단되지 않으면 true, 
차단되면 false입니다. false를 반환해도 
다음 읽기가 반드시 차단되는 것은 아닙니다.

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `Reader`

**Returns:**
- 이 스트림만 표시 작업을 지원하면 true입니다.

### mark

```java
public void mark(int readAheadLimit)
          throws IOException
```

**Overrides:**
- `mark` in class `Reader`

**Parameters:**
- `readAheadLimit` - 표시가 유지되는 동안 읽을 수 있는 
 문자 수 제한.
 이렇게 많은 문자를 읽은 후 스트림을 재설정하려고 
 하면 실패할 수도 있습니다.

**Throws:**
- `IOException` - 스트림이 mark()를 지원하지 않거나 
 다른 I/O 오류가 발생한 경우

### reset

```java
public void reset()
           throws IOException
```

**Overrides:**
- `reset` in class `Reader`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Specified by:**
- `close` in class `Reader`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 메서드 상세

### read

```java
public int read()
         throws IOException
```

**Overrides:**
- `read` in class `Reader`

**Returns:**
- 읽은 문자 또는 스트림의 끝에 
 도달한 경우 -1

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public int read(char[] cbuf,
                int off,
                int len)
         throws IOException
```

**Specified by:**
- `read` in class `Reader`

**Parameters:**
- `len` - 읽을 최대 문자 수

**Returns:**
- 읽은 문자 수 또는 스트림의 끝에 
 도달한 경우 -1

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### skip

```java
public long skip(long n)
          throws IOException
```

**Overrides:**
- `skip` in class `Reader`

**Parameters:**
- `n` - 건너뛸 문자 수

**Returns:**
- 실제로 건너뛴 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### ready

```java
public boolean ready()
              throws IOException
```

**Overrides:**
- `ready` in class `Reader`

**Returns:**
- 다음 read()가 입력을 위해 차단되지 않으면 true, 
차단되면 false입니다. false를 반환해도 
다음 읽기가 반드시 차단되는 것은 아닙니다.

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `Reader`

**Returns:**
- 이 스트림만 표시 작업을 지원하면 true입니다.

### mark

```java
public void mark(int readAheadLimit)
          throws IOException
```

**Overrides:**
- `mark` in class `Reader`

**Parameters:**
- `readAheadLimit` - 표시가 유지되는 동안 읽을 수 있는 
 문자 수 제한.
 이렇게 많은 문자를 읽은 후 스트림을 재설정하려고 
 하면 실패할 수도 있습니다.

**Throws:**
- `IOException` - 스트림이 mark()를 지원하지 않거나 
 다른 I/O 오류가 발생한 경우

### reset

```java
public void reset()
           throws IOException
```

**Overrides:**
- `reset` in class `Reader`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Specified by:**
- `close` in class `Reader`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우
