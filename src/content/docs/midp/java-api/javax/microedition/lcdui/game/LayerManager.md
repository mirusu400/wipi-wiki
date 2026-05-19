---
title: "Class LayerManager"
---

`package javax.microedition.lcdui.game`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.game.LayerManager
```

## 설명

**extends Object:**

LayerManager는 일련의 Layer를 관리합니다. 
LayerManager는 각 Layer의 올바른 영역을 적절한 순서로 
자동 렌더링함으로써 추가된 Layer를 
렌더링하는 과정을 단순화합니다.

LayerManager는 Layer를 추가, 삽입 및 제거할 수 있는 정렬된 
목록을 유지 관리합니다. Layer의 색인은 해당 z-order와 상관 관계가 있습니다. 
가장 높은 색인을 갖는 Layer는 사용자로부터 가장 멀리 있는 반면 
색인 0의 계층은 사용자와 가장 가깝습니다. 
색인은 항상 연속적이어야 합니다. 
즉, Layer가 제거되면 연속성을 유지하기 위해 후속 Layer의 색인이 조정됩니다.

LayerManager 클래스는 화면에서 게임의 Layer를 렌더링하는 
방법을 제어하는 몇 가지 기능을 제공합니다.

*보기 창*은 표시 가능 영역의 크기 및 
LayerManager 좌표계에 대한 위치를 제어합니다. 
보기 창의 위치를 변경하면 사용자 보기를 스크롤하거나 화면 이동하는 
효과가 발생합니다. 예를 들어, 오른쪽으로 스크롤하려면 보기 창의 
위치를 오른쪽으로 이동하면 됩니다. 
보기 창의 크기는 사용자 보기의 크기를 제어하며 대개는 
장치 화면에 적절한 크기로 고정됩니다.

이 예에서 보기 창은 85 x 85 픽셀로 설정되며 
LayerManager 좌표계의 (52, 11)에 위치합니다. 
각 Layer는 LayerManager 원점에 상대적인 위치에 표시됩니다.

``paint(Graphics, int, int)`` 메소드는 화면에 대하여 
보기 창을 렌더링할 위치를 제어하는 (x,y) 위치를 포함합니다. 
이러한 매개 변수를 변경하더라도 보기 창의 내용은 변경되지 않고 
보기 창이 그려질 위치만 변경됩니다. 
이 위치는 Graphics 객체의 원점에 상대적이므로 Graphics 
객체의 변환 속성에 종속됩니다.

예를 들어, 게임에서 화면 위쪽에 현재 점수를 표시하는 경우 
보기 창은 점수를 표시할 충분할 공간을 제공하기 위해 (17, 17)에서 
렌더링될 수 있습니다.

**Since:**
- MIDP 2.0

## 생성자 요약

- LayerManager () 새 LayerManager를 만듭니다.

## 메서드 요약

- `void append ( Layer l)` — Layer를 LayerManager에 추가합니다.
- `Layer getLayerAt (int index)` — 지정된 색인의 Layer를 가져옵니다.
- `int getSize ()` — 이 LayerManager에 있는 Layer의 수를 가져옵니다.
- `void insert ( Layer l, int index)` — 이 LayerManager의 지정된 색인에 새 Layer를 삽입합니다.
- `void paint ( Graphics g, int x, int y)` — LayerManager의 현재 보기 창을 지정된 위치에서 렌더링합니다.
- `void remove ( Layer l)` — 이 LayerManager에서 지정된 Layer를 제거합니다.
- `void setViewWindow (int x, int y, int width, int height)` — LayerManager에서 보기 창을 설정합니다.

## 생성자 상세

### LayerManager

```java
public LayerManager()
```

- 새 LayerManager를 만듭니다.

### append

```java
public void append(Layer l)
```

**Parameters:**
- `l` - 추가되는 `Layer`

**Throws:**
- `NullPointerException` - `Layer`가 
`null`인 경우

**See Also:**
- ``insert(Layer, int)``, 
``remove(Layer)``

### insert

```java
public void insert(Layer l,
                   int index)
