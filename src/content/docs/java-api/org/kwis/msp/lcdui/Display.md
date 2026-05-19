---
title: "Class Display"
---

`package org.kwis.msp.lcdui`

```text
java.lang.Object
  |
  +--org.kwis.msp.lcdui.Display
```

## 설명

**extends Object:**

화면의 출력 관련 함수와 정보를 가지는 클래스입니다.
 
 기본적으로 화면에 무언가를 출력하기 위해서 `Display`를 구한후에 
 `Card`를 생성하고, 
 `pushCard`함수를 호출하여 `Display`에 
 `Card`를 등록 시킵니다.
 이후에 `Card`의 `paint`함수에서 
 그려지는 내용이 화면에 출력됩니다.

한 화면(LCD)은 `Display`에 대응합니다.
 응용프로그램은 `Display`을 여러개 가질 수 있습니다. 
 이는 휴대폰중에 듀얼 LCD가 있는 모델을 지원하기 위하여
 JLet상에서 두 화면을 사용할 수도록 
 하기 위함입니다.
 `Display`를 얻어 오기 위해서는 ``getDisplay(java.lang.String)``함수를 사용하여 
 가져옵니다.

한 화면을 여러개의 `Card`로 구성됩니다. 
 `Card`는 맨 아래 `Card`부터 시작해서
 하나씩 그려지며, 맨 마지막에는 스택 맨 상위에 있는 `Card`가 
 그려집니다.
 이런 메커니즘으로 대화 상자등을 처리할 수 있도록 하였습니다.

입력은 반대 방향으로 맨 상위에 있는 `Card`에게 
 전달되며 이 `Card`는 자신이 
 이벤트를 처리했는지 않했는지 여부를 돌려줍니다. 만일 처리했다면, 더이상 
 이벤트는 하위 `Card`에게 전달되지 않지만, 처리하지 
 않았다면 하위 `Card`에게
 전달되며, 다시한번 처리여부를 확인하게 되어 맨 아래 `Card`까지 
 전달 될 
 수도 있습니다. 실제로 `InputMethodHandler`에 의해서 
 생성되는 창이나 기타 대화 상자등은
 이런 식으로 처리가 됩니다.

듀얼 LCD에 대응하는 `Display`에서는 사용자 
 입력 이벤트(키 이벤트, 포인터 이벤트)가 발생하지
 않음을 유의하십시오.

**See Also:**
- ``Card``

## 메서드 요약

- `void addJletEventListener ( JletEventListener qel)` — JletEvent 를 받을 리스너를 등록합니다. key, repaint, point외에 발생하는 모든 이벤트가 발생시에 호출되는 리스너를 등록합니다.
- `void callSerially ( Runnable r)` — 이벤트가 다 처리되고 난 후에 특정 Runnable 의 함수 run 을 호출하도록 합니다.
- `void callSerially ( Runnable r, int timeout)` — 이벤트가 다 처리되고 난 후에 특정 Runnable 의 함수 run 을 호출하도록 합니다.
- `int countCard ()` — Display에 등록된 카드의 갯수를 가져옵니다.
- `void flush ()` — 내부의 버퍼의 내용을 화면에 출력하도록 합니다.
- `int getBitsPerPixel ()` — 화면의 한 픽셀당 차지하는 비트(bit)를 돌려줍니다.
- `static Display getDefaultDisplay ()` — 기본 Display 를 얻어 옵니다.
- `static Display getDisplay ( String str)` — 문자열에 대응하는 Display 를 얻어 옵니다.
- `Card getDockedCard ()` — 붙여진 카드를 돌려줍니다.
- `static int getGameAction (int key)` — 지정한 키 코드에 대응하는 게임키를 구합니다.
- `int getHeight ()` — 화면의 높이를 돌려줍니다.
- `static int getKeyCode (int gameKey)` — 게임키에 대응하는 키 코드값을 얻어 옵니다. gameKey는 EventQueue.UP, EventQueue.DOWN, EventQueue.LEFT, EventQueue.RIGHT, EventQueue.FIRE, EventQueue.GAME_A, EventQueue.GAME_B, EventQueue.GAME_C, EventQueue.GAME_D, ```java 중 하나가 되며, 돌려주는 값은 실제적인 키 코드 값이 됩니다. ```
- `static String getKeyName (int key)` — 키 코드에 대응하는 키 이름의 문자열을 돌려 받습니다.
- `int getWidth ()` — 화면의 폭을 돌려줍니다.
- `void grabKey (int key, JletEventListener qel)` — 특정 키를 함수를 부르는 응용 프로그램에서 소유하게 합니다.
- `boolean hasPointerEvents ()` — 시스템에 포인터 디바이스관련 이벤트가 있는지 여부를 돌려줍니다.
- `boolean hasPointerMotionEvents ()` — 시스템에 포인터 움직임 디바이스 이벤트가 있는지 여부를 돌려줍니다.
- `boolean hasRepeatEvents ()` — 키 반복 이벤트가 발생할 수 있는지 없는지 여부를 돌려줍니다.
- `boolean isColor ()` — 화면이 컬러 색상을 지원하는지 여부를 돌려줍니다.
- `boolean isDoubleBuffered ()` — 화면이 더블 버퍼링(double buffering)인지 여부를 돌려줍니다.
- `int numColors ()` — 화면에서 사용할 수 있는 색상의 갯수를 돌려줍니다.
- `Card popCard ()` — 카드를 꺼내옵니다.
- `void pushCard ( Card c)` — 카드를 화면에 보일 수 있도록 합니다.
- `void removeAllCards ()` — 모든 카드를 제거합니다.
- `boolean removeCard ( Card c)` — 특정 카드를 제거합니다.
- `void removeJletEventListener ( JletEventListener qel)` — JletEvent 를 받을 리스너를 삭제합니다.
- `void setDockedCard ( Card cd, int where)`
- `void setJletEventListener ( JletEventListener qel)`
- `void ungrabKey (int key)` — grabKey 로 인한 이벤트 소유를 이전 상태로 돌립니다.
- `static void where ()`

