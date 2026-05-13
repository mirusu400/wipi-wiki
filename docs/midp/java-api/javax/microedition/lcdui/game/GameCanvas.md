# Class GameCanvas

`package javax.microedition.lcdui.game`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Displayable
        |
        +--javax.microedition.lcdui.Canvas
              |
              +--javax.microedition.lcdui.game.GameCanvas
```

## 설명

**extends Canvas:**

GameCanvas 클래스는 게임 사용자 인터페이스 기반을 제공합니다. 
Canvas(명령, 입력 이벤트 등)로부터 상속된 기능 이외에 오프스크린 
그래픽 버퍼 및 키 상태 쿼리 기능 같은 
게임 관련 기능도 제공합니다.

각 GameCanvas 인스턴스에 대해 전용 버퍼가 만들어집니다. 
각 GameCanvas 인스턴스에 대해 고유한 버퍼가 제공되므로 
힙 사용을 최소화하기 위해 단일 GameCanvas 
인스턴스를 다시 사용하는 것이 
좋습니다. 개발자는 GameCanvas 인스턴스로부터 얻은 Graphics 객체에 
대한 호출에 의해서만 이 버퍼의 내용이 수정된다고 가정할 수 있습니다. 
다른 MIDlet이나 시스템 수준 알림 같은 외부 소스에 의해서는 
수정되지 않습니다. 버퍼는 초기에 흰색 픽셀로 채워집니다.

버퍼 크기는 GameCanvas의 최대 치수로 설정됩니다. 
하지만 플러시가 요청되면 플러시될 영역은 GameCanvas의 현재 
치수(티커, 명령 등의 존재 여부에 따라)의 제한을 받습니다. 
GameCanvas의 현재 치수는 
``getWidth``와 
``getHeight``를 
호출하여 얻을 수 있습니다.

게임은 게임 루프를 실행하기 위해 고유 스레드를 제공합니다. 
일반 루프는 입력을 검사하고 게임 논리를 구현한 다음 업데이트된 사용자 
인터페이스를 렌더링합니다. 다음 코드는 일반 게임 루프의 
구조를 설명합니다. 

```java
 // Get the Graphics object for the off-screen buffer
 Graphics g = getGraphics();
 while (true) {
      // Check user input and update positions if necessary
      int keyState = getKeyStates();
      if ((keyState & LEFT_PRESSED) != 0) {
          sprite.move(-1, 0);
      }
      else if ((keyState & RIGHT_PRESSED) != 0) {
          sprite.move(1, 0);
      }
	// Clear the background to white
	g.setColor(0xFFFFFF);
	g.fillRect(0,0,getWidth(), getHeight());
      // Draw the Sprite
      sprite.paint(g);
      // Flush the off-screen buffer
      flushGraphics();
 }
