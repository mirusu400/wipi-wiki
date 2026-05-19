---
title: "Class LabelComponent"
---

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.LabelComponent
```

## 설명

**Direct Known Subclasses:**
- `CheckboxComponent`, `ListItemComponent`

**extends Component:**

문자열을 보여주는 컴포넌트 입니다.

 사용자에게 보여줄때 문자열과 이미지를 포맷팅해서 출력해 줍니다.

 `LabelComponent`는 ``setLayout(int)``를 사용하여 정렬형태를 지정
 할 수 있습니다.
 `LabelComponent`에서 사용되는 정렬형태는 ``Component``에서 제공하는
 `정렬 조합 규칙`을 참조하고 있습니다.
 `LabelComponent`생성시 기본 정렬 형태는 `LAYOUT_LEFT`입니다.
 문자열이나 이미지는 `null`이 될 수도 있습니다.

## 필드 요약

- `protected  int layout` — LabelComoponent 의 정렬형태.
- `protected Font m_ft` — 문자 데이타에서 사용하는 폰트
- `protected Image m_image` — 이미지 데이타
- `protected String m_str` — 문자 데이타

## 생성자 요약

- LabelComponent () 레이블 컴포넌트를 생성합니다.
- LabelComponent ( String str) 주어진 문자열로 레이블 컴포넌트를 생성합니다.
- LabelComponent ( String str, Image img) 주어진 문자열과 이미지 데이타로 레이블 컴포넌트를 생성합니다.
- LabelComponent ( String str, String imgString) 주어진 문자열과 지정한 자원에서 읽어들이는 이미지 데이타로 레이블 컴포넌트를
 생성합니다.

## 메서드 요약

- `protected  void calcPreferredSize (int cw)` — 컴포넌트의 적절한 크기를 계산합니다.
- `Font getFont ()` — 폰트를 얻어옵니다.
- `Image getImage ()` — 내부 이미지를 가져옵니다.
- `String getLabel ()` — 내부 문자열을 가져옵니다.
- `void paintContent ( Graphics g)` — 내부를 칠합니다.
- `void setFont ( Font ft)` — 폰트를 지정합니다.
- `void setImage ( Image img)` — 내부 이미지을 주어진 이미지로 지정합니다.
- `void setLabel ( String str)` — 내부 문자열을 주어진 문자열값으로 지정합니다.
- `void setLayout (int layout)` — 레이블의 정렬 형태를 지정합니다.

## 필드 상세

### layout

```java
protected int layout
```

- `LabelComoponent`의 정렬형태.
 기본 정렬형태는 ``Component.LAYOUT_LEFT``입니다.

### m_ft

```java
protected Font m_ft
```

- 문자 데이타에서 사용하는 폰트

### m_str

```java
protected String m_str
```

- 문자 데이타

### m_image

```java
protected Image m_image
```

- 이미지 데이타

### LabelComponent

```java
public LabelComponent()
```

- 레이블 컴포넌트를 생성합니다.
 문자열과 이미지는 모두 `null`로 지정되며, 기본 정렬형태는
 `LAYOUT_LEFT`입니다.

### LabelComponent

```java
public LabelComponent(String str)
```

**Parameters:**
- `str` - 레이블 컴포넌트가 보여줄 문자열 혹은 `null`

### LabelComponent

```java
public LabelComponent(String str,
                      Image img)
```

**Parameters:**
- `img` - 이미지 혹은 `null`

### LabelComponent

```java
public LabelComponent(String str,
                      String imgString)
