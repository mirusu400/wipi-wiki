# Class Item

`package javax.microedition.lcdui`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.Item
```

## 설명

**Direct Known Subclasses:**
- `ChoiceGroup`, `CustomItem`, `DateField`, `Gauge`, `ImageItem`, `Spacer`, `StringItem`, `TextField`

**extends Object:**

``Form``에 추가할 수 있는 구성 요소의 수퍼 클래스. 
모든 `Item` 객체에는 
항목에 연결된 문자열인 레이블 필드가 있습니다. 레이블은 일반적으로 
화면에 표시될 때 구성 요소 가까이에 
표시됩니다. 레이블은 항목과 같은 가로 행이나 항목의 
바로 위에 있어야 합니다. 
구현 시 레이블이 다른 문자열과 같은 행에 
놓인 경우 레이블을 다른 글꼴로 표시하거나, 
다른 여백에 맞추어 정렬하거나, 콜론을 추가하여 레이블 문자열을 
다른 텍스트 내용과 구별할 수 있도록 해야 합니다. 
화면이 스크롤될 때 `Item`과 동시에 레이블도 
계속 표시되도록 해야 합니다.

사용자가 `Item`과 상호 작용하려고 할 때 
시스템에서는 실제 상호 작용이 발생하는 시스템 생성 화면으로 
전환하는 경우도 있습니다. 
이러한 경우 일반적으로 레이블도 함께 
새 화면에 표시되어 사용자에게 작업 상황을 알려줍니다. 
그러므로 응용 프로그램은 모든 대화식 항목 객체에 레이블을 
제공하는 것이 좋습니다. 
그러나 이것은 필수 사항은 아니며 
레이블에 `null` 값을 사용하여 레이블이 없음을 
지정할 수도 있습니다.

### 항목 레이아웃

컨테이너 내의 `Item` 레이아웃은 
레이아웃 지시어에 의해 영향을 받습니다.

- `LAYOUT_DEFAULT`
- `LAYOUT_LEFT`
- `LAYOUT_RIGHT`
- `LAYOUT_CENTER`
- `LAYOUT_TOP`
- `LAYOUT_BOTTOM`
- `LAYOUT_VCENTER`
- `LAYOUT_NEWLINE_BEFORE`
- `LAYOUT_NEWLINE_AFTER`
- `LAYOUT_SHRINK`
- `LAYOUT_VSHRINK`
- `LAYOUT_EXPAND`
- `LAYOUT_VEXPAND`
- `LAYOUT_2`

`LAYOUT_DEFAULT` 지시어는 
이 항목에 사용할 컨테이너의 기본 레이아웃 정책을 나타냅니다. 
`LAYOUT_DEFAULT`의 값은 0이며 다른 레이아웃 지시어와 
결합되면 아무런 효과가 없습니다. 
이 지시어는 프로그램 내에서 프로그래머의 의도를 명시적으로 
나타내는 데 유용합니다.

`LAYOUT_LEFT`, `LAYOUT_RIGHT` 
및 `LAYOUT_CENTER` 지시어는 수평 정렬을 나타내며 
상호 배타적입니다. 이와 유사하게, 
`LAYOUT_TOP`, 
`LAYOUT_BOTTOM` 및 `LAYOUT_VCENTER` 
지시어는 수직 정렬을 나타내며 상호 배타적입니다.

수평 정렬 지시어, 수직 정렬 지시어 및 기타 레이아웃 지시어의 조합은 
비트 단위 `OR` 연산자(`|`)로 
조합하여 레이아웃 지시어 값을 구성할 수 있습니다. 
이러한 값은 ``setLayout(int)`` 메소드에 매개 변수로 
사용되고 ``getLayout()`` 메소드의 
반환 값입니다.

일부 지시어는 컨텍스트에 따라 정의된 동작이 없는 경우도 있습니다. 
`Item`이 있는 특정 컨텍스트 내에서 지시어의 
동작이 정의되지 않은 경우에는 해당 레이아웃 지시어가 무시됩니다.

`Form`에 있는 `Item` 레이아웃의 
전체 사양은 `여기`에서 
제공됩니다.

### 항목 크기

`Item`에는 2개의 명시적 크기 개념인 *최소* 크기와 
*권장* 크기가 있습니다. 
최소 및 권장 크기 모두 
`Item`의 총 영역을 가리키며 
여기에는 `Item` 
내용 공간, `Item` 레이블 
공간 및 레이아웃 정책에 중요한 다른 공간도 포함됩니다. 
이러한 크기는 레이아웃 용도에 중요하지 않은 
공간은 포함하지 않습니다. 
예를 들어, `Item`에 레이블을 
추가하면 여기에 필요한 공간을 만들기 위해 다른 `Item`을 
이동하게 되므로 이 레이블이 차지하는 
공간은 레이아웃에 중요하며 
`Item`의 최소 및 
권장 크기의 일부로 계산됩니다. 
그러나 구현 시 레이블용으로 
예약된 여백 영역에 레이블을 배치한 경우에는 
인접한 `Item`의 레이아웃에 영향을 미치지 않습니다. 
이런 경우 레이블이 차지하는 공간은 최소 및 권장 크기의 일부로 
간주되지 않습니다.

최소 크기는 최적의 크기는 아니지만 `Item`이 작동하고 
내용을 표시할 수 있는 가장 작은 크기입니다. 
최소 크기는 `Item`의 내용이 변경될 때마다 
재계산될 수 있습니다.

권장 크기는 일반적으로 `Item`의 내용을 
기준으로 하는 크기이며 정보가 잘리지 않고 텍스트 줄 바꿈(있는 경우)이 
허용 가능한 최소치로 유지되는 가장 작은 크기입니다. 
권장 크기는 `Item`의 내용이 변경될 때마다 
재계산될 수 있습니다. 응용 프로그램은 
``setPreferredSize`` 메소드에 
특정 매개 변수 값을 제공하여 권장 너비나 권장 높이(또는 둘 모두)를 
*잠글 수*있습니다. 응용 프로그램이 지정한 권장 크기에 
`Item`의 내용을 맞추는 방법은 구현별로 다릅니다. 
그러나 텍스트 내용은 단어 단위로 줄바꿈하여 응용 프로그램에서 
설정한 권장 크기에 맞추는 것이 좋습니다. 
응용 프로그램은 `setPreferredSize` 메소드의 
매개 변수에 `-1` 값을 
제공하여 두 치수 중 하나 또는 
모두를 *잠금 해제*할 수 있습니다.

`Item`이 작성되면 
권장 너비와 높이 모두 잠금 해제됩니다. 
이 상태에서 가능하면 `Item`의 그래픽 디자인과 
화면 치수와 같은 관련 요소를 포함하여 
`Item`의 
내용을 기준으로 권장 너비와 높이를 계산합니다. 
권장 너비 또는 높이를 잠근 후 
응용 프로그램에서는 
`setPreferredSize(-1, -1)`을 호출하여 
초기의 잠금 해제된 상태로 복원할 수 있습니다.

응용 프로그램은 권장 크기의 한 치수는 잠그고 
다른 치수는 잠금 해제 상태로 둘 수 있습니다. 
이렇게 하면 시스템은 잠긴 치수에 맞게 내용을 정렬하여 
잠금 해제된 치수의 적절한 값을 계산합니다. 
내용이 변경되면 잠금 해제된 치수의 크기는 
새로운 내용을 반영할 수 있도록 재계산되지만 잠금 해제된 치수의 
크기는 변경되지 않습니다. 
예를 들어, 응용 프로그램이 `setPreferredSize(50, -1)`을 
호출하면 권장 너비는 `50` 픽셀로 잠겨지고 
권장 높이는 `Item`의 내용을 기준으로 계산됩니다. 
이와 유사하게, 응용 프로그램이 
`setPreferredSize(-1, 60)`을 호출하면 
권장 높이는 `60` 픽셀로 잠겨지고 
권장 너비는 `Item`의 내용을 기준으로 계산됩니다. 
이 기능은 특히 줄 바꿈할 수 있는 텍스트 내용이 있는 
`Item`에 유용합니다.

응용 프로그램은 권장 너비와 높이 모두를 특정 값으로 
잠글 수도 있습니다. `Item`의 내용은 
이 요청을 처리하기 위해 필요에 따라 잘리거나 채워집니다. 
텍스트를 포함하는 `Item`의 경우 텍스트는 지정된 너비에 
맞춰 줄바꿈되어야 하며 텍스트의 끝부분에서 잘라야 합니다.

`Item`에는 구현에 의해 제공되는 암시적 최대 
크기도 있습니다. 최대 크기는 일반적으로 `Form`에 
사용 가능한 화면 공간의 너비를 기준으로 합니다. 
`Form`은 수직으로 스크롤할 수 있으므로 사용 가능한 
화면 공간의 높이를 기준으로 최대 높이를 설정하면 안 됩니다.

응용 프로그램이 권장 크기 수치를 최소보다 작거나 최대보다 
큰 값으로 잠그려고 하면 구현에서는 요청된 값을 무시하고 대신 
해당하는 최소값이나 최대값을 사용합니다. 
이런 경우 응용 프로그램은 
``getPreferredWidth`` 및 
``getPreferredHeight`` 메소드에서 
반환된 값을 통해 사용되는 실제 값을 볼 수 있습니다.

### 명령

``addCommand(javax.microedition.lcdui.Command)`` 또는 ``setDefaultCommand(javax.microedition.lcdui.Command)``를 
사전 호출하여 `Command`를 
`Item`에 추가한 후 ``removeCommand(javax.microedition.lcdui.Command)``를 호출하여 
`Command`를 
제거하지 않은 경우 `Item`에 
`Command`가 있다고 
합니다. 항목에 있는 `Command`는 `ITEM` 
명령 유형을 가져야 합니다. 
그러나, 유형이 `ITEM`이 아닌 
명령이 항목에 추가되는 것이 오류는 아닙니다. 
사용자 인터페이스 내에 표시되고 배치되도록 하기 위해 구현 시 
명령의 항목 유형이 `ITEM`인 것처럼 
처리할 수 있습니다.

`Item`은 *기본*
`Command`를 가질 수 있으며 
이 상태는 ``setDefaultCommand(javax.microedition.lcdui.Command)`` 메소드로 제어됩니다. 
기본 `Command`는 플랫폼 종속적인 특별한 사용자 
동작으로 연결될 수 있습니다. 
구현 시 해당 특정 `Item`에서 
기본 명령을 시작하기 위해 
가장 적합한 동작을 선택합니다. 
예를 들어, 전용 선택 키가 있는 장치에서 이 키를 누르면 항목의 
기본 명령을 호출할 수 있습니다. 
또는 스타일러스 기반 장치에서 
`Item`을 누르면 기본 명령을 호출할 수 있습니다. 
기본 명령은 특별한 동작을 통해 호출할 수 있지만 
다른 항목 명령과 같은 
방식으로 호출할 수도 있습니다.

장치에 따라 항목의 기본 명령을 호출하는 데 적합한 특별한 동작이 
없는 경우도 있습니다. 이런 경우 기본 명령은 다른 항목 명령과 
같은 방식으로 사용자가 접근할 수 있어야 합니다. 
구현 시 사용자 인터페이스 내에 
명령 배치 위치를 결정하기 위해 
기본 명령의 상태를 사용할 수 있습니다.

`Item`에 따라 
기본 명령이 없는 경우도 있습니다. 
이런 경우 특별한 사용자 동작(있는 경우)을 명령 메뉴 표시와 같은 
다른 용도에 사용할 수도 있습니다. 
`Item`의 기본 상태에는 
기본 명령이 없습니다. `Item`은 
`Item`에서 명령을 제거하거나 
`setDefaultCommand()` 메소드에 `null`을 
전달하여 기본 `Command`가 
없는 것으로 설정될 수 있습니다.

둘 이상의 `Item`과 둘 이상의 
`Displayable`에서 
같은 명령이 발생할 수 있습니다. 
이러한 상황이 발생하면 해당 `Item` 또는 
`Displayable`이 디스플레이에 표시되는 동안 
각 `Item` 또는 
`Displayable`에서 해당 명령을 
호출할 고유한 동작을 
사용자에게 제공해야 합니다. 
사용자가 명령을 호출하면 명령이 호출된 
해당 객체의 수신기(`CommandListener` 또는 
`ItemCommandListener`에 해당)가 
호출됩니다.

`Item`에 명령을 추가하면 모양, 
배치 방법 및 순회 동작에 영향을 미칠 수 있습니다. 
예를 들어, `Item`에 명령이 있으면 행이 분리되거나 
추가 그래픽 요소(예: 메뉴 아이콘)가 나타날 수 있습니다. 
특히, 모양 모드가 `PLAIN`(아래 참조)인 
`StringItem`에 하나 이상의 
`Command`가 제공되면 구현 시 이 항목에 
다른 모양 모드가 있는 것처럼 처리할 수 있습니다.

### 모양 모드

`StringItem` 및 `ImageItem` 클래스에는 
구성자에 설정할 수 있는 *모양 모드* 속성이 있습니다. 
이 속성은 ``PLAIN``, 
``HYPERLINK`` 또는 
``BUTTON`` 값 중 하나를 가질 수 있습니다. 
`PLAIN` 모양 모드는 일반적으로 텍스트나 
그래픽 자료의 비대화형 
디스플레이에 사용됩니다. 
모양 모드 값은 항목의 상호 작용에 어떠한 부작용도 미치지 않습니다. 
대화식이 되려면 항목에는 하나 이상의 
`Command`(기본 명령을 지정하는 것이 좋음)가 
있어야 하며 `Command` 호출 통지를 
수신하는 `CommandListener`가 있어야 합니다. 
모양 모드 값은 항목에서 `Command` 호출의 의미에 
영향을 미치지 않습니다. 
예를 들어, `StringItem`의 모양 모드를 
`HYPERLINK`로 설정하면 문자열 내용은 
브라우저에서 하이퍼링크인 것처럼 표시됩니다. 
하이퍼링크의 작업을 호출할 때 사용자가 기대하는 
동작(예: 링크의 참조 대상 로딩 또는 
링크를 사용자의 책갈피 집합에 추가)을 
제공하는 `StringItem`에 
`Command`와 
수신기를 연결하는 것은 응용 프로그램의 
책임입니다.

`Item`을 `PLAIN`이 아닌 
모양 모드로 설정하면 배치 방법뿐 아니라 항목의 최소, 권장 및 
최대 크기에까지 영향을 미칠 수 있습니다. 
예를 들어, 모양 모드가 `BUTTON`인 `StringItem`은 여러 행에 걸쳐 줄 바꾸기를 
수행할 수 없습니다. 그러나 모양 모드가 `HYPERLINK`인 
`StringItem`은 모양 모드가 `PLAIN`인 것과 
같은 방법으로 줄 바꾸기 되어야 합니다.

`BUTTON` 
모드에 있는 `StringItem` 
또는 `ImageItem`은 
버튼 기반 사용자 인터페이스를 작성하는 데 
사용할 수 있습니다. 그러면 응용 프로그램을 
사용하기가 불편해질 수 있습니다. 
예를 들어, 순회 기반 시스템에서 사용자가 버튼의 명령을 
호출하려면 해당 버튼으로 이동해야 합니다. 
버튼이 긴 `Form`에 흩어져 있다면 사용 가능한 
모든 명령을 찾기 위해 상당 시간 탐색을 수행해야 할 수 있습니다. 
게다가, `Form`의 다른 쪽 끝에 있는 버튼에서 
명령을 호출하는 것은 매우 번거로울 수 있습니다. 
순회 기반 시스템은 때로 특정 항목까지 순회할 필요 없이 
어디에서나(예: 메뉴) 명령을 호출할 수 있는 수단을 제공합니다. 
버튼에 명령을 추가하고 
해당 버튼을 `Form`에 배치하는 
대신 해당 명령을 `Form`에 직접 추가하는 것이 
더 적절하고 편리할 수 있습니다. 
버튼은 항목의 문자열이나 이미지 내용을 직접 사용해야 
해당 항목에서 호출 가능한 명령을 알 수 있는 경우에만 
사용되어야 합니다.

### 기본 상태

서브 클래스에서 별도로 지정하지 않는 한 새로 
작성된 `Item`의 기본 상태는 다음과 같습니다.

- 해당 `Item`은 어떠한 컨테이너에도 
들어 있지 않습니다("소유되지 않음")
- `Command`가 없습니다.
- 기본 `Command`가 `null`입니다.
- `ItemCommandListener`가 `null`입니다.
- 레이아웃 지시어 값이 `LAYOUT_DEFAULT`입니다.
- 권장 너비와 권장 높이가 모두 잠금 해제되어 있습니다.

**Since:**
- MIDP 1.0

## 필드 요약

- `static int BUTTON` — Item 이 버튼으로 표시됨을 나타내는 모양 모드 값.
- `static int HYPERLINK` — Item 이 하이퍼링크로 표시됨을 나타내는 모양 모드 값.
- `static int LAYOUT_2` — 새 MIDP 2.0 레이아웃 규칙이 이 Item 에 적용되어 있음을 나타내는 레이아웃 지시어.
- `static int LAYOUT_BOTTOM` — 이 Item 이 아래로 정렬된 레이아웃이어야 함을 나타내는 레이아웃 지시어.
- `static int LAYOUT_CENTER` — 이 Item 이 수평 중심 레이아웃이어야 함을 나타내는 레이아웃 지시어.
- `static int LAYOUT_DEFAULT` — 이 Item 이 해당 컨테이너의 기본 레이아웃 정책을 따라야 함을 나타내는 레이아웃 지시어.
- `static int LAYOUT_EXPAND` — 이 Item 의 너비가 사용 가능한 공간을 채우기 위해 늘어날 수 있음을 나타내는 레이아웃 지시어.
- `static int LAYOUT_LEFT` — 이 Item 이 왼쪽 정렬된 레이아웃이어야 함을 나타내는 레이아웃 지시어.
- `static int LAYOUT_NEWLINE_AFTER` — 이 Item 이 줄이나 행의 마지막 항목이어야 하고 컨테이너의 다음 Item (있는 경우)은 새 줄이나 행에 배치되어야 함을 나타내는 레이아웃 지시어.
- `static int LAYOUT_NEWLINE_BEFORE` — 이 Item 이 새 줄이나 행의 시작 위치에 배치되어야 함을 나타내는 레이아웃 지시어.
- `static int LAYOUT_RIGHT` — 이 Item 이 오른쪽 정렬된 레이아웃이어야 함을 나타내는 레이아웃 지시어.
- `static int LAYOUT_SHRINK` — 이 Item 의 너비가 최소 너비로 줄어들 수 있음을 나타내는 레이아웃 지시어.
- `static int LAYOUT_TOP` — 이 Item 이 위로 정렬된 레이아웃이어야 함을 나타내는 레이아웃 지시어.
- `static int LAYOUT_VCENTER` — 이 Item 이 수직 중심 레이아웃이어야 함을 나타내는 레이아웃 지시어.
- `static int LAYOUT_VEXPAND` — 이 Item 의 높이가 사용 가능한 공간을 채우기 위해 늘어날 수 있음을 나타내는 레이아웃 지시어.
- `static int LAYOUT_VSHRINK` — 이 Item 의 높이가 최소 높이로 줄어들 수 있음을 나타내는 레이아웃 지시어.
- `static int PLAIN` — Item 이 일반 모양임을 나타내는 모양 모드 값.

## 메서드 요약

- `void addCommand ( Command cmd)` — 컨텍스트에 맞는 Command 를 항목에 추가합니다.
- `String getLabel ()` — 이 Item 객체의 레이블을 가져옵니다.
- `int getLayout ()` — 항목을 배치하는 데 사용되는 레이아웃 지시어를 가져옵니다.
- `int getMinimumHeight ()` — 이 Item 의 최소 높이를 가져옵니다.
- `int getMinimumWidth ()` — 이 Item 의 최소 너비를 가져옵니다.
- `int getPreferredHeight ()` — 이 Item 의 권장 높이를 가져옵니다.
- `int getPreferredWidth ()` — 이 Item 의 권장 너비를 가져옵니다.
- `void notifyStateChanged ()` — Form 을 포함하는 이 Item 이 Item 의 `ItemStateListener` 에게 알려 줍니다.
- `void removeCommand ( Command cmd)` — 항목에서 상황에 맞는 명령을 제거합니다.
- `void setDefaultCommand ( Command cmd)` — 이 Item 에 기본 Command 를 설정합니다.
- `void setItemCommandListener ( ItemCommandListener l)` — 이 Item 에 Command 의 수신기를 설정하고 이전 ItemCommandListener 를 교체합니다.
- `void setLabel ( String label)` — Item 의 레이블을 설정합니다.
- `void setLayout (int layout)` — 이 항목에 레이아웃 지시어를 설정합니다.
- `void setPreferredSize (int width, int height)` — 이 Item 의 권장 너비와 높이를 설정합니다.

## 필드 상세

### LAYOUT_DEFAULT

```java
public static final int LAYOUT_DEFAULT
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_LEFT

