---
title: "Class DateField"
---

`package javax.microedition.lcdui`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.Item
        |
        +--javax.microedition.lcdui.DateField
```

## 설명

**extends Item:**

`DateField`는 
`Form`에 넣을 수 있는 
날짜와 시간(달력) 정보를 나타내기 위한 편집 가능한 구성 요소입니다. 
이 필드에 대한 값은 처음에 설정하거나 설정하지 않은 상태로 둘 수 있습니다. 
값이 설정되어 있지 않으면 이 필드의 UI에 분명히 표시됩니다. 
"초기화되지 않은 상태"에 대한 필드 값은 유효한 값이 아니며 
이 상태에 대한 `getDate()`는 
`null`을 반환합니다.

날짜나 시간 정보 또는 두 가지를 모두 받아들이도록 
`DateField`의 인스턴스를 구성할 수 있습니다. 
입력 모드는 이 클래스의 `DATE`, `TIME` 또는 
`DATE_TIME` 정적 필드로 구성됩니다. 
`DATE` 입력 모드를 사용하면 
날짜 정보만 설정할 수 있으며 
`TIME` 입력 모드를 사용하면 시간 정보(시, 분)만 
설정할 수 있지만 `DATE_TIME`을 사용하면 
시간과 날짜 값을 모두 설정할 수 있습니다.

`TIME` 입력 모드에서 `Date` 
객체의 날짜 구성 요소는 1970년 1월 1일을 "원년" 값으로 
설정해야 합니다.

이 필드의 달력 계산은 기본 로켈 및 정의된 표준 시간대를 
기반으로 합니다. 계산 및 다양한 입력 모드로 인해 날짜 객체를 
이 필드로 설정한 다음 이 필드에서 값을 다시 가져오면 같은 
밀리초 값을 포함하지 않습니다.

**Since:**
- MIDP 1.0

## 필드 요약

- `static int DATE` — 날짜 정보(년, 월, 일)에 대한 입력 모드.
- `static int DATE_TIME` — 날짜(년, 월, 일) 및 시간(시, 분) 정보에 대한 입력 모드.
- `static int TIME` — 시간 정보(시, 분)에 대한 입력 모드.

## 생성자 요약

- DateField ( String label,
 int mode) 지정된 레이블과 모드를 사용하여 DateField 객체를 만듭니다.
- DateField ( String label,
 int mode, TimeZone timeZone) 특정 TimeZone 객체 및 현재 로켈의 
기본 달력 시스템을 기반으로 달력을 
계산하는 날짜 필드를 만듭니다.

## 메서드 요약

- `Date getDate ()` — 이 필드의 날짜 값을 반환합니다.
- `int getInputMode ()` — 이 날짜 필드의 입력 모드를 가져옵니다.
- `void setDate ( Date date)` — 이 필드에 새 값을 설정합니다.
- `void setInputMode (int mode)` — 이 날짜 필드의 입력 모드를 설정합니다.

## 필드 상세

### DATE

```java
public static final int DATE
```

**See Also:**
- `Constant Field Values`

### TIME

```java
public static final int TIME
```

**See Also:**
- `Constant Field Values`

### DATE_TIME

```java
public static final int DATE_TIME
```

**See Also:**
- `Constant Field Values`

### DateField

```java
public DateField(String label,
                 int mode)
```

- 지정된 레이블과 모드를 사용하여 `DateField` 
객체를 만듭니다. 
이 호출은 `DateField(label, mode, null)`에 대한 호출과 동일합니다.

**Parameters:**
- `mode` - 입력 모드, `DATE`, `TIME`, 
`DATE_TIME` 중 하나

**Throws:**
- `IllegalArgumentException` - 입력 `mode` 값이 
유효하지 않은 경우

### DateField

```java
public DateField(String label,
                 int mode,
                 TimeZone timeZone)
