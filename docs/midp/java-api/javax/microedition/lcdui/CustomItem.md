# Class CustomItem

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Item
        |
        +--javax.microedition.lcdui.CustomItem
```

## 설명

**extends Item:**

CustomItem은 새로운 시각적 요소 및 대화식 요소를 
`Forms`에 도입하기 위해 클래스 세분화를 통해 
사용자 정의할 수 있습니다. 서브 클래스는 크기 조정과 렌더링 및 색, 글꼴, 
그래픽 선택을 비롯한 시각적 모양을 담당합니다. 
서브 클래스는 키, 포인터 작업 및 순회 작업으로 생성된 이벤트에 응답하여 
사용자 상호 작용 모드를 담당합니다. 
마지막으로 서브 클래스는 `CustomItem` 값이 변경된 
수신기의 알림을 트리거하기 위해 ``Item.notifyStateChanged()`` 호출을 
담당합니다.

다른 `Item`과 
마찬가지로 `CustomItem`에는 
*최소* 및 *기본* 크기의 개념이 있습니다. 
이는 내용, 레이블, 경계 등의 
공간을 포함하는 `Item`의 
전체 영역과 관련됩니다. `Item`의 영역 및 크기에 대한 
자세한 내용은 `항목 크기`를 참조하십시오.

또한 `CustomItem` 서브 클래스에는 
`CustomItem`의 컨텐트 영역 크기인 *내용* 
크기의 개념이 있습니다. 컨텐트 영역은 
`CustomItem`이 
차지하는 전체 영역 내의 직사각형 영역입니다. 
컨텐트 영역은 `CustomItem` 서브 클래스가 
입력 이벤트를 그리고 수신하는 영역입니다. 
여기에는 레이블과 경계에 사용되는 공간은 포함되어 있지 않습니다. 
구현 시 컨텐트 영역을 벗어난 `Item`의 영역 내에서 
입력 이벤트를 레이아웃하고 그리며 처리합니다.

구현과 `CustomItem` 
서브 클래스 간에 
전달된 모든 좌표는 
`(0,0)`에 있는 이 영역의 
왼쪽 위 모서리와 함께 항목의 
컨텐트 영역에 상대적입니다. 

``getMinContentHeight``, 
``getMinContentWidth``, 
``getPrefContentHeight``, 
``getPrefContentWidth`` 및 
``sizeChanged`` 

메소드를 사용하여 구현과 
`CustomItem` 서브 클래스 
사이에 전달된 크기 정보는 모두 컨텐트 영역의 크기를 참조합니다. 
구현 시 항목 크기 메소드 

``Item.getMinimumHeight``, 
``Item.getMinimumWidth``, 
``Item.getPreferredHeight`` 및 
``Item.getPreferredWidth``에서 보고하는 대로 `Item`의 전체 영역 크기와 컨텐트 영역 크기 간의 차이를 계산하고 유지합니다.

구현 시 `CustomItem`에서 반환하는 
크기 정보가 사용자 인터페이스 정책에 의해 부과된 제한을 
초과하는 경우 무시합니다. 이 경우 구현 시에는 
``sizeChanged``와 
``paint`` 메소드를 통해 `CustomItem`에 부여된 
실제 크기를 항상 보고해야 합니다. 
예를 들어, 구현 시 `Item`이 화면보다 더 커지지 않도록 하는 
경우에 이러한 상황이 발생할 수 있습니다. 
`CustomItem` 서브 클래스 코드가 
`CustomItem`을 
화면보다 크게 만드는 `getMinContentWidth`에서 값을 
반환하는 경우 구현 시 `getMinContentWidth`에서 
반환된 최소 너비보다 더 좁은 너비를 할당할 수 있습니다.

구현 시 다른 `CustomItem` 메소드와 
관련된 순서로 `CustomItem`의 내용 크기 메소드 

``getMinContentHeight``, 
``getMinContentWidth``, 
``getPrefContentHeight`` 및 
``getPrefContentWidth``를 

호출할 수 있습니다. 
이러한 모든 메소드에 대해 `CustomItem` 
서브 클래스 코드는 현재 `CustomItem`의 내용과 
일치하는 값을 반환해야 합니다. 
내용이 변경되면 `CustomItem` 서브 클래스 코드가 
단순히 내용 크기 메소드에서 다양한 값을 반환하기 시작하기에 
충분하지 않습니다. 
대신 내용이 변경될 때마다 서브 클래스 코드는 
``invalidate`` 메소드를 호출해야 합니다. 
이는 구현에 레이아웃 계산을 수행해야 할 수 있음을 알려 구현 시 `CustomItem`의 새 내용을 기반으로 새 값을 얻기 위한 내용 크기 메소드를 호출합니다.

`CustomItem` 클래스는 많은 항목에서 
적당한 편집을 허용하지만 가능한 상호 작용을 모두 허용하지는 않습니다. 
융통성에 대한 요구는 쉽게 마스터할 수 있는 
단순한 API를 만드는 것에 대한 
요구 사항과 상호 운용성을 저해하지 않으면서도 
플랫폼별로 모양 및 
색감의 변화를 허용할 필요성과 함께 균형을 이루고 있습니다.

일반적인 개념은 여러 상호 작용 "모드"가 있어 
`Form` 구현 시 지원하는 내용을 전달할 수 있도록 
하는 것입니다. 그런 다음 `CustomItem`에서 
하나 이상의 상호 작용 모드를 지원하도록 선택할 수 있습니다. 
`CustomItem`에서 
모든 상호 작용 모드를 조합하여 구현할 때 
필요한 요구 사항은 없습니다. 
일반적으로 `CustomItem`은 
특정 상호 작용 모드에 의존하는 고도의 대화식 접근 이외에도 
모든 플랫폼에서 작동하는 접근 방법(예: 아래에 설명된 별도의 
화면 편집 기술)을 구현합니다. 런타임 시 `CustomItem` 
코드는 이 상호 작용 모드를 지원할 것인지 여부를 결정하기 위해 
시스템에 쿼리할 수 있습니다. 
지원하는 경우 `CustomItem`은 이 
상호 작용 모드를 사용할 수 있으며 지원하지 않는 경우 
모든 플랫폼에서 작동하는 방법으로 폴백합니다.

`CustomItem`은 항상 항목 명령을 사용하여 
별도의 편집 화면을 호출할 수 있으며, 구분되는 상태 수가 적은 
구성 요소는 상태를 변경한 다음 
`notifyStateChanged` 알림을 
발생시켜 간단히 응답할 수 있습니다. 
별도의 편집 화면을 사용하기 위한 기술로는 
다른 `Displayable` 객체(예: List)에 값을 로드한 
다음 여기에서 ``Display.setCurrent(Displayable)``를 호출하는 것이 
있습니다. 사용자가 이 값의 편집이 
완료되었음을 알리기 위해 
명령(예: "OK")을 실행하면 
수신기는 해당 `Displayable` 
객체에서 값을 검색한 다음 
이 항목을 반환하기 위해 
``Display.setCurrentItem(Item)``을 
호출합니다.

구현 시 키패드 이벤트를 
`CustomItem`에 
전달하는 기능을 선택적으로 지원할 수 있습니다. 
구현 시에는 `getInteractionModes`에서 반환하는 값의 
`KEY_PRESS`, 
`KEY_RELEASE` 및 
`KEY_REPEAT` 비트를 설정하여 지원 수준을 나타냅니다. 
이러한 비트에 해당하는 이벤트는 
`keyPressed()`, 
`keyReleased()` 및 
`keyRepeated()` 메소드 
각각에 대한 호출을 통해 전달됩니다. 
구현 시 `KEY_RELEASE` 이벤트를 지원하면 
`KEY_PRESS` 이벤트도 지원해야 합니다. 
구현 시 `KEY_REPEAT` 이벤트를 지원하면 
`KEY_PRESS` 및 
`KEY_RELEASE` 
이벤트도 지원해야 합니다. 
지원되는 경우 `KEY_RELEASE` 이벤트는 
보통 해당 `KEY_PRESS` 이벤트가 수신된 다음에 발생하며 
`KEY_REPEAT` 이벤트는 보통 
`KEY_PRESS`와 `KEY_RELEASE` 
이벤트 사이에서 발생합니다. 하지만 `CustomItem`이 
표시될 때 키를 누르면 해당 `KEY_PRESS`가 없어도 
`CustomItem`은 `KEY_RELEASE`나 
`KEY_REPEAT` 이벤트를 수신할 수 있습니다.

이벤트가 발생한 키를 나타내기 위해 키 이벤트 메소드가 
`keyCode`에 전달됩니다. 
구현 시 키 코드 `Canvas.KEY_NUM0` 에서 
`Canvas.KEY_NUM9`, `Canvas.KEY_STAR` 
및 `Canvas.KEY_POUND`를 사용하여 사용자가 
이벤트를 생성할 수 있는 방법을 제공해야 합니다. 
또한 구현 시 장치별 키를 포함하여 
다른 키에 대한 키 이벤트도 
전달할 수 있습니다. `CustomItem`에 사용할 수 있는 
키 집합은 명령이 추가되었는지 
여부에 따라 달라질 수 있습니다.

응용 프로그램은 `getGameAction` 메소드를 
사용하여 키 코드를 게임 작업에 매핑할 수 있습니다. 
구현 시 `CustomItem`에서 
키 이벤트를 지원하는 경우 
모든 게임 작업을 `CustomItem`에서 사용할 수 있도록 
충분한 키 코드 집합과 게임 작업에 대한 매핑을 
제공해야 합니다.

`CustomItem`에서 사용할 수 있는 
키 집합과 키 이벤트는 `Canvas`에서 
사용할 수 있는 것에 따라 
달라질 수 있습니다. 
특히, 순회를 지원하는 시스템에서 시스템은 
순회용 방향 키를 사용하고 
이러한 키를 `CustomItem`에 
전달하지 않도록 선택할 수 있습니다. 
`CustomItem`의 키 코드와 게임 작업 사이의 
매핑은 `Canvas`의 매핑과 다를 수 있습니다. 
키 코드와 게임 작업에 대한 자세한 내용은 `Canvas` 
클래스에서 `키 이벤트` 및 
`게임 작업`을 
참조하십시오.

구현 시 선택적으로 `CustomItem`에 포인터 
이벤트(예: 스타일러스 탭) 전달을 지원할 수 있습니다. 
구현 시 `getInteractionModes`가 반환하는 값에서 
`POINTER_PRESS`, 
`POINTER_RELEASE` 
및 `POINTER_DRAG` 비트를 설정하여 지원 수준을 나타냅니다. 
이러한 비트에 해당하는 이벤트는 
`pointerPressed()`, 
`pointerReleased()`, 
`pointerDragged()` 메소드 
각각에 대한 호출을 통해 전달됩니다. 
구현 시 `POINTER_RELEASE` 이벤트를 지원하면 
`POINTER_PRESS` 이벤트도 지원해야 합니다. 
구현 시 `POINTER_DRAG` 이벤트를 지원하면 
`POINTER_PRESS` 및 
`POINTER_RELEASE` 이벤트도 지원해야 합니다.
지원되는 경우 `POINTER_RELEASE` 이벤트는 
보통 해당 `POINTER_PRESS` 이벤트를 수신한 다음 
발생하며 `POINTER_DRAG` 이벤트는 
보통 `POINTER_PRESS`와 `POINTER_RELEASE` 이벤트 
사이에서 발생합니다. 
하지만 `CustomItem`이 표시될 때 포인터를 누르면 해당 
`POINTER_PRESS`가 없어도 
`CustomItem`은 `POINTER_RELEASE`나 
`POINTER_DRAG` 
이벤트를 수신할 수 있습니다.

포인터 이벤트의 `(x,y)` 위치는 
각 포인터 이벤트에 의해 보고됩니다. 
이 위치는 `CustomItem`의 좌표 시스템으로 표현되며 
여기서 `(0,0)`은 `CustomItem`의 
왼쪽 위 모서리입니다. 특정 상황에서 포인터 이벤트는 
해당 항목의 범위를 벗어나서 
발생할 수 있습니다.

구현 시 `CustomItem`에 대한 
*내부* 순회를 지원합니다. 
즉, 구현 시 일시적으로 해당 항목에 순회를 위임합니다. 
`CustomItem` 
내부에 순회 위치가 하나만 있더라도 
사용자가 항목을 순회할 때 특수화된 강조 표시, 애니메이션 등을 
수행할 수 있도록 항목에 내부 순회 프로토콜을 
지원하려 할 수 있습니다.

구현 시 `getInteractionModes()`가 
반환하는 값에서 `TRAVERSE_HORIZONTAL` 
또는 `TRAVERSE_VERTICAL` 비트 중 하나나 
두 가지 모두를 설정하여 `CustomItem`에 대한 
내부 순회 지원을 표시합니다. 이러한 비트 중 
어느 하나도 설정되어 있지 않은 경우에는 구현 시 
`CustomItem`이 내부적으로 순회하는 것을 
허용하지 않거나 구현 시 순회를 전혀 지원하지 않습니다. 
구현 시 순회를 지원하지만 
`CustomItem`에 대한 
내부 순회를 거부하는 경우 
`CustomItem`의 컨텐트 영역을 
벗어나는 고유 강조 표시 기능을 제공합니다.

`CustomItem`은 내부 순회를 전혀 지원하지 않아도 됩니다. 
`traverse` 메소드에 대한 초기 호출에 
`false`를 반환하여 이를 수행할 수 
있습니다(`CustomItem`에서 
이 메소드를 무시하지 않는 
경우의 기본 동작). 이 경우 
시스템은 사용자가 항목을 순회하여 통과할 수 있도록 조정해야 합니다. 
특히 내부 순회의 발생 여부에 상관없이 해당 항목이 화면 높이를 
초과하는 경우 시스템은 적절한 스크롤이 
발생할 수 있도록 조정해야 합니다.

구현 시 순회 이벤트를 `CustomItem`에 
전달하는 기능을 지원하지 않더라도 키패드나 포인터 이벤트를 
`CustomItem`에 전달하는 기능을 지원할 수 있습니다. 
구현 시 키패드나 포인터 이벤트를 
`CustomItem`에 전달하는 기능을 지원하는 경우 
이러한 `CustomItem`이 
초기 `traverse()` 
호출에 대해 `false`를 반환하여 내부 순회를 거부했더라도 
모든 `CustomItem`에 대해 전달할 수 있는 
방법을 제공해야 합니다. 이는 특정 항목이 내부 순회를 
지원하지 않더라도 구현 시 해당 항목에 대한 
초점 개념을 지원해야 한다는 것을 
의미합니다.

항목이 내부 순회를 수행하는 데 
필요한 동작 및 책임에 대한 전체 사양은 
``traverse`` 메소드 설명서를 
참조하십시오.

각 항목의 시각적 모양은 레이블(구현 시 처리) 
및 내용(서브 클래스에서 처리)으로 
구성됩니다.

레이블은 해당 항목이 아닌 구현 담당입니다. 
`CustomItem`의 내용에 대해 할당된 
화면 영역은 구현 시 
`CustomItem` 레이블을 
표시하기 위해 사용하는 영역과는 별도입니다. 
구현 시 컨텐트 영역에 대하여 레이블 및 레이아웃의 
렌더링을 제어합니다.

`CustomItem`은 
`paint` 
메소드가 호출될 때마다 내용 그리기를 담당합니다.

포그라운드, 백그라운드, 강조 표시된 포그라운드, 
강조 표시된 백그라운드, 경계선 및 강조 표시된 경계선 색은 
``Display.getColor(int)``에서 
검색해야 합니다. 
그러면 `CustomItem`이 장치에서 제공한 
다른 항목의 색 구성표와 일치합니다. `CustomItem`은 
고유의 강조 표시 상태와 
강조 표시되지 않은 상태를 추적합니다.

사용된 글꼴은 ``Font.getFont(int)``에서 검색해야 합니다. 
그러면 일관된 시각적 모양을 위해 장치의 다른 항목에서 
사용한 글꼴과 일치시킬 수 있습니다.

**Since:**
- MIDP 2.0

## 필드 요약

- `protected static int KEY_PRESS` — 키 누르기 이벤트 지원을 나타내는 상호 작용 모드 비트.
- `protected static int KEY_RELEASE` — 키 놓기 이벤트 지원을 나타내는 상호 작용 모드 비트.
- `protected static int KEY_REPEAT` — 키 반복 이벤트 지원을 나타내는 상호 작용 모드 비트.
- `protected static int NONE` — 순회가 이 항목 내에 들어갔거나 위치가 변경되었음을 알리고 이 순회 이벤트와 관련된 특정 방향이 없음을 알리는 순회 방향에 대한 값.
- `protected static int POINTER_DRAG` — 포인트 끌기 이벤트 지원을 나타내는 상호 작용 모드 비트.
- `protected static int POINTER_PRESS` — 포인트 누르기 이벤트 지원을 나타내는 상호 작용 모드 비트.
- `protected static int POINTER_RELEASE` — 포인트 놓기 이벤트 지원을 나타내는 상호 작용 모드 비트.
- `protected static int TRAVERSE_HORIZONTAL` — CustomItem 에 대한 수평 내부 순회 지원을 나타내는 상호 작용 모드 비트.
- `protected static int TRAVERSE_VERTICAL` — CustomItem 에 대한 수직 내부 순회 지원을 나타내는 상호 작용 모드 비트.

## 생성자 요약

- `protected CustomItem ( String label)` — CustomItem 서브 클래스가 해당 레이블을 지정할 수 있게 하는 수퍼 클래스 구성자

## 메서드 요약

- `int getGameAction (int keyCode)` — 장치의 지정된 키 코드와 관련된 게임 작업을 가져옵니다.
- `protected  int getInteractionModes ()` — 사용 가능한 상호 작용 모드를 가져옵니다.
- `protected abstract  int getMinContentHeight ()` — 컨텐트 영역의 최소 높이를 픽셀 단위로 반환하기 위해 서브 클래스에 의해 구현됩니다.
- `protected abstract  int getMinContentWidth ()` — 컨텐트 영역의 최소 너비를 픽셀 단위로 반환하기 위해 서브 클래스에 의해 구현됩니다.
- `protected abstract  int getPrefContentHeight (int width)` — 컨텐트 영역의 기본 높이를 반환하기 위해 서브 클래스에 의해 구현됩니다.
- `protected abstract  int getPrefContentWidth (int height)` — 컨텐트 영역의 기본 너비를 픽셀 단위로 반환하기 위해 서브 클래스에 의해 구현됩니다.
- `protected  void hideNotify ()` — 이전에는 부분이라도 표시되었지만 현재는 전혀 표시되지 않는 항목을 알리기 위해 시스템에서 호출합니다.
- `protected  void invalidate ()` — CustomItem 의 크기와 순회 위치를 업데이트해야 한다는 것을 알립니다.
- `protected  void keyPressed (int keyCode)` — 키를 누를 때 시스템에서 호출합니다.
- `protected  void keyReleased (int keyCode)` — 키를 놓을 때 시스템에서 호출합니다.
- `protected  void keyRepeated (int keyCode)` — 키가 반복되면 시스템에서 호출합니다.
- `protected abstract  void paint ( Graphics g, int w, int h)` — 컨테이너 내에서 항목을 렌더링하기 위해 서브 클래스에 의해 구현됩니다.
- `protected  void pointerDragged (int x, int y)` — 항목 내에서 포인터 끌기 작업(예: 누르고 놓기 전의 펜 모션)이 발생하면 시스템에서 호출합니다.
- `protected  void pointerPressed (int x, int y)` — 항목 내에서 포인터 내리기 작업(예: 펜 탭)이 발생하면 시스템에서 호출합니다.
- `protected  void pointerReleased (int x, int y)` — 항목 내에서 포인터 내리기 작업이 발생한 다음 포인터 올리기 작업(예: 펜 리프트)이 발생하면 시스템에서 호출합니다.
- `protected  void repaint ()` — 항목 다시 그리기를 요청하기 위해 서브 클래스 코드에 의해 호출됩니다.
- `protected  void repaint (int x, int y, int w, int h)` — 항목의 지정된 직사각형 영역을 다시 그리도록 요청하기 위해 서브 클래스 코드에 의해 호출됩니다.
- `protected  void showNotify ()` — 이전에는 완전히 표시되지 않았지만 현재 부분적으로 표시되는 항목을 알리기 위해 시스템에서 호출합니다.
- `protected  void sizeChanged (int w, int h)` — 크기 변경 이벤트를 처리하기 위해 서브 클래스에 의해 구현됩니다.
- `protected  boolean traverse (int dir, int viewportWidth, int viewportHeight, int[] visRect_inout)` — 순회가 항목 내에 들어갔거나 해당 항목 내에서 순회가 발생한 경우 시스템에 의해 호출됩니다.
- `protected  void traverseOut ()` — 순회가 항목을 벗어나 발생하면 시스템에서 호출합니다.

## 필드 상세

### TRAVERSE_HORIZONTAL

```java
protected static final int TRAVERSE_HORIZONTAL
```

**See Also:**
- ``getInteractionModes()``, 
``traverse(int, int, int, int[])``, 
`Constant Field Values`

### TRAVERSE_VERTICAL

```java
protected static final int TRAVERSE_VERTICAL
```

**See Also:**
- ``getInteractionModes()``, 
``traverse(int, int, int, int[])``, 
`Constant Field Values`

### KEY_PRESS

```java
protected static final int KEY_PRESS
```

**See Also:**
- ``getInteractionModes()``, 
``keyPressed(int)``, 
`Constant Field Values`

### KEY_RELEASE

```java
protected static final int KEY_RELEASE
```

**See Also:**
- ``getInteractionModes()``, 
``keyReleased(int)``, 
`Constant Field Values`

### KEY_REPEAT

```java
protected static final int KEY_REPEAT
```

**See Also:**
- ``getInteractionModes()``, 
``keyRepeated(int)``, 
`Constant Field Values`

### POINTER_PRESS

```java
protected static final int POINTER_PRESS
```

**See Also:**
- ``getInteractionModes()``, 
``pointerPressed(int, int)``, 
`Constant Field Values`

### POINTER_RELEASE

```java
protected static final int POINTER_RELEASE
```

**See Also:**
- ``getInteractionModes()``, 
``pointerReleased(int, int)``, 
`Constant Field Values`

### POINTER_DRAG

```java
protected static final int POINTER_DRAG
```

**See Also:**
- ``getInteractionModes()``, 
``pointerDragged(int, int)``, 
`Constant Field Values`

### NONE

```java
protected static final int NONE
```

**See Also:**
- ``traverse(int, int, int, int[])``, 
`Constant Field Values`

### CustomItem

```java
protected CustomItem(String label)
```

- `CustomItem` 서브 클래스가 
해당 레이블을 지정할 수 있게 하는 수퍼 클래스 구성자

**Parameters:**
- `label` - `CustomItem`의 레이블

### getInteractionModes

```java
protected final int getInteractionModes()
```

**Returns:**
- 사용 가능한 상호 작용 모드의 비트 마스크

### getMinContentWidth

```java
protected abstract int getMinContentWidth()
```

**Returns:**
- 최소 내용 너비(픽셀 단위)

### getMinContentHeight

```java
protected abstract int getMinContentHeight()
```

**Returns:**
- 최소 내용 높이(픽셀 단위)

### getPrefContentWidth

```java
protected abstract int getPrefContentWidth(int height)
```

**Parameters:**
- `height` - 임시 컨텐트 높이(픽셀 단위), 
또는 임시 높이가 계산되지 않은 경우 -1

**Returns:**
- 기본 컨텐트 너비(픽셀 단위)

### getPrefContentHeight

```java
protected abstract int getPrefContentHeight(int width)
```

**Parameters:**
- `width` - 임시 컨텐트 너비(픽셀 단위), 
또는 임시 너비가 계산되지 않은 경우 -1

**Returns:**
- 기본 컨텐트 높이(픽셀 단위)

### sizeChanged

```java
protected void sizeChanged(int w,
                           int h)
