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

**extends Object:**

`Calendar`는 `Date` 객체 및 
`YEAR`, `MONTH`, `DAY`, 
`HOUR` 등의 정수 필드 집합 간의 변환을 위한 
추상 기본 클래스입니다. (`Date` 객체는 
특정 시간을 밀리초까지 나타냅니다. `Date` 클래스에 대한 
자세한 내용은 ``Date``를 
참조하십시오.)

`Calendar`의 서브 클래스는 특정 달력 시스템의 
규칙에 따라 `Date`를 해석합니다.

로켈에 영향을 받는 다른 클래스와 마찬가지로 `Calendar`는 
일반적으로 유용한 이 유형의 객체를 가져오는 
클래스 메소드인 `getInstance`를 제공합니다.

`Calendar` 객체는 특정 언어와 달력 스타일
(예: 일본어-그레고리안, 일본어-전통)의 날짜-시간 서식을 구현하는 데 
필요한 필드 값을 항상 생성할 수 있습니다.

시간 필드에서 `Date`를 계산할 때 연도와 달만 있고 
일이 없는 경우와 같이 `Date`를 계산하는 데 
필요한 정보가 부족할 수도 있습니다.

**정보 부족.** 달력은 기본 정보를 사용하여 누락된 필드를 
지정합니다. 기본 정보는 달력별로 다를 수 있습니다. 
그레고리안력의 경우 필드 기본값은 기원년의 값과 같습니다. 
예를 들어, YEAR = 1970년, MONTH = 1월, DATE = 1일과 같습니다. 

**주:** 자정이 어느 날에 속할지에 대한 해석의 모호성은 
다음 날에 "속하는" 것으로 해결합니다.
 
 1969년 12월 31일 23:59 < 1970년 1월 1일 00:00
 
 12:00 PM은 정오, 12:00 AM은 자정
 
 1월 1일 11:59 PM < 1월 2일 12:00 AM < 1월 2일 12:01 AM
 
 3월 10일 11:59 AM < 3월 10일 12:00 PM < 3월 10일 12:01 PM
 
 24:00 이상은 유효하지 않습니다. 
AM/PM 모드에서 12보다 큰 시간은 유효하지 않습니다. 
시간 설정은 날짜를 변경하지 않습니다.

같은 시간을 AM/PM 또는 24시간 모드로 입력하면 입력된 시간이 아닌 
실제 시간으로 등가를 확인합니다.

이 클래스는 JDK 1.3 Calendar 클래스를 기반으로 하는 J2ME의 하위 집합이었습니다. 
이 클래스의 크기를 줄이기 위해 많은 메소드와 변수가 정리되고 
다른 메소드가 간소화되었습니다.

**See Also:**
- ``Date``, 
``TimeZone``

## 필드 요약

