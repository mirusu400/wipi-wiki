---
title: "Class Integer"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Integer
```

## 설명

**extends Object:**

Integer 클래스는 프리미티브 유형의 `int` 값을 
객체에 포함합니다. `Integer` 유형의 객체에는 유형이 
`int`인 단일 필드가 있습니다.

또한, 이 클래스는 `int`를 
`String`으로, 
`String`을 `int`로 변환하는 여러 메소드와, 
`int`을 처리하는 데 유용한 
다른 상수와 메소드를 제공합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 필드 요약

- `static int MAX_VALUE` — int 유형의 최대값.
- `static int MIN_VALUE` — int 유형의 최소값.

## 생성자 요약

- Integer (int value) 프리미티브 int 인자를 나타내는 새로 할당된 Integer 객체를 구성합니다.

## 메서드 요약

- `byte byteValue ()` — 이 정수 값을 바이트로 반환합니다.
- `double doubleValue ()` — 이 정수 값을 double 로 반환합니다.
- `boolean equals ( Object obj)` — 이 객체를 지정된 객체와 비교합니다.
- `float floatValue ()` — 이 정수 값을 float 로 반환합니다.
- `int hashCode ()` — 이 정수의 해시 코드를 반환합니다.
- `int intValue ()` — 이 정수 값을 int로 반환합니다.
- `long longValue ()` — 이 정수 값을 long 으로 반환합니다.
- `static int parseInt ( String s)` — 문자열 인자를 부호 있는 십진 정수로 구문 분석합니다.
- `static int parseInt ( String s, int radix)` — 문자열 인자를 두 번째 인자로 지정된 기수의 부호 있는 정수로 구문 분석합니다.
- `short shortValue ()` — 이 정수 값을 short로 반환합니다.
- `static String toBinaryString (int i)` — 정수 인자의 문자열 표현을 기수 2의 부호 없는 정수로 만듭니다.
- `static String toHexString (int i)` — 정수 인자의 문자열 표현을 기수 16의 부호 없는 정수로 만듭니다.
- `static String toOctalString (int i)` — 정수 인자의 문자열 표현을 기수 8의 부호 없는 정수로 만듭니다.
- `String toString ()` — 이 정수의 값을 나타내는 문자열 객체를 반환합니다.
- `static String toString (int i)` — 지정된 정수를 나타내는 새 문자열 객체를 반환합니다.
- `static String toString (int i, int radix)` — 두 번째 인자로 지정된 기수에 첫 번째 인자의 문자열 표현을 만듭니다.
- `static Integer valueOf ( String s)` — 지정된 문자열 값으로 초기화된 새 정수 객체를 반환합니다.
- `static Integer valueOf ( String s, int radix)` — 지정된 문자열 값으로 초기화된 새 정수 객체를 반환합니다.

## 필드 상세

### MIN_VALUE

```java
public static final int MIN_VALUE
```

**See Also:**
- `Constant Field Values`

### MAX_VALUE

```java
public static final int MAX_VALUE
```

**See Also:**
- `Constant Field Values`

### Integer

```java
public Integer(int value)
```

- 프리미티브 `int` 인자를 나타내는 새로 할당된 
`Integer` 객체를 구성합니다.

**Parameters:**
- `value` - `Integer`가 나타내는 값

### toString

```java
public static String toString(int i,
                              int radix)
```

**Parameters:**
- `radix` - 기수

**Returns:**
- 지정된 기수를 사용한 인자의 문자열 표현

**See Also:**
- ``Character.MAX_RADIX``, 
``Character.MIN_RADIX``

### toHexString

```java
public static String toHexString(int i)
```

**Parameters:**
- `i` - 정수

**Returns:**
- 16진수(기수 16) 인자가 나타내는 
 부호 없는 정수 값의 문자열 표현

**Since:**
- JDK1.0.2

### toOctalString

```java
public static String toOctalString(int i)
```

**Parameters:**
- `i` - 정수

**Returns:**
- 8진수(기수 8) 인자가 나타내는 
 부호 없는 정수 값의 문자열 표현

**Since:**
- JDK1.0.2

### toBinaryString

```java
public static String toBinaryString(int i)
```

**Parameters:**
- `i` - 정수

**Returns:**
- 2진수(기수 2) 인자가 나타내는 
 부호 없는 정수 값의 문자열 표현

**Since:**
- JDK1.0.2

### toString

```java
public static String toString(int i)
```

**Parameters:**
- `i` - 변환되는 정수

**Returns:**
- 기수 10을 사용한 인자의 문자열 표현

### parseInt

```java
public static int parseInt(String s,
                           int radix)
                    throws NumberFormatException
