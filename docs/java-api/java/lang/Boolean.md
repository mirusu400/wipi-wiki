# Class Boolean

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Boolean
```

## 설명

**extends Object:**

Primitive 타입인 Boolean 타입을 지원하기 위한 Wrap 클래스.

## 생성자 요약

- Boolean (boolean value) Boolean 객체를 생성한다.

## 메서드 요약

- `boolean booleanValue ()` — 현 객체의 값을 구한다.
- `boolean equals ( Object obj)` — 현 객체와 매개변수로 전달된 객체 값이 일치함을 검사한다.
- `int hashCode ()` — 현 객체의 해쉬코드 값을 구한다.
- `String toString ()` — 현 객체 값을 표현할 수 있는 문자열을 구한다.

## 생성자 상세

### Boolean

```java
public Boolean(boolean value)
```

**Parameters:**
- `value` - 초기값.

### booleanValue

```java
public boolean booleanValue()
```

**Returns:**
- 현 객체의 참,거짓 값.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 현 객체의 정수형 해쉬코드.

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
- value값이 참이면 `true` 거짓이면 `false` 문자열.## 메서드 상세

### booleanValue

```java
public boolean booleanValue()
```

**Returns:**
- 현 객체의 참,거짓 값.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 현 객체의 정수형 해쉬코드.

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
- value값이 참이면 `true` 거짓이면 `false` 문자열.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
