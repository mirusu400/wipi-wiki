# Class Card

`package org.kwis.msp.lcdui`

```
java.lang.Object
  |
  +--org.kwis.msp.lcdui.Card
```

## 설명

**Direct Known Subclasses:**
- `ProxyCard`, `TextComponent.ModeViewer`

**extends Object:**

화면에 출력될 수 있는 하나의 단위 클래스입니다.

이 클래스는 화면에 출력할 수 있는 단위가 되며 한 화면은 여러 카드가 
 쌓인 스택으로 구성됩니다.
 스택에 싸인 여러 카드는 한 화면(``Display``)에 보여집니다.
 한 카드는 여러 화면에 넣을 수는 없습니다.

카드는 화면상에서의 위치와 크기를 가지고 있습니다.
 `move`나 `resize`함수를 이용하여 
 그 위치나 크기를 변경할 수 있습니다.

`repaint`라는 함수를 사용하게 되면, 카드의 일부분에 
 대해서 다시 이벤트 
 처리 쓰레드에 의해서 `paint` 함수가 불려서 화면에 내용이 
 나타나도록 되어 있습니다.

카드는 사용자 입력을 받을 수 있습니다. 
 `keyNotify`, `pointerNotify`,
 등의 사용자에 의해서 불려지는 함수가 있으며, 
 모든 이벤트는 일단 스택 상위의 `Card`로 전달됩니다. 
 전달된 이벤트가
 그 카드에서 처리를 한다면 위의 불려지는 함수는 `true`를 돌려주며,
 그러면, 하위 `Card`는 이벤트를 받지 못합니다. 그러나 반대로 
 `false`
 를 돌려주면, 하위 카드에게 이벤트를 전달하며, 같은 식으로 이벤트를 
 받은 하위 카드는 `true`, `false`를 돌려줍니다. 
 이 과정은 맨 하위
 `Card`까지 반복이 됩니다.

카드가 입력받은 키는 기본적으로 ITU-Key '0'부터 '9' 그리고 '#', '*'
 이 가능합니다. 이 키들은 휴대폰에 꼭 존재하는 키입니다. 그외의 키들은
 게임키로 판별이 가능합니다. 지원되는 키들은 `EventQueue.UP`, 
 `EventQueue.DOWN`, `EventQueue.LEFT`, 
 `EventQueue.RIGHT`,
 `EventQueue.FIRE`등이며, `EventQueue.SOFT1`, 
 `EventQueue.SOFT2`도 있지만, 
 이 경우에는 폰에서 지원하지 않는
 경우가 있으므로 유의해서 사용하십시오.
 게임 키로 판별할 경우에는 ``Display.getGameAction(int)``와
 ``Display.getKeyCode(int)``라는 함수로 
 키 코드와 게임 키로의 서로의 변환이 가능합니다.

카드가 `pushCard`, `popCard`에 의해서 보여지거나, 
 보이지 않게되는 경우에 `showNotify`라는 
 함수가 불립니다.

좌표체계는 화면 좌측 상단이 원점이 되고, 밑으로 가면 y축의 값이 증가하고,
 오른쪽으로 가면 x축의 값이 증가하도록 되어 있습니다.

## 필드 요약

- `protected  boolean bTrans` — Card가 투명한지 아닌지 여부.
- `protected  int h` — Card의 화면상의 높이.
- `protected  int w` — Card의 화면상의 폭.
- `protected  int x` — card의 화면상의 x축 좌표.
- `protected  int y` — Card의 화면상의 y축 좌표.

## 생성자 요약

- Card () 화면 크기 만큼의 카드를 생성합니다.
- Card (boolean bTrans)
- Card ( Display d) 화면 크기의 카드를 생성합니다.
- Card ( Display d,
 int x,
 int y,
 int w,
 int h) 지정한 display를 위해서 지정한 크기와 위치로 카드를 생성합니다.
- Card ( Display d,
 int x,
 int y,
 int w,
 int h,
 boolean bTrans)
- Card (int x,
 int y,
 int w,
 int h) 지정한 크기와 위치로 카드를 생성합니다.

## 메서드 요약

- `Display getDisplay ()` — 카드의 display를 돌려줍니다.
- `int getHeight ()` — 카드의 높이를 얻어 옵니다.
- `int getWidth ()` — 카드의 폭을 얻어 옵니다.
- `int getX ()` — 카드의 x축 위치를 얻어 옵니다.
- `int getY ()` — 카드의 y축 위치를 얻어 옵니다.
- `boolean isShown ()` — Card가 화면에 보이는지 안 보이는지 여부를 돌려줍니다.
- `protected  boolean keyNotify (int type, int key)` — 사용자 키 입력이 생성되면 불립니다.
- `void move (int x, int y)` — 카드의 화면상의 위치를 변경합니다.
- `protected abstract  void paint ( Graphics g)` — Card의 내용을 그려줍니다.
- `protected  boolean pointerNotify (int type, int x, int y)` — 사용자 포인팅 디바이스의 입력이 생성되면 불립니다.
- `void repaint ()` — Card전체 영역을 다시 그려줍니다.
- `void repaint (int x, int y, int w, int h)` — 지정된 영역을 다시 그려줍니다.
- `void resize (int w, int h)` — 카드의 크기를 변경합니다. w, h 둘중 하나가 0보다 작거나 같은 경우에는 IllegalArgumentException 오류를 발생 시킵니다.
- `void serviceRepaints ()` — repaint영역을 다시 그리고, 화면에 출력합니다. repaint할 영역을 강제적으로 그립니다.
- `protected  void showNotify (boolean bShow)` — 이 카드가 보이기 바로 직전이나, 카드가 화면에서 삭제되는 경우에 불립니다.