```

**Parameters:**
- `imgString` - 이미지 자원의 경로명을 나타내는 문자열 혹은 `null`

### setLabel

```java
public void setLabel(String str)
```

**Parameters:**
- `str` - 변경할 문자열 혹은 `null`

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - 변경할 이미지 혹은 `null`

### getLabel

```java
public String getLabel()
```

**Returns:**
- 내부 출력 문자열

### getImage

```java
public Image getImage()
```

**Returns:**
- 내부 출력 이미지

### setFont

```java
public void setFont(Font ft)
```

**Parameters:**
- `ft` - 사용자 폰트

### getFont

```java
public Font getFont()
```

**Returns:**
- 설정된 폰트

### calcPreferredSize

```java
protected void calcPreferredSize(int cw)
```

- **Description copied from class: `Component`**

**Overrides:**
- `calcPreferredSize` in class `Component`

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

### setLayout

```java
public void setLayout(int layout)
```

**Parameters:**
- `type` - 정렬 형태

**Throws:**
- `IllegalArgumentException` - 컴포넌트에 정의된 정렬 형태 외의 값을 지정한
 경우 발생

**See Also:**
- ``Component.LAYOUT_LEFT``, 
``Component.LAYOUT_RIGHT``, 
``Component.LAYOUT_HCENTER``, 
``Component.LAYOUT_TOP``, 
`Component#LYAOUT_VCENTER`, 
``Component.LAYOUT_BOTTOM``## 생성자 상세

### LabelComponent

```java
public LabelComponent()
```

- 레이블 컴포넌트를 생성합니다.
 문자열과 이미지는 모두 `null`로 지정되며, 기본 정렬형태는
 `LAYOUT_LEFT`입니다.

### LabelComponent

```java
public LabelComponent(String str)
```

**Parameters:**
- `str` - 레이블 컴포넌트가 보여줄 문자열 혹은 `null`

### LabelComponent

```java
public LabelComponent(String str,
                      Image img)
```

**Parameters:**
- `img` - 이미지 혹은 `null`

### LabelComponent

```java
public LabelComponent(String str,
                      String imgString)
```

**Parameters:**
- `imgString` - 이미지 자원의 경로명을 나타내는 문자열 혹은 `null`

### setLabel

```java
public void setLabel(String str)
```

**Parameters:**
- `str` - 변경할 문자열 혹은 `null`

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - 변경할 이미지 혹은 `null`

### getLabel

```java
public String getLabel()
```

**Returns:**
- 내부 출력 문자열

### getImage

```java
public Image getImage()
```

**Returns:**
- 내부 출력 이미지

### setFont

```java
public void setFont(Font ft)
```

**Parameters:**
- `ft` - 사용자 폰트

### getFont

```java
public Font getFont()
```

**Returns:**
- 설정된 폰트

### calcPreferredSize

```java
protected void calcPreferredSize(int cw)
```

- **Description copied from class: `Component`**

**Overrides:**
- `calcPreferredSize` in class `Component`

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

### setLayout

```java
public void setLayout(int layout)
```

**Parameters:**
- `type` - 정렬 형태

**Throws:**
- `IllegalArgumentException` - 컴포넌트에 정의된 정렬 형태 외의 값을 지정한
 경우 발생

**See Also:**
- ``Component.LAYOUT_LEFT``, 
``Component.LAYOUT_RIGHT``, 
``Component.LAYOUT_HCENTER``, 
``Component.LAYOUT_TOP``, 
`Component#LYAOUT_VCENTER`, 
``Component.LAYOUT_BOTTOM``## 메서드 상세

### setLabel

```java
public void setLabel(String str)
```

**Parameters:**
- `str` - 변경할 문자열 혹은 `null`

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - 변경할 이미지 혹은 `null`

### getLabel

```java
public String getLabel()
```

**Returns:**
- 내부 출력 문자열

### getImage

```java
public Image getImage()
```

**Returns:**
- 내부 출력 이미지

### setFont

```java
public void setFont(Font ft)
```

**Parameters:**
- `ft` - 사용자 폰트

### getFont

```java
public Font getFont()
```

**Returns:**
- 설정된 폰트

### calcPreferredSize

```java
protected void calcPreferredSize(int cw)
```

- **Description copied from class: `Component`**

**Overrides:**
- `calcPreferredSize` in class `Component`

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

### setLayout

```java
public void setLayout(int layout)
```

**Parameters:**
- `type` - 정렬 형태

**Throws:**
- `IllegalArgumentException` - 컴포넌트에 정의된 정렬 형태 외의 값을 지정한
 경우 발생

**See Also:**
- ``Component.LAYOUT_LEFT``, 
``Component.LAYOUT_RIGHT``, 
``Component.LAYOUT_HCENTER``, 
``Component.LAYOUT_TOP``, 
`Component#LYAOUT_VCENTER`, 
``Component.LAYOUT_BOTTOM``

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
