---
title: "Class OutputStream"
---

`package java.io`

```text
java.lang.Object
  |
  +--java.io.OutputStream
```

## 설명

**Direct Known Subclasses:**
- `ByteArrayOutputStream`, `DataOutputStream`, `PrintStream`

**extends Object:**

출력 스트림들이 상속받아야 할 추상 클래스.

## 생성자 요약

- OutputStream () 새로운 객체를 생성한다.

## 메서드 요약

- `void close ()` — 출력 스트림을 닫는다.
- `void flush ()` — 중간 버퍼에 남아있는 정보들을 실제 출력한다.
- `void write (byte[] buf)` — 바이트 배열을 출력한다.
- `void write (byte[] buf, int offset, int len)` — 바이트 배열의 일부분을 출력한다.
- `abstract  void write (int b)` — 매개변수로 받은 변수 값 중 상위 24비트는 버리고 나머지 8비트만 출력한다.

## 생성자 상세

### OutputStream

```java
public OutputStream()
```

- 새로운 객체를 생성한다.

### flush

```java
public void flush()
           throws IOException
```

**Throws:**
- `IOException` -

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` -

### write

```java
public abstract void write(int b)
                    throws IOException
```

**Parameters:**
- `b` - 출력할 정보.

**Throws:**
- `IOException` -

### write

```java
public void write(byte[] buf)
           throws IOException
```

**Parameters:**
- `buf` - 출력할 바이트 배열.

**Throws:**
- `IOException` -

### write

```java
public void write(byte[] buf,
                  int offset,
                  int len)
           throws IOException
```

**Parameters:**
- `len` - 출력할 갯수.

**Throws:**
- `IOException` -## 메서드 상세

### flush

```java
public void flush()
           throws IOException
```

**Throws:**
- `IOException` -

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` -

### write

```java
public abstract void write(int b)
                    throws IOException
```

**Parameters:**
- `b` - 출력할 정보.

**Throws:**
- `IOException` -

### write

```java
public void write(byte[] buf)
           throws IOException
```

**Parameters:**
- `buf` - 출력할 바이트 배열.

**Throws:**
- `IOException` -

### write

```java
public void write(byte[] buf,
                  int offset,
                  int len)
           throws IOException
```

**Parameters:**
- `len` - 출력할 갯수.

**Throws:**
- `IOException` -

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