## 필드 상세

### x

```java
protected int x
```

- card의 화면상의 x축 좌표.

### y

```java
protected int y
```

- Card의 화면상의 y축 좌표.

### w

```java
protected int w
```

- Card의 화면상의 폭.

### h

```java
protected int h
```

- Card의 화면상의 높이.

### bTrans

```java
protected boolean bTrans
```

- Card가 투명한지 아닌지 여부.

 이 옵션을 사용하면, 현재 카드 바로 하위 컴포넌트가 그린후에
 카드가 그려지므로, 알파 블랜딩이나 다양한 형태의 
 카드를 그릴 수 있습니다.

### Card

```java
public Card()
```

- 화면 크기 만큼의 카드를 생성합니다.

 기본적으로 화면의 크기 만큼의 카드를 생성합니다.
 이때 `Display.getDefaultDisplay`함수가 
 돌려주는 `Display`의 크기로 잡힙니다.

### Card

```java
public Card(boolean bTrans)
```

### Card

```java
public Card(Display d)
```

**Parameters:**
- `d` - 카드를 생성할 display

### Card

```java
public Card(int x,
            int y,
            int w,
            int h)
```

**Parameters:**
- `h` - Card의 높이

**Throws:**
- `IllegalArgumentException` - w나 h가 0 이하인 경우

### Card

```java
public Card(Display d,
            int x,
            int y,
            int w,
            int h)
```

**Parameters:**
- `h` - Card의 높이

**Throws:**
- `IllegalArgumentException` - w나 h가 0 이하인 경우

### Card

```java
public Card(Display d,
            int x,
            int y,
            int w,
            int h,
            boolean bTrans)
```

### move

```java
public void move(int x,
                 int y)
```

**Parameters:**
- `y` - Card의 display상에서의 y축 좌표

### resize

```java
public void resize(int w,
                   int h)
```

**Parameters:**
- `h` - 카드의 높이

**Throws:**
- `IllegalArgumentException` - w나 h가 0 이하인 경우

### getWidth

```java
public int getWidth()
```

**Returns:**
- 카드의 폭

### getHeight

```java
public int getHeight()
```

**Returns:**
- 카드의 높이

### getX

```java
public int getX()
```

**Returns:**
- 카드의 x축 상의 좌표

### getY

```java
public int getY()
```

**Returns:**
- 카드의 y축 상의 좌표

### showNotify

```java
protected void showNotify(boolean bShow)
```

**Parameters:**
- `bShow` - 보이는지 안보이는지 여부

### keyNotify

```java
protected boolean keyNotify(int type,
                            int key)
```

**Parameters:**
- `key` - keyCode값; 자세한 키코드는 ``EventQueue``를 참조

**Returns:**
- 하위 카드에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### pointerNotify

```java
protected boolean pointerNotify(int type,
                                int x,
                                int y)
```

**Parameters:**
- `key` - 키 코드 값

**Returns:**
- 하위 `Card`에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### paint

```java
protected abstract void paint(Graphics g)
```

**Parameters:**
- `g` - 칠해질 graphics

### repaint

```java
public void repaint(int x,
                    int y,
                    int w,
                    int h)
```

**Parameters:**
- `h` - 특정영역을 폭

### repaint

```java
public void repaint()
```

- Card전체 영역을 다시 그려줍니다.

 `repaint(0, 0, getWidth(), getHeight())`을 
 부르는것과 마찬가지 효과입니다.

### serviceRepaints

```java
public void serviceRepaints()
```

- repaint영역을 다시 그리고, 화면에 출력합니다.
 
 repaint할 영역을 강제적으로 그립니다. 이 함수 내에서 직접 paint
 함수를 부릅니다.

### isShown

```java
public boolean isShown()
```

**Returns:**
- 보이는지 안 보이는 지 여부

### getDisplay

```java
public Display getDisplay()
```

**Returns:**
- 吏

## 생성자 상세

### Card

```java
public Card()
```

- 화면 크기 만큼의 카드를 생성합니다.

 기본적으로 화면의 크기 만큼의 카드를 생성합니다.
 이때 `Display.getDefaultDisplay`함수가 
 돌려주는 `Display`의 크기로 잡힙니다.

### Card

```java
public Card(boolean bTrans)
```

### Card

```java
public Card(Display d)
```

**Parameters:**
- `d` - 카드를 생성할 display

