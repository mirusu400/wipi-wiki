---
title: "Class TickerComponent"
---

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.TickerComponent
```

## 설명

**extends Component:**

`TickerComponent`는 문자열과 이미지로 구성되면 우측에서 좌측으로 움직이는
 컴포넌트입니다.
 좌측으로 이동하여 문자열의 끝이 좌측으로 사라지면 다시 문자열의 처음부터 우측에서
 보여지게 되어 동일한 방향으로 이동을 계속합니다.

`TickerComponent`의 넓이 값은 `TickerComponent`를 추가한
 `ContainerComponent`의 넓이 값과 같으며, 높이는 이미지가 문자의 한 줄
 높이보다 작은 경우 한줄 높이 값을 가지며, 이미지의 높이가 더 큰 경우 이미지 높이 값을
 가지게 됩니다.

움직이는 속도는 ``setDelay(int)``메소드를 사용하여 변경할 수 있습니다.
 이 때 지정해주는 시간 값은 milleseconds 단위입니다. 기본으로 설정된 값은
 ``DEFAULT_DELAY``입니다. 움직임 속도 값은 '-'값은 지정될 수 없으며,
 '-'값이 지정된 경우 `IllegalArgumentException`이 발생됩니다.

`TickerComponent`에서는 움직임을 제어할 수 있는 기능을 제공하고
 있습니다. 움직임 상태는 ``setTickerState(boolean)``메소드를 사용하여 제어할 수 있습니다.
 `true`값이 지정되면 움직이고, `false`값이 지정되면 움직임을
 멈추게 됩니다. 기본적으로 움직임 상태에 지정된 값은 `true`입니다.

`TickerComponent`는 서로 다른 `ContainerComponent`에
 공유되어 사용될 수 없습니다.
 공유되어 사용되어질 경우 `IllegalArgumentException`이 발생됩니다.

## 필드 요약

- `int DEFAULT_DELAY` — TickerComponent 의 기본 움직임 속도값. 500 milliseconds

## 생성자 요약

- TickerComponent ( String str, Image img) TickerComponent 의 인스턴스를 생성합니다.

## 메서드 요약

- `Image getImage ()` — TickerComponent 의 이미지 데이타를 전달합니다.
- `int getPreferredHeight ()` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredHeight (int w)` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredWidth ()` — 컴포넌트의 적절한 폭을 결정합니다.
- `String getString ()` — TickerComponent 의 문자 데이타를 얻어옵니다.
- `void paintContent ( Graphics g)` — 내부를 칠합니다.
- `void setDelay (int delay)` — TickerComponent 의 문자 흐름 속도를 설정합니다.
- `void setImage ( Image img)` — TickerComponent 의 이미지 데이타를 지정합니다.
- `void setString ( String str)` — 화면에 출력될 TickerComponent 의 문자 데이타를 지정합니다.
- `boolean setTickerState (boolean st)` — TickerComponent 의 움직임/정지 상태를 설정합니다.

## 필드 상세

### DEFAULT_DELAY

```java
public int DEFAULT_DELAY
```

- `TickerComponent`의 기본 움직임 속도값.
 500` milliseconds`

### TickerComponent

```java
public TickerComponent(String str,
                       Image img)
