# Class ContainerComponent

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.ContainerComponent
```

## 설명

**Direct Known Subclasses:**
- `FormComponent`, `ShellComponent`

**extends Component:**

다른 컴포넌트의 상위 부모 컴포넌트가 될수 있는 컴포넌트.

 자식 컴포넌트의 위치와 크기를 결정해 주며, 포커스 관리를
 해줍니다.

 컴포넌트는 `addComponent`함수로 자식 컴포넌트로
 등록할 수 있으며, `removeComponent`함수로
 삭제할 수 있습니다.

 컴포넌트는 상위 부모 컴포넌트가 있으며, 그 맨 상위 부모
 컴포넌트가 ShellComponent이며 show함수로 보여질 때 화면에
 나타나게 됩니다.

 컨테이너 컴포넌트는 `layout`함수를 통해서 하위
 자식 컴포넌트들의 크기와 위치를 결정해줍니다.

 컨테이너 내에는 인셋(Inset)이 있어 하위 자식 컴포넌트들이
 인셋내부에만 나타나고, 인셋 밖에는 출력되지 않도록 되어 있습니다.

 특정 컴포넌트가 키 입력을 받기 위해서는 `setFocus`
 함수를 호출해 주어야만 합니다.

**See Also:**
- ``ShellComponent``, 
``Component``

## 필드 요약

- `protected Component cmpFocus`
- `protected Component [] cmps`
- `protected  short insetBottom`
- `protected  short insetLeft`
- `protected  short insetRight`
- `protected  short insetTop`
- `protected  int ncomp`
- `protected  int offsetX`
- `protected  int offsetY`
- `protected  boolean useFrame` — 프레임의 사용여부.

## 생성자 요약

- `protected ContainerComponent ()`

## 메서드 요약

- `int addComponent ( Component cmp)` — 자식 컴포넌트를 하나 추가합니다.
- `void addComponent (int index, Component cmp)` — 자식 컴포넌트를 하나 추가합니다.
- `protected  void controlInset (boolean flag)` — ContainerComponent 에서 사용할 테두리 두께값을 제어합니다.
- `Component getComponent (int i)` — 특정 stack 순서의 컴포넌트를 가져옵니다.
- `int getIndexOf ( Component cmp)` — 컴포넌트의 stack 순서를 가져옵니다.
- `protected Component getNextTraversalComponent ()` — 포커스 가질 수 있는 다음 컴포넌트를 돌려줍니다.
- `int getNumberOfComponent ()` — 등록된 Component의 수를 수합니다
- `protected Component getPrevTraversalComponent ()` — 포커스 가질 수 있는 이전 컴포넌트를 돌려줍니다.
- `protected  boolean keyNotify (int type, int key)` — 키 입력을 받으면 호출됩니다.
- `protected  void paint ( Graphics g)`
- `protected  void paintFrame ( Graphics g)` — useFrame 의 인수를 true 으로 호출하는 경우에 화면을 그릴때 호출됩니다.
- `protected  boolean processEvent (int type, int subtype, int param1, int param2)` — 이벤트를 처리합니다.
- `void removeAllComponents ()` — 모든 컴포넌트를 삭제합니다.
- `void removeComponent ( Component cmp)` — 지정된 컴포넌트를 삭제합니다.
- `void removeComponent (int index)` — 지정된 순서의 컴포넌트를 삭제합니다. index번째 있는 컴포넌트를 삭제합니다.
- `void repaint ()` — 화면의 내용을 갱신할 필요가 있을때 부릅니다.
- `void repaint (int x, int y, int w, int h)` — 화면의 내용을 갱신할 필요가 있을때 부릅니다.
- `protected  boolean scrollTo (int dx, int dy)` — 특정 위치로 화면을 이동합니다.
- `void setComponent (int index, Component cmp)` — 자식 컴포넌트를 하나 대치합니다.
- `void useFrame (boolean useFrame)` — ContainterComponent 에서 테두리를 화면에 출력할 것인지를 지정합니다.
- `void validate ()` — 컴포넌트에 유효한 좌표와 크기를 가지게 합니다.

## 필드 상세

### cmps

```java
protected Component[] cmps
```

### ncomp

```java
protected int ncomp
```

### cmpFocus

```java
protected Component cmpFocus
```

### offsetX

```java
protected int offsetX
```

### offsetY

```java
protected int offsetY
```

### insetTop

```java
protected short insetTop
```

### insetBottom

```java
protected short insetBottom
```

### insetLeft

```java
protected short insetLeft
```

### insetRight

```java
protected short insetRight
```

### useFrame

```java
protected boolean useFrame
```

- 프레임의 사용여부.

### ContainerComponent

```java
protected ContainerComponent()
```

### addComponent

```java
public void addComponent(int index,
                         Component cmp)
```

**Parameters:**
- `cmp` - 넣을 컴포넌트

**Throws:**
- `NullPointerException` - `cmp`이 `null`인 경우

### addComponent

```java
public int addComponent(Component cmp)
```

**Parameters:**
- `cmp` - 추가할 자식 컴포넌트

**Throws:**
- `NullPointerException` - `cmp`이 `null`인 경우

### setComponent

```java
public void setComponent(int index,
                         Component cmp)
```

**Parameters:**
- `cmp` - 바뀔 컴포넌트

**Throws:**

## 생성자 상세

### ContainerComponent

```java
protected ContainerComponent()
```

### addComponent

```java
public void addComponent(int index,
                         Component cmp)
```

**Parameters:**
- `cmp` - 넣을 컴포넌트

**Throws:**
- `NullPointerException` - `cmp`이 `null`인 경우

### addComponent

```java
public int addComponent(Component cmp)
```

**Parameters:**
- `cmp` - 추가할 자식 컴포넌트

**Throws:**
- `NullPointerException` - `cmp`이 `null`인 경우

### setComponent

```java
public void setComponent(int index,
                         Component cmp)
```

**Parameters:**
- `cmp` - 바뀔 컴포넌트

**Throws:**

## 메서드 상세

### addComponent

```java
public void addComponent(int index,
                         Component cmp)
```

**Parameters:**
- `cmp` - 넣을 컴포넌트

**Throws:**
- `NullPointerException` - `cmp`이 `null`인 경우

### addComponent

```java
public int addComponent(Component cmp)
```

**Parameters:**
- `cmp` - 추가할 자식 컴포넌트

**Throws:**
- `NullPointerException` - `cmp`이 `null`인 경우

### setComponent

```java
public void setComponent(int index,
                         Component cmp)
```

**Parameters:**
- `cmp` - 바뀔 컴포넌트

**Throws:**
