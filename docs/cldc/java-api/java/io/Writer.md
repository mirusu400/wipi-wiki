# Class Writer

`package java.io`

```
java.lang.Object
  |
  +--java.io.Writer
```

## 설명

**Direct Known Subclasses:**
- `OutputStreamWriter`

**extends Object:**

문자 스트림에 쓰기 위한 추상 클래스 
서브 클래스가 구현해야 하는 유일한 메소드는 write(char[], int, int), flush() 및 close()입니다. 
그러나 대부분의 서브 클래스는 효율성 증가나 추가 기능 제공, 또는 
둘 모두를 위해 여기에 정의된 일부 메소드를 무시합니다.

**Since:**
- JDK1.1, CLDC 1.0

**See Also:**
- ``OutputStreamWriter``, 
``Reader``

## 필드 요약

- `protected Object lock` — 이 스트림에 대한 작업을 동기화하는 데 사용된 객체.

## 생성자 요약

- `protected Writer ()` — 임계 지역이 작성기 자체에서 동기화되는 새로운 문자 스트림 작성기를 만듭니다.
- `protected Writer ( Object lock)` — 임계 지역이 지정된 객체에서 동기화되는 새로운 문자 스트림 작성기를 만듭니다.

## 메서드 요약

- `abstract  void close ()` — 스트림을 먼저 플러시한 후 닫습니다.
- `abstract  void flush ()` — 스트림을 플러시합니다.
- `void write (char[] cbuf)` — 문자 배열을 씁니다.
- `abstract  void write (char[] cbuf, int off, int len)` — 문자 배열의 일부를 씁니다.
- `void write (int c)` — 단일 문자를 씁니다.
- `void write ( String str)` — 문자열을 씁니다.
- `void write ( String str, int off, int len)` — 문자열의 일부를 씁니다.

## 필드 상세

### lock

```java
protected Object lock
```

- 이 스트림에 대한 작업을 동기화하는 데 사용된 객체. 
효율성 증가를 위해 문자 스트림 객체는 자신 이외의 객체를 사용하여 
임계 영역을 보호할 수도 있습니다. 
따라서 서브 클래스는 이 필드에 있는 `this` 이외의 
객체나 동기화된 메소드를 사용해야 합니다.

### Writer

```java
protected Writer()
```

- 임계 지역이 작성기 자체에서 동기화되는 
새로운 문자 스트림 작성기를 만듭니다.

### Writer

```java
protected Writer(Object lock)
```

- 임계 지역이 지정된 객체에서 동기화되는 
새로운 문자 스트림 작성기를 만듭니다.

**Parameters:**
- `lock` - 동기화되는 객체

### write

```java
public void write(int c)
           throws IOException
```

**Parameters:**
- `c` - 기록되는 문자를 지정하는 int

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(char[] cbuf)
           throws IOException
```

**Parameters:**
- `cbuf` - 기록되는 문자 배열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public abstract void write(char[] cbuf,
                           int off,
                           int len)
                    throws IOException
```

**Parameters:**
- `len` - 기록할 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(String str)
           throws IOException
```

**Parameters:**
- `str` - 기록되는 문자열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(String str,
                  int off,
                  int len)
           throws IOException
```

**Parameters:**
- `len` - 기록할 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### flush

```java
public abstract void flush()
                    throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 생성자 상세

### Writer

```java
protected Writer()
```

- 임계 지역이 작성기 자체에서 동기화되는 
새로운 문자 스트림 작성기를 만듭니다.

### Writer

```java
protected Writer(Object lock)
```

- 임계 지역이 지정된 객체에서 동기화되는 
새로운 문자 스트림 작성기를 만듭니다.

**Parameters:**
- `lock` - 동기화되는 객체

### write

```java
public void write(int c)
           throws IOException
```

**Parameters:**
- `c` - 기록되는 문자를 지정하는 int

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(char[] cbuf)
           throws IOException
```

**Parameters:**
- `cbuf` - 기록되는 문자 배열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public abstract void write(char[] cbuf,
                           int off,
                           int len)
                    throws IOException
```

**Parameters:**
- `len` - 기록할 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(String str)
           throws IOException
```

**Parameters:**
- `str` - 기록되는 문자열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(String str,
                  int off,
                  int len)
           throws IOException
```

**Parameters:**
- `len` - 기록할 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### flush

```java
public abstract void flush()
                    throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 메서드 상세

### write

```java
public void write(int c)
           throws IOException
```

**Parameters:**
- `c` - 기록되는 문자를 지정하는 int

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(char[] cbuf)
           throws IOException
```

**Parameters:**
- `cbuf` - 기록되는 문자 배열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public abstract void write(char[] cbuf,
                           int off,
                           int len)
                    throws IOException
```

**Parameters:**
- `len` - 기록할 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(String str)
           throws IOException
```

**Parameters:**
- `str` - 기록되는 문자열

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### write

```java
public void write(String str,
                  int off,
                  int len)
           throws IOException
```

**Parameters:**
- `len` - 기록할 문자 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### flush

```java
public abstract void flush()
                    throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우
