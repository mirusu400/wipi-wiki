# Class Long

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Long
```

## 설명

**extends Object:**

Long 클래스는 프리미티브 유형의 `long` 값을 
객체에 포함합니다. `Long` 유형의 객체에는 
유형이 `long`인 단일 필드가 있습니다.

또한, 이 클래스는 `long`을 
`String`으로, `String`을 
`long`으로 변환하는 여러 메소드와, `long`을 
처리하는 데 유용한 다른 상수와 
메소드를 제공합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 필드 요약

- `static long MAX_VALUE` — long 유형의 최대값
- `static long MIN_VALUE` — long 유형의 최소값

## 생성자 요약

- Long (long value) 프리미티브 long 인자를 나타내는 새로 할당된 Long 객체를 구성합니다.

## 메서드 요약

- `double doubleValue ()` — 이 Long 값을 double로 반환합니다.
- `boolean equals ( Object obj)` — 이 객체를 지정된 객체와 비교합니다.
- `float floatValue ()` — 이 Long 값을 float로 반환합니다.
- `int hashCode ()` — 이 Long의 해시 코드를 계산합니다.
- `long longValue ()` — 이 Long 값을 long 값으로 반환합니다.
- `static long parseLong ( String s)` — 문자열 인자를 부호 있는 십진수 long 으로 구문 분석합니다.
- `static long parseLong ( String s, int radix)` — 문자열 인자를 두 번째 인자로 지정된 기수의 부호 있는 long 으로 구문 분석합니다.
- `String toString ()` — 이 Long의 값을 나타내는 문자열 객체를 반환합니다.
- `static String toString (long i)` — 지정된 정수를 나타내는 새 문자열 객체를 반환합니다.
- `static String toString (long i, int radix)` — 두 번째 인자로 지정된 기수에 첫 번째 인자의 문자열 표현을 만듭니다.

## 필드 상세

### MIN_VALUE

```java
public static final long MIN_VALUE
```

**See Also:**
- `Constant Field Values`

### MAX_VALUE

```java
public static final long MAX_VALUE
```

**See Also:**
- `Constant Field Values`

### Long

```java
public Long(long value)
```

- 프리미티브 `long` 인자를 나타내는 새로 할당된 
`Long` 객체를 구성합니다.

**Parameters:**
- `value` - `Long` 
 객체가 나타내는 값

### toString

```java
public static String toString(long i,
                              int radix)
```

**Parameters:**
- `radix` - 기수

**Returns:**
- 지정된 기수를 사용한 인자의 문자열 표현

**See Also:**
- ``Character.MAX_RADIX``, 
``Character.MIN_RADIX``

### toString

```java
public static String toString(long i)
```

**Parameters:**
- `i` - 변환되는 `long`

**Returns:**
- 기수 10을 사용한 인자의 문자열 표현

### parseLong

```java
public static long parseLong(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 사용되는 기수

**Returns:**
- 지정된 기수의 문자열 인자가 나타내는 
 `long`

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 정수가 없는 경우

### parseLong

```java
public static long parseLong(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 문자열

**Returns:**
- 십진수 인자가 나타내는 `long`

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 `long`이 없는 경우

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `long` 값

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `long` 값이 
 `float` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- CLDC 1.1

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `long` 값이 
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
- 기수 10을 사용한 인자의 문자열 표현

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
- 두 객체가 동일하면 `true`, 
 다르면 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

## 생성자 상세

### Long

```java
public Long(long value)
```

- 프리미티브 `long` 인자를 나타내는 새로 할당된 
`Long` 객체를 구성합니다.

**Parameters:**
- `value` - `Long` 
 객체가 나타내는 값

### toString

```java
public static String toString(long i,
                              int radix)
```

**Parameters:**
- `radix` - 기수

**Returns:**
- 지정된 기수를 사용한 인자의 문자열 표현

**See Also:**
- ``Character.MAX_RADIX``, 
``Character.MIN_RADIX``

### toString

```java
public static String toString(long i)
```

**Parameters:**
- `i` - 변환되는 `long`

**Returns:**
- 기수 10을 사용한 인자의 문자열 표현

### parseLong

```java
public static long parseLong(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 사용되는 기수

**Returns:**
- 지정된 기수의 문자열 인자가 나타내는 
 `long`

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 정수가 없는 경우

### parseLong

```java
public static long parseLong(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 문자열

**Returns:**
- 십진수 인자가 나타내는 `long`

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 `long`이 없는 경우

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `long` 값

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `long` 값이 
 `float` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- CLDC 1.1

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `long` 값이 
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
- 기수 10을 사용한 인자의 문자열 표현

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
- 두 객체가 동일하면 `true`, 
 다르면 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

## 메서드 상세

### toString

```java
public static String toString(long i,
                              int radix)
```

**Parameters:**
- `radix` - 기수

**Returns:**
- 지정된 기수를 사용한 인자의 문자열 표현

**See Also:**
- ``Character.MAX_RADIX``, 
``Character.MIN_RADIX``

### toString

```java
public static String toString(long i)
```

**Parameters:**
- `i` - 변환되는 `long`

**Returns:**
- 기수 10을 사용한 인자의 문자열 표현

### parseLong

```java
public static long parseLong(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 사용되는 기수

**Returns:**
- 지정된 기수의 문자열 인자가 나타내는 
 `long`

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 정수가 없는 경우

### parseLong

```java
public static long parseLong(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 문자열

**Returns:**
- 십진수 인자가 나타내는 `long`

**Throws:**
- `NumberFormatException` - 문자열에 구문 분석 가능한 
 `long`이 없는 경우

### longValue

```java
public long longValue()
```

**Returns:**
- 이 객체가 나타내는 `long` 값

### floatValue

```java
public float floatValue()
```

**Returns:**
- 이 객체가 나타내는 `long` 값이 
 `float` 유형으로 변환되어 
 그 변환 결과가 반환됩니다.

**Since:**
- CLDC 1.1

### doubleValue

```java
public double doubleValue()
```

**Returns:**
- 이 객체가 나타내는 `long` 값이 
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
- 기수 10을 사용한 인자의 문자열 표현

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
- 두 객체가 동일하면 `true`, 
 다르면 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``
