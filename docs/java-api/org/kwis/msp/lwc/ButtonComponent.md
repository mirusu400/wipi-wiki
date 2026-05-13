# Class ButtonComponent

`package org.kwis.msp.lwc`

```
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.ButtonComponent
```

## 설명

**extends Component:**

버튼 컴포넌트.

 "select"키가 눌렸다 떼어 졌을 때 자신에게 등록된
 `ActionListener`를 호출합니다.
 버튼은 문자열과 이미지 두개로 구성됩니다.

Fields inherited from class org.kwis.msp.lwc. Component bg , evtListener , evtListenerObj , fg , FOCUS_NOTIFY , h , HAS_FOCUS_MASK , INPUT_MASK , KEY_NOTIFY , KEY_PRESSED , KEY_RELEASED , KEY_REPEATED , KEY_TYPED , LAYOUT_BOTTOM , LAYOUT_HCENTER , LAYOUT_LEFT , LAYOUT_RIGHT , LAYOUT_TOP , LAYOUT_VCENTER , mask , parent , POINT_DRAGGED , POINT_PRESSED , POINT_RELEASED , POINTER_NOTIFY , POS_MASK , PREFER_SIZE_MASK , prefH , prefW , SHOW_NOTIFY , SIZE_MASK , VALID_MASK , w , x , y

Constructor Summary ButtonComponent () 버튼을 생성합니다. ButtonComponent ( String str, Image img) 지정된 Image와 문자열을 버튼을 생성합니다.

Method Summary protected  void calcPreferredSize (int w) 컴포넌트의 적절한 크기를 계산합니다. Font getFont () 폰트를 돌려줍니다. Image getImage () 현재 버튼의 이미지를 돌려줍니다. String getString () 현재 버튼의 문자열을 돌려줍니다. boolean keyNotify (int type,
 int chr) 키 입력을 받으면 호출됩니다. protected  void layout () 하위 컴포넌트의 크기와 위치를 결정합니다. void paintContent ( Graphics g) 내부를 칠합니다. void setActionListener ( ActionListener l, Object o) ActionListener 를 등록합니다. void setFont ( Font ft) 버튼의 폰트를 설정합니다. void setImage ( Image img) 버튼의 이미지을 지정합니다. void setString ( String str) 버튼의 문자열을 지정합니다.

Methods inherited from class org.kwis.msp.lwc. Component canHandleInput , configure , focusNotify , getBackground , getCard , getForeground , getHeight , getPreferredHeight , getPreferredHeight , getPreferredWidth , getWidth , getX , getXOnScreen , getY , getYOnScreen , hasFocus , invalidate , isShown , isValid , pointerNotify , processEvent , repaint , repaint , serviceRepaints , setBackground , setEventListener , setFocus , setForeground , showNotify , toString , validate

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , wait , wait , wait

Constructor Detail

### ButtonComponent

- 버튼을 생성합니다.

### ButtonComponent

**Parameters:**
- `img` - 버튼의 이미지

Method Detail

### setFont

**Parameters:**
- `ft` - 지정할 폰트

### getFont

**Returns:**
- 지정된 폰트

### setActionListener

**Parameters:**
- `o` - 불려질때 넘겨질 인수

**See Also:**
- ``ActionListener.action(org.kwis.msp.lwc.Component, java.lang.Object)``

### keyNotify

- **Description copied from class: `Component`**

