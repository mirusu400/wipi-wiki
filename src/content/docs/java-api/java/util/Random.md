---
title: "Class Random"
---

`package java.util`

```text
java.lang.Object
  |
  +--java.util.Random
```

## 설명

**extends Object:**

난수 발생을 위한 클래스.

## 생성자 요약

- Random () 현재 시각을 seed로하는 객체를 생성한다.
- Random (long seed) 특정 seed값을 초기값으로 가지는 객체를 생성한다.

## 메서드 요약

- `protected  int next (int bits)`
- `int nextInt ()` — 정수형의 다음 난수를 구한다.
- `long nextLong ()` — Long형의 다음 난수를 구한다.
- `void setSeed (long seed)` — 객체의 seed를 변경한다.

## 생성자 상세

### Random

```java
public Random()
```

- 현재 시각을 seed로하는 객체를 생성한다.

### Random

```java
public Random(long seed)
```

**Parameters:**
- `seed` - 사용하고자 하는 seed값.

### setSeed

```java
public void setSeed(long seed)
```

**Parameters:**
- `seed` - 새로운 seed값.

### next

```java
protected int next(int bits)
```

### nextInt

```java
public int nextInt()
```

**Returns:**
- 정수형의 새로운 난수.

### nextLong

```java
public long nextLong()
```

**Returns:**
- Long형의 새로운 난수.## 메서드 상세

### setSeed

```java
public void setSeed(long seed)
```

**Parameters:**
- `seed` - 새로운 seed값.

### next

```java
protected int next(int bits)
```

### nextInt

```java
public int nextInt()
```

**Returns:**
- 정수형의 새로운 난수.

### nextLong

```java
public long nextLong()
```

**Returns:**
- Long형의 새로운 난수.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
