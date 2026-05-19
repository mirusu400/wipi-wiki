---
title: "Class String"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.String
```

## 설명

**extends Object:**

문자열을 지원하는 클래스.

## 생성자 요약

- String () 길이가 0인 문자열을 생성한다.
- String (byte[] bytes) 바이트 배열 전체를 유니코드 문자로 변환 후 새로운 문자열을 
 만든다.
- String (byte[] bytes,
 int off,
 int len) 바이트 배열 중 일부분을 유니코드 문자로 변환 후 새로운 문자열을 
 만든다.
- String (byte[] bytes,
 int off,
 int len, String enc) 바이트 배열 중 일부분을 특정 디코딩 방식을 통해 유니코드 문자로 변환 후 
 새로운 문자열을 만든다.
- String (byte[] bytes, String enc) 바이트 배열 전체를 특정 디코딩 방식을 통해 유니코드 문자로 변환 후 
 새로운 문자열을 만든다.
- String (char[] value) 문자 배열을 가지고 문자열을 만든다.
- String (char[] value,
 int offset,
 int count) 문자열의 일부를 복사해 새로운 문자열을 만든다.
- String ( String value) 문자열을 복사해 새로운 문자열을 만든다.
- String ( StringBuffer buffer) StringBuffer에 저장된 값들을 사용해 새로운 문자열을 만든다.

## 메서드 요약

- `char charAt (int index)` — 현 문자열 중 index에 해당하는 문자를 구한다.
- `int compareTo ( String anotherString)` — 현 문자열과 다른 문자열을 비교한다.
- `String concat ( String str)` — 현 문자열에 특정 문자열을 덧붙여 새로운 문자열을 만든다.
- `boolean endsWith ( String suffix)` — 현 문자열이 특정 문자열로 끝나는지 여부를 구한다.
- `boolean equals ( Object anObject)` — 현 객체와 매개변수로 전달된 객체 값이 일치함을 검사한다.
- `boolean equalsIgnoreCase ( String anotherString)` — 현 객체와 매개변수로 전달된 객체 값이 일치함을 검사한다.단 대소문자 구별을 하지 안는다.
- `byte[] getBytes ()` — 현 문자열을 유니코드에서 byte배열로 변환시킨다.
- `byte[] getBytes ( String enc)` — 현 문자열을 특정 인코딩 방식을 사용해 유니코드에서 byte배열로 변환시킨다.
- `void getChars (int srcBegin, int srcEnd, char[] dst, int dstBegin)` — 문자열의 일부분을 문자 배열로 복사한다.
- `int hashCode ()` — 현 문자열의 해쉬코드 값을 구한다.
- `int indexOf (int ch)` — 현 문자열에서 특정 문자의 첫번째 위치를 구한다.
- `int indexOf (int ch, int fromIndex)` — 현 문자열의 특정 위치 이후 특정 문자의 첫번째 위치를 구한다.
- `int indexOf ( String str)` — 현 문자열에서 특정 문자열의 첫번째 위치를 구한다.
- `int indexOf ( String str, int fromIndex)` — 현 문자열의 특정 위치 이후 특정 문자열의 첫번째 위치를 구한다.
- `int lastIndexOf (int ch)` — 현 문자열에서 특정 문자의 마지막 위치를 구한다.
- `int lastIndexOf (int ch, int fromIndex)` — 현 문자열의 특정 위치까지 특정 문자의 마지막 위치를 구한다.
- `int length ()` — 현 문자열의 길이를 구한다.
- `boolean regionMatches (boolean ignoreCase, int toffset, String other, int ooffset, int len)` — 현 문자열의 일부와 다른 문자열의 일부를 비교해 동일한지 여부를 구한다.
- `String replace (char oldChar, char newChar)` — 현 문자열에서 특정 문자를 모두 다른 문자로 대체한 새로운 문자열을 만든다.
- `boolean startsWith ( String prefix)` — 현 문자열이 특정 문자열로 시작하는지 여부를 구한다.
- `boolean startsWith ( String prefix, int toffset)` — 현 문자열 특정 위치에 특정 문자열이 존재하는 지 여부를 구한다.
- `String substring (int beginIndex)` — 현 문자열 중 일부분을 사용해서 새로운 문자열을 생성한다.
- `String substring (int beginIndex, int endIndex)` — 현 문자열 중 일부분을 사용해서 새로운 문자열을 생성한다.
- `char[] toCharArray ()` — 현 문자열을 사용해 새로운 문자 배열을 만든다.
- `String toLowerCase ()` — 현 문자열의 대문자를 모두 소문자로 바꾼 새로운 문자열을 만든다.
- `String toString ()` — 자기 자신이 문자열이므로 자기자신을 리턴한다.
- `String toUpperCase ()` — 현 문자열의 소문자를 모두 대문자로 바꾼 새로운 문자열을 만든다.
- `String trim ()` — 현 문자열의 시작과 끝에 있는 공백문자를 모두 제거한 새로운 문자열을 만든다.
- `static String valueOf (boolean b)` — boolean객체를 설명하는 문자열을 구한다.
- `static String valueOf (char c)` — 문자열 길이가 1인 새로운 문자열을 만든다.
- `static String valueOf (char[] data)` — 문자 배열을 사용해서 새로운 문자열을 만든다.
- `static String valueOf (char[] data, int offset, int count)` — 문자 배열 일부분을 사용해서 새로운 문자열을 만든다.
- `static String valueOf (double d)`
- `static String valueOf (float f)`
- `static String valueOf (int i)` — 정수 값을 10진법으로 표현한 새로운 문자열을 만든다.
- `static String valueOf (long l)` — Long 값을 10진법으로 표현한 새로운 문자열을 만든다.
- `static String valueOf ( Object obj)` — 매개변수 객체를 설명하는 문자열을 구한다.

## 생성자 상세

### String

```java
public String()
```

- 길이가 0인 문자열을 생성한다.

### String

```java
public String(byte[] bytes)
```

**Parameters:**
- `bytes` - 문자열을 만들 바이트 배열.

### String

```java
public String(byte[] bytes,
              int off,
              int len)
