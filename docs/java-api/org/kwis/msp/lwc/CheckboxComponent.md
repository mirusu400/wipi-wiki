# Class CheckboxComponent

`package org.kwis.msp.lwc`

```
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.LabelComponent
              |
              +--org.kwis.msp.lwc.CheckboxComponent
```

## 설명

**extends LabelComponent:**

`CheckboxComponent`는 개별 선택가능한 체크버튼과 라디오버튼을 만들기 위한
 클래스 입니다.

`CheckboxGroup`의 지정이 없이 생성되는 `CheckboxComponent`
 의 경우는 독립적인 체크박스로 동작하며, `CheckboxGroup`이 지정되는 경우
 같은 `CheckboxGroup`으로 묶여진 `CheckboxComponent`들은
 역여진 라디오버튼으로 동작하게 됩니다.

동일한 `CheckboxGroup`으로 묶여진 CheckBox 들은 초기 값으로 선택되지
 않은 상태로 되며, 그중 맨 처음에 추가 된것만 선택되어진 상태로 초기화 됩니다.
 이 값을 바꾸기 위해서는 `setState`를 사용하십시오.

**See Also:**
- ``CheckboxGroup``

======== INNER CLASS SUMMARY ======== 
 =========== FIELD SUMMARY ===========

Fields inherited from class org.kwis.msp.lwc. LabelComponent layout , m_ft , m_image , m_str

Fields inherited from class org.kwis.msp.lwc. Component bg , evtListener , evtListenerObj , fg , FOCUS_NOTIFY , h , HAS_FOCUS_MASK , INPUT_MASK , KEY_NOTIFY , KEY_PRESSED , KEY_RELEASED , KEY_REPEATED , KEY_TYPED , LAYOUT_BOTTOM , LAYOUT_HCENTER , LAYOUT_LEFT , LAYOUT_RIGHT , LAYOUT_TOP , LAYOUT_VCENTER , mask , parent , POINT_DRAGGED , POINT_PRESSED , POINT_RELEASED , POINTER_NOTIFY , POS_MASK , PREFER_SIZE_MASK , prefH , prefW , SHOW_NOTIFY , SIZE_MASK , VALID_MASK , w , x , y

======== CONSTRUCTOR SUMMARY ========

Constructor Summary CheckboxComponent ( String str, Image img) 새로운 CheckboxComponent 를 생성합니다. CheckboxComponent ( String str, Image img,
 boolean bSet) 새로운 CheckboxComponent 를 생성합니다. CheckboxComponent ( String str, Image img, CheckboxGroup cb) 새로운 CheckboxComponent 를 생성합니다.

========== METHOD SUMMARY ===========

Method Summary boolean getState () CheckboxComponent 의 선택상태를 구합니다. boolean keyNotify (int type,
 int key) 키 입력을 받으면 호출됩니다. void paintContent ( Graphics g) 내부를 칠합니다. void setChangeListener ( ChangeListener listener, Object obj) CheckboxComponent 에 ChangeListener 를 등록 합니다. void setState (boolean bState) CheckboxComponent 의 선택상태를 변경합니다.

Methods inherited from class org.kwis.msp.lwc. LabelComponent calcPreferredSize , getFont , getImage , getLabel , setFont , setImage , setLabel , setLayout

Methods inherited from class org.kwis.msp.lwc. Component canHandleInput , configure , focusNotify , getBackground , getCard , getForeground , getHeight , getPreferredHeight , getPreferredHeight , getPreferredWidth , getWidth , getX , getXOnScreen , getY , getYOnScreen , hasFocus , invalidate , isShown , isValid , layout , pointerNotify , processEvent , repaint , repaint , serviceRepaints , setBackground , setEventListener , setFocus , setForeground , showNotify , toString , validate

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , wait , wait , wait

============ FIELD DETAIL =========== 
 ========= CONSTRUCTOR DETAIL ========

Constructor Detail

### CheckboxComponent

**Parameters:**
- `img` - 체크박스의 이미지.

**See Also:**
- ``CheckboxComponent(String, Image, CheckboxGroup)``, 
``CheckboxComponent(String, Image, boolean)``, 
`#CheckboxComponent(String, Image, CheckboxGroup, boolean)`, 
``CheckboxGroup``

### CheckboxComponent

**See Also:**
- ``CheckboxComponent(String, Image)``, 
``CheckboxComponent(String, Image, boolean)``, 
`#CheckboxComponent(String, Image, CheckboxGroup, boolean)`, 
``CheckboxGroup``