```

**Parameters:**
- `h` - 항목 컨텐트 영역의 새 높이

### invalidate

```java
protected final void invalidate()
```

CustomItem 의 크기와 순회 위치를 
업데이트해야 한다는 것을 알립니다. 
이 메소드는 구현 시 CustomItem 컨텐트 영역의 
크기나 내부 순회 위치를 변경해야 할 수 있다는 것을 알리기 위해 CustomItem 서브 클래스 코드에 의해 호출됩니다. 
이는 CustomItem 의 
내용이 수정될 때 자주 발생합니다. 이 메소드에 대한 호출은 즉시 결과를 반환하며 
컨테이너 레이아웃 알고리즘이 향후의 특정 시점에 실행되도록 하므로 getMinContentHeight , getMinContentWidth , getPrefContentHeight , getPrefContentWidth , sizeChanged 나 traverse 에 대한 호출이 발생할 수 있습니다. 

레이아웃 작업의 결과로 다시 그리기가 필요한 경우 paint 메소드도 호출될 수 있습니다. CustomItem 이 표시되지 않은 상태에서 
컨텐트 크기가 무효화된 경우 해당 레이아웃 작업이 지연될 수 있습니다. invalidate 가 호출될 때 CustomItem 에 현재 순회 위치가 포함되어 있는 경우 traverse 메소드가 호출됩니다.

### paint

```java
protected abstract void paint(Graphics g,
                              int w,
                              int h)
