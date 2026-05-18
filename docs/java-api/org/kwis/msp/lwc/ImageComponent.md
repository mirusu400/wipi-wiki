# Class ImageComponent

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.ImageComponent
```

## 설명

**extends Component:**

`ImageComponent`는 이미지데이타를 지정한 정렬형태로 화면에 출력하는
 클래스 입니다.

`ImageComponent`는 ``setLayout(int)``를 사용하여 정렬형태를 지정
 할 수 있습니다.
 `ImageComponent`에서 제공하고 있는 정렬형태는
 ``Component.LAYOUT_LEFT``와 ``Component.LAYOUT_RIGHT``,
 ``Component.LAYOUT_HCENTER``,``Component.LAYOUT_TOP``,
 ``Component.LAYOUT_BOTTOM``,``Component.LAYOUT_HCENTER``입니다.

 `정렬 조합 규칙`을 참고하여 각 정렬형태를 조합할
 수 있습니다. `ImageComponent`생성시 정렬 형태는
 `LAYOUT_LEFT|LAYOUT_TOP`로 초기화 됩니다.

**See Also:**
- ``Image``

## 필드 요약

- `protected Image img` — 이미지
- `protected String imgStr` — 이미지 리소스

## 생성자 요약

- ImageComponent () 새로운 ImageComponent 의 인스턴스를 생성합니다.
- ImageComponent ( Image img) 새로운 ImageComponent 의 인스턴스를 생성합니다.
- ImageComponent ( String str) 새로운 ImageComponent 의 인스턴스를 생성합니다.

## 메서드 요약

- `Image getImage ()` — ImageComponent 에 설정된 이미지를 얻어옵니다.
- `int getPreferredHeight ()` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredHeight (int w)` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredWidth ()` — 컴포넌트의 적절한 폭을 결정합니다.
- `void paintContent ( Graphics g)` — 내부를 칠합니다.
- `void play ()` — ImageComponent 의 이미지 데이타가 Animation Image 인 경우에 이 함수가 사용될 수 있으며 이미지의 움직임을 시작합니다.
- `void setImage ( Image img)` — ImageComponent 에 이미지를 설정합니다.
- `void setImage ( String str)` — ImageComponent 에 주어진 이미지 리소스을 가지고 이미지를 생성하여 설정합니다.
- `void setLayout (int layout)` — 이미지의 정렬형태를 설정합니다.
- `protected  void showNotify (boolean bShow)` — 화면의 내용이 보이면 호출됩니다.
- `void stop ()` — ImageComponent 의 이미지 데이타가 Animation Image 인 경우에 이 함수가 사용되며, 이미지의 움직임을 멈춥니다.

## 필드 상세

### imgStr

```java
protected String imgStr
```

- 이미지 리소스

### img

```java
protected Image img
```

- 이미지

### ImageComponent

```java
public ImageComponent()
```

- 새로운 `ImageComponent`의 인스턴스를 생성합니다.
 이미지 데이타는 `null`로 초기화 됩니다.

### ImageComponent

```java
public ImageComponent(Image img)
```

**Parameters:**
- `img` - 초기값으로 사용할 이미지 혹은 `null`

### ImageComponent

```java
public ImageComponent(String str)
```

**Parameters:**
- `str` - 초기값으로 사용할 이미지의 리소스 혹은 `null`

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - 설정할 이미지

### getImage

```java
public Image getImage()
```

**Returns:**
- 설정된 이미지

### setImage

```java
public void setImage(String str)
```

**Parameters:**
- `str` - 자료의 경로명을 지정하는 문자열

**Throws:**
- `IllegalArgumentException` - 자료의 경로명이 null인경우

### setLayout

```java
public void setLayout(int layout)
```

**Parameters:**
- `type` - Layout Type값.

**See Also:**
- ``Component.LAYOUT_LEFT``, 
``Component.LAYOUT_RIGHT``, 
``Component.LAYOUT_HCENTER``, 
``Component.LAYOUT_TOP``, 
``Component.LAYOUT_BOTTOM``, 
``Component.LAYOUT_VCENTER``

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

### play

```java
public void play()
```

- `ImageComponent`의 이미지 데이타가 `Animation Image`
 인 경우에 이 함수가 사용될 수 있으며 이미지의 움직임을 시작합니다.
 

```java
Animation이 진행되는 동안 ImageObserver에 animation 진행 상황을
 ImageObserver의 notify()함수를 호출함으로써 알려줍니다.
 Animation 이미지가 아닌 경우에 이 함수는 아무런 작업도 하지
 않습니다
