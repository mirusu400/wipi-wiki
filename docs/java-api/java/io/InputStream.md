# Class InputStream

`package java.io`

```
java.lang.Object
  |
  +--java.io.InputStream
```

## 설명

**Direct Known Subclasses:**
- `ByteArrayInputStream`, `DataInputStream`

**extends Object:**

입력 스트림들이 상속받아야 할 추상 클래스.

## 생성자 요약

- InputStream ()

## 메서드 요약

- `int available ()` — 현재 입력 스트림에서 읽을 수 있는 정보량을 구한다.
- `void close ()` — 입력 스트림을 닫는다.
- `void mark (int readlimit)` — 입력 스트림에 mark정보를 설정한다.
- `boolean markSupported ()` — 입력 스트림이 mark기능을 지원하는지 여부를 구한다.
- `abstract  int read ()` — 한 바이트를 읽는다.
- `int read (byte[] buf)` — 바이트 배열로 읽는다.
- `int read (byte[] buf, int offset, int len)` — 바이트 배열 일부분으로 읽어 들인다.
- `void reset ()` — 입력 스트림의 읽는 위치를 mark정보에 설정된 위치로 변경한다.
- `long skip (long num_bytes_to_skip)` — 입력 스트림에서 정보를 읽지 않고 건너뛴다.

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
- 성공하면 읽은 바이트 정보 더 이상 읽을 것이 없으면 -1.

**Throws:**
- `IOException` -

### read

```java
public int read(byte[] buf)
         throws IOException
```

**Parameters:**
- `b` - 읽은 정보가 저장될 바이트 배열.

**Returns:**
- 실제 읽은 바이트 수 읽은 내용이 없으면 -1.

**Throws:**
- `IOException` -

### read

```java
public int read(byte[] buf,
                int offset,
                int len)
         throws IOException
```

**Parameters:**
- `len` - 읽을 바이트 수.

**Returns:**
- 실제 읽은 바이트 수 읽은 내용이 없으면 -1.

**Throws:**
- `IOException` -

### skip

```java
public long skip(long num_bytes_to_skip)
          throws IOException
```

**Parameters:**
- `n` - 건너 뛸 갯수.

**Returns:**
- 실제로 건너 뛴 갯수.

**Throws:**
- `IOException` -

### available

```java
public int available()
              throws IOException
```

**Returns:**
- 입력 스트림에서 읽을 수 있는 정보량.

**Throws:**
- `IOException` -

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` -

### mark

```java
public void mark(int readlimit)
```

- 입력 스트림에 mark정보를 설정한다.

### markSupported

```java
public boolean markSupported()
```

**Returns:**
- 지원하면 true 아니면 false.

### reset

```java
public void reset()
           throws IOException
```

**Throws:**
- `IOException` -

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 메서드 상세

### read

```java
public abstract int read()
                  throws IOException
```

**Returns:**
- 성공하면 읽은 바이트 정보 더 이상 읽을 것이 없으면 -1.

**Throws:**
- `IOException` -

### read

```java
public int read(byte[] buf)
         throws IOException
```

**Parameters:**
- `b` - 읽은 정보가 저장될 바이트 배열.

**Returns:**
- 실제 읽은 바이트 수 읽은 내용이 없으면 -1.

**Throws:**
- `IOException` -

### read

```java
public int read(byte[] buf,
                int offset,
                int len)
         throws IOException
```

**Parameters:**
- `len` - 읽을 바이트 수.

**Returns:**
- 실제 읽은 바이트 수 읽은 내용이 없으면 -1.

**Throws:**
- `IOException` -

### skip

```java
public long skip(long num_bytes_to_skip)
          throws IOException
```

**Parameters:**
- `n` - 건너 뛸 갯수.

**Returns:**
- 실제로 건너 뛴 갯수.

**Throws:**
- `IOException` -

### available

```java
public int available()
              throws IOException
```

**Returns:**
- 입력 스트림에서 읽을 수 있는 정보량.

**Throws:**
- `IOException` -

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` -

### mark

```java
public void mark(int readlimit)
```

- 입력 스트림에 mark정보를 설정한다.

### markSupported

```java
public boolean markSupported()
```

**Returns:**
- 지원하면 true 아니면 false.

### reset

```java
public void reset()
           throws IOException
```

**Throws:**
- `IOException` -

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
