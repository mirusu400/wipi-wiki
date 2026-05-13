# Class Character

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Character
```

## 설명

**extends Object:**

Character 클래스는 프리미티브 유형의 `char` 값을 
객체에 포함합니다. `Character` 유형의 객체에는 
유형이 `char`인 단일 필드가 있습니다.

이 클래스는 문자 유형을 확인하고 문자를 대문자에서 소문자로, 
또는 그 반대로 변환하기 위한 여러 메소드도 
제공합니다.

문자 정보는 유니코드 표준, 버전 3.0을 기반으로 합니다. 
하지만 풋프린트를 줄이기 위해 기본적으로 CLDC의 문자 등록 정보와 
대소문자 변환 작업은 ISO Latin-1 범위의 문자에 대해서만 
사용할 수 있습니다. 필요하면 다른 유니코드 문자 블록도 
지원할 수 있습니다.

**Since:**
- JDK1.0, CLDC 1.0

## 필드 요약

- `static int MAX_RADIX` — 문자열과의 변환에 사용할 수 있는 최대 기수
- `static char MAX_VALUE` — 이 필드의 상수 값은 char 유형의 최대값입니다.
- `static int MIN_RADIX` — 문자열과의 변환에 사용할 수 있는 최소 기수
- `static char MIN_VALUE` — 이 필드의 상수 값은 char 유형의 최소값입니다.

## 생성자 요약

- Character (char value) Character 객체를 구성하고 프리미티브 value 인자를 나타내도록 초기화합니다.

## 메서드 요약

- `char charValue ()` — 이 Character 객체 값을 반환합니다.
- `static int digit (char ch, int radix)` — 문자 ch 의 숫자 값을 지정된 기수로 반환합니다.
- `boolean equals ( Object obj)` — 이 객체를 지정된 객체와 비교합니다.
- `int hashCode ()` — 이 Character의 해시 코드를 반환합니다.
- `static boolean isDigit (char ch)` — 지정된 문자가 숫자인지 확인합니다.
- `static boolean isLowerCase (char ch)` — 지정된 문자가 소문자인지 확인합니다.
- `static boolean isUpperCase (char ch)` — 지정된 문자가 대문자인지 확인합니다.
- `static char toLowerCase (char ch)` — 지정된 문자는 해당 소문자로 매핑됩니다.
- `String toString ()` — 이 문자의 값을 나타내는 문자열 객체를 반환합니다.
- `static char toUpperCase (char ch)` — 문자 인자를 대문자로 변환합니다.

## 필드 상세

### MIN_RADIX

```java
public static final int MIN_RADIX
```

**See Also:**
- ``Integer.toString(int, int)``, 
``Integer.valueOf(java.lang.String)``, 
`Constant Field Values`

### MAX_RADIX

```java
public static final int MAX_RADIX
```

**See Also:**
- ``Integer.toString(int, int)``, 
``Integer.valueOf(java.lang.String)``, 
`Constant Field Values`

### MIN_VALUE

```java
public static final char MIN_VALUE
```

**Since:**
- JDK1.0.2

**See Also:**
- `Constant Field Values`

### MAX_VALUE

```java
public static final char MAX_VALUE
```

**Since:**
- JDK1.0.2

**See Also:**
- `Constant Field Values`

### Character

```java
public Character(char value)
```

- `Character` 객체를 구성하고 프리미티브 
`value` 인자를 나타내도록 초기화합니다.

**Parameters:**
- `value` - 새로운 `Character` 객체 값

### charValue

```java
public char charValue()
```

**Returns:**
- 이 객체가 나타내는 프리미티브 `char` 
 값

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

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 객체의 문자열 표현

### isLowerCase

```java
public static boolean isLowerCase(char ch)
```

**Parameters:**
- `ch` - 테스트되는 문자

**Returns:**
- 문자가 소문자이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### isUpperCase

```java
public static boolean isUpperCase(char ch)
```

**Parameters:**
- `ch` - 테스트되는 문자

**Returns:**
- 문자가 대문자이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- 1.0

**See Also:**
- ``isLowerCase(char)``, 
``toUpperCase(char)``

### isDigit

```java
public static boolean isDigit(char ch)
```

**Parameters:**
- `ch` - 테스트되는 문자

**Returns:**
- 문자가 숫자이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### toLowerCase

```java
public static char toLowerCase(char ch)
```

**Parameters:**
- `ch` - 변환되는 문자

**Returns:**
- 문자에 해당 소문자가 있으면 소문자, 
 없으면 문자 자체

**Since:**
- JDK1.0

**See Also:**
- ``isLowerCase(char)``, 
``isUpperCase(char)``, 
``toUpperCase(char)``

### toUpperCase

```java
public static char toUpperCase(char ch)
```

**Parameters:**
- `ch` - 변환되는 문자

**Returns:**
- 문자에 해당 대문자가 있으면 대문자, 
 없으면 문자 자체

**Since:**
- JDK1.0

**See Also:**
- ``isLowerCase(char)``, 
``isUpperCase(char)``, 
``toLowerCase(char)``

### digit

```java
public static int digit(char ch,
                        int radix)