```java
public static final int LAYOUT_LEFT
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_RIGHT

```java
public static final int LAYOUT_RIGHT
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_CENTER

```java
public static final int LAYOUT_CENTER
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_TOP

```java
public static final int LAYOUT_TOP
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_BOTTOM

```java
public static final int LAYOUT_BOTTOM
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_VCENTER

```java
public static final int LAYOUT_VCENTER
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_NEWLINE_BEFORE

```java
public static final int LAYOUT_NEWLINE_BEFORE
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_NEWLINE_AFTER

```java
public static final int LAYOUT_NEWLINE_AFTER
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_SHRINK

```java
public static final int LAYOUT_SHRINK
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_EXPAND

```java
public static final int LAYOUT_EXPAND
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_VSHRINK

```java
public static final int LAYOUT_VSHRINK
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_VEXPAND

```java
public static final int LAYOUT_VEXPAND
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### LAYOUT_2

```java
public static final int LAYOUT_2
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### PLAIN

```java
public static final int PLAIN
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### HYPERLINK

```java
public static final int HYPERLINK
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### BUTTON

```java
public static final int BUTTON
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### setLabel

```java
public void setLabel(String label)
```

**Parameters:**
- `label` - 레이블 문자열

**Throws:**
- `IllegalStateException` - 이 `Item`이 
`Alert`에 포함되어 있는 경우