```

**Parameters:**
- `radix` - 사용되는 기수

**Returns:**
- 지정된 기수의 문자열 인자가 
 나타내는 정수

**Throws:**
- `NumberFormatException` - 문자열에 
 구문 분석 가능한 정수가 없는 경우

### parseInt

```java
public static int parseInt(String s)
                    throws NumberFormatException
```

**Parameters:**
- `s` - 문자열

**Returns:**
- 십진수 인자가 나타내는 정수

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 정수가 없는 경우

### valueOf

```java
public static Integer valueOf(String s,
                              int radix)
                       throws NumberFormatException
```

**Parameters:**
- `radix` - 문자열 `s`가 나타내는 
 정수의 기수

**Returns:**
- 지정된 기수의 문자열 인자가 나타내는 값으로 초기화된 
 새로 구성된
 `Integer`

**Throws:**
- `NumberFormatException` - 문자열을
 `int`로 구문 분석할 수 없는 경우

### valueOf

```java
public static Integer valueOf(String s)
                       throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 값으로 초기화된 
 새로 구성된 `Integer`

**Throws:**
- `NumberFormatException` - 문자열을 정수로 
 구문 분석할 수 없는 경우

### byteValue

```java
public byte byteValue()
```

**Returns:**
- 이 정수 값(바이트)

**Since:**
- JDK1.1

### shortValue

```java
public short shortValue()
```

**Returns:**
- 이 정수 값(short)

**Since:**
- JDK1.1

### intValue

```java
public int intValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값이 
 `long` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값이 
 `float` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- CLDC 1.1

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값이 
 `double` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- CLDC 1.1

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 기수 10을 사용한 이 객체 값의 
 문자열 표현

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- `Integer` 객체가 나타내는 
 프리미티브 `int` 값과 같은 
 이 객체의 해시 코드 값

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
- 두 객체가 동일하면 `true`, 
 다르면 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

## 생성자 상세

### Integer

```java
public Integer(int value)
```

- 프리미티브 `int` 인자를 나타내는 새로 할당된 
`Integer` 객체를 구성합니다.

**Parameters:**
- `value` - `Integer`가 나타내는 값

### toString

```java
public static String toString(int i,
                              int radix)
```

**Parameters:**
- `radix` - 기수

**Returns:**
- 지정된 기수를 사용한 인자의 문자열 표현

**See Also:**
- ``Character.MAX_RADIX``, 
``Character.MIN_RADIX``

### toHexString

```java
public static String toHexString(int i)
```

**Parameters:**
- `i` - 정수

**Returns:**
- 16진수(기수 16) 인자가 나타내는 
 부호 없는 정수 값의 문자열 표현

**Since:**
- JDK1.0.2

### toOctalString

```java
public static String toOctalString(int i)
```

**Parameters:**
- `i` - 정수

**Returns:**
- 8진수(기수 8) 인자가 나타내는 
 부호 없는 정수 값의 문자열 표현

**Since:**
- JDK1.0.2

### toBinaryString

```java
public static String toBinaryString(int i)
```

**Parameters:**
- `i` - 정수

**Returns:**
- 2진수(기수 2) 인자가 나타내는 
 부호 없는 정수 값의 문자열 표현

**Since:**
- JDK1.0.2

### toString

```java
public static String toString(int i)
```

**Parameters:**
- `i` - 변환되는 정수

**Returns:**
- 기수 10을 사용한 인자의 문자열 표현

### parseInt

```java
public static int parseInt(String s,
                           int radix)
                    throws NumberFormatException
```

**Parameters:**
- `radix` - 사용되는 기수

**Returns:**
- 지정된 기수의 문자열 인자가 
 나타내는 정수

**Throws:**
- `NumberFormatException` - 문자열에 
 구문 분석 가능한 정수가 없는 경우

### parseInt

```java
public static int parseInt(String s)
                    throws NumberFormatException
```

**Parameters:**
- `s` - 문자열

**Returns:**
- 십진수 인자가 나타내는 정수

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 정수가 없는 경우

### valueOf

```java
public static Integer valueOf(String s,
                              int radix)
                       throws NumberFormatException
