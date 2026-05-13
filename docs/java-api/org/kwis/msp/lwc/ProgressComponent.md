# Class ProgressComponent

`package org.kwis.msp.lwc`

```
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.ProgressComponent
```

## 설명

**extends Component:**

프로그래스 컴퍼넌트는 진행상태등을 나타내기 위해 사용하는 콤포넌트입니다.
 Interactive NoneInteractive두가지 모드가 있으며 생성시에 결정됩니다.
 Interactive의 경우 사용자의 키 입력을 받아 setStep에서 정의 된 값만큼 증가 혹은 감소하게 됩니다. 
 NoneInteractive모드에서는 사용자의 입력은 받지 않으며 setValue에 의해 값이 변경 됩니다.
 기본적으로 step값은 1로 되어 있으며 setStep함수에 의해 변경 가능합니다.
 ProgressComponent의 최소값은 0으로 고정되어 있으며 최대값만 변경 가능합니다.

======== INNER CLASS SUMMARY ======== 
 =========== FIELD SUMMARY ===========

Fields inherited from class org.kwis.msp.lwc. Component bg , evtListener , evtListenerObj , fg , FOCUS_NOTIFY , h , HAS_FOCUS_MASK , INPUT_MASK , KEY_NOTIFY , KEY_PRESSED , KEY_RELEASED , KEY_REPEATED , KEY_TYPED , LAYOUT_BOTTOM , LAYOUT_HCENTER , LAYOUT_LEFT , LAYOUT_RIGHT , LAYOUT_TOP , LAYOUT_VCENTER , mask , parent , POINT_DRAGGED , POINT_PRESSED , POINT_RELEASED , POINTER_NOTIFY , POS_MASK , PREFER_SIZE_MASK , prefH , prefW , SHOW_NOTIFY , SIZE_MASK , VALID_MASK , w , x , y

======== CONSTRUCTOR SUMMARY ========

Constructor Summary ProgressComponent (boolean bInteractive,
 int max) 생성자함수 
 0을 최소값으로 하는 새로운 프로그래스 콤포넌트를 만든다.

========== METHOD SUMMARY ===========

Method Summary int getMaxValue () 설정되어 있는 최대값을 구하는 함수. int getPreferredHeight () 컴포넌트의 적절한 높이를 결정합니다. int getPreferredHeight (int w) 컴포넌트의 적절한 높이를 결정합니다. int getPreferredWidth () 컴포넌트의 적절한 폭을 결정합니다. int getStep () 프로그래스바의 증감 단위를 구합니다 int getValue () 프로그래스의 설정되어 있는 현재 값을 구하는 함수. boolean keyNotify (int type,
 int key) 키 입력을 받으면 호출됩니다. void paintContent ( Graphics g) 내부를 칠합니다. void setChangeListener ( ChangeListener listener, Object obj) void setMargin (int top,
 int bottom) 프로그래스바의 상하 여백을 설정합니다(픽셀단위) void setMaxValue (int maxValue) Progress의 최대 값을 설정합니다. void setStep (int step) 프로그래스바의 증감 단위를 설정합니다
 Interactive인 경우 사용자의 입력에의한 증가량이으로 사용되며 , 
 setValue등에 의한 입력시에도 주어진 단위별로 증감이 됩니다.
 step값이 변경되는경우 현재값도 step단위로 변경됩니다. int setValue (int value) Progress의 현재값을 설정합니다.
 setStep에 의해 step이 설정된 경우 설정한 step 단위로 값이 변경됩니다.

Methods inherited from class org.kwis.msp.lwc. Component calcPreferredSize , canHandleInput , configure , focusNotify , getBackground , getCard , getForeground , getHeight , getWidth , getX , getXOnScreen , getY , getYOnScreen , hasFocus , invalidate , isShown , isValid , layout , pointerNotify , processEvent , repaint , repaint , serviceRepaints , setBackground , setEventListener , setFocus , setForeground , showNotify , toString , validate

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , wait , wait , wait

============ FIELD DETAIL =========== 
 ========= CONSTRUCTOR DETAIL ========

Constructor Detail

### ProgressComponent

**Parameters:**
- `max` - 프로그래스의 최대값을 설정한다.

============ METHOD DETAIL ==========

Method Detail

### setStep

**Parameters:**
- `nStep` - 증가량.

**Throws:**
- `IllegalArgumentException` - step 값이 0이하거나 최대값보다 큰 경우

**See Also:**
- ``getStep()``

### getStep

**Returns:**
- 설정된 증가량.

**See Also:**
- `#setStep()`

### setMargin

**See Also:**
- `#setStep()`

### setMaxValue

