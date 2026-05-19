---
title: "Class FormComponent"
---

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.ContainerComponent
              |
              +--org.kwis.msp.lwc.FormComponent
```

## 설명

**Direct Known Subclasses:**
- `ListComponent`

**extends ContainerComponent:**

다양한 컴포넌트를 일렬로 배열하여 화면을 구성하는 컴포넌트.

 `FormComponent`는 `ContainerComponent`를 확장하여
 자식 컴포넌트로서 다양한 컴포넌트를 담아서 화면을 구성하는
 컴포넌트입니다. 또한 각 컴포넌트들의 배치와 스크롤 여부를 관리합니다.

자식 컴포넌트들이 포커스 이동은 상하만 동작하도록 되어 있습니다.
 UP/DOWN키를 사용하여 자식 컴포넌트들의 포커스 이동을 할 수 있습니다.
 내부의 컴포넌트가 많으면 자동적으로 scrollbar가 생성되도록
 되어 있습니다.

Fields inherited from class org.kwis.msp.lwc. ContainerComponent cmpFocus , cmps , insetBottom , insetLeft , insetRight , insetTop , ncomp , offsetX , offsetY , useFrame

Fields inherited from class org.kwis.msp.lwc. Component bg , evtListener , evtListenerObj , fg , FOCUS_NOTIFY , h , HAS_FOCUS_MASK , INPUT_MASK , KEY_NOTIFY , KEY_PRESSED , KEY_RELEASED , KEY_REPEATED , KEY_TYPED , LAYOUT_BOTTOM , LAYOUT_HCENTER , LAYOUT_LEFT , LAYOUT_RIGHT , LAYOUT_TOP , LAYOUT_VCENTER , mask , parent , POINT_DRAGGED , POINT_PRESSED , POINT_RELEASED , POINTER_NOTIFY , POS_MASK , PREFER_SIZE_MASK , prefH , prefW , SHOW_NOTIFY , SIZE_MASK , VALID_MASK , w , x , y

Constructor Summary FormComponent () 폼 컴포넌트를 생성합니다. FormComponent (boolean bVertical) 폼 컴포넌트를 생성합니다.

Method Summary protected  void calcPreferredSize (int cw) 컴포넌트의 적절한 크기를 계산합니다. void focusNotify (boolean b) 포커스를 받으면 호출됩니다. int getGab () 컴포넌트 간의 간격을 돌려줍니다. protected Component getNextTraversalComponent () 포커스 가질 수 있는 다음 컴포넌트를 돌려줍니다. boolean getPacked () 자식 컴포넌트의 폭을 맞출것인지 여부를 돌려줍니다. protected Component getPrevTraversalComponent () 포커스 가질 수 있는 이전 컴포넌트를 돌려줍니다. protected  boolean keyNotify (int type,
 int key) 키 입력을 받으면 호출됩니다. void layout () 하위 컴포넌트의 크기와 위치를 결정합니다. protected  void layoutChildHorizontal () protected  void layoutChildVertical () void paint ( Graphics g) void removeAllComponents () 모든 컴포넌트를 삭제합니다. protected  boolean scrollTo (int dx,
 int dy) 특정 위치로 화면을 이동합니다. void setFocus ( Component c) void setGab (int gab) 컴포넌트 간의 간격을 결정합니다. void setPacked (boolean b) 폼의 내부의 컴포넌트의 폭을 폼의 폭으로 맞출 것인지 여부를
 지정합니다.

Methods inherited from class org.kwis.msp.lwc. ContainerComponent addComponent , addComponent , controlInset , getComponent , getIndexOf , getNumberOfComponent , paintFrame , processEvent , removeComponent , removeComponent , repaint , repaint , setComponent , useFrame , validate

Methods inherited from class org.kwis.msp.lwc. Component canHandleInput , configure , getBackground , getCard , getForeground , getHeight , getPreferredHeight , getPreferredHeight , getPreferredWidth , getWidth , getX , getXOnScreen , getY , getYOnScreen , hasFocus , invalidate , isShown , isValid , paintContent , pointerNotify , serviceRepaints , setBackground , setEventListener , setFocus , setForeground , showNotify , toString

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , wait , wait , wait

Constructor Detail

### FormComponent

- 폼 컴포넌트를 생성합니다.

### FormComponent

- 폼 컴포넌트를 생성합니다.

Method Detail

### removeAllComponents

**Overrides:**
- `removeAllComponents` in class `ContainerComponent`

### setPacked

**Parameters:**
- `b` - 폭에 맞추면 true, 그렇지 않으면 false

### getPacked

**Returns:**
- 폭에 맞추는지 여부

### setGab

**Parameters:**
- `gab` - 컴포넌트 간의 간격

### getGab

**Returns:**
- 컴포넌트 간의 간격

### layoutChildHorizontal

### layoutChildVertical

### focusNotify

- **Description copied from class: `Component`**

**Overrides:**
- `focusNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `b` - 포커스를 가질땐 `true`가 넘어오고,
 가지지 않을땐 `false`

