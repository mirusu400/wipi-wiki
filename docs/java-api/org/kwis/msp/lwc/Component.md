# Class Component

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
```

## 설명

**Direct Known Subclasses:**
- `ButtonComponent`, `ComboComponent`, `CommandBarComponent`, `ContainerComponent`, `DateFieldComponent`, `ImageComponent`, `LabelComponent`, `ProgressComponent`, `ScrollbarComponent`, `TextComponent`, `TickerComponent`

**extends Object:**

가장 기본이 되는 화면에 보여지는 클래스입니다.

위치과 크기를 가지며, 사용자의 입력을 받아서 적절한 행동을 하는
 클래스입니다.

화면에 보여지는 모든 UI 컴포넌트는 이 클래스를 상속 받아서
 구현되어야 합니다.

`Component` 클래스를 상속 받은 자식 클래스들의 상위
 부모 컴포넌트 상에서의
 위치와 폭과 넓이를 가지며,
 배경색과 컴포넌트의 특성(입력 가능인지, 입력 포커스등)을 가집니다.

`Component`클래스는 항상 상위 부모가 있어야 하며,
 상위 부모가 없어도 되는
 `Component`
 는 ``ShellComponent``가 됩니다. 즉, 화면에 적어도 하나 이상의
 `ShellComponent`
 가 있어야지만, `Component`가 화면에 보이게 됩니다.
 컴포넌트는 `addComponent`한 후에 다른 부모 컴포넌트에
 더이상 `addComponent`할수 없습니다.

모든 컴포넌트는 자신의 폭과 넓이를 프로그램에 의해서 결정할수 있지만,
 때에 따라서는 상위 컴포넌트에 의해서 그 크기가 결정이 됩니다.
 예를 들면, `FormComponent`위에 있는
 `LabelComponent`와 같은 컴포넌트는 내부의 문자열의 길이에 따라서,
 `Component`의 크기가 달라집니다.

수행 도중에 사용자가 컴포넌트의 내용을 변경함으로써, 컴포넌트의 크기가
 다시 계산될 필요가 있다면, `invalidate`함수를 호출합니다.
 그러면, `Component`가 화면에 보여질 때나,
 `paintContent`함수가 호출될 때에
 `validate()`함수를 호출하며, 이 함수에 의해 하위 컴포넌트까지
 다시 모두 적당한 크기가 계산이 됩니다.

컴포넌트는 자신의 적절한 크기를 계산하여 돌려주는 기능을 가집니다.
 컴포넌트의 내용에 따라서 적당한 크기를 돌려주며, 이 함수는 상위의
 `ContainerComponent`의 `layout`함수에서
 하위 컴포넌트의 크기를 결정하기 위해서
 사용됩니다. 포맷팅을 할 수 있는 컴포넌트(`Label`,
`TextField`, `TextArea`)를
 위해서 특정 폭을 주었을때 적당한 높이을 얻어오는 함수도 있습니다.

컴포넌트의 크기 결정은 자신이 하는 것이 아니라 상위 컴포넌트가 결정합니다.
 그 상위 컴포넌트의 전체 크기는 상위 컴포넌트의 상위 컴포넌트가 합니다.
 모든 UI컴포넌트는 맨 마지막 상위 컴포넌트는
 항상 `ShellComponent`가 되어야 합니다.

컴포넌트는 이벤트에 대해서 처리할 책임을 가집니다.
 만일 컴포넌트의 `CanHandleInput`함수가 `true`를
 돌려주면,
 그 컴포넌트는 `ContainerComponent`의
 `setFocus`함수에 의해서 입력
 포커스를 가질 수 있으며, 입력 포커스를 가지는 경우에
 `keyNotify`함수가 불릴 수 있습니다.
 이외에도 `showNotify`함수와 `focusNotify`함수,
 `pointerNotify`함수가 불리며,
 특히나 화면에 어떤 내용을 칠해야 하는 경우에는
 `paintContent`함수가 불립니다.

`keyNotify`함수나 `pointerNotify`함수는
 자기 자신이 이벤트를 처리했으면,
 `true`를 돌려줍니다. 그러면, 상위 컴포넌트에
 키 이벤트가 전달되지 않습니다.
 만일 `false`를 돌려주면, 상위 컴포넌트에 키 이벤트가 전달됩니다.

모든 이벤트에 대해서는 `setEventListener`함수를 통하여
 지정된 이벤트 리스너에게 모든 발생한 이벤트를 알려줍니다.
 이 이벤트 리스너가 `true`로 돌려주는 경우에는 더 이상
 이벤트가 처리되지 않고 `false`로 돌려주는 경우에는
 이벤트는 정상적으로 처리 됩니다.

`paintContent`함수를 구현할 때에는
 `Graphics`내용이 컴포넌트의 위치와 크기에 맞도록
 원점과 클리핑 영역이 변경되어서 되어서 넘어 옵니다.
 만일 이 클리핑의 내용을 setClip함수로 변경하거나, `reset`
 함수로 재 초기화를 시키면
 컴포넌트의 내용이 엉뚱한 곳에 출력되거나 화면에 나중에 나타나는등의
 문제가 생길 수 있습니다.

에서 제공하고 있는 정렬형태는

와

,

,

,

,

입니다.
 아래의 경우

이 발생합니다.

- `LAYOUT_LEFT`|`LAYOUT_RIGHT`
- ```java
LAYOUT_LEFT|LAYOUT_HCENTER
LAYOTU_RIGHT|LAYOUT_HCENTER
```
- `LAYOUT_TOP`|`LAYOUT_BOTTOM`
- `LAYOUT_TOP`|`LAYOUT_VCENTER`
- `LAYOUT_BOTTOM`|`LAYOUT_VCENTER`

**Since:**
- qtp 1.0

## 필드 요약

- `protected  int bg` — 배경색.
- `protected EventListener evtListener`
- `protected Object evtListenerObj`
- `protected  int fg` — 전경색 기본값은 각 컴포넌트에 따라 다르게 지정됩니다.
- `static int FOCUS_NOTIFY` — 포커스가 왔음을 알리는 상수. 1로 지정되어 있습니다.
- `protected  int h` — 컴포넌트의 높이의 픽셀 크기.
- `protected static int HAS_FOCUS_MASK`
- `protected static int INPUT_MASK`
- `static int KEY_NOTIFY` — 키 관련 이벤트가 생성됨을 알리는 상수. 3로 지정되어 있습니다.
- `static int KEY_PRESSED` — 키가 눌렸을 때 이벤트 타입.
- `static int KEY_RELEASED` — 키가 떼어졌을 때 이벤트 타입.
- `static int KEY_REPEATED` — 키가 반복해서 눌렸을 때 이벤트 타입.
- `static int KEY_TYPED` — 키가 눌렸을때 이벤트 타입.
- `static int LAYOUT_BOTTOM` — Component 의 아래쪽 정렬값.
- `static int LAYOUT_HCENTER` — Component 의 가운데 수평 정렬 값.
- `static int LAYOUT_LEFT` — Component 의 좌측 정렬 값.
- `static int LAYOUT_RIGHT` — Component 의 우측 정렬 값.
- `static int LAYOUT_TOP` — Component 의 위쪽 정렬값.
- `static int LAYOUT_VCENTER` — Component 의 가운데 수직 정렬 값.
- `protected  int mask`
- `protected ContainerComponent parent` — 상위 부모 컴포넌트.
- `static int POINT_DRAGGED` — 포인터 기기가 눌린 상태에서 움직였을때 이벤트 타입.
- `static int POINT_PRESSED` — 포인터 기기가 눌렸을 때 이벤트 타입.
- `static int POINT_RELEASED` — 포인터 기기가 떼어졌을 때 이벤트 타입.
- `static int POINTER_NOTIFY` — 포인터 관련 이벤트가 생성됨을 알리는 상수. 4로 지정되어 있습니다.
- `static int POS_MASK` — 위치 이동이 됨을 알리는 상수.
- `protected static int PREFER_SIZE_MASK`
- `protected  int prefH`
- `protected  int prefW`
- `static int SHOW_NOTIFY` — 보여지거나 가려짐을 알리는 상수. 2로 지정되어 있습니다.
- `static int SIZE_MASK` — 크기 변경이 됨을 알리는 상수.
- `protected static int VALID_MASK`
- `protected  int w` — 컴포넌트의 폭의 픽셀 크기.
- `protected  int x` — 상위 부모 Component로 부터의 x축 픽셀 위치.
- `protected  int y` — 상위 부모 Component로 부터의 y축 픽셀 위치.

## 생성자 요약

- `protected Component ()`

## 메서드 요약

- `protected  void calcPreferredSize (int w)` — 컴포넌트의 적절한 크기를 계산합니다.
- `boolean canHandleInput ()` — 컴포넌트가 입력을 받을 수 있는 여부를 돌려줍니다.
- `void configure (int x, int y, int w, int h, int mask)` — 컴포넌트의 위치나 크기를 변경합니다.
- `void focusNotify (boolean b)` — 포커스를 받으면 호출됩니다.
- `int getBackground ()` — 배경색을 돌려 줍니다.
- `Card getCard ()` — 현재 컴포넌트에 연결된 카드를 돌려줍니다.
- `int getForeground ()` — 전경생을 돌려줍니다.
- `int getHeight ()` — 컴포넌트의 높이를 돌려 줍니다.
- `int getPreferredHeight ()` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredHeight (int w)` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredWidth ()` — 컴포넌트의 적절한 폭을 결정합니다.
- `int getWidth ()` — 컴포넌트의 폭을 돌려 줍니다.
- `int getX ()` — x축의 좌표를 돌려줍니다.
- `int getXOnScreen ()` — 화면상에 대응되는 실제 좌표를 구합니다.
- `int getY ()` — y축의 좌표를 돌려줍니다.
- `int getYOnScreen ()` — 화면상에 대응되는 실제 좌표를 구합니다.
- `boolean hasFocus ()` — 컴포넌트가 입력 포커스를 가지고 있는지의 여부를 돌려줍니다.
- `void invalidate ()` — 컴포넌트가 유효한 좌표와 크기를 가지 않음을 알려줍니다.
- `boolean isShown ()` — 현재 컴포넌트가 보이는지 안보이는지 여부를 돌려줍니다.
- `protected  boolean isValid ()` — 컴포넌트가 유효한 좌표와 크기를 가지는지 여부를 돌려줍니다.