- `static int AM` — 자정부터 정오 직전까지의 시간을 나타내는 AM_PM 필드 값.
- `static int AM_PM` — HOUR 가 정오 전인지 또는 후인지를 나타내는 get 및 set 의 필드 번호.
- `static int APRIL` — 한 해의 네 번째 달을 나타내는 MONTH 필드 값.
- `static int AUGUST` — 한 해의 여덟 번째 달을 나타내는 MONTH 필드 값.
- `static int DATE` — 날짜를 나타내는 get 및 set 의 필드 번호.
- `static int DAY_OF_MONTH` — 날짜를 나타내는 get 및 set 의 필드 번호.
- `static int DAY_OF_WEEK` — 주를 나타내는 get 및 set 의 필드 번호.
- `static int DECEMBER` — 한 해의 열두 번째 달을 나타내는 MONTH 필드 값.
- `static int FEBRUARY` — 한 해의 두 번째 달을 나타내는 MONTH 필드 값.
- `protected  int[] fields` — 이 달력에 현재 설정된 시간의 필드 값.
- `static int FRIDAY` — 금요일을 나타내는 DAY_OF_WEEK 필드 값.
- `static int HOUR` — 오전 시간인지 또는 오후 시간인지를 나타내는 get 및 set 의 필드 번호.
- `static int HOUR_OF_DAY` — 시간을 나타내는 get 및 set 의 필드 번호.
- `protected  boolean[] isSet` — 달력에 지정된 시간 필드가 설정되었는지 여부를 나타내는 플래그.
- `static int JANUARY` — 한 해의 첫 번째 달을 나타내는 MONTH 필드 값.
- `static int JULY` — 한 해의 일곱 번째 달을 나타내는 MONTH 필드 값.
- `static int JUNE` — 한 해의 여섯 번째 달을 나타내는 MONTH 필드 값.
- `static int MARCH` — 한 해의 세 번째 달을 나타내는 MONTH 필드 값.
- `static int MAY` — 한 해의 다섯 번째 달을 나타내는 MONTH 필드 값.
- `static int MILLISECOND` — 밀리초를 나타내는 get 및 set 의 필드 번호.
- `static int MINUTE` — 분을 나타내는 get 및 set 의 필드 번호.
- `static int MONDAY` — 월요일을 나타내는 DAY_OF_WEEK 필드 값.
- `static int MONTH` — 달을 나타내는 get 및 set 의 필드 번호.
- `static int NOVEMBER` — 한 해의 열한 번째 달을 나타내는 MONTH 필드 값.
- `static int OCTOBER` — 한 해의 열 번째 달을 나타내는 MONTH 필드 값.
- `static int PM` — 정오부터 자정 직전까지의 시간을 나타내는 AM_PM 필드 값.
- `static int SATURDAY` — 토요일을 나타내는 DAY_OF_WEEK 필드 값.
- `static int SECOND` — 초를 나타내는 get 및 set 의 필드 번호.
- `static int SEPTEMBER` — 한 해의 아홉 번째 달을 나타내는 MONTH 필드 값.
- `static int SUNDAY` — 일요일을 나타내는 DAY_OF_WEEK 필드 값.
- `static int THURSDAY` — 목요일을 나타내는 DAY_OF_WEEK 필드 값.
- `protected  long time` — 이 달력에 현재 설정된 시간(1970년 1월 1일, 0:00:00 GMT 이후의 밀리초 단위로 표시)
- `static int TUESDAY` — 화요일을 나타내는 DAY_OF_WEEK 필드 값.
- `static int WEDNESDAY` — 수요일을 나타내는 DAY_OF_WEEK 필드 값.
- `static int YEAR` — 연도를 나타내는 get 및 set 의 필드 번호.

## 생성자 요약

- `protected Calendar ()` — 기본 표준 시간대를 사용하여 달력을 구성합니다.

## 메서드 요약

- `boolean after ( Object when)` — 시간 필드 레코드를 비교합니다.
- `boolean before ( Object when)` — 시간 필드 레코드를 비교합니다.
- `protected abstract  void computeFields ()` — 현재 밀리초 시간 값인 time 을 fields[] 의 필드 값으로 변환합니다.
- `protected abstract  void computeTime ()` — fields[] 의 현재 필드 값을 밀리초 시간 값인 time 으로 변환합니다.
- `boolean equals ( Object obj)` — 이 달력을 지정된 객체와 비교합니다.
- `int get (int field)` — 지정된 시간 필드 값을 가져옵니다.
- `static Calendar getInstance ()` — 기본 표준 시간대를 사용하여 달력을 가져옵니다.
- `static Calendar getInstance ( TimeZone zone)` — 지정한 표준 시간대를 사용하여 달력을 가져옵니다.
- `Date getTime ()` — 이 달력의 현재 시간을 가져옵니다.
- `protected  long getTimeInMillis ()` — 이 달력의 현재 시간을 가져옵니다(1970년 1월 1일, 0:00:00 GMT(기원년) 이후의 밀리초 단위로 표시된 long).
- `TimeZone getTimeZone ()` — 표준 시간대를 가져옵니다.
- `void set (int field, int value)` — 지정된 값을 사용하여 시간 필드를 설정합니다.
- `void setTime ( Date date)` — 지정된 날짜를 사용하여 이 달력의 현재 시간을 설정합니다.
- `protected  void setTimeInMillis (long millis)` — 지정된 long 값을 사용하여 이 달력의 현재 시간을 설정합니다.
- `void setTimeZone ( TimeZone value)` — 지정된 표준 시간대 값을 사용하여 표준 시간대를 설정합니다.

## 필드 상세

### YEAR

```java
public static final int YEAR
```

**See Also:**
- `Constant Field Values`

### MONTH

```java
public static final int MONTH
```

**See Also:**
- `Constant Field Values`

### DATE

```java
public static final int DATE
```

**See Also:**
- ``DAY_OF_MONTH``, 
`Constant Field Values`

### DAY_OF_MONTH

```java
public static final int DAY_OF_MONTH
```

**See Also:**
- ``DATE``, 
`Constant Field Values`

### DAY_OF_WEEK

```java
public static final int DAY_OF_WEEK
```

**See Also:**
- `Constant Field Values`