### CheckboxComponent

**See Also:**
- ``CheckboxComponent(String, Image)``, 
``CheckboxComponent(String, Image, CheckboxGroup)``, 
`#CheckboxComponent(String, Image, CheckboxGroup, boolean)`, 
``setState(boolean)``, 
``CheckboxGroup``

============ METHOD DETAIL ==========

Method Detail

### setState

**See Also:**
- ``getState()``

### getState

**See Also:**
- ``setState(boolean)``

### paintContent

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `LabelComponent`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `g` - 칠할 Graphics.

**See Also:**
- ``Graphics``

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

### setChangeListener

**Parameters:**
- `obj` - Listener가 불려질때 넘겨 받을 Object (확장 파라메터)

**See Also:**
- ``CheckboxGroup.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object)``

========= END OF CLASS DATA =========

========== START OF NAVBAR ==========

=========== END OF NAVBAR ===========## 생성자 요약

- CheckboxComponent ( String str, Image img) 새로운 CheckboxComponent 를 생성합니다.
- CheckboxComponent ( String str, Image img,
 boolean bSet) 새로운 CheckboxComponent 를 생성합니다.
- CheckboxComponent ( String str, Image img, CheckboxGroup cb) 새로운 CheckboxComponent 를 생성합니다.

## 메서드 요약

- `boolean getState ()` — CheckboxComponent 의 선택상태를 구합니다.
- `boolean keyNotify (int type, int key)` — 키 입력을 받으면 호출됩니다.
- `void paintContent ( Graphics g)` — 내부를 칠합니다.
- `void setChangeListener ( ChangeListener listener, Object obj)` — CheckboxComponent 에 ChangeListener 를 등록 합니다.
- `void setState (boolean bState)` — CheckboxComponent 의 선택상태를 변경합니다.

## 생성자 상세

### CheckboxComponent

```java
public CheckboxComponent(String str,
                         Image img)
```

**Parameters:**
- `img` - 체크박스의 이미지.

**See Also:**
- ``CheckboxComponent(String, Image, CheckboxGroup)``, 
``CheckboxComponent(String, Image, boolean)``, 
`#CheckboxComponent(String, Image, CheckboxGroup, boolean)`, 
``CheckboxGroup``

### CheckboxComponent

```java
public CheckboxComponent(String str,
                         Image img,
                         CheckboxGroup cb)
```

**See Also:**
- ``CheckboxComponent(String, Image)``, 
``CheckboxComponent(String, Image, boolean)``, 
`#CheckboxComponent(String, Image, CheckboxGroup, boolean)`, 
``CheckboxGroup``

### CheckboxComponent

```java
public CheckboxComponent(String str,
                         Image img,
                         boolean bSet)
```

**See Also:**
- ``CheckboxComponent(String, Image)``, 
``CheckboxComponent(String, Image, CheckboxGroup)``, 
`#CheckboxComponent(String, Image, CheckboxGroup, boolean)`, 
``setState(boolean)``, 
``CheckboxGroup``

### setState

```java
public void setState(boolean bState)
```

**See Also:**
- ``getState()``

### getState

```java
public boolean getState()
```

**See Also:**
- ``setState(boolean)``

### paintContent

```java
public void paintContent(Graphics g)
```

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `LabelComponent`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `g` - 칠할 Graphics.

**See Also:**
- ``Graphics``

### keyNotify

```java
public boolean keyNotify(int type,
                         int key)
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

### setChangeListener

```java
public void setChangeListener(ChangeListener listener,
                              Object obj)
```

**Parameters:**
- `obj` - Listener가 불려질때 넘겨 받을 Object (확장 파라메터)

**See Also:**
- ``CheckboxGroup.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object)``## 메서드 상세

### setState

```java
public void setState(boolean bState)
```

**See Also:**
- ``getState()``

### getState

```java
public boolean getState()
```

**See Also:**
- ``setState(boolean)``

### paintContent

```java
public void paintContent(Graphics g)
```

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `LabelComponent`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `g` - 칠할 Graphics.

**See Also:**
- ``Graphics``

### keyNotify

```java
public boolean keyNotify(int type,
                         int key)
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

### setChangeListener

```java
public void setChangeListener(ChangeListener listener,
                              Object obj)
```

**Parameters:**
- `obj` - Listener가 불려질때 넘겨 받을 Object (확장 파라메터)

**See Also:**
- ``CheckboxGroup.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object)``

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