```

**Parameters:**
- `len` - bytes배열에서 변환할 byte갯수.

### String

```java
public String(char[] value)
```

**Parameters:**
- `value` - 문자열을 만든 문자 배열.

### String

```java
public String(String value)
```

**Parameters:**
- `value` - 복사할 문자열.

### String

```java
public String(char[] value,
              int offset,
              int count)
```

**Parameters:**
- `count` - 복사할 길이.

### String

```java
public String(byte[] bytes,
              String enc)
       throws UnsupportedEncodingException
```

**Parameters:**
- `bytes` - 문자열을 만들 바이트 배열.

### String

```java
public String(byte[] bytes,
              int off,
              int len,
              String enc)
       throws UnsupportedEncodingException
```

**Parameters:**
- `len` - bytes배열에서 변환할 byte갯수.

### String

```java
public String(StringBuffer buffer)
```

**Parameters:**
- `buffer` - 문자열 생성에 사용할 StringBuffer.

### length

```java
public int length()
```

**Returns:**
- 문자열의 길이.

### charAt

```java
public char charAt(int index)
```

**Parameters:**
- `index` - 구하고자 하는 문자 인덱스.

**Returns:**
- index에 해당하는 문자.

### getChars

```java
public void getChars(int srcBegin,
                     int srcEnd,
                     char[] dst,
                     int dstBegin)
```

**Parameters:**
- `dstBegin` - 문자 배열dst에서 저장이 시작될 인덱스.

### getBytes

```java
public byte[] getBytes(String enc)
                throws UnsupportedEncodingException,
                       IOException
```

**Parameters:**
- `enc` - 인코딩방식.

**Returns:**
- 인코딩된 Byte배열.

**Throws:**
- `UnsupportedEncodingException` - enc에 해당하는 인코더가 없을 때 발생.

### getBytes

```java
public byte[] getBytes()
```

**Returns:**
- 인코딩된 Byte배열.

### equals

```java
public boolean equals(Object anObject)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `anObject` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### equalsIgnoreCase

```java
public boolean equalsIgnoreCase(String anotherString)
```

**Parameters:**
- `anotherString` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### compareTo

```java
public int  - enc
```

## 메서드 상세

### length

```java
public int length()
```

**Returns:**
- 문자열의 길이.

### charAt

```java
public char charAt(int index)
```

**Parameters:**
- `index` - 구하고자 하는 문자 인덱스.

**Returns:**
- index에 해당하는 문자.

### getChars

```java
public void getChars(int srcBegin,
                     int srcEnd,
                     char[] dst,
                     int dstBegin)
```

**Parameters:**
- `dstBegin` - 문자 배열dst에서 저장이 시작될 인덱스.

### getBytes

```java
public byte[] getBytes(String enc)
                throws UnsupportedEncodingException,
                       IOException
```

**Parameters:**
- `enc` - 인코딩방식.

**Returns:**
- 인코딩된 Byte배열.

**Throws:**
- `UnsupportedEncodingException` - enc에 해당하는 인코더가 없을 때 발생.

### getBytes

```java
public byte[] getBytes()
```

**Returns:**
- 인코딩된 Byte배열.

### equals

```java
public boolean equals(Object anObject)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `anObject` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### equalsIgnoreCase

```java
public boolean equalsIgnoreCase(String anotherString)
```

**Parameters:**
- `anotherString` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### compareTo

```java
public int  - enc
```
