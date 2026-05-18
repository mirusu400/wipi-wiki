# Class Layer

`package javax.microedition.lcdui.game`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.game.Layer
```

## 설명

**Direct Known Subclasses:**
- `Sprite`, `TiledLayer`

**extends Object:**

Layer는 게임의 시각적 요소를 나타내는 추상 클래스입니다. 
각 Layer는 위치(표시되는 범위 내의 왼쪽 위 모서리를 중심으로), 
너비, 높이를 포함하며 Layer의 표시 여부를 선택할 수 있습니다. 
Layer 서브 클래스는 렌더링될 수 있도록 ``paint(Graphics)`` 
메소드를 구현해야 합니다.

Layer의 위치(x,y)는 항상 Layer의 paint() 메소드에 전달된 
Graphics 객체의 좌표계와 연관되어 해석됩니다. 
이 좌표계는 *painter*의 좌표계로 불립니다. 
Layer의 처음 위치는 (0,0)입니다.

**Since:**
- MIDP 2.0

## 메서드 요약

- `int getHeight ()` — 이 계층의 현재 높이(픽셀 단위)를 가져옵니다.
- `int getWidth ()` — 이 계층의 현재 너비(픽셀 단위)를 가져옵니다.
- `int getX ()` — painter의 좌표계에서 이 Layer 왼쪽 위 모서리의 수평 위치를 가져옵니다.
- `int getY ()` — painter의 좌표계에서 이 Layer 왼쪽 위 모서리의 수직 위치를 가져옵니다.
- `boolean isVisible ()` — 이 Layer의 표시 여부를 가져옵니다.
- `void move (int dx, int dy)` — 지정한 수평 및 수직 거리를 기준으로 이 Layer를 이동합니다.
- `abstract  void paint ( Graphics g)` — Layer가 표시되면 이 Layer를 그립니다.
- `void setPosition (int x, int y)` — 왼쪽 위 모서리가 painter 좌표계의 (x,y)에 위치하도록 Layer의 위치를 설정합니다.
- `void setVisible (boolean visible)` — Layer의 표시 여부를 설정합니다.

## 메서드 상세

### setPosition

```java
public void setPosition(int x,
                        int y)
```

**Parameters:**
- `y` - 수직 위치

**See Also:**
- ``move(int, int)``, 
``getX()``, 
``getY()``

### move

```java
public void move(int dx,
                 int dy)
```

**Parameters:**
- `dy` - 세로 축을 따라 이동할 
거리(양수는 아래, 음수는 위)

**See Also:**
- ``setPosition(int, int)``, 
``getX()``, 
``getY()``

### getX

```java
public final int getX()
```

**Returns:**
- Layer의 수평 위치

**See Also:**
- ``getY()``, 
``setPosition(int, int)``, 
``move(int, int)``

### getY

```java
public final int getY()
```

**Returns:**
- Layer의 수직 위치

**See Also:**
- ``getX()``, 
``setPosition(int, int)``, 
``move(int, int)``

### getWidth

```java
public final int getWidth()
```

**Returns:**
- 너비(픽셀 단위)

**See Also:**
- ``getHeight()``

### getHeight

```java
public final int getHeight()
```

**Returns:**
- 높이(픽셀 단위)

**See Also:**
- ``getWidth()``

### setVisible

```java
public void setVisible(boolean visible)
```

**Parameters:**
- `visible` - `Layer`를 표시하려면 
`true`, 표시하지 않으려면 `false`

**See Also:**
- ``isVisible()``

### isVisible

```java
public final boolean isVisible()
```

**Returns:**
- `Layer`가 표시되면 `true`, 
표시되지 않으면 `false`

**See Also:**
- ``setVisible(boolean)``

### paint

```java
public abstract void paint(Graphics g)
```

**Parameters:**
- `g` - `Layer`를 렌더링하기 위한 그래픽 객체

**Throws:**
- `NullPointerException` - `g`가 `null`인 경우
