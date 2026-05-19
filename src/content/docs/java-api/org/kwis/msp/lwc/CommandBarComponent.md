---
title: "Class CommandBarComponent"
---

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.CommandBarComponent
```

## 설명

**extends Component:**

Command 컴포넌트.

 등록된 하나 이상의 커맨드를 바 형태로 구성합니다.
 화면에 현재 화면에 사용자가 내릴 수 있는 명령어를 보여주며,
 사용자로 부터 명령을 선택 받습니다.
 Active된 Index의 초기값은 -1입니다.

Fields inherited from class org.kwis.msp.lwc. Component bg , evtListener , evtListenerObj , fg , FOCUS_NOTIFY , h , HAS_FOCUS_MASK , INPUT_MASK , KEY_NOTIFY , KEY_PRESSED , KEY_RELEASED , KEY_REPEATED , KEY_TYPED , LAYOUT_BOTTOM , LAYOUT_HCENTER , LAYOUT_LEFT , LAYOUT_RIGHT , LAYOUT_TOP , LAYOUT_VCENTER , mask , parent , POINT_DRAGGED , POINT_PRESSED , POINT_RELEASED , POINTER_NOTIFY , POS_MASK , PREFER_SIZE_MASK , prefH , prefW , SHOW_NOTIFY , SIZE_MASK , VALID_MASK , w , x , y

Constructor Summary CommandBarComponent () 커맨드 바 컴포넌트를 생성합니다.

Method Summary int addCommand ( Command cmd) 커맨드를 하나 추가 시킵니다. int getActiveIndex () 선택된 커맨드의 인덱스를 돌려줍니다. Command getCommand (int index) 커맨드를 돌려줍니다. int getPreferredHeight () 컴포넌트의 적절한 높이를 결정합니다. int getPreferredHeight (int w) 컴포넌트의 적절한 높이를 결정합니다. int getPreferredWidth () 컴포넌트의 적절한 폭을 결정합니다. int getSize () 등록된 커맨드의 개수를 구합니다 protected  boolean keyNotify (int type,
 int chr) 키 입력을 받으면 호출됩니다. void paintContent ( Graphics g) 내부를 칠합니다. protected  boolean pointerNotify (int type,
 int x,
 int y) 포인터 입력을 받으면 호출됩니다. void removeAll () 모든 커맨드를 삭제합니다. void removeCommand ( Command cmd) 커맨드를 삭제합니다. void setActiveIndex (int index) 선택된 커맨드를 지정합니다. void setCommandListener ( CommandListener cl, Object obj) 커맨드 리스너를 지정합니다.

Methods inherited from class org.kwis.msp.lwc. Component calcPreferredSize , canHandleInput , configure , focusNotify , getBackground , getCard , getForeground , getHeight , getWidth , getX , getXOnScreen , getY , getYOnScreen , hasFocus , invalidate , isShown , isValid , layout , processEvent , repaint , repaint , serviceRepaints , setBackground , setEventListener , setFocus , setForeground , showNotify , toString , validate

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , wait , wait , wait

Constructor Detail

### CommandBarComponent

- 커맨드 바 컴포넌트를 생성합니다.

Method Detail

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

### getSize

**Returns:**
- 등록된 Command의 개수

### addCommand

**Parameters:**
- `cmd` - 추가할 커맨드

**Returns:**
- 추가된 Command의 Index , 실패한경우 -1을 리턴합니다.

**See Also:**
- ``Command``, 
``setActiveIndex(int)``

### removeCommand

**Parameters:**
- `cmd` - 삭제할 커맨드

**See Also:**
- ``Command``

### removeAll

**Parameters:**
- `cmd` - 삭제할 커맨드

**See Also:**
- ``Command``

### setActiveIndex

**Parameters:**
- `index` - 선택할 커맨드의 인덱스

### getActiveIndex

**Returns:**
- 선택된 커맨드의 인덱스

### getCommand

**Parameters:**
- `index` - 가져올 커맨드의 인덱스

**Returns:**
- 지정한 커맨드

### setCommandListener

**Parameters:**
- `obj` - commandAction시에 넘어가는 Object

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

### pointerNotify

- **Description copied from class: `Component`**

**Overrides:**
- `pointerNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `y` - 디바이스의 'y'축 좌표

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 이벤트를 이 컴포넌트가 처리했다면,
 false를 넘김

### paintContent

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `g` - 칠할 Graphics.

**See Also:**
- ``Graphics``## 생성자 요약

- CommandBarComponent () 커맨드 바 컴포넌트를 생성합니다.

## 메서드 요약

