# Class TimeZone

`package java.util`

```text
java.lang.Object
  |
  +--java.util.TimeZone
```

## 설명

**Direct Known Subclasses:**
- `SimpleTimeZone`

**extends Object:**

시간대 객체의 추상 클래스.

## 생성자 요약

- TimeZone () 새로운 객체를 생성한다.

## 메서드 요약

- `static String [] getAvailableIDs ()` — VM에서 지원가능한 TimeZone 문자열 배열을 구한다.
- `static String [] getAvailableIDs (int rawOffset)` — VM에서 지원가능하고 특정 offset도 지원하는 TimeZone 문자열 배열을 구한다.
- `static TimeZone getDefault ()` — VM에서 디폴트로 사용하는 TimeZone객체를 구한다.
- `String getID ()` — 현 객체를 나타낼 수 있는 시간대 문자열을 구한다.
- `abstract  int getOffset (int era, int year, int month, int day, int dayOfWeek, int milliseconds)` — 특정 시각에서의 GMT대상으로 한 millisecond단위의 offset을 구한다.
- `abstract  int getRawOffset ()` — 썸머 타임을 무시한 GMT기준 offset을 구한다.
- `static TimeZone getTimeZone ( String ID)` — 특정 시간대를 지원하는 TimeZone객체를 구한다.
- `static void initialize ()`
- `void setID ( String ID)` — 현 객체를 특정 시간대로 변환한다.
- `String toString ()` — 현 객체를 설명할 수 있는 문자열을 구한다.
- `abstract  boolean useDaylightTime ()` — 현 시간대가 썸머타임을 사용하는지 여부를 구한다.

## 생성자 상세

### TimeZone

```java
public TimeZone()
```

- 새로운 객체를 생성한다.

### initialize

```java
public static void initialize()
```

### getOffset

```java
public abstract int getOffset(int era,
                              int year,
                              int month,
                              int day,
                              int dayOfWeek,
                              int milliseconds)
```

**Parameters:**
- `milliseconds` - 시각.

**Returns:**
- GMT기준 offset.

### getRawOffset

```java
public abstract int getRawOffset()
```

**Returns:**
- GMT기준 offset.

### useDaylightTime

```java
public abstract boolean useDaylightTime()
```

**Returns:**
- 썸머타임을 사용하면 true 아니면 false.

### getID

```java
public String getID()
```

**Returns:**
- 시간대 문자열.

### getTimeZone

```java
public static TimeZone getTimeZone(String ID)
```

**Parameters:**
- `ID` - 시간대 문자열

**Returns:**
- TimeZone객체.

### getDefault

```java
public static TimeZone getDefault()
```

**Returns:**
- TimeZone객체.

### getAvailableIDs

```java
public static String[] getAvailableIDs()
```

**Returns:**
- VM에서 지원가능한 TimeZone 문자열 배열.

### getAvailableIDs

```java
public static String[] getAvailableIDs(int rawOffset)
```

**Parameters:**
- `rawOffset` - TimeZone이 지원해야 할 offset값.

**Returns:**
- TimeZone 문자열 배열 대상이 없으면 null.

### setID

```java
public void setID(String ID)
```

**Parameters:**
- `ID` - 변환할 시간대 문자열.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체를 설명할 수 있는 문자열.## 메서드 상세

### initialize

```java
public static void initialize()
```

### getOffset

```java
public abstract int getOffset(int era,
                              int year,
                              int month,
                              int day,
                              int dayOfWeek,
                              int milliseconds)
```

**Parameters:**
- `milliseconds` - 시각.

**Returns:**
- GMT기준 offset.

### getRawOffset

```java
public abstract int getRawOffset()
```

**Returns:**
- GMT기준 offset.

### useDaylightTime

```java
public abstract boolean useDaylightTime()
```

**Returns:**
- 썸머타임을 사용하면 true 아니면 false.

### getID

```java
public String getID()
```

**Returns:**
- 시간대 문자열.

### getTimeZone

```java
public static TimeZone getTimeZone(String ID)
```

**Parameters:**
- `ID` - 시간대 문자열

**Returns:**
- TimeZone객체.

### getDefault

```java
public static TimeZone getDefault()
```

**Returns:**
- TimeZone객체.

### getAvailableIDs

```java
public static String[] getAvailableIDs()
```

**Returns:**
- VM에서 지원가능한 TimeZone 문자열 배열.

### getAvailableIDs

```java
public static String[] getAvailableIDs(int rawOffset)
```

**Parameters:**
- `rawOffset` - TimeZone이 지원해야 할 offset값.

**Returns:**
- TimeZone 문자열 배열 대상이 없으면 null.

### setID

```java
public void setID(String ID)
```

**Parameters:**
- `ID` - 변환할 시간대 문자열.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체를 설명할 수 있는 문자열.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
