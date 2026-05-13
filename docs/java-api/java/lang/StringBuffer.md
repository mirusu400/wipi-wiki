# Class StringBuffer

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.StringBuffer
```

## 설명

**extends Object:**

문자들이 저장될 버퍼와 버퍼에 대한 삽입,확장,제거등에 대한 메소드가 
 정의 된 클래스.

## 생성자 요약

- StringBuffer () 버퍼사이즈가 16바이트인 객체를 생성한다.
- StringBuffer (int length) 특정 크기의 버퍼를 가진 객체를 생성한다.
- StringBuffer ( String str) 특정 문자열 길이+16 크기를 가진 버퍼와 초기값으로 특정 문자열의
 문자 정보를 가진 객체를 생성한다.

## 메서드 요약

- `StringBuffer append (boolean b)` — 문자 버퍼에 boolean변수 값을 끝에 추가한다.
- `StringBuffer append (char c)` — 문자 버퍼에 문자를 끝에 추가한다.
- `StringBuffer append (char[] str)` — 문자 버퍼에 문자 배열을 끝에 추가한다.
- `StringBuffer append (char[] str, int offset, int len)` — 문자 버퍼에 문자 배열 일부분을 끝에 추가한다.
- `StringBuffer append (double dnum)`
- `StringBuffer append (float fnum)`
- `StringBuffer append (int i)` — 문자 버퍼에 특정 정수값을 나타내는 문자열을 끝에 추가한다.
- `StringBuffer append (long l)` — 문자 버퍼에 특정 Long값을 나타내는 문자열을 끝에 추가한다.
- `StringBuffer append ( Object obj)` — 문자 버퍼에 객체를 설명하는 문자열을 끝에 추가한다.
- `StringBuffer append ( String str)` — 문자 버퍼에 특정 문자열을 끝에 추가한다.
- `int capacity ()` — 현재 버퍼 크기를 구한다.
- `char charAt (int index)` — 문자 버퍼 특정위치의 문자를 구한다.
- `StringBuffer delete (int start, int end)` — 문자 버퍼의 일부분을 제거한다.
- `StringBuffer deleteCharAt (int index)` — 문자 버퍼에서 특정 위치 문자를 제거한다.
- `void ensureCapacity (int minimumCapacity)` — 버퍼 크기가 특정 크기 이상이 되도록 한다.
- `void getChars (int srcBegin, int srcEnd, char[] dst, int dstBegin)` — 문자 버퍼의 일부분을 문자 배열로 복사한다.
- `StringBuffer insert (int offset, boolean b)` — 문자 버퍼에 boolean변수 값을 중간에 삽입한다.
- `StringBuffer insert (int offset, char c)` — 문자 버퍼에 문자를 중간에 삽입한다.
- `StringBuffer insert (int offset, char[] str)` — 문자버퍼 중간에 특정 문자 배열을 삽입한다.
- `StringBuffer insert (int offset, double dnum)`
- `StringBuffer insert (int offset, float fnum)`
- `StringBuffer insert (int offset, int i)` — 문자 버퍼에 특정 정수값을 나타내는 문자열을 중간에 추가한다.
- `StringBuffer insert (int offset, long l)` — 문자 버퍼에 특정 Long값을 나타내는 문자열을 끝에 삽입한다.
- `StringBuffer insert (int offset, Object obj)` — 문자버퍼 중간에 특정 객체에 대한 설명 문자열을 삽입한다.
- `StringBuffer insert (int offset, String str)` — 문자버퍼 중간에 특정 문자열을 삽입한다.
- `int length ()` — 현재 버퍼에 저장된 문자 갯수를 구한다.
- `StringBuffer reverse ()` — 문자 버퍼에 저장된 값을 역으로 뒤집는다.
- `void setCharAt (int index, char ch)` — 문자 버퍼의 특정 위치 문자를 다른 문자로 바꾼다.
- `void setLength (int newLength)` — 문자 버퍼를 특정 크기로 만든다.
- `String toString ()` — 현 문자버퍼를 가지고 새 문자열을 만든다.

## 생성자 상세

### StringBuffer

```java
public StringBuffer()
```

- 버퍼사이즈가 16바이트인 객체를 생성한다.

### StringBuffer

```java
public StringBuffer(int length)
```

- 특정 크기의 버퍼를 가진 객체를 생성한다.

### StringBuffer

```java
public StringBuffer(String str)
```

**Parameters:**
- `str` - 문자 버퍼의 초기값.

### length

```java
public int length()
```

**Returns:**
- 저장된 문자 갯수.

### capacity

```java
public int capacity()
```

**Returns:**
- 버퍼 크기.

### ensureCapacity

```java
public void ensureCapacity(int minimumCapacity)
```

**Parameters:**
- `minimumCapacity` - 버퍼의 최소 크기

### setLength

```java
public void setLength(int newLength)
```

**Parameters:**
- `newLength` - 새로운 버퍼 크기.

### charAt

```java
public char charAt(int index)
```

**Parameters:**
- `index` - 구하고자 하는 문자의 위치.

**Returns:**
- 구하는 문자.

### getChars

```java
public void getChars(int srcBegin,
                     int srcEnd,
                     char[] dst,
                     int dstBegin)
