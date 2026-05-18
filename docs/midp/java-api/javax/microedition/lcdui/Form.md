# Class Form

`package javax.microedition.lcdui`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.Displayable
        |
        +--javax.microedition.lcdui.Screen
              |
              +--javax.microedition.lcdui.Form
```

## 설명

**extends Screen:**

`Form`은 이미지, 읽기 전용 텍스트 필드, 
편집 가능 텍스트 필드, 편집 가능 날짜 필드, 게이지, 선택 그룹 및 
사용자 정의 항목 등의 임의 혼합을 포함하는 `Screen`입니다. 
일반적으로 ``Item`` 클래스의 모든 서브 클래스는 양식 안에 
포함될 수 있습니다. 구현 시 레이아웃, 순회 및 
스크롤을 처리합니다. `Form`의 전체 내용은 
함께 스크롤됩니다.

`Form` 안에 
포함된 항목은 append, delete, insert, 
및 set 메소드를 사용하여 편집할 수 있습니다. `Form` 
내의 `Item`은 
해당 색인으로 참조되며 0에서 
`size()-1`까지의 범위에 있는 연속 정수로, 
0은 첫 번째 항목을 참조하고 `size()-1`은 
마지막 항목을 참조합니다.

한 항목은 한 `Form` 내에만 놓일 수 있습니다. 
응용 프로그램이 한 항목을 
`Form`에 놓으려 하고 
해당 항목을 이것이나 다른 
`Form`이 이미 소유한 경우 
`IllegalStateException`이 발생합니다. 
항목을 새 `Form`에 
삽입하기 전에 응용 프로그램은 
현재 포함하는 `Form`에서 
해당 항목을 제거해야 합니다.

응용 프로그램에서 내용에 대한 변경을 요청할 때 
디스플레이에 `Form`이 표시되는 경우 
구현 시 가능한 한 빨리 
디스플레이에 대한 업데이트가 이루어집니다. 
양식의 내용이 수정된 다음 응용 프로그램은 
`Form`의 디스플레이를 갱신하기 위해 
아무런 작업을 수행하지 않아도 됩니다.

`Form`의 레이아웃 정책은 행을 중심으로 구성됩니다. 
행은 일반적으로 여백, 스크롤 막대 등과 함께 화면의 너비와
연관되어 있습니다. 특정 `Form`에 있는 
모든 행의 너비는 같습니다. 
스크롤 막대를 추가하거나 제거해야 하는 것과 같은 
특수 상황에서 행의 너비를 모두 변경할 수는 있지만 
행 너비는 `Form`에 포함된 `Item`에 따라 
달라지지 않습니다. 
`Form`은 일반적으로 가로로 
스크롤하지 않습니다.

`Form`은 세로로 확장되므로 필요하면 
세로로 스크롤합니다. `Form`의 높이는 행의 
수와 각 행의 높이에 따라 달라집니다. 
각 행의 높이는 해당 행에 위치한 항목에 따라 결정됩니다. 
행의 높이가 모두 같아야 할 필요는 없습니다. 
`Item` 레이블을 세로로 정렬하거나 
적절한 채워넣기를 제공하기 위해 구현 시 행 높이가 
달라질 수도 있습니다.

사용 중인 언어 규칙에 따라 구현 시 왼쪽에서 
오른쪽이나 오른쪽에서 왼쪽 방향으로 `Item`을 
배치하도록 선택할 수 있습니다. 레이아웃 방향과 같게 선택하면 
특정 `Form` 내의 모든 행에 적용해야 합니다.

레이아웃 알고리즘을 시작하기 전에 
`Form`은 맨 위에 
빈 행이 하나 있는 것으로 간주됩니다. 
레이아웃 알고리즘은 `Item` 0에서 
시작하여 `Form`의 
마지막 `Item`이 처리될 
때까지 각 `Item`을 차례로 진행합니다. 
레이아웃 방향(위에 설명)이 왼쪽에서 오른쪽인 경우 
행은 `Form`의 왼쪽 
가장자리부터 시작합니다. 
레이아웃 방향이 오른쪽에서 왼쪽인 경우 
행은 `Form`의 오른쪽 가장자리부터 시작합니다. 
행 압축을 일찍 종료시키는 조건이 발생하지 않는 한 
`Item`은 각 행의 
시작 부분에 놓이며 선택된 
레이아웃 방향의 각 행을 거쳐 진행하여 
각 행에 들어갈 만큼 압축됩니다. 
그런 다음 새 행이 추가되고 위에 설명된 대로 거기에 
`Item`이 압축됩니다. `Item`이 행에 
압축되고 레이아웃 알고리즘에 의해 모든 `Item`이 
처리될 때까지 기존 행 아래에 새 행이 
필요한 만큼 추가됩니다.

레이아웃 알고리즘은 *현재 정렬*의 개념을 가집니다. 
`LAYOUT_LEFT`, `LAYOUT_CENTER` 
또는 `LAYOUT_RIGHT`의 값일 수 있습니다. 
레이아웃 알고리즘 시작 시 현재 정렬의 값은 
이 `Form`에 유효한 레이아웃 방향에 따라 달라집니다. 
레이아웃 방향이 왼쪽에서 오른쪽인 경우 
초기 정렬 값은 `LAYOUT_LEFT`여야 합니다. 
레이아웃 방향이 오른쪽에서 왼쪽인 경우 
초기 정렬 값은 `LAYOUT_RIGHT`여야 합니다. 
레이아웃 알고리즘에 `LAYOUT_LEFT`, 
`LAYOUT_CENTER` 또는 `LAYOUT_RIGHT` 
레이아웃 지시어 중 하나를 가진 `Item`이 나타나면 
현재 정렬이 변경됩니다. `Item`에 이러한 지시어 중 
어느 하나도 없으면 현재 레이아웃 지시문은 변경되지 않습니다. 
이 규칙은 정렬 값을 공유하는 연속 `Item`의 시퀀스로 `Form`의 
내용을 그룹화하는 효과가 있습니다. 
각 `Item`의 정렬 값은 `Form`에 대해 
내부적으로 유지되어야 하며 ``Item.getLayout`` 
메소드에서 보고할 때 `Item`의 레이아웃 값에 영향을 미치지 않습니다.

"행 바꿈"을 일으키는 특정 조건이 
발생하지 않는 한 레이아웃 알고리즘은 일반적으로 
이전 항목과 같은 행에 항목을 두려고 시도합니다. 
행 바꿈이 있으면 현재 항목은 여유 공간이 있더라도 
이전 항목 다음이 아닌 새 행의 
시작 부분에 놓입니다.

다음 조건 중 하나가 발생하면 행 바꿈이 
항목 앞에서 발생합니다.

- 이전 행 다음에 행 바꿈이 있습니다.
- `LAYOUT_NEWLINE_BEFORE` 지시문이 있습니다.
- `StringItem` 내용이 "\n"으로 시작됩니다.
- `ChoiceGroup`, 
`DateField`, 
`Gauge` 또는 `TextField` 
중 하나이며 `LAYOUT_2` 지시문이 
설정되어 있지 않습니다.
- 이 `Item`에는 `Form`의 
현재 정렬과 다른 `LAYOUT_LEFT`, 
`LAYOUT_CENTER` 또는 `LAYOUT_RIGHT` 지시문 중 하나가 있습니다.

다음 조건 중 하나가 발생하면 항목 뒤에 
행 바꿈이 발생합니다.

- `StringItem` 내용이 "\n"으로 
끝납니다.
- `LAYOUT_NEWLINE_AFTER` 지시문이 있습니다.
- `ChoiceGroup`, `DateField`, 
`Gauge` 또는 `TextField` 중 하나이며 
`LAYOUT_2` 지시문이 설정되어 있지 않습니다.

이미 행 바꿈이 이미 있는 경우 
`LAYOUT_NEWLINE_BEFORE`나 
`LAYOUT_NEWLINE_AFTER` 지시문이 있더라도 
추가 행 바꿈이 발생하지 않습니다. 
예를 들어, 내용이 "\n"으로 시작하는 
`StringItem`에 `LAYOUT_NEWLINE_BEFORE` 
지시문이 표시되는 경우 행 바꿈은 하나만 있습니다. 
유사한 규칙이 후행 "\n"과 
`LAYOUT_NEWLINE_AFTER`에도 적용됩니다. 
또한 한 항목에 `LAYOUT_NEWLINE_AFTER` 지시문이 있고 
다음 항목에 `LAYOUT_NEWLINE_BEFORE` 지시문이 있는 경우 
행 바꿈은 하나만 있습니다. 
하지만 단일 `StringItem` 내에 또는 
인접 `StringItem`에 연속 "\n" 문자가 
있으면 "\n" 문자 만큼의 행 바꿈이 발생합니다. 
이렇게 하면 빈 행이 생깁니다. 
행을 끝내는 "\n"이 발생하는 `StringItem`의 일반적인 글꼴 높이에 의해 빈 행의 높이가 결정됩니다.

구현 시 행 바꿈이 일어날 수 있는 추가 조건을 제공할 수 있습니다. 
예를 들어, 구현 시 레이아웃 정책에 따라 
레이블이 특별하게 배치될 수 있습니다. 
따라서 레이블이 있는 모든 `Item` 앞에는 암시적으로 
줄 바꿈이 일어납니다. 또 다른 예로 특정 구현 시 사용자 인터페이스 
스타일에서 DateField 항목이 항상 한 행에 따로 표시되도록 
지시할 수 있습니다. 이 경우 구현 시 각 `DateField` 항목의 
앞과 뒤에서 모두 행 바꿈이 발생하게 됩니다.

인접한 `Form` 색인이 있는 
두 개의 항목이 있을 때 두 항목 사이의 행 바꿈에 대해 지정한 조건이나 
구현별 조건이 발생하지 않고 공간이 허용하는 경우 
이러한 항목은 같은 행에 
놓여야 합니다.

한 행에 `Item`을 압축할 때 항목의 
너비는 행의 나머지 공간과 비교됩니다. 
이를 위해 `Item`에 
`Item`의 최소 너비를 
사용하는 `LAYOUT_SHRINK` 지시문이 없는 경우 
`Item`의 기본 너비가 사용됩니다. 
`Item`의 너비가 
행에 남아 있는 공간에 비해 
너무 넓은 경우 해당 행은 가득 찬 것으로 간주되어 
이 행 바로 아래에 새 행이 추가되고 
`Item`이 
새 행에 놓입니다.

일단 행의 내용이 결정되면 항목을 확장하고 
항목 사이에 공간을 추가하여 행에서 사용 가능한 공간이 분산됩니다. 
이 행의 항목에 `LAYOUT_SHRINK` 지시문이 있는 
경우(즉, 축소 가능한 경우) 공간이 이러한 항목에 먼저 분산됩니다. 
공간은 `Item`의 기본 
크기와 최소 크기 간의 차이에 
비례하여 이러한 각 항목에 분산됩니다. 
이 단계에서 기본 너비를 초과하여 확장되는 
축소 가능 항목은 없습니다.

예를 들어, 한 행에 사용 가능한 공간이 `30`픽셀이고 
두 개의 축소 가능 항목 `A`와 `B`가 있다고 
가정합니다. `A` 항목의 기본 크기는 
`15`이고 최소 크기는 
`10`입니다. 
`B` 항목의 기본 크기는 
`30`이고 
최소 크기는 `20`입니다. 
`A`의 기본 크기와 최소 크기의 차이는 
`5`이며 `B`의 
차이는 `10`입니다. 
이러한 차이에 비례하여 `30` 픽셀이 
이러한 항목에 분산됩니다. 
따라서 `10` 픽셀은 
`A` 항목에 분산되고 `20` 픽셀은 
`B` 항목에 분산됩니다.

축소 가능 항목을 기본 너비로 모두 확장해도 여전히 
행에 남는 공간이 있습니다. 이 남은 공간은 
`LAYOUT_EXPAND` 
지시문(확장 가능 `Item`)이 
있는 항목 사이에 균등하게 분산됩니다. 
행에 확장 가능 항목이 있으면 
이 행의 `Item`이 행의 
전체 너비를 차지하게 됩니다.

이 행에 확장 가능 항목이 없고 사용 가능한 공간은 
있는 경우 `Item`은 가능한 한 빽빽하게 압축되고 
이 행의 `Item`에서 공유하는 정렬 값에 따라 행에 놓입니다. 
현재 정렬을 변경하면 행 바꿈이 
일어나기 때문에 같은 행에 있는 
모든 `Item`은 같은 정렬 값을 공유해야 합니다. 
정렬 값이 `LAYOUT_LEFT`인 경우 `Item`은 
행의 왼쪽 끝에 놓이며 나머지 공간은 행의 오른쪽 끝에 놓입니다. 
정렬 값이 `LAYOUT_RIGHT`인 경우 `Item`은 
행의 오른쪽 끝에 놓이며 나머지 공간은 행의 왼쪽 끝에 놓입니다. 
정렬 값이 `LAYOUT_CENTER`인 경우 나머지 공간이 
행의 왼쪽 끝과 오른쪽 끝에 균등하게 
나뉘도록 `Item`은 
행의 중간에 놓입니다.

특정 행에 항목 집합이 있다고 가정하면 
이러한 `Item`의 높이가 검사됩니다. 
각 `Item`에서 
`Item`의 최소 높이를 
사용하는 `LAYOUT_VSHRINK` 지시문이 
`Item`에 없는 경우 기본 높이가 사용됩니다. 
`Item`의 
최고 높이가 행의 높이를 결정합니다. 
`LAYOUT_VSHRINK` 
지시문이 있는 `Item`이 
기본 높이나 해당 행의 높이 중 작은 값으로 확장됩니다. 
행 높이보다 짧고 `LAYOUT_VEXPAND` 지시문이 
있는 `Item`은 
해당 행의 높이로 확장됩니다. 
한 항목에 있는 
`LAYOUT_VEXPAND` 지시문은 
행의 높이를 결코 늘리지 않습니다.

행 높이보다 짧은 나머지 `Item`은 
`LAYOUT_TOP`, `LAYOUT_BOTTOM` 및 
`LAYOUT_VCENTER` 지시문을 사용하여 행 내에서 
수직으로 배치됩니다. 수직 레이아웃 
지시문이 지정되어 있지 않은 경우 
항목은 행의 아래쪽을 따라 정렬되어야 합니다.

`StringItem`은 
위의 알고리즘에서 특수 처리됩니다. 
`StringItem`의 
내용(레이블을 제외한 문자열 값)이 
개행 문자("\n")를 포함하는 경우 문자열은 
그 지점에서 분할되어야 하며 나머지는 
다음 행의 시작 부분에 놓여야 합니다.

`StringItem` 기본 크기의 하나나 
두 개의 치수가 잠긴 경우 `StringItem`은 
해당 너비와 높이에 맞춰 줄 바꿈되며 최소 및 기본 너비와 높이가 
이 직사각형의 너비와 높이인 직사각형으로 처리됩니다. 
이 경우 `LAYOUT_SHRINK`, 
`LAYOUT_EXPAND` 
및 `LAYOUT_VEXPAND` 지시문은 무시됩니다.

`StringItem` 기본 크기의 두 치수가 
잠기지 않은 경우 `StringItem`의 텍스트는 
여러 행에 걸쳐 줄 바꿈할 수 있습니다. 
`Item`의 너비가 행의 나머지 공간과 비교되는 
레이아웃 알고리즘에서는 현재 행에 맞춰 `StringItem` 
시작 부분에서 텍스트가 선택됩니다. 
그런 다음 이 행의 내용은 현재 정렬 값에 따라 배치됩니다. 
`StringItem`의 텍스트 나머지 부분은 텍스트를 
채워 넣는 데 필요한 만큼 많은 새 행을 전체 너비로 줄 바꿈합니다. 
채워진 각 행은 현재 정렬 값에 따라 배치됩니다. 
텍스트의 마지막 줄에는 해당 행에 사용 가능한 공간이 남습니다. 
이 `StringItem` 뒤에 행 바꿈이 없으면 
후속 `Item`은 나머지 공간에 압축되며 행의 내용은 
현재 정렬 값을 따라 배치됩니다. 
이 규칙은 현재 정렬 값이 `LAYOUT_LEFT`, 
`LAYOUT_RIGHT` 또는 `LAYOUT_CENTER`인지에 
따라 `StringItem`의 내용을 왼쪽 맞춤, 
오른쪽 맞춤 또는 가운데 맞춤으로 설정된 텍스트 단락으로 표시하는 
효과를 가집니다. 
``Item.getPreferredWidth``와
``Item.getPreferredHeight`` 메소드에서 
보고하는 대로 여러 행에 걸쳐 줄 바꿈된 
`StringItem`의 기본 너비와 높이는 줄 바꿈된 
텍스트의 경계 직사각형의 너비와 높이를 설명합니다.

`ImageItem`은 위의 알고리즘에 의해 
특수하게 처리됩니다. 수평 정렬 값 및 
`LAYOUT_LEFT`, `LAYOUT_RIGHT`, 
`LAYOUT_CENTER` 지시문과 관련하여 앞에 언급한 규칙은 
`LAYOUT_2` 지시문이 해당 항목에 있는 경우에만 
`ImageItem`에 적용됩니다. 
`LAYOUT_2` 지시문이 `ImageItem`에 없으면 
`LAYOUT_LEFT`, `LAYOUT_RIGHT` 및 
`LAYOUT_CENTER` 지시문의 동작은 구현별로 달라집니다.

`Form`의 레이아웃은 
필요하면 자동으로 다시 계산됩니다. 
이는 내용의 변경으로 인한 `Item`의 크기 변경으로 인해 
또는 해당 항목의 기본 크기를 변경하기 위한 응용 프로그램의 
요청으로 인해 발생할 수 있습니다. 
응용 프로그램이 `Item`의 레이아웃 지시문을 
변경한 경우에도 발생할 수 있습니다. 
응용 프로그램은 `Form`의 
레이아웃을 업데이트하기 위해 
특정 작업을 수행하지 않아도 됩니다.

텍스트가 줄 바꾸기되는 모든 경우 줄 바꿈은 
개행 문자(`'\n'` = Unicode `'U+000A'`)마다 
발생해야 합니다. 전체 텍스트를 표시할 공간이 없는 경우 
줄 바꿈에서 잘립니다. 적절한 
줄 바꿈이 없는 경우 구현 시 단어를 
경계로 텍스트를 자르는 것이 좋습니다. 
단어 경계가 없는 경우 구현 시 문자를 경계로 텍스트를 
자르는 것이 좋습니다.

줄 바꿈이 있는 레이블은 줄 바꿈에서 잘리고 
레이블의 나머지 부분이 표시되지 않을 수 있습니다.

디스플레이에 `Form`이 있으면 
사용자는 해당 `Item`과 
무한정으로 상호 작용할 수 
있습니다(예: `Item`에서 
`Item`으로 순회 및 
가능한 경우 스크롤). 이러한 순회 및 
스크롤 작업은 응용 프로그램 표시 
가능 이벤트를 발생시키지 않습니다. 
`Form`에 포함된 상호 작용 
`Item`의 상태를 
사용자가 수정하면 시스템은 응용 프로그램에 알립니다. 
``setItemStateListener()`` 메소드와 
함께 `Form`에 선언된 수신기의 ``itemStateChanged()`` 
메소드를 호출하여 
알릴 수 있습니다.

다른 `Displayable` 객체와 마찬가지로 
`Form`은 ``commands``를 선언하고 
``setCommandListener()`` 메소드와 
함께 명령 수신기를 
선언할 수 있습니다. 
``CommandListener`` 객체는 
``ItemStateListener`` 객체와 
구분되며 별도로 선언되고 호출됩니다.

- 이 클래스는 구성 요소를 임의로 
조합하는 것을 허용하지만 
응용 프로그램 개발자는 
작은 화면 크기를 유념해야 합니다. 
`Form`은 *소수의 밀접히 연관된* UI 요소를 
포함하도록 설계되었습니다.
- 여러 개의 항목을 화면에 넣을 수 없는 경우 요소를 편집할 때 별도의 화면이 나타나도록 
화면을 스크롤할 수 있게 할 것인지 일부 구성 요소를 접을 것인지를 
구현 시 선택할 수 있습니다.

**Since:**
- MIDP 1.0

**See Also:**
- ``Item``

## 생성자 요약

- Form ( String title) 새로운, 빈 Form 을 만듭니다.
- Form ( String title, Item [] items) 지정된 내용으로 새 Form 을 만듭니다.

## 메서드 요약

- `int append ( Image img)` — 한 개의 Image 로 구성된 항목을 Form 에 추가합니다.
- `int append ( Item item)` — Item 을 Form 에 추가합니다.
- `int append ( String str)` — 한 개의 String 으로 구성된 항목을 Form 에 추가합니다.
- `void delete (int itemNum)` — itemNum 이 참조하는 Item 을 삭제합니다.
- `void deleteAll ()` — 이 Form 에서 모든 항목을 삭제하여 0개의 항목을 남깁니다.
- `Item get (int itemNum)` — 지정된 위치에서 항목을 가져옵니다.
- `int getHeight ()` — 항목에 대해 사용할 수 있는 표시 가능 영역의 높이(픽셀 단위)를 반환합니다.
- `int getWidth ()` — 항목에 대해 사용할 수 있는 표시 가능 영역의 너비(픽셀 단위)를 반환합니다.
- `void insert (int itemNum, Item item)` — Form 에 지정된 항목 바로 앞에 항목을 삽입합니다.
- `void set (int itemNum, Item item)` — itemNum 이 참조하는 항목을 지정 항목으로 설정하여 이전 항목을 대체합니다.
- `void setItemStateListener ( ItemStateListener iListener)` — 이전의 모든 ItemStateListener 를 대체하여 Form 에 대한 ItemStateListener 를 설정합니다.
- `int size ()` — Form 에 있는 항목의 수를 가져옵니다.

## 생성자 상세

### Form

```java
public Form(String title)
```

- 새로운, 빈 `Form`을 만듭니다.

**Parameters:**
- `title` - `Form`의 제목, 또는 제목이 없는 경우 
`null`

### Form

```java
public Form(String title,
            Item[] items)