**See Also:**
- ``getLabel()``

### getLabel

```java
public String getLabel()
```

**Returns:**
- 레이블 문자열

**See Also:**
- ``setLabel(java.lang.String)``

### getLayout

```java
public int getLayout()
```

**Returns:**
- 레이아웃 지시어 값의 조합

**Since:**
- MIDP 2.0

**See Also:**
- ``setLayout(int)``

### setLayout

```java
public void setLayout(int layout)
```

**Parameters:**
- `layout` - 이 항목의 레이아웃 지시어 값의 조합

**Throws:**
- `IllegalStateException` - 이 `Item`이 
`Alert`에 포함되어 있는 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getLayout()``

### addCommand

```java
public void addCommand(Command cmd)
```

**Parameters:**
- `cmd` - 추가되는 명령

**Throws:**
- `NullPointerException` - cmd가 `null`인 경우

**Since:**
- MIDP 2.0

### removeCommand

```java
public void removeCommand(Command cmd)
```

**Parameters:**
- `cmd` - 제거되는 명령

**Since:**
- MIDP 2.0

### setItemCommandListener

```java
public void setItemCommandListener(ItemCommandListener l)
```

**Parameters:**
- `l` - 새 수신기 또는 `null`

**Throws:**
- `IllegalStateException` - 이 `Item`이 
`Alert`에 포함되어 있는 경우