```

**Parameters:**
- `dstBegin` - dst내에서 정보가 저장될 시작위치.

### setCharAt

```java
public void setCharAt(int index,
                      char ch)
```

**Parameters:**
- `ch` - 바꿀 문자.

### append

```java
public StringBuffer append(Object obj)
```

**Parameters:**
- `obj` - 문자 버퍼에 설명이 추가될 객체.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(String str)
```

**Parameters:**
- `str` - 문자 버퍼에 추가될 문자열.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(char[] str)
```

**Parameters:**
- `str` - 문자 버퍼에 추가될 문자배열.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(char[] str,
                           int offset,
                           int len)
```

**Parameters:**
- `len` - 추가될 길이.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(boolean b)
```

**Parameters:**
- `b` - 문자 버퍼에 추가될 boolean 변수.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(char c)
```

**Parameters:**
- `b` - 문자 버퍼에 추가될 문자.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(int i)
```

**Parameters:**
- `i` - 문자 버퍼에 추가될 정수값.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(long l)
```

**Parameters:**
- `l` - 문자 버퍼에 추가될 Long값.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(float fnum)
```

### append

```java
public StringBuffer append(double dnum)
```

### delete

```java
public StringBuffer delete(int start,
                           int end)
```

**Parameters:**
- `end` - 제거가 끝나는 위치+1값.

**Returns:**
- 현 문자 버퍼.

### deleteCharAt

```java
public StringBuffer deleteCharAt(int index)
```

**Parameters:**
- `index` - 제거할 위치.

**Returns:**
- 현 문자 버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           Object obj)
```

**Parameters:**
- `obj` - 문자 버퍼에 설명이 삽입될 객체.

**Returns:**
- 현 문자 버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           String str)
```

**Parameters:**
- `str` - 문자 버퍼에 삽입될 문자열.

**Returns:**
- 현 문자 버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           char[] str)
```

**Parameters:**
- `str` - 문자 버퍼에 삽입될 문자 배열.

**Returns:**
- 현 문자 버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           boolean b)
```

**Parameters:**
- `b` - 문자 버퍼에 추가될 boolean 변수.

**Returns:**
- 현 문자버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           char c)
```

**Parameters:**
- `c` - 문자 버퍼에 추가될 문자변수.

**Returns:**
- 현 문자버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           int i)
```

**Parameters:**
- `i` - 문자 버퍼에 삽입될 정수값.

**Returns:**
- 현 문자버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           long l)
```

**Parameters:**
- `l` - 문자 버퍼에 추가될 Long값.

**Returns:**
- 현 문자버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           float fnum)
```

### insert

```java
public StringBuffer insert(int offset,
                           double dnum)