### AM_PM

```java
public static final int AM_PM
```

**See Also:**
- ``AM``, 
``PM``, 
``HOUR``, 
`Constant Field Values`

### HOUR

```java
public static final int HOUR
```

**See Also:**
- ``AM_PM``, 
``HOUR_OF_DAY``, 
`Constant Field Values`

### HOUR_OF_DAY

```java
public static final int HOUR_OF_DAY
```

**See Also:**
- `Constant Field Values`

### MINUTE

```java
public static final int MINUTE
```

**See Also:**
- `Constant Field Values`

### SECOND

```java
public static final int SECOND
```

**See Also:**
- `Constant Field Values`

### MILLISECOND

```java
public static final int MILLISECOND
```

**See Also:**
- `Constant Field Values`

### SUNDAY

```java
public static final int SUNDAY
```

**See Also:**
- `Constant Field Values`

### MONDAY

```java
public static final int MONDAY
```

**See Also:**
- `Constant Field Values`

### TUESDAY

```java
public static final int TUESDAY
```

**See Also:**
- `Constant Field Values`

### WEDNESDAY

```java
public static final int WEDNESDAY
```

**See Also:**
- `Constant Field Values`

### THURSDAY

```java
public static final int THURSDAY
```

**See Also:**
- `Constant Field Values`

### FRIDAY

```java
public static final int FRIDAY
```

**See Also:**
- `Constant Field Values`

### SATURDAY

```java
public static final int SATURDAY
```

**See Also:**
- `Constant Field Values`

### JANUARY

```java
public static final int JANUARY
```

**See Also:**
- `Constant Field Values`

### FEBRUARY

```java
public static final int FEBRUARY
```

**See Also:**
- `Constant Field Values`

### MARCH

```java
public static final int MARCH
```

**See Also:**
- `Constant Field Values`

### APRIL

```java
public static final int APRIL
```

**See Also:**
- `Constant Field Values`

### MAY

```java
public static final int MAY
```

**See Also:**
- `Constant Field Values`

### JUNE

```java
public static final int JUNE
```

**See Also:**
- `Constant Field Values`

### JULY

```java
public static final int JULY
```

**See Also:**
- `Constant Field Values`

### AUGUST

```java
public static final int AUGUST
```

**See Also:**
- `Constant Field Values`

### SEPTEMBER

```java
public static final int SEPTEMBER
```

**See Also:**
- `Constant Field Values`

### OCTOBER

```java
public static final int OCTOBER
```

**See Also:**
- `Constant Field Values`

### NOVEMBER

```java
public static final int NOVEMBER
```

**See Also:**
- `Constant Field Values`

### DECEMBER

```java
public static final int DECEMBER
```

**See Also:**
- `Constant Field Values`

### AM

```java
public static final int AM
```

**See Also:**
- `Constant Field Values`

### PM

```java
public static final int PM
```

**See Also:**
- `Constant Field Values`

### fields

```java
protected int[] fields
```

- 이 달력에 현재 설정된 시간의 필드 값.

### isSet

```java
protected boolean[] isSet
```

- 달력에 지정된 시간 필드가 설정되었는지 여부를 나타내는 플래그. 
이는 `FIELD_COUNT` 부울 배열입니다.

### time

```java
protected long time
```

- 이 달력에 현재 설정된 시간(1970년 1월 1일, 
0:00:00 GMT 이후의 밀리초 단위로 표시)

### Calendar

```java
protected Calendar()
```

- 기본 표준 시간대를 사용하여 달력을 구성합니다.

**See Also:**
- ``TimeZone.getDefault()``

### getTime

```java
public final Date getTime()
```

**Returns:**
- 현재 시간

**See Also:**
- ``setTime(java.util.Date)``

### setTime

```java
public final void setTime(Date date)
```

**Parameters:**
- `date` - 지정된 날짜

**See Also:**
- ``getTime()``

### getInstance

```java
public static Calendar getInstance()
```

**Returns:**
- 달력

### getInstance

```java
public static Calendar getInstance(TimeZone zone)
```

**Parameters:**
- `zone` - 사용할 표준 시간대

**Returns:**
- 달력

### getTimeInMillis

```java
protected long getTimeInMillis()
```

**Returns:**
- 기원년으로부터의 UTC 밀리초로 표시된 현재 시간

**See Also:**
- ``setTimeInMillis(long)``

### setTimeInMillis

```java
protected void setTimeInMillis(long millis)
```

**Parameters:**
- `millis` - 기원년으로부터의 UTC 밀리초로 표시된 새 시간

