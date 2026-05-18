# Class Reader

`package java.io`

```text
java.lang.Object
  |
  +--java.io.Reader
```

## 설명

**Direct Known Subclasses:**
- `InputStreamReader`

**extends Object:**

바이트 입력 스트림을 문자 스트림으로 변환해주는 클래스를 위한
 추상클래스.

## 필드 요약

- `protected Object lock`

## 생성자 요약

- `protected Reader ()` — Reader를 생성한다.
- `protected Reader ( Object lock)` — Reader를 생성한다.

## 메서드 요약

- `abstract  void close ()` — 입력 스트림을 닫는다.
- `void mark (int readLimit)` — mark를 설정한다.
- `boolean markSupported ()` — mark 기능을 지원하는지 여부를 구한다.
- `int read ()` — 한 문자를 읽는다.
- `int read (char[] buf)` — 문자배열로 문자를 읽는다.
- `abstract  int read (char[] buf, int offset, int count)` — 문자배열 특정 부분으로 문자를 읽는다.
- `boolean ready ()` — 현 입력스트림에서 문자를 읽을 수 있는 지 여부를 구한다.
- `void reset ()` — 읽을 위치를 mark로 설정된 위치로 변경한다.
- `long skip (long count)` — 특정 갯수의 문자를 읽지 않고 건너 뛴다.

## 필드 상세

### lock

```java
protected Object lock
```

### Reader

```java
protected Reader()
```

- Reader를 생성한다. 동기화를 위한 lock은 자기자신을 
 사용한다.

### Reader

```java
protected Reader(Object lock)
```

- Reader를 생성한다. 동기화를 위한 lock은 매개변수로 받은
 객체를 사용한다.

### read

```java
public int read()
         throws IOException
```

**Returns:**
- 성공하면 읽은 문자 읽은 문자가 없으면 -1.

**Throws:**
- `IOException` -

### read

```java
public int read(char[] buf)
         throws IOException
```

**Parameters:**
- `buf` - 읽을 문자를 저장할 문자배열.

**Returns:**
- 실제 읽은 문자 갯수 읽은 문자가 없으면 -1.

**Throws:**
- `IOException` -

### read

```java
public abstract int read(char[] buf,
                         int offset,
                         int count)
                  throws IOException
```

**Parameters:**
- `count` - 읽을 문자 갯수.

**Returns:**
- 실제 읽은 문자 갯수 읽은 문자가 없으면 -1.

**Throws:**
- `IOException` -

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` -

### mark

```java
public void mark(int readLimit)
          throws IOException
```

**Throws:**
- `IOException` -

### markSupported

```java
public boolean markSupported()
```

**Returns:**
- 지원하면 true 아니면 false.

### ready

```java
public boolean ready()
              throws IOException
```

**Returns:**
- 아직 읽을 준비가 안瑛만

## 생성자 상세

### Reader

```java
protected Reader()
```

- Reader를 생성한다. 동기화를 위한 lock은 자기자신을 
 사용한다.

### Reader

```java
protected Reader(Object lock)
```

- Reader를 생성한다. 동기화를 위한 lock은 매개변수로 받은
 객체를 사용한다.

### read

```java
public int read()
         throws IOException
```

**Returns:**
- 성공하면 읽은 문자 읽은 문자가 없으면 -1.

**Throws:**
- `IOException` -

### read

```java
public int read(char[] buf)
         throws IOException
```

**Parameters:**
- `buf` - 읽을 문자를 저장할 문자배열.

**Returns:**
- 실제 읽은 문자 갯수 읽은 문자가 없으면 -1.

**Throws:**
- `IOException` -

### read

```java
public abstract int read(char[] buf,
                         int offset,
                         int count)
                  throws IOException
```

**Parameters:**
- `count` - 읽을 문자 갯수.

**Returns:**
- 실제 읽은 문자 갯수 읽은 문자가 없으면 -1.

**Throws:**
- `IOException` -

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` -

### mark

```java
public void mark(int readLimit)
          throws IOException
```

**Throws:**
- `IOException` -

### markSupported

```java
public boolean markSupported()
```

**Returns:**
- 지원하면 true 아니면 false.

### ready

```java
public boolean ready()
              throws IOException
```

**Returns:**
- 아직 읽을 준비가 안瑛만

## 메서드 상세

### read

```java
public int read()
         throws IOException
```

**Returns:**
- 성공하면 읽은 문자 읽은 문자가 없으면 -1.

**Throws:**
- `IOException` -

### read

```java
public int read(char[] buf)
         throws IOException
```

**Parameters:**
- `buf` - 읽을 문자를 저장할 문자배열.

**Returns:**
- 실제 읽은 문자 갯수 읽은 문자가 없으면 -1.

**Throws:**
- `IOException` -

### read

```java
public abstract int read(char[] buf,
                         int offset,
                         int count)
                  throws IOException
```

**Parameters:**
- `count` - 읽을 문자 갯수.

**Returns:**
- 실제 읽은 문자 갯수 읽은 문자가 없으면 -1.

**Throws:**
- `IOException` -

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` -

### mark

```java
public void mark(int readLimit)
          throws IOException
```

**Throws:**
- `IOException` -

### markSupported

```java
public boolean markSupported()
```

**Returns:**
- 지원하면 true 아니면 false.

### ready

```java
public boolean ready()
              throws IOException
```

**Returns:**
- 아직 읽을 준비가 안瑛만