```

**Since:**
- MIDP 2.0

## 필드 요약

- `static int DOWN_PRESSED` — DOWN 키를 나타내는 비트.
- `static int FIRE_PRESSED` — FIRE 키를 나타내는 비트.
- `static int GAME_A_PRESSED` — GAME_A 키를 나타내는 비트(일부 장치에서 지원하지 않을 수 있음).
- `static int GAME_B_PRESSED` — GAME_B 키를 나타내는 비트(일부 장치에서 지원하지 않을 수 있음).
- `static int GAME_C_PRESSED` — GAME_C 키를 나타내는 비트(일부 장치에서 지원하지 않을 수 있음).
- `static int GAME_D_PRESSED` — GAME_D 키를 나타내는 비트(일부 장치에서 지원하지 않을 수 있음).
- `static int LEFT_PRESSED` — LEFT 키를 나타내는 비트.
- `static int RIGHT_PRESSED` — RIGHT 키를 나타내는 비트.
- `static int UP_PRESSED` — UP 키를 나타내는 비트.

## 생성자 요약

- `protected GameCanvas (boolean suppressKeyEvents)` — GameCanvas의 새 인스턴스를 만듭니다.

## 메서드 요약

- `void flushGraphics ()` — 오프스크린 버퍼를 디스플레이에 플러시합니다.
- `void flushGraphics (int x, int y, int width, int height)` — 오프스크린 버퍼의 지정된 영역을 디스플레이로 플러시합니다.
- `protected Graphics getGraphics ()` — GameCanvas를 렌더링하기 위한 Graphics 객체를 얻습니다.
- `int getKeyStates ()` — 물리적 게임 키의 상태를 가져옵니다.
- `void paint ( Graphics g)` — 이 GameCanvas를 그립니다.

## 필드 상세

### UP_PRESSED

```java
public static final int UP_PRESSED
```

**See Also:**
- `Constant Field Values`

### DOWN_PRESSED

```java
public static final int DOWN_PRESSED
```

**See Also:**
- `Constant Field Values`

### LEFT_PRESSED

```java
public static final int LEFT_PRESSED
```

**See Also:**
- `Constant Field Values`

### RIGHT_PRESSED

```java
public static final int RIGHT_PRESSED
```

**See Also:**
- `Constant Field Values`

### FIRE_PRESSED

```java
public static final int FIRE_PRESSED
```

**See Also:**
- `Constant Field Values`

### GAME_A_PRESSED

```java
public static final int GAME_A_PRESSED
```

**See Also:**
- `Constant Field Values`

### GAME_B_PRESSED

```java
public static final int GAME_B_PRESSED
```

**See Also:**
- `Constant Field Values`

### GAME_C_PRESSED

```java
public static final int GAME_C_PRESSED
```

**See Also:**
- `Constant Field Values`

### GAME_D_PRESSED

```java
public static final int GAME_D_PRESSED
```

**See Also:**
- `Constant Field Values`

### GameCanvas

```java
protected GameCanvas(boolean suppressKeyEvents)
```

- GameCanvas의 새 인스턴스를 만듭니다. GameCanvas에 대해서도 
새 버퍼가 만들어지며 초기에는 흰색 픽셀로 채워집니다.

개발자가 getKeyStates 메소드를 사용하여 
키 상태만 쿼리하면 되는 경우 이 GameCanvas가 표시되는 동안 
게임 키에 대해 표준 키 이벤트 기법을 억제할 수 있습니다. 
응용 프로그램에서 필요한 경우가 아니라면 키 이벤트 억제는 
keyPressed, keyRepeated 및 keyReleased 메소드에 대한 불필요한 
시스템 호출을 제거하여 성능을 향상시킬 수 있습니다.

요청하는 경우 GameCanvas가 표시되면(showNotify가 호출되면) 
지정된 GameCanvas에 대한 키 이벤트 억제가 시작되며, 
숨겨지면(hideNotify가 호출되면) 중지됩니다. 
화면 표시 및 숨기기는 이벤트 대기열을 사용하여 일련화되므로 
이러한 정렬은 억제가 해당 GameCanvas용 키 이벤트에 대해서만 
영향을 미치도록 합니다. 따라서 다른 화면이 아직 표시되는 동안 
키 이벤트가 생성된 경우 해당 화면이 숨겨지고 
GameCanvas로 대체될 때까지 
이러한 키 이벤트는 계속 대기열에 있으며 디스패치됩니다.

정의된 게임 키(UP, DOWN, FIRE 등)에 대해서만 
키 이벤트가 억제되고 다른 모든 키에 대해서는 
항상 키 이벤트가 생성됩니다.

**Parameters:**
- `suppressKeyEvents` - 게임 키에 대해 일반 키 이벤트 기법을 억제하는 경우 `true`, 
그렇지 않은 경우 `false`

### getGraphics

```java
protected Graphics getGraphics()
```

**Returns:**
- 이 GameCanvas의 오프스크린 버퍼로 
렌더링하는 Graphics 객체

**See Also:**
- ``flushGraphics()``, 
``flushGraphics(int, int, int, int)``

### getKeyStates

```java
public int getKeyStates()
```

**Returns:**
- 키 상태 정보를 포함하는 정수(키당 한 비트), 
또는 GameCanvas가 현재 표시되지 않은 경우 0

**See Also:**
- ``UP_PRESSED``, 
``DOWN_PRESSED``, 
``LEFT_PRESSED``, 
``RIGHT_PRESSED``, 
``FIRE_PRESSED``, 
``GAME_A_PRESSED``, 
``GAME_B_PRESSED``, 
``GAME_C_PRESSED``, 
``GAME_D_PRESSED``

### paint

```java
public void paint(Graphics g)
```

**Specified by:**
- `paint` in class `Canvas`

**Parameters:**
- `g` - 화면을 렌더링할 때 사용할 Graphics 객체.

**Throws:**
- `NullPointerException` - `g`가 `null`인 경우

### flushGraphics

```java
public void flushGraphics(int x,
                          int y,
                          int width,
                          int height)
