# Class InputStreamReader

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

바이트 입력 스트림을 문자 스트림으로 변환해주는 클래스.

Fields inherited from class java.io. Reader lock

Constructor Summary InputStreamReader ( InputStream in) 새로운 객체를 생성한다. InputStreamReader ( InputStream in, String encoding_name) 특정 디코더를 사용하는 새로운 객체를 생성한다.

Method Summary void close () 입력 스트림을 닫는다. void mark (int readAheadLimit) mark를 설정한다. boolean markSupported () mark 기능을 지원하는지 여부를 구한다. int read () 한 문자를 읽는다. int read (char[] buf,
 int offset,
 int len) 문자 배열의 일부분으로 읽어 들인다. boolean ready () 정보를 읽을 수 있느지 여부를 구한다. void reset () 읽을 위치를 mark로 설정된 위치로 변경한다. long skip (long n) 입력 스트림에서 특정 갯수의 문자을 건너뛴다.

Methods inherited from class java.io. Reader read

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , toString , wait , wait , wait

Constructor Detail

### InputStreamReader

**Parameters:**
- `in` - 바이트 정보를 읽을 입력 스트림.

### InputStreamReader

**Parameters:**
- `encoding_name` - 사용할 디코더.

**Throws:**
- `UnsupportedEncodingException` - encoding_name이 지원할 수 없는 방식일 때 발생.

Method Detail

### ready

**Overrides:**
- `ready` in class `Reader`

**Returns:**
- 읽을 수 있으면 true 아니면 false.

**Throws:**
- `IOException` -

### read

**Overrides:**
- `read` in class `Reader`

**Returns:**
- 읽은 한문자.

**Throws:**
- `IOException` -

### read

**Overrides:**
- `read` in class `Reader`

**Parameters:**
- `len` - 읽은 문자의 갯수.

**Returns:**
- 실제 읽은 문자 수

**Throws:**
- `IOException` -

### skip

**Overrides:**
- `skip` in class `Reader`

**Parameters:**
- `n` - 건너 뛸 문자 수.

**Returns:**
- 실제 건너 뛴 문자 수.

**Throws:**
- `IOException` -

### markSupported

**Overrides:**
- `markSupported` in class `Reader`

**Returns:**
- 지원하면 true 아니면 false.

### mark

**Overrides:**
- `mark` in class `Reader`
- Following copied from class: `java.io.Reader`

**Throws:**
- `IOException` -

### reset

**Overrides:**
- `reset` in class `Reader`

**Throws:**
- `IOException` -

### close

**Overrides:**
- `close` in class `Reader`

**Throws:**
- `IOException` -## 생성자 요약

- InputStreamReader ( InputStream in) 새로운 객체를 생성한다.
- InputStreamReader ( InputStream in, String encoding_name) 특정 디코더를 사용하는 새로운 객체를 생성한다.

## 메서드 요약

- `void close ()` — 입력 스트림을 닫는다.
- `void mark (int readAheadLimit)` — mark를 설정한다.
- `boolean markSupported ()` — mark 기능을 지원하는지 여부를 구한다.
- `int read ()` — 한 문자를 읽는다.
- `int read (char[] buf, int offset, int len)` — 문자 배열의 일부분으로 읽어 들인다.
- `boolean ready ()` — 정보를 읽을 수 있느지 여부를 구한다.
- `void reset ()` — 읽을 위치를 mark로 설정된 위치로 변경한다.
- `long skip (long n)` — 입력 스트림에서 특정 갯수의 문자을 건너뛴다.

## 생성자 상세

### InputStreamReader

```java
public InputStreamReader(InputStream in)
```

**Parameters:**
- `in` - 바이트 정보를 읽을 입력 스트림.

### InputStreamReader

```java
public InputStreamReader(InputStream in,
                         String encoding_name)
                  throws UnsupportedEncodingException
```

**Parameters:**
- `encoding_name` - 사용할 디코더.

**Throws:**
- `UnsupportedEncodingException` - encoding_name이 지원할 수 없는 방식일 때 발생.

### ready

```java
public boolean ready()
              throws IOException
```

**Overrides:**
- `ready` in class `Reader`

**Returns:**
- 읽을 수 있으면 true 아니면 false.

**Throws:**
- `IOException` -

### read

```java
public int read()
         throws IOException
```

**Overrides:**
- `read` in class `Reader`

**Returns:**
- 읽은 한문자.

**Throws:**
- `IOException` -

### read

```java
public int read(char[] buf,
                int offset,
                int len)
         throws IOException
```

**Overrides:**
- `read` in class `Reader`

**Parameters:**
- `len` - 읽은 문자의 갯수.

**Returns:**
- 실제 읽은 문자 수

**Throws:**
- `IOException` -

### skip

```java
public long skip(long n)
          throws IOException
```

**Overrides:**
- `skip` in class `Reader`

**Parameters:**
- `n` - 건너 뛸 문자 수.

**Returns:**
- 실제 건너 뛴 문자 수.

**Throws:**
- `IOException` -

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `Reader`

**Returns:**
- 지원하면 true 아니면 false.

### mark

```java
public void mark(int readAheadLimit)
          throws IOException
```

**Overrides:**
- `mark` in class `Reader`
- Following copied from class: `java.io.Reader`

**Throws:**
- `IOException` -

### reset

```java
public void reset()
           throws IOException
```

**Overrides:**
- `reset` in class `Reader`

**Throws:**
- `IOException` -

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `Reader`

**Throws:**
- `IOException` -## 메서드 상세

### ready

```java
public boolean ready()
              throws IOException
```

**Overrides:**
- `ready` in class `Reader`

**Returns:**
- 읽을 수 있으면 true 아니면 false.

**Throws:**
- `IOException` -

### read

```java
public int read()
         throws IOException
```

**Overrides:**
- `read` in class `Reader`

**Returns:**
- 읽은 한문자.

**Throws:**
- `IOException` -

### read

```java
public int read(char[] buf,
                int offset,
                int len)
         throws IOException
```

**Overrides:**
- `read` in class `Reader`

**Parameters:**
- `len` - 읽은 문자의 갯수.

**Returns:**
- 실제 읽은 문자 수

**Throws:**
- `IOException` -

### skip

```java
public long skip(long n)
          throws IOException
```

**Overrides:**
- `skip` in class `Reader`

**Parameters:**
- `n` - 건너 뛸 문자 수.

**Returns:**
- 실제 건너 뛴 문자 수.

**Throws:**
- `IOException` -

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `Reader`

**Returns:**
- 지원하면 true 아니면 false.

### mark

```java
public void mark(int readAheadLimit)
          throws IOException
```

**Overrides:**
- `mark` in class `Reader`
- Following copied from class: `java.io.Reader`

**Throws:**
- `IOException` -

### reset

```java
public void reset()
           throws IOException
```

**Overrides:**
- `reset` in class `Reader`

**Throws:**
- `IOException` -

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `Reader`

**Throws:**
- `IOException` -

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