**Since:**
- MIDP 2.0

### getPreferredWidth

```java
public int getPreferredWidth()
```

**Returns:**
- 항목의 권장 너비

**Since:**
- MIDP 2.0

**See Also:**
- ``getPreferredHeight()``, 
``setPreferredSize(int, int)``

### getPreferredHeight

```java
public int getPreferredHeight()
```

**Returns:**
- `Item`의 권장 높이

**Since:**
- MIDP 2.0

**See Also:**
- ``getPreferredWidth()``, 
``setPreferredSize(int, int)``

### setPreferredSize

```java
public void setPreferredSize(int width,
                             int height)
```

**Parameters:**
- `height` - 높이를 잠글 값 또는 
잠금 해제할 경우 `-1`

**Throws:**
- `IllegalStateException` - 이 `Item`이 
`Alert`에 포함되어 있는 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getPreferredHeight()``, 
``getPreferredWidth()``

### getMinimumWidth

```java
public int getMinimumWidth()
```

**Returns:**
- 항목의 최소 너비

**Since:**
- MIDP 2.0

### getMinimumHeight

```java
public int getMinimumHeight()
```

**Returns:**
- 항목의 최소 높이

**Since:**
- MIDP 2.0

### setDefaultCommand

```java
public void setDefaultCommand(Command cmd)
```

