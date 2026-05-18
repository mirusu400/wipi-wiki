# Class InputStream

`package java.io`

```text
java.lang.Object
  |
  +--java.io.InputStream
```

## 설명

**Direct Known Subclasses:**
- `ByteArrayInputStream`, `DataInputStream`

**extends Object:**

이 추상 클래스는 바이트 입력 스트림을 나타내는 
모든 클래스의 수퍼 클래스입니다.

`InputStream`의 서브 클래스를 정의할 필요가 있는 
응용 프로그램은 항상 다음 입력 바이트를 반환하는 메소드를 제공해야 합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``ByteArrayInputStream``, 
``DataInputStream``, 
``read()``, 
``OutputStream``

## 생성자 요약

- InputStream ()

## 메서드 요약

- `int available ()` — 이 입력 스트림에 대한 메소드의 다음 호출자가 차단되지 않고 이 입력 스트림에서 읽거나 건너뛸 수 있는 바이트 수를 반환합니다.
- `void close ()` — 이 입력 스트림을 닫고 스트림과 연결된 시스템 자원을 해제합니다.
- `void mark (int readlimit)` — 이 입력 스트림에서의 현재 위치를 표시합니다.
- `boolean markSupported ()` — 이 입력 스트림이 mark 및 reset 메소드를 지원하는지 테스트합니다.
- `abstract  int read ()` — 이 입력 스트림에서 다음 바이트의 데이터를 읽습니다.
- `int read (byte[] b)` — 입력 스트림에서 일부 바이트를 읽어 버퍼 배열 b 에 저장합니다.
- `int read (byte[] b, int off, int len)` — 입력 스트림에서 최대 len 바이트의 데이터를 바이트 배열로 읽어 옵니다.
- `void reset ()` — 이 입력 스트림에서 mark 메소드를 마지막으로 호출했을 때의 위치에 다시 스트림을 놓습니다.
- `long skip (long n)` — 이 입력 스트림에서 n 바이트의 데이터를 건너뛰어 무시합니다.

## 생성자 상세

### InputStream

```java
public InputStream()
```

### read

```java
public abstract int read()
                  throws IOException
```

**Returns:**
- 다음 바이트의 데이터 또는 
 스트림의 끝에 도달한 경우 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public int read(byte[] b)
         throws IOException
```

**Parameters:**
- `b` - 데이터를 읽어들이는 버퍼

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 또는 
 스트림의 끝에 도달하여 더 이상 데이터가 없는 경우 
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``read(byte[], int, int)``

### read

```java
public int read(byte[] b,
                int off,
                int len)
         throws IOException
```

**Parameters:**
- `len` - 읽는 최대 바이트 수

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 또는
 스트림의 끝에 도달하여 더 이상 데이터가 없는 경우 
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``read()``

### skip

```java
public long skip(long n)
          throws IOException
```

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### available

```java
public int available()
              throws IOException
```

**Returns:**
- 차단되지 않고 입력 스트림에서 
 읽을 수 있는 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### mark

```java
public void mark(int readlimit)
```

**Parameters:**
- `readlimit` - 표시 위치가 무효화될 때까지 읽을 수 있는 
 최대 바이트 수 한계

**See Also:**
- ``reset()``

### reset

```java
public void reset()
           throws IOException
```

**Throws:**
- `IOException` - 이 스트림이 표시되어 있지 않거나 
 표시가 무효화된 경우

**See Also:**
- ``mark(int)``, 
``IOException``

### markSupported

```java
public boolean markSupported()
```

**Returns:**
- 이 true 유형이 mark 메소드와 reset 메소드를 지원하면 
 `true`, 지원하지 않으면 `false`

**See Also:**
- ``mark(int)``, 
``reset()``

## 메서드 상세

### read

```java
public abstract int read()
                  throws IOException
```

**Returns:**
- 다음 바이트의 데이터 또는 
 스트림의 끝에 도달한 경우 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### read

```java
public int read(byte[] b)
         throws IOException
```

**Parameters:**
- `b` - 데이터를 읽어들이는 버퍼

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 또는 
 스트림의 끝에 도달하여 더 이상 데이터가 없는 경우 
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``read(byte[], int, int)``

### read

```java
public int read(byte[] b,
                int off,
                int len)
         throws IOException
```

**Parameters:**
- `len` - 읽는 최대 바이트 수

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 또는
 스트림의 끝에 도달하여 더 이상 데이터가 없는 경우 
 `-1`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

**See Also:**
- ``read()``

### skip

```java
public long skip(long n)
          throws IOException
```

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### available

```java
public int available()
              throws IOException
```

**Returns:**
- 차단되지 않고 입력 스트림에서 
 읽을 수 있는 바이트 수

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### mark

```java
public void mark(int readlimit)
```

**Parameters:**
- `readlimit` - 표시 위치가 무효화될 때까지 읽을 수 있는 
 최대 바이트 수 한계

**See Also:**
- ``reset()``

### reset

```java
public void reset()
           throws IOException
```

**Throws:**
- `IOException` - 이 스트림이 표시되어 있지 않거나 
 표시가 무효화된 경우

**See Also:**
- ``mark(int)``, 
``IOException``

### markSupported

```java
public boolean markSupported()
```

**Returns:**
- 이 true 유형이 mark 메소드와 reset 메소드를 지원하면 
 `true`, 지원하지 않으면 `false`

**See Also:**
- ``mark(int)``, 
``reset()``
