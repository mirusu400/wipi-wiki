---
title: "Class Boolean"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Boolean
```

## 설명

**extends Object:**

Boolean 클래스는 프리미티브 유형의 
`boolean` 값을 객체에 포함합니다. 
`Boolean` 유형의 객체에는 유형이 
`boolean`인 단일 필드가 있습니다.

**Since:**
- JDK1.0, CLDC 1.0

## 필드 요약

- `static Boolean FALSE` — 프리미티브 값 false 에 해당하는 Boolean 객체
- `static Boolean TRUE` — 프리미티브 값 true 에 해당하는 Boolean 객체

## 생성자 요약

- Boolean (boolean value) value 인자를 나타내는 Boolean 객체를 할당합니다.

## 메서드 요약

- `boolean booleanValue ()` — 이 Boolean 객체의 값을 부울 프리미티브로 반환합니다.
- `boolean equals ( Object obj)` — 인자가 null 이 아니고 이 객체와 동일한 boolean 값을 나타내는 Boolean 객체인 경우에만 true 를 반환합니다.
- `int hashCode ()` — 이 Boolean 객체의 해시 코드를 반환합니다.
- `String toString ()` — 이 부울 값을 나타내는 문자열 객체를 반환합니다.

## 필드 상세

### TRUE

```java
public static final Boolean TRUE
```

- 프리미티브 값 `true`에 해당하는 
`Boolean` 객체

### FALSE

```java
public static final Boolean FALSE
```

- 프리미티브 값 `false`에 해당하는 `Boolean` 
객체

### Boolean

```java
public Boolean(boolean value)
```

- `value` 인자를 나타내는 
`Boolean` 객체를 할당합니다.

**Parameters:**
- `value` - `Boolean` 값

### booleanValue

```java
public boolean booleanValue()
```

**Returns:**
- 이 객체의 프리미티브 `boolean` 값

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 객체의 문자열 표현

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 이 객체가 `true`를 나타내면 정수 
`1231`, 객체가 `false`를 나타내면 
정수 `1237`

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
- Boolean 객체가 동일한 값을 나타내면 `true`, 
그렇지 않으면 `false`

**See Also:**
- ``hashCode()``, 
``Hashtable``

## 생성자 상세

### Boolean

```java
public Boolean(boolean value)
```

- `value` 인자를 나타내는 
`Boolean` 객체를 할당합니다.

**Parameters:**
- `value` - `Boolean` 값

### booleanValue

```java
public boolean booleanValue()
```

**Returns:**
- 이 객체의 프리미티브 `boolean` 값

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 객체의 문자열 표현

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 이 객체가 `true`를 나타내면 정수 
`1231`, 객체가 `false`를 나타내면 
정수 `1237`

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
- Boolean 객체가 동일한 값을 나타내면 `true`, 
그렇지 않으면 `false`

**See Also:**
- ``hashCode()``, 
``Hashtable``

## 메서드 상세

### booleanValue

```java
public boolean booleanValue()
```

**Returns:**
- 이 객체의 프리미티브 `boolean` 값

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 객체의 문자열 표현

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 이 객체가 `true`를 나타내면 정수 
`1231`, 객체가 `false`를 나타내면 
정수 `1237`

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
- Boolean 객체가 동일한 값을 나타내면 `true`, 
그렇지 않으면 `false`

**See Also:**
- ``hashCode()``, 
``Hashtable``