**Parameters:**
- `cmd` - 이 `Item`의 기본 
`Command`로 사용될 명령 또는 
기본 명령이 없는 경우에는 `null`

**Throws:**
- `IllegalStateException` - 이 `Item`이 
`Alert`에 포함되어 있는 경우

**Since:**
- MIDP 2.0

### notifyStateChanged

```java
public void notifyStateChanged()
```

**Throws:**
- `IllegalStateException` - `Item`이 
`Form`의 소유가 아닌 경우

**Since:**
- MIDP 2.0

## 메서드 상세

### setLabel

```java
public void setLabel(String label)
```

**Parameters:**
- `label` - 레이블 문자열

**Throws:**
- `IllegalStateException` - 이 `Item`이 
`Alert`에 포함되어 있는 경우

**See Also:**
- ``getLabel()``

### getLabel

```java
public String getLabel()
```

**Returns:**
- 레이블 문자열

**See Also:**
- ``setLabel(java.lang.String)``

### getLayout

```java
public int getLayout()
```

**Returns:**
- 레이아웃 지시어 값의 조합

**Since:**
- MIDP 2.0

**See Also:**
- ``setLayout(int)``

### setLayout

```java
public void setLayout(int layout)
```

**Parameters:**
- `layout` - 이 항목의 레이아웃 지시어 값의 조합