```

- 지정된 내용으로 새 `Form`을 만듭니다. 
이는 빈 `Form`을 만든 다음 일련의 
`append` 메소드를 
사용하는 것과 같습니다. 
항목 배열은 `null`일 수 있으며 이 경우 
`Form`은 
빈 상태로 만들어집니다. 
항목 배열이 null이 아닌 경우 각 요소는 다른 
`Form`에 이미 포함되지 않은 유효한 
`Item`이어야 합니다.

**Parameters:**
- `items` - `Form`에 
놓일 항목의 배열, 
또는 항목이 없는 경우 `null`

**Throws:**
- `NullPointerException` - 항목 배열의 요소가 
`null`인 경우

### append

```java
public int append(Item item)
```

**Parameters:**
- `item` - 추가되는 ``Item``

**Returns:**
- `Item`의 할당된 색인

**Throws:**
- `NullPointerException` - 항목이 `null`인 경우

### append

```java
public int append(String str)
```

**Parameters:**
- `str` - 추가되는 `String`

**Returns:**
- `Item`의 할당된 색인

**Throws:**
- `NullPointerException` - str이 `null`인 경우

### append

```java
public int append(Image img)
```

**Parameters:**
- `img` - 추가되는 이미지

**Returns:**
- `Item`의 할당된 색인

**Throws:**
- `NullPointerException` - `img`가 `null`인 경우

### insert

```java
public void insert(int itemNum,
                   Item item)
