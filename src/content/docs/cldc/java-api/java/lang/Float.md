---
title: "Class Float"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Float
```

## 설명

**extends Object:**

Float 클래스는 프리미티브 유형의 `float` 값을 객체에 
포함합니다. `Float` 유형의 객체에는 유형이 
`float`인 단일 필드가 있습니다.

또한, 이 클래스는 `float`를 `String`으로, 
`String`을 `float`로 변환하는 
여러 메소드와, `double`을 
처리하는 데 유용한 다른 상수와 메소드를 
제공합니다.

**Since:**
- JDK1.0, CLDC 1.1

## 필드 요약

- `static float MAX_VALUE` — float 유형의 최대 양수 값.
- `static float MIN_VALUE` — float 유형의 최소 양수 값.
- `static float NaN` — float 유형의 NaN (Not-a-Number) 값.
- `static float NEGATIVE_INFINITY` — float 유형의 음의 무한대.
- `static float POSITIVE_INFINITY` — float 유형의 양의 무한대.

## 생성자 요약

- Float (double value) float 유형으로 변환된 인자를 나타내는 
새로 할당된 Float 객체를 구성합니다.
- Float (float value) 프리미티브 float 인자를 나타내는 
새로 할당된 Float 객체를 구성합니다.

## 메서드 요약

- `byte byteValue ()` — 이 Float 값을 바이트로 반환합니다(byte로 캐스트).
- `double doubleValue ()` — 이 Float 객체의 double 값을 반환합니다.
- `boolean equals ( Object obj)` — 이 객체를 다른 객체와 비교합니다.
- `static int floatToIntBits (float value)` — 단일 float 값의 비트 표현을 반환합니다.
- `float floatValue ()` — 이 Float 객체의 float 값을 반환합니다.
- `int hashCode ()` — 이 Float 객체의 해시 코드를 반환합니다.
- `static float intBitsToFloat (int bits)` — 지정된 비트 표현에 해당하는 single-float를 반환합니다.
- `int intValue ()` — 이 Float의 정수 값을 반환합니다(int로 캐스트).
- `boolean isInfinite ()` — 이 Float 값의 크기가 무한히 크면 true를 반환합니다.
- `static boolean isInfinite (float v)` — 지정된 숫자의 크기가 무한히 크면 true를 반환합니다.
- `boolean isNaN ()` — 이 Float 값이 NaN (Not-a-Number)이면 true를 반환합니다.
- `static boolean isNaN (float v)` — 지정된 숫자가 특수 NaN (Not-a-Number) 값이면 true를 반환합니다.
- `long longValue ()` — 이 Float의 long 값을 반환합니다(long으로 캐스트).
- `static float parseFloat ( String s)` — 지정된 String 이 나타내는 값으로 초기화된 새 float를 반환합니다.
- `short shortValue ()` — 이 Float 값을 short로 반환합니다(short로 캐스트).
- `String toString ()` — 이 Float 객체의 String 표현을 반환합니다.
- `static String toString (float f)` — 지정된 float 값의 문자열 표현을 반환합니다.
- `static Float valueOf ( String s)` — 지정된 문자열이 나타내는 부동 소수점 값을 반환합니다.

## 필드 상세

### POSITIVE_INFINITY

```java
public static final float POSITIVE_INFINITY
```

**See Also:**
- `Constant Field Values`

### NEGATIVE_INFINITY

```java
public static final float NEGATIVE_INFINITY
```

**See Also:**
- `Constant Field Values`

### NaN

```java
public static final float NaN
```

**See Also:**
- `Constant Field Values`

### MAX_VALUE

```java
public static final float MAX_VALUE
```

**See Also:**
- `Constant Field Values`

### MIN_VALUE

```java
public static final float MIN_VALUE
```

**See Also:**
- `Constant Field Values`

### Float

```java
public Float(float value)
```

- 프리미티브 `float` 인자를 나타내는 
새로 할당된 `Float` 객체를 구성합니다.

**Parameters:**
- `value` - `Float`가 나타내는 값

### Float

```java
public Float(double value)
```

- `float` 유형으로 변환된 인자를 나타내는 
새로 할당된 `Float` 객체를 구성합니다.

**Parameters:**
- `value` - `Float`가 나타내는 값

### toString

```java
public static String toString(float f)
```

**Parameters:**
- `f` - 변환되는 float

**Returns:**
- 인자의 문자열 표현

### valueOf

```java
public static Float valueOf(String s)
                     throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 
 가능한 정수가 없는 경우

### parseFloat