### keyNotify

- **Description copied from class: `Component`**

**Overrides:**
- `keyNotify` in class `ContainerComponent`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며
 이외의 문자도 넘어 올 수 있습니다.

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 키를 이 컴포넌트가 처리했다면,
 `true`를 넘겨 줍니다. 그렇지 않았다면 `false`를
 돌려줍니다.

### calcPreferredSize

- **Description copied from class: `Component`**

**Overrides:**
- `calcPreferredSize` in class `Component`

### layout

- **Description copied from class: `Component`**

**Overrides:**
- `layout` in class `Component`

### setFocus

### paint

**Overrides:**
- `paint` in class `ContainerComponent`

### getNextTraversalComponent

- **Description copied from class: `ContainerComponent`**

**Overrides:**
- `getNextTraversalComponent` in class `ContainerComponent`
- Following copied from class: `org.kwis.msp.lwc.ContainerComponent`

**Returns:**
- 포커스를 가질 수 있는 다음 컴포넌트

### getPrevTraversalComponent

- **Description copied from class: `ContainerComponent`**

**Overrides:**
- `getPrevTraversalComponent` in class `ContainerComponent`
- Following copied from class: `org.kwis.msp.lwc.ContainerComponent`

**Returns:**
- 포커스를 가질 수 있는 이전 컴포넌트

### scrollTo

## 생성자 요약

- FormComponent () 폼 컴포넌트를 생성합니다.
- FormComponent (boolean bVertical) 폼 컴포넌트를 생성합니다.

## 메서드 요약

- `protected  void calcPreferredSize (int cw)` — 컴포넌트의 적절한 크기를 계산합니다.
- `void focusNotify (boolean b)` — 포커스를 받으면 호출됩니다.
- `int getGab ()` — 컴포넌트 간의 간격을 돌려줍니다.
- `protected Component getNextTraversalComponent ()` — 포커스 가질 수 있는 다음 컴포넌트를 돌려줍니다.
- `boolean getPacked ()` — 자식 컴포넌트의 폭을 맞출것인지 여부를 돌려줍니다.
- `protected Component getPrevTraversalComponent ()` — 포커스 가질 수 있는 이전 컴포넌트를 돌려줍니다.
- `protected  boolean keyNotify (int type, int key)` — 키 입력을 받으면 호출됩니다.
- `void layout ()` — 하위 컴포넌트의 크기와 위치를 결정합니다.
- `protected  void layoutChildHorizontal ()`
- `protected  void layoutChildVertical ()`
- `void paint ( Graphics g)`
- `void removeAllComponents ()` — 모든 컴포넌트를 삭제합니다.
- `protected  boolean scrollTo (int dx, int dy)` — 특정 위치로 화면을 이동합니다.
- `void setFocus ( Component c)`
- `void setGab (int gab)` — 컴포넌트 간의 간격을 결정합니다.
- `void setPacked (boolean b)` — 폼의 내부의 컴포넌트의 폭을 폼의 폭으로 맞출 것인지 여부를 지정합니다.

## 생성자 상세

### FormComponent

```java
public FormComponent()
```

- 폼 컴포넌트를 생성합니다.

### FormComponent

```java
public FormComponent(boolean bVertical)
```

- 폼 컴포넌트를 생성합니다.

### removeAllComponents

```java
public void removeAllComponents()
```

**Overrides:**
- `removeAllComponents` in class `ContainerComponent`

### setPacked

```java
public void setPacked(boolean b)
```

**Parameters:**
- `b` - 폭에 맞추면 true, 그렇지 않으면 false

### getPacked

```java
public boolean getPacked()
```

**Returns:**
- 폭에 맞추는지 여부

### setGab

```java
public void setGab(int gab)
```

**Parameters:**
- `gab` - 컴포넌트 간의 간격

### getGab

```java
public int getGab()
```

**Returns:**
- 컴포넌트 간의 간격

### layoutChildHorizontal

```java
protected void layoutChildHorizontal()
```

### layoutChildVertical

```java
protected void layoutChildVertical()
```

### focusNotify

```java
public void focusNotify(boolean b)
```

- **Description copied from class: `Component`**

