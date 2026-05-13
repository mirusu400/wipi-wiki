# Class Character

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Character
```

## 설명

**extends Object:**

Primitive 타입인 char 타입을 지원하기 위한 Wrap 클래스.

## 필드 요약

- `static int MAX_RADIX` — 문자열로 변환시 사용할 수 있는 최대 진법 값.
- `static char MAX_VALUE` — char형의 최대값.
- `static int MIN_RADIX` — 문자열로 변환시 사용할 수 있는 최소 진법 값.
- `static char MIN_VALUE` — char형의 최소값.

## 생성자 요약

- Character (char value) Character형 객체를 생성한다.

## 메서드 요약

- `char charValue ()` — 현 객체의 값을 구한다.
- `static int digit (char ch, int radix)` — 주어진 문자를 특정 진법에 의해 정수형으로 바꾼다.
- `boolean equals ( Object o)` — 현 객체와 매개변수로 전달된 객체 값이 일치함을 검사한다.
- `int hashCode ()` — 현 객체의 해쉬코르 값을 구한다.
- `static boolean isDigit (char ch)` — 문자가 숫자인지 여부를 구한다.
- `static boolean isLowerCase (char ch)` — 문자가 소문자인지 여부를 구한다.
- `static boolean isUpperCase (char ch)` — 문자가 대문자인지 여부를 구한다.
- `static char toLowerCase (char ch)` — 주어진 문자를 소문자로 바꾼다.
- `String toString ()` — 현 객체를 나타내는 문자열을 구한다.
- `static char toUpperCase (char ch)` — 주어진 문자를 대문자로 바꾼다.

## 필드 상세

### MIN_VALUE

```java
public static final char MIN_VALUE
```

- char형의 최소값.

### MAX_VALUE

```java
public static final char MAX_VALUE
```

- char형의 최대값.

### MIN_RADIX

```java
public static final int MIN_RADIX
```

**See Also:**
- `java.lang.Character#digiti(char,int)`

### MAX_RADIX

```java
public static final int MAX_RADIX
```

**See Also:**
- `java.lang.Character#digiti(char,int)`

### Character

```java
public Character(char value)
```

**Parameters:**
- `value` - 초기값.

### charValue

```java
public char charValue()
```

**Returns:**
- 현 객체의 값.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 정수형의 해쉬코드값.

### equals

```java
public boolean equals(Object o)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `o` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체 값을 사용해 만든 문자열.

### isLowerCase

```java
public static boolean isLowerCase(char ch)
```

**Parameters:**
- `ch` - 검토할 문자.

**Returns:**
- 소문자이면 true 아니면 false.

### toLowerCase

```java
public static char toLowerCase(char ch)
```

**Parameters:**
- `ch` - 변환할 문자.

**Returns:**
- 소문자로 변환된 문자.

### isUpperCase

```java
public static boolean isUpperCase(char ch)
```

**Parameters:**
- `ch` - 검토할 문자.

**Returns:**
- 대문자이면 true 아니면 false.

### toUpperCase

```java
public static char toUpperCase(char ch)
```

**Parameters:**
- `ch` - 변환할 문자.

**Returns:**
- 대문자로 변환된 문자.

### isDigit

```java
public static boolean isDigit(char ch)
```

**Parameters:**
- `ch` - 검토할 문자.

**Returns:**
- 숫자이면 true 아니면 false.

### digit

```java
public static int digit(char ch,
                        int radix)
```

**Parameters:**
- `radix` - 변환시 사용할 진법.

**Returns:**
- 문자에 해당하는 정수값.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 생성자 상세

### Character

```java
public Character(char value)
```

**Parameters:**
- `value` - 초기값.

### charValue

```java
public char charValue()
```

**Returns:**
- 현 객체의 값.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 정수형의 해쉬코드값.

### equals

```java
public boolean equals(Object o)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `o` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체 값을 사용해 만든 문자열.

### isLowerCase

```java
public static boolean isLowerCase(char ch)
```

**Parameters:**
- `ch` - 검토할 문자.

**Returns:**
- 소문자이면 true 아니면 false.

### toLowerCase

```java
public static char toLowerCase(char ch)
```

**Parameters:**
- `ch` - 변환할 문자.

**Returns:**
- 소문자로 변환된 문자.

### isUpperCase

```java
public static boolean isUpperCase(char ch)
```

**Parameters:**
- `ch` - 검토할 문자.

**Returns:**
- 대문자이면 true 아니면 false.

### toUpperCase

```java
public static char toUpperCase(char ch)
```

**Parameters:**
- `ch` - 변환할 문자.

**Returns:**
- 대문자로 변환된 문자.

### isDigit

```java
public static boolean isDigit(char ch)
```

**Parameters:**
- `ch` - 검토할 문자.

**Returns:**
- 숫자이면 true 아니면 false.

### digit

```java
public static int digit(char ch,
                        int radix)
```

**Parameters:**
- `radix` - 변환시 사용할 진법.

**Returns:**
- 문자에 해당하는 정수값.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 메서드 상세

### charValue

```java
public char charValue()
```

**Returns:**
- 현 객체의 값.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 정수형의 해쉬코드값.

### equals

```java
public boolean equals(Object o)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `o` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체 값을 사용해 만든 문자열.

### isLowerCase

```java
public static boolean isLowerCase(char ch)
```

**Parameters:**
- `ch` - 검토할 문자.

**Returns:**
- 소문자이면 true 아니면 false.

### toLowerCase

```java
public static char toLowerCase(char ch)
```

**Parameters:**
- `ch` - 변환할 문자.

**Returns:**
- 소문자로 변환된 문자.

### isUpperCase

```java
public static boolean isUpperCase(char ch)
```

**Parameters:**
- `ch` - 검토할 문자.

**Returns:**
- 대문자이면 true 아니면 false.

### toUpperCase

```java
public static char toUpperCase(char ch)
```

**Parameters:**
- `ch` - 변환할 문자.

**Returns:**
- 대문자로 변환된 문자.

### isDigit

```java
public static boolean isDigit(char ch)
```

**Parameters:**
- `ch` - 검토할 문자.

**Returns:**
- 숫자이면 true 아니면 false.

### digit

```java
public static int digit(char ch,
                        int radix)
```

**Parameters:**
- `radix` - 변환시 사용할 진법.

**Returns:**
- 문자에 해당하는 정수값.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
