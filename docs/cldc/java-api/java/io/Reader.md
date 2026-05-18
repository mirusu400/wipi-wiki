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

문자 스트림을 읽기 위한 추상 클래스. 
서브 클래스가 구현해야 하는 유일한 메소드는 read(char[], int, int)와 close()입니다. 
그러나 대부분의 서브 클래스는 효율성 증가나 추가 기능 제공, 또는 
둘 모두를 위해 여기에 정의된 일부 메소드를 무시합니다.

**Since:**
- JDK1.1, CLDC 1.0

**See Also:**
- ``InputStreamReader``, 
``Writer``

## 필드 요약

- `protected Object lock` — 이 스트림에 대한 작업을 동기화하는 데 사용된 객체.

## 생성자 요약

- `protected Reader ()` — 임계 지역이 판독기 자체에서 동기화되는 새로운 문자 스트림 판독기를 만듭니다.
- `protected Reader ( Object lock)` — 임계 지역이 지정된 객체에서 동기화되는 새로운 문자 스트림 판독기를 만듭니다.

## 메서드 요약

- `abstract  void close ()` — 스트림을 닫습니다.
- `void mark (int readAheadLimit)` — 스트림에서의 현재 위치를 표시합니다.
- `boolean markSupported ()` — 이 스트림이 mark() 작업을 지원하는지 알려줍니다.
- `int read ()` — 단일 문자를 읽습니다.
- `int read (char[] cbuf)` — 문자를 배열로 읽어 옵니다.
- `abstract  int read (char[] cbuf, int off, int len)` — 문자를 배열의 일부로 읽어 옵니다.
- `boolean ready ()` — 이 스트림을 읽을 준비가 되었는지 알려줍니다.
- `void reset ()` — 스트림을 재설정합니다.
- `long skip (long n)` — 문자를 건너뜁니다.

## 필드 상세

### lock

```java
protected Object lock
```

- 이 스트림에 대한 작업을 동기화하는 데 
사용된 객체. 효율성 증가를 위해 문자 스트림 객체는 자신 이외의 객체를 
사용하여 임계 영역을 보호할 수도 있습니다. 
따라서 서브 클래스는 이 필드에 있는 `this` 이외의 
객체나 동기화된 메소드를 사용해야 합니다.

### Reader

```java
protected Reader()
```

- 임계 지역이 판독기 자체에서 동기화되는 
새로운 문자 스트림 판독기를 만듭니다.

### Reader

```java
protected Reader(Object lock)
```

- 임계 지역이 지정된 객체에서 동기화되는 
새로운 문자 스트림 판독기를 만듭니다.

**Parameters:**
- `lock` - 동기화되는 객체

### read

```java
public int read()
         throws IOException
```

**Returns:**
- 0에서 65535(`0x00-0xffff`) 
 사이의 정수로 읽은 문자 또는 스트림 끝에 
 도달한 경우 -1

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public int read(char[] cbuf)
         throws IOException
```

**Parameters:**
- `cbuf` - 대상 버퍼

**Returns:**
- 읽은 바이트 수 또는 스트림의 끝에 
 도달한 경우 -1

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public abstract int read(char[] cbuf,
                         int off,
                         int len)
                  throws IOException
```

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

**Returns:**
- 이 스트림만 표시 작업을 지원하면 true입니다.

### mark

```java
public void mark(int readAheadLimit)
          throws IOException
```

**Parameters:**
- `readAheadLimit` - 표시가 유지되는 동안 읽을 수 있는 문자 수 제한
 이렇게 많은 문자를 읽은 후 스트림을 
 재설정하려고 하면 
 실패할 수도 있습니다.

**Throws:**
- `IOException` - 스트림이 mark()를 지원하지 않거나 
 다른 I/O 오류가 발생한 경우

### reset

```java
public void reset()
           throws IOException
```

**Throws:**
- `IOException` - 스트림이 표시되어 있지 않거나 
 표시가 무효화된 경우, 또는 
 스트림이 reset()을 
 지원하지 않거나 다른 I/O 오류가 발생한 경우

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 생성자 상세

### Reader

```java
protected Reader()
```

- 임계 지역이 판독기 자체에서 동기화되는 
새로운 문자 스트림 판독기를 만듭니다.

### Reader

```java
protected Reader(Object lock)
```

- 임계 지역이 지정된 객체에서 동기화되는 
새로운 문자 스트림 판독기를 만듭니다.

**Parameters:**
- `lock` - 동기화되는 객체

### read

```java
public int read()
         throws IOException
```

**Returns:**
- 0에서 65535(`0x00-0xffff`) 
 사이의 정수로 읽은 문자 또는 스트림 끝에 
 도달한 경우 -1

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public int read(char[] cbuf)
         throws IOException
```

**Parameters:**
- `cbuf` - 대상 버퍼

**Returns:**
- 읽은 바이트 수 또는 스트림의 끝에 
 도달한 경우 -1

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public abstract int read(char[] cbuf,
                         int off,
                         int len)
                  throws IOException
```

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

**Returns:**
- 이 스트림만 표시 작업을 지원하면 true입니다.

### mark

```java
public void mark(int readAheadLimit)
          throws IOException
```

**Parameters:**
- `readAheadLimit` - 표시가 유지되는 동안 읽을 수 있는 문자 수 제한
 이렇게 많은 문자를 읽은 후 스트림을 
 재설정하려고 하면 
 실패할 수도 있습니다.

**Throws:**
- `IOException` - 스트림이 mark()를 지원하지 않거나 
 다른 I/O 오류가 발생한 경우

### reset

```java
public void reset()
           throws IOException
```

**Throws:**
- `IOException` - 스트림이 표시되어 있지 않거나 
 표시가 무효화된 경우, 또는 
 스트림이 reset()을 
 지원하지 않거나 다른 I/O 오류가 발생한 경우

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 메서드 상세

### read

```java
public int read()
         throws IOException
```

**Returns:**
- 0에서 65535(`0x00-0xffff`) 
 사이의 정수로 읽은 문자 또는 스트림 끝에 
 도달한 경우 -1

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public int read(char[] cbuf)
         throws IOException
```

**Parameters:**
- `cbuf` - 대상 버퍼

**Returns:**
- 읽은 바이트 수 또는 스트림의 끝에 
 도달한 경우 -1

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public abstract int read(char[] cbuf,
                         int off,
                         int len)
                  throws IOException
```

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

**Returns:**
- 이 스트림만 표시 작업을 지원하면 true입니다.

### mark

```java
public void mark(int readAheadLimit)
          throws IOException
```

**Parameters:**
- `readAheadLimit` - 표시가 유지되는 동안 읽을 수 있는 문자 수 제한
 이렇게 많은 문자를 읽은 후 스트림을 
 재설정하려고 하면 
 실패할 수도 있습니다.

**Throws:**
- `IOException` - 스트림이 mark()를 지원하지 않거나 
 다른 I/O 오류가 발생한 경우

### reset

```java
public void reset()
           throws IOException
```

**Throws:**
- `IOException` - 스트림이 표시되어 있지 않거나 
 표시가 무효화된 경우, 또는 
 스트림이 reset()을 
 지원하지 않거나 다른 I/O 오류가 발생한 경우

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우
