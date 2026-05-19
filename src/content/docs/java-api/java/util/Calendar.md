---
title: "Class Calendar"
---

`package java.util`

```text
java.lang.Object
  |
  +--java.util.Calendar
```

## 설명

**Direct Known Subclasses:**
- `GregorianCalendar`

**extends Object:**

연도,월,일,요일 등의 정보를 얻기 위한 캘린더 클래스들이
 상속받아야 할 추상 클래스.

## 필드 요약

- `static int AM`
- `static int AM_PM`
- `static int APRIL`
- `protected  boolean areFieldsSet`
- `static int AUGUST`
- `static int DATE`
- `static int DAY_OF_MONTH`
- `static int DAY_OF_WEEK`
- `static int DAY_OF_WEEK_IN_MONTH`
- `static int DAY_OF_YEAR`
- `static int DECEMBER`
- `static int DST_OFFSET`
- `static int ERA`
- `static int FEBRUARY`
- `static int FIELD_COUNT`
- `protected  int[] fields`
- `static int FRIDAY`
- `static int HOUR`
- `static int HOUR_OF_DAY`
- `protected  boolean[] isSet`
- `protected  boolean isTimeSet`
- `static int JANUARY`
- `static int JULY`
- `static int JUNE`
- `static int MARCH`
- `static int MAY`
- `static int MILLISECOND`
- `static int MINUTE`
- `static int MONDAY`
- `static int MONTH`
- `static int NOVEMBER`
- `static int OCTOBER`
- `static int PM`
- `static int SATURDAY`
- `static int SECOND`
- `static int SEPTEMBER`
- `static int SUNDAY`
- `static int THURSDAY`
- `protected  long time`
- `static int TUESDAY`
- `static int UNDECIMBER`
- `static int WEDNESDAY`
- `static int WEEK_OF_MONTH`
- `static int WEEK_OF_YEAR`
- `static int YEAR`
- `static int ZONE_OFFSET`

## 생성자 요약

- `protected Calendar ()` — 새로운 객체를 만든다.
- `protected Calendar ( TimeZone zne)` — 새로운 객체를 만든다.

## 메서드 요약

- `boolean after ( Object when)` — 현 객체에 설정된 시각와 매개변수로 넘어온 시각을 비교한다.
- `boolean before ( Object when)` — 현 객체에 설정된 시각와 매개변수로 넘어온 시각을 비교한다.
- `protected  void complete ()` — 현 캘랜더에 설정한 시각을 가지고 날짜,년도,월 등을 구한 다음 저장하고 현 시각에 대응하는 GMT+0시각을 구해 저장한다.
- `protected abstract  void computeFields ()` — 캘린더 내에 년도,월,일등을 저장하는 fields 필드에 현 캘랜더가 나타내는 시각을 기준으로 계산해서 얻은 값을 저장한다.
- `protected abstract  void computeTime ()` — 현 시각을 GMT시각으로 변환 후 time 필드에 저장한다.
- `boolean equals ( Object when)` — 현 객체에 설정된 시각와 매개변수로 넘어온 시각을 비교한다.
- `int get (int field)` — 년도,월,일,요일 등 field값에 따라 필요한 정보를 구한다.
- `protected  int getFirstDayOfWeek ()` — 일주일의 첫번째 요일이 무엇인지 구한다.
- `protected abstract  int getGreatestMinimum (int field)`
- `static Calendar getInstance ()` — VM에서 사용하는 디폴트 캘랜더 객체를 얻는다.
- `static Calendar getInstance ( TimeZone zone)` — 특정 시간대를 사용하는 캘랜더 객체를 얻는다.
- `protected abstract  int getLeastMaximum (int field)`
- `protected abstract  int getMaximum (int field)`
- `protected  int getMinimalDaysInFirstWeek ()`
- `protected abstract  int getMinimum (int field)`
- `Date getTime ()` — 현 시간을 구한다.
- `protected  long getTimeInMillis ()` — 현 캘랜더가 나타내는 시각을 GMT+0시각으로 변환한 값을 구한다.
- `TimeZone getTimeZone ()` — 현 객체가 사용하는 시간대를 구한다.
- `static void initialize ()`
- `protected  int internalGet (int field)`
- `protected  boolean isLenient ()`
- `protected  boolean isSet (int field)`
- `void set (int field, int value)` — 캘랜더의 관련 필드에 값을 설정한다.
- `protected  void set (int year, int month, int date)` — 현 캘랜더가 나타내는 년도,달,날짜를 재설정한다.
- `void setTime ( Date date)` — 캘랜더의 현 날짜를 설정한다.
- `protected  void setTimeInMillis (long millis)` — 현 캘랜더가 나타내는 시각을 재설정한다.
- `void setTimeZone ( TimeZone value)` — 캘랜더의 시간대를 바꾼다.

## 필드 상세

### ERA

```java
public static final int ERA
```

### YEAR

```java
public static final int YEAR
```

### MONTH

```java
public static final int MONTH
```

### WEEK_OF_YEAR

```java
public static final int WEEK_OF_YEAR
```

### WEEK_OF_MONTH

```java
public static final int WEEK_OF_MONTH
```

### DATE

```java
public static final int DATE
```
