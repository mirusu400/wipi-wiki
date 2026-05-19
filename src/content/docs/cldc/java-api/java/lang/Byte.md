---
title: "Class Byte"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Byte
```

## 설명

**extends Object:**

Byte 클래스는 바이트 값의 표준 래퍼입니다.

**Since:**
- JDK1.1, CLDC 1.0

## 필드 요약

- `static byte MAX_VALUE` — Byte가 가질 수 있는 최대값
- `static byte MIN_VALUE` — Byte가 가질 수 있는 최소값

## 생성자 요약

- Byte (byte value) 지정된 바이트 값으로 초기화되는 Byte 객체를 구성합니다.

## 메서드 요약

- `byte byteValue ()` — 이 Byte 값을 바이트로 반환합니다.
- `boolean equals ( Object obj)` — 이 객체를 지정된 객체와 비교합니다.
- `int hashCode ()` — 이 Byte의 해시 코드를 반환합니다.
- `static byte parseByte ( String s)` — 지정된 문자열이 한 바이트를 나타내는 경우 해당 바이트의 값을 반환합니다.
- `static byte parseByte ( String s, int radix)` — 지정된 문자열이 한 바이트를 나타내는 경우 해당 바이트의 값을 반환합니다.
- `String toString ()` — 이 Byte의 값을 나타내는 문자열 객체를 반환합니다.

## 필드 상세

### MIN_VALUE

```java
public static final byte MIN_VALUE
```

**See Also:**
- `Constant Field Values`

### MAX_VALUE

```java
public static final byte MAX_VALUE
```

**See Also:**
- `Constant Field Values`

### Byte

```java
public Byte(byte value)
```

- 지정된 바이트 값으로 초기화되는 Byte 객체를 구성합니다.

**Parameters:**
- `value` - Byte의 초기값

### parseByte

```java
public static byte parseByte(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 해당 바이트를 포함하는 문자열

**Returns:**
- 구문 분석된 바이트 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 바이트가 없는 경우

### parseByte

```java
public static byte parseByte(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 사용되는 기수

**Returns:**
- 구문 분석된 바이트 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 정수가 없는 경우

### byteValue

```java
public byte byteValue()
```

**Returns:**
- 이 Byte 값(바이트)

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 객체의 문자열 표현

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 이 객체의 해시 코드 값

**See Also:**
- ``Object.equals(java.lang.Object)``, 
``Hashtable``

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `obj` - 비교할 객체

**Returns:**
- 두 객체가 동일하면 true, 다르면 false

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

## 생성자 상세

### Byte

```java
public Byte(byte value)
```

- 지정된 바이트 값으로 초기화되는 Byte 객체를 구성합니다.

**Parameters:**
- `value` - Byte의 초기값

### parseByte

```java
public static byte parseByte(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 해당 바이트를 포함하는 문자열

**Returns:**
- 구문 분석된 바이트 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 바이트가 없는 경우

### parseByte

```java
public static byte parseByte(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 사용되는 기수

**Returns:**
- 구문 분석된 바이트 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 정수가 없는 경우

### byteValue

```java
public byte byteValue()
```

**Returns:**
- 이 Byte 값(바이트)

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 객체의 문자열 표현

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 이 객체의 해시 코드 값

**See Also:**
- ``Object.equals(java.lang.Object)``, 
``Hashtable``

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `obj` - 비교할 객체

**Returns:**
- 두 객체가 동일하면 true, 다르면 false

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

## 메서드 상세

### parseByte

```java
public static byte parseByte(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 해당 바이트를 포함하는 문자열

**Returns:**
- 구문 분석된 바이트 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 바이트가 없는 경우

### parseByte

```java
public static byte parseByte(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 사용되는 기수

**Returns:**
- 구문 분석된 바이트 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 정수가 없는 경우

### byteValue

```java
public byte byteValue()
```

**Returns:**
- 이 Byte 값(바이트)

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 객체의 문자열 표현

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 이 객체의 해시 코드 값

**See Also:**
- ``Object.equals(java.lang.Object)``, 
``Hashtable``

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `obj` - 비교할 객체

**Returns:**
- 두 객체가 동일하면 true, 다르면 false

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``
