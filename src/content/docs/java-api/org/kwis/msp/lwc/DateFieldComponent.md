---
title: "Class DateFieldComponent"
---

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.DateFieldComponent
```

## 설명

**extends Component:**

`DateFieldComponent`는 날짜와 시간을 보여주는 필드를 화면에 표시해주고
 이 값을 수정할 수 있습니다.

`DateFieldComponent`를 생성할 때 지정한 모드에 관계없이 시스템에 설정된
 기본 ``TimeZone``과 ``Date``를 사용하여 현재 시간과
 날짜로 초기화된 데이타를 가지게 됩니다. 이 값은 `getDate,setDate`를 통해서
 값을 얻어오거나 수정할 수 있습니다.

`DateFieldComponent`의 날짜와 시간은 지정한 모드에 따라 화면에 출력되고
 그 값을 방향키 입력에 의해서 수정할 수 있습니다.

`DateFieldComponent`에서는 시간과 날짜를 지정하거나 수정 할 수 있는
 3가지 타입의 모드를 제공합니다.

- ``MODE_TIME``는 시간을 보여주는 필드를 화면에 출력하고 시간을 수정할 수
 있습니다.
- ``MODE_DATE``는 날짜을 보여주는 필드를 화면에 출력하고 날짜를
 수정할 수 있습니다.
- ``MODE_TIME_DATE``는 날짜와 시간을 보여주는 필드를 화면에
 출력하고 각 시간과 날짜를 수정할 수 있습니다.

**See Also:**
- ``Date``, 
``Calendar``, 
``TimeZone``

## 필드 요약

- `static int MODE_DATE` — 날자 표시모드.
- `static int MODE_TIME` — 시간 표시모드.
- `static int MODE_TIME_DATE` — 날자와 시간 표시모드.

## 생성자 요약

- DateFieldComponent (int mode) 시스템의 기본 TimeZone 과 Date 를 사용하여
 현재 시간과 날짜로 초기화된 DateFieldComponent 의 인스턴스를
 생성합니다.

## 메서드 요약

- `Date getDate ()` — DateFieldComponent 에서 현재 설정되어 있는 날짜 정보를 가지고 있는 Date 객체를 얻어옵니다.
- `int getMode ()` — DateFieldComponent 에 설정된 모드를 얻어 옵니다.
- `int getPreferredHeight ()` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredHeight (int w)` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredWidth ()` — 컴포넌트의 적절한 폭을 결정합니다.
- `String getStringValue (int mode)` — 인자로 주어진 모드값에 따라 날짜나 시간 값을 스트링 형태로 얻어 옵니다.
- `TimeZone getTimeZone ()` — DateFieldComponent 에 설정되어 있는 TimeZone 을 얻어 옵니다.
- `boolean keyNotify (int type, int key)` — 키 입력을 받으면 호출됩니다.
- `void paintContent ( Graphics g)` — 내부를 칠합니다.
- `void setDate ( Date dt)` — DateFieldComponent 에 Date 를 설정합니다.
- `void setMode (int mode)` — DateFieldComponent 의 모드를 설정합니다.
- `void setTimeZone ( TimeZone tz)` — DateFieldComponent 의 TimeZone 을 설정합니다.
- `protected  void showNotify (boolean bShow)` — 화면의 내용이 보이면 호출됩니다.

## 필드 상세

### MODE_TIME

```java
public static final int MODE_TIME
```

- 시간 표시모드.
 이 모드를 사용하면 `DateFieldComponent`에서는 시간을 보여주는
 필드를 화면에 출력하고 시간을 수정할 수 있습니다.
 

`MODE_TIME`값으로 '0'이 지정되어 있습니다.

### MODE_DATE

```java
public static final int MODE_DATE
```

- 날자 표시모드.
 이 모드를 사용하면 `DateFieldComponent`에서는 날짜를 보여주는 필드를
 화면에 출력하고 날짜를 수정할 수 있습니다.
 

`MODE_DATE`값으로 '1'이 지정되어 있습니다.

### MODE_TIME_DATE

```java
public static final int MODE_TIME_DATE
```

- 날자와 시간 표시모드.
 이 모드를 사용하면 `DateFieldComponent`에서는 시간과 날짜을
 보여주는 필드를 화면에 출력하고 시간과 날짜를 수정할 수 있습니다.
 

`MODE_TIME_DATE`값으로 '2'이 지정되어 있습니다.

### DateFieldComponent

```java
public DateFieldComponent(int mode)
```

**Parameters:**
- `mode` - 생성할 `DateFieldComponent`의 모드값

**Throws:**
- `IllegalArgumentException` - 선언된 3가지모드 -
 `MODE_TIME,MODE_DATE,MODE_DATE`- 외의 값을 지정한 경우

**See Also:**
- ``MODE_TIME``, 
``MODE_DATE``, 
``MODE_TIME_DATE``, 
``TimeZone``, 
``Date``

### getDate

```java
public Date getDate()
```

**See Also:**
- ``setDate(Date dt)``, 
``Date``

### getMode

```java
public int getMode()
```

**See Also:**
- ``setMode(int mode)``

### getTimeZone

```java
public TimeZone getTimeZone()
```

**Returns:**
- `DateFieldComponent`에 설정된 `TimeZone`

**See Also:**
- ``setTimeZone(TimeZone tz)``, 
``TimeZone``

### showNotify

```java
protected void showNotify(boolean bShow)
```

- **Description copied from class: `Component`**

**Overrides:**
- `showNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `bShow` - 컴포넌트가 나타나는지 안나타나는지 여부

### setDate

```java
public void setDate(Date dt)
```

