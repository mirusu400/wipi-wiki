# Class Canvas

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Displayable
        |
        +--javax.microedition.lcdui.Canvas
```

## 설명

**Direct Known Subclasses:**
- `GameCanvas`

**extends Displayable:**

`Canvas` 클래스는 
낮은 수준의 이벤트를 처리하고 
디스플레이로 이동하기 위한 그래픽을 
호출해야 하는 응용 프로그램을 
작성하기 위한 기본 클래스입니다. 
대체로 게임 응용 프로그램에서 
`Canvas` 클래스를 많이 사용합니다. 
응용 프로그램 개발 면에서 보자면 `Canvas` 클래스는 
표준 `Screen` 클래스와 바꾸어 사용할 수 있으므로 
응용 프로그램은 필요한 경우 높은 수준 화면과 
`Canvas`를 혼합하여 일치시킬 수 있습니다. 
예를 들어, List 화면은 레이싱 게임 추적을 선택하는 데 사용되며 
`Canvas` 서브 클래스는 실제 게임을 구현합니다.

`Canvas`는 개발자에게 게임 동작, 
키 이벤트 및 포인터 이벤트(장치에서 지원하는 경우)를 
처리하는 메소드를 제공합니다. 또한 장치의 기능 및 
게임 작업에 대한 키 매핑을 
식별하기 위한 메소드가 제공됩니다. 
키 이벤트는 *키 코드*에 관하여 보고되며, 
키 코드는 장치의 실제 키에 직접 바운드되므로 
키 코드를 사용하면 이식 가능성이 줄어듭니다. 
이식 가능 응용 프로그램은 키 코드 대신 게임 
작업을 사용해야 합니다.

`Displayable`의 다른 서브 클래스와 
마찬가지로 `Canvas` 클래스를 사용하면 
응용 프로그램은 명령의 수신기를 등록할 수 있습니다. 
하지만 다른 `Displayables`와는 
달리 `Canvas` 클래스에서는 응용 프로그램이 
해당 클래스를 분류하여 사용해야 합니다. 
`paint()` 메소드는 `abstract`로 선언되므로 
응용 프로그램은 해당 서브 클래스 내에 
*반드시* 구현을 제공해야 합니다. 
다른 이벤트 보고 메소드는 `abstract`로 선언되지 않으므로 
기본 구현은 비어 있습니다(즉, 아무 작업도 하지 않음). 
따라서 응용 프로그램은 관심 있는 이벤트를 보고하는 
메소드만 무시할 수 있습니다.

이 클래스는 응용 프로그램이 수신기를 정의하고 `Screen` 클래스의 
인스턴스를 사용하여 이를 등록할 수 있도록 허용하는 
``Screen`` 클래스와는 대조적입니다. 
전달되어야 하는 각 이벤트 종류별로 하나씩 여러 개의 새 수신기 인터페이스를 
만들어야 하기 때문에 이 스타일은 `Canvas` 클래스에 
사용되지 않습니다. 보다 적은 수신기 인터페이스를 갖도록 하는 것이 
대안이 될 수는 있지만, 이 경우 수신기는 관심이 없는 
이벤트를 필터링해야 합니다.

### 키 이벤트

응용 프로그램은 *키 코드*의 공간 내에서 
개별 키의 이름이 지정된 키입력 이벤트를 받습니다. 
MIDP 응용 프로그램에 이벤트를 보고하는 각 키에는 키 코드가 할당됩니다. 
두 키가 서로에 대해 정확히 동일한 기능을 하지 않는 이상 
키 코드 값은 각 하드웨어 키에 고유합니다. 
MIDP에는 
``KEY_NUM0``, 
``KEY_NUM1``, 
``KEY_NUM2``, 
``KEY_NUM3``, 
``KEY_NUM4``, 
``KEY_NUM5``, 
``KEY_NUM6``, 
``KEY_NUM7``, 
``KEY_NUM8``, 
``KEY_NUM9``, 
``KEY_STAR`` 및
``KEY_POUND``와 같은 키 코드가 정의되어 있습니다.

이러한 키 코드는 ITU-T 표준 전화 키패드의 키에 해당합니다. 
다른 키가 키보드에 있을 수 있으며 일반적으로 위의 목록과 구별되는 
키 코드를 가집니다. 이식 가능성을 보장하려면 응용 프로그램에서 
해당 표준 키 코드만 사용해야 합니다.

표준 키 코드 값은 키를 나타내는 
문자의 유니코드 인코딩과 같습니다. 
장치에 유니코드 문자와 정확하게 일치하는 다른 키가 포함되어 있는 경우 
이러한 키 코드 값은 해당 문자의 유니코드 인코딩과 같아야 합니다. 
일치하는 유니코드 문자가 없는 키의 경우 구현 시 음수 값을 사용해야 합니다. 
0은 잘못된 키 코드로 정의됩니다. 
다음 코드를 사용하여 응용 프로그램에서 키 코드를 유니코드로 
변환할 수 있습니다.

if (keyCode > 0) {
 char ch = (char)keyCode; 
 // ...
 }

이 기술은 제한된 특정 경우에만 유용합니다. 
특히 대문자와 소문자, 키보드 shift 키 상태, 
두 개 이상의 키입력을 요구하는 문자를 처리하지 않기 때문에 
전체 텍스트 입력에 충분하지 않습니다. 텍스트 입력을 위해서 
응용 프로그램은 항상 ``TextBox`` 또는 
``TextField`` 객체를 사용해야 합니다.

때로 이 키에 대한 메시지를 표시하기 위해 
키의 *이름*을 찾는 것이 유용한 경우도 있습니다. 
이 경우 응용 프로그램은 ``getKeyName()`` 메소드를 사용하여 키 이름을 찾을 수 있습니다.

### 게임 작업

화살표 키 이벤트와 게임 관련 이벤트가 필요한 
이식 가능 응용 프로그램은 키 코드와 키 이름보다는 *게임 작업*을 
사용해야 합니다. MIDP에는 
``UP``, 
``DOWN``, 
``LEFT``, 
``RIGHT``, 
``FIRE``, 
``GAME_A``, 
``GAME_B``, 
``GAME_C`` 및 
``GAME_D``와 같은 게임 작업이 정의됩니다.

각 키 코드는 기껏해야 하나의 게임 작업에 매핑될 수 있습니다. 
하지만 게임 작업은 두 개 이상의 키 코드와 연관됩니다. 
응용 프로그램은 ``getGameAction(int keyCode)`` 
메소드를 사용하여 키 코드를 게임 작업으로 변환할 수 있으며 
``getKeyCode(int gameAction)`` 메소드를 사용하여 
게임 작업을 키 코드로 변환할 수 있습니다. 
특정 게임 작업과 연관된 키 코드는 여러 개 있을 수 있지만 
`getKeyCode`는 이러한 키 코드 중 하나만 반환합니다. 
`g`가 유효한 게임 작업이고 `k`가 게임 작업과 
연관된 키에 대해 유효한 키 코드인 경우 다음 표현식을 고려합니다.

g == getGameAction(getKeyCode(g)) // (1)
 k == getKeyCode(getGameAction(k)) // (2)

표현식 (1)은 *항상* true입니다. 
하지만 표현식 (2)는 true일 수도 있지만 *반드시 true인 것은 아닙니다*.

구현 시에는 응용 프로그램 실행 도중 게임 작업 및 키 코드의 매핑을 
변경할 수 없습니다.

게임 작업을 사용하려는 이식 가능 응용 프로그램은 
``getGameAction()`` 메소드를 호출한 다음 
결과를 테스트하여 각 키 이벤트를 게임 작업으로 변환해야 합니다. 
예를 들어, 일부 장치에서 게임 작업 `UP`, 
`DOWN`, `LEFT` 및 `RIGHT`는 
네 방향의 이동 화살표 키에 매핑됩니다. 
이 경우 `getKeyCode(UP)`는 위쪽 화살표 키에 대해 
장치 종속 코드를 반환합니다. 
다른 장치의 경우 가능한 매핑은 번호 키 `2`, 
`4`, `6` 및 `8`에 있습니다. 
이 경우 `getKeyCode(UP)`는 
`KEY_NUM2`를 반환합니다. 
두 경우 모두 사용자가 장치에서 "실제로 왼쪽에 있는" 키를 
누르면 `getGameAction()` 메소드는 `LEFT` 
게임 작업을 반환합니다.

### 명령

또한 현재 캔버스를 사용 중인 경우 
사용자는 ``commands``를 실행할 수 있습니다. 
`Commands`는 장치별 
고유 방식으로 키와 메뉴에 매핑됩니다. 
일부 장치의 경우 명령에 사용된 키는 키 코드 이벤트를 캔버스에 전달할 키와 
중복됩니다. 이 경우 장치는 이러한 키가 명령이나 
키 코드 이벤트를 응용 프로그램에 전달할 것인지 여부를 결정하는 모드를 
사용자가 선택하도록 허용하는 응용 프로그램에 투명한 수단을 제공합니다. 
`Canvas`가 표준 모드에 있는 경우(아래 참조), 
캔버스에 사용 가능한 일련의 키 코드 이벤트는 
현재의 명령 개수나 명령 수신기의 존재에 따라 변경되지 않습니다. 
`Canvas`가 전체 화면 모드에 있으며 명령 수신기가 없는 경우 
장치는 명령 전달을 위해 예약될 수도 있는 키에 대한 
키 코드 이벤트 전달을 선택합니다. 
게임 개발자는 명령에 대한 액세스가 
장치별로 크게 달라지며 게임 도중 사용자에게 명령 실행을 요구하면 
실행 가능한 게임의 용이성에 
큰 영향을 미칠 수 있음을 알아야 합니다.

### 이벤트 전달

`Canvas` 객체는 구현 시 호출되는 
여러 메소드를 정의합니다. 
이러한 메소드는 대개 응용 프로그램에 이벤트를 전달하는 것이 목적이므로 
이를 *이벤트 전달* 메소드라고 합니다. 
일련의 메소드는 다음과 같습니다.

- `showNotify()`
- `hideNotify()`
- `keyPressed()`
- `keyRepeated()`
- `keyReleased()`
- `pointerPressed()`
- `pointerDragged()`
- `pointerReleased()`
- `paint()`

이러한 메소드는 연속적으로 모두 호출됩니다. 
즉, 구현 시 이벤트 전달 메소드 중 *하나*에 대한 
이전 호출이 반환되어야 이벤트 전달 메소드를 호출할 수 있습니다. 
`serviceRepaints()` 메소드는 `paint()`가 
호출되어 반환될 때까지 차단되므로 이 규칙에 대한 예외가 됩니다. 
이러한 예외는 이벤트 전달 메소드 중 하나에 있는 
해당 응용 프로그램에서 `serviceRepaints()`를 호출하는 경우에도 발생합니다.

``Display.callSerially()`` 메소드는 
이벤트 스트림을 사용하여 일부 응용 프로그램 정의 작업을 일련화하는 데 
사용할 수 있습니다. 자세한 내용은 패키지 요약의 
`이벤트 처리` 및 
`동시 처리` 절을 
참조하십시오.

키 관련, 포인터 관련 및 `paint()` 메소드는 
`Canvas`가 출력 장치에 
실제로 표시되는 동안만 호출됩니다. 
그러므로 이러한 메소드는 `showNotify()`에 대한 호출 이후 
및 `hideNotify()`에 대한 호출 이전에 
이 `Canvas` 객체에서만 호출됩니다. 
`hideNotify()`가 호출된 다음에는 
`showNotify()`에 대한 후속 호출이 반환될 때까지 
키, 포인터 및 `paint` 메소드 중 
어느 것도 호출되지 않습니다. 
`callSerially()`에서 발생하는 
`run()` 메소드에 대한 호출은 
`showNotify()` 
및 `hideNotify()`에 대한 호출과 상관없이 발생합니다.

``showNotify()`` 메소드는 
`Canvas`가 실제로 
디스플레이에 표시되기 전에 호출되며 
``hideNotify()`` 
메소드는 `Canvas`가 
디스플레이에서 제거된 다음 호출됩니다. 
`Canvas`의 표시 상태(또는 
다른 `Displayable` 
객체)는 ``Displayable.isShown()`` 메소드를 
사용하여 쿼리할 수 있습니다. 
`Canvas`의 표시 상태는 
포그라운드와 백그라운드 상태 사이에서 
`MIDlet`을 이동하는 
응용 프로그램 관리 소프트웨어에 의해 또는 시스템 화면을 사용하여 
`Canvas`를 흐리게 만드는 
시스템에 의해 변경됩니다. 
따라서 `showNotify()` 및 
`hideNotify()`에 대한 
호출은 `MIDlet`의 제어를 받지 않으므로 
상당히 자주 발생할 수 있습니다. 
응용 프로그램 개발자가 경량을 
최소로 유지하려면 비용이 많이 드는 
설치 및 분해 작업은 `showNotify()`와 
`hideNotify()` 메소드 밖에서 
수행하는 것이 좋습니다.

`Canvas`는 표준 모드나 
전체 화면 모드에 있을 수 있습니다. 
표준 모드에서 디스플레이의 공간은 명령 레이블, 제목 및 티커가 
차지할 수 있습니다. 
`Canvas`를 전체 화면 모드로 설정하면 
응용 프로그램은 `Canvas`가 
디스플레이 공간을 가능한 한 많이 차지하도록 요청합니다. 
전체 화면 모드에서는 제목 및 티커가 
`Canvas`에 있더라도 
표시되지 않으며 `Commands`는 
몇 가지 대체 수단(팝업 메뉴를 통하는 등)을 사용하여 표시됩니다. 
표시된 `Canvas`가 
전체 화면 모드에 있더라도 
구현 시에는 상태 표시기 등에 디스플레이의 일부분을 할애합니다. 
전체 화면 모드에서 제목은 표시되지 않더라도 
해당 텍스트는 `Commands`의 팝업 메뉴 제목 등 
다른 용도로 계속 사용될 수 있습니다.

`Canvas` 객체는 기본적으로 표준 모드에 있습니다. 
표준 대 전체 화면 모드 설정은 ``setFullScreenMode(boolean)`` 메소드 
사용을 통해 제어됩니다.

``setFullScreenMode(boolean)``를 호출하면 
``sizeChanged()``가 호출될 수 있습니다. 
이 메소드의 기본 구현은 어떤 작업도 하지 않습니다. 
응용 프로그램은 사용 가능한 그리기 영역 크기에서 
변경 내용을 처리하기 위해 이 메소드를 무시할 수 있습니다.

**주:** 개요의 "사양 요구 사항" 절에서 
언급한 대로 구현 시 사용자에게 
네트워크 사용에 대한 표시를 
제공해야 합니다. 표시기가 화면에 제공되는 경우에는 
`Canvas`가 전체 화면 모드에 있어도 
네트워크 활동이 발생하면 표시되어야 합니다.

**Since:**
- MIDP 1.0

## 필드 요약

- `static int DOWN` — DOWN 게임 작업의 상수.
- `static int FIRE` — FIRE 게임 작업의 상수.
- `static int GAME_A` — 일반 용도 " A " 게임 작업의 상수.
- `static int GAME_B` — 일반 용도 " B " 게임 작업의 상수.
- `static int GAME_C` — 일반 용도 " C " 게임 작업의 상수.
- `static int GAME_D` — 일반 용도 " D " 게임 작업의 상수.
- `static int KEY_NUM0` — ITU-T 키 0 의 키 코드.
- `static int KEY_NUM1` — ITU-T 키 1 의 키 코드.
- `static int KEY_NUM2` — ITU-T 키 2 의 키 코드.
- `static int KEY_NUM3` — ITU-T 키 3 의 키 코드.
- `static int KEY_NUM4` — ITU-T 키 4 의 키 코드.
- `static int KEY_NUM5` — ITU-T 키 5 의 키 코드.
- `static int KEY_NUM6` — ITU-T 키 6 의 키 코드.
- `static int KEY_NUM7` — ITU-T 키 7 의 키 코드.
- `static int KEY_NUM8` — ITU-T 키 8 의 키 코드.
- `static int KEY_NUM9` — ITU-T 키 9 의 키 코드.
- `static int KEY_POUND` — ITU-T 키 "파운드"( # )의 키 코드.
- `static int KEY_STAR` — ITU-T 키 "스타"( * )의 키 코드.
- `static int LEFT` — LEFT 게임 작업의 상수.
- `static int RIGHT` — RIGHT 게임 작업의 상수.
- `static int UP` — UP 게임 작업의 상수.

## 생성자 요약

- `protected Canvas ()` — 새 Canvas 객체를 구성합니다.

## 메서드 요약

- `int getGameAction (int keyCode)` — 장치의 지정된 키 코드와 연관된 게임 작업을 가져옵니다.
- `int getHeight ()` — Canvas 의 디스플레이 가능 영역의 높이를 픽셀 단위로 가져옵니다.
- `int getKeyCode (int gameAction)` — 장치에 지정된 게임 작업에 해당하는 키 코드를 가져옵니다.
- `String getKeyName (int keyCode)` — 키에 대한 정보가 들어 있는 키 문자열을 가져옵니다.
- `int getWidth ()` — Canvas 의 디스플레이 가능 영역의 너비를 픽셀 단위로 가져옵니다.
- `boolean hasPointerEvents ()` — 플랫폼이 포인터 누르기 및 놓기 이벤트를 지원하는지 검사합니다.
- `boolean hasPointerMotionEvents ()` — 플랫폼이 포인터 모션 이벤트(포인터 끌기)를 지원하는지 검사합니다.
- `boolean hasRepeatEvents ()` — 키를 누른 채로 있을 때 플랫폼에서 반복 이벤트를 생성할 수 있는지 검사합니다.
- `protected  void hideNotify ()` — 구현 시 Canvas 가 디스플레이에서 제거된 다음 바로 hideNotify() 를 호출합니다.
- `boolean isDoubleBuffered ()` — 구현 시 Canvas 가 이중 버퍼되었는지 검사합니다.
- `protected  void keyPressed (int keyCode)` — 키를 누르면 호출됩니다.
- `protected  void keyReleased (int keyCode)` — 키를 놓으면 호출됩니다.
- `protected  void keyRepeated (int keyCode)` — 키가 반복되면(누른 채로 있으면) 호출됩니다.
- `protected abstract  void paint ( Graphics g)` — Canvas 를 렌더링합니다.
- `protected  void pointerDragged (int x, int y)` — 포인터를 끌면 호출됩니다.
- `protected  void pointerPressed (int x, int y)` — 포인터를 누르면 호출됩니다.
- `protected  void pointerReleased (int x, int y)` — 포인터를 놓으면 호출됩니다.
- `void repaint ()` — 전체 Canvas 에 대해 다시 그리기를 요청합니다.
- `void repaint (int x, int y, int width, int height)` — Canvas 의 지정한 영역에 대해 다시 그리기를 요청합니다.
- `void serviceRepaints ()` — 보류 중인 다시 그리기 요청이 즉시 처리되도록 합니다.
- `void setFullScreenMode (boolean mode)` — Canvas 를 전체 화면 모드에 둘지 표준 모드에 둘지 여부를 제어합니다.
- `protected  void showNotify ()` — 구현 시 Canvas 가 디스플레이에 표시되기 전에 바로 showNotify() 를 호출합니다.
- `protected  void sizeChanged (int w, int h)` — Canvas 의 그리기 가능 영역이 변경되면 호출됩니다.

## 필드 상세

### UP

```java
public static final int UP
```

**See Also:**
- `Constant Field Values`

### DOWN

```java
public static final int DOWN
```

**See Also:**
- `Constant Field Values`

### LEFT

```java
public static final int LEFT
```

**See Also:**
- `Constant Field Values`

### RIGHT

```java
public static final int RIGHT
```

**See Also:**
- `Constant Field Values`

### FIRE

```java
public static final int FIRE
```

**See Also:**
- `Constant Field Values`

### GAME_A

```java
public static final int GAME_A
```

**See Also:**
- `Constant Field Values`

### GAME_B

```java
public static final int GAME_B
```

**See Also:**
- `Constant Field Values`

### GAME_C

```java
public static final int GAME_C
```

**See Also:**
- `Constant Field Values`

### GAME_D

```java
public static final int GAME_D
```

**See Also:**
- `Constant Field Values`

### KEY_NUM0

```java
public static final int KEY_NUM0
```

**See Also:**
- `Constant Field Values`

### KEY_NUM1

```java
public static final int KEY_NUM1
```

**See Also:**
- `Constant Field Values`

### KEY_NUM2

```java
public static final int KEY_NUM2
```

**See Also:**
- `Constant Field Values`

### KEY_NUM3

```java
public static final int KEY_NUM3
```

**See Also:**
- `Constant Field Values`

### KEY_NUM4

```java
public static final int KEY_NUM4
```

**See Also:**
- `Constant Field Values`

### KEY_NUM5

```java
public static final int KEY_NUM5
```

**See Also:**
- `Constant Field Values`

### KEY_NUM6

```java
public static final int KEY_NUM6
```

**See Also:**
- `Constant Field Values`

### KEY_NUM7

```java
public static final int KEY_NUM7
```

**See Also:**
- `Constant Field Values`

### KEY_NUM8

```java
public static final int KEY_NUM8
```

**See Also:**
- `Constant Field Values`

### KEY_NUM9

```java
public static final int KEY_NUM9
```

**See Also:**
- `Constant Field Values`

### KEY_STAR

```java
public static final int KEY_STAR
```

**See Also:**
- `Constant Field Values`

### KEY_POUND

```java
public static final int KEY_POUND
```

**See Also:**
- `Constant Field Values`

### Canvas

```java
protected Canvas()
```

- 새 `Canvas` 객체를 구성합니다.

### getWidth

```java
public int getWidth()
```

**Overrides:**
- `getWidth` in class `Displayable`

**Returns:**
- 디스플레이 가능 영역의 너비

### getHeight

```java
public int getHeight()
```

**Overrides:**
- `getHeight` in class `Displayable`

**Returns:**
- 디스플레이 가능 영역의 높이

### isDoubleBuffered

```java
public boolean isDoubleBuffered()
```

**Returns:**
- 이중 버퍼된 경우 `true`, 
그렇지 않으면 `false`입니다.

### hasPointerEvents

```java
public boolean hasPointerEvents()
```

**Returns:**
- 장치에서 포인터 이벤트를 지원하는 경우 `true`입니다.

### hasPointerMotionEvents

```java
public boolean hasPointerMotionEvents()
```

**Returns:**
- 장치에서 포인터 모션 이벤트를 지원하는 경우 `true`입니다.

### hasRepeatEvents

```java
public boolean hasRepeatEvents()
```

**Returns:**
- 장치에서 반복 이벤트를 지원하는 경우 `true`입니다.

### getKeyCode

```java
public int getKeyCode(int gameAction)
```

**Parameters:**
- `gameAction` - 게임 작업

**Returns:**
- 이 게임 작업에 해당하는 키 코드

**Throws:**
- `IllegalArgumentException` - `gameAction`이 
유효한 게임 작업이 아닌 경우

### getKeyName

```java
public String getKeyName(int keyCode)
```

**Parameters:**
- `keyCode` - 요청된 키 코드

**Returns:**
- 키의 문자열 이름

**Throws:**
- `IllegalArgumentException` - `keyCode`가 
유효한 키 코드가 아닌 경우

### getGameAction

```java
public int getGameAction(int keyCode)
```

**Parameters:**
- `keyCode` - 키 코드

**Returns:**
- 이 키에 해당하는 게임 작업, 또는 해당 게임 작업이 없는 경우 
`0`

**Throws:**
- `IllegalArgumentException` - `keyCode`가 
유효한 키 코드가 아닌 경우

### setFullScreenMode

```java
public void setFullScreenMode(boolean mode)
```

**Parameters:**
- `mode` - `Canvas`가 전체 화면 모드에 있으면 
`true`, 그렇지 않은 경우 `false`

**Since:**
- MIDP 2.0

### keyPressed

```java
protected void keyPressed(int keyCode)
```

**Parameters:**
- `keyCode` - 누른 키에 대한 키 코드

### keyRepeated

```java
protected void keyRepeated(int keyCode)
```

**Parameters:**
- `keyCode` - 반복된 키에 대한 키 코드

**See Also:**
- ``hasRepeatEvents()``

### keyReleased

```java
protected void keyReleased(int keyCode)
```

**Parameters:**
- `keyCode` - 해제된 키에 대한 키 코드

### pointerPressed

```java
protected void pointerPressed(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터를 누른 수직 
위치(`Canvas`에 상대적)

### pointerReleased

```java
protected void pointerReleased(int x,
                               int y)
```

**Parameters:**
- `y` - 포인터를 놓은 수직 
위치(`Canvas`에 상대적)

### pointerDragged

```java
protected void pointerDragged(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터를 끈 수직 
위치(`Canvas`에 상대적)

### repaint

```java
public final void repaint(int x,
                          int y,
                          int width,
                          int height)
```

**Parameters:**
- `height` - 다시 그릴 직사각형의 높이

**See Also:**
- ``Display.callSerially(Runnable)``, 
``serviceRepaints()``

### repaint

```java
public final void repaint()
```

전체 Canvas 에 대해 다시 그리기를 요청합니다. 
결과는 다음과 같습니다. repaint(0, 0, getWidth(), getHeight());

### serviceRepaints

```java
public final void serviceRepaints()
```

**See Also:**
- ``Display.callSerially(Runnable)``

### showNotify

```java
protected void showNotify()
```

구현 시 Canvas 가 
디스플레이에 표시되기 전에 바로 showNotify() 를 호출합니다. 
Canvas 서브 클래스는 애니메이션 설정, 
타이머 시작 등이 표시되기 전에 
작업을 수행하기 위해 이 메소드를 무시할 수 있습니다. Canvas 클래스에 있는 이 메소드의 
기본 구현은 비어 있습니다.

### hideNotify

```java
protected void hideNotify()
```

구현 시 Canvas 가 
디스플레이에서 제거된 다음 
바로 hideNotify() 를 호출합니다. Canvas 서브 클래스는 애니메이션 일시 중지, 
타이머 해지 등의 작업을 수행하기 위해 
이 메소드를 무시할 수 있습니다. Canvas 클래스에서 
이 메소드의 기본 구현은 비어 있습니다.

### paint

```java
protected abstract void paint(Graphics g)
```

**Parameters:**
- `g` - `Canvas` 렌더링에 사용된 `Graphics` 
객체

### sizeChanged

```java
protected void sizeChanged(int w,
                           int h)
```

**Overrides:**
- `sizeChanged` in class `Displayable`

**Parameters:**
- `h` - `Canvas` 그리기 가능 
영역의 새 높이(픽셀 단위)

**Since:**
- MIDP 2.0

## 생성자 상세

### Canvas

```java
protected Canvas()
```

- 새 `Canvas` 객체를 구성합니다.

### getWidth

```java
public int getWidth()
```

**Overrides:**
- `getWidth` in class `Displayable`

**Returns:**
- 디스플레이 가능 영역의 너비

### getHeight

```java
public int getHeight()
```

**Overrides:**
- `getHeight` in class `Displayable`

**Returns:**
- 디스플레이 가능 영역의 높이

### isDoubleBuffered

```java
public boolean isDoubleBuffered()
```

**Returns:**
- 이중 버퍼된 경우 `true`, 
그렇지 않으면 `false`입니다.

### hasPointerEvents

```java
public boolean hasPointerEvents()
```

**Returns:**
- 장치에서 포인터 이벤트를 지원하는 경우 `true`입니다.

### hasPointerMotionEvents

```java
public boolean hasPointerMotionEvents()
```

**Returns:**
- 장치에서 포인터 모션 이벤트를 지원하는 경우 `true`입니다.

### hasRepeatEvents

```java
public boolean hasRepeatEvents()
```

**Returns:**
- 장치에서 반복 이벤트를 지원하는 경우 `true`입니다.

### getKeyCode

```java
public int getKeyCode(int gameAction)
```

**Parameters:**
- `gameAction` - 게임 작업

**Returns:**
- 이 게임 작업에 해당하는 키 코드

**Throws:**
- `IllegalArgumentException` - `gameAction`이 
유효한 게임 작업이 아닌 경우

### getKeyName

```java
public String getKeyName(int keyCode)
```

**Parameters:**
- `keyCode` - 요청된 키 코드

**Returns:**
- 키의 문자열 이름

**Throws:**
- `IllegalArgumentException` - `keyCode`가 
유효한 키 코드가 아닌 경우

### getGameAction

```java
public int getGameAction(int keyCode)
```

**Parameters:**
- `keyCode` - 키 코드

**Returns:**
- 이 키에 해당하는 게임 작업, 또는 해당 게임 작업이 없는 경우 
`0`

**Throws:**
- `IllegalArgumentException` - `keyCode`가 
유효한 키 코드가 아닌 경우

### setFullScreenMode

```java
public void setFullScreenMode(boolean mode)
```

**Parameters:**
- `mode` - `Canvas`가 전체 화면 모드에 있으면 
`true`, 그렇지 않은 경우 `false`

**Since:**
- MIDP 2.0

### keyPressed

```java
protected void keyPressed(int keyCode)
```

**Parameters:**
- `keyCode` - 누른 키에 대한 키 코드

### keyRepeated

```java
protected void keyRepeated(int keyCode)
```

**Parameters:**
- `keyCode` - 반복된 키에 대한 키 코드

**See Also:**
- ``hasRepeatEvents()``

### keyReleased

```java
protected void keyReleased(int keyCode)
```

**Parameters:**
- `keyCode` - 해제된 키에 대한 키 코드

### pointerPressed

```java
protected void pointerPressed(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터를 누른 수직 
위치(`Canvas`에 상대적)

### pointerReleased

```java
protected void pointerReleased(int x,
                               int y)
```

**Parameters:**
- `y` - 포인터를 놓은 수직 
위치(`Canvas`에 상대적)

### pointerDragged

```java
protected void pointerDragged(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터를 끈 수직 
위치(`Canvas`에 상대적)

### repaint

```java
public final void repaint(int x,
                          int y,
                          int width,
                          int height)
```

**Parameters:**
- `height` - 다시 그릴 직사각형의 높이

**See Also:**
- ``Display.callSerially(Runnable)``, 
``serviceRepaints()``

### repaint

```java
public final void repaint()
```

전체 Canvas 에 대해 다시 그리기를 요청합니다. 
결과는 다음과 같습니다. repaint(0, 0, getWidth(), getHeight());

### serviceRepaints

```java
public final void serviceRepaints()
```

**See Also:**
- ``Display.callSerially(Runnable)``

### showNotify

```java
protected void showNotify()
```

구현 시 Canvas 가 
디스플레이에 표시되기 전에 바로 showNotify() 를 호출합니다. 
Canvas 서브 클래스는 애니메이션 설정, 
타이머 시작 등이 표시되기 전에 
작업을 수행하기 위해 이 메소드를 무시할 수 있습니다. Canvas 클래스에 있는 이 메소드의 
기본 구현은 비어 있습니다.

### hideNotify

```java
protected void hideNotify()
```

구현 시 Canvas 가 
디스플레이에서 제거된 다음 
바로 hideNotify() 를 호출합니다. Canvas 서브 클래스는 애니메이션 일시 중지, 
타이머 해지 등의 작업을 수행하기 위해 
이 메소드를 무시할 수 있습니다. Canvas 클래스에서 
이 메소드의 기본 구현은 비어 있습니다.

### paint

```java
protected abstract void paint(Graphics g)
```

**Parameters:**
- `g` - `Canvas` 렌더링에 사용된 `Graphics` 
객체

### sizeChanged

```java
protected void sizeChanged(int w,
                           int h)
```

**Overrides:**
- `sizeChanged` in class `Displayable`

**Parameters:**
- `h` - `Canvas` 그리기 가능 
영역의 새 높이(픽셀 단위)

**Since:**
- MIDP 2.0

## 메서드 상세

### getWidth

```java
public int getWidth()
```

**Overrides:**
- `getWidth` in class `Displayable`

**Returns:**
- 디스플레이 가능 영역의 너비

### getHeight

```java
public int getHeight()
```

**Overrides:**
- `getHeight` in class `Displayable`

**Returns:**
- 디스플레이 가능 영역의 높이

### isDoubleBuffered

```java
public boolean isDoubleBuffered()
```

**Returns:**
- 이중 버퍼된 경우 `true`, 
그렇지 않으면 `false`입니다.

### hasPointerEvents

```java
public boolean hasPointerEvents()
```

**Returns:**
- 장치에서 포인터 이벤트를 지원하는 경우 `true`입니다.

### hasPointerMotionEvents

```java
public boolean hasPointerMotionEvents()
```

**Returns:**
- 장치에서 포인터 모션 이벤트를 지원하는 경우 `true`입니다.

### hasRepeatEvents

```java
public boolean hasRepeatEvents()
```

**Returns:**
- 장치에서 반복 이벤트를 지원하는 경우 `true`입니다.

### getKeyCode

```java
public int getKeyCode(int gameAction)
```

**Parameters:**
- `gameAction` - 게임 작업

**Returns:**
- 이 게임 작업에 해당하는 키 코드

**Throws:**
- `IllegalArgumentException` - `gameAction`이 
유효한 게임 작업이 아닌 경우

### getKeyName

```java
public String getKeyName(int keyCode)
```

**Parameters:**
- `keyCode` - 요청된 키 코드

**Returns:**
- 키의 문자열 이름

**Throws:**
- `IllegalArgumentException` - `keyCode`가 
유효한 키 코드가 아닌 경우

### getGameAction

```java
public int getGameAction(int keyCode)
```

**Parameters:**
- `keyCode` - 키 코드

**Returns:**
- 이 키에 해당하는 게임 작업, 또는 해당 게임 작업이 없는 경우 
`0`

**Throws:**
- `IllegalArgumentException` - `keyCode`가 
유효한 키 코드가 아닌 경우

### setFullScreenMode

```java
public void setFullScreenMode(boolean mode)
```

**Parameters:**
- `mode` - `Canvas`가 전체 화면 모드에 있으면 
`true`, 그렇지 않은 경우 `false`

**Since:**
- MIDP 2.0

### keyPressed

```java
protected void keyPressed(int keyCode)
```

**Parameters:**
- `keyCode` - 누른 키에 대한 키 코드

### keyRepeated

```java
protected void keyRepeated(int keyCode)
```

**Parameters:**
- `keyCode` - 반복된 키에 대한 키 코드

**See Also:**
- ``hasRepeatEvents()``

### keyReleased

```java
protected void keyReleased(int keyCode)
```

**Parameters:**
- `keyCode` - 해제된 키에 대한 키 코드

### pointerPressed

```java
protected void pointerPressed(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터를 누른 수직 
위치(`Canvas`에 상대적)

### pointerReleased

```java
protected void pointerReleased(int x,
                               int y)
```

**Parameters:**
- `y` - 포인터를 놓은 수직 
위치(`Canvas`에 상대적)

### pointerDragged

```java
protected void pointerDragged(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터를 끈 수직 
위치(`Canvas`에 상대적)

### repaint

```java
public final void repaint(int x,
                          int y,
                          int width,
                          int height)
```

**Parameters:**
- `height` - 다시 그릴 직사각형의 높이

**See Also:**
- ``Display.callSerially(Runnable)``, 
``serviceRepaints()``

### repaint

```java
public final void repaint()
```

전체 Canvas 에 대해 다시 그리기를 요청합니다. 
결과는 다음과 같습니다. repaint(0, 0, getWidth(), getHeight());

### serviceRepaints

```java
public final void serviceRepaints()
```

**See Also:**
- ``Display.callSerially(Runnable)``

### showNotify

```java
protected void showNotify()
```

구현 시 Canvas 가 
디스플레이에 표시되기 전에 바로 showNotify() 를 호출합니다. 
Canvas 서브 클래스는 애니메이션 설정, 
타이머 시작 등이 표시되기 전에 
작업을 수행하기 위해 이 메소드를 무시할 수 있습니다. Canvas 클래스에 있는 이 메소드의 
기본 구현은 비어 있습니다.

### hideNotify

```java
protected void hideNotify()
```

구현 시 Canvas 가 
디스플레이에서 제거된 다음 
바로 hideNotify() 를 호출합니다. Canvas 서브 클래스는 애니메이션 일시 중지, 
타이머 해지 등의 작업을 수행하기 위해 
이 메소드를 무시할 수 있습니다. Canvas 클래스에서 
이 메소드의 기본 구현은 비어 있습니다.

### paint

```java
protected abstract void paint(Graphics g)
```

**Parameters:**
- `g` - `Canvas` 렌더링에 사용된 `Graphics` 
객체

### sizeChanged

```java
protected void sizeChanged(int w,
                           int h)
```

**Overrides:**
- `sizeChanged` in class `Displayable`

**Parameters:**
- `h` - `Canvas` 그리기 가능 
영역의 새 높이(픽셀 단위)

**Since:**
- MIDP 2.0