```

**Parameters:**
- `img` - `TickerComponent`의 이미지 데이타 혹은 null

**Throws:**
- `NullPointerException` - 문자 데이타가 null인경우

### setString

```java
public void setString(String str)
```

**Parameters:**
- `str` - `TickerComponent`의 문자 데이타

**Throws:**
- `NullPointerException` - 문자데이타 str이 null인경우

**See Also:**
- ``getString()``, 
``setImage(Image img)``

### getString

```java
public String getString()
```

**Returns:**
- string TickerComponent의 문자 데이타

**See Also:**
- ``setString(String str)``

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - `TickerComponent`의 이미지 데이타.

**See Also:**
- ``getImage()``, 
``setString(String str)``

### getImage

```java
public Image getImage()
```

**Returns:**
- img `TickerComponent`의 이미지 데이타.

**See Also:**
- ``setImage(Image img)``

### setDelay

```java
public void setDelay(int delay)
```

**Parameters:**
- `delay` - 문자 속도 값.milliseconds 단위

**Throws:**
- `IllegalArgumentException` - delay값이 '-'값인경우

### setTickerState

```java
public boolean setTickerState(boolean st)
```

**Parameters:**
- `st` - `true` : 문자,이미지 움직임
 `false`: 움직임 정지.

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
public int getPreferredHeight()
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 높이

### getPreferredWidth

```java
public int getPreferredWidth()
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredWidth` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 폭.

### paintContent

```java
public void paintContent(Graphics g)
```

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `g` - 칠할 Graphics.

**See Also:**
- ``Graphics``## 생성자 상세

### TickerComponent

```java
public TickerComponent(String str,
                       Image img)
```

**Parameters:**
- `img` - `TickerComponent`의 이미지 데이타 혹은 null

**Throws:**
- `NullPointerException` - 문자 데이타가 null인경우

### setString

```java
public void setString(String str)
```

**Parameters:**
- `str` - `TickerComponent`의 문자 데이타

**Throws:**
- `NullPointerException` - 문자데이타 str이 null인경우

**See Also:**
- ``getString()``, 
``setImage(Image img)``

### getString

```java
public String getString()
```

**Returns:**
- string TickerComponent의 문자 데이타

**See Also:**
- ``setString(String str)``

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - `TickerComponent`의 이미지 데이타.

**See Also:**
- ``getImage()``, 
``setString(String str)``

### getImage

```java
public Image getImage()
```

**Returns:**
- img `TickerComponent`의 이미지 데이타.

**See Also:**
- ``setImage(Image img)``

### setDelay

```java
public void setDelay(int delay)
```

**Parameters:**
- `delay` - 문자 속도 값.milliseconds 단위

**Throws:**
- `IllegalArgumentException` - delay값이 '-'값인경우

### setTickerState

```java
public boolean setTickerState(boolean st)
```

**Parameters:**
- `st` - `true` : 문자,이미지 움직임
 `false`: 움직임 정지.

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
public int getPreferredHeight()
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 높이

### getPreferredWidth

```java
public int getPreferredWidth()
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredWidth` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 폭.

### paintContent

```java
public void paintContent(Graphics g)
```

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `g` - 칠할 Graphics.

**See Also:**
- ``Graphics``## 메서드 상세

### setString

```java
public void setString(String str)
```

**Parameters:**
- `str` - `TickerComponent`의 문자 데이타

**Throws:**
- `NullPointerException` - 문자데이타 str이 null인경우

**See Also:**
- ``getString()``, 
``setImage(Image img)``

### getString

```java
public String getString()
```

**Returns:**
- string TickerComponent의 문자 데이타

**See Also:**
- ``setString(String str)``

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - `TickerComponent`의 이미지 데이타.

**See Also:**
- ``getImage()``, 
``setString(String str)``

### getImage

```java
public Image getImage()
```

**Returns:**
- img `TickerComponent`의 이미지 데이타.

**See Also:**
- ``setImage(Image img)``

### setDelay

```java
public void setDelay(int delay)
```

**Parameters:**
- `delay` - 문자 속도 값.milliseconds 단위

**Throws:**
- `IllegalArgumentException` - delay값이 '-'값인경우

### setTickerState

```java
public boolean setTickerState(boolean st)
```

**Parameters:**
- `st` - `true` : 문자,이미지 움직임
 `false`: 움직임 정지.

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
public int getPreferredHeight()
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 높이

### getPreferredWidth

```java
public int getPreferredWidth()
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredWidth` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 폭.

### paintContent

```java
public void paintContent(Graphics g)
```

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `g` - 칠할 Graphics.

**See Also:**
- ``Graphics``

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