**Parameters:**
- `dt` - `DateFieldComponent`에 설정할 Date객체

**Throws:**
- `NullPointerException` - Date가 null인경우

**See Also:**
- ``getDate()``, 
``Date``

### setMode

```java
public void setMode(int mode)
```

**Parameters:**
- `mode` - `DateFieldComponent`에 설정할 모드

**Throws:**
- `IllegalArgumentException` - 지정된 모드외의 값이 인자로 주어진 경우

**See Also:**
- ``getMode()``, 
``MODE_TIME``, 
``MODE_DATE``, 
``MODE_TIME_DATE``

### setTimeZone

```java
public void setTimeZone(TimeZone tz)
```

**Parameters:**
- `tz` - `DateFieldComponent`에 설정할 `TimeZone`

**Throws:**
- `NullPointerException` - TimeZone이 null인경우

**See Also:**
- ``getTimeZone()``, 
``TimeZone``

### getPreferredHeight

```java
public int getPreferredHeight(int w)
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `w` - 가변폭.

**Returns:**
- 컴포넌트의 높이.

### getPreferredHeight

```java
public int getPreferredHeight(int w)
```

- **Description copied from class: `Component`**
- 而댄щ

## 생성자 상세

### DateFieldComponent

```java
public DateFieldComponent(int mode)
```

**Parameters:**
- `mode` - 생성할 `DateFieldComponent`의 모드값

**Throws:**
- `IllegalArgumentException` - 선언된 3가지모드 -
 `MODE_TIME,MODE_DATE,MODE_DATE`- 외의 값을 지정한 경우

**See Also:**
- ``MODE_TIME``, 
``MODE_DATE``, 
``MODE_TIME_DATE``, 
``TimeZone``, 
``Date``

### getDate

```java
public Date getDate()
```

**See Also:**
- ``setDate(Date dt)``, 
``Date``

### getMode

```java
public int getMode()
```

**See Also:**
- ``setMode(int mode)``

### getTimeZone

```java
public TimeZone getTimeZone()
```

**Returns:**
- `DateFieldComponent`에 설정된 `TimeZone`

**See Also:**
- ``setTimeZone(TimeZone tz)``, 
``TimeZone``

### showNotify

```java
protected void showNotify(boolean bShow)
```

- **Description copied from class: `Component`**

**Overrides:**
- `showNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `bShow` - 컴포넌트가 나타나는지 안나타나는지 여부

### setDate

```java
public void setDate(Date dt)
```

**Parameters:**
- `dt` - `DateFieldComponent`에 설정할 Date객체

**Throws:**
- `NullPointerException` - Date가 null인경우

**See Also:**
- ``getDate()``, 
``Date``

### setMode

```java
public void setMode(int mode)
```

**Parameters:**
- `mode` - `DateFieldComponent`에 설정할 모드

**Throws:**
- `IllegalArgumentException` - 지정된 모드외의 값이 인자로 주어진 경우

**See Also:**
- ``getMode()``, 
``MODE_TIME``, 
``MODE_DATE``, 
``MODE_TIME_DATE``

### setTimeZone

```java
public void setTimeZone(TimeZone tz)
```

**Parameters:**
- `tz` - `DateFieldComponent`에 설정할 `TimeZone`

**Throws:**
- `NullPointerException` - TimeZone이 null인경우

**See Also:**
- ``getTimeZone()``, 
``TimeZone``

### getPreferredHeight

```java
public int getPreferredHeight(int w)
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `w` - 가변폭.

**Returns:**
- 컴포넌트의 높이.

### getPreferredHeight

```java
public int getPreferredHeight(int w)
```

- **Description copied from class: `Component`**
- 而댄щ

## 메서드 상세

### getDate

```java
public Date getDate()
```

**See Also:**
- ``setDate(Date dt)``, 
``Date``

### getMode

```java
public int getMode()
```

**See Also:**
- ``setMode(int mode)``

### getTimeZone

```java
public TimeZone getTimeZone()
```

**Returns:**
- `DateFieldComponent`에 설정된 `TimeZone`

**See Also:**
- ``setTimeZone(TimeZone tz)``, 
``TimeZone``

### showNotify

```java
protected void showNotify(boolean bShow)
```

- **Description copied from class: `Component`**

**Overrides:**
- `showNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `bShow` - 컴포넌트가 나타나는지 안나타나는지 여부

### setDate

```java
public void setDate(Date dt)
```

**Parameters:**
- `dt` - `DateFieldComponent`에 설정할 Date객체

**Throws:**
- `NullPointerException` - Date가 null인경우

**See Also:**
- ``getDate()``, 
``Date``

### setMode

```java
public void setMode(int mode)
```

**Parameters:**
- `mode` - `DateFieldComponent`에 설정할 모드

**Throws:**
- `IllegalArgumentException` - 지정된 모드외의 값이 인자로 주어진 경우

**See Also:**
- ``getMode()``, 
``MODE_TIME``, 
``MODE_DATE``, 
``MODE_TIME_DATE``

### setTimeZone

```java
public void setTimeZone(TimeZone tz)
```

**Parameters:**
- `tz` - `DateFieldComponent`에 설정할 `TimeZone`

**Throws:**
- `NullPointerException` - TimeZone이 null인경우

**See Also:**
- ``getTimeZone()``, 
``TimeZone``

### getPreferredHeight

```java
public int getPreferredHeight(int w)
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `w` - 가변폭.

**Returns:**
- 컴포넌트의 높이.

### getPreferredHeight

```java
public int getPreferredHeight(int w)
```

- **Description copied from class: `Component`**
- 而댄щ
