# Class SimpleTimeZone

`package java.util`

```text
java.lang.Object
  |
  +--java.util.TimeZone
        |
        +--java.util.SimpleTimeZone
```

## 설명

**extends TimeZone:**

실제 사용하게 될 시간대 객체 클래스.

## 생성자 요약

- SimpleTimeZone (int rawOffset, String ID) SimpleTimeZone 새로운 객체를 생성한다.
- SimpleTimeZone (int rawOffset, String ID,
 int startMonth,
 int startDayOfWeekInMonth,
 int startDayOfWeek,
 int startTime,
 int endMonth,
 int endDayOfWeekInMonth,
 int endDayOfWeek,
 int endTime) 썸머 타임을 적용하는 새로운 객체를 만든다.

## 메서드 요약

- `boolean equals ( Object o)` — 현 시간대와 다른 시간대가 일치하는지 여부를 구한다.
- `int getOffset (int era, int year, int month, int day, int dayOfWeek, int millis)` — 특정 시각에서의 GMT대상으로 한 millisecond단위의 offset을 구한다.
- `int getRawOffset ()` — 썸머 타임을 무시한 GMT기준 offset을 구한다.
- `int hashCode ()` — 현객체를 위한 정수형의 해쉬코드를 구한다.
- `boolean inDaylightTime ( Date date)` — 특정일이 썸머 타임 기간 중인지 여부를 구한다.
- `void setRawOffset (int offsetMillis)` — GMT기준 offset값을 변경한다.
- `void setStartYear (int year)` — 섬머타임이 시작된 연수를 설정한다.
- `boolean useDaylightTime ()` — 현 시간대가 썸머타임을 사용하는지 여부를 구한다.

## 생성자 상세

### SimpleTimeZone

```java
public SimpleTimeZone(int rawOffset,
                      String ID)
```

**Parameters:**
- `ID` - 이 시간대 대표하는 문자열.

### SimpleTimeZone

```java
public SimpleTimeZone(int rawOffset,
                      String ID,
                      int startMonth,
                      int startDayOfWeekInMonth,
                      int startDayOfWeek,
                      int startTime,
                      int endMonth,
                      int endDayOfWeekInMonth,
                      int endDayOfWeek,
                      int endTime)
```

**Parameters:**
- `endTime` - 썸머타임 종료 시간 millisecond단위.

### equals

```java
public boolean equals(Object o)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `o` - 비교할 대상.

**Returns:**
- 일치하면 true아니면 false.

### getOffset

```java
public int getOffset(int era,
                     int year,
                     int month,
                     int day,
                     int dayOfWeek,
                     int millis)
```

**Overrides:**
- `getOffset` in class `TimeZone`

**Parameters:**
- `millis` - 시각.

**Returns:**
- GMT기준 offset.

### getRawOffset

```java
public int getRawOffset()
```

**Overrides:**
- `getRawOffset` in class `TimeZone`

**Returns:**
- GMT기준 offset.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 현 객체를 나타내는 해쉬코드.

### inDaylightTime

```java
public boolean inDaylightTime(Date date)
```

**Parameters:**
- `date` - 검토할 시각.

**Returns:**
- 썸머타임 기간 중이면 true 아니면 false.

### setRawOffset

```java
public void setRawOffset(int offsetMillis)
```

**Parameters:**
- `offsetMillis` - 변경할 offset.

### setStartYear

```java
public void setStartYear(int year)
```

**Parameters:**
- `year` - 섬머타임이 시작된 연수.

### useDaylightTime

```java
public boolean useDaylightTime()
```

**Overrides:**
- `useDaylightTime` in class `TimeZone`

**Returns:**
- 썸머타임을 사용하면 true 아니면 false.## 메서드 상세

### equals

```java
public boolean equals(Object o)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `o` - 비교할 대상.

**Returns:**
- 일치하면 true아니면 false.

### getOffset

```java
public int getOffset(int era,
                     int year,
                     int month,
                     int day,
                     int dayOfWeek,
                     int millis)
```

**Overrides:**
- `getOffset` in class `TimeZone`

**Parameters:**
- `millis` - 시각.

**Returns:**
- GMT기준 offset.

### getRawOffset

```java
public int getRawOffset()
```

**Overrides:**
- `getRawOffset` in class `TimeZone`

**Returns:**
- GMT기준 offset.

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 현 객체를 나타내는 해쉬코드.

### inDaylightTime

```java
public boolean inDaylightTime(Date date)
```

**Parameters:**
- `date` - 검토할 시각.

**Returns:**
- 썸머타임 기간 중이면 true 아니면 false.

### setRawOffset

```java
public void setRawOffset(int offsetMillis)
```

**Parameters:**
- `offsetMillis` - 변경할 offset.

### setStartYear

```java
public void setStartYear(int year)
```

**Parameters:**
- `year` - 섬머타임이 시작된 연수.

### useDaylightTime

```java
public boolean useDaylightTime()
```

**Overrides:**
- `useDaylightTime` in class `TimeZone`

**Returns:**
- 썸머타임을 사용하면 true 아니면 false.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
