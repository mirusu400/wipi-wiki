# Class Writer

`package java.io`

```text
java.lang.Object
  |
  +--java.io.Writer
```

## 설명

**Direct Known Subclasses:**
- `OutputStreamWriter`

**extends Object:**

Unicode로 된 내부 문자열을 KSC5601과 같은 형식의 문자열로
 변환하여 출력하는 출력 스트림의 추상클래스

## 필드 요약

- `protected Object lock`

## 생성자 요약

- `protected Writer ()` — 출력스트림을 생성한다.
- `protected Writer ( Object lock)` — 출력스트림을 생성한다.

## 메서드 요약

- `abstract  void close ()` — 출력스트림을 닫는다.
- `abstract  void flush ()` — 중간 버퍼에 남아있는 값을 실제로 출력한다.
- `void write (char[] buf)` — 문자배열을 출력한다.
- `abstract  void write (char[] buf, int offset, int len)` — 문자배열을 출력한다.
- `void write (int b)` — 한문자를 출력한다.
- `void write ( String str)` — 문자열을 출력한다.
- `void write ( String str, int offset, int len)` — 문자열을 출력한다.

## 필드 상세

### lock

```java
protected Object lock
```

### Writer

```java
protected Writer()
```

- 출력스트림을 생성한다. 동기화를 위한 lock은 자기자신을 
 사용한다.

### Writer

```java
protected Writer(Object lock)
```

- 출력스트림을 생성한다. 동기화를 위한 lock은 매개변수로 받은
 객체를 사용한다.

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` -

### flush

```java
public abstract void flush()
                    throws IOException
```

**Throws:**
- `IOException` -

### write

```java
public abstract void write(char[] buf,
                           int offset,
                           int len)
                    throws IOException
```

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -

### write

```java
public void write(char[] buf)
           throws IOException
```

**Parameters:**
- `buf` - 출력할 문자배열.

**Throws:**
- `IOException` -

### write

```java
public void write(int b)
           throws IOException
```

**Parameters:**
- `b` - 출력할 문자.

**Throws:**
- `IOException` -

### write

```java
public void write(String str)
           throws IOException
```

**Parameters:**
- `str` - 출력할 문자열.

**Throws:**
- `IOException` -

### write

```java
public void write(String str,
                  int offset,
                  int len)
           throws IOException
```

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -## 생성자 상세

### Writer

```java
protected Writer()
```

- 출력스트림을 생성한다. 동기화를 위한 lock은 자기자신을 
 사용한다.

### Writer

```java
protected Writer(Object lock)
```

- 출력스트림을 생성한다. 동기화를 위한 lock은 매개변수로 받은
 객체를 사용한다.

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` -

### flush

```java
public abstract void flush()
                    throws IOException
```

**Throws:**
- `IOException` -

### write

```java
public abstract void write(char[] buf,
                           int offset,
                           int len)
                    throws IOException
```

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -

### write

```java
public void write(char[] buf)
           throws IOException
```

**Parameters:**
- `buf` - 출력할 문자배열.

**Throws:**
- `IOException` -

### write

```java
public void write(int b)
           throws IOException
```

**Parameters:**
- `b` - 출력할 문자.

**Throws:**
- `IOException` -

### write

```java
public void write(String str)
           throws IOException
```

**Parameters:**
- `str` - 출력할 문자열.

**Throws:**
- `IOException` -

### write

```java
public void write(String str,
                  int offset,
                  int len)
           throws IOException
```

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -## 메서드 상세

### close

```java
public abstract void close()
                    throws IOException
```

**Throws:**
- `IOException` -

### flush

```java
public abstract void flush()
                    throws IOException
```

**Throws:**
- `IOException` -

### write

```java
public abstract void write(char[] buf,
                           int offset,
                           int len)
                    throws IOException
```

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -

### write

```java
public void write(char[] buf)
           throws IOException
```

**Parameters:**
- `buf` - 출력할 문자배열.

**Throws:**
- `IOException` -

### write

```java
public void write(int b)
           throws IOException
```

**Parameters:**
- `b` - 출력할 문자.

**Throws:**
- `IOException` -

### write

```java
public void write(String str)
           throws IOException
```

**Parameters:**
- `str` - 출력할 문자열.

**Throws:**
- `IOException` -

### write

```java
public void write(String str,
                  int offset,
                  int len)
           throws IOException
```

**Parameters:**
- `len` - 출력할 문자 갯수.

**Throws:**
- `IOException` -

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