### Card

```java
public Card(int x,
            int y,
            int w,
            int h)
```

**Parameters:**
- `h` - Card의 높이

**Throws:**
- `IllegalArgumentException` - w나 h가 0 이하인 경우

### Card

```java
public Card(Display d,
            int x,
            int y,
            int w,
            int h)
```

**Parameters:**
- `h` - Card의 높이

**Throws:**
- `IllegalArgumentException` - w나 h가 0 이하인 경우

### Card

```java
public Card(Display d,
            int x,
            int y,
            int w,
            int h,
            boolean bTrans)
```

### move

```java
public void move(int x,
                 int y)
```

**Parameters:**
- `y` - Card의 display상에서의 y축 좌표

### resize

```java
public void resize(int w,
                   int h)
```

**Parameters:**
- `h` - 카드의 높이

**Throws:**
- `IllegalArgumentException` - w나 h가 0 이하인 경우

### getWidth

```java
public int getWidth()
```

**Returns:**
- 카드의 폭

### getHeight

```java
public int getHeight()
```

**Returns:**
- 카드의 높이

### getX

```java
public int getX()
```

**Returns:**
- 카드의 x축 상의 좌표

### getY

```java
public int getY()
```

**Returns:**
- 카드의 y축 상의 좌표

### showNotify

```java
protected void showNotify(boolean bShow)
```

**Parameters:**
- `bShow` - 보이는지 안보이는지 여부

### keyNotify

```java
protected boolean keyNotify(int type,
                            int key)
```

**Parameters:**
- `key` - keyCode값; 자세한 키코드는 ``EventQueue``를 참조

**Returns:**
- 하위 카드에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### pointerNotify

```java
protected boolean pointerNotify(int type,
                                int x,
                                int y)
```

**Parameters:**
- `key` - 키 코드 값

**Returns:**
- 하위 `Card`에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### paint

```java
protected abstract void paint(Graphics g)
```

**Parameters:**
- `g` - 칠해질 graphics

### repaint

```java
public void repaint(int x,
                    int y,
                    int w,
                    int h)
```

**Parameters:**
- `h` - 특정영역을 폭

### repaint

```java
public void repaint()
```

- Card전체 영역을 다시 그려줍니다.

 `repaint(0, 0, getWidth(), getHeight())`을 
 부르는것과 마찬가지 효과입니다.

### serviceRepaints

```java
public void serviceRepaints()
```

- repaint영역을 다시 그리고, 화면에 출력합니다.
 
 repaint할 영역을 강제적으로 그립니다. 이 함수 내에서 직접 paint
 함수를 부릅니다.

### isShown

```java
public boolean isShown()
```

**Returns:**
- 보이는지 안 보이는 지 여부

### getDisplay

```java
public Display getDisplay()
```

**Returns:**
- 吏

## 메서드 상세

### move

```java
public void move(int x,
                 int y)
```

**Parameters:**
- `y` - Card의 display상에서의 y축 좌표

### resize

```java
public void resize(int w,
                   int h)
```

**Parameters:**
- `h` - 카드의 높이

**Throws:**
- `IllegalArgumentException` - w나 h가 0 이하인 경우

### getWidth

```java
public int getWidth()
```

**Returns:**
- 카드의 폭

### getHeight

```java
public int getHeight()
```

**Returns:**
- 카드의 높이

### getX

```java
public int getX()
```

**Returns:**
- 카드의 x축 상의 좌표

### getY

```java
public int getY()
```

**Returns:**
- 카드의 y축 상의 좌표

### showNotify

```java
protected void showNotify(boolean bShow)
```

**Parameters:**
- `bShow` - 보이는지 안보이는지 여부

### keyNotify

```java
protected boolean keyNotify(int type,
                            int key)
```

**Parameters:**
- `key` - keyCode값; 자세한 키코드는 ``EventQueue``를 참조

**Returns:**
- 하위 카드에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### pointerNotify

```java
protected boolean pointerNotify(int type,
                                int x,
                                int y)
```

**Parameters:**
- `key` - 키 코드 값

**Returns:**
- 하위 `Card`에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### paint

```java
protected abstract void paint(Graphics g)
```

**Parameters:**
- `g` - 칠해질 graphics

### repaint

```java
public void repaint(int x,
                    int y,
                    int w,
                    int h)
```

**Parameters:**
- `h` - 특정영역을 폭

### repaint

```java
public void repaint()
```

- Card전체 영역을 다시 그려줍니다.

 `repaint(0, 0, getWidth(), getHeight())`을 
 부르는것과 마찬가지 효과입니다.

### serviceRepaints

```java
public void serviceRepaints()
```

- repaint영역을 다시 그리고, 화면에 출력합니다.
 
 repaint할 영역을 강제적으로 그립니다. 이 함수 내에서 직접 paint
 함수를 부릅니다.

### isShown

```java
public boolean isShown()
```

**Returns:**
- 보이는지 안 보이는 지 여부

### getDisplay

```java
public Display getDisplay()
```

**Returns:**
- 吏
