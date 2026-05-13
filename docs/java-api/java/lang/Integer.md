# Class Integer

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Integer
```

## 설명

**extends Object:**

Primitive 타입인 Int 타입을 지원하기 위한 Wrap 클래스.

## 필드 요약

- `static int MAX_VALUE` — Interger의 최대값.
- `static int MIN_VALUE` — Interger의 최소값.

## 생성자 요약

- Integer (int value) Interger 객체를 생성한다.

## 메서드 요약

- `byte byteValue ()` — 현 객체의 값을 Byte형으로 구한다.
- `double doubleValue ()`
- `boolean equals ( Object obj)` — 현 객체와 매개변수로 전달된 객체 값이 일치함을 검사한다.
- `float floatValue ()`
- `int hashCode ()` — 현 객체의 해쉬코드 값을 구한다.
- `int intValue ()` — 현 객체의 값을 Int형으로 구한다.
- `long longValue ()` — 현 객체의 값을 Long형으로 구한다.
- `static int parseInt ( String s)` — 주어진 문자열을 10진법에 의해 Int형으로 변환한다.
- `static int parseInt ( String s, int radix)` — 주어진 문자열을 특정 진법에 의해 Int형으로 변환한다.
- `short shortValue ()` — 현 객체의 값을 Short형으로 구한다.
- `static String toBinaryString (int i)` — 정수형 매개변수를 이진수 문자열로 변환한다.
- `static String toHexString (int i)` — 정수형 매개변수를 16진수 문자열로 변환한다.
- `static String toOctalString (int i)` — 정수형 매개변수를 8진수 문자열로 변환한다.
- `String toString ()` — 현 객체값을 나타내는 문자열을 구한다.
- `static String toString (int i)` — 정수형 매개변수를 10진수 문자열로 변환한다.
- `static String toString (int i, int radix)` — 정수형 매개변수를 특정 진수 문자열로 변환한다.
- `static Integer valueOf ( String s)` — 주어진 문자열을 10진법 변환을 사용해 정수값을 구한다.
- `static Integer valueOf ( String s, int radix)` — 주어진 문자열을 특정 진법 변환을 사용해 정수값을 구한다.

## 필드 상세

### MIN_VALUE

```java
public static final int MIN_VALUE
```

- Interger의 최소값.

### MAX_VALUE

```java
public static final int MAX_VALUE
```

- Interger의 최대값.

### Integer

```java
public Integer(int value)
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

### byteValue

```java
public byte byteValue()
```

**Returns:**
- Byte형으로 변환된 현 객체의 값.

### shortValue

```java
public short shortValue()
```

**Returns:**
- Short형으로 변환된 현 객체의 값.

### intValue

```java
public int intValue()
```

**Returns:**
- Int형으로 변환된 현 객체의 값.

### longValue

```java
public long longValue()
```

**Returns:**
- Long형으로 변환된 현 객체의 값.

### floatValue

```java
public float floatValue()
```

### doubleValue

```java
public double doubleValue()
```

### parseInt

```java
public static int parseInt(String s)
                    throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 문자열이 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### parseInt

```java
public static int parseInt(String s,
                           int radix)
                    throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- 문자열이 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### toBinaryString

```java
public static String toBinaryString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 이진수 문자열.

### toHexString

```java
public static String toHexString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 16진수 문자열.

### toOctalString

```java
public static String toOctalString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 8진수 문자열.

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
public static String toString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 10진수 문자열.

### toString

```java
public static String toString(int i,
                              int radix)
```

**Parameters:**
- `redix` - 변환 진법.

**Returns:**
- i가 변환된 radix진수 문자열.

### valueOf

```java
public static Integer valueOf(String s)
                       throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- s가 10진법으로 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### valueOf

```java
public static Integer valueOf(String s,
                              int radix)
                       throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- s가 radix진법으로 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.## 생성자 상세

### Integer

```java
public Integer(int value)
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

### byteValue

```java
public byte byteValue()
```

**Returns:**
- Byte형으로 변환된 현 객체의 값.

### shortValue

```java
public short shortValue()
```

**Returns:**
- Short형으로 변환된 현 객체의 값.

### intValue

```java
public int intValue()
```

**Returns:**
- Int형으로 변환된 현 객체의 값.

### longValue

```java
public long longValue()
```

**Returns:**
- Long형으로 변환된 현 객체의 값.

### floatValue

```java
public float floatValue()
```

### doubleValue

```java
public double doubleValue()
```

### parseInt

```java
public static int parseInt(String s)
                    throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 문자열이 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### parseInt

```java
public static int parseInt(String s,
                           int radix)
                    throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- 문자열이 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### toBinaryString

```java
public static String toBinaryString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 이진수 문자열.

### toHexString

```java
public static String toHexString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 16진수 문자열.

### toOctalString

```java
public static String toOctalString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 8진수 문자열.

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
public static String toString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 10진수 문자열.

### toString

```java
public static String toString(int i,
                              int radix)
```

**Parameters:**
- `redix` - 변환 진법.

**Returns:**
- i가 변환된 radix진수 문자열.

### valueOf

```java
public static Integer valueOf(String s)
                       throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- s가 10진법으로 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### valueOf

```java
public static Integer valueOf(String s,
                              int radix)
                       throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- s가 radix진법으로 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.## 메서드 상세

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

### byteValue

```java
public byte byteValue()
```

**Returns:**
- Byte형으로 변환된 현 객체의 값.

### shortValue

```java
public short shortValue()
```

**Returns:**
- Short형으로 변환된 현 객체의 값.

### intValue

```java
public int intValue()
```

**Returns:**
- Int형으로 변환된 현 객체의 값.

### longValue

```java
public long longValue()
```

**Returns:**
- Long형으로 변환된 현 객체의 값.

### floatValue

```java
public float floatValue()
```

### doubleValue

```java
public double doubleValue()
```

### parseInt

```java
public static int parseInt(String s)
                    throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 문자열이 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### parseInt

```java
public static int parseInt(String s,
                           int radix)
                    throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- 문자열이 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### toBinaryString

```java
public static String toBinaryString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 이진수 문자열.

### toHexString

```java
public static String toHexString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 16진수 문자열.

### toOctalString

```java
public static String toOctalString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 8진수 문자열.

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
public static String toString(int i)
```

**Parameters:**
- `i` - 변환할 정수.

**Returns:**
- i가 변환된 10진수 문자열.

### toString

```java
public static String toString(int i,
                              int radix)
```

**Parameters:**
- `redix` - 변환 진법.

**Returns:**
- i가 변환된 radix진수 문자열.

### valueOf

```java
public static Integer valueOf(String s)
                       throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- s가 10진법으로 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

### valueOf

```java
public static Integer valueOf(String s,
                              int radix)
                       throws NumberFormatException
```

**Parameters:**
- `radix` - 변환 진법.

**Returns:**
- s가 radix진법으로 변환된 정수값.

**Throws:**
- `NumberFormatException` - 문자열이 변환될 수 없울 때 발생.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