**Overrides:**
- `focusNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `b` - 포커스를 가질땐 `true`가 넘어오고,
 가지지 않을땐 `false`

### keyNotify

```java
protected boolean keyNotify(int type,
                            int key)
```

- **Description copied from class: `Component`**

**Overrides:**
- `keyNotify` in class `ContainerComponent`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며
 이외의 문자도 넘어 올 수 있습니다.

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 키를 이 컴포넌트가 처리했다면,
 `true`를 넘겨 줍니다. 그렇지 않았다면 `false`를
 돌려줍니다.

### calcPreferredSize

```java
protected void calcPreferredSize(int cw)
```

- **Description copied from class: `Component`**

**Overrides:**
- `calcPreferredSize` in class `Component`

### layout

```java
public void layout()
```

- **Description copied from class: `Component`**

**Overrides:**
- `layout` in class `Component`

### setFocus

```java
public void setFocus(Component c)
```

### paint

```java
public void paint(Graphics g)
```

**Overrides:**
- `paint` in class `ContainerComponent`

### getNextTraversalComponent

```java
protected Component getNextTraversalComponent()
```

- **Description copied from class: `ContainerComponent`**

**Overrides:**
- `getNextTraversalComponent` in class `ContainerComponent`
- Following copied from class: `org.kwis.msp.lwc.ContainerComponent`

**Returns:**
- 포커스를 가질 수 있는 다음 컴포넌트

### getPrevTraversalComponent

```java
protected Component getPrevTraversalComponent()
```

- **Description copied from class: `ContainerComponent`**

**Overrides:**
- `getPrevTraversalComponent` in class `ContainerComponent`
- Following copied from class: `org.kwis.msp.lwc.ContainerComponent`

**Returns:**
- 포커스를 가질 수 있는 이전 컴포넌트

### scrollTo

```java
protected boolean scrollTo(inODE>ContainerComponent
```

## 메서드 상세

### removeAllComponents

```java
public void removeAllComponents()
```

**Overrides:**
- `removeAllComponents` in class `ContainerComponent`

### setPacked

```java
public void setPacked(boolean b)
```

**Parameters:**
- `b` - 폭에 맞추면 true, 그렇지 않으면 false

### getPacked

```java
public boolean getPacked()
```

**Returns:**
- 폭에 맞추는지 여부

### setGab

```java
public void setGab(int gab)
```

**Parameters:**
- `gab` - 컴포넌트 간의 간격

### getGab

```java
public int getGab()
```

**Returns:**
- 컴포넌트 간의 간격

### layoutChildHorizontal

```java
protected void layoutChildHorizontal()
```

### layoutChildVertical

```java
protected void layoutChildVertical()
```

### focusNotify

```java
public void focusNotify(boolean b)
```

- **Description copied from class: `Component`**

**Overrides:**
- `focusNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `b` - 포커스를 가질땐 `true`가 넘어오고,
 가지지 않을땐 `false`

### keyNotify

```java
protected boolean keyNotify(int type,
                            int key)
```

- **Description copied from class: `Component`**

**Overrides:**
- `keyNotify` in class `ContainerComponent`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며
 이외의 문자도 넘어 올 수 있습니다.

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 키를 이 컴포넌트가 처리했다면,
 `true`를 넘겨 줍니다. 그렇지 않았다면 `false`를
 돌려줍니다.

### calcPreferredSize

```java
protected void calcPreferredSize(int cw)
```

- **Description copied from class: `Component`**

**Overrides:**
- `calcPreferredSize` in class `Component`

### layout

```java
public void layout()
```

- **Description copied from class: `Component`**

**Overrides:**
- `layout` in class `Component`

### setFocus

```java
public void setFocus(Component c)
```

### paint

```java
public void paint(Graphics g)
```

**Overrides:**
- `paint` in class `ContainerComponent`

### getNextTraversalComponent

```java
protected Component getNextTraversalComponent()
```

- **Description copied from class: `ContainerComponent`**

**Overrides:**
- `getNextTraversalComponent` in class `ContainerComponent`
- Following copied from class: `org.kwis.msp.lwc.ContainerComponent`

**Returns:**
- 포커스를 가질 수 있는 다음 컴포넌트

### getPrevTraversalComponent

```java
protected Component getPrevTraversalComponent()
```

- **Description copied from class: `ContainerComponent`**

**Overrides:**
- `getPrevTraversalComponent` in class `ContainerComponent`
- Following copied from class: `org.kwis.msp.lwc.ContainerComponent`

**Returns:**
- 포커스를 가질 수 있는 이전 컴포넌트

### scrollTo

```java
protected boolean scrollTo(inODE>ContainerComponent
```