```

**Parameters:**
- `item` - 삽입되는 항목

**Throws:**
- `NullPointerException` - `item`이 
`null`인 경우

### delete

```java
public void delete(int itemNum)
```

**Parameters:**
- `itemNum` - 삭제되는 항목의 색인

**Throws:**
- `IndexOutOfBoundsException` - `itemNum`이 유효하지 않은 경우

### deleteAll

```java
public void deleteAll()
```

**Since:**
- MIDP 2.0

### set

```java
public void set(int itemNum,
                Item item)
```

**Parameters:**
- `item` - `Form`에 놓일 새 항목

**Throws:**
- `NullPointerException` - `item`이 
`null`인 경우

### get

```java
public Item get(int itemNum)
```

**Parameters:**
- `itemNum` - 항목의 색인

**Returns:**
- 지정된 위치의 항목

**Throws:**
- `IndexOutOfBoundsException` - `itemNum`이 유효하지 않은 경우

### setItemStateListener

```java
public void setItemStateListener(ItemStateListener iListener)
```

**Parameters:**
- `iListener` - 새 수신기, 또는 이를 제거하려면 `null`

### size

```java
public int size()
```

**Returns:**
- 항목의 수

### getWidth

```java
public int getWidth()
```

**Overrides:**
- `getWidth` in class `Displayable`

**Returns:**
- `Form`의 너비(픽셀 단위)

**Since:**
- MIDP 2.0

### getHeight

```java
public int getHeight()
```

**Overrides:**
- `getHeight` in class `Displayable`

**Returns:**
- `Form`의 
표시 가능 영역 높이(픽셀 단위)

**Since:**
- MIDP 2.0

## 메서드 상세

### append

```java
public int append(Item item)
```

**Parameters:**
- `item` - 추가되는 ``Item``

**Returns:**
- `Item`의 할당된 색인

**Throws:**
- `NullPointerException` - 항목이 `null`인 경우

### append

```java
public int append(String str)
```

**Parameters:**
- `str` - 추가되는 `String`

**Returns:**
- `Item`의 할당된 색인

**Throws:**
- `NullPointerException` - str이 `null`인 경우

### append

```java
public int append(Image img)
```

**Parameters:**
- `img` - 추가되는 이미지

**Returns:**
- `Item`의 할당된 색인

**Throws:**
- `NullPointerException` - `img`가 `null`인 경우

### insert

```java
public void insert(int itemNum,
                   Item item)
