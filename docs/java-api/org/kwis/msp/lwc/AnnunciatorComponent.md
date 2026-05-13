# Class AnnunciatorComponent

`package org.kwis.msp.lwc`

```
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.ContainerComponent
              |
              +--org.kwis.msp.lwc.ShellComponent
                    |
                    +--org.kwis.msp.lwc.AnnunciatorComponent
```

## 설명

**extends ShellComponent:**

Annunciator를 나타내기 위한 컴포넌트.

 ContainerComponent를 상속 받았지만 addComponent, removeComponent등의 함수를 사용할 수 없다.
 사용시 IllegalStateException발생.
 이 컴포는트는 Display에 추가 되어 들어 가며

**See Also:**
- ``ShellComponent``, 
``ContainerComponent``

Fields inherited from class org.kwis.msp.lwc. ShellComponent cd , cmpCommand , cmpTitle , cmpWork , RESIZE_MASK

Fields inherited from class org.kwis.msp.lwc. ContainerComponent cmpFocus , cmps , insetBottom , insetLeft , insetRight , insetTop , ncomp , offsetX , offsetY , useFrame

Fields inherited from class org.kwis.msp.lwc. Component bg , evtListener , evtListenerObj , fg , FOCUS_NOTIFY , h , HAS_FOCUS_MASK , INPUT_MASK , KEY_NOTIFY , KEY_PRESSED , KEY_RELEASED , KEY_REPEATED , KEY_TYPED , LAYOUT_BOTTOM , LAYOUT_HCENTER , LAYOUT_LEFT , LAYOUT_RIGHT , LAYOUT_TOP , LAYOUT_VCENTER , mask , parent , POINT_DRAGGED , POINT_PRESSED , POINT_RELEASED , POINTER_NOTIFY , POS_MASK , PREFER_SIZE_MASK , prefH , prefW , SHOW_NOTIFY , SIZE_MASK , VALID_MASK , w , x , y

Constructor Summary AnnunciatorComponent (boolean bTrans)

Method Summary void addComponent (int idx, Component cmp) 자식 컴포넌트를 하나 추가합니다. void hide () 컴포넌트를 화면에서 삭제 합니다. void layout () 하위 컴포넌트의 크기와 위치를 결정합니다. protected  void paint ( Graphics g) void removeComponent ( Component cmp) 지정된 순서의 컴포넌트를 삭제합니다.

 index번째 있는 컴포넌트를 삭제합니다. protected  void setParameter () void show () 컴포넌트를 화면상에 보여줍니다.

Methods inherited from class org.kwis.msp.lwc. ShellComponent addComponent , configure , controlInset , getCard , getCommand , getNextTraversalComponent , getPrevTraversalComponent , getTitle , getWorkComponent , getX , getY , grabKey , isShown , keyNotify , processEvent , removeAllComponents , repaint , serviceRepaints , setCommand , setGrabKeyListener , setTitle , setTitle , setWorkComponent , showNotify , ungrabKey

Methods inherited from class org.kwis.msp.lwc. ContainerComponent getComponent , getIndexOf , getNumberOfComponent , paintFrame , removeComponent , repaint , scrollTo , setComponent , useFrame , validate

Methods inherited from class org.kwis.msp.lwc. Component calcPreferredSize , canHandleInput , focusNotify , getBackground , getForeground , getHeight , getPreferredHeight , getPreferredHeight , getPreferredWidth , getWidth , getXOnScreen , getYOnScreen , hasFocus , invalidate , isValid , paintContent , pointerNotify , setBackground , setEventListener , setFocus , setForeground , toString

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , wait , wait , wait

Constructor Detail

### AnnunciatorComponent

Method Detail

### addComponent

**Overrides:**
- `addComponent` in class `ShellComponent`

**Parameters:**
- `cmp` - 넣을 컴포넌트

**Throws:**
- `IllegalStateException` - 항상 발생

### removeComponent

**Overrides:**
- `removeComponent` in class `ShellComponent`

**Parameters:**
- `index` - 삭제할 컴포넌트

**Throws:**
- `IllegalStateException` - 항상발생

### layout

- **Description copied from class: `Component`**

**Overrides:**
- `layout` in class `ShellComponent`

### setParameter

### show

**Overrides:**
- `show` in class `ShellComponent`

### hide

**Overrides:**
- `hide` in class `ShellComponent`

**Throws:**
- `IllegalStateException` - 항상발생

### paint

**Overrides:**
- `paint` in class `ContainerComponent`## 생성자 요약

- AnnunciatorComponent (boolean bTrans)

## 메서드 요약

- `void addComponent (int idx, Component cmp)` — 자식 컴포넌트를 하나 추가합니다.
- `void hide ()` — 컴포넌트를 화면에서 삭제 합니다.
- `void layout ()` — 하위 컴포넌트의 크기와 위치를 결정합니다.
- `protected  void paint ( Graphics g)`
- `void removeComponent ( Component cmp)` — 지정된 순서의 컴포넌트를 삭제합니다. index번째 있는 컴포넌트를 삭제합니다.
- `protected  void setParameter ()`
- `void show ()` — 컴포넌트를 화면상에 보여줍니다.

## 생성자 상세

### AnnunciatorComponent

```java
public AnnunciatorComponent(boolean bTrans)
```

### addComponent

```java
public void addComponent(int idx,
                         Component cmp)
```

**Overrides:**
- `addComponent` in class `ShellComponent`

**Parameters:**
- `cmp` - 넣을 컴포넌트

**Throws:**
- `IllegalStateException` - 항상 발생

### removeComponent

```java
public void removeComponent(Component cmp)
```

**Overrides:**
- `removeComponent` in class `ShellComponent`

**Parameters:**
- `index` - 삭제할 컴포넌트

**Throws:**
- `IllegalStateException` - 항상발생

### layout

```java
public void layout()
```

- **Description copied from class: `Component`**

**Overrides:**
- `layout` in class `ShellComponent`

### setParameter

```java
protected void setParameter()
```

### show

```java
public void show()
```

**Overrides:**
- `show` in class `ShellComponent`

### hide

```java
public void hide()
```

**Overrides:**
- `hide` in class `ShellComponent`

**Throws:**
- `IllegalStateException` - 항상발생

### paint

```java
protected void paint(Graphics g)
```

**Overrides:**
- `paint` in class `ContainerComponent`## 메서드 상세

### addComponent

```java
public void addComponent(int idx,
                         Component cmp)
```

**Overrides:**
- `addComponent` in class `ShellComponent`

**Parameters:**
- `cmp` - 넣을 컴포넌트

**Throws:**
- `IllegalStateException` - 항상 발생

### removeComponent

```java
public void removeComponent(Component cmp)
```

**Overrides:**
- `removeComponent` in class `ShellComponent`

**Parameters:**
- `index` - 삭제할 컴포넌트

**Throws:**
- `IllegalStateException` - 항상발생

### layout

```java
public void layout()
```

- **Description copied from class: `Component`**

**Overrides:**
- `layout` in class `ShellComponent`

### setParameter

```java
protected void setParameter()
```

### show

```java
public void show()
```

**Overrides:**
- `show` in class `ShellComponent`

### hide

```java
public void hide()
```

**Overrides:**
- `hide` in class `ShellComponent`

**Throws:**
- `IllegalStateException` - 항상발생

### paint

```java
protected void paint(Graphics g)
```

**Overrides:**
- `paint` in class `ContainerComponent`

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