**Throws:**
- `IllegalStateException` - 이 `Item`이 
`Alert`에 포함되어 있는 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getLayout()``

### addCommand

```java
public void addCommand(Command cmd)
```

**Parameters:**
- `cmd` - 추가되는 명령

**Throws:**
- `NullPointerException` - cmd가 `null`인 경우

**Since:**
- MIDP 2.0

### removeCommand

```java
public void removeCommand(Command cmd)
```

**Parameters:**
- `cmd` - 제거되는 명령

**Since:**
- MIDP 2.0

### setItemCommandListener

```java
public void setItemCommandListener(ItemCommandListener l)
```

**Parameters:**
- `l` - 새 수신기 또는 `null`

**Throws:**
- `IllegalStateException` - 이 `Item`이 
`Alert`에 포함되어 있는 경우

**Since:**
- MIDP 2.0

### getPreferredWidth

```java
public int getPreferredWidth()
```

**Returns:**
- 항목의 권장 너비

**Since:**
- MIDP 2.0

**See Also:**
- ``getPreferredHeight()``, 
``setPreferredSize(int, int)``

### getPreferredHeight

```java
public int getPreferredHeight()
```

**Returns:**
- `Item`의 권장 높이

**Since:**
- MIDP 2.0

**See Also:**
- ``getPreferredWidth()``, 
``setPreferredSize(int, int)``