```

**Parameters:**
- `radix` - 기수

**Returns:**
- 문자가 나타내는 지정된 기수의 
 숫자 값

**Since:**
- JDK1.0

**See Also:**
- ``isDigit(char)``

## 생성자 상세

### Character

```java
public Character(char value)
```

- `Character` 객체를 구성하고 프리미티브 
`value` 인자를 나타내도록 초기화합니다.

**Parameters:**
- `value` - 새로운 `Character` 객체 값

### charValue

```java
public char charValue()
```

**Returns:**
- 이 객체가 나타내는 프리미티브 `char` 
 값

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

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 객체의 문자열 표현

### isLowerCase

```java
public static boolean isLowerCase(char ch)
```

**Parameters:**
- `ch` - 테스트되는 문자

**Returns:**
- 문자가 소문자이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### isUpperCase

```java
public static boolean isUpperCase(char ch)
```

**Parameters:**
- `ch` - 테스트되는 문자

**Returns:**
- 문자가 대문자이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- 1.0

**See Also:**
- ``isLowerCase(char)``, 
``toUpperCase(char)``

### isDigit

```java
public static boolean isDigit(char ch)
```

**Parameters:**
- `ch` - 테스트되는 문자

**Returns:**
- 문자가 숫자이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### toLowerCase

```java
public static char toLowerCase(char ch)
```

**Parameters:**
- `ch` - 변환되는 문자

**Returns:**
- 문자에 해당 소문자가 있으면 소문자, 
 없으면 문자 자체

**Since:**
- JDK1.0

**See Also:**
- ``isLowerCase(char)``, 
``isUpperCase(char)``, 
``toUpperCase(char)``

### toUpperCase

```java
public static char toUpperCase(char ch)
```

**Parameters:**
- `ch` - 변환되는 문자

**Returns:**
- 문자에 해당 대문자가 있으면 대문자, 
 없으면 문자 자체

**Since:**
- JDK1.0

**See Also:**
- ``isLowerCase(char)``, 
``isUpperCase(char)``, 
``toLowerCase(char)``

### digit

```java
public static int digit(char ch,
                        int radix)
```

**Parameters:**
- `radix` - 기수

**Returns:**
- 문자가 나타내는 지정된 기수의 
 숫자 값

**Since:**
- JDK1.0

**See Also:**
- ``isDigit(char)``

## 메서드 상세

### charValue

```java
public char charValue()
```

**Returns:**
- 이 객체가 나타내는 프리미티브 `char` 
 값

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

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 객체의 문자열 표현

### isLowerCase

```java
public static boolean isLowerCase(char ch)
```

**Parameters:**
- `ch` - 테스트되는 문자

**Returns:**
- 문자가 소문자이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### isUpperCase

```java
public static boolean isUpperCase(char ch)
```

**Parameters:**
- `ch` - 테스트되는 문자

**Returns:**
- 문자가 대문자이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- 1.0

**See Also:**
- ``isLowerCase(char)``, 
``toUpperCase(char)``

### isDigit

```java
public static boolean isDigit(char ch)
```

**Parameters:**
- `ch` - 테스트되는 문자

**Returns:**
- 문자가 숫자이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### toLowerCase

```java
public static char toLowerCase(char ch)
```

**Parameters:**
- `ch` - 변환되는 문자

**Returns:**
- 문자에 해당 소문자가 있으면 소문자, 
 없으면 문자 자체

**Since:**
- JDK1.0

**See Also:**
- ``isLowerCase(char)``, 
``isUpperCase(char)``, 
``toUpperCase(char)``

### toUpperCase

```java
public static char toUpperCase(char ch)
```

**Parameters:**
- `ch` - 변환되는 문자

**Returns:**
- 문자에 해당 대문자가 있으면 대문자, 
 없으면 문자 자체

**Since:**
- JDK1.0

**See Also:**
- ``isLowerCase(char)``, 
``isUpperCase(char)``, 
``toLowerCase(char)``

### digit

```java
public static int digit(char ch,
                        int radix)
```

**Parameters:**
- `radix` - 기수

**Returns:**
- 문자가 나타내는 지정된 기수의 
 숫자 값

**Since:**
- JDK1.0

**See Also:**
- ``isDigit(char)``
