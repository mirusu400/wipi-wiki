# Class GregorianCalendar

`package java.util`

```
java.lang.Object
  |
  +--java.util.Calendar
        |
        +--java.util.GregorianCalendar
```

## 설명

**extends Calendar:**

그레고리안 역법을 이용한 캘랜더 클래스.

## 필드 요약

- `static int AD`
- `static int BC`

## 생성자 요약

- GregorianCalendar () 새로운 객체를 만든다.
- GregorianCalendar (int year,
 int month,
 int date) 새로운 객체를 만든다.
- GregorianCalendar ( TimeZone zone) 새로운 객체를 만든다.

## 메서드 요약

- `boolean after ( Object when)` — 현 객체에 설정된 시각와 매개변수로 넘어온 시각을 비교한다.
- `boolean before ( Object when)` — 현 객체에 설정된 시각와 매개변수로 넘어온 시각을 비교한다.
- `protected  void computeFields ()` — 캘린더 내에 년도,월,일등을 저장하는 fields 필드에 현 캘랜더가 나타내는 시각을 기준으로 계산해서 얻은 값을 저장한다.
- `protected  void computeTime ()` — 현 시각을 GMT시각으로 변환 후 time 필드에 저장한다.
- `boolean equals ( Object obj)` — 현 객체에 설정된 시각와 매개변수로 넘어온 시각을 비교한다.
- `protected  int getGreatestMinimum (int field)`
- `protected  int getLeastMaximum (int field)`
- `protected  int getMaximum (int field)`
- `protected  int getMinimum (int field)`
- `int hashCode ()` — 현 객체를 나타내기 위한 정수형의 해쉬코드를 구한다.
- `boolean isLeapYear (int year)` — 특정 연도가 윤년인지 여부를 구한다.

## 필드 상세

### BC

```java
public static final int BC
```

### AD

```java
public static final int AD
```

### GregorianCalendar

```java
public GregorianCalendar()
```

- 새로운 객체를 만든다. 사용하는 시간대는 VM에 설정된 시간대를
 사용한다.

### GregorianCalendar

```java
public GregorianCalendar(TimeZone zone)
```

**Parameters:**
- `zone` - 사용할 시간대.

### GregorianCalendar

```java
public GregorianCalendar(int year,
                         int month,
                         int date)
```

**Parameters:**
- `date` - 일.

### after

```java
public boolean after(Object when)
```

**Overrides:**
- `after` in class `Calendar`

**Parameters:**
- `when` - 비교 대상이 되는 객체이며 Calendar에서 생성된 객체.

**Returns:**
- 현 객체에 생성된 시각이 나중이면 true 아니면 false.

### before

```java
public boolean before(Object when)
```

**Overrides:**
- `before` in class `Calendar`

**Parameters:**
- `when` - 비교 대상이 되는 객체이며 Calendar에서 생성된 객체.

**Returns:**
- 현 객체에 생성된 시각이 이전이면 true 아니면 false.

### computeFields

```java
protected void computeFields()
```

- **Description copied from class: `Calendar`**

**Overrides:**
- `computeFields` in class `Calendar`

### computeTime

```java
protected void computeTime()
```

- **Description copied from class: `Calendar`**

**Overrides:**
- `computeTime` in class `Calendar`

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Calendar`

**Parameters:**
- `when` - 비교 대상이 되는 객체이며 Calendar에서 생성된 객체.

**Returns:**
- 현 객체에 생성된 시각이 같으면 true 아니면 false.

### getGreatestMinimum

```java
protected int getGreatestMinimum(int field)
```

**Overrides:**
- `getGreatestMinimum` in class `Calendar`

### getLeastMaximum

```java
protected int getLeastMaximum(int field)
```

**Overrides:**
- `getLeastMaximum` in class `Calendar`

### getMaximum

```java
protected int getMaximum(int field)
```

**Overrides:**
- `getMaximum` in class `Calendar`

### getMinimum

```java
protected int getMinimum(int field)
```

**Overrides:**
- `getMinimum` in class `Calendar`

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 정수형의 해쉬코드.

### isLeapYear

```java
public boolean isLeapYear(int year)
```

**Parameters:**
- `year` - 검토하고자 하는 년도.

**Returns:**
- 윤년이면 true 아니면 false.## 생성자 상세

### GregorianCalendar

```java
public GregorianCalendar()
```

- 새로운 객체를 만든다. 사용하는 시간대는 VM에 설정된 시간대를
 사용한다.

### GregorianCalendar

```java
public GregorianCalendar(TimeZone zone)
```

**Parameters:**
- `zone` - 사용할 시간대.

### GregorianCalendar

```java
public GregorianCalendar(int year,
                         int month,
                         int date)