```

**Parameters:**
- `height` - 플러시되는 영역의 높이

**See Also:**
- ``flushGraphics()``

### flushGraphics

```java
public void flushGraphics()
```

**See Also:**
- ``flushGraphics(int,int,int,int)``

## 생성자 상세

### GameCanvas

```java
protected GameCanvas(boolean suppressKeyEvents)
```

- GameCanvas의 새 인스턴스를 만듭니다. GameCanvas에 대해서도 
새 버퍼가 만들어지며 초기에는 흰색 픽셀로 채워집니다.

개발자가 getKeyStates 메소드를 사용하여 
키 상태만 쿼리하면 되는 경우 이 GameCanvas가 표시되는 동안 
게임 키에 대해 표준 키 이벤트 기법을 억제할 수 있습니다. 
응용 프로그램에서 필요한 경우가 아니라면 키 이벤트 억제는 
keyPressed, keyRepeated 및 keyReleased 메소드에 대한 불필요한 
시스템 호출을 제거하여 성능을 향상시킬 수 있습니다.

요청하는 경우 GameCanvas가 표시되면(showNotify가 호출되면) 
지정된 GameCanvas에 대한 키 이벤트 억제가 시작되며, 
숨겨지면(hideNotify가 호출되면) 중지됩니다. 
화면 표시 및 숨기기는 이벤트 대기열을 사용하여 일련화되므로 
이러한 정렬은 억제가 해당 GameCanvas용 키 이벤트에 대해서만 
영향을 미치도록 합니다. 따라서 다른 화면이 아직 표시되는 동안 
키 이벤트가 생성된 경우 해당 화면이 숨겨지고 
GameCanvas로 대체될 때까지 
이러한 키 이벤트는 계속 대기열에 있으며 디스패치됩니다.

정의된 게임 키(UP, DOWN, FIRE 등)에 대해서만 
키 이벤트가 억제되고 다른 모든 키에 대해서는 
항상 키 이벤트가 생성됩니다.

**Parameters:**
- `suppressKeyEvents` - 게임 키에 대해 일반 키 이벤트 기법을 억제하는 경우 `true`, 
그렇지 않은 경우 `false`

### getGraphics

```java
protected Graphics getGraphics()
```

**Returns:**
- 이 GameCanvas의 오프스크린 버퍼로 
렌더링하는 Graphics 객체

**See Also:**
- ``flushGraphics()``, 
``flushGraphics(int, int, int, int)``

### getKeyStates

```java
public int getKeyStates()
```

**Returns:**
- 키 상태 정보를 포함하는 정수(키당 한 비트), 
또는 GameCanvas가 현재 표시되지 않은 경우 0

**See Also:**
- ``UP_PRESSED``, 
``DOWN_PRESSED``, 
``LEFT_PRESSED``, 
``RIGHT_PRESSED``, 
``FIRE_PRESSED``, 
``GAME_A_PRESSED``, 
``GAME_B_PRESSED``, 
``GAME_C_PRESSED``, 
``GAME_D_PRESSED``

### paint

```java
public void paint(Graphics g)
```

**Specified by:**
- `paint` in class `Canvas`

**Parameters:**
- `g` - 화면을 렌더링할 때 사용할 Graphics 객체.

**Throws:**
- `NullPointerException` - `g`가 `null`인 경우

### flushGraphics

```java
public void flushGraphics(int x,
                          int y,
                          int width,
                          int height)
```

**Parameters:**
- `height` - 플러시되는 영역의 높이

**See Also:**
- ``flushGraphics()``

### flushGraphics

```java
public void flushGraphics()
```

**See Also:**
- ``flushGraphics(int,int,int,int)``

## 메서드 상세

### getGraphics

```java
protected Graphics getGraphics()
```

**Returns:**
- 이 GameCanvas의 오프스크린 버퍼로 
렌더링하는 Graphics 객체

**See Also:**
- ``flushGraphics()``, 
``flushGraphics(int, int, int, int)``

### getKeyStates

```java
public int getKeyStates()
```

**Returns:**
- 키 상태 정보를 포함하는 정수(키당 한 비트), 
또는 GameCanvas가 현재 표시되지 않은 경우 0

**See Also:**
- ``UP_PRESSED``, 
``DOWN_PRESSED``, 
``LEFT_PRESSED``, 
``RIGHT_PRESSED``, 
``FIRE_PRESSED``, 
``GAME_A_PRESSED``, 
``GAME_B_PRESSED``, 
``GAME_C_PRESSED``, 
``GAME_D_PRESSED``

### paint

```java
public void paint(Graphics g)
```

**Specified by:**
- `paint` in class `Canvas`

**Parameters:**
- `g` - 화면을 렌더링할 때 사용할 Graphics 객체.

**Throws:**
- `NullPointerException` - `g`가 `null`인 경우

### flushGraphics

```java
public void flushGraphics(int x,
                          int y,
                          int width,
                          int height)
```

**Parameters:**
- `height` - 플러시되는 영역의 높이

**See Also:**
- ``flushGraphics()``

### flushGraphics

```java
public void flushGraphics()
```

**See Also:**
- ``flushGraphics(int,int,int,int)``
