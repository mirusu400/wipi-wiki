---
title: "Class Double"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Double
```

## 설명

**extends Object:**

Double 클래스는 프리미티브 유형의 `double` 
값을 객체에 포함합니다. `Double` 유형의 객체에는 
유형이 `double`인 단일 필드가 
있습니다.

또한, 이 클래스는 `double`을 `String`으로, 
`String`을 `double`로 변환하는 
여러 메소드와, `double`을 처리하는 데 
유용한 다른 상수와 메소드를 
제공합니다.

**Since:**
- JDK1.0, CLDC 1.1

## 필드 요약

- `static double MAX_VALUE` — double 유형의 최대 양수 값.
- `static double MIN_VALUE` — double 유형의 최소 양수 값.
- `static double NaN` — double 유형의 NaN (Not-a-Number) 값.
- `static double NEGATIVE_INFINITY` — double 유형의 음의 무한대.
- `static double POSITIVE_INFINITY` — double 유형의 양의 무한대.

## 생성자 요약

- Double (double value) 프리미티브 double 인자를 나타내는 새로 할당된 Double 객체를 구성합니다.

## 메서드 요약

- `byte byteValue ()` — 이 Double 값을 byte로 반환합니다(byte로 캐스트).
- `static long doubleToLongBits (double value)` — IEEE 754 부동 소수점 "double 형식" 비트 레이아웃에 따라 지정된 부동 소수점 값의 표현을 반환합니다.
- `double doubleValue ()` — 이 Double의 double 값을 반환합니다.
- `boolean equals ( Object obj)` — 이 객체를 지정된 객체와 비교합니다.
- `float floatValue ()` — 이 Double의 float 값을 반환합니다.
- `int hashCode ()` — 이 Double 객체의 해시 코드를 반환합니다.
- `int intValue ()` — 이 Double의 정수 값을 반환합니다(int로 캐스트).
- `boolean isInfinite ()` — 이 Double 값의 크기가 무한히 크면 true를 반환합니다.
- `static boolean isInfinite (double v)` — 지정된 숫자의 크기가 무한히 크면 true를 반환합니다.
- `boolean isNaN ()` — 이 Double 값이 특수 NaN (Not-a-Number) 값이면 true를 반환합니다.
- `static boolean isNaN (double v)` — 지정된 숫자가 특수 NaN (Not-a-Number) 값이면 true를 반환합니다.
- `static double longBitsToDouble (long bits)` — 지정된 비트 표현에 해당하는 double-float를 반환합니다.
- `long longValue ()` — 이 Double의 long 값을 반환합니다(long으로 캐스트).
- `static double parseDouble ( String s)` — Double 클래스의 valueOf 메소드와 같이 지정된 String 이 나타내는 값으로 초기화된 새 double을 반환합니다.
- `short shortValue ()` — 이 Double 값을 short로 반환합니다(short로 캐스트).
- `String toString ()` — 이 Double 객체의 String 표현을 반환합니다.
- `static String toString (double d)` — double 인자의 문자열 표현을 만듭니다.
- `static Double valueOf ( String s)` — 지정된 문자열이 나타내는 값으로 초기화된 새 Double 객체를 반환합니다.

## 필드 상세

### POSITIVE_INFINITY

```java
public static final double POSITIVE_INFINITY
```

**See Also:**
- `Constant Field Values`

### NEGATIVE_INFINITY

```java
public static final double NEGATIVE_INFINITY
```

**See Also:**
- `Constant Field Values`

### NaN

```java
public static final double NaN
```

**See Also:**
- `Constant Field Values`

### MAX_VALUE

```java
public static final double MAX_VALUE
```

**See Also:**
- `Constant Field Values`

### MIN_VALUE

```java
public static final double MIN_VALUE
```

- `double` 유형의 최소 양수 값. 
`Double.longBitsToDouble(0x1L)`에서 반환하는 값과 
같습니다.

### Double

```java
public Double(double value)
```

- 프리미티브 `double` 인자를 나타내는 새로 할당된 
`Double` 객체를 구성합니다.

**Parameters:**
- `value` - `Double`이 나타내는 값

### toString

```java
public static String toString(double d)
```

**Parameters:**
- `d` - 변환되는 `double`

**Returns:**
- 인자의 문자열 표현

### valueOf

```java
public static Double valueOf(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 값으로 초기화된 새로 구성된 
 `Double`

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 숫자가 없는 경우

### parseDouble

```java
public static double parseDouble(String s)
                          throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 double 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 double이 
 없는 경우

**Since:**
- JDK1.2

**See Also:**
- ``valueOf(String)``

### isNaN

```java
public static boolean isNaN(double v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자 값이 NaN이면 `true`, 
 NaN이 아니면 `false`

### isInfinite

```java
public static boolean isInfinite(double v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자 값이 양의 무한대이거나 음의 무한대이면 
 `true`, 그렇지 않으면 `false`

### isNaN

```java
public boolean isNaN()
```

**Returns:**
- 이 객체가 나타내는 값이 NaN이면 `true`, 
 NaN이 아니면 `false`

### isInfinite

```java
public boolean isInfinite()
```

**Returns:**
- 이 객체가 나타내는 값이 양의 무한대이거나 
 음의 무한대이면 `true`, 
 그렇지 않으면 `false`

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 객체의 `String` 표현

**See Also:**
- ``toString(double)``

### byteValue

```java
public byte byteValue()
```

**Since:**
- JDK1.1

### shortValue

```java
public short shortValue()
```

**Since:**
- JDK1.1

### intValue

```java
public int intValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값이 
 `int` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값이 
 `long` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값이 
 `float` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- JDK1.0

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 이 객체의 `hash code` 값

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
- 두 객체가 동일하면 `true`, 다르면 
 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

### doubleToLongBits

```java
public static long doubleToLongBits(double value)
```

**Parameters:**
- `value` - 배정도 부동 소수점 숫자

**Returns:**
- 부동 소수점 숫자를 나타내는 비트

### longBitsToDouble

```java
public static double longBitsToDouble(long bits)
```

**Parameters:**
- `bits` - 모든 `long` 정수

**Returns:**
- 동일한 비트 패턴을 가진 `double` 
 부동 소수점 값

## 생성자 상세

### Double

```java
public Double(double value)
```

- 프리미티브 `double` 인자를 나타내는 새로 할당된 
`Double` 객체를 구성합니다.

**Parameters:**
- `value` - `Double`이 나타내는 값

### toString

```java
public static String toString(double d)
```

**Parameters:**
- `d` - 변환되는 `double`

**Returns:**
- 인자의 문자열 표현

### valueOf

```java
public static Double valueOf(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 값으로 초기화된 새로 구성된 
 `Double`

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 숫자가 없는 경우

### parseDouble

```java
public static double parseDouble(String s)
                          throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 double 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 double이 
 없는 경우

**Since:**
- JDK1.2

**See Also:**
- ``valueOf(String)``

### isNaN

```java
public static boolean isNaN(double v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자 값이 NaN이면 `true`, 
 NaN이 아니면 `false`

### isInfinite

```java
public static boolean isInfinite(double v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자 값이 양의 무한대이거나 음의 무한대이면 
 `true`, 그렇지 않으면 `false`

### isNaN

```java
public boolean isNaN()
```

**Returns:**
- 이 객체가 나타내는 값이 NaN이면 `true`, 
 NaN이 아니면 `false`

### isInfinite

```java
public boolean isInfinite()
```

**Returns:**
- 이 객체가 나타내는 값이 양의 무한대이거나 
 음의 무한대이면 `true`, 
 그렇지 않으면 `false`

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 객체의 `String` 표현

**See Also:**
- ``toString(double)``

### byteValue

```java
public byte byteValue()
```

**Since:**
- JDK1.1

### shortValue

```java
public short shortValue()
```

**Since:**
- JDK1.1

### intValue

```java
public int intValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값이 
 `int` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값이 
 `long` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값이 
 `float` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- JDK1.0

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 이 객체의 `hash code` 값

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
- 두 객체가 동일하면 `true`, 다르면 
 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

### doubleToLongBits

```java
public static long doubleToLongBits(double value)
```

**Parameters:**
- `value` - 배정도 부동 소수점 숫자

**Returns:**
- 부동 소수점 숫자를 나타내는 비트

### longBitsToDouble

```java
public static double longBitsToDouble(long bits)
```

**Parameters:**
- `bits` - 모든 `long` 정수

**Returns:**
- 동일한 비트 패턴을 가진 `double` 
 부동 소수점 값

## 메서드 상세

### toString

```java
public static String toString(double d)
```

**Parameters:**
- `d` - 변환되는 `double`

**Returns:**
- 인자의 문자열 표현

### valueOf

```java
public static Double valueOf(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 값으로 초기화된 새로 구성된 
 `Double`

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 숫자가 없는 경우

### parseDouble

```java
public static double parseDouble(String s)
                          throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 double 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 double이 
 없는 경우

**Since:**
- JDK1.2

**See Also:**
- ``valueOf(String)``

### isNaN

```java
public static boolean isNaN(double v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자 값이 NaN이면 `true`, 
 NaN이 아니면 `false`

### isInfinite

```java
public static boolean isInfinite(double v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자 값이 양의 무한대이거나 음의 무한대이면 
 `true`, 그렇지 않으면 `false`

### isNaN

```java
public boolean isNaN()
```

**Returns:**
- 이 객체가 나타내는 값이 NaN이면 `true`, 
 NaN이 아니면 `false`

### isInfinite

```java
public boolean isInfinite()
```

**Returns:**
- 이 객체가 나타내는 값이 양의 무한대이거나 
 음의 무한대이면 `true`, 
 그렇지 않으면 `false`

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 객체의 `String` 표현

**See Also:**
- ``toString(double)``

### byteValue

```java
public byte byteValue()
```

**Since:**
- JDK1.1

### shortValue

```java
public short shortValue()
```

**Since:**
- JDK1.1

### intValue

```java
public int intValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값이 
 `int` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값이 
 `long` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값이 
 `float` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- JDK1.0

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `double` 값

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 이 객체의 `hash code` 값

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
- 두 객체가 동일하면 `true`, 다르면 
 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

### doubleToLongBits

```java
public static long doubleToLongBits(double value)
```

**Parameters:**
- `value` - 배정도 부동 소수점 숫자

**Returns:**
- 부동 소수점 숫자를 나타내는 비트

### longBitsToDouble

```java
public static double longBitsToDouble(long bits)
```

**Parameters:**
- `bits` - 모든 `long` 정수

**Returns:**
- 동일한 비트 패턴을 가진 `double` 
 부동 소수점 값
