---
title: "Class Date"
---

`package java.util`

```text
java.lang.Object
  |
  +--java.util.Date
```

## 설명

**extends Object:**

Date 클래스는 특정 시간을 밀리초까지 
나타냅니다.

이 클래스는 JDK 1.3 Date 클래스를 기반으로 하는 
J2ME의 하위 집합이었습니다. 이 클래스의 크기를 줄이기 위해 
많은 메소드와 변수가 정리되고 다른 메소드가 간소화되었습니다.

Date 클래스는 세계 표준시(UTC)를 반영하도록 만들어졌지만 
Java 가상 머신의 호스트 환경에 따라 
정확히 이를 반영하지 않을 수도 있습니다. 
오늘날의 거의 모든 운영 체제는 항상 1일 = 24x60x60 = 86400초로 가정합니다. 
하지만 UTC에서는 매년 또는 2년에 한 번 여분의 1초가 발생합니다. 
이를 "윤초"라고 합니다. 
윤초는 항상 12월 31일 또는 6월 30일의 마지막 초에 추가됩니다. 
예를 들어, 1995년의 마지막 초는 추가된 윤초로 인해 61초가 됩니다. 
대부분의 컴퓨터 시계는 윤초를 반영할 수 있을 만큼 
정확하지 않습니다.

**See Also:**
- ``TimeZone``, 
``Calendar``

## 생성자 요약

- Date () "기원년"이라고도 하는 표준 기본 시간인 1970년 1월 1일, 
00:00:00 GMT 이후의 지정된 밀리초 수로 현재 시간을 나타내도록 Date 객체를 할당하고 
초기화합니다.
- Date (long date) "기원년"이라고도 하는 표준 기본 시간인 1970년 1월 1일, 
00:00:00 GMT 이후의 지정된 밀리초 수를 나타내도록 Date 객체를 할당하고 
초기화합니다.

## 메서드 요약

- `boolean equals ( Object obj)` — 두 날짜가 같은지 비교합니다.
- `long getTime ()` — 이 Date 객체가 나타내는 1970년 1월 1일, 00:00:00 GMT 이후의 밀리초 수를 반환합니다.
- `int hashCode ()` — 이 객체의 해시 코드 값을 반환합니다.
- `void setTime (long time)` — 이 Date 객체가 1970년 1월 1일, 00:00:00 GMT로부터 time 밀리초 이후의 시간 지점을 나타내도록 설정합니다.
- `String toString ()` — 이 Date 객체를 다음 형식의 String 으로 변환합니다.

## 생성자 상세

### Date

```java
public Date()
```

- "기원년"이라고도 하는 표준 기본 시간인 1970년 1월 1일, 
00:00:00 GMT 이후의 지정된 밀리초 수로 현재 시간을 나타내도록 
`Date` 객체를 할당하고 
초기화합니다.

**See Also:**
- ``System.currentTimeMillis()``

### Date

```java
public Date(long date)
```

- "기원년"이라고도 하는 표준 기본 시간인 1970년 1월 1일, 
00:00:00 GMT 이후의 지정된 밀리초 수를 나타내도록 
`Date` 객체를 할당하고 
초기화합니다.

**Parameters:**
- `date` - 1970년 1월 1일, 00:00:00 GMT 이후의 밀리초

**See Also:**
- ``System.currentTimeMillis()``

### getTime

```java
public long getTime()
```

**Returns:**
- 이 날짜가 나타내는 1970년 1월 1일, 00:00:00 GMT 
 이후의 밀리초 수

**See Also:**
- ``setTime(long)``

### setTime

```java
public void setTime(long time)
```

**Parameters:**
- `time` - 밀리초 수

**See Also:**
- ``getTime()``

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
- ``getTime()``

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

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 날짜의 문자열 표현

**Since:**
- CLDC 1.1

## 메서드 상세

### getTime

```java
public long getTime()
```

**Returns:**
- 이 날짜가 나타내는 1970년 1월 1일, 00:00:00 GMT 
 이후의 밀리초 수

**See Also:**
- ``setTime(long)``

### setTime

```java
public void setTime(long time)
```

**Parameters:**
- `time` - 밀리초 수

**See Also:**
- ``getTime()``

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
- ``getTime()``

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

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 날짜의 문자열 표현

**Since:**
- CLDC 1.1