**Parameters:**
- `maxValue` - 설정할 최대값

**Throws:**
- `IllegalArgumentException` - maxValue 값이 0이하인 경우

### setValue

**Parameters:**
- `value` - 설정할 값

**Returns:**
- 설정된 값

### getValue

**Returns:**
- 설정되어 있는 현재값

### getMaxValue

**Returns:**
- 설정되어 있는 최대값

### getPreferredHeight

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `w` - 가변폭.

**Returns:**
- 컴포넌트의 높이.

### getPreferredHeight

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 높이

### getPreferredWidth

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredWidth` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 폭.

### paintContent

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `Component`
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

========= END OF CLASS DATA =========

========== START OF NAVBAR ==========

=========== END OF NAVBAR ===========

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 생성자 요약

- ProgressComponent (boolean bInteractive,
 int max) 생성자함수 
 0을 최소값으로 하는 새로운 프로그래스 콤포넌트를 만든다.

## 메서드 요약

- `int getMaxValue ()` — 설정되어 있는 최대값을 구하는 함수.
- `int getPreferredHeight ()` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredHeight (int w)` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredWidth ()` — 컴포넌트의 적절한 폭을 결정합니다.
- `int getStep ()` — 프로그래스바의 증감 단위를 구합니다
- `int getValue ()` — 프로그래스의 설정되어 있는 현재 값을 구하는 함수.
- `boolean keyNotify (int type, int key)` — 키 입력을 받으면 호출됩니다.
- `void paintContent ( Graphics g)` — 내부를 칠합니다.
- `void setChangeListener ( ChangeListener listener, Object obj)`
- `void setMargin (int top, int bottom)` — 프로그래스바의 상하 여백을 설정합니다(픽셀단위)
- `void setMaxValue (int maxValue)` — Progress의 최대 값을 설정합니다.
- `void setStep (int step)` — 프로그래스바의 증감 단위를 설정합니다 Interactive인 경우 사용자의 입력에의한 증가량이으로 사용되며 , setValue등에 의한 입력시에도 주어진 단위별로 증감이 됩니다. step값이 변경되는경우 현재값도 step단위로 변경됩니다.
- `int setValue (int value)` — Progress의 현재값을 설정합니다. setStep에 의해 step이 설정된 경우 설정한 step 단위로 값이 변경됩니다.

## 생성자 상세

### ProgressComponent

```java
public ProgressComponent(boolean bInteractive,
                         int max)
```

**Parameters:**
- `max` - 프로그래스의 최대값을 설정한다.

### setStep

```java
public void setStep(int step)
```

**Parameters:**
- `nStep` - 증가량.

**Throws:**
- `IllegalArgumentException` - step 값이 0이하거나 최대값보다 큰 경우

**See Also:**
- ``getStep()``

### getStep

```java
public int getStep()
```

**Returns:**
- 설정된 증가량.

**See Also:**
- `#setStep()`

### setMargin

```java
public void setMargin(int top,
                      int bottom)
```

**See Also:**
- `#setStep()`

### setMaxValue

```java
public void setMaxValue(int maxValue)
```

**Parameters:**
- `maxValue` - 설정할 최대값

**Throws:**
- `IllegalArgumentException` - maxValue 값이 0이하인 경우

### setValue

```java
public int setValue(int value)
```

**Parameters:**
- `value` - 설정할 값

**Returns:**
- 설정된 값

### getValue

```java
public int getValue()
```

**Returns:**
- 설정되어 있는 현재값

### getMaxValue

```java
public int getMaxValue()
```

**Returns:**
- 설정되어 있는 최대값

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

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 메서드 상세

### setStep

```java
public void setStep(int step)
```

**Parameters:**
- `nStep` - 증가량.

**Throws:**
- `IllegalArgumentException` - step 값이 0이하거나 최대값보다 큰 경우

**See Also:**
- ``getStep()``

### getStep

```java
public int getStep()
```

**Returns:**
- 설정된 증가량.

**See Also:**
- `#setStep()`

### setMargin

```java
public void setMargin(int top,
                      int bottom)
```

**See Also:**
- `#setStep()`

### setMaxValue

```java
public void setMaxValue(int maxValue)
```

**Parameters:**
- `maxValue` - 설정할 최대값

**Throws:**
- `IllegalArgumentException` - maxValue 값이 0이하인 경우

### setValue

```java
public int setValue(int value)
```

**Parameters:**
- `value` - 설정할 값

**Returns:**
- 설정된 값

### getValue

```java
public int getValue()
```

**Returns:**
- 설정되어 있는 현재값

### getMaxValue

```java
public int getMaxValue()
```

**Returns:**
- 설정되어 있는 최대값

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

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