```

**Parameters:**
- `date` - 일.

### after

```java
public boolean after(Object when)
```

**Overrides:**
- `after` in class `Calendar`

**Parameters:**
- `when` - 비교 대상이 되는 객체이며 Calendar에서 생성된 객체.

**Returns:**
- 현 객체에 생성된 시각이 나중이면 true 아니면 false.

### before

```java
public boolean before(Object when)
```

**Overrides:**
- `before` in class `Calendar`

**Parameters:**
- `when` - 비교 대상이 되는 객체이며 Calendar에서 생성된 객체.

**Returns:**
- 현 객체에 생성된 시각이 이전이면 true 아니면 false.

### computeFields

```java
protected void computeFields()
```

- **Description copied from class: `Calendar`**

**Overrides:**
- `computeFields` in class `Calendar`

### computeTime

```java
protected void computeTime()
```

- **Description copied from class: `Calendar`**

**Overrides:**
- `computeTime` in class `Calendar`

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Calendar`

**Parameters:**
- `when` - 비교 대상이 되는 객체이며 Calendar에서 생성된 객체.

**Returns:**
- 현 객체에 생성된 시각이 같으면 true 아니면 false.

### getGreatestMinimum

```java
protected int getGreatestMinimum(int field)
```

**Overrides:**
- `getGreatestMinimum` in class `Calendar`

### getLeastMaximum

```java
protected int getLeastMaximum(int field)
```

**Overrides:**
- `getLeastMaximum` in class `Calendar`

### getMaximum

```java
protected int getMaximum(int field)
```

**Overrides:**
- `getMaximum` in class `Calendar`

### getMinimum

```java
protected int getMinimum(int field)
```

**Overrides:**
- `getMinimum` in class `Calendar`

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 정수형의 해쉬코드.

### isLeapYear

```java
public boolean isLeapYear(int year)
```

**Parameters:**
- `year` - 검토하고자 하는 년도.

**Returns:**
- 윤년이면 true 아니면 false.## 메서드 상세

### after

```java
public boolean after(Object when)
```

**Overrides:**
- `after` in class `Calendar`

**Parameters:**
- `when` - 비교 대상이 되는 객체이며 Calendar에서 생성된 객체.

**Returns:**
- 현 객체에 생성된 시각이 나중이면 true 아니면 false.

### before

```java
public boolean before(Object when)
```

**Overrides:**
- `before` in class `Calendar`

**Parameters:**
- `when` - 비교 대상이 되는 객체이며 Calendar에서 생성된 객체.

**Returns:**
- 현 객체에 생성된 시각이 이전이면 true 아니면 false.

### computeFields

```java
protected void computeFields()
```

- **Description copied from class: `Calendar`**

**Overrides:**
- `computeFields` in class `Calendar`

### computeTime

```java
protected void computeTime()
```

- **Description copied from class: `Calendar`**

**Overrides:**
- `computeTime` in class `Calendar`

### equals

```java
public boolean equals(Object obj)
```

**Overrides:**
- `equals` in class `Calendar`

**Parameters:**
- `when` - 비교 대상이 되는 객체이며 Calendar에서 생성된 객체.

**Returns:**
- 현 객체에 생성된 시각이 같으면 true 아니면 false.

### getGreatestMinimum

```java
protected int getGreatestMinimum(int field)
```

**Overrides:**
- `getGreatestMinimum` in class `Calendar`

### getLeastMaximum

```java
protected int getLeastMaximum(int field)
```

**Overrides:**
- `getLeastMaximum` in class `Calendar`

### getMaximum

```java
protected int getMaximum(int field)
```

**Overrides:**
- `getMaximum` in class `Calendar`

### getMinimum

```java
protected int getMinimum(int field)
```

**Overrides:**
- `getMinimum` in class `Calendar`

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 정수형의 해쉬코드.

### isLeapYear

```java
public boolean isLeapYear(int year)
```

**Parameters:**
- `year` - 검토하고자 하는 년도.

**Returns:**
- 윤년이면 true 아니면 false.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