```

- 특정 `TimeZone` 객체 및 현재 로켈의 
기본 달력 시스템을 기반으로 달력을 
계산하는 날짜 필드를 만듭니다. 
`DateField`의 값은 
처음에는 "초기화되지 않은" 
상태에 있습니다. 
`timeZone`이 `null`인 경우 
시스템의 기본 표준 시간대가 사용됩니다.

**Parameters:**
- `timeZone` - 특정 표준 시간대, 또는 기본 표준 시간대에 대해서는 
`null`

**Throws:**
- `IllegalArgumentException` - 입력 `mode`의 값이 
유효하지 않은 경우

### getDate

```java
public Date getDate()
```

**Returns:**
- 입력 모드에 따라 시간이나 날짜를 나타내는 날짜 객체

**See Also:**
- ``setDate(java.util.Date)``

### setDate

```java
public void setDate(Date date)
```

**Parameters:**
- `date` - 이 필드의 새 값

**See Also:**
- ``getDate()``

### getInputMode

```java
public int getInputMode()
```

**Returns:**
- 이 필드의 입력 모드

**See Also:**
- ``setInputMode(int)``

### setInputMode

```java
public void setInputMode(int mode)
```

**Parameters:**
- `mode` - 입력 모드는 `DATE`, `TIME`, 
`DATE_TIME` 중 하나여야 합니다.

**Throws:**
- `IllegalArgumentException` - 유효하지 않은 값이 지정된 경우

**See Also:**
- ``getInputMode()``

## 생성자 상세

### DateField

```java
public DateField(String label,
                 int mode)
```

- 지정된 레이블과 모드를 사용하여 `DateField` 
객체를 만듭니다. 
이 호출은 `DateField(label, mode, null)`에 대한 호출과 동일합니다.

**Parameters:**
- `mode` - 입력 모드, `DATE`, `TIME`, 
`DATE_TIME` 중 하나

**Throws:**
- `IllegalArgumentException` - 입력 `mode` 값이 
유효하지 않은 경우

### DateField

```java
public DateField(String label,
                 int mode,
                 TimeZone timeZone)
```

- 특정 `TimeZone` 객체 및 현재 로켈의 
기본 달력 시스템을 기반으로 달력을 
계산하는 날짜 필드를 만듭니다. 
`DateField`의 값은 
처음에는 "초기화되지 않은" 
상태에 있습니다. 
`timeZone`이 `null`인 경우 
시스템의 기본 표준 시간대가 사용됩니다.

**Parameters:**
- `timeZone` - 특정 표준 시간대, 또는 기본 표준 시간대에 대해서는 
`null`

**Throws:**
- `IllegalArgumentException` - 입력 `mode`의 값이 
유효하지 않은 경우

### getDate

```java
public Date getDate()
```

**Returns:**
- 입력 모드에 따라 시간이나 날짜를 나타내는 날짜 객체

**See Also:**
- ``setDate(java.util.Date)``

### setDate

```java
public void setDate(Date date)
```

**Parameters:**
- `date` - 이 필드의 새 값

**See Also:**
- ``getDate()``

### getInputMode

```java
public int getInputMode()
```

**Returns:**
- 이 필드의 입력 모드

**See Also:**
- ``setInputMode(int)``

### setInputMode

```java
public void setInputMode(int mode)
```

**Parameters:**
- `mode` - 입력 모드는 `DATE`, `TIME`, 
`DATE_TIME` 중 하나여야 합니다.

**Throws:**
- `IllegalArgumentException` - 유효하지 않은 값이 지정된 경우

**See Also:**
- ``getInputMode()``

## 메서드 상세

### getDate

```java
public Date getDate()
```

**Returns:**
- 입력 모드에 따라 시간이나 날짜를 나타내는 날짜 객체

**See Also:**
- ``setDate(java.util.Date)``

### setDate

```java
public void setDate(Date date)
```

**Parameters:**
- `date` - 이 필드의 새 값

**See Also:**
- ``getDate()``

### getInputMode

```java
public int getInputMode()
```

**Returns:**
- 이 필드의 입력 모드

**See Also:**
- ``setInputMode(int)``

### setInputMode

```java
public void setInputMode(int mode)
```

**Parameters:**
- `mode` - 입력 모드는 `DATE`, `TIME`, 
`DATE_TIME` 중 하나여야 합니다.

**Throws:**
- `IllegalArgumentException` - 유효하지 않은 값이 지정된 경우

**See Also:**
- ``getInputMode()``
