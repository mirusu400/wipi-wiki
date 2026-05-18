# Class Long

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Long
```

## 설명

**extends Object:**

Primitive 타입인 Long 타입을 지원하기 위한 Wrap 클래스.

## 필드 요약

- `static long MAX_VALUE` — Long타입의 최대값.
- `static long MIN_VALUE` — Long타입의 최소값.

## 생성자 요약

- Long (long value) Long 객체를 생성한다.

## 메서드 요약

- `double doubleValue ()`
- `boolean equals ( Object obj)` — 현 객체와 매개변수로 전달된 객체 값이 일치함을 검사한다.
- `float floatValue ()`
- `int hashCode ()` — 현 객체의 해쉬코드 값을 구한다.
- `long longValue ()` — 현 객체의 값을 구한다.
- `static long parseLong ( String s)` — 주어진 문자열을 10진법에 의해 Long형으로 변환한다.
- `static long parseLong ( String s, int radix)` — 주어진 문자열을 특정 진법에 의해 Long형으로 변환한다.
- `String toString ()` — 현 객체값을 나타내는 문자열을 구한다.
- `static String toString (long i)` — Long형 매개변수를 10진수 문자열로 변환한다.
- `static String toString (long i, int radix)` — Long형 매개변수를 특정 진수 문자열로 변환한다.

## 필드 상세

### MIN_VALUE

```java
public static final long MIN_VALUE
```

- Long타입의 최소값.

### MAX_VALUE

```java
public static final long MAX_VALUE
```

- Long타입의 최대값.

### Long

```java
public Long(long value)
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

### longValue

```java
public long longValue()
```

**Returns:**
- Long타입인 현 객체 값.

### floatValue

```java
public float floatValue()
```

### doubleValue

```java
public double doubleValue()
```

### parseLong

```java
public static long parseLong(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 문자열이 변환된 Long값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### parseLong

```java
public static long parseLong(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- 문자열이 변환된 Long값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### toString

```java
public static String toString(long i)
```

**Parameters:**
- `i` - 변환할 Long타입 값.

**Returns:**
- i가 변환된 10진수 문자열.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체값을 10진수로 변환한 문자열.

### toString

```java
public static String toString(long i,
                              int radix)
```

**Parameters:**
- `redix` - 변환 진법.

**Returns:**
- i가 변환된 radix진수 문자열.## 생성자 상세

### Long

```java
public Long(long value)
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

### longValue

```java
public long longValue()
```

**Returns:**
- Long타입인 현 객체 값.

### floatValue

```java
public float floatValue()
```

### doubleValue

```java
public double doubleValue()
```

### parseLong

```java
public static long parseLong(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 문자열이 변환된 Long값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### parseLong

```java
public static long parseLong(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- 문자열이 변환된 Long값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### toString

```java
public static String toString(long i)
```

**Parameters:**
- `i` - 변환할 Long타입 값.

**Returns:**
- i가 변환된 10진수 문자열.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체값을 10진수로 변환한 문자열.

### toString

```java
public static String toString(long i,
                              int radix)
```

**Parameters:**
- `redix` - 변환 진법.

**Returns:**
- i가 변환된 radix진수 문자열.## 메서드 상세

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

### longValue

```java
public long longValue()
```

**Returns:**
- Long타입인 현 객체 값.

### floatValue

```java
public float floatValue()
```

### doubleValue

```java
public double doubleValue()
```

### parseLong

```java
public static long parseLong(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 문자열이 변환된 Long값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### parseLong

```java
public static long parseLong(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- 문자열이 변환된 Long값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### toString

```java
public static String toString(long i)
```

**Parameters:**
- `i` - 변환할 Long타입 값.

**Returns:**
- i가 변환된 10진수 문자열.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체값을 10진수로 변환한 문자열.

### toString

```java
public static String toString(long i,
                              int radix)
```

**Parameters:**
- `redix` - 변환 진법.

**Returns:**
- i가 변환된 radix진수 문자열.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
