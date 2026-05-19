---
title: "Class Display"
---

`package javax.microedition.lcdui`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.Display
```

## 설명

**extends Object:**

`Display`는 시스템의 입력 장치 및 
디스플레이 관리자를 나타냅니다. 
여기에는 장치의 등록 정보를 검색하고 장치에 해당 객체를 표시할 것을 
요청하는 메소드가 포함됩니다. 장치 속성을 다루는 다른 메소드는 
주로 ``Canvas`` 객체와 함께 사용되므로 여기가 아닌 
그 쪽에서 정의됩니다.

``MIDlet``마다 
정확히 한 개의 Display 인스턴스가 있으며 응용 프로그램은 
``getDisplay()`` 
메소드를 호출하여 해당 인스턴스에 대한 
참조를 가져올 수 있습니다. 
응용 프로그램은 실행 중에 언제든지 `getDisplay()` 
메소드를 호출할 수 있습니다. 
`getDisplay()`에 대한 모든 호출로 반환되는 
`Display` 객체는 이 기간 동안 
동일한 상태로 있게 됩니다.

일반 응용 프로그램은 해당 `MIDlet` 메소드 호출에 대한 
응답으로 다음 작업을 수행합니다.

- **startApp** - 응용 프로그램이 
일시 중지 상태에서 활성 상태로 이동합니다. 
응용 프로그램이 활성화되는 동안 
필요한 객체를 초기화해야 합니다. 
초기화가 이루어지지 않은 경우 응용 프로그램은 
첫 화면에서 ``setCurrent()``를 
호출할 수 있습니다. 
그 사이에 `pauseApp()`가 호출되는 경우 
`startApp()`를 
여러 번 호출할 수 있습니다. 
이는 일회성 초기화가 발생해서는 안 되며 대신 
`MIDlet` 
구성자 내에서 발생해야 한다는 것을 의미합니다.
- **pauseApp** - 응용 프로그램이 자신의 스레드를 
일시 중지합니다. 또한 응용 프로그램이 
다시 활성화될 때 다른 화면에서 시작하려는 경우에는 
`setCurrent()`를 사용하여 새 화면을 설정합니다.
- **destroyApp** - 응용 프로그램에서 자원을 
사용 가능하게 만들고 스레드를 종료합니다. `destroyApp()`가 
반환된 후 사용자 인터페이스 객체에 있는 메소드 호출에 대한 
동작은 정의되지 않습니다.

디스플레이 장치에 표시된 사용자 인터페이스 객체는 
``Displayable`` 객체 내에 포함됩니다. 
응용 프로그램은 언제든 
디스플레이 장치에 표시되어 이를 통해 
사용자 상호 작용이 가능한 `Displayable` 객체를 하나 정도 
가질 수 있습니다. 이 `Displayable`을 *현재*
`Displayable`이라고 합니다.

`Display` 클래스에는 
현재 `Displayable`을 설정하는 
``setCurrent()`` 메소드가 있으며 
현재 `Displayable`을 검색하는 
``getCurrent()`` 메소드가 있습니다. 
응용 프로그램은 현재 `Displayable`을 제어하며 
언제든지 `setCurrent()`를 
호출할 수 있습니다. 
일반적으로 응용 프로그램은 
일부 사용자 작업에 대한 응답으로 
현재 `Displayable`을 변경합니다. 
하지만 항상 그런 것은 아닙니다. 
다른 스레드가 다른 자극에 대한 응답으로 현재 
`Displayable`을 변경할 수 있습니다. 
``Alert`` 타이머의 
시간이 경과하면 현재 
`Displayable`도 변경됩니다.

응용 프로그램의 현재 `Displayable`은 
실제로 화면에 나타나지 않을 수 있으며 발생하는 사용자 
이벤트(예: 키 입력)가 반드시 현재 `Displayable`로 
지정되지 않을 수도 있습니다. 
이는 같은 장치에서 동시에 
다른 `MIDlet` 응용 프로그램이 
실행되기 때문에 발생합니다.

현재 `Displayable`이 디스플레이 장치에 
실제로 표시되고 사용자 입력 장치 이벤트가 이 장치에 전달되는 경우 
응용 프로그램이 *포그라운드*에 있다고 말할 수 있습니다. 
응용 프로그램이 포그라운드에 있지 않은 경우에는 
디스플레이 장치와 입력 장치 모두에 액세스하기 어려우며 
이 경우 *백그라운드*에 있다고 말할 수 있습니다. 
이러한 장치를 다른 `MIDlet` 응용 프로그램에 
할당하는 정책은 이 사양의 범위를 벗어나며 *응용 프로그램 
관리 소프트웨어*라는 외부 에이전트의 
제어를 받습니다.

위에 언급된 대로 응용 프로그램이 백그라운드에 있더라도 
현재 `Displayable`의 개념은 여전히 가집니다. 
현재 `Displayable`은 다음에 응용 프로그램을 
포그라운드로 가져올 때 표시할 내용이므로 
백그라운드 응용 
프로그램인 경우에도 현재 
`Displayable`은 중요합니다. 
응용 프로그램은 ``isShown()``을 
호출하여 `Displayable`을 디스플레이에서 
실제로 표시할지 결정할 수 있습니다. 
`Canvas`의 경우 
`Canvas`를 표시하고 
숨길 때 각각 ``showNotify()``와 
``hideNotify()`` 메소드가 
호출됩니다.

각 `MIDlet` 응용 프로그램은 고유한 
현재 `Displayable`을 가집니다. 
이는 `MIDlet`의 포그라운드/백그라운드 상태에 
상관없이 ``getCurrent()`` 메소드가 
`MIDlet`의 현재 `Displayable`을 반환한다는 것을 
의미합니다. 
예를 들어, 포그라운드에서 실행되는 `MIDlet`에 
현재 `Displayable` *F*가 있고, 
백그라운드에서 실행되는 `MIDlet`에 현재 
`Displayable` *B*가 있다고 가정하는 경우, 
포그라운드 `MIDlet`에서 `getCurrent()`를 
호출하면 *F*를 반환하며 백그라운드 `MIDlet`에서 
`getCurrent()`를 호출하면 *B*를 반환합니다. 
그리고 `MIDlet`에서 
`setCurrent()`를 호출하여 
현재 `Displayable`을 변경하는 경우 
다른 `MIDlet`의 현재 
`Displayable`에 
아무런 영향을 미치지 않습니다.

`getCurrent()`에서 `null`을 
반환할 가능성이 있습니다. `MIDlet` 응용 프로그램이 
첫 화면에서 `setCurrent()`를 호출하기 전에 시작하면 
이러한 일이 발생할 수 있습니다. 
`getCurrent(`) 메소드는 
이전에 이 `MIDlet`에서 
`setCurrent()`를 
호출할 때 전달되지 않은 `Displayable` 객체에 대한 
참조는 절대 반환하지 않습니다.

### 시스템 화면

일반적으로 포그라운드 `MIDlet`의 현재 화면은 
디스플레이에 표시됩니다. 
하지만 특정 상황에서 시스템은 응용 프로그램의 
현재 화면을 일시적으로 흐리게 하는 화면을 만들 수 있습니다. 
이러한 화면을 *시스템 화면*이라고 합니다. 
이는 시스템이 명령 메뉴를 표시해야 하거나 시스템이
`Form` 내의 텍스트 필드 안이 아닌 
별도의 화면에서 텍스트를 편집하도록 사용자에게 요구하는 경우에 
발생합니다. 시스템 화면이 응용 프로그램 화면을 흐리게 하더라도 
현재 화면의 개념은 변경되지 않습니다. 
특히 시스템 화면이 표시되는 동안 
`getCurrent()`에 대한 
호출은 시스템 화면이 아닌 응용 
프로그램의 현재 화면을 반환합니다. 
시스템 화면으로 현재 `Displayable`이 희미해진 경우 
`isShown()`이 반환하는 값은 
`false`입니다.

시스템 화면이 캔버스를 흐리게 하면 `hideNotify()` 
메소드가 호출됩니다. 
시스템 화면이 제거되면 
캔버스가 복구되면서 해당 `showNotify()` 메소드와 
`paint()` 메소드가 호출됩니다. 
명령을 실행할 사용자가 시스템 화면을 사용하는 경우 
`showNotify()`가 호출된 다음 
`commandAction()` 
메소드가 호출됩니다.

이 클래스는 높은 수준 사용자 인터페이스의 일반적인 전경색 
및 배경색을 검색하는 메소드를 포함합니다. 
이러한 메소드는 다른 항목의 사용자 인터페이스와 일치하는 
`CustomItem` 객체를 만들고 시스템 나머지 부분의 
사용자 인터페이스와 일치하는 `Canvas` 내에서 
사용자 인터페이스를 만들 때 유용합니다. 
구현 시 사용자 인터페이스에서 전경색 및 배경색만 사용하도록 
제한하지는 않지만(예: 비스듬하게 보이도록 강조 표시 및 그림자 색 사용) 
반환되는 색은 해당 구현의 색 구성표와 상당히 일치하는 색입니다. 
사용자 정의 항목을 구현하는 응용 프로그램은 배경색을 사용하여 
해당 영역을 지운 다음 텍스트 및 기하 그래픽(선, 호, 직사각형)을 
전경색으로 칠합니다.

**Since:**
- MIDP 1.0

## 필드 요약

- `static int ALERT` — Alert 이미지의 이미지 유형.
- `static int CHOICE_GROUP_ELEMENT` — ChoiceGroup 요소 이미지의 이미지 유형.
- `static int COLOR_BACKGROUND` — getColor 에서 사용할 색 지정자.
- `static int COLOR_BORDER` — getColor 에서 사용할 색 지정자.
- `static int COLOR_FOREGROUND` — getColor 에서 사용할 색 지정자.
- `static int COLOR_HIGHLIGHTED_BACKGROUND` — getColor 에서 사용할 색 지정자.
- `static int COLOR_HIGHLIGHTED_BORDER` — getColor 에서 사용할 색 지정자.
- `static int COLOR_HIGHLIGHTED_FOREGROUND` — getColor 에서 사용할 색 지정자.
- `static int LIST_ELEMENT` — List 요소 이미지의 이미지 유형.

## 메서드 요약

- `void callSerially ( Runnable r)` — Runnable 객체 r 이 해당 run() 메소드를 나중에 호출하여 다시 그리기 주기가 완료된 직후 해당 이벤트 스트림과 일련화되도록 합니다.
- `boolean flashBacklight (int duration)` — 장치의 후광으로 깜박임 효과를 요청합니다.
- `int getBestImageHeight (int imageType)` — 지정된 이미지 유형에 최적인 이미지 높이를 반환합니다.
- `int getBestImageWidth (int imageType)` — 지정된 이미지 유형에 최적인 이미지 너비를 반환합니다.
- `int getBorderStyle (boolean highlighted)` — 구성 요소의 상태(강조 표시된/강조 표시되지 않은)에 따라 경계선 그리기에 사용된 입력 스타일을 반환합니다.
- `int getColor (int colorSpecifier)` — 전달된 colorSpecifier 를 기반으로 한 0x00RRGGBB 형식으로 높은 수준의 사용자 인터페이스 색 구성표에서 색 하나를 반환합니다.
- `Displayable getCurrent ()` — 이 MIDlet 의 현재 Displayable 객체를 가져옵니다.
- `static Display getDisplay ( MIDlet m)` — 이 MIDlet 에 고유한 Display 객체를 가져옵니다.
- `boolean isColor ()` — 장치의 색 지원에 대한 정보를 가져옵니다.
- `int numAlphaLevels ()` — 이 구현에서 지원하는 알파 투명도 수준의 수를 가져옵니다.
- `int numColors ()` — 장치에서 표현할 수 있는 색의 수( isColor() 가 true 인 경우) 또는 회색 수준( isColor() 가 false 인 경우)을 가져옵니다.
- `void setCurrent ( Alert alert, Displayable nextDisplayable)` — 이 Alert 를 현재로 만들고, Alert 가 닫힌 후에는 nextDisplayable 을 현재로 만들 것을 요청합니다.
- `void setCurrent ( Displayable nextDisplayable)` — 다양한 Displayable 객체를 디스플레이에 표시하도록 요청합니다.
- `void setCurrentItem ( Item item)` — 이 Item 을 포함하는 Displayable 이 현재가 되고 Displayable 을 스크롤하여 Item 을 표시하고 여기에 해당 초점을 할당하도록 요청합니다.
- `boolean vibrate (int duration)` — 장치의 바이브레이터 작업을 요청합니다.

## 필드 상세

### LIST_ELEMENT

```java
public static final int LIST_ELEMENT
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getBestImageWidth(int imageType)``, 
``getBestImageHeight(int imageType)``, 
`Constant Field Values`

### CHOICE_GROUP_ELEMENT

```java
public static final int CHOICE_GROUP_ELEMENT
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getBestImageWidth(int imageType)``, 
``getBestImageHeight(int imageType)``, 
`Constant Field Values`

### ALERT

```java
public static final int ALERT
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getBestImageWidth(int imageType)``, 
``getBestImageHeight(int imageType)``, 
`Constant Field Values`

### COLOR_BACKGROUND

```java
public static final int COLOR_BACKGROUND
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getColor(int)``, 
`Constant Field Values`

### COLOR_FOREGROUND

```java
public static final int COLOR_FOREGROUND
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getColor(int)``, 
`Constant Field Values`

### COLOR_HIGHLIGHTED_BACKGROUND

```java
public static final int COLOR_HIGHLIGHTED_BACKGROUND
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getColor(int)``, 
`Constant Field Values`

### COLOR_HIGHLIGHTED_FOREGROUND

```java
public static final int COLOR_HIGHLIGHTED_FOREGROUND
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getColor(int)``, 
`Constant Field Values`

### COLOR_BORDER

```java
public static final int COLOR_BORDER
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getColor(int)``, 
`Constant Field Values`

### COLOR_HIGHLIGHTED_BORDER

```java
public static final int COLOR_HIGHLIGHTED_BORDER
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getColor(int)``, 
`Constant Field Values`

### getDisplay

```java
public static Display getDisplay(MIDlet m)
```

**Parameters:**
- `m` - 응용 프로그램의 `MIDlet`

**Returns:**
- 응용 프로그램이 사용자 인터페이스에 사용할 수 있는 
디스플레이 객체

**Throws:**
- `NullPointerException` - `m`이 `null`인 경우

### getColor

```java
public int getColor(int colorSpecifier)
```

**Parameters:**
- `colorSpecifier` - 미리 
정의된 색 지정자. 
``COLOR_BACKGROUND``, 
``COLOR_FOREGROUND``, 
``COLOR_HIGHLIGHTED_BACKGROUND``, 
``COLOR_HIGHLIGHTED_FOREGROUND``, 
``COLOR_BORDER``, 
``COLOR_HIGHLIGHTED_BORDER`` 중 하나여야 합니다.

**Returns:**
- `0x00RRGGBB` 형식의 색

**Throws:**
- `IllegalArgumentException` - `colorSpecifier`가 
유효한 색 지정자가 아닌 경우

**Since:**
- MIDP 2.0

### getBorderStyle

```java
public int getBorderStyle(boolean highlighted)
```

**Parameters:**
- `highlighted` - 요청된 경계선 스타일이 
강조 표시된 상태용이면 `true`, 
요청된 경계선 스타일이 
강조 표시되지 않은 상태용이면 
`false`

**Returns:**
- ``Graphics.DOTTED`` 또는 ``Graphics.SOLID``

**Since:**
- MIDP 2.0

### isColor

```java
public boolean isColor()
```

**Returns:**
- 디스플레이에서 색을 지원하면 `true`, 
그렇지 않으면 `false`

### numColors

```java
public int numColors()
```

**Returns:**
- 색의 수

### numAlphaLevels

```java
public int numAlphaLevels()
```

**Returns:**
- 지원되는 알파 수준 수

**Since:**
- MIDP 2.0

### getCurrent

```java
public Displayable getCurrent()
```

**Returns:**
- `MIDlet`의 현재 `Displayable` 객체

**See Also:**
- ``setCurrent(javax.microedition.lcdui.Displayable)``

### setCurrent

```java
public void setCurrent(Displayable nextDisplayable)
```

**Parameters:**
- `nextDisplayable` - 현재로 만들기 위해 
요청된 `Displayable`로 
`null`이 허용됩니다.

**See Also:**
- ``getCurrent()``

### setCurrent

```java
public void setCurrent(Alert alert,
                       Displayable nextDisplayable)
```

**Parameters:**
- `nextDisplayable` - 이 경고가 닫힌 다음 표시될 
`Displayable`

**Throws:**
- `IllegalArgumentException` - `nextDisplayable`이 
`Alert`인 경우

**See Also:**
- ``Alert``, 
``getCurrent()``

### setCurrentItem

```java
public void setCurrentItem(Item item)
```

**Parameters:**
- `item` - 표시되어야 하는 항목

**Throws:**
- `NullPointerException` - `item`이 `null`인 경우

**Since:**
- MIDP 2.0

### callSerially

```java
public void callSerially(Runnable r)
```

**Parameters:**
- `r` - 호출되는 `Runnable` 인터페이스의 인스턴스

### flashBacklight

```java
public boolean flashBacklight(int duration)
```

**Parameters:**
- `duration` - 후광이 깜박여야 할 시간(밀리초), 
또는 깜박임이 중지되어야 하는 경우 0

**Returns:**
- 응용 프로그램에서 후광을 제어할 수 있고 
이 디스플레이가 포그라운드에 있는 경우 `true`, 
그렇지 않은 경우 `false`

**Throws:**
- `IllegalArgumentException` - `duration`이 음수인 경우

**Since:**
- MIDP 2.0

### vibrate

```java
public boolean vibrate(int duration)
```

**Parameters:**
- `duration` - 바이브레이터를 실행해야 하는 시간(밀리초), 
또는 바이브레이터를 해제해야 하는 경우 0

**Returns:**
- 응용 프로그램에서 바이브레이터를 제어할 수 있고 
이 디스플레이가 포그라운드에 있는 경우 `true`, 
그렇지 않은 경우 `false`

**Throws:**
- `IllegalArgumentException` - `duration`이 음수인 경우

**Since:**
- MIDP 2.0

### getBestImageWidth

```java
public int getBestImageWidth(int imageType)
```

**Parameters:**
- `imageType` - 이미지 유형

**Returns:**
- 이미지 유형에 최적인 이미지 너비로 최적의 크기가 
없는 경우 0일 수 있으며 음수가 아니어야 합니다.

**Throws:**
- `IllegalArgumentException` - `imageType`이 유효하지 않은 경우

**Since:**
- MIDP 2.0

### getBestImageHeight

```java
public int getBestImageHeight(int imageType)
```

**Parameters:**
- `imageType` - 이미지 유형

**Returns:**
- 이미지 유형에 최적인 이미지 높이로 최적의 크기가 
없는 경우 0일 수 있으며 음수가 아니어야 합니다.

**Throws:**
- `IllegalArgumentException` - `imageType`이 유효하지 않은 경우

**Since:**
- MIDP 2.0

## 메서드 상세

### getDisplay

```java
public static Display getDisplay(MIDlet m)
```

**Parameters:**
- `m` - 응용 프로그램의 `MIDlet`

**Returns:**
- 응용 프로그램이 사용자 인터페이스에 사용할 수 있는 
디스플레이 객체

**Throws:**
- `NullPointerException` - `m`이 `null`인 경우

### getColor

```java
public int getColor(int colorSpecifier)
```

**Parameters:**
- `colorSpecifier` - 미리 
정의된 색 지정자. 
``COLOR_BACKGROUND``, 
``COLOR_FOREGROUND``, 
``COLOR_HIGHLIGHTED_BACKGROUND``, 
``COLOR_HIGHLIGHTED_FOREGROUND``, 
``COLOR_BORDER``, 
``COLOR_HIGHLIGHTED_BORDER`` 중 하나여야 합니다.

**Returns:**
- `0x00RRGGBB` 형식의 색

**Throws:**
- `IllegalArgumentException` - `colorSpecifier`가 
유효한 색 지정자가 아닌 경우

**Since:**
- MIDP 2.0

### getBorderStyle

```java
public int getBorderStyle(boolean highlighted)
```

**Parameters:**
- `highlighted` - 요청된 경계선 스타일이 
강조 표시된 상태용이면 `true`, 
요청된 경계선 스타일이 
강조 표시되지 않은 상태용이면 
`false`

**Returns:**
- ``Graphics.DOTTED`` 또는 ``Graphics.SOLID``

**Since:**
- MIDP 2.0

### isColor

```java
public boolean isColor()
```

**Returns:**
- 디스플레이에서 색을 지원하면 `true`, 
그렇지 않으면 `false`

### numColors

```java
public int numColors()
```

**Returns:**
- 색의 수

### numAlphaLevels

```java
public int numAlphaLevels()
```

**Returns:**
- 지원되는 알파 수준 수

**Since:**
- MIDP 2.0

### getCurrent

```java
public Displayable getCurrent()
```

**Returns:**
- `MIDlet`의 현재 `Displayable` 객체

**See Also:**
- ``setCurrent(javax.microedition.lcdui.Displayable)``

### setCurrent

```java
public void setCurrent(Displayable nextDisplayable)
```

**Parameters:**
- `nextDisplayable` - 현재로 만들기 위해 
요청된 `Displayable`로 
`null`이 허용됩니다.

**See Also:**
- ``getCurrent()``

### setCurrent

```java
public void setCurrent(Alert alert,
                       Displayable nextDisplayable)
```

**Parameters:**
- `nextDisplayable` - 이 경고가 닫힌 다음 표시될 
`Displayable`

**Throws:**
- `IllegalArgumentException` - `nextDisplayable`이 
`Alert`인 경우

**See Also:**
- ``Alert``, 
``getCurrent()``

### setCurrentItem

```java
public void setCurrentItem(Item item)
```

**Parameters:**
- `item` - 표시되어야 하는 항목

**Throws:**
- `NullPointerException` - `item`이 `null`인 경우

**Since:**
- MIDP 2.0

### callSerially

```java
public void callSerially(Runnable r)
```

**Parameters:**
- `r` - 호출되는 `Runnable` 인터페이스의 인스턴스

### flashBacklight

```java
public boolean flashBacklight(int duration)
```

**Parameters:**
- `duration` - 후광이 깜박여야 할 시간(밀리초), 
또는 깜박임이 중지되어야 하는 경우 0

**Returns:**
- 응용 프로그램에서 후광을 제어할 수 있고 
이 디스플레이가 포그라운드에 있는 경우 `true`, 
그렇지 않은 경우 `false`

**Throws:**
- `IllegalArgumentException` - `duration`이 음수인 경우

**Since:**
- MIDP 2.0

### vibrate

```java
public boolean vibrate(int duration)
```

**Parameters:**
- `duration` - 바이브레이터를 실행해야 하는 시간(밀리초), 
또는 바이브레이터를 해제해야 하는 경우 0

**Returns:**
- 응용 프로그램에서 바이브레이터를 제어할 수 있고 
이 디스플레이가 포그라운드에 있는 경우 `true`, 
그렇지 않은 경우 `false`

**Throws:**
- `IllegalArgumentException` - `duration`이 음수인 경우

**Since:**
- MIDP 2.0

### getBestImageWidth

```java
public int getBestImageWidth(int imageType)
```

**Parameters:**
- `imageType` - 이미지 유형

**Returns:**
- 이미지 유형에 최적인 이미지 너비로 최적의 크기가 
없는 경우 0일 수 있으며 음수가 아니어야 합니다.

**Throws:**
- `IllegalArgumentException` - `imageType`이 유효하지 않은 경우

**Since:**
- MIDP 2.0

### getBestImageHeight

```java
public int getBestImageHeight(int imageType)
```

**Parameters:**
- `imageType` - 이미지 유형

**Returns:**
- 이미지 유형에 최적인 이미지 높이로 최적의 크기가 
없는 경우 0일 수 있으며 음수가 아니어야 합니다.

**Throws:**
- `IllegalArgumentException` - `imageType`이 유효하지 않은 경우

**Since:**
- MIDP 2.0
