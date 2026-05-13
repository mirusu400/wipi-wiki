# Class ScrollbarComponent

`package org.kwis.msp.lwc`

```
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.ScrollbarComponent
```

## 설명

**extends Component:**

`ScrollBarComponent`는 최대,최소값을 가지고
 그 영역 내에서 값을 유동적으로 변경할 수 있는 컴포넌트입니다.

`ScrollBarComponent`에서는 좌우스크롤 `HORIZONTAL`과
 상하스크롤 `VERTICAL`의 두가지 스크롤 방향값을 제공합니다.
 이 값은 ``setDirection(int direction)``을 통해서 지정할 수 있으며,
 `HORIZONTAL`과 `VERTICAL` 이외의 값이 지정된 경우
 `IllegalArgumentException`이 발생합니다.

스크롤 바의 값은 사용자의 키입력에 따라 값이 변경될 수도 있으며 ,``setCurrentValue(int)``
 등의 메소드를 사용하여 스크롤 바의 위치 값을 변경할 수도 있습니다.

예를 들어 그림과 같은 크기값을 갖는 `ScrollbarComponent`를
 생성하려면 ````java
ScrollbarComponent(int direction, int currentValue,
 int viewAmount, int minimum, int maximum, int chAmount)
```` 생성자를 사용하고,
 아래와 같이 지정합니다.

값을 지정할 때 주의할 점은 그림에서 보듯이 현재 위치값을 지정할 수 있는 최대값은
 스크롤바의 최대값이 아니고, 스크롤바의 최대값에서 영역값을 뺀값이 현재 위치값의 최대값
 으로 지정될 수 있습니다. 스크롤바의 각 크기값은 아래의 표를 참고하시기 바랍니다.

**스크롤 크기값**

설명 기본값 영역 방향값(direction) 스크롤 방향. VERTICAL 와 HORIZONTAL 값을 지정할 수 있고 이외의 값이 지정된 경우 IllegalArgumentException 발생 VERTICAL VERTICAL HORIZONTAL 현재값(currentValue) 현재 ScrollbarComponent 의 위치값. 주의 할 점은 현재값이 실질적으로 지정될 수 있는 영역은 최대값이 아니고, 최대값과 영역값의 차이값은 최대값으로 가질 수 있습니다. 0 최소값(minimum)<=현재값(currentValue)<=(최대값(maximum)-영역값(viewAmount)) 영역값(viewAmount) ScrollbarComponent 에서 전체 영역중 현재 사용되는 영역의 크기값. 1 0 < 영역값(viewAmount) <= (최대값(maximum) - 최소값(minimum)) 최소값(minimum) ScrollbarComponent 의 최소값 0 최소(minimum)값<최대값(maximum) 최대값(maximum) ScrollbarComponent 의 최대값 10 최소(minimum)값<최대값(maximum) 증감값(chAmount) ScrollbarComponent 에서 방향키 입력이나과 같은 이동 액션이 발생하면 스크롤바가 움직이는 크기값. 1 0 < 증감값(chAmount) <= 영역값(viewAmount)

**Since:**
- qtp 1.0

## 필드 요약

- `static int HORIZONTAL` — 좌우 스크롤 방향값.
- `static int VERTICAL` — 상하 스크롤 방향값.

## 생성자 요약

- ScrollbarComponent () 스크롤 바의 인스턴스를 생성합니다.
- ScrollbarComponent (int direction) 지정한 스크롤 바의 방향값으로 스크롤 바의 인스턴스를 생성합니다.
- ScrollbarComponent (int direction,
 int currentValue,
 int viewAmount,
 int minimum,
 int maximum,
 int chAmount) 주어진 스크롤 바의 각 크기값과 스크롤 방향값을 ScrollbarComponent 의 인스턴스를 생성합니다.

## 메서드 요약

- `void focusNotify (boolean b)` — 포커스를 받으면 호출됩니다.
- `int getChangeAmount ()` — 스크롤시 증감되는 증감값의 크기를 얻어옵니다.
- `int getCurrentValue ()` — 스크롤바의 현재 위치값( currentValue )을 리턴합니다.
- `int getDirection ()` — 현재 지정된 ScrollbarComponent 의 스크롤 방향값을 리턴합니다.
- `int getForegroundColor ()` — 스크롤바의 전경색을 돌려줍니다.
- `int getMaximum ()` — 스크롤바의 최대값을 리턴합니다.
- `int getMinimum ()` — 스크롤바의 최소값을 리턴합니다.
- `int getPreferredHeight ()` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredHeight (int w)` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredWidth ()` — 컴포넌트의 적절한 폭을 결정합니다.
- `int getViewAmount ()` — 스크롤바의 영역크기값을 얻어옵니다.
- `boolean keyNotify (int type, int key)` — 키 입력을 받으면 호출됩니다.
- `void paintContent ( Graphics g)` — 내부를 칠합니다.
- `void setChangeAmount (int newChAmount)` — 스크롤시 증감되는 값의 크기를 셋팅합니다.
- `void setCurrentValue (int newValue)` — 스크롤바의 현재 위치값( currentValue )을 지정합니다.
- `void setDirection (int direction)` — 스크롤바의 스크롤 방향값을 지정합니다.
- `void setForegroundColor (int fg)` — 스크롤바의 전경색을 지정합니다.
- `void setMaximum (int newMaximum)` — 스크롤바의 최대값을 지정합니다.
- `void setMinimum (int newMinimum)` — 스크롤바의 최소값을 지정합니다.
- `void setViewAmount (int newAmount)` — 스크롤바의 영역크기값을 지정합니다.

