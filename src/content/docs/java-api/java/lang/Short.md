---
title: "Class Short"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Short
```

## 설명

**extends Object:**

Primitive 타입인 Short 타입을 지원하기 위한 Wrap 클래스.

## 필드 요약

- `static short MAX_VALUE` — short타입의 최대값.
- `static short MIN_VALUE` — short타입의 최소값.

## 생성자 요약

- Short (short value) Short 객체를 생성한다.

## 메서드 요약

- `boolean equals ( Object obj)` — 현 객체와 매개변수로 전달된 객체 값이 일치함을 검사한다.
- `int hashCode ()` — 현 객체의 해쉬코드 값을 구한다.
- `static short parseShort ( String s)` — 주어진 문자열을 10진법에 의해 Short형으로 변환한다.
- `static short parseShort ( String s, int radix)` — 주어진 문자열을 특정 진법에 의해 Short형으로 변환한다.
- `short shortValue ()` — 현 객체의 값을 구한다.
- `String toString ()` — 현 객체값을 나타내는 문자열을 구한다.

## 필드 상세

### MIN_VALUE

```java
public static final short MIN_VALUE
```

- short타입의 최소값.

### MAX_VALUE

```java
public static final short MAX_VALUE
```

- short타입의 최대값.

### Short

```java
public Short(short value)
```

**Parameters:**
- `value` - 초기값.

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `obj` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 현 객체의 정수형 해쉬코드.

### parseShort

```java
public static short parseShort(String s)
                        throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 문자열이 변환된 Short값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### parseShort

```java
public static short parseShort(String s,
                               int radix)
                        throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- 문자열이 변환된 Short값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### shortValue

```java
public short shortValue()
```

**Returns:**
- Short타입인 현 객체 값.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체값을 10진수로 변환한 문자열.## 생성자 상세

### Short

```java
public Short(short value)
```

**Parameters:**
- `value` - 초기값.

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `obj` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 현 객체의 정수형 해쉬코드.

### parseShort

```java
public static short parseShort(String s)
                        throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 문자열이 변환된 Short값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### parseShort

```java
public static short parseShort(String s,
                               int radix)
                        throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- 문자열이 변환된 Short값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### shortValue

```java
public short shortValue()
```

**Returns:**
- Short타입인 현 객체 값.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체값을 10진수로 변환한 문자열.## 메서드 상세

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `obj` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 현 객체의 정수형 해쉬코드.

### parseShort

```java
public static short parseShort(String s)
                        throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 문자열이 변환된 Short값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### parseShort

```java
public static short parseShort(String s,
                               int radix)
                        throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- 문자열이 변환된 Short값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### shortValue

```java
public short shortValue()
```

**Returns:**
- Short타입인 현 객체 값.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체값을 10진수로 변환한 문자열.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