```

### stop

```java
public void stop()
```

- `ImageComponent`의 이미지 데이타가 `Animation Image`
 인 경우에 이 함수가 사용되며, 이미지의 움직임을 멈춥니다.
 `Animation Image`가 아닌 경우에 아무런 작업도 하지 않습니다.
 이미지를 더이상 사용하지 않으면 이 함수를 불러서 이미지의 레퍼런스를 없애야 합니다.
 그렇지 않으면, 사용하지 않은 이미지 레퍼런스를 가지게 되므로, 메모리를 낭비할 수
 있습니다.

## 생성자 상세

### ImageComponent

```java
public ImageComponent()
```

- 새로운 `ImageComponent`의 인스턴스를 생성합니다.
 이미지 데이타는 `null`로 초기화 됩니다.

### ImageComponent

```java
public ImageComponent(Image img)
```

**Parameters:**
- `img` - 초기값으로 사용할 이미지 혹은 `null`

### ImageComponent

```java
public ImageComponent(String str)
```

**Parameters:**
- `str` - 초기값으로 사용할 이미지의 리소스 혹은 `null`

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - 설정할 이미지

### getImage

```java
public Image getImage()
```

**Returns:**
- 설정된 이미지

### setImage

```java
public void setImage(String str)
```

**Parameters:**
- `str` - 자료의 경로명을 지정하는 문자열

**Throws:**
- `IllegalArgumentException` - 자료의 경로명이 null인경우

### setLayout

```java
public void setLayout(int layout)
```

**Parameters:**
- `type` - Layout Type값.

**See Also:**
- ``Component.LAYOUT_LEFT``, 
``Component.LAYOUT_RIGHT``, 
``Component.LAYOUT_HCENTER``, 
``Component.LAYOUT_TOP``, 
``Component.LAYOUT_BOTTOM``, 
``Component.LAYOUT_VCENTER``

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

### play

```java
public void play()
```

- `ImageComponent`의 이미지 데이타가 `Animation Image`
 인 경우에 이 함수가 사용될 수 있으며 이미지의 움직임을 시작합니다.
 

```java
Animation이 진행되는 동안 ImageObserver에 animation 진행 상황을
 ImageObserver의 notify()함수를 호출함으로써 알려줍니다.
 Animation 이미지가 아닌 경우에 이 함수는 아무런 작업도 하지
 않습니다
```

### stop

```java
public void stop()
```

- `ImageComponent`의 이미지 데이타가 `Animation Image`
 인 경우에 이 함수가 사용되며, 이미지의 움직임을 멈춥니다.
 `Animation Image`가 아닌 경우에 아무런 작업도 하지 않습니다.
 이미지를 더이상 사용하지 않으면 이 함수를 불러서 이미지의 레퍼런스를 없애야 합니다.
 그렇지 않으면, 사용하지 않은 이미지 레퍼런스를 가지게 되므로, 메모리를 낭비할 수
 있습니다.

## 메서드 상세

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - 설정할 이미지

### getImage

```java
public Image getImage()
```

**Returns:**
- 설정된 이미지

### setImage

```java
public void setImage(String str)
```

**Parameters:**
- `str` - 자료의 경로명을 지정하는 문자열

**Throws:**
- `IllegalArgumentException` - 자료의 경로명이 null인경우

### setLayout

```java
public void setLayout(int layout)
```

**Parameters:**
- `type` - Layout Type값.

**See Also:**
- ``Component.LAYOUT_LEFT``, 
``Component.LAYOUT_RIGHT``, 
``Component.LAYOUT_HCENTER``, 
``Component.LAYOUT_TOP``, 
``Component.LAYOUT_BOTTOM``, 
``Component.LAYOUT_VCENTER``

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

### play

```java
public void play()
```

- `ImageComponent`의 이미지 데이타가 `Animation Image`
 인 경우에 이 함수가 사용될 수 있으며 이미지의 움직임을 시작합니다.
 

```java
Animation이 진행되는 동안 ImageObserver에 animation 진행 상황을
 ImageObserver의 notify()함수를 호출함으로써 알려줍니다.
 Animation 이미지가 아닌 경우에 이 함수는 아무런 작업도 하지
 않습니다
```

### stop

```java
public void stop()
```

- `ImageComponent`의 이미지 데이타가 `Animation Image`
 인 경우에 이 함수가 사용되며, 이미지의 움직임을 멈춥니다.
 `Animation Image`가 아닌 경우에 아무런 작업도 하지 않습니다.
 이미지를 더이상 사용하지 않으면 이 함수를 불러서 이미지의 레퍼런스를 없애야 합니다.
 그렇지 않으면, 사용하지 않은 이미지 레퍼런스를 가지게 되므로, 메모리를 낭비할 수
 있습니다.