```java
public static float parseFloat(String s)
                        throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 float 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 float가 없는 경우

**Since:**
- JDK1.2

### isNaN

```java
public static boolean isNaN(float v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자가 NaN이면 `true`, 
 NaN이 아니면 `false`

### isInfinite

```java
public static boolean isInfinite(float v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자가 양의 무한대이거나 음의 무한대이면 
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
- ``toString(float)``

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
- 이 객체가 나타내는 `float` 값이 
 `int` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `float` 값이 
 `long` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `float` 값

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `float` 값이 
 `double` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

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
- `obj` - 비교되는 객체

**Returns:**
- 두 객체가 동일하면 `true`, 다르면 
 `false`

**See Also:**
- ``floatToIntBits(float)``

### floatToIntBits

```java
public static int floatToIntBits(float value)
```

**Parameters:**
- `value` - 부동 소수점 숫자

**Returns:**
- 부동 소수점 숫자를 나타내는 비트

### intBitsToFloat

```java
public static float intBitsToFloat(int bits)
```

**Parameters:**
- `bits` - 정수

**Returns:**
- 동일한 비트 패턴을 가진 단일 형식의 
 부동 소수점 값

## 생성자 상세

### Float

```java
public Float(float value)
```

- 프리미티브 `float` 인자를 나타내는 
새로 할당된 `Float` 객체를 구성합니다.

**Parameters:**
- `value` - `Float`가 나타내는 값

### Float

```java
public Float(double value)
```

- `float` 유형으로 변환된 인자를 나타내는 
새로 할당된 `Float` 객체를 구성합니다.

**Parameters:**
- `value` - `Float`가 나타내는 값

### toString

```java
public static String toString(float f)
```

**Parameters:**
- `f` - 변환되는 float

**Returns:**
- 인자의 문자열 표현

### valueOf

```java
public static Float valueOf(String s)
                     throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 
 가능한 정수가 없는 경우

### parseFloat

```java
public static float parseFloat(String s)
                        throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 float 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 float가 없는 경우

**Since:**
- JDK1.2

### isNaN

```java
public static boolean isNaN(float v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자가 NaN이면 `true`, 
 NaN이 아니면 `false`

### isInfinite

```java
public static boolean isInfinite(float v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자가 양의 무한대이거나 음의 무한대이면 
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
- ``toString(float)``

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
- 이 객체가 나타내는 `float` 값이 
 `int` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `float` 값이 
 `long` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `float` 값

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `float` 값이 
 `double` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

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
- `obj` - 비교되는 객체

**Returns:**
- 두 객체가 동일하면 `true`, 다르면 
 `false`

**See Also:**
- ``floatToIntBits(float)``

### floatToIntBits

```java
public static int floatToIntBits(float value)
```

**Parameters:**
- `value` - 부동 소수점 숫자

**Returns:**
- 부동 소수점 숫자를 나타내는 비트

### intBitsToFloat

```java
public static float intBitsToFloat(int bits)
```

**Parameters:**
- `bits` - 정수

**Returns:**
- 동일한 비트 패턴을 가진 단일 형식의 
 부동 소수점 값

## 메서드 상세

### toString

```java
public static String toString(float f)
```

**Parameters:**
- `f` - 변환되는 float

**Returns:**
- 인자의 문자열 표현

### valueOf

```java
public static Float valueOf(String s)
                     throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 
 가능한 정수가 없는 경우

### parseFloat

```java
public static float parseFloat(String s)
                        throws NumberFormatException
```

**Parameters:**
- `s` - 구문 분석되는 문자열

**Returns:**
- 문자열 인자가 나타내는 float 값

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 float가 없는 경우

**Since:**
- JDK1.2

### isNaN

```java
public static boolean isNaN(float v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자가 NaN이면 `true`, 
 NaN이 아니면 `false`

### isInfinite

```java
public static boolean isInfinite(float v)
```

**Parameters:**
- `v` - 테스트되는 값

**Returns:**
- 인자가 양의 무한대이거나 음의 무한대이면 
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
- ``toString(float)``

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
- 이 객체가 나타내는 `float` 값이 
 `int` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `float` 값이 
 `long` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `float` 값

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `float` 값이 
 `double` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

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
- `obj` - 비교되는 객체

**Returns:**
- 두 객체가 동일하면 `true`, 다르면 
 `false`

**See Also:**
- ``floatToIntBits(float)``

### floatToIntBits

```java
public static int floatToIntBits(float value)
```

**Parameters:**
- `value` - 부동 소수점 숫자

**Returns:**
- 부동 소수점 숫자를 나타내는 비트

### intBitsToFloat

```java
public static float intBitsToFloat(int bits)
```

**Parameters:**
- `bits` - 정수

**Returns:**
- 동일한 비트 패턴을 가진 단일 형식의 
 부동 소수점 값