```

**Parameters:**
- `item` - 삽입되는 항목

**Throws:**
- `NullPointerException` - `item`이 
`null`인 경우

### delete

```java
public void delete(int itemNum)
```

**Parameters:**
- `itemNum` - 삭제되는 항목의 색인

**Throws:**
- `IndexOutOfBoundsException` - `itemNum`이 유효하지 않은 경우

### deleteAll

```java
public void deleteAll()
```

**Since:**
- MIDP 2.0

### set

```java
public void set(int itemNum,
                Item item)
```

**Parameters:**
- `item` - `Form`에 놓일 새 항목

**Throws:**
- `NullPointerException` - `item`이 
`null`인 경우

### get

```java
public Item get(int itemNum)
```

**Parameters:**
- `itemNum` - 항목의 색인

**Returns:**
- 지정된 위치의 항목

**Throws:**
- `IndexOutOfBoundsException` - `itemNum`이 유효하지 않은 경우

### setItemStateListener

```java
public void setItemStateListener(ItemStateListener iListener)
```

**Parameters:**
- `iListener` - 새 수신기, 또는 이를 제거하려면 `null`

### size

```java
public int size()
```

**Returns:**
- 항목의 수

### getWidth

```java
public int getWidth()
```

**Overrides:**
- `getWidth` in class `Displayable`

**Returns:**
- `Form`의 너비(픽셀 단위)

**Since:**
- MIDP 2.0

### getHeight

```java
public int getHeight()
```

**Overrides:**
- `getHeight` in class `Displayable`

**Returns:**
- `Form`의 
표시 가능 영역 높이(픽셀 단위)

**Since:**
- MIDP 2.0