```

**Parameters:**
- `radix` - 문자열 `s`가 나타내는 
 정수의 기수

**Returns:**
- 지정된 기수의 문자열 인자가 나타내는 값으로 초기화된 
 새로 구성된
 `Integer`

**Throws:**
- `NumberFormatException` - 문자열을
 `int`로 구문 분석할 수 없는 경우

### valueOf

```java
public static Integer valueOf(String s)
                       throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 값으로 초기화된 
 새로 구성된 `Integer`

**Throws:**
- `NumberFormatException` - 문자열을 정수로 
 구문 분석할 수 없는 경우

### byteValue

```java
public byte byteValue()
```

**Returns:**
- 이 정수 값(바이트)

**Since:**
- JDK1.1

### shortValue

```java
public short shortValue()
```

**Returns:**
- 이 정수 값(short)

**Since:**
- JDK1.1

### intValue

```java
public int intValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값이 
 `long` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값이 
 `float` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- CLDC 1.1

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값이 
 `double` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- CLDC 1.1

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 기수 10을 사용한 이 객체 값의 
 문자열 표현

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- `Integer` 객체가 나타내는 
 프리미티브 `int` 값과 같은 
 이 객체의 해시 코드 값

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
- 두 객체가 동일하면 `true`, 
 다르면 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

## 메서드 상세

### toString

```java
public static String toString(int i,
                              int radix)
```

**Parameters:**
- `radix` - 기수

**Returns:**
- 지정된 기수를 사용한 인자의 문자열 표현

**See Also:**
- ``Character.MAX_RADIX``, 
``Character.MIN_RADIX``

### toHexString

```java
public static String toHexString(int i)
```

**Parameters:**
- `i` - 정수

**Returns:**
- 16진수(기수 16) 인자가 나타내는 
 부호 없는 정수 값의 문자열 표현

**Since:**
- JDK1.0.2

### toOctalString

```java
public static String toOctalString(int i)
```

**Parameters:**
- `i` - 정수

**Returns:**
- 8진수(기수 8) 인자가 나타내는 
 부호 없는 정수 값의 문자열 표현

**Since:**
- JDK1.0.2

### toBinaryString

```java
public static String toBinaryString(int i)
```

**Parameters:**
- `i` - 정수

**Returns:**
- 2진수(기수 2) 인자가 나타내는 
 부호 없는 정수 값의 문자열 표현

**Since:**
- JDK1.0.2

### toString

```java
public static String toString(int i)
```

**Parameters:**
- `i` - 변환되는 정수

**Returns:**
- 기수 10을 사용한 인자의 문자열 표현

### parseInt

```java
public static int parseInt(String s,
                           int radix)
                    throws NumberFormatException
```

**Parameters:**
- `radix` - 사용되는 기수

**Returns:**
- 지정된 기수의 문자열 인자가 
 나타내는 정수

**Throws:**
- `NumberFormatException` - 문자열에 
 구문 분석 가능한 정수가 없는 경우

### parseInt

```java
public static int parseInt(String s)
                    throws NumberFormatException
```

**Parameters:**
- `s` - 문자열

**Returns:**
- 십진수 인자가 나타내는 정수

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 정수가 없는 경우

### valueOf

```java
public static Integer valueOf(String s,
                              int radix)
                       throws NumberFormatException
```

**Parameters:**
- `radix` - 문자열 `s`가 나타내는 
 정수의 기수

**Returns:**
- 지정된 기수의 문자열 인자가 나타내는 값으로 초기화된 
 새로 구성된
 `Integer`

**Throws:**
- `NumberFormatException` - 문자열을
 `int`로 구문 분석할 수 없는 경우

### valueOf

```java
public static Integer valueOf(String s)
                       throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 값으로 초기화된 
 새로 구성된 `Integer`

**Throws:**
- `NumberFormatException` - 문자열을 정수로 
 구문 분석할 수 없는 경우

### byteValue

```java
public byte byteValue()
```

**Returns:**
- 이 정수 값(바이트)

**Since:**
- JDK1.1

### shortValue

```java
public short shortValue()
```

**Returns:**
- 이 정수 값(short)

**Since:**
- JDK1.1

### intValue

```java
public int intValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값이 
 `long` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값이 
 `float` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- CLDC 1.1

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `int` 값이 
 `double` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- CLDC 1.1

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 기수 10을 사용한 이 객체 값의 
 문자열 표현

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- `Integer` 객체가 나타내는 
 프리미티브 `int` 값과 같은 
 이 객체의 해시 코드 값

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
- 두 객체가 동일하면 `true`, 
 다르면 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``