## 필드 상세

### HORIZONTAL

```java
public static final int HORIZONTAL
```

- 좌우 스크롤 방향값. '1'값이 지정되어 있습니다.

### VERTICAL

```java
public static final int VERTICAL
```

- 상하 스크롤 방향값. '2'값이 지정되어 있습니다.

### ScrollbarComponent

```java
public ScrollbarComponent()
```

**See Also:**
- ``ScrollbarComponent(int direction)``, 
````java
ScrollbarComponent(int direction, int currentValue,
int viewAmount, int minimum, int maximum, int chAmount)
````

### ScrollbarComponent

```java
public ScrollbarComponent(int direction)
```

**Parameters:**
- `direction` - 스크롤 바의 방향값

**Throws:**
- `IllegalArgumentException` - 스크롤 바의 방향값이
 `HORIZONTAL`나 `VERTICAL` 이외의 값으로 잘못 지정된
 경우 발생.

**See Also:**
- ``ScrollbarComponent()``, 
````java
ScrollbarComponent(int direction, int currentValue,
               int viewAmount, int minimum, int maximum, int chAmount)
````

### ScrollbarComponent

```java
public ScrollbarComponent(int direction,
                          int currentValue,
                          int viewAmount,
                          int minimum,
                          int maximum,
                          int chAmount)
```

**Parameters:**
- `maximum` - 스크롤 바의 maximum값.

**Throws:**
- `IllegalArgumentException` - 각 크기값에서 오류가 발생한 경우

**See Also:**
- ``ScrollbarComponent()``, 
``ScrollbarComponent(int direction)``

### getDirection

```java
public int getDirection()
```

**Returns:**
- 스크롤의 방향값.

**See Also:**
- ``setDirection(int direction)``

### setDirection

```java
public void setDirection(int direction)
```

- 스크롤바의 스크롤 방향값을 지정합니다.
 

지정할 수 있는 스크롤 방향값은 ``HORIZONTAL``과`ScrollbarComponent()`, 
``ScrollbarComponent(int direction)``

### getDirection

```java
public int getDirection()
```

## 생성자 상세

### ScrollbarComponent

```java
public ScrollbarComponent()
```

**See Also:**
- ``ScrollbarComponent(int direction)``, 
````java
ScrollbarComponent(int direction, int currentValue,
int viewAmount, int minimum, int maximum, int chAmount)
````

### ScrollbarComponent

```java
public ScrollbarComponent(int direction)
```

**Parameters:**
- `direction` - 스크롤 바의 방향값

**Throws:**
- `IllegalArgumentException` - 스크롤 바의 방향값이
 `HORIZONTAL`나 `VERTICAL` 이외의 값으로 잘못 지정된
 경우 발생.

**See Also:**
- ``ScrollbarComponent()``, 
````java
ScrollbarComponent(int direction, int currentValue,
               int viewAmount, int minimum, int maximum, int chAmount)
````

### ScrollbarComponent

```java
public ScrollbarComponent(int direction,
                          int currentValue,
                          int viewAmount,
                          int minimum,
                          int maximum,
                          int chAmount)
```

**Parameters:**
- `maximum` - 스크롤 바의 maximum값.

**Throws:**
- `IllegalArgumentException` - 각 크기값에서 오류가 발생한 경우

**See Also:**
- ``ScrollbarComponent()``, 
``ScrollbarComponent(int direction)``

### getDirection

```java
public int getDirection()
```

**Returns:**
- 스크롤의 방향값.

**See Also:**
- ``setDirection(int direction)``

### setDirection

```java
public void setDirection(int direction)
```

- 스크롤바의 스크롤 방향값을 지정합니다.
 

지정할 수 있는 스크롤 방향값은 ``HORIZONTAL``과`ScrollbarComponent()`, 
``ScrollbarComponent(int direction)``

### getDirection

```java
public int getDirection()
```

## 메서드 상세

### getDirection

```java
public int getDirection()
```

**Returns:**
- 스크롤의 방향값.

**See Also:**
- ``setDirection(int direction)``

### setDirection

```java
public void setDirection(int direction)
```

- 스크롤바의 스크롤 방향값을 지정합니다.
 

지정할 수 있는 스크롤 방향값은 ``HORIZONTAL``과`ScrollbarComponent()`, 
``ScrollbarComponent(int direction)``

### getDirection

```java
public int getDirection()
```