**See Also:**
- ``getTimeInMillis()``

### get

```java
public final int get(int field)
```

**Parameters:**
- `field` - 지정된 시간 필드(YEAR, MONTH, DATE, DAY_OF_WEEK, 
 HOUR_OF_DAY, HOUR, AM_PM, MINUTE, 
 SECOND 또는 MILLISECOND)

**Returns:**
- 지정된 시간 필드 값

**Throws:**
- `ArrayIndexOutOfBoundsException` - 매개 변수가 위의 값 중 하나가 아닌 경우

### set

```java
public final void set(int field,
                      int value)
```

**Parameters:**
- `value` - 지정된 시간 필드에 설정되는 값

**Throws:**
- `ArrayIndexOutOfBoundsException` - 유효하지 않은 
필드 매개 변수를 받은 경우

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `obj` - 비교할 객체

**Returns:**
- 두 객체가 동일하면 `true`, 
다르면 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

### before

```java
public boolean before(Object when)
```

**Parameters:**
- `when` - 이 달력과 비교되는 달력

**Returns:**
- 이 달력의 현재 시간이 when 달력의 시간보다 빠르면 true, 
그렇지 않으면 false

### after

```java
public boolean after(Object when)
```

**Parameters:**
- `when` - 이 달력과 비교되는 달력

**Returns:**
- 이 달력의 현재 시간이 when 달력의 시간보다 늦으면 true, 
그렇지 않으면 false

### setTimeZone

```java
public void setTimeZone(TimeZone value)
```

**Parameters:**
- `value` - 지정된 표준 시간대

**See Also:**
- ``getTimeZone()``

### getTimeZone

```java
public TimeZone getTimeZone()
```

**Returns:**
- 이 달력에 연결된 표준 시간대 객체

**See Also:**
- ``setTimeZone(java.util.TimeZone)``

### computeFields

```java
protected abstract void computeFields()
```

현재 밀리초 시간 값인 time 을 fields[] 의 
필드 값으로 변환합니다. 
이렇게 하면 시간 필드 값을 달력에 설정된 
새 값과 동기화할 수 있습니다.

### computeTime

```java
protected abstract void computeTime()
```

fields[] 의 현재 필드 값을 밀리초 
시간 값인 time 으로 
변환합니다.

## 생성자 상세

### Calendar

```java
protected Calendar()
```

- 기본 표준 시간대를 사용하여 달력을 구성합니다.

**See Also:**
- ``TimeZone.getDefault()``

### getTime

```java
public final Date getTime()
```

**Returns:**
- 현재 시간

**See Also:**
- ``setTime(java.util.Date)``

### setTime

```java
public final void setTime(Date date)
```

**Parameters:**
- `date` - 지정된 날짜

**See Also:**
- ``getTime()``

### getInstance

```java
public static Calendar getInstance()
```

**Returns:**
- 달력

### getInstance

```java
public static Calendar getInstance(TimeZone zone)
```

**Parameters:**
- `zone` - 사용할 표준 시간대

**Returns:**
- 달력

### getTimeInMillis

```java
protected long getTimeInMillis()
```

**Returns:**
- 기원년으로부터의 UTC 밀리초로 표시된 현재 시간

**See Also:**
- ``setTimeInMillis(long)``

### setTimeInMillis

```java
protected void setTimeInMillis(long millis)
```

**Parameters:**
- `millis` - 기원년으로부터의 UTC 밀리초로 표시된 새 시간

**See Also:**
- ``getTimeInMillis()``

### get

```java
public final int get(int field)
```

**Parameters:**
- `field` - 지정된 시간 필드(YEAR, MONTH, DATE, DAY_OF_WEEK, 
 HOUR_OF_DAY, HOUR, AM_PM, MINUTE, 
 SECOND 또는 MILLISECOND)

**Returns:**
- 지정된 시간 필드 값

**Throws:**
- `ArrayIndexOutOfBoundsException` - 매개 변수가 위의 값 중 하나가 아닌 경우

### set

```java
public final void set(int field,
                      int value)
```

**Parameters:**
- `value` - 지정된 시간 필드에 설정되는 값

**Throws:**
- `ArrayIndexOutOfBoundsException` - 유효하지 않은 
필드 매개 변수를 받은 경우

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `obj` - 비교할 객체

**Returns:**
- 두 객체가 동일하면 `true`, 
다르면 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

### before

```java
public boolean before(Object when)
```

**Parameters:**
- `when` - 이 달력과 비교되는 달력

