# Class ByteArrayOutputStream

`package java.io`

```text
java.lang.Object
  |
  +--java.io.OutputStream
        |
        +--java.io.ByteArrayOutputStream
```

## 설명

**extends OutputStream:**

바이트 형 정보의 출력 스트림을 구현한 클래스.

## 필드 요약

- `protected  byte[] buf` — 출력된 바이트형 정보가 저장되는 크기가 자동증가되는 버퍼.
- `protected  int count` — 출력된 바이트 갯수.

## 생성자 요약

- ByteArrayOutputStream () 디폴트 사이즈 출력버퍼를 가진 객체를 생성한다.
- ByteArrayOutputStream (int size) 출력버퍼 사이즈를 지정해서 객체를 생성한다.

## 메서드 요약

- `void reset ()` — 출력된 값들을 모두 버린다.
- `int size ()` — 출력된 값들의 갯수를 구한다.
- `byte[] toByteArray ()` — 출력된 값들을 새로운 바이트 배열 객체로 구한다.
- `String toString ()` — 출력된 내용을 문자열로 바꾼다.
- `void write (byte[] buffer, int offset, int add)` — 특정 바이트 배열의 일부분을 출력한다.
- `void write (int oneByte)` — 한 바이트 값을 출력한다.

## 필드 상세

### buf

```java
protected byte[] buf
```

- 출력된 바이트형 정보가 저장되는 크기가 자동증가되는 버퍼.

### count

```java
protected int count
```

- 출력된 바이트 갯수.

### ByteArrayOutputStream

```java
public ByteArrayOutputStream()
```

- 디폴트 사이즈 출력버퍼를 가진 객체를 생성한다.

### ByteArrayOutputStream

```java
public ByteArrayOutputStream(int size)
```

**Parameters:**
- `size` - 출력버퍼 사이즈.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 출력된 내용이 담긴 문자열.

### reset

```java
public void reset()
```

- 출력된 값들을 모두 버린다.

### size

```java
public int size()
```

**Returns:**
- 출력된 값들의 갯수.

### toByteArray

```java
public byte[] toByteArray()
```

**Returns:**
- 출력된 값이 복사된 바이트 배열.

### write

```java
public void write(int oneByte)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `oneByte` - 출력할 값.

### write

```java
public void write(byte[] buffer,
                  int offset,
                  int add)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `add` - 출력될 갯수.## 생성자 상세

### ByteArrayOutputStream

```java
public ByteArrayOutputStream()
```

- 디폴트 사이즈 출력버퍼를 가진 객체를 생성한다.

### ByteArrayOutputStream

```java
public ByteArrayOutputStream(int size)
```

**Parameters:**
- `size` - 출력버퍼 사이즈.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 출력된 내용이 담긴 문자열.

### reset

```java
public void reset()
```

- 출력된 값들을 모두 버린다.

### size

```java
public int size()
```

**Returns:**
- 출력된 값들의 갯수.

### toByteArray

```java
public byte[] toByteArray()
```

**Returns:**
- 출력된 값이 복사된 바이트 배열.

### write

```java
public void write(int oneByte)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `oneByte` - 출력할 값.

### write

```java
public void write(byte[] buffer,
                  int offset,
                  int add)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `add` - 출력될 갯수.## 메서드 상세

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 출력된 내용이 담긴 문자열.

### reset

```java
public void reset()
```

- 출력된 값들을 모두 버린다.

### size

```java
public int size()
```

**Returns:**
- 출력된 값들의 갯수.

### toByteArray

```java
public byte[] toByteArray()
```

**Returns:**
- 출력된 값이 복사된 바이트 배열.

### write

```java
public void write(int oneByte)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `oneByte` - 출력할 값.

### write

```java
public void write(byte[] buffer,
                  int offset,
                  int add)
```

**Overrides:**
- `write` in class `OutputStream`

**Parameters:**
- `add` - 출력될 갯수.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
