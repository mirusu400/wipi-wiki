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

바이트 형 정보의 입력 스트림을 구현한 클래스.

## 필드 요약

- `protected  byte[] buf` — 바이트형 정보가 저장된 버퍼.
- `protected  int count` — buf에 저장된 바이트 정보량.
- `protected  int mark` — mark기능을 위한 위치정보 저장변수.
- `protected  int pos` — buf내에서 다음에 읽을 위치.

## 생성자 요약

- ByteArrayInputStream (byte[] buf) 특정 바이트 배열 정보를 읽을 수 있도록 새로운 ByteArrayInputStream 객체를
 생성한다.
- ByteArrayInputStream (byte[] buf,
 int offset,
 int length) 특정 바이트 배열 정보 중 일부분를 읽을 수 있도록 새로운 ByteArrayInputStream 객체를
 생성한다.

## 메서드 요약

- `int available ()` — 현 압력 스트림으로 부터 읽을 수 있는 정보의 갯수를 구한다.
- `void close ()` — 입력스트림을 닫는다.
- `void mark (int readlimit)` — 입력 스트림 내에서 mark정보를 저장한다.
- `boolean markSupported ()` — mark기능을 지원하는지 여부를 구한다.
- `int read ()` — 입력 스트림으로 부터 한 바이트 정보를 읽는다.
- `int read (byte[] buf, int offset, int len)` — 입력 스트림으로 부터 특정 배열로 바이트 정보를 읽는다.
- `void reset ()` — 입력 스트림 내에서 다음에 읽을 위치를 mark메소드를 통해 저장한 값으로 복원한다.
- `long skip (long num_bytes)` — 입력 스트림을 읽지 않고 특정 갯수만큼 건너 뛴다.

## 필드 상세

### buf

```java
protected byte[] buf
```

- 바이트형 정보가 저장된 버퍼.

### pos

```java
protected int pos
```

- buf내에서 다음에 읽을 위치.

### mark

```java
protected int mark
```

- mark기능을 위한 위치정보 저장변수.

### count

```java
protected int count
```

- buf에 저장된 바이트 정보량.

### ByteArrayInputStream

```java
public ByteArrayInputStream(byte[] buf)
```

**Parameters:**
- `buf` - 입력스트림을 만들 대상.

### ByteArrayInputStream

```java
public ByteArrayInputStream(byte[] buf,
                            int offset,
                            int length)
```

**Parameters:**
- `length` - 입력스트림을 만들 대상의 길이.

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `InputStream`
- Following copied from class: `java.io.InputStream`

**Throws:**
- `IOException` -

### available

```java
public int available()
```

**Overrides:**
- `available` in class `InputStream`

**Returns:**
- 현 압력 스트림으로 부터 읽을 수 있는 정보의 갯수.

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 항상 true.

### mark

```java
public void mark(int readlimit)
```

**Overrides:**
- `mark` in class `InputStream`

### reset

```java
public void reset()
```

**Overrides:**
- `reset` in class `InputStream`
- Following copied from class: `java.io.InputStream`

**Throws:**
- `IOException` -

### skip

```java
public long skip(long num_bytes)
          throws IOException
```

**Overrides:**
- `skip` in class `InputStream`

**Parameters:**
- `num_bytes` - 건너 뛸 갯수.

**Returns:**
- 실제 건너 뛴 갯수.

### read

```java
public int read()
```

**Overrides:**
- `read` in class `InputStream`

**Returns:**
- 읽을 내용이 없으면 -1 아니면 읽은 값.

### read

```java
public int read(byte[] buf,
                int offset,
                int len)
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `len` - 읽고자 하는 갯수.

**Returns:**
- 읽을 내용이 없으면 -1 아니면 실제 읽은 갯수.## 생성자 상세

### ByteArrayInputStream

```java
public ByteArrayInputStream(byte[] buf)
```

**Parameters:**
- `buf` - 입력스트림을 만들 대상.

### ByteArrayInputStream

```java
public ByteArrayInputStream(byte[] buf,
                            int offset,
                            int length)
```

**Parameters:**
- `length` - 입력스트림을 만들 대상의 길이.

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `InputStream`
- Following copied from class: `java.io.InputStream`

**Throws:**
- `IOException` -

### available

```java
public int available()
```

**Overrides:**
- `available` in class `InputStream`

**Returns:**
- 현 압력 스트림으로 부터 읽을 수 있는 정보의 갯수.

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 항상 true.

### mark

```java
public void mark(int readlimit)
```

**Overrides:**
- `mark` in class `InputStream`

### reset

```java
public void reset()
```

**Overrides:**
- `reset` in class `InputStream`
- Following copied from class: `java.io.InputStream`

**Throws:**
- `IOException` -

### skip

```java
public long skip(long num_bytes)
          throws IOException
```

**Overrides:**
- `skip` in class `InputStream`

**Parameters:**
- `num_bytes` - 건너 뛸 갯수.

**Returns:**
- 실제 건너 뛴 갯수.

### read

```java
public int read()
```

**Overrides:**
- `read` in class `InputStream`

**Returns:**
- 읽을 내용이 없으면 -1 아니면 읽은 값.

### read

```java
public int read(byte[] buf,
                int offset,
                int len)
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `len` - 읽고자 하는 갯수.

**Returns:**
- 읽을 내용이 없으면 -1 아니면 실제 읽은 갯수.## 메서드 상세

### close

```java
public void close()
           throws IOException
```

**Overrides:**
- `close` in class `InputStream`
- Following copied from class: `java.io.InputStream`

**Throws:**
- `IOException` -

### available

```java
public int available()
```

**Overrides:**
- `available` in class `InputStream`

**Returns:**
- 현 압력 스트림으로 부터 읽을 수 있는 정보의 갯수.

### markSupported

```java
public boolean markSupported()
```

**Overrides:**
- `markSupported` in class `InputStream`

**Returns:**
- 항상 true.

### mark

```java
public void mark(int readlimit)
```

**Overrides:**
- `mark` in class `InputStream`

### reset

```java
public void reset()
```

**Overrides:**
- `reset` in class `InputStream`
- Following copied from class: `java.io.InputStream`

**Throws:**
- `IOException` -

### skip

```java
public long skip(long num_bytes)
          throws IOException
```

**Overrides:**
- `skip` in class `InputStream`

**Parameters:**
- `num_bytes` - 건너 뛸 갯수.

**Returns:**
- 실제 건너 뛴 갯수.

### read

```java
public int read()
```

**Overrides:**
- `read` in class `InputStream`

**Returns:**
- 읽을 내용이 없으면 -1 아니면 읽은 값.

### read

```java
public int read(byte[] buf,
                int offset,
                int len)
```

**Overrides:**
- `read` in class `InputStream`

**Parameters:**
- `len` - 읽고자 하는 갯수.

**Returns:**
- 읽을 내용이 없으면 -1 아니면 실제 읽은 갯수.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