**Returns:**
- 이 달력의 현재 시간이 when 달력의 시간보다 빠르면 true, 
그렇지 않으면 false

### after

```java
public boolean after(Object when)
```

**Parameters:**
- `when` - 이 달력과 비교되는 달력

**Returns:**
- 이 달력의 현재 시간이 when 달력의 시간보다 늦으면 true, 
그렇지 않으면 false

### setTimeZone

```java
public void setTimeZone(TimeZone value)
```

**Parameters:**
- `value` - 지정된 표준 시간대

**See Also:**
- ``getTimeZone()``

### getTimeZone

```java
public TimeZone getTimeZone()
```

**Returns:**
- 이 달력에 연결된 표준 시간대 객체

**See Also:**
- ``setTimeZone(java.util.TimeZone)``

### computeFields

```java
protected abstract void computeFields()
```

현재 밀리초 시간 값인 time 을 fields[] 의 
필드 값으로 변환합니다. 
이렇게 하면 시간 필드 값을 달력에 설정된 
새 값과 동기화할 수 있습니다.

### computeTime

```java
protected abstract void computeTime()
```

fields[] 의 현재 필드 값을 밀리초 
시간 값인 time 으로 
변환합니다.

## 메서드 상세

### getTime

```java
public final Date getTime()
```

**Returns:**
- 현재 시간

**See Also:**
- ``setTime(java.util.Date)``

### setTime

```java
public final void setTime(Date date)
```

**Parameters:**
- `date` - 지정된 날짜

**See Also:**
- ``getTime()``

### getInstance

```java
public static Calendar getInstance()
```

**Returns:**
- 달력

### getInstance

```java
public static Calendar getInstance(TimeZone zone)
```

**Parameters:**
- `zone` - 사용할 표준 시간대

**Returns:**
- 달력

### getTimeInMillis

```java
protected long getTimeInMillis()
```

**Returns:**
- 기원년으로부터의 UTC 밀리초로 표시된 현재 시간

**See Also:**
- ``setTimeInMillis(long)``

### setTimeInMillis

```java
protected void setTimeInMillis(long millis)
```

**Parameters:**
- `millis` - 기원년으로부터의 UTC 밀리초로 표시된 새 시간

**See Also:**
- ``getTimeInMillis()``

### get

```java
public final int get(int field)
```

**Parameters:**
- `field` - 지정된 시간 필드(YEAR, MONTH, DATE, DAY_OF_WEEK, 
 HOUR_OF_DAY, HOUR, AM_PM, MINUTE, 
 SECOND 또는 MILLISECOND)

**Returns:**
- 지정된 시간 필드 값

**Throws:**
- `ArrayIndexOutOfBoundsException` - 매개 변수가 위의 값 중 하나가 아닌 경우

### set

```java
public final void set(int field,
                      int value)
```

**Parameters:**
- `value` - 지정된 시간 필드에 설정되는 값

**Throws:**
- `ArrayIndexOutOfBoundsException` - 유효하지 않은 
필드 매개 변수를 받은 경우

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `obj` - 비교할 객체

**Returns:**
- 두 객체가 동일하면 `true`, 
다르면 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

### before

```java
public boolean before(Object when)
```

**Parameters:**
- `when` - 이 달력과 비교되는 달력

**Returns:**
- 이 달력의 현재 시간이 when 달력의 시간보다 빠르면 true, 
그렇지 않으면 false

### after

```java
public boolean after(Object when)
```

**Parameters:**
- `when` - 이 달력과 비교되는 달력

**Returns:**
- 이 달력의 현재 시간이 when 달력의 시간보다 늦으면 true, 
그렇지 않으면 false

### setTimeZone

```java
public void setTimeZone(TimeZone value)
```

**Parameters:**
- `value` - 지정된 표준 시간대

**See Also:**
- ``getTimeZone()``

### getTimeZone

```java
public TimeZone getTimeZone()
```

**Returns:**
- 이 달력에 연결된 표준 시간대 객체

**See Also:**
- ``setTimeZone(java.util.TimeZone)``

### computeFields

```java
protected abstract void computeFields()
```

현재 밀리초 시간 값인 time 을 fields[] 의 
필드 값으로 변환합니다. 
이렇게 하면 시간 필드 값을 달력에 설정된 
새 값과 동기화할 수 있습니다.

### computeTime

```java
protected abstract void computeTime()
```

fields[] 의 현재 필드 값을 밀리초 
시간 값인 time 으로 
변환합니다.