```

**Parameters:**
- `index` - 새 `Layer`가 
삽입되는 색인

**Throws:**
- `IndexOutOfBoundsException` - 색인이 
`0`보다 작거나 
이 `LayerManager`에 이미 추가된 
Layer 수보다 큰 경우

**See Also:**
- ``append(Layer)``, 
``remove(Layer)``

### getLayerAt

```java
public Layer getLayerAt(int index)
```

**Parameters:**
- `index` - 원하는 Layer의 색인

**Returns:**
- 지정된 색인을 갖는 Layer

**Throws:**
- `IndexOutOfBoundsException` - 지정된 
`index`가 0보다 작은 경우 또는 
이 `LayerManager`에 추가된 
Layer의 수보다 큰 경우

### getSize

```java
public int getSize()
```

**Returns:**
- Layer의 수

### remove

```java
public void remove(Layer l)
```

**Parameters:**
- `l` - 제거되는 `Layer`

**Throws:**
- `NullPointerException` - 지정된 
`Layer`가 `null`인 경우

**See Also:**
- ``append(Layer)``, 
``insert(Layer, int)``

### paint

```java
public void paint(Graphics g,
                  int x,
                  int y)
```

**Parameters:**
- `y` - Graphics의 변환 원점에 상대적인 보기 창을 
렌더링할 수직 위치

**Throws:**
- `NullPointerException` - `g`가 `null`인 경우

**See Also:**
- ``setViewWindow(int, int, int, int)``

### setViewWindow

```java
public void setViewWindow(int x,
                          int y,
                          int width,
                          int height)
```

**Parameters:**
- `height` - 보기 창의 높이

**Throws:**
- `IllegalArgumentException` - `width`나 
`height`가 `0`보다 작은 경우

## 메서드 상세

### append

```java
public void append(Layer l)
```

**Parameters:**
- `l` - 추가되는 `Layer`

**Throws:**
- `NullPointerException` - `Layer`가 
`null`인 경우

**See Also:**
- ``insert(Layer, int)``, 
``remove(Layer)``

### insert

```java
public void insert(Layer l,
                   int index)
```

**Parameters:**
- `index` - 새 `Layer`가 
삽입되는 색인

**Throws:**
- `IndexOutOfBoundsException` - 색인이 
`0`보다 작거나 
이 `LayerManager`에 이미 추가된 
Layer 수보다 큰 경우

**See Also:**
- ``append(Layer)``, 
``remove(Layer)``

### getLayerAt

```java
public Layer getLayerAt(int index)
```

**Parameters:**
- `index` - 원하는 Layer의 색인

**Returns:**
- 지정된 색인을 갖는 Layer

**Throws:**
- `IndexOutOfBoundsException` - 지정된 
`index`가 0보다 작은 경우 또는 
이 `LayerManager`에 추가된 
Layer의 수보다 큰 경우

### getSize

```java
public int getSize()
```

**Returns:**
- Layer의 수

### remove

```java
public void remove(Layer l)
```

**Parameters:**
- `l` - 제거되는 `Layer`

**Throws:**
- `NullPointerException` - 지정된 
`Layer`가 `null`인 경우

**See Also:**
- ``append(Layer)``, 
``insert(Layer, int)``

### paint

```java
public void paint(Graphics g,
                  int x,
                  int y)
```

**Parameters:**
- `y` - Graphics의 변환 원점에 상대적인 보기 창을 
렌더링할 수직 위치

**Throws:**
- `NullPointerException` - `g`가 `null`인 경우

**See Also:**
- ``setViewWindow(int, int, int, int)``

### setViewWindow

```java
public void setViewWindow(int x,
                          int y,
                          int width,
                          int height)
```

**Parameters:**
- `height` - 보기 창의 높이

**Throws:**
- `IllegalArgumentException` - `width`나 
`height`가 `0`보다 작은 경우