**Overrides:**
- `keyNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며
 이외의 문자도 넘어 올 수 있습니다.

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 키를 이 컴포넌트가 처리했다면,
 `true`를 넘겨 줍니다. 그렇지 않았다면 `false`를
 돌려줍니다.

### setString

**Parameters:**
- `str` - 지정할 문자열

### getString

**Returns:**
- 현재 버튼의 문자열

### getImage

**Returns:**
- 버튼의 이미지

### setImage

**Parameters:**
- `img` - 지정할 이미지

### paintContent

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `g` - 칠할 Graphics.

**See Also:**
- ``Graphics``

### layout

- **Description copied from class: `Component`**

**Overrides:**
- `layout` in class `Component`

### calcPreferredSize

- **Description copied from class: `Component`**

**Overrides:**
- `calcPreferredSize` in class `Component`## 생성자 요약

- ButtonComponent () 버튼을 생성합니다.
- ButtonComponent ( String str, Image img) 지정된 Image와 문자열을 버튼을 생성합니다.

## 메서드 요약

- `protected  void calcPreferredSize (int w)` — 컴포넌트의 적절한 크기를 계산합니다.
- `Font getFont ()` — 폰트를 돌려줍니다.
- `Image getImage ()` — 현재 버튼의 이미지를 돌려줍니다.
- `String getString ()` — 현재 버튼의 문자열을 돌려줍니다.
- `boolean keyNotify (int type, int chr)` — 키 입력을 받으면 호출됩니다.
- `protected  void layout ()` — 하위 컴포넌트의 크기와 위치를 결정합니다.
- `void paintContent ( Graphics g)` — 내부를 칠합니다.
- `void setActionListener ( ActionListener l, Object o)` — ActionListener 를 등록합니다.
- `void setFont ( Font ft)` — 버튼의 폰트를 설정합니다.
- `void setImage ( Image img)` — 버튼의 이미지을 지정합니다.
- `void setString ( String str)` — 버튼의 문자열을 지정합니다.

## 생성자 상세

### ButtonComponent

```java
public ButtonComponent()
```

- 버튼을 생성합니다.

### ButtonComponent

```java
public ButtonComponent(String str,
                       Image img)
```

**Parameters:**
- `img` - 버튼의 이미지

### setFont

```java
public void setFont(Font ft)
```

**Parameters:**
- `ft` - 지정할 폰트

### getFont

```java
public Font getFont()
```

**Returns:**
- 지정된 폰트

### setActionListener

```java
public void setActionListener(ActionListener l,
                              Object o)
```

**Parameters:**
- `o` - 불려질때 넘겨질 인수

**See Also:**
- ``ActionListener.action(org.kwis.msp.lwc.Component, java.lang.Object)``

### keyNotify

```java
public boolean keyNotify(int type,
                         int chr)
```

- **Description copied from class: `Component`**

**Overrides:**
- `keyNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며
 이외의 문자도 넘어 올 수 있습니다.

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 키를 이 컴포넌트가 처리했다면,
 `true`를 넘겨 줍니다. 그렇지 않았다면 `false`를
 돌려줍니다.

### setString

```java
public void setString(String str)
```

**Parameters:**
- `str` - 지정할 문자열

### getString

```java
public String getString()
```

**Returns:**
- 현재 버튼의 문자열

### getImage

```java
public Image getImage()
```

**Returns:**
- 버튼의 이미지

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - 지정할 이미지

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

### layout

```java
protected void layout()
```

- **Description copied from class: `Component`**

**Overrides:**
- `layout` in class `Component`

### calcPreferredSize

```java
protected void calcPreferredSize(int w)
```

- **Description copied from class: `Component`**

**Overrides:**
- `calcPreferredSize` in class `Component`## 메서드 상세

### setFont

```java
public void setFont(Font ft)
```

**Parameters:**
- `ft` - 지정할 폰트

### getFont

```java
public Font getFont()
```

**Returns:**
- 지정된 폰트

### setActionListener

```java
public void setActionListener(ActionListener l,
                              Object o)
```

**Parameters:**
- `o` - 불려질때 넘겨질 인수

**See Also:**
- ``ActionListener.action(org.kwis.msp.lwc.Component, java.lang.Object)``

### keyNotify

```java
public boolean keyNotify(int type,
                         int chr)
```

- **Description copied from class: `Component`**

**Overrides:**
- `keyNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며
 이외의 문자도 넘어 올 수 있습니다.

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 키를 이 컴포넌트가 처리했다면,
 `true`를 넘겨 줍니다. 그렇지 않았다면 `false`를
 돌려줍니다.

### setString

```java
public void setString(String str)
```

**Parameters:**
- `str` - 지정할 문자열

### getString

```java
public String getString()
```

**Returns:**
- 현재 버튼의 문자열

### getImage

```java
public Image getImage()
```

**Returns:**
- 버튼의 이미지

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - 지정할 이미지

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

### layout

```java
protected void layout()
```

- **Description copied from class: `Component`**

**Overrides:**
- `layout` in class `Component`

### calcPreferredSize

```java
protected void calcPreferredSize(int w)
```

- **Description copied from class: `Component`**

**Overrides:**
- `calcPreferredSize` in class `Component`

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
