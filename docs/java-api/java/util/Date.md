# Class Date

`package java.util`

```text
java.lang.Object
  |
  +--java.util.Date
```

## 설명

**extends Object:**

millisecond단위로 특정 시간을 나타내는 클래스

## 생성자 요약

- Date () VM의 현재 시각을 기준으로 객체를 생성한다.
- Date (long date) 특정 시각을 나타내는 객체를 생성한다.

## 메서드 요약

- `boolean equals ( Object obj)` — 현 객체와 매개변수로 전달된 객체 값이 일치함을 검사한다.
- `long getTime ()` — 현 객체가 나타내는 시각을 구한다.
- `int hashCode ()` — 현 객체의 해쉬코드를 구한다.
- `void setTime (long time)` — 현 객체의 시각을 특정 시각으로 바꾼다.

## 생성자 상세

### Date

```java
public Date()
```

- VM의 현재 시각을 기준으로 객체를 생성한다.

### Date

```java
public Date(long date)
```

**Parameters:**
- `date` - 나타내고자 하는 millesecond단위 시각.

### getTime

```java
public long getTime()
```

**Returns:**
- millisecond단위로 나타낸 현 객체 시각.

### setTime

```java
public void setTime(long time)
```

**Parameters:**
- `time` - 바꾸고자 하는 millisecond단위 시각.

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

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 정수형의 해쉬코드.## 메서드 상세

### getTime

```java
public long getTime()
```

**Returns:**
- millisecond단위로 나타낸 현 객체 시각.

### setTime

```java
public void setTime(long time)
```

**Parameters:**
- `time` - 바꾸고자 하는 millisecond단위 시각.

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

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 정수형의 해쉬코드.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
