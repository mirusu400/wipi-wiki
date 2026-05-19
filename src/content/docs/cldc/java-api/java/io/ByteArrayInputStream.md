---
title: "Class ByteArrayInputStream"
---

`package java.io`

```text
java.lang.Object
  |
  +--java.io.InputStream
        |
        +--java.io.ByteArrayInputStream
```

## 설명

**extends InputStream:**

`ByteArrayInputStream`에는
 스트림에서 읽을 수 있는 
 바이트가 포함되는 내부 버퍼가 있습니다. 
 내부 카운터는 `read` 
 메소드에서 제공할 다음 바이트를 추적합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 필드 요약

- `protected  byte[] buf` — 스트림을 만든 사람이 제공한 바이트 배열.
- `protected  int count` — 입력 스트림 버퍼의 마지막 유효 문자에 1을 더한 색인.
- `protected  int mark` — 스트림에서 현재 표시된 위치.
- `protected  int pos` — 입력 스트림 버퍼에서 읽을 다음 문자의 색인.

## 생성자 요약

- ByteArrayInputStream (byte[] buf) buf 를 버퍼 배열로 사용하도록 ByteArrayInputStream 을
 만듭니다.
- ByteArrayInputStream (byte[] buf,
 int offset,
 int length) buf 를 버퍼 배열로 사용하는 ByteArrayInputStream 을 만듭니다.

## 메서드 요약

- `int available ()` — 차단되지 않고 이 입력 스트림에서 읽을 수 있는 바이트 수를 반환합니다.
- `void close ()` — 이 입력 스트림을 닫고 스트림과 연결된 시스템 자원을 해제합니다.
- `void mark (int readAheadLimit)` — 스트림에서 현재 표시된 위치를 설정합니다.
- `boolean markSupported ()` — ByteArrayInputStream이 표시/재설정을 지원하는지 테스트합니다.
- `int read ()` — 이 입력 스트림에서 다음 바이트의 데이터를 읽습니다.
- `int read (byte[] b, int off, int len)` — 이 입력 스트림에서 최대 len 바이트의 데이터를 바이트 배열로 읽어 옵니다.
- `void reset ()` — 버퍼를 표시된 위치로 재설정합니다.
- `long skip (long n)` — 이 입력 스트림에서 n 바이트의 입력을 건너뜁니다.

## 필드 상세

### buf

```java
protected byte[] buf
```

- 스트림을 만든 사람이 제공한 바이트 배열.
 `buf[0]`에서
 `buf[count-1]`까지의
 요소가 스트림에서 읽을 수 있는 
 유일한 바이트입니다. `buf[pos]` 요소는
 읽을 다음 바이트입니다.

### pos

```java
protected int pos
```

- 입력 스트림 버퍼에서 읽을 다음 문자의 색인.
 이 값은 항상 음수가 아니고
 `count` 값보다 크지 않아야 합니다.
 입력 스트림 버퍼에서 읽을 다음 바이트는
 `buf[pos]`입니다.

### mark

```java
protected int mark
```

**Since:**
- JDK1.1

### count

```java
protected int count
```

- 입력 스트림 버퍼의 마지막 유효 문자에 1을 더한 색인.
 이 값은 항상 음수가 아니고
 `buf` 길이보다
 크지 않아야 합니다.
 입력 스트림 버퍼에서 읽을 수 있는
 `buf` 내의
 마지막 바이트 위치보다 1만큼 큽니다.

### ByteArrayInputStream

```java
public ByteArrayInputStream(byte[] buf)
```

- `buf`를 버퍼 배열로 사용하도록
 `ByteArrayInputStream`을
 만듭니다.
 버퍼 배열은 복사되지 않습니다.
 `pos`의 초기 값은
 `0`이고
 `count`의 초기 값은
 `buf` 길이입니다.

**Parameters:**
- `buf` - 입력 버퍼

### ByteArrayInputStream

```java
public ByteArrayInputStream(byte[] buf,
                            int offset,
                            int length)
```

- `buf`를 버퍼 배열로 사용하는 `ByteArrayInputStream`을 만듭니다.
 `pos`의 초기 값은
 `offset`이고
 `count`의 초기 값은
 `offset+length`입니다.
 버퍼 배열은 복사되지 않습니다.

결과로 만들어진 입력 스트림에서 단순히 바이트를 읽으면
 `buf[pos]`에서
 `buf[pos+len-1]`까지의 요소를 읽습니다.
 하지만 `reset` 작업을 수행하면
 `buf[0]`에서
 `buf[pos-1]`까지의
 바이트를 입력할 수 있게 됩니다.

**Parameters:**
- `length` - 버퍼에서 읽을 최대 바이트 수

### read

```java
public int read()
```

**Specified by:**
- `read` in class `InputStream`

**Returns:**
- 다음 바이트의 데이터 또는 스트림 끝에 도달한 경우
 `-1`

### read