### setPreferredSize

```java
public void setPreferredSize(int width,
                             int height)
```

**Parameters:**
- `height` - 높이를 잠글 값 또는 
잠금 해제할 경우 `-1`

**Throws:**
- `IllegalStateException` - 이 `Item`이 
`Alert`에 포함되어 있는 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getPreferredHeight()``, 
``getPreferredWidth()``

### getMinimumWidth

```java
public int getMinimumWidth()
```

**Returns:**
- 항목의 최소 너비

**Since:**
- MIDP 2.0

### getMinimumHeight

```java
public int getMinimumHeight()
```

**Returns:**
- 항목의 최소 높이

**Since:**
- MIDP 2.0

### setDefaultCommand

```java
public void setDefaultCommand(Command cmd)
```

**Parameters:**
- `cmd` - 이 `Item`의 기본 
`Command`로 사용될 명령 또는 
기본 명령이 없는 경우에는 `null`

**Throws:**
- `IllegalStateException` - 이 `Item`이 
`Alert`에 포함되어 있는 경우

**Since:**
- MIDP 2.0

### notifyStateChanged

```java
public void notifyStateChanged()
```

**Throws:**
- `IllegalStateException` - `Item`이 
`Form`의 소유가 아닌 경우

**Since:**
- MIDP 2.0