```

**Parameters:**
- `h` - 항목의 현재 높이(픽셀 단위)

### repaint

```java
protected final void repaint()
```

항목 다시 그리기를 요청하기 위해 서브 클래스 코드에 의해 호출됩니다. 
이 항목을 디스플레이에서 표시할 수 있는 경우 다음에 CustomItem 이 표시될 때 paint() 에 대한 
호출이 발생합니다. 항목의 내부 상태가 업데이트되어 해당 시각적 표현을 
업데이트해야 하는 경우 CustomItem 서브 클래스에서 
이 메소드를 호출해야 합니다.

### repaint

```java
protected final void repaint(int x,
                             int y,
                             int w,
                             int h)
```

**Parameters:**
- `h` - 업데이트할 직사각형 영역의 높이

### traverse

```java
protected boolean traverse(int dir,
                           int viewportWidth,
                           int viewportHeight,
                           int[] visRect_inout)
```

**Parameters:**
- `visRect_inout` - 표시 가능한 직사각형을 메소드에 
전달한 다음 메소드로부터 업데이트된 순회 직사각형을 반환합니다.

**Returns:**
- 내부 순회가 발생한 경우 `true`, 
순회가 범위를 벗어나는 경우 `false`

**See Also:**
- ``getInteractionModes()``, 
``traverseOut()``, 
``TRAVERSE_HORIZONTAL``, 
``TRAVERSE_VERTICAL``

### traverseOut

```java
protected void traverseOut()
```

**See Also:**
- ``getInteractionModes()``, 
``traverse(int, int, int, int[])``, 
``TRAVERSE_HORIZONTAL``, 
``TRAVERSE_VERTICAL``

### keyPressed

```java
protected void keyPressed(int keyCode)
```

**Parameters:**
- `keyCode` - 누른 키의 키 코드

**See Also:**
- ``getInteractionModes()``

### keyReleased

```java
protected void keyReleased(int keyCode)
```

**Parameters:**
- `keyCode` - 놓은 키의 키 코드

**See Also:**
- ``getInteractionModes()``

### keyRepeated

```java
protected void keyRepeated(int keyCode)
```

**Parameters:**
- `keyCode` - 반복된 키의 키 코드

**See Also:**
- ``getInteractionModes()``

### getGameAction

```java
public int getGameAction(int keyCode)
```

**Parameters:**
- `keyCode` - 키 코드

**Returns:**
- 이 키에 해당하는 게임 작업, 
또는 이러한 게임 작업이 없는 경우 `0`

**Throws:**
- `IllegalArgumentException` - `keyCode`가 
유효한 키 코드가 아닌 경우

### pointerPressed

```java
protected void pointerPressed(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터 내리기의 `y` 좌표

**See Also:**
- ``getInteractionModes()``

### pointerReleased

```java
protected void pointerReleased(int x,
                               int y)
```

**Parameters:**
- `y` - 포인터 내리기의 x 좌표

**See Also:**
- ``getInteractionModes()``

### pointerDragged

```java
protected void pointerDragged(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터 끌기의 `y` 좌표

**See Also:**
- ``getInteractionModes()``

### showNotify

```java
protected void showNotify()
```

이전에는 완전히 표시되지 않았지만 현재 부분적으로 
표시되는 항목을 알리기 위해 시스템에서 호출합니다. showNotify() 가 호출된 다음 항목은 paint() 호출을 받습니다. 이 메소드의 기본 구현은 어떤 작업도 하지 않습니다.

### hideNotify

```java
protected void hideNotify()
```

이전에는 부분이라도 표시되었지만 
현재는 전혀 표시되지 않는 항목을 알리기 위해 시스템에서 호출합니다. showNotify() 가 다시 호출될 때까지는 
이 항목에 대한 paint() 를 호출하지 않습니다. 이 메소드의 기본 구현은 어떤 작업도 하지 않습니다.

## 생성자 상세

### CustomItem

```java
protected CustomItem(String label)
```

- `CustomItem` 서브 클래스가 
해당 레이블을 지정할 수 있게 하는 수퍼 클래스 구성자

**Parameters:**
- `label` - `CustomItem`의 레이블

### getInteractionModes

```java
protected final int getInteractionModes()
```

**Returns:**
- 사용 가능한 상호 작용 모드의 비트 마스크

### getMinContentWidth

```java
protected abstract int getMinContentWidth()
```

**Returns:**
- 최소 내용 너비(픽셀 단위)

### getMinContentHeight

```java
protected abstract int getMinContentHeight()
```

**Returns:**
- 최소 내용 높이(픽셀 단위)

### getPrefContentWidth

```java
protected abstract int getPrefContentWidth(int height)
```

**Parameters:**
- `height` - 임시 컨텐트 높이(픽셀 단위), 
또는 임시 높이가 계산되지 않은 경우 -1

**Returns:**
- 기본 컨텐트 너비(픽셀 단위)

### getPrefContentHeight

```java
protected abstract int getPrefContentHeight(int width)
```

**Parameters:**
- `width` - 임시 컨텐트 너비(픽셀 단위), 
또는 임시 너비가 계산되지 않은 경우 -1

**Returns:**
- 기본 컨텐트 높이(픽셀 단위)

### sizeChanged

```java
protected void sizeChanged(int w,
                           int h)
```

**Parameters:**
- `h` - 항목 컨텐트 영역의 새 높이

### invalidate

```java
protected final void invalidate()
```

CustomItem 의 크기와 순회 위치를 
업데이트해야 한다는 것을 알립니다. 
이 메소드는 구현 시 CustomItem 컨텐트 영역의 
크기나 내부 순회 위치를 변경해야 할 수 있다는 것을 알리기 위해 CustomItem 서브 클래스 코드에 의해 호출됩니다. 
이는 CustomItem 의 
내용이 수정될 때 자주 발생합니다. 이 메소드에 대한 호출은 즉시 결과를 반환하며 
컨테이너 레이아웃 알고리즘이 향후의 특정 시점에 실행되도록 하므로 getMinContentHeight , getMinContentWidth , getPrefContentHeight , getPrefContentWidth , sizeChanged 나 traverse 에 대한 호출이 발생할 수 있습니다. 

레이아웃 작업의 결과로 다시 그리기가 필요한 경우 paint 메소드도 호출될 수 있습니다. CustomItem 이 표시되지 않은 상태에서 
컨텐트 크기가 무효화된 경우 해당 레이아웃 작업이 지연될 수 있습니다. invalidate 가 호출될 때 CustomItem 에 현재 순회 위치가 포함되어 있는 경우 traverse 메소드가 호출됩니다.

### paint

```java
protected abstract void paint(Graphics g,
                              int w,
                              int h)
```

**Parameters:**
- `h` - 항목의 현재 높이(픽셀 단위)

### repaint

```java
protected final void repaint()
```

항목 다시 그리기를 요청하기 위해 서브 클래스 코드에 의해 호출됩니다. 
이 항목을 디스플레이에서 표시할 수 있는 경우 다음에 CustomItem 이 표시될 때 paint() 에 대한 
호출이 발생합니다. 항목의 내부 상태가 업데이트되어 해당 시각적 표현을 
업데이트해야 하는 경우 CustomItem 서브 클래스에서 
이 메소드를 호출해야 합니다.

### repaint

```java
protected final void repaint(int x,
                             int y,
                             int w,
                             int h)
```

**Parameters:**
- `h` - 업데이트할 직사각형 영역의 높이

### traverse

```java
protected boolean traverse(int dir,
                           int viewportWidth,
                           int viewportHeight,
                           int[] visRect_inout)
```

**Parameters:**
- `visRect_inout` - 표시 가능한 직사각형을 메소드에 
전달한 다음 메소드로부터 업데이트된 순회 직사각형을 반환합니다.

**Returns:**
- 내부 순회가 발생한 경우 `true`, 
순회가 범위를 벗어나는 경우 `false`

**See Also:**
- ``getInteractionModes()``, 
``traverseOut()``, 
``TRAVERSE_HORIZONTAL``, 
``TRAVERSE_VERTICAL``

### traverseOut

```java
protected void traverseOut()
```

**See Also:**
- ``getInteractionModes()``, 
``traverse(int, int, int, int[])``, 
``TRAVERSE_HORIZONTAL``, 
``TRAVERSE_VERTICAL``

### keyPressed

```java
protected void keyPressed(int keyCode)
```

**Parameters:**
- `keyCode` - 누른 키의 키 코드

**See Also:**
- ``getInteractionModes()``

### keyReleased

```java
protected void keyReleased(int keyCode)
```

**Parameters:**
- `keyCode` - 놓은 키의 키 코드

**See Also:**
- ``getInteractionModes()``

### keyRepeated

```java
protected void keyRepeated(int keyCode)
```

**Parameters:**
- `keyCode` - 반복된 키의 키 코드

**See Also:**
- ``getInteractionModes()``

### getGameAction

```java
public int getGameAction(int keyCode)
```

**Parameters:**
- `keyCode` - 키 코드

**Returns:**
- 이 키에 해당하는 게임 작업, 
또는 이러한 게임 작업이 없는 경우 `0`

**Throws:**
- `IllegalArgumentException` - `keyCode`가 
유효한 키 코드가 아닌 경우

### pointerPressed

```java
protected void pointerPressed(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터 내리기의 `y` 좌표

**See Also:**
- ``getInteractionModes()``

### pointerReleased

```java
protected void pointerReleased(int x,
                               int y)
```

**Parameters:**
- `y` - 포인터 내리기의 x 좌표

**See Also:**
- ``getInteractionModes()``

### pointerDragged

```java
protected void pointerDragged(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터 끌기의 `y` 좌표

**See Also:**
- ``getInteractionModes()``

### showNotify

```java
protected void showNotify()
```

이전에는 완전히 표시되지 않았지만 현재 부분적으로 
표시되는 항목을 알리기 위해 시스템에서 호출합니다. showNotify() 가 호출된 다음 항목은 paint() 호출을 받습니다. 이 메소드의 기본 구현은 어떤 작업도 하지 않습니다.

### hideNotify

```java
protected void hideNotify()
```

이전에는 부분이라도 표시되었지만 
현재는 전혀 표시되지 않는 항목을 알리기 위해 시스템에서 호출합니다. showNotify() 가 다시 호출될 때까지는 
이 항목에 대한 paint() 를 호출하지 않습니다. 이 메소드의 기본 구현은 어떤 작업도 하지 않습니다.

## 메서드 상세

### getInteractionModes

```java
protected final int getInteractionModes()
```

**Returns:**
- 사용 가능한 상호 작용 모드의 비트 마스크

### getMinContentWidth

```java
protected abstract int getMinContentWidth()
```

**Returns:**
- 최소 내용 너비(픽셀 단위)

### getMinContentHeight

```java
protected abstract int getMinContentHeight()
```

**Returns:**
- 최소 내용 높이(픽셀 단위)

### getPrefContentWidth

```java
protected abstract int getPrefContentWidth(int height)
```

**Parameters:**
- `height` - 임시 컨텐트 높이(픽셀 단위), 
또는 임시 높이가 계산되지 않은 경우 -1

**Returns:**
- 기본 컨텐트 너비(픽셀 단위)

### getPrefContentHeight

```java
protected abstract int getPrefContentHeight(int width)
```

**Parameters:**
- `width` - 임시 컨텐트 너비(픽셀 단위), 
또는 임시 너비가 계산되지 않은 경우 -1

**Returns:**
- 기본 컨텐트 높이(픽셀 단위)

### sizeChanged

```java
protected void sizeChanged(int w,
                           int h)
```

**Parameters:**
- `h` - 항목 컨텐트 영역의 새 높이

### invalidate

```java
protected final void invalidate()
```

CustomItem 의 크기와 순회 위치를 
업데이트해야 한다는 것을 알립니다. 
이 메소드는 구현 시 CustomItem 컨텐트 영역의 
크기나 내부 순회 위치를 변경해야 할 수 있다는 것을 알리기 위해 CustomItem 서브 클래스 코드에 의해 호출됩니다. 
이는 CustomItem 의 
내용이 수정될 때 자주 발생합니다. 이 메소드에 대한 호출은 즉시 결과를 반환하며 
컨테이너 레이아웃 알고리즘이 향후의 특정 시점에 실행되도록 하므로 getMinContentHeight , getMinContentWidth , getPrefContentHeight , getPrefContentWidth , sizeChanged 나 traverse 에 대한 호출이 발생할 수 있습니다. 

레이아웃 작업의 결과로 다시 그리기가 필요한 경우 paint 메소드도 호출될 수 있습니다. CustomItem 이 표시되지 않은 상태에서 
컨텐트 크기가 무효화된 경우 해당 레이아웃 작업이 지연될 수 있습니다. invalidate 가 호출될 때 CustomItem 에 현재 순회 위치가 포함되어 있는 경우 traverse 메소드가 호출됩니다.

### paint

```java
protected abstract void paint(Graphics g,
                              int w,
                              int h)
```

**Parameters:**
- `h` - 항목의 현재 높이(픽셀 단위)

### repaint

```java
protected final void repaint()
```

항목 다시 그리기를 요청하기 위해 서브 클래스 코드에 의해 호출됩니다. 
이 항목을 디스플레이에서 표시할 수 있는 경우 다음에 CustomItem 이 표시될 때 paint() 에 대한 
호출이 발생합니다. 항목의 내부 상태가 업데이트되어 해당 시각적 표현을 
업데이트해야 하는 경우 CustomItem 서브 클래스에서 
이 메소드를 호출해야 합니다.

### repaint

```java
protected final void repaint(int x,
                             int y,
                             int w,
                             int h)
```

**Parameters:**
- `h` - 업데이트할 직사각형 영역의 높이

### traverse

```java
protected boolean traverse(int dir,
                           int viewportWidth,
                           int viewportHeight,
                           int[] visRect_inout)
```

**Parameters:**
- `visRect_inout` - 표시 가능한 직사각형을 메소드에 
전달한 다음 메소드로부터 업데이트된 순회 직사각형을 반환합니다.

**Returns:**
- 내부 순회가 발생한 경우 `true`, 
순회가 범위를 벗어나는 경우 `false`

**See Also:**
- ``getInteractionModes()``, 
``traverseOut()``, 
``TRAVERSE_HORIZONTAL``, 
``TRAVERSE_VERTICAL``

### traverseOut

```java
protected void traverseOut()
```

**See Also:**
- ``getInteractionModes()``, 
``traverse(int, int, int, int[])``, 
``TRAVERSE_HORIZONTAL``, 
``TRAVERSE_VERTICAL``

### keyPressed

```java
protected void keyPressed(int keyCode)
```

**Parameters:**
- `keyCode` - 누른 키의 키 코드

**See Also:**
- ``getInteractionModes()``

### keyReleased

```java
protected void keyReleased(int keyCode)
```

**Parameters:**
- `keyCode` - 놓은 키의 키 코드

**See Also:**
- ``getInteractionModes()``

### keyRepeated

```java
protected void keyRepeated(int keyCode)
```

**Parameters:**
- `keyCode` - 반복된 키의 키 코드

**See Also:**
- ``getInteractionModes()``

### getGameAction

```java
public int getGameAction(int keyCode)
```

**Parameters:**
- `keyCode` - 키 코드

**Returns:**
- 이 키에 해당하는 게임 작업, 
또는 이러한 게임 작업이 없는 경우 `0`

**Throws:**
- `IllegalArgumentException` - `keyCode`가 
유효한 키 코드가 아닌 경우

### pointerPressed

```java
protected void pointerPressed(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터 내리기의 `y` 좌표

**See Also:**
- ``getInteractionModes()``

### pointerReleased

```java
protected void pointerReleased(int x,
                               int y)
```

**Parameters:**
- `y` - 포인터 내리기의 x 좌표

**See Also:**
- ``getInteractionModes()``

### pointerDragged

```java
protected void pointerDragged(int x,
                              int y)
```

**Parameters:**
- `y` - 포인터 끌기의 `y` 좌표

**See Also:**
- ``getInteractionModes()``

### showNotify

```java
protected void showNotify()
```

이전에는 완전히 표시되지 않았지만 현재 부분적으로 
표시되는 항목을 알리기 위해 시스템에서 호출합니다. showNotify() 가 호출된 다음 항목은 paint() 호출을 받습니다. 이 메소드의 기본 구현은 어떤 작업도 하지 않습니다.

### hideNotify

```java
protected void hideNotify()
```

이전에는 부분이라도 표시되었지만 
현재는 전혀 표시되지 않는 항목을 알리기 위해 시스템에서 호출합니다. showNotify() 가 다시 호출될 때까지는 
이 항목에 대한 paint() 를 호출하지 않습니다. 이 메소드의 기본 구현은 어떤 작업도 하지 않습니다.