```java
public int read(byte[] b,
                int off,
                int len)
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `len` - 읽는 최대 바이트 수

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 
 또는 스트림 끝에 도달하여 더 이상 
 데이터가 없는 경우 `-1`

**See Also:**
- ``InputStream.read()``

### skip

```java
public long skip(long n)
```

**Overrides:**
- `skip` in class `InputStream`

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

### available

```java
public int available()
```

**Overrides:**
- `available` in class `InputStream`

**Returns:**
- 차단되지 않고 입력 스트림에서 읽을 수 있는 
 바이트 수

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 이 true 유형이 mark 메소드와 reset 메소드를 지원하면 
 `true`, 지원하지 않으면 `false`

**Since:**
- JDK1.1

**See Also:**
- ``InputStream.mark(int)``, 
``InputStream.reset()``

### mark

```java
public void mark(int readAheadLimit)
```

**Overrides:**
- `mark` in class `InputStream`

**Parameters:**
- `readAheadLimit` - 표시 위치가 무효화될 때까지 읽을 수 있는 
 최대 바이트 수 한계

**Since:**
- JDK1.1

**See Also:**
- ``InputStream.reset()``

### reset

```java
public void reset()
```

**Overrides:**
- `reset` in class `InputStream`

**See Also:**
- ``InputStream.mark(int)``, 
``IOException``

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `InputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 생성자 상세

### ByteArrayInputStream

```java
public ByteArrayInputStream(byte[] buf)
```

- `buf`를 버퍼 배열로 사용하도록
 `ByteArrayInputStream`을
 만듭니다.
 버퍼 배열은 복사되지 않습니다.
 `pos`의 초기 값은
 `0`이고
 `count`의 초기 값은
 `buf` 길이입니다.

**Parameters:**
- `buf` - 입력 버퍼

### ByteArrayInputStream

```java
public ByteArrayInputStream(byte[] buf,
                            int offset,
                            int length)
```

- `buf`를 버퍼 배열로 사용하는 `ByteArrayInputStream`을 만듭니다.
 `pos`의 초기 값은
 `offset`이고
 `count`의 초기 값은
 `offset+length`입니다.
 버퍼 배열은 복사되지 않습니다.

결과로 만들어진 입력 스트림에서 단순히 바이트를 읽으면
 `buf[pos]`에서
 `buf[pos+len-1]`까지의 요소를 읽습니다.
 하지만 `reset` 작업을 수행하면
 `buf[0]`에서
 `buf[pos-1]`까지의
 바이트를 입력할 수 있게 됩니다.

**Parameters:**
- `length` - 버퍼에서 읽을 최대 바이트 수

### read

```java
public int read()
```

**Specified by:**
- `read` in class `InputStream`

**Returns:**
- 다음 바이트의 데이터 또는 스트림 끝에 도달한 경우
 `-1`

### read

```java
public int read(byte[] b,
                int off,
                int len)
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `len` - 읽는 최대 바이트 수

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 
 또는 스트림 끝에 도달하여 더 이상 
 데이터가 없는 경우 `-1`

**See Also:**
- ``InputStream.read()``

### skip

```java
public long skip(long n)
```

**Overrides:**
- `skip` in class `InputStream`

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

### available

```java
public int available()
```

**Overrides:**
- `available` in class `InputStream`

**Returns:**
- 차단되지 않고 입력 스트림에서 읽을 수 있는 
 바이트 수

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 이 true 유형이 mark 메소드와 reset 메소드를 지원하면 
 `true`, 지원하지 않으면 `false`

**Since:**
- JDK1.1

**See Also:**
- ``InputStream.mark(int)``, 
``InputStream.reset()``

### mark

```java
public void mark(int readAheadLimit)
```

**Overrides:**
- `mark` in class `InputStream`

**Parameters:**
- `readAheadLimit` - 표시 위치가 무효화될 때까지 읽을 수 있는 
 최대 바이트 수 한계

**Since:**
- JDK1.1

**See Also:**
- ``InputStream.reset()``

### reset

```java
public void reset()
```

**Overrides:**
- `reset` in class `InputStream`

**See Also:**
- ``InputStream.mark(int)``, 
``IOException``

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `InputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

## 메서드 상세

### read

```java
public int read()
```

**Specified by:**
- `read` in class `InputStream`

**Returns:**
- 다음 바이트의 데이터 또는 스트림 끝에 도달한 경우
 `-1`

### read

```java
public int read(byte[] b,
                int off,
                int len)
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `len` - 읽는 최대 바이트 수

**Returns:**
- 버퍼로 읽어들인 총 바이트 수 
 또는 스트림 끝에 도달하여 더 이상 
 데이터가 없는 경우 `-1`

**See Also:**
- ``InputStream.read()``

### skip

```java
public long skip(long n)
```

**Overrides:**
- `skip` in class `InputStream`

**Parameters:**
- `n` - 건너뛸 바이트 수

**Returns:**
- 건너뛴 실제 바이트 수

### available

```java
public int available()
```

**Overrides:**
- `available` in class `InputStream`

**Returns:**
- 차단되지 않고 입력 스트림에서 읽을 수 있는 
 바이트 수

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 이 true 유형이 mark 메소드와 reset 메소드를 지원하면 
 `true`, 지원하지 않으면 `false`

**Since:**
- JDK1.1

**See Also:**
- ``InputStream.mark(int)``, 
``InputStream.reset()``

### mark

```java
public void mark(int readAheadLimit)
```

**Overrides:**
- `mark` in class `InputStream`

**Parameters:**
- `readAheadLimit` - 표시 위치가 무효화될 때까지 읽을 수 있는 
 최대 바이트 수 한계

**Since:**
- JDK1.1

**See Also:**
- ``InputStream.reset()``

### reset

```java
public void reset()
```

**Overrides:**
- `reset` in class `InputStream`

**See Also:**
- ``InputStream.mark(int)``, 
``IOException``

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `InputStream`

**Throws:**
- `IOException` - I/O 오류가 발생한 경우
