---
title: "Class TimeZone"
---

`package java.util`

```text
java.lang.Object
  |
  +--java.util.TimeZone
```

## 설명

**extends Object:**

`TimeZone`은 표준 시간대 오프셋을 나타내며 일광 절약 시간도 
고려합니다.

일반적으로 `TimeZone`은 프로그램이 실행되는 표준 시간대를 
기반으로 `TimeZone`을 만드는 `getDefault`를 
사용하여 구합니다. 예를 들어, 일본에서 프로그램을 실행하는 경우 
`getDefault`는 일본 표준 시간을 기반으로 `TimeZone` 객체를 만듭니다.

`getTimeZone`을 표준 시간대 ID와 함께 사용하여 
`TimeZone`을 구할 수도 있습니다. 
예를 들어, 태평양 표준시의 표준 시간대는 "PST"입니다. 
따라서 다음과 같은 PST `TimeZone` 객체를 얻을 수 있습니다.

이 클래스는 JDK 1.3에 포함된 java.util.TimeZone 클래스의 순수 하위 집합입니다.

표준 시간대 ID는 "GMT"만 지원하면 됩니다.

메소드와 변수가 하위 집합이 되는 것과 별도로 getTimeZone() 메소드의 
의미 체계도 하위 집합이 될 수 있습니다. 
"GMT-8:00"과 같은 사용자 정의 ID는 지원하지 않아도 됩니다.

**See Also:**
- ``Calendar``, 
``Date``

## 생성자 요약

- TimeZone ()

## 메서드 요약

- `static String [] getAvailableIDs ()` — 지원되는 사용 가능한 모든 ID를 가져옵니다.
- `static TimeZone getDefault ()` — 이 호스트의 기본 TimeZone 을 가져옵니다.
- `String getID ()` — 이 표준 시간대의 ID를 가져옵니다.
- `abstract  int getOffset (int era, int year, int month, int day, int dayOfWeek, int millis)` — 일광 절약 시간의 경우 현재 날짜에 대한 수정된 오프셋을 구합니다.
- `abstract  int getRawOffset ()` — 이 표준 시간대의 GMT 오프셋을 가져옵니다.
- `static TimeZone getTimeZone ( String ID)` — 지정된 ID의 TimeZone 을 가져옵니다.
- `abstract  boolean useDaylightTime ()` — 표준 시간대가 일광 절약 시간을 사용하는지 쿼리합니다.

## 생성자 상세

### TimeZone

```java
public TimeZone()
```

### getOffset

```java
public abstract int getOffset(int era,
                              int year,
                              int month,
                              int day,
                              int dayOfWeek,
                              int millis)
```

**Parameters:**
- `millis` - *표준* 현지 시간에서의 일(밀리초)

**Returns:**
- 이는 현지 시간을 얻기 위해 GMT에 추가해야 하는 오프셋

**Throws:**
- `IllegalArgumentException` - era, month, day,
 dayOfWeek 또는 millis 매개 변수가 범위에서 벗어난 경우

### getRawOffset

```java
public abstract int getRawOffset()
```

**Returns:**
- 이 표준 시간대의 GMT 오프셋

### useDaylightTime

```java
public abstract boolean useDaylightTime()
```

**Returns:**
- 표준 시간대가 일광 절약 시간을 사용하는지 여부

### getID

```java
public String getID()
```

**Returns:**
- 이 표준 시간대의 ID

### getTimeZone

```java
public static TimeZone getTimeZone(String ID)
```

**Parameters:**
- `ID` - `TimeZone` ID ("GMT"와 같은 약어 또는 
"America/Los_Angeles"와 같은 전체 이름)

표준 시간대 ID는 "GMT"만 지원하면 됩니다.

**Returns:**
- 지정된 TimeZone 또는 지정된 ID를 확인할 수 없는 경우 
GMT 영역

### getDefault

```java
public static TimeZone getDefault()
```

**Returns:**
- 기본 `TimeZone`

### getAvailableIDs

```java
public static String[] getAvailableIDs()
```

**Returns:**
- ID 배열

## 메서드 상세

### getOffset

```java
public abstract int getOffset(int era,
                              int year,
                              int month,
                              int day,
                              int dayOfWeek,
                              int millis)
```

**Parameters:**
- `millis` - *표준* 현지 시간에서의 일(밀리초)

**Returns:**
- 이는 현지 시간을 얻기 위해 GMT에 추가해야 하는 오프셋

**Throws:**
- `IllegalArgumentException` - era, month, day,
 dayOfWeek 또는 millis 매개 변수가 범위에서 벗어난 경우

### getRawOffset

```java
public abstract int getRawOffset()
```

**Returns:**
- 이 표준 시간대의 GMT 오프셋

### useDaylightTime

```java
public abstract boolean useDaylightTime()
```

**Returns:**
- 표준 시간대가 일광 절약 시간을 사용하는지 여부

### getID

```java
public String getID()
```

**Returns:**
- 이 표준 시간대의 ID

### getTimeZone

```java
public static TimeZone getTimeZone(String ID)
```

**Parameters:**
- `ID` - `TimeZone` ID ("GMT"와 같은 약어 또는 
"America/Los_Angeles"와 같은 전체 이름)

표준 시간대 ID는 "GMT"만 지원하면 됩니다.

**Returns:**
- 지정된 TimeZone 또는 지정된 ID를 확인할 수 없는 경우 
GMT 영역

### getDefault

```java
public static TimeZone getDefault()
```

**Returns:**
- 기본 `TimeZone`

### getAvailableIDs

```java
public static String[] getAvailableIDs()
```

**Returns:**
- ID 배열