## 메서드 상세

### getDefaultDisplay

```java
public static Display getDefaultDisplay()
```

**Returns:**
- 기본 display

**Throws:**
- `NullPointerException` - ql이 null인 경우

### getDisplay

```java
public static final Display getDisplay(String str)
```

**Parameters:**
- `str` - display를 가르키는 문자열

**Returns:**
- display 객체

**Throws:**
- `NullPointerException` - ql이 null인 경우

### pushCard

```java
public final void pushCard(Card c)
```

**Parameters:**
- `c` - 화면에 맨 상위에 보여질 카드.

**Throws:**
- `NullPointerException` - c가 null인 경우

### popCard

```java
public final Card popCard()
```

**Returns:**
- 꺼내온 카드

### removeCard

```java
public final boolean removeCard(Card c)
```

**Parameters:**
- `c` - 삭제할 카드

**Returns:**
- 성공적으로 스택에 카드를 제거했는지 여부

### removeAllCards

```java
public void removeAllCards()
```

- 모든 카드를 제거합니다.

 현재 수행중인 `Jlet`이 생성한 
 모든 카드를 `Display`
 에서 제거합니다.
 각 카드의 `showNotify()`가 각각 불리며,
 더 이상 카드는 화면에 나타나지 않습니다.

### countCard

```java
public final int countCard()
```

**Returns:**
- 카드 스택에 있는 카드의 갯수

### callSerially

```java
public final void callSerially(Runnable r)
```

**Parameters:**
- `r` - 수행할 runnable 객체

**Throws:**
- `NullPointerException` - `r`이 `null`인 경우

### callSerially

```java
public final void callSerially(Runnable r,
                               int timeout)
```

**Parameters:**
- `timeout` - Runnable이 불려질 시간(밀리 세컨드 단위)

**Throws:**
- `IllegalArgumentException` - `timeout이 음수인 경우`

### getDockedCard

```java
public Card getDockedCard()
```

- 붙여진 카드를 돌려줍니다.

### setDockedCard

```java
public void setDockedCard(Card cd,
                          int where)
```

### isColor

```java
public final boolean isColor()
```

**Returns:**
- 컬러 지원 여부

### numColors

```java
public final int numColors()
```

**Returns:**
- 색상 갯수

### hasPointerEvents

```java
public final boolean hasPointerEvents()
```

**Returns:**
- 포인터 이벤트 여부

### hasPointerMotionEvents

```java
public final boolean hasPointerMotionEvents()
```

**Returns:**
- 포인터 움직임 이벤트 여부

### hasRepeatEvents

```java
public final boolean hasRepeatEvents()
```

**Returns:**
- 키 반복 이벤트 여부

### getWidth

```java
public final int getWidth()
```

**Returns:**
- 화면의 폭

### getHeight

```java
public final int getHeight()
```

**Returns:**
- 화면의 높이

### isDoubleBuffered

```java
public boolean isDoubleBuffered()
```

**Returns:**
- double buffer 여부

### getKeyCode

```java
public static int getKeyCode(int gameKey)
```

- 게임키에 대응하는 키 코드값을 얻어 옵니다. 
 gameKey는 

```java
EventQueue.UP, EventQueue.DOWN, EventQueue.LEFT, 
 EventQueu
```