- `int addCommand ( Command cmd)` — 커맨드를 하나 추가 시킵니다.
- `int getActiveIndex ()` — 선택된 커맨드의 인덱스를 돌려줍니다.
- `Command getCommand (int index)` — 커맨드를 돌려줍니다.
- `int getPreferredHeight ()` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredHeight (int w)` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredWidth ()` — 컴포넌트의 적절한 폭을 결정합니다.
- `int getSize ()` — 등록된 커맨드의 개수를 구합니다
- `protected  boolean keyNotify (int type, int chr)` — 키 입력을 받으면 호출됩니다.
- `void paintContent ( Graphics g)` — 내부를 칠합니다.
- `protected  boolean pointerNotify (int type, int x, int y)` — 포인터 입력을 받으면 호출됩니다.
- `void removeAll ()` — 모든 커맨드를 삭제합니다.
- `void removeCommand ( Command cmd)` — 커맨드를 삭제합니다.
- `void setActiveIndex (int index)` — 선택된 커맨드를 지정합니다.
- `void setCommandListener ( CommandListener cl, Object obj)` — 커맨드 리스너를 지정합니다.

## 생성자 상세

### CommandBarComponent

```java
public CommandBarComponent()
```

- 커맨드 바 컴포넌트를 생성합니다.

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

### getSize

```java
public int getSize()
```

**Returns:**
- 등록된 Command의 개수

### addCommand

```java
public int addCommand(Command cmd)
```

**Parameters:**
- `cmd` - 추가할 커맨드

**Returns:**
- 추가된 Command의 Index , 실패한경우 -1을 리턴합니다.

**See Also:**
- ``Command``, 
``setActiveIndex(int)``

### removeCommand

```java
public void removeCommand(Command cmd)
```

**Parameters:**
- `cmd` - 삭제할 커맨드

**See Also:**
- ``Command``

### removeAll

```java
public void removeAll()
```

**Parameters:**
- `cmd` - 삭제할 커맨드

**See Also:**
- ``Command``

### setActiveIndex

```java
public void setActiveIndex(int index)
```

**Parameters:**
- `index` - 선택할 커맨드의 인덱스

### getActiveIndex

```java
public int getActiveIndex()
```

**Returns:**
- 선택된 커맨드의 인덱스

### getCommand

```java
public Command getCommand(int index)
```

**Parameters:**
- `index` - 가져올 커맨드의 인덱스

**Returns:**
- 지정한 커맨드

### setCommandListener

```java
public void setCommandListener(CommandListener cl,
                               Object obj)
```

**Parameters:**
- `obj` - commandAction시에 넘어가는 Object

### keyNotify

```java
protected boolean keyNotify(int type,
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

### pointerNotify

```java
protected boolean pointerNotify(int type,
                                int x,
                                int y)
```

- **Description copied from class: `Component`**

**Overrides:**
- `pointerNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `y` - 디바이스의 'y'축 좌표

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 이벤트를 이 컴포넌트가 처리했다면,
 false를 넘김

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

### getSize

```java
public int getSize()
```

**Returns:**
- 등록된 Command의 개수

### addCommand

```java
public int addCommand(Command cmd)
```

**Parameters:**
- `cmd` - 추가할 커맨드

**Returns:**
- 추가된 Command의 Index , 실패한경우 -1을 리턴합니다.

**See Also:**
- ``Command``, 
``setActiveIndex(int)``

### removeCommand

```java
public void removeCommand(Command cmd)
```

**Parameters:**
- `cmd` - 삭제할 커맨드

**See Also:**
- ``Command``

### removeAll

```java
public void removeAll()
```

**Parameters:**
- `cmd` - 삭제할 커맨드

**See Also:**
- ``Command``

### setActiveIndex

```java
public void setActiveIndex(int index)
```

**Parameters:**
- `index` - 선택할 커맨드의 인덱스

### getActiveIndex

```java
public int getActiveIndex()
```

**Returns:**
- 선택된 커맨드의 인덱스

### getCommand

```java
public Command getCommand(int index)
```

**Parameters:**
- `index` - 가져올 커맨드의 인덱스

**Returns:**
- 지정한 커맨드

### setCommandListener

```java
public void setCommandListener(CommandListener cl,
                               Object obj)
```

**Parameters:**
- `obj` - commandAction시에 넘어가는 Object

### keyNotify

```java
protected boolean keyNotify(int type,
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

### pointerNotify

```java
protected boolean pointerNotify(int type,
                                int x,
                                int y)
```

- **Description copied from class: `Component`**

**Overrides:**
- `pointerNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `y` - 디바이스의 'y'축 좌표

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 이벤트를 이 컴포넌트가 처리했다면,
 false를 넘김

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
