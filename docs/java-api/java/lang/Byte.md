# Class Byte

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Byte
```

## 설명

**extends Object:**

Primitive 타입인 Byte 타입을 지원하기 위한 Wrap 클래스.

## 필드 요약

- `static byte MAX_VALUE` — Byte형의 최대값.
- `static byte MIN_VALUE` — Byte형의 최소값.

## 생성자 요약

- Byte (byte value) Byte형 객체를 생성한다.

## 메서드 요약

- `byte byteValue ()` — 현 객체의 값을 구한다.
- `boolean equals ( Object obj)` — 현 객체와 매개변수로 전달된 객체 값이 일치함을 검사한다.
- `int hashCode ()` — 현 Byte형 객체의 해쉬코드를 구한다.
- `static byte parseByte ( String s)` — 문자열을 10진법에의해 Byte형으로 변환한다.
- `static byte parseByte ( String s, int radix)` — 문자열을 특정 진법에의해 Byte형으로 변환한다.
- `String toString ()` — 현 객체 값을 표현할 수 있는 문자열을 구한다.

## 필드 상세

### MIN_VALUE

```java
public static final byte MIN_VALUE
```

- Byte형의 최소값.

### MAX_VALUE

```java
public static final byte MAX_VALUE
```

- Byte형의 최대값.

### Byte

```java
public Byte(byte value)
```

**Parameters:**
- `value` - 초기값.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 정수형의 해쉬코드.

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

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체의 값을 나타내는 문자열.

### parseByte

```java
public static byte parseByte(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 변환된 Byte형 값.

**Throws:**
- `NumberFormatException` - 변환할 수 없는 문자열일 때 발생.

### parseByte

```java
public static byte parseByte(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 변환시 사용할 진법.

**Returns:**
- 변환된 Byte형 값.

**Throws:**
- `NumberFormatException` - 변환할 수 없는 문자열일 때 발생.

### byteValue

```java
public byte byteValue()
```

**Returns:**
- 현 객체의 값.## 생성자 상세

### Byte

```java
public Byte(byte value)
```

**Parameters:**
- `value` - 초기값.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 정수형의 해쉬코드.

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

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체의 값을 나타내는 문자열.

### parseByte

```java
public static byte parseByte(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 변환된 Byte형 값.

**Throws:**
- `NumberFormatException` - 변환할 수 없는 문자열일 때 발생.

### parseByte

```java
public static byte parseByte(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 변환시 사용할 진법.

**Returns:**
- 변환된 Byte형 값.

**Throws:**
- `NumberFormatException` - 변환할 수 없는 문자열일 때 발생.

### byteValue

```java
public byte byteValue()
```

**Returns:**
- 현 객체의 값.## 메서드 상세

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 정수형의 해쉬코드.

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

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체의 값을 나타내는 문자열.

### parseByte

```java
public static byte parseByte(String s)
                      throws NumberFormatException
```

**Parameters:**
- `s` - 변환할 문자열.

**Returns:**
- 변환된 Byte형 값.

**Throws:**
- `NumberFormatException` - 변환할 수 없는 문자열일 때 발생.

### parseByte

```java
public static byte parseByte(String s,
                             int radix)
                      throws NumberFormatException
```

**Parameters:**
- `radix` - 변환시 사용할 진법.

**Returns:**
- 변환된 Byte형 값.

**Throws:**
- `NumberFormatException` - 변환할 수 없는 문자열일 때 발생.

### byteValue

```java
public byte byteValue()
```

**Returns:**
- 현 객체의 값.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