```

### reverse

```java
public StringBuffer reverse()
```

**Returns:**
- 현 문자 버퍼.

### toString

## 메서드 상세

### length

```java
public int length()
```

**Returns:**
- 저장된 문자 갯수.

### capacity

```java
public int capacity()
```

**Returns:**
- 버퍼 크기.

### ensureCapacity

```java
public void ensureCapacity(int minimumCapacity)
```

**Parameters:**
- `minimumCapacity` - 버퍼의 최소 크기

### setLength

```java
public void setLength(int newLength)
```

**Parameters:**
- `newLength` - 새로운 버퍼 크기.

### charAt

```java
public char charAt(int index)
```

**Parameters:**
- `index` - 구하고자 하는 문자의 위치.

**Returns:**
- 구하는 문자.

### getChars

```java
public void getChars(int srcBegin,
                     int srcEnd,
                     char[] dst,
                     int dstBegin)
```

**Parameters:**
- `dstBegin` - dst내에서 정보가 저장될 시작위치.

### setCharAt

```java
public void setCharAt(int index,
                      char ch)
```

**Parameters:**
- `ch` - 바꿀 문자.

### append

```java
public StringBuffer append(Object obj)
```

**Parameters:**
- `obj` - 문자 버퍼에 설명이 추가될 객체.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(String str)
```

**Parameters:**
- `str` - 문자 버퍼에 추가될 문자열.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(char[] str)
```

**Parameters:**
- `str` - 문자 버퍼에 추가될 문자배열.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(char[] str,
                           int offset,
                           int len)
```

**Parameters:**
- `len` - 추가될 길이.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(boolean b)
```

**Parameters:**
- `b` - 문자 버퍼에 추가될 boolean 변수.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(char c)
```

**Parameters:**
- `b` - 문자 버퍼에 추가될 문자.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(int i)
```

**Parameters:**
- `i` - 문자 버퍼에 추가될 정수값.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(long l)
```

**Parameters:**
- `l` - 문자 버퍼에 추가될 Long값.

**Returns:**
- 현 문자버퍼.

### append

```java
public StringBuffer append(float fnum)
```

### append

```java
public StringBuffer append(double dnum)
```

### delete

```java
public StringBuffer delete(int start,
                           int end)
```

**Parameters:**
- `end` - 제거가 끝나는 위치+1값.

**Returns:**
- 현 문자 버퍼.

### deleteCharAt

```java
public StringBuffer deleteCharAt(int index)
```

**Parameters:**
- `index` - 제거할 위치.

**Returns:**
- 현 문자 버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           Object obj)
```

**Parameters:**
- `obj` - 문자 버퍼에 설명이 삽입될 객체.

**Returns:**
- 현 문자 버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           String str)
```

**Parameters:**
- `str` - 문자 버퍼에 삽입될 문자열.

**Returns:**
- 현 문자 버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           char[] str)
```

**Parameters:**
- `str` - 문자 버퍼에 삽입될 문자 배열.

**Returns:**
- 현 문자 버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           boolean b)
```

**Parameters:**
- `b` - 문자 버퍼에 추가될 boolean 변수.

**Returns:**
- 현 문자버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           char c)
```

**Parameters:**
- `c` - 문자 버퍼에 추가될 문자변수.

**Returns:**
- 현 문자버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           int i)
```

**Parameters:**
- `i` - 문자 버퍼에 삽입될 정수값.

**Returns:**
- 현 문자버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           long l)
```

**Parameters:**
- `l` - 문자 버퍼에 추가될 Long값.

**Returns:**
- 현 문자버퍼.

### insert

```java
public StringBuffer insert(int offset,
                           float fnum)
```

### insert

```java
public StringBuffer insert(int offset,
                           double dnum)
```

### reverse

```java
public StringBuffer reverse()
```

**Returns:**
- 현 문자 버퍼.

### toString
