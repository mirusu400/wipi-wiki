---
title: "3.1.1. 그래픽"
---

Interface ImageObserver public interface ImageObserver 이미지의 생성 상태를 볼 수 있도록 해주는 인터페이스이다. 이미지가 생성될 때 각 이미지 프레임마다 생성된 여부를 알려줄 때 사용되는 인터페이스이다. 필드 상세 설명

#### FRAME_END

public static final int FRAME_END 이미지 프레임 하나가 디코딩에 성공하였음을 알리는 상수.

#### IMAGE_END

public static final int IMAGE_END 이미지 전체가 디코딩에 성공하거나, 이미지의 애니메이션이 끝났음을 알리는 상수.

#### NOT_EXIST

public static final int NOT_EXIST 지정된 리소스가 존재하지 않아 이미지를 읽어 들일 수 없음을 알리는 상수.

#### DECODE_ERROR

public static final int DECODE_ERROR 데이터가 잘못 들어 있어 디코딩에 실패함을 알리는 상수.

#### OUT_OF_MEMORY

public static final int OUT_OF_MEMORY 메쏘드 상세 설명

#### notify

public void notify(Image img, int status) 이미지 한 프레임이 완성되었음을 알린다. 디코딩 결과를 status로 알려준다. status 값 은 한 프레임이 끝난 경우 FRAME_END이 되고, 이미지 전체 디코딩이 끝났다면, IMAGE_END이 된다. 만일 디코딩 결과가 오류인 경우에는 status가 NOT_EXIST나 DECODE_ERROR OUT_OF_MEMORY이 된다.

**참고 항목**

Image.loadImage(java.lang.String,org.kwis.msp.lcdui.ImageObserver) Image.play(org.kwis.msp.lcdui.ImageObserver) Interface InputMethodListener public interface InputMethodListener InputMethodHandler에서 사용자 키 입력에 대해 처리된 문자와 입력 상태- 삽입/삭제/수정-를 감지하기 위한 인터페이스이다. InputMethodListener를 상속하여 구현한 클래스는 inputMethodHandler의 InputMethodHandler.setInputMethodListener(org.kwis.msp.lcdui.InputMethodListener)에서 등록하여 사용한다. InputMethodHandler에서 InputMethodListener의 notifyTextChanged에 넘겨주는 인자는 처리된 문자와 처리할 문자의 개수, 처리상태이다. 메쏘드 상세 설명

#### notifyTextChanged

public void notifyTextChanged(char[] chText, int len,int pMode) InputMethod를 통해 전달된 문자객체를 받아 처리한다.

**매개 변수**

- `chText` - 입력문자
- `len` - 처리할 문자의 개수
- `pMode` - 처리상태 Insert(-1) / replace(0) / delete(1)
- `Interface` - JletEventListener
- `public` - interface JletEventListener 응용 프로그램(Jlet)의 이벤트를 처리해주는 인터페이스. postEvent에 의해서 넣어진 이벤트를 처리한다. 기본적으로 입력장치에 의한 이벤트를 제외한 모든 이벤트는 이
- `Listener를` - 통해서 처리되어야 한다. 메쏘드 상세 설명 notifyEvent
- `public` - void notifyEvent(int type, int param1, int param2) 응용 프로그램 이벤트가 발생하면 불린다.

**매개 변수**

- `type` - 이벤트 타입
- `param1` - 이벤트 파라미터
- `param2` - 이벤트 파라미터

**참고 항목**

Display.addJletEventListener(org.kwis.msp.lcdui.JletEventListener) Class Card java.lang.Object | +--org.kwis.msp.lcdui.Card Direct Known Subclasses: ProxyCard public abstract class Card extends Object 화면에 출력될 수 있는 하나의 단위 클래스이다. 이 클래스는 화면에 출력할 수 있는 단위가 되며 한 화면은 여러 카드가 쌓인 스택으로 구성된다. 스택에 싸인 여러 카드는 한 화면(Display)에 보여진다. 한 카드는 여러 화면에 넣을 수는 없다. 카드는 화면상에서의 위치와 크기를 가지고 있다. move나 resize함수를 이용하여 그 위치나 크기를 변경할 수 있다. repaint라는 함수를 사용하게 되면, 카드의 일부분에 대해서 다시 이벤트 처리 쓰레드에 의해서 paint 함수가 불려서 화면에 내용이 나타나도록 되어 있다. 카드는 사용자 입력을 받을 수 있다. keyNotify, pointerNotify, 등의 사용자에 의해서 불려지는 함수가 있으며, 모든 이벤트는 일단 스택 상위의 Card로 전달된다. 전달된 이벤트가 그 카드에서 처리를 한다면 위의 불려지는 함수는 true를 돌려주며, 그러면, 하위 Card는 이벤트를 받지 못한다. 그러나 반대로 false 를 돌려주면, 하위 카드에게 이벤트를 전달하며, 같은 식으로 이벤트를 받은 하위 카드는 true, false를 돌려준다. 이 과정은 맨 하위 Card까지 반복이 된다. 카드가 입력 받은 키는 기본적으로 ITU-Key '0'부터 '9' 그리고 '#', '*' 이 가능하다. 이 키들은 휴대폰에 꼭 존재하는 키이다. 그 외의 키들은 게임 키로 판별이 가능하다. 지원되는 키들은 EventQueue.UP, EventQueue.DOWN, EventQueue.LEFT, EventQueue.RIGHT, EventQueue.FIRE등이며, EventQueue.SOFT1, EventQueue.SOFT2도 있지만, 이 경우에는 폰에서 지원하지 않는 경우가 있으므로 유의해서 사용하십시오. 게임 키로 판별할 경우에는 Display.getGameAction(int)와 Display.getKeyCode(int)라는 함수로 키 코드와 게임 키로의 서로의 변환이 가능한다. 카드가 pushCard, popCard에 의해서 보여지거나, 보이지 않게 되는 경우에 showNotify라는 함수가 불린다. 좌표체계는 화면 좌측 상단이 원점이 되고, 밑으로 가면 y축의 값이 증가하고, 오른쪽으로 가면 x축의 값이 증가하도록 되어 있다. Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 필드 상세 설명

#### x

protected int x card의 화면상의 x축 좌표.

#### y

protected int y Card의 화면상의 y축 좌표.

#### w

protected int w Card의 화면상의 폭.

#### h

protected int h Card의 화면상의 높이.

#### bTrans

protected boolean bTrans Card가 투명한지 아닌지 여부. 이 옵션을 사용하면, 현재 카드 바로 하위 컴포넌트가 그린 후에 카드가 그려지므로, 알파 블랜딩이나 다양한 형태의 카드를 그릴 수 있다. 생성자 상세 설명

#### Card

public Card() 화면 크기만큼의 카드를 생성한다. 기본적으로 화면의 크기만큼의 카드를 생성한다. 이때 Display.getDefaultDisplay함수가 돌려주는 Display의 크기로 잡힌다.

#### Card

public Card(boolean bTrans) 화면 크기만큼의 카드를 생성한다. BTrans에 따라서 투명한 여부가 결정된다. 기본적으로 화면의 크기만큼의 카드를 생성한다. 이때 Display.getDefaultDisplay함수가 돌려주는 Display의 크기로 잡힌다.

**매개 변수**

- `bTrans` - – 투명한 여부 Card
- `public` - Card(Display d) 화면 크기의 카드를 생성한다. 카드는 지정된 디스플레이에서만 사용할 수 있다.

**매개 변수**

- `d` - 카드를 생성할 display Throws
- `NullPointerException` - d가 null일 경우 Card
- `public` - Card(int x, int y, int w,int h) 지정한 크기와 위치로 카드를 생성한다. Display.getDefaultDisplay함수를 통해서 기본
- `Display를` - 얻어와서 그 Display를 위한 Card를 만든다. 이때에는 인수로 넘어오는 값으로 위치와 그 크기를 결정한다.

**매개 변수**

- `x` - Card의 display상에서의 x축 좌표
- `y` - Card의 display상에서의 y축 좌표
- `w` - Card의 폭
- `h` - Card의 높이 Throws
- `IllegalArgumentException` - w나 h가 0 이하인 경우 Card
- `public` - Card(Display d, int x, int y, int w, int h) 지정한 display를 위해서 지정한 크기와 위치로 카드를 생성한다. 지정된 Display를 위한 Card를 만든다. 이때에는 인수로 넘어오는 값으로 위치와 그 크기를 결정한다.

**매개 변수**

- `d` - 카드를 생성할 display.
- `x` - Card의 display상에서의 x축 좌표
- `y` - Card의 display상에서의 y축 좌표
- `w` - Card의 폭
- `h` - Card의 높이 Throws
- `IllegalArgumentException` - w나 h가 0 이하인 경우 Card
- `public` - Card(Display d, int x, int y, int w, int h, boolean bTrans) 지정한 display를 위해서 지정한 크기와 위치로 카드를 생성한다. 지정된 Display를 위한 Card를 만든다. 이때에는 인수로 넘어오는 값으로 위치와 그 크기를 결정한다.

**매개 변수**

- `d` - 카드를 생성할 display.
- `x` - Card의 display상에서의 x축 좌표
- `y` - Card의 display상에서의 y축 좌표
- `w` - Card의 폭
- `h` - Card의 높이
- `bTrans` - 투명한 여부 Throws
- `IllegalArgumentException` - w나 h가 0 이하인 경우
- `NullPointerException` - Display가 null일 경우 메쏘드 상세 설명 move
- `public` - void move(int x, int y) 카드의 화면상의 위치를 변경한다. 지정된 x, y값으로 화면상의 위치를 변경한다.

**매개 변수**

- `x` - Card의 display상에서의 x축 좌표
- `y` - Card의 display상에서의 y축 좌표 resize
- `public` - void resize(int w,int h) 카드의 크기를 변경한다. w, h 둘 중 하나가 0보다 작거나 같은 경우에는
- `IllegalArgumentException` - 오류를 발생 시킨다.

**매개 변수**

- `w` - 카드의 폭
- `h` - 카드의 높이 Throws
- `IllegalArgumentException` - w나 h가 0 이하인 경우 getWidth
- `public` - int getWidth() 카드의 폭을 얻어 온다. 카드의 화면상에서의 폭을 얻어 온다.

**반환 값**

카드의 폭 getHeight public int getHeight() 카드의 높이를 얻어 온다. 카드의 화면상에서의 높이를 얻어 온다.

**반환 값**

카드의 높이 getX public int getX() 카드의 x축 위치를 얻어 온다. 카드의 x축 상에서의 위치를 얻어 온다.

**반환 값**

카드의 x축 상의 좌표 getY public int getY() 카드의 y축 위치를 얻어 온다. 카드의 y축 상에서의 위치를 얻어 온다.

**반환 값**

카드의 y축 상의 좌표 showNotify protected void showNotify(boolean bShow) 이 카드가 보이기 바로 직전이나, 카드가 화면에서 삭제되는 경우에 불린다. 화면에서 이 카드 보이기 바로 직전에는 bShow파라미터가 true가 되어서 호출되며, 카드가 화면에 사라지기 전에는 bShow가 false가 되어서 호출된다. 상속하는 클래스에서 이 함수 내에 애니메이션이나 타이머를 등록하거나 삭제하는 기능을 넣으면 된다.

**매개 변수**

- `bShow` - 보이는지 안 보이는지 여부 keyNotify
- `protected` - boolean keyNotify(int type, int key) 사용자 키 입력이 생성되면 불린다. 사용자가 키를 누르거나 뗄 때 포커스를 가지는 컴포넌트의 이 함수가 불린다. 키를 누르거나 뗄 때에는 param1이 키 코드 값이 되고, type에는 KEY_PRESSED나
- `KEY_RELEASED등과` - 같은 내부 서브 이벤트 타입 값이 넘어 온다. 이 함수는 반환 값으로 false를 넘기면 이벤트가 하위 카드로 전달된다. 만일 true를 넘기면 이벤트는 더 이상 하위 카드로 전달되지 않는다. 키 코드 값은 기본 ITU 키인 경우에는 대응하는 ASCII 코드 값이 되며, 그렇지 않은 경우에는 모두 음수 값으로 넘어 온다. 제어 키인 경우에는 Display.getGameAction(int)으로 해당하는 키인지를 판별한다.

**매개 변수**

- `type` - KEY_PRESSED나 KEY_RELEASED, KEY_TYPED,
- `KEY_REPEATED중` - 하나
- `key` - keyCode값; 자세한 키코드는 EventQueue를 참조

**반환 값**

하위 카드에 이벤트 전달하려면 false, 그렇지 않으면 true pointerNotify protected boolean pointerNotify(int type,int x, int y) 사용자 포인팅 디바이스의 입력이 생성되면 불린다. 사용자가 키를 누르거나 뗄 때, 혹은 포인팅 디바이스의 입력이 있는 경우 불린다. type은 POINT_PRESSED, POINT_RELEASED, POINT_DRAGGED중 하나가 되며, 포인팅 디바이스의 x, y축 값은 Card상에서의 좌표체계 값이 된다. 이 함수가 반환 값으로 false를 넘기면 이벤트는 하위 카드로 전달된다. 만일 true를 넘기면 이벤트는 더 이상 하위 카드로 전달되지 않는다.

**매개 변수**

- `type` - POINT_PRESSED나 POINT_RELEASED,
- `POINT_DRAGGED중` - 하나
- `x` - x Card의 display 상에서의 x 축 값
- `y` - y Card의 display 상에서의 y 축 값

**반환 값**

하위 Card에 이벤트 전달하려면 false, 그렇지 않으면 true paint protected abstract void paint(Graphics g) Card의 내용을 그려준다. 응용 프로그램은 이 함수를 꼭 구현해 주어야 한다. 이때 인수로 넘어오는 g는 Card에 맞도록 클리핑 되어 있다. translate, setClip에 의해서 클리핑 영역을 변경하게 되면, Card가 지정하는 이상의 부분을 칠하게 되어 있으므로 유의해서 사용해야 한다. 그릴 내용은 Graphics객체를 사용하여 그리게 된다.

**매개 변수**

- `g` - 칠해질 graphics repaint
- `public` - void repaint(int x,int y, int w, int h) 지정된 영역을 다시 그려준다. x, y로 시작해서 폭 w, 높이 h만큼의 사각형의 내용을 다시 그려준다. 이 함수는 직접 paint함수를 부르지 않고, 다만 특정 시간 이후에
- `paint함수가` - 이벤트 처리 쓰레드에서 부른다.
- `paint함수를` - 부를 때 넘어오는 Graphics 객체는 다시 칠할 영역으로 클리핑 되어 넘어 온다. 클리핑 영역은 이 함수를 부르기 전까지의 칠할 영역을 모두 합하므로
- `repaint한` - 영역 보다 클 수 있다. 다시 칠해지는 영역은 Card의 영역을 벗어 날 수 없다.

**매개 변수**

- `x` - 특정영역을 가리키는 Card상에서의 x축 좌표
- `y` - 특정영역을 가리키는 Card상에서의 y축 좌표
- `w` - 특정영역의 넓이
- `h` - 특정영역의 폭 repaint
- `public` - void repaint()
- `Card전체` - 영역을 다시 그려준다. repaint(0, 0, getWidth(), getHeight())을 부르는 것과 마찬가지 효과이다. serviceRepaints
- `public` - void serviceRepaints()
- `repaint영역을` - 다시 그리고, 화면에 출력한다. repaint할 영역을 강제적으로 그린다. 이 함수 내에서 직접 paint 함수를 부른다. isShown
- `public` - boolean isShown()
- `Card가` - 화면에 보이는지 안 보이는지 여부를 돌려준다. Card가 Display에
- `pushCard함수로` - 등록되어야만 화면에 출력 되어 이 함수가 true를 반환하게 된다.

**반환 값**

보이는지 안 보이는 지 여부 getDisplay public Display getDisplay() 카드의 display를 돌려준다.

**반환 값**

카드의 display Class Display java.lang.Object | +--org.kwis.msp.lcdui.Display public class Display extends Object 화면의 출력 관련 함수와 정보를 가지는 클래스이다. 기본적으로 화면에 무언가를 출력하기 위해서 Display를 구한 후에 Card를 생성하고, pushCard함수를 호출하여 Display에 Card를 등록 시킨다. 이후에 Card의 paint함수에서 그려지는 내용이 화면에 출력된다. 한 화면(LCD)은 Display에 대응한다. 응용프로그램은 Display을 여러 개 가질 수 있다. 이는 휴대폰 중에 듀얼 LCD가 있는 모델을 지원하기 위하여 Jlet상에서 두 화면을 사용할 수 있도록 하기 위함이다. Display를 얻어 오기 위해서는 getDisplay(java.lang.String)함수를 사용하여 가져온다. 한 화면을 여러 개의 Card로 구성된다. Card는 맨 아래 Card부터 시작해서 하나씩 그려지며, 맨 마지막에는 스택 맨 상위에 있는 Card가 그려진다. 이런 메커니즘으로 대화 상자 등을 처리할 수 있도록 하였다. 입력은 반대 방향으로 맨 상위에 있는 Card에게 전달되며 이 Card는 자신이 이벤트를 처리했는지 안 했는지 여부를 돌려준다. 만일 처리했다면, 더 이상 이벤트는 하위 Card에게 전달되지 않지만, 처리하지 않았다면 하위 Card에게 전달되며, 다시 한번 처리여부를 확인하게 되어 맨 아래 Card까지 전달 될 수도 있다. 실제로 InputMethodHandler에 의해서 생성되는 창이나 기타 대화 상자 등은 이런 식으로 처리가 된다. 듀얼 LCD에 대응하는 Display에서는 사용자 입력 이벤트(키 이벤트, 포인터 이벤트)가 발생하지 않음을 유의하십시오. Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 메쏘드 상세 설명 getDefaultDisplay public static Display getDefaultDisplay() 기본 Display를 얻어 온다. 기본 화면에 대응하는 Display를 얻어 온다.

**반환 값**

기본 display getD isplay public static final Display getDisplay(String str) 문자열에 대응하는 Display를 얻어 온다. 이때 문자열이 null이면 기본 Display를 얻어 오며, 폰에 따라서는 문자열을 "dual"로 넘겨주면 듀얼 lcd에 대응하는 Display를 얻어 올 수 있다. 만일 해당하는 Display가 없는 경우에는 null을 돌려준다.

**매개 변수**

- `str` - display를 가리키는 문자열

**반환 값**

display 객체 pushCard public final void pushCard(Card c) 카드를 화면에 보일 수 있도록 한다. 카드를 화면에 보여지도록 하며 사용자의 입력을 받으면 지정된 함수가 불러지도록 한다. 카드는 화면 상위에 위치하여 다른 카드들이 다 그려진 후 그려진다. 만일 같은 카드가 이미 화면에 보여지고 있다면, 이 함수는 아무런 일도 하지 않는다. 또한 c값이 null이면 아무런 동작도 하지 않는다. 화면에 카드가 보여지게 되면, 그리기 전에 showNotify함수를 호출한다. 그리고 나서 repaint가 불리기 때문에 특정 시간 이후에 paint가 불려져 화면에 나타난다. 이후로 isShown()이라는 함수는 항상 true를 돌려주도록 되어 있다. 응용 프로그램이 타 응용 프로그램을 수행한 후에 pushCard()를 하게 되면, 그 카드는 화면 맨 상단에 보여지지 않고, 타 응용 프로그램의 바로 아래에 위치하게 된다.

**매개 변수**

- `c` - 화면에 맨 상위에 보여질 카드. Throws
- `NullPointerException` - c가 null인 경우
- `IllegalArgumentException` - c가 생성될 때 지정된 Display가 현재 Display와 다른 경우 popCard
- `public` - final Card popCard() 카드를 꺼내온다. 카드를 화면에서 제거하며, 그 카드를 가져온다. 만일 아무런 Card 도 없다면 null을 돌려준다. 카드는 현재 수행하고 있는 Jlet에서 생성한 카드만을 꺼내 온다. 만일 카드가 존재한다면, 그 카드의 showNotify()함수를 불러준 후에 카드를 화면에서 제거한다. 이 함수 이후로 popCard()로 반환된 Card에 대해서 isShown()함수를 부르면 항상
- `false를` - 돌려준다.

**반환 값**

꺼내온 카드 removeCard public final boolean removeCard(Card c) 특정 카드를 제거한다. 카드를 화면에서 제거하며, 그 성공여부를 반환한다. popCard와는 카드를 지정하는 것 외에 다른 점은 없다. 만일 c가 null이라면 false를 돌려준다.

**매개 변수**

- `c` - 삭제할 카드

**반환 값**

성공적으로 스택에 카드를 제거했는지 여부 removeAllCards public void removeAllCards() 모든 카드를 제거한다. 현재 수행중인 Jlet이 생성한 모든 카드를 Display 에서 제거한다. 각 카드의 showNotify()가 각각 불리며, 더 이상 카드는 화면에 나타나지 않는다. countCard public final int countCard() Display에 등록된 카드의 개수를 가져온다. 현재 Jlet이 Display에 등록한 카드의 개수를 가져온다.

**반환 값**

카드 스택에 있는 카드의 개수 callSerially public final void callSerially(Runnable r) 이벤트가 다 처리되고 난 후에 특정 Runnable의 함수 run을 호출하도록 한다. 이벤트 큐 맨 뒤에 'Runnable'을 부르는 이벤트를 넣고, 곧바로 함수가 종료 된다. 이벤트 처리 쓰레드가 이 이벤트를 처리할 때에는 Runnable 클래스의 run을 수행하도록 되어 있다. 이런 구조로 인해서 r.run()은 될 수 있으면 짧은 수행 시간을 가져야 한다. 여기서 무한 루프나 상당히 많은 시간을 소모 하는 작업을 하면, 이벤트관련 처리를 못하므로, 프로그램이 사용자 입력을 제대로 처리하지 못한다.

**매개 변수**

- `r` - 수행할 runnable 객체 Throws
- `NullPointerException` - r이 null인 경우 callSerially
- `public` - final void callSerially(Runnable r, int timeout) 이벤트가 다 처리되고 난 후에 특정 Runnable의 함수 run을 호출하도록 한다. 이벤트 큐 맨 뒤에 'Runnable'을 부르는 이벤트를 넣고, 곧바로 함수가 종료 된다. 이벤트 처리 thread가 이 이벤트를 처리할 때에는 Runnable 클래스의 run을 수행하도록 되어 있다. 이런 구조로 인해서 r.run()은 될 수 있으면 짧은 수행 시간을 가져야 한다. 여기서 무한 루프나 상당히 많은 시간을 소모 하는 작업을 하면, 이벤트관련 처리를 못하므로, 프로그램이 사용자 입력을 제대로 처리하지 못한다. 이 함수는 특정 시간 이후에 r의 run 을 부를 수 있도록 해준다. 만일 timeout이 0보다 작으면 0으로 간주한다.

**매개 변수**

- `r` - 수행할 runnable 객체
- `timeout` - Runnable이 불려질 시간(밀리 세컨드 단위) Throws
- `NullPointerException` - r이 null인 경우 getDockedCard
- `public` - Card getDockedCard() 붙여진 카드를 돌려준다. setDockedCard
- `public` - void setDockedCard(Card cd, int where) 화면 특정 부분에 카드를 붙이다. 이 카드는 다른 카드에 의해서 가려지지 않으며, 카드가 설정되면 카드의 크기를 뺀 나머지 영역으로 Display 크기가 변경된다. 기본적으로 카드의 x,y 값은 무시되며, where 값이 TOP, BOTTOM인 경우 width 값이, LEFT, RIGHT 인 경우 height 값이 무시되고 Display의 width, height값을 따른다. 단,
- `pushCard로` - 등록된 카드가 존재하지 않아야 하고, 하나의 DockedCard만 설정할 수 있다.

**매개 변수**

- `cd` - 붙일 카드
- `where` - Graphics.TOP 혹은 BOTTOM, LEFT, RIGHT 네가지 중 하나의 값 Throws
- `NullPointerException` - cd가 null인경우
- `IllegalArgumentException` - cd의 Display가 현재의 Dispaly와 다른 경우나 잘못된
- `where값인` - 경우
- `IllegalStateException` - Display에 pushCard나 setDockedCard로 하나 이상의 카드가 등록되어 있는 경우 isColor
- `public` - final boolean isColor() 화면이 컬러 색상을 지원하는지 여부를 돌려준다.

**반환 값**

컬러 지원 여부 numColors public final int numColors() 화면에서 사용할 수 있는 색상의 개수를 돌려준다.

**반환 값**

색상 개수 hasPointerEvents public final boolean hasPointerEvents() 시스템에 포인터 디바이스관련 이벤트가 있는지 여부를 돌려준다.

**반환 값**

포인터 이벤트 여부 hasPointerMotionEvents public final boolean hasPointerMotionEvents() 시스템에 포인터 움직임 디바이스 이벤트가 있는지 여부를 돌려준다.

**반환 값**

포인터 움직임 이벤트 여부 hasRepeatEvents public final boolean hasRepeatEvents() 키 반복 이벤트가 발생할 수 있는지 없는지 여부를 돌려준다.

**반환 값**

키 반복 이벤트 여부 getWidth public final int getWidth() 화면의 폭을 돌려준다. 화면의 픽셀단위의 폭을 돌려준다.

**반환 값**

화면의 폭 getHeight public final int getHeight() 화면의 높이를 돌려준다. 화면의 픽셀단위의 높이를 돌려준다.

**반환 값**

화면의 높이 isDoubleBuffered public boolean isDoubleBuffered() 화면이 더블 버퍼링(double buffering)인지 여부를 돌려준다. 대부분의 휴대폰은 더블 버퍼링을 지원한다. 즉 화면의 Graphics에 그릴 때 화면에 즉시 나타나는 것이 아니라, 특정 함수(flush)를 호출해야만 그린 내용이 화면에 나타난다.

**반환 값**

double buffer 여부 getKeyCode public static int getKeyCode(int gameKey) 게임키에 대응하는 키 코드값을 얻어 온다. gameKey는 EventQueue.UP, EventQueue.DOWN, EventQueue.LEFT, EventQueue.RIGHT, EventQueue.FIRE, EventQueue.GAME_A, EventQueue.GAME_B, EventQueue.GAME_C, EventQueue.GAME_D, 중 하나가 되며, 돌려주는 값은 실제적인 키 코드 값이 된다. 만일 대응하는 키 코드값이 없을 경우에는 0을 돌려준다.

**반환 값**

- 0 또는 대응하는 키 코드값

**참고 항목**

EventQueue

#### getKeyName

public static String getKeyName(int key) 키 코드에 대응하는 키 이름의 문자열을 돌려 받다. 키 코드에 대해서는 EventQueue를 참조하십시오. 만일 적절한 키가 아닌 경우에는 null을 돌려준다. 돌려주는 문자열은 대문자로 된 문자열이며 "UP", "DOWN"와 같다. 돌려주는 문자열은 시스템에 따라서 다르다.

**반환 값**

대응하는 키 이름의 문자열

**참고 항목**

EventQueue

#### getGameAction

public static int getGameAction(int key) 지정한 키 코드에 대응하는 게임키를 구한다. 시스템 키 코드를 넘긴다. 시스템 키코드는 ITU-Key '0' - '9', '*', '#"이 되고, 나머지 제어 키들이 있다. 제어 키는 시스템 마다 다르므로 getGameAction함수를 통해서 어떤 키인지를 판별한다. 키 코드에 대해서는 EventQueue를 참조하십시오. 만일 게임키가 아니거나 대응하는 키 코드값이 없을 경우에는 0을 돌려준다.

**반환 값**

- 0 또는 대응하는 키 코드값

**참고 항목**

EventQueue

#### getBitsPerPixel

public int getBitsPerPixel() 화면의 한 픽셀당 차지하는 비트(bit)를 돌려준다.

**반환 값**

한 픽셀당 차지하는 비트 수 flush public void flush() 내부의 버퍼의 내용을 화면에 출력하도록 한다. 특정 Graphics로 그린 내용을 화면에 출력하기 위해서는 이 함수를 꼭 불러주어야만 화면에 나타나게 된다. serviceRepaints()함수는 내부에 flush()함수를 포함한다. 이 함수는 isDoubleBuffer함수가 true를 돌려주는 시스템인 경우에 화면에 내용을 출력해주고, 그렇지 않은 시스템에 대해서는 아무런 역할을 하지 않는다. addJletEventListener public void addJletEventListener(JletEventListener qel) JletEvent를 받을 Listener를 등록한다. key, repaint, point외에 발생하는 모든 이벤트가 발생시에 호출되는 Listener를 등록한다. 만일 이전에 등록한 Listener를 다시 등록하게 되면, 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `qel` - 이벤트 Listener removeJletEventListener
- `public` - void removeJletEventListener(JletEventListener qel)
- `JletEvent를` - 받을 Listener를 삭제한다.

**매개 변수**

- `qel` - 삭제할 이벤트 Listener grabKey
- `public` - void grabKey(int key, JletEventListener qel) 특정 키를 함수를 부르는 응용 프로그램에서 소유하게 한다. 특정 키에 대한 이벤트가 발생하는 경우 이 키에 대한 이벤트를 이 함수를 부르는 응용 프로그램으로 넘긴다. 같은 키에 대하여는 한번의 grab만을 할 수 있으며 여러 번 grab한 경우 맨 처음
- `grab에` - 대하여만 동작한다. 어플리케이션에 상관없이 해당 키를 가로채는 함수이므로, AccessLevel이 SYSTEM 레벨에서만 사용하도록 제한할 것을 권고한다. AccessLevel이 SYSTEM미만인 프로그램에서는 동작을 하지 않는다.

**매개 변수**

- `key` - 현재 키 ungrabKey
- `public` - void ungrabKey(int key)
- `grabKey로` - 인한 이벤트 소유를 이전 상태로 돌린다. 특정 키에 대한 이벤트 소유를 더 이상 하지 않도록 한다.
- `AccessLevel이` - SYSTEM 레벨에서만 사용하도록 제한할 것을 권고한다.
- `AccessLevel이` - SYSTEM미만인 프로그램에서는 동작을 하지 않는다.

**매개 변수**

- `key` - ungrab할 키
- `Class` - EventQueue java.lang.Object | +--org.kwis.msp.lcdui.EventQueue
- `public` - class EventQueue extends Object 시스템에서 발생하는 이벤트를 관리하는 큐 클래스이다. 응용 프로그램(Jlet) 하나에는 이벤트를 관리하는 EventQueue 객체가 하나 존재하게 된다. 응용 프로그램에 발생한 모든 이벤트는 이 객체에 일단 저장하고. 응용 프로그램은 발생한 이벤트를 하나씩 가져와서 적절히 처리하면, 응용 프로그램이 동작한다. Jlet안에는 이벤트를 가져와서 처리하는 쓰레드가 내부에 존재 한다. 이벤트를 가져오거나 새로운 이벤트를 넣을 때에는 EVENT_SIZE가 지정한 개수 이상의 정수 어레이를 사용한다. 이 어레이에 들어가는 내용은 이벤트 타입에 따라서 다르다. 각 이벤트 타입에 따른 저장되는 내용은 다음과 같다. 단, POINTER_EVENT는 터치 스크린과 같은 포인팅 장치가 없을 경우 선택 사항이다. <표 3-1-1> 이벤트 타입에 따른 저장 내용 event[0] Event[1] event[2] event[3] 키 값(ITU키인
- `KEY_PRESSED` - | KEY_RELEASED
- `KEY_EVENT` - 경우에는 ascii값이 0 | KEY_REPEATED | KEY_TYPED 아니면 음수)
- `POINTER_PRESSED` - | 포인터의 포인터의 화면상
- `POINTER_EVENT` - P OINTER_RELEASED | 화면상 y축
- `x축` - 값
- `POINTER_DRAGGED` - 값
- `TIMER_EVENT` - 타이머 값 실행되는 Jlet 응용 프로그램 내부에서는 getNextEvent와 dispatchEvent를 무한히 수행하도록 되어 있으며, 그 수행 코드는 다음과 같다.
- `int` - event[] = new int[EventQueue.EVENT_SIZE]; while(true){ eq.getNextEvent(event); eq.dispatchEvent(event); } 키 코드는 시스템에 따라서 다르다. 그러나, ITU-키인 경우에는 '0' 에서부터 '9', '*', '#'가 들어오며, 그 외에 아스키 코드값에 대응되는 키가 들어오게 된다. 파워키나 방향키와 같은 제어키는 음수 값으로 들어 오며, 그 값은 플랫폼마다 다를 수 있다. 플랫폼 마다 다른 제어키를 처리하기 위해서 getGameAction와 getKeyCode함수가 존재 한다. 특정 키가 들어 왔을 때 어떤 제어키인지를 알기 위해서 getGameAction함수를 사용한다. 물론 시스템에 따라서 숫자키가 제어키로 사용할 수도 있다. 현재 getGameAction에 반대되는 함수인 getKeyCode함수가 존재하게 된다.
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 필드 상세 설명 EVENT_SIZE
- `public` - static final int EVENT_SIZE 이벤트 하나가 저장되는 단위크기. 4로 지정되어 있으며, getNextEvent함수 호출 시에 적어도 이 크기 이상의 정수 어레이를 넘겨야만 한다. UP
- `public` - static final int UP
- `UP` - 게임 키를 지정하는 상수. 1로 지정되어 있다. DOWN
- `public` - static final int DOWN
- `DOWN` - 게임 키를 지정하는 상수. 6로 지정되어 있다. LEFT
- `public` - static final int LEFT
- `LEFT` - 게임 키를 지정하는 상수. 2로 지정되어 있다. RIGHT
- `public` - static final int RIGHT
- `RIGHT` - 게임 키를 지정하는 상수. 5로 지정되어 있다. FIRE
- `public` - static final int FIRE
- `FIRE` - 게임 키를 지정하는 상수. 8로 지정되어 있다. GAME_A
- `public` - static final int GAME_A
- `GAME_A` - 게임 키를 지정하는 상수. 9로 지정되어 있다. GAME_B
- `public` - static final int GAME_B
- `GAME_B` - 게임 키를 지정하는 상수. 10로 지정되어 있다. GAME_C
- `public` - static final int GAME_C
- `GAME_C` - 게임 키를 지정하는 상수. 11로 지정되어 있다. GAME_D
- `public` - static final int GAME_D
- `GAME_D` - 게임 키를 지정하는 상수. 12로 지정되어 있다. KEY_NUM0
- `public` - static final int KEY_NUM0 ITU-T '0' 키를 지정하는 상수. 48('0')로 지정되어 있다. KEY_NUM1
- `public` - static final int KEY_NUM1 ITU-T '1' 키를 지정하는 상수. 49('1')로 지정되어 있다. KEY_NUM2
- `public` - static final int KEY_NUM2 ITU-T '2' 키를 지정하는 상수. 50('2')으로 지정되어 있다. KEY_NUM3
- `public` - static final int KEY_NUM3 ITU-T '3' 키를 지정하는 상수. 51('3')로 지정되어 있다. KEY_NUM4
- `public` - static final int KEY_NUM4 ITU-T '4' 키를 지정하는 상수. 52('4')로 지정되어 있다. KEY_NUM5
- `public` - static final int KEY_NUM5 ITU-T '5' 키를 지정하는 상수. 53('5')으로 지정되어 있다. KEY_NUM6
- `public` - static final int KEY_NUM6 ITU-T '6' 키를 지정하는 상수. 54('6')로 지정되어 있다. KEY_NUM7
- `public` - static final int KEY_NUM7 ITU-T '7' 키를 지정하는 상수. 55('7')로 지정되어 있다. KEY_NUM8
- `public` - static final int KEY_NUM8 ITU-T '8' 키를 지정하는 상수. 56('8')으로 지정되어 있다. KEY_NUM9
- `public` - static final int KEY_NUM9 ITU-T '9' 키를 지정하는 상수. 57('9')로 지정되어 있다. KEY_STAR
- `public` - static final int KEY_STAR ITU-T '*' 키를 지정하는 상수. 42('*')로 지정되어 있다. KEY_POUND
- `public` - static final int KEY_POUND ITU-T '#' 키를 지정하는 상수. 35('#')로 지정되어 있다. KEY_SEND
- `public` - static final int KEY_SEND 통화키로, -10으로 지정되어 있다. KEY_END
- `public` - static final int KEY_END 종료(전원) 키로, -11로 지정되어 있다. KEY_CAMERA
- `public` - static final int KEY_CAMERA 카메라를 동작시키는 키로, -19로 지정되어 있다. SOFT1
- `public` - static final int SOFT1
- `SOFT1` - 게임 키를 지정하는 상수. 90으로 지정되어 있다. SOFT2
- `public` - static final int SOFT2
- `SOFT2` - 게임 키를 지정하는 상수. 91로 지정되어 있다. SOFT3
- `public` - static final int SOFT3
- `SOFT3` - 게임 키를 지정하는 상수. 92로 지정되어 있다. SIDE_UP
- `public` - static final int SIDE_UP
- `SIDE_UP` - 게임 키를 지정하는 상수. 96로 지정되어 있다. SIDE_DOWN
- `public` - static final int SIDE_DOWN
- `SIDE_DOWN` - 게임 키를 지정하는 상수. 97로 지정되어 있다. SIDE_SEL
- `public` - static final int SIDE_SEL
- `SIDE_SEL` - 게임 키를 지정하는 상수. 98로 지정되어 있다. CLEAR
- `public` - static final int CLEAR
- `CLEAR` - 게임 키를 지정하는 상수. 99로 지정되어 있다. KEY_PRESSED
- `public` - static final int KEY_PRESSED 키 누름 이벤트 타입 상수. 1로 지정되어 있다. KEY_RELEASED
- `public` - static final int KEY_RELEASED 키 떼임 이벤트 타입 상수. 2로 지정되어 있다. KEY_REPEATED
- `public` - static final int KEY_REPEATED 키 반복 이벤트 타입 상수. 3로 지정되어 있다. KEY_TYPED
- `public` - static final int KEY_TYPED 키 입력 이벤트 타입 상수. 4로 지정되어 있다. POINT_PRESSED
- `public` - static final int POINT_PRESSED 포인터 기기 누름 이벤트 타입 상수. 1로 지정되어 있다. POINT_RELEASED
- `public` - static final int POINT_RELEASED 포인터 기기 떼임 이벤트 타입 상수. 2로 지정되어 있다. POINT_DRAGGED
- `public` - static final int POINT_DRAGGED 포인터 기기 드래그 이벤트 타입 상수. 5로 지정되어 있다. KEY_EVENT
- `public` - static final int KEY_EVENT 키 이벤트 상수. 1로 지정되어 있다. POINTER_EVENT
- `public` - static final int POINTER_EVENT 포인터 이벤트 상수. 2로 지정되어 있다. SMS_EVENT
- `public` - static final int SMS_EVENT
- `SMS` - 이벤트 상수. 4로 지정되어 있다. CALL_EVENT
- `public` - static final int CALL_EVENT 단말기 Call Notify 이벤트 상수. 7로 지정되어 있다. ANN_EVENT
- `public` - static final int ANN_EVENT 단말기 indicator Notify 이벤트 상수. 8로 지정되어 있다. REPAINT_EVENT
- `public` - static final int REPAINT_EVENT TIMER_EVENT
- `public` - static final int TIMER_EVENT 타이머 이벤트 상수. 내부용으로 사용된다. 42로 지정되어 있다. CALL_SERIALLY_EVENT
- `public` - static final int CALL_SERIALLY_EVENT 내부 call serially 이벤트 상수. 내부용으로 사용된다. 43로 지정되어 있다. APP_EVENT
- `public` - static final int APP_EVENT 응용 프로그램 이벤트 상수. 100으로 지정되어 있다. CHILDSTART_EVENT
- `public` - static final int CHILDSTART_EVENT 하위 프로그램 시작 이벤트 상수. 101로 지정되어 있다. CHILDSTOP_EVENT
- `public` - static final int CHILDSTOP_EVENT 하위 프로그램 종료 이벤트 상수. 102로 지정되어 있다. ANNUNCIATOR_CHANGE_EVENT
- `public` - static final int ANNUNCIATOR_CHANGE_EVENT 상위 지시자가 변경된 이벤트 상수. 103으로 지정되어 있다. USER_EVENT
- `public` - static final int USER_EVENT 사용자 이벤트 상수. 0x5000으로 지정되어 있다. APP_STOP
- `public` - static final int APP_STOP 응용프로그램 정지 이벤트; APP_EVENT의 서브타입이다. 1로 지정되어 있다. APP_RESUME
- `public` - static final int APP_RESUME 응용프로그램 지속 이벤트; APP_EVENT의 서브타입이다. 2로 지정되어 있다. APP_DESTROY
- `public` - static final int APP_DESTROY 응용프로그램 종료 이벤트; APP_EVENT의 서브타입이다. 3로 지정되어 있다. APP_ACTIVE
- `public` - static final int APP_ACTIVE 현재 Active된 프로그램을 자기 자신으로 변경한다. 내부 용이다.4로 지정되어 있다. 메쏘드 상세 설명 getNextEvent
- `public` - void getNextEvent(int[] event) 발생한 새 이벤트를 가져온다. 새 이벤트는 정수 어레이에 복사 된다. 어레이에는 첫번째에는 이벤트 타입이며, 다음에는 이벤트 타입에 따라서 각기 다른 내용이 저장된다. 이벤트 어레이는 크기가 EVENT_SIZE보다 크거나 같아야 한다. 그렇지 않은 경우
- `ArrayIndexOutOfBoundsException이` - 발생한다. 이 함수는 이벤트 처리 쓰레드 안에서 불려져야 한다. 만일 이벤트 처리 쓰레드가 아닌 경우에는 IllegalThreadStateException이 발생한다.
- `Card의` - keyNotify, paint과 같은 함수를 불러주는 쓰레드가 이벤트 처리 쓰레드가 이다.

**매개 변수**

- `event` - 이벤트가 저장될 어레이. EVENT_SIZE보다 크거나 같아야 한다. Throws
- `ArrayIndexOutOfBoundsException` - 이벤트 어레이의 크기가 'EVENT_SIZE' 보다 작은 경우
- `IllegalThreadStateException` - 이벤트 처리 쓰레드가 아닌 쓰레드에 서 이 함수를 호출하였을 경우
- `NullPointerException` - event가 null인 경우 postEvent
- `public` - boolean postEvent(int[] event) 새로운 이벤트를 넣다. 새로운 이벤트를 넣다. 이벤트를 넣어서 이벤트 처리 쓰레드가 그 이벤트를 처리하도록 한다. 이벤트는 어레이에 넣어주며 이 내용은 복사가 된다. 이때 어레이의 크기는
- `EVENT_SIZE크기보다` - 크거나 같아야 한다. 이벤트 큐가 다 찼다면 false를 돌려주고, 이벤트 큐에 제대로 쌓았다면 true를 돌려준다.

**매개 변수**

- `event` - 넣을 이벤트

**반환 값**

제대로 넣었다면 true, 그렇지 않으면 false. Throws ArrayIndexOutOfBoundsException 이벤트 어레이의 크기가 EVENT_SIZE 보다 작은 경우 NullPointerException event가 null인 경우 postEvent public static void postEvent(int id, int[] event) 특정 응용 프로그램에 이벤트를 전달한다. id가 가리키는 아이디를 가지고 있는 수행중인 프로그램에게 이벤트를 전달한다. 만일 id가 -1인 경우에는 현재 active한 프로그램에게 parameter가 전달된다. 그 외의 값을 가지는 경우에는 보내는 이벤트는 무시된다. 보내는 이벤트는 시스템 이벤트가 아니어야 한다.

**매개 변수**

- `id` - 수행중인 응용 프로그램 아이디
- `event` - event dispatchEvent
- `public` - void dispatchEvent(int[] event) 이벤트를 처리해 준다. 넘겨진 이벤트를 시스템 내부에 있는 이벤트 처리 쓰레드에서 처리하도록 한다.

**매개 변수**

- `event` - 처리할 이벤트 Throws
- `ArrayIndexOutOfBoundsException` - 이벤트 어레이의 크기가 EVENT_SIZE 보다 작은 경우
- `Class` - Font java.lang.Object | +--org.kwis.msp.lcdui.Font
- `public` - class Font extends Object 글꼴 클래스 이다. 문자열을 찍는데 사용되는 문자를 나타내는 글꼴 클래스이다. getFont를 사용해서 원하는 폰트를 가져온다. 기본적으로 getFont를 해서 가져온 폰트는 내부적으로 공유하므로 자원을 해제해야할 필요는 없다.
- `getFont함수로` - 가져와서 Graphics.setFont(org.kwis.msp.lcdui.Font)함수를 통해서 폰트를 지정하여 문자의 화면 출력 외형을 변경할 수 있다.
- `getFont를` - 통해서 시스템에 따라서, 지정한 폰트가 아닌 그와 유사한 폰트를 돌려 받을 수 있다. 문자열의 화면 출력 길이를 알기 위해서는 stringWidth나 substringWidth함수를 사용한다. 폰트의 스타일은 다음 중 하나가 된다. STYLE_PLAIN STYLE_UNDERLINED STYLE_BOLD
- `STYLE_BOLD` - | STYLE_UNDERLINED STYLE_ITALIC
- `STYLE_ITALIC` - | STYLE_UNDERLINED
- `STYLE_BOLD` - | STYLE_ITALIC
- `STYLE_BOLD` - | STYLE_ITALIC | STYLE_UNDERLINED
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 필드 상세 설명 FACE_MONOSPACE
- `public` - static int FACE_MONOSPACE
- `Monospace폰트` - 페이스. 값 32로 지정되어 있으며, 폭이 일정한 폰트를 지정한다. FACE_PROPORTIONAL
- `public` - static int FACE_PROPORTIONAL
- `Proportional폰트` - 페이스. 값이 64로 지정되어 있으며, 폭이 일정하지 않은 폰트를 지정한다. FACE_SYSTEM
- `public` - static int FACE_SYSTEM
- `System` - 폰트 페이스. 값이 0으로 지정되어 있으며, 시스템 폰트에서 사용하는 폰트이다. MONOSPACE혹은 PROPORTIONAL둘 중 하나 이다. SIZE_LARGE
- `public` - static int SIZE_LARGE 큰 크기의 폰트 크기. 값이 16으로 지정되어 있으며, 시스템의 큰 폰트를 지정한다. SIZE_MEDIUM
- `public` - static int SIZE_MEDIUM 중간 크기의 폰트 크기. 값이 0으로 지정되어 있으며, 시스템의 중간 폰트를 지정한다. SIZE_SMALL
- `public` - static int SIZE_SMALL 작은 크기의 폰트 크기. 값이 8로 지정되어 있으며, 시스템의 작은 폰트를 지정한다. STYLE_BOLD
- `public` - static int STYLE_BOLD 진한 폰트 스타일. 다른 폰트 스타일과 혼합되어 사용할 수 있다. 값은 1로 지정한다. STYLE_ITALIC
- `public` - static int STYLE_ITALIC 기운 폰트 스타일. 다른 폰트 스타일과 혼합되어 사용할 수 있다. 값은 2로 지정한다. STYLE_PLAIN
- `public` - static int STYLE_PLAIN 보통 폰트 스타일. 다른 폰트 스타일과 혼합되어 사용할 수 있다. 값은 0로 지정한다. STYLE_UNDERLINED
- `public` - static int STYLE_UNDERLINED 밑줄 그은 폰트 스타일. 다른 폰트 스타일과 혼합되어 사용할 수 있다. 값은 4로 지정되어 있다. style
- `protected` - int style 폰트 스타일을 저장하는 필드. size
- `protected` - int size 폰트 크기를 저장하는 필드. face
- `protected` - int face 폰트 페이스를 저장하는 필드 . 메쏘드 상세 설명 getFont
- `public` - static Font getFont(int face, int style, int size) 특정 폰트를 얻어 온다. 지정된 폰트와 가장 유사한 폰트를 얻어 온다. 이 함수는 시스템에 따라서 제대로 된 폰트가 나올 수 있다.

**매개 변수**

- `face` - 폰트의 face; FACE_MONOSPACE, FACE_PROPORTIONAL,
- `FACE_SYSTEM과` - 같은 값이 올 수 있음
- `style` - 폰트 스타일; STYLE_PLAIN이나 STYLE_ITALIC, STYLE_BOLD, STYLE_UNDERLINED의 조합이 올 수 있음.
- `size` - 폰트 크기; SIZE_LARGE, SIZE_MEDIUM, SIZE_SMALL중 하나가 올 수 있음 Throws
- `IllegalArgumentException` - face, style, size중에 하나라도 유효한 값을 가지지 않는 경우. charsWidth
- `public` - int charsWidth(char[] ch, int offset, int length) 문자열의 화면상의 폭을 넘겨준다. 문자열의 화면상의 폭을 픽셀 단위로 넘겨준다. 계산되는 문자열을 ch가 가리키는 문자 배열의 offset부터 시작해서 length개 까지의 문자가 된다.

**매개 변수**

- `ch` - 문자 배열
- `offset` - 문자 배열에서의 위치
- `length` - 문자 개수

**반환 값**

문자열의 화면상의 픽셀 단위의 폭 Throws ArrayIndexOutOfBoundsException offset이 0보다 작거나 ch의 길이보다 큰 경우, length가 0보다 작은 경우, offset + length가 ch의 길이보다 큰 경우 NullPointerException ch가 null인 경우 charWidth public int charWidth(char ch) 문자의 화면상의 폭을 넘겨 준다. ch가 나타내는 문자의 화면상의 픽셀 단위의 폭을 넘겨준다. 만일 시스템이 지원하지 않는 문자라면 ' '(0x20)의 폭을 넘겨준다. 물론 화면에 출력 시에도 ' '가 출력된다.

**매개 변수**

- `ch` - 문자

**반환 값**

문자의 화면상의 픽셀 단위의 폭 getBaselinePosition public int getBaselinePosition() 문자의 베이스 라인(base line) 높이를 돌려준다.

**반환 값**

문자의 baseline getDefaultFont public static Font getDefaultFont() 시스템의 기본 폰트를 돌려준다.

**반환 값**

시스템 기본 폰트 getFace public int getFace() 폰트의 페이스를 돌려준다. 돌려주는 값은 폰트에 따라서 FACE_MONOSPACE, FACE_PROPORTIONAL, FACE_SYSTEM중의 하나가 된다.

**반환 값**

폰트의 페이스 getHeight public int getHeight() 폰트의 높이를 얻어온다.

**반환 값**

폰트의 높이 getSize public int getSize() 폰트의 크기를 얻어 온다.

**반환 값**

폰트의 크기 getStyle public int getStyle() 폰트의 스타일을 얻어 온다. 폰트의 스타일에 따라서 STYLE_BOLD, STYLE_ITALIC, STYLE_UNDERLINE, STYLE_PLAIN의 값을 OR한 값을 돌려준다.

**반환 값**

폰트의 스타일 isBold public boolean isBold() 폰트의 스타일을 STYLE_BOLD인지 아닌지 여부를 돌려준다.

**반환 값**

폰트의 스타일이 STYLE_BOLD이면 true 그렇지 않으면 false isItalic public boolean isItalic() 폰트의 스타일을 STYLE_ITALIC인지 아닌지 여부를 돌려준다.

**반환 값**

폰트의 스타일이 STYLE_ITALIC이면 true 그렇지 않으면 false isPlain public boolean isPlain() 폰트의 스타일을 STYLE_PLAIN인지 아닌지 여부를 돌려준다.

**반환 값**

폰트의 스타일이 STYLE_PLAIN이면 true 그렇지 않으면 false isUnderlined public boolean isUnderlined() 폰트의 스타일을 STYLE_UNDERLINED인지 아닌지 여부를 돌려준다.

**반환 값**

폰트의 스타일이 STYLE_UNDERLINED이면 true 그렇지 않으면 false stringWidth public int stringWidth(String str) 문자열의 폭을 얻어 온다. str가 지정하는 문자열의 화면에 출력 시 폭을 얻어 온다.

**매개 변수**

- `str` - 폭을 계산할 문자열

**반환 값**

문자열의 폭 Throws NullPointerException str이 null인 경우. substringWidth public int substringWidth(String str, int offset, int len) 문자열의 일부의 폭을 얻어 온다. str가 지정하는 문자열의 offset부터 len개의 문자의 폭을 얻어 온다.

**매개 변수**

- `str` - 폭을 계산할 문자열
- `offset` - 문자열의 시작 점
- `len` - 문자열의 문자 개수

**반환 값**

문자열의 폭 Throws StringIndexOutOfBoundsException offset과 len값이 문자열의 범위를 벗어나는 경우 NullPointerException str이 null인 경우 Class Graphics java.lang.Object | +--org.kwis.msp.lcdui.Graphics public class Graphics extends Object 간단한 2차 기하학적인 도형을 그리는 기능을 제공한다. 텍스트나 이미지, 선, 사각형, 아크 등을 그릴 수 있는 단순한 기능을 제공한다. 사각형과 아크는 특정 색상으로 칠해 질 수 있고, 사각형은 둥근 모서리를 가질 수도 있다. 좌표 체계 화면의 좌측 상단이 (0, 0)이 되며, 아래로 y축이 증가하고, 오른쪽으로 x축이 증가하는 좌표체계를 가진다. 그래픽객체에서 사용되는 모든 좌표는 translate함수에 의해서 변경 될 수 있는 원점을 가지는 좌표체계 하에 있게 된다. 앵커 앵커는 이미지나 폰트 등을 출력 시에 위치를 결정해주는 파라미터가 된다. 지정된 좌표에 객체의 어떤 부분을 위치시킬 것인지를 결정한다. 폰트의 경우에는 앵커는 수평적으로는 LEFT, HCENTER, RIGHT중에 하나가 될 수 있으며, 수직적으로는 TOP, BASELINE, BOTTOM이 될 수 있다. 이 수평/수직적인 내용을 논리적 OR을 사용해서 앵커를 지정한다. 이미지의 경우에는 BASELINE대신에 VCENTER를 사용한다. 수평 앵커는 적어도 하나 지정이 되어야 하며, 거기에 OR되는 수직 앵커는 지정되지 않아도 된다. 앵커는 0 값을 허용하며 만일 앵커가 0 일 경우 LEFT, TOP을 OR 한 값을 갖는다. 스트로크 스타일 스트로크 스타일은 DOTTED나 SOLID로 정의된다. 이 정의된 스타일은 drawLine, drawArc등에서만 적용이 되며fillRect같이 칠하기 함수에는 적용이 되지 않는다. 다른 그림 모드 스트로크 스타일 외에 Graphics에서 지원하는 그리기 모드가 있다. 하나는 XOR 모드로 그리기 이며, 또 하나는 투명정도를 지정한다. setXORMode(boolean)함수를 사용하면, 화면의 내용과 현재 출력하는 내용을 XOR하여 출력할 수 있으며 setAlpha(int)함수를 사용하면, 화면의 내용과 현재 출력하는 내용을 적절히 섞어서 출력할 수 있다. g.setAlpha(255) 는 일반적으로 화면에 나타나며 g.setAlpha(0) 하면 화면에 내용이 출력되지 않는다. XOR모드나 Alpha모드로 출력 시에 속도가 저하 된다. 모든 그래픽 오퍼레이션은 클리핑 영역에 영향을 받다. 이 클리핑 영역 외에는 오퍼레이션에 의해서 내용이 바뀌지 않는다. 클리핑 영역은 Graphics객체가 생성될 때 사용된 화면이나 이미지의 크기보다는 클 수가 없다. Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 필드 상세 설명 BASELINE public static final int BASELINE 앵커 위치를 문자열의 baseline으로 지정하는 상수. 64으로 지정되어 있다. BOTTOM public static final int BOTTOM 앵커의 위치를 문자나 이미지의 아래로 지정하는 상수. 32로 지정되어 있다. DOTTED public static final int DOTTED 도트 스트로크 스타일을 지정하는 상수. 1로 지정되어 있다. HCENTER public static final int HCENTER 앵커의 수평 위치를 문자나 이미지의 가운데로 지정하는 상수. 1로 지정되어 있다. LEFT public static final int LEFT 앵커의 수평 위치를 문자나 이미지의 왼쪽으로 지정하는 상수. 4로 지정되어 있다. RIGHT public static final int RIGHT 앵커의 수평 위치를 문자나 이미지의 오른쪽으로 지정하는 상수. 8로 지정되어 있다. SOLID public static final int SOLID 솔리드 스트로크 스타일을 지정하는 상수. 0으로 지정되어 있다. TOP public static final int TOP 앵커의 수직 위치를 문자나 이미지의 맨 위로 지정하는 상수. 0 으로 지정되어 있다. VCENTER public static final int VCENTER 앵커의 수직 위치를 이미지의 가운대로 지정하는 상수. 2로 지정되어 있다. 메쏘드 상세 설명 clipRect public void clipRect(int x, int y, int width, int height) 클리핑 영역을 지정된 사각형과 공통된 부분을 클리핑 영역으로 지정 한다. 현재 그래픽 개체의 좌표계의 (x, y)점에서 시작하고, 높이가 height이고 폭이 width인 사각형과 내부 클리핑 사각형에 공통으로 포함되는 가장 큰 사각형을 내부 클리핑 사각형으로 지정한다.

**매개 변수**

- `x` - 인터섹트할 사각형의 graphics 좌표계에서의 x축 위치
- `y` - 인터섹트할 사각형의 graphics 좌표계에서의 y축 위치
- `width` - 인터섹트할 사각형의 폭
- `height` - 인터섹트할 사각형의 높이

**참고 항목**

setClip(int, int, int, int)

#### drawChar

public void drawChar(char character, int x, int y, int anchor) 그래픽 좌표계에서 현재 그래픽 개체가 가지고 있는 폰트와 색상으로 character가 지정하는 문자를 지정된 위치에 그려 준다.

**매개 변수**

- `character` - 그려질 문자
- `x` - 앵커 포인트의 x축 좌표
- `y` - 앵커 포인트의 y축 좌표
- `anchor` - 텍스트의 앵커 위치; 앵커를 참조 Throws
- `IllegalArgumentException` - anchor가 유효하지 않은 값을 가지는 경우

**참고 항목**

drawChars(char[], int, int, int, int, int)

#### drawChars

public void drawChars(char[] data, int offset, int length, int x, int y,

```c
int anchor)
data가 가리키는 문자열의 일부를 현재 그래픽 개체가 가지고 있는 폰트와 색상으로
```

지정된 위치에 그려준다.

**매개 변수**

- `data` - 그려질 문자열
- `offset` - 그릴 문자열의 시작 위치
- `length` - 문자열의 개수
- `x` - 앵커 포인트의 x축 좌표
- `y` - 앵커 포인트의 y축 좌표
- `anchor` - 텍스트의 앵커 위치; 앵커를 참조 Throws
- `ArrayIndexOutOfBoundsException` - offset이나 length가 데이타 어레이의 밖에 있는 값일 경우
- `IllegalArgumentException` - anchor값이 유효한 값이 아닌 경우
- `NullPointerException` - data값이 null인 경우

**참고 항목**

drawString(java.lang.String, int, int, int)

#### drawImage

public void drawImage(Image img, int x, int y, int anchor) img가 가리키는 이미지를 지정된 위치에 그려준다.

**매개 변수**

- `img` - 그려질 이미지
- `x` - 앵커 포인트의 x축 좌표
- `y` - 앵커 포인트의 y축 좌표
- `anchor` - 텍스트의 앵커 위치; 앵커를 참조 Throws
- `IllegalArgumentException` - anchor값이 유효한 값이 아닌 경우
- `NullPointerException` - img가 null인 경우

**참고 항목**

Image

#### drawLine

public void drawLine(int x1, int y1, int x2, int y2) 현재 그래픽이 가지고 있는 좌표체계의 두 점을 연결하는 선을 그래픽 개체가 정의하는 색상과 스트로크 스타일로 그려준다.

**매개 변수**

- `x1` - 선의 시작점의 x축 좌표
- `y1` - 선의 시작점의 y축 좌표
- `x2` - 선의 끝점의 x축 좌표
- `y2` - 선의 끝점의 y축 좌표 drawRect
- `public` - void drawRect(int x, int y, int width, int height) 현재 그래픽이 지정하는 색상과 스트로크 스타일로 사각형을 그린다. 이 함수로 그려지는 영역은 (width + 1)의 폭과 (height + 1)의 높이를 가진다. width나
- `height가` - 0보다 작으면 아무 것도 그려지지 않는다. 그릴 때에는 fillRect과는 달리 내부는 칠해지지 않는다.

**매개 변수**

- `x` - 사각형을 그릴 x축 좌표
- `y` - 사각형을 그릴 y축 좌표
- `width` - 사각형의 폭
- `height` - 사각형의 높이

**참고 항목**

fillRect(int, int, int, int)

#### drawRoundRect

public void drawRoundRect(int x, int y, int width, int height, int arcWidth,

```c
int arcHeight)
현재 그래픽이 지정하는 색상과 스트로크 스타일로 모서리가 둥근 사각형을 그린다.
```

이 함수로 그려지는 영역은 (width + 1)의 폭과 (height + 1)의 높이를 가진다. width나 height가 0보다 작으면 아무 것도 그려지지 않는다. 그릴 때에는 fillRoundRect과는 달리 내부는 칠해지지 않는다. 만일 arcWidth가 width / 2보다 큰 경우에는 width / 2 로 된다. 만일 arcHeight가 height / 2보다 큰 경우에는 height / 2로 된다.

**매개 변수**

- `x` - 사각형을 그릴 x축 좌표
- `y` - 사각형을 그릴 y축 좌표
- `width` - 사각형의 폭
- `height` - 사각형의 높이
- `arcWidth` - 네 모서리에 그려질 둥근 아크 부분의 수평 반지름
- `arcHeight` - 네 모서리에 그려질 둥근 아크 부분의 수직 반지름

**참고 항목**

fillRoundRect(int, int, int, int, int, int)

#### drawString

public void drawString(String str, int x, int y, int anchor) 현재 그래픽이 지정하는 색상과 폰트로 문자열을 그린다. 만일 문자열 중에 그릴 수 없는 문자가 있는 경우에는 공백문자(space)로 처리한다.

**매개 변수**

- `str` - 그릴 문자열
- `x` - 앵커 포인트의 x축 좌표
- `y` - 앵커 포인트의 y축 좌표
- `anchor` - 텍스트의 앵커 위치; 앵커를 참조 Throws
- `IllegalArgumentException` - anchor가 유효한 값이 아닌 경우
- `NullPointerException` - str이 null인 경우

**참고 항목**

drawChars(char[], int, int, int, int, int), drawSubstring(String, int, int, int, int, int)

#### drawSubstring

public void drawSubstring(String str, int offset, int len, int x, int y,

```c
int anchor)
현재 그래픽이 지정하는 색상과 폰트로 문자열의 일부를 그린다. 만일 문자열 중에
```

그릴 수 없는 문자가 있는 경우에는 공백문자(space)로 처리한다.

**매개 변수**

- `str` - 그릴 문자열
- `offset` - 그릴 문자열 내부의 „0‟으로부터 세는 시작 인덱스
- `len` - 문자열 일부의 문자 개수
- `x` - 앵커 포인트의 x축 좌표
- `y` - 앵커 포인트의 y축 좌표
- `anchor` - 텍스트의 앵커 위치; 앵커를 참조 Throws
- `IllegalArgumentException` - anchor가 유효한 값이 아닌 경우
- `NullPointerException` - str이 null인 경우
- `StringIndexOutOfBoundsException` - offset과 len의 값이 str의 내부 문자열을 가리킬 수 없는 경우

**참고 항목**

drawString(String, int, int, int)

#### drawArc

public void drawArc(int x, int y, int width, int height, int startAngle,

```c
int arcAngle)
현재 그래픽이 지정하는 색상과 스트로크 스타일로 아크를 그린다.
```

startAngle에서 시작해서 arcAngle만큼 아크를 그린다. 각도는 0 도가 x축이 증가하는 방향 Y축이 증가하지 않는 방향, 즉 3시 방향이 된다. 양수 값은 시계 반대 방향이고, 음수 값은 시계 방향이 이다. 아크의 중심은 (x, y)이 시작점이고 width이고, height가 지정하는 크기를 가진 사각형의 중심이 되며, drawRect할 때와 마찬가지로 width + 1의 폭과 height + 1높이를 가지는 영역 차지한다. 만일 폭이나 높이가 0보다 작은 경우에 아무것도 그려지지 않는다.

**매개 변수**

- `x` - 아크의 상위-좌측 모서리의 x축 좌표
- `y` - 아크의 상위-좌측 모서리의 y축 좌표
- `width` - 아크가 그려질 때 폭
- `height` - 아크가 그려질 때 높이
- `startAngle` - 시작 각도
- `arcAngle` - 시작 각도로부터 아크의 폭의 크기 각도

**참고 항목**

fillArc(int, int, int, int, int, int)

#### fillArc

public void fillArc(int x, int y, int width, int height, int startAngle,

```c
int arcAngle)
현재 그래픽이 지정하는 색상으로 아크를 칠한다.
```

startAngle, arcAngle만큼 아크를 그린다. 위치는 drawArc와 같은 그리는 방법을 취한다. 아크는 fillRect할 때와 마찬가지로 width의 폭과 height높이를 가지는 영역 차지한다. 칠해지는 영역은 pie와 같은 형태가 된다. 만일 폭이나 높이가 0과 같거나 작은 경우에 아무것도 그려지지 않는다.

**매개 변수**

- `x` - 아크의 상위-좌측 모서리의 x축 좌표
- `y` - 아크의 상위-좌측 모서리의 y축 좌표
- `width` - 아크가 그려질 때 폭
- `height` - 아크가 그려질 때 높이
- `startAngle` - 시작 각도
- `arcAngle` - 시작 각도로부터 아크의 폭의 크기 각도

**참고 항목**

fillArc(int, int, int, int, int, int)

#### fillRect

public void fillRect(int x, int y, int width, int height) 현재 그래픽이 지정하는 색상으로 사각형을 칠한다. 이 함수로 그려지는 영역은 width의 폭과 height의 높이를 가진다. width나 height가 0같거나 보다 작으면 아무 것도 그려지지 않는다. 그릴 때에는 내부도 칠한다.

**매개 변수**

- `x` - 사각형을 그릴 x축 좌표
- `y` - 사각형을 그릴 y축 좌표
- `width` - 사각형의 폭
- `height` - 사각형의 높이

**참고 항목**

drawRect(int, int, int, int)

#### fillRoundRect

public void fillRoundRect(int x, int y, int width, int height, int arcWidth,

```c
int arcHeight)
현재 그래픽이 지정하는 색상으로 모서리가 둥근 사각형을 칠한다.
```

이 함수로 그려지는 영역은 width의 폭과 height의 높이를 가진다. 폭이나 높이가 0보다 작으면 아무 것도 그려지지 않는다. 그릴 때에는 내부도 칠한다. 만일 arcWidth가 width / 2보다 큰 경우에는 width / 2 로 된다. 만일 arcHeight가 height / 2보다 큰 경우에는 height / 2로 된다.

**매개 변수**

- `x` - 사각형을 그릴 x축 좌표
- `y` - 사각형을 그릴 y축 좌표
- `width` - 사각형의 폭
- `height` - 사각형의 높이
- `arcWidth` - 네 모서리에 그려질 둥근 아크 부분의 수평 반지름
- `arcHeight` - 네 모서리에 그려질 둥근 아크 부분의 수직 반지름

**참고 항목**

drawRoundRect(int, int, int, int, int, int)

#### fillPolygon

public void fillPolygon(int[] x, int[] y) 지정된 (x,y) 점들로 다각형을 그리고 현재 그래픽에 지정된 색상으로 내부를 채운다.

**매개 변수**

- `x` - 그릴 다각형의 x축 array
- `y` - 그릴 다각형의 y축 array Throws
- `IllegalArgumentException` - x와 y 의 어레이 크기가 다른 경우
- `NullPointerException` - x나 y가 null 인 경우 getBlueComponent
- `public` - int getBlueComponent() 현재 지정된 색상의 파랑색 값을 돌려준다.

**반환 값**

- 0-255까지의 정수값

**참고 항목**

setColor(int, int, int)

#### getClipHeight

public int getClipHeight() 클리핑 사각형의 높이를 돌려준다.

**반환 값**

클리핑 사각형의 높이

**참고 항목**

clipRect(int, int, int, int), setClip(int, int, int, int)

#### getClipWidth

public int getClipWidth() 클리핑 사각형의 폭을 돌려준다.

**반환 값**

클리핑 사각형의 폭

**참고 항목**

clipRect(int, int, int, int), setClip(int, int, int, int)

#### getClipX

public int getClipX() 클리핑 사각형의 그래픽 좌표계에서의 x축 좌표를 돌려준다.

**반환 값**

클리핑 사각형의 x축 좌표

**참고 항목**

clipRect(int, int, int, int), setClip(int, int, int, int)

#### getClipY

public int getClipY() 클리핑 사각형의 그래픽 좌표계에서의 y축 좌표를 돌려준다.

**반환 값**

클리핑 사각형의 y축 좌표

**참고 항목**

clipRect(int, int, int, int), setClip(int, int, int, int)

#### getColor

public int getColor() 현재 지정된 색상을 돌려준다.

**반환 값**

- 0x00RRGGBB의 형식을 가지는 정수

**참고 항목**

setColor(int, int, int), setColor(int)

#### getFont

public Font getFont() 현재 지정된 폰트를 돌려준다.

**반환 값**

현재 지정된 폰트

**참고 항목**

Font, setFont(org.kwis.msp.lcdui.Font)

#### getGrayScale

public int getGrayScale() 현재 지정된 색상의 회색조 값을 얻어 온다. 만일 색상이 setGrayScale에 의해서 지정되었다면, 그 값이 그대로 돌려지고, 만일 색상이 빨강, 파랑, 녹색으로 지정되었다면, 그 색에 대응하는 가장 근접하는 회색조 색상값이 돌려준다.

**반환 값**

- 0-255까지의 정수

**참고 항목**

setGrayScale(int)

#### getGreenComponent

public int getGreenComponent() 현재 지정된 색상의 녹색값을 돌려준다.

**반환 값**

- 0-255까지의 정수값

**참고 항목**

setColor(int, int, int)

#### getRedComponent

public int getRedComponent() 현재 지정된 색상의 빨강색값을 돌려준다.

**반환 값**

- 0-255까지의 정수값

**참고 항목**

setColor(int, int, int)

#### getStrokeStyle

public int getStrokeStyle() 선, 아크, 사각형 그리기에 사용되는 현재 지정된 스트로크 스타일을 돌려준다.

**반환 값**

스트로크 스타일, SOLID 또는 DOTTED getTranslateX public int getTranslateX() 그래픽 좌표체계의 원점의 x축 좌표를 돌려준다.

**반환 값**

원점의 x축 좌표

**참고 항목**

getTranslateX(), translate(int, int)

#### getTranslateY

public int getTranslateY() 그래픽 좌표체계의 원점의 y축 좌표를 돌려준다.

**반환 값**

원점의 y축 좌표

**참고 항목**

getTranslateX(), translate(int, int)

#### setClip

public void setClip(int x, int y, int width, int height) 클리핑 사각형 영역을 지정한다. 모든 그리는 연산은 클리핑 영역 밖에서는 일어나지 않는다. 사각형의 시작점은 현재 그래픽 좌표체계 (x, y) 에서 시작하며, 폭은 width이며, 높이는 height가 된다. x, y 의 값은 getTranslateX() + x 값이 0 보다 작거나 getTranslateY() + y 값이 0보다 작을 경우 0으로 설정된다.

**매개 변수**

- `x` - 새 클리핑 사각형의 시작점 x축 좌표
- `y` - 새 클리핑 사각형의 시작점 y축 좌표
- `width` - 새 클리핑 사각형의 폭
- `height` - 새 클리핑 사각형의 높이

**참고 항목**

clipRect(int, int, int, int)

#### setColor

public void setColor(int rgb) 모든 그리기 연산에 사용되는 색상을 지정한다. 이 함수가 불리고 나서는 모든 그리기 연산은 이 함수가 지정한 색상을 사용하여 그린다. 색상은 RGB 형태로 넘겨지며, 0x00RRGGBB와 같은 형태로 넘겨진다. 맨 상위 8bit는 어떤 값을 가지고 있어도 상관이 없다.

**매개 변수**

rgb
setColor
- `public` - void setColor(int r, int g, int b) 모든 그리기 연산에 사용되는 색상을 RGB형태로 지정한다. 이 함수가 불리고 나서는 모든 그리기 연산은 이 함수가 지정한 색상을 사용하여 그린다. 색상은 각기
- `RGB값을` - 따로 받다.

**매개 변수**

- `r` - 0-255까지의 빨강색 값
- `g` - 0-255까지의 녹색 값
- `b` - 0-255까지의 파랑색 값 Throws
- `IllegalArgumentException` - r, g, b값이 범위를 벗어나는 경우. setFont
- `public` - void setFont(Font font) 문자열을 그릴때 사용되는 폰트를 지정한다. 이 함수가 불린 이후에 모든 문자열 그리기 연산은 이 함수가 지정한 폰트로써 그린다. 만일 폰트가 null이면 setFont(Font.getDefaultFont()) 와 같다.

**매개 변수**

- `font` - 지정할 폰트 setGrayScale
- `public` - void setGrayScale(int val) 모든 그리기 영산에 사용되는 회색조 색상으로 지정한다. 이 함수가 불리고 나서는 모든 그리기 연산은 이 함수가 지정한 색상을 사용하여 그린다. 화면에 출력할 수 있는 가장 근접한 색상으로 출력 된다. 이 값은 0-255값이 되어야 한다.

**매개 변수**

- `val` - 0-255까지의 회색조 색상 Throws
- `IllegalArgumentException` - 회색조 색상이 범위를 넘어가는 경우 setStrokeStyle
- `public` - void setStrokeStyle(int style) 그리기에 사용되는 스트로크 스타일을 결정한다. 칠하기나 이미지 그리기에는 이 함수에 영향을 받지않는다.

**매개 변수**

- `style` - SOLID 또는 DOTTED Throws
- `IllegalArgumentException` - style이 유효한 값을 가지지 않는 경우. translate
- `public` - void translate(int x, int y) 그래픽 좌표체계의 원점을 상대적으로 이동한다. 연산의 모든 좌표 체계는 이 함수에 의해서 변경이 된다. 이 함수를 호출한 후에 모든 연산은 영향을 받다.

**매개 변수**

- `x` - 새로운 원점의 x축 좌표(현재 좌표체계에서)
- `y` - 새로운 원점의 y축 좌표(현재 좌표체계에서)

**참고 항목**

getTranslateX(), getTranslateY()

#### getPixel

public int getPixel(int x, int y) 특정 위치의 픽셀을 RGB 형태로 가지고 온다. 화면이나 이미지의 특정 (x, y)위치에서 픽셀 값을 가지고 온다. 가져온 픽셀 값은 0x00RRGGBB형태를 가진다. 이 함수는 클리핑 영역에 영향을 받지 않는다.

**매개 변수**

- `x` - 가져올 pixel의 x축 좌표
- `y` - 가져올 pixel의 y축 좌표

**반환 값**

pixel 값. Throws IllegalArgumentException x, y가 음수이거나 Graphics의 범위를 벗어날 경우 setPixel public void setPixel(int x, int y) 특정 위치에 지정된 색상으로 점을 찍다. 화면이나 이미지의 특정 (x, y)위치에 지정된 픽셀을 찍다. 이 함수는 클리핑 영역에 영향을 받는다.

**매개 변수**

- `x` - 가져올 pixel의 x축 좌표
- `y` - 가져올 pixel의 y축 좌표 Throws
- `IllegalArgumentException` - x, y가 음수이거나 Graphics의 범위를 벗어날 경우 getPixels
- `public` - void getPixels(int x, int y, int w, int h, byte[] pixels, int offset, int bpl) 화면이나 이미지에서 특정 부분의 픽셀 값들을 가지고 온다. Graphics와 연결된 화면이나 이미지의 특정 부분의 픽셀 값들을 가져온다. 이때 픽셀의 데이타 타입은 기기마다 다르며, setPixel에서 지정하는 데이타 타입과 동일하게 된다. 이 함수는 클리핑 함수에 영향을 받지 않는다.

**매개 변수**

- `x` - 가져올 픽셀 영역의 x축 좌표
- `y` - 가져올 픽셀 영역의 y축 좌표
- `w` - 가져올 픽셀 영역의 폭
- `h` - 가져올 픽셀 영역의 높이
- `pixels` - 픽셀이 저장될 어레이
- `offset` - 픽셀이 저장되기 시작할 위치
- `bpl` - 한 줄의 이미지가 저장되기 위해서 필요한 바이트 수 Throws
- `ArrayIndexOutOfBoundsException` - pixels의 어레이 크기가. h*bpl 보다 작은 경우
- `NullPointerException` - pixels가 null인 경우 getRGBPixels
- `public` - void getRGBPixels(int x, int y, int w, int h, int[] pixels, int offset,
- `int` - bpl) 화면이나 이미지에서 특정 부분의 픽셀 값들을 가지고 온다. Graphics와 연결된 화면이나 이미지의 특정 부분의 픽셀 값들을 가져온다. 이때 픽셀의 data타입은 0x00RRGGBB값이 된다. 이 함수는 클리핑 함수에 영향을 받지 않는다.

**매개 변수**

- `x` - 가져올 픽셀 영역의 x축 좌표
- `y` - 가져올 픽셀 영역의 y축 좌표
- `w` - 가져올 픽셀 영역의 폭
- `h` - 가져올 픽셀 영역의 높이
- `pixels` - 픽셀이 저장될 어레이
- `offset` - 픽셀이 저장되기 시작할 위치
- `bpl` - 한 줄의 이미지가 저장되기 위해서 필요한 바이트 수 Throws
- `ArrayIndexOutOfBoundsException` - 배열의 범위를 벗어나는 색인을 가진 pixels 배열의 요소에 접근하려고 시도하는 경우
- `NullPointerException` - pixels가 null인 경우 setPixels
- `public` - void setPixels(int x, int y, int w, int h, byte[] pixels, int offset, int bpl) 화면이나 이미지에서 특정 부분의 픽셀 값들을 동시에 지정한다. Graphic와 연결된 화면이나 이미지의 특정 부분의 픽셀 값들을 동시에 지정한다. 이때 픽셀의
- `data타입은` - 기기마다 다르며, getPixel에서 지정하는 데이타 타입과 동일하게 된다. 이 함수는 클리핑 함수에 영향을 받는다.

**매개 변수**

- `x` - 가져올 픽셀 영역의 x축 좌표
- `y` - 가져올 픽셀 영역의 y축 좌표
- `w` - 가져올 픽셀 영역의 폭
- `h` - 가져올 픽셀 영역의 높이
- `pixels` - 픽셀이 저장될 어레이
- `offset` - 픽셀이 저장되기 시작할 위치
- `bpl` - 한 줄의 이미지가 저장되기 위해서 필요한 바이트 수 Throws
- `ArrayIndexOutOfBoundsException` - 배열의 범위를 벗어나는 색인을 가진 pixels 배열의 요소에 접근하려고 시도하는 경우
- `NullPointerException` - pixels가 null인 경우 setRGBPixels
- `public` - void setRGBPixels(int x,int y,int w,int h, int[] pixels,int offset, int bpl) 화면이나 이미지에서 특정 부분의 픽셀 값들을 동시에 지정한다. Graphic와 연결된 화면이나 이미지의 특정 부분의 픽셀 값들을 동시에 지정한다. 이때 픽셀의
- `data타입은` - 0x00RRGGBB로 각각 한 integer에 저장한다.

**매개 변수**

- `x` - 가져올 픽셀 영역의 x축 좌표
- `y` - 가져올 픽셀 영역의 y축 좌표
- `w` - 가져올 픽셀 영역의 폭
- `h` - 가져올 픽셀 영역의 높이
- `pixels` - 픽셀이 저장될 어레이
- `offset` - 픽셀이 저장되기 시작할 위치
- `bpl` - 한 줄의 이미지가 저장되기 위해서 필요한 바이트 수 Throws
- `ArrayIndexOutOfBoundsException` - 배열의 범위를 벗어나는 색인을 가진 pixels 배열의 요소에 접근하려고 시도하는 경우
- `NullPointerException` - pixels가 null인 경우
- `IllegalArgumentException` - 대상 영역의 일부가 Graphics의 범위를 벗어나는 경우 또는 w, h가 음수인 경우 이 함수는 클리핑 함수에 영향을 받다. copyArea
- `public` - void copyArea(int dx,int dy,int sx,int sy,int w,int h) 화면이나 이미지를 내부에서 내부로 복사한다. Graphics와 연결된 화면이나 이미지의 특정 부분을 복사한다.

**매개 변수**

- `dx` - 복사될 위치의 영역의 x축 좌표
- `dy` - 복사될 위치의 영역의 y축 좌표
- `sx` - 복사할 위치의 영역의 x축 좌표
- `sy` - 복사할 위치의 영역의 y축 좌표
- `w` - 복사할 영역의 폭
- `h` - 복사할 영역의 높이 drawPolygon
- `public` - void drawPolygon(int[] x,int[] y) 다각형을 그린다. 지정된 (x, y)점들로 다각형을 그린다.

**매개 변수**

- `x` - 그릴 다각형의 x축 array
- `y` - 그릴 다각형의 y축 array Throws
- `IllegalArgumentException` - x와 y 의 어레이 크기가 다른 경우
- `NullPointerException` - x나 y가 null 인 경우 reset
- `public` - void reset() 그래픽이 가지고 있는 모든 내용을 초기화 한다. 스타일, 클리핑 영역, 좌표체계의 원점, 색상 폰트를 초기화 한다. setAlpha
- `public` - void setAlpha(int alpha) 모든 그래픽 오퍼레이션의 투명 정도를 지정한다. alpha값이 0인 경우에는 투명하게 되고, 255값인 경우에는 화면에 그대로 출력된다. 0 에서 255 범위 이외의 값인 경우에는 255로 간주한다. 투명정도를 지정하면 더 이상 XOR모드로 그림이 그려지지 않는다.

**매개 변수**

- `alpha` - 지정할 투명 정도 getAlpha
- `public` - int getAlpha()
- `alpha값을` - 가져온다.

**반환 값**

지정된 alpha값 setXORMode public void setXORMode(boolean b) XOR모드로 그리도록 한다. drawLine, drawPolygon시에 XOR로 화면에 그려준다. XOR모드로 변경하게 되면 더 이상 투명(alpha)으로 그려지지 않으며 모든 그리기 연산에 적용된다.

**매개 변수**

- `b` - true XOR모드로 그림. false면 일반적으로 그려줌. isXORMode
- `public` - boolean isXORMode() 설정된XOR모드를 반환한다

**반환 값**

XOR 모드가 설정되어 있으면 true. encodeImage public byte[] encodeImage(int x,int y,int w,int h) 화면의 특정 영역을 BMP 포맷으로 인코딩한다. 인코딩된 BMP 포맷은 바이트 어레이로 반환되며 파일로 저장하거나 다시 이미지 생성에 이용할 수도 있다.

**매개 변수**

- `x` - 인코딩할 영역의 시작 x 좌표
- `y` - 인코딩할 영역의 시작 y 좌표
- `w` - 인코딩할 영역의 폭
- `h` - 인코딩할 영역의 높이 Throws
- `IllegalArgumentException` - 대상 영역의 일부가 Graphics의 범위를 벗어나는 경우 또는 w, h가 음수인 경우

**반환 값**

인코딩된 BMP 포맷의 바이트어레이, 인코딩에 실패하면 null Class Image java.lang.Object | +--org.kwis.msp.lcdui.Image public class Image extends Object 이미지를 나타내는 클래스이다. 이미지 클래스는 gif나 png등의 여러 가지 이미지 포맷의 데이타로 부터 생성할 수 있으며, 이전에 있는 이미지로부터 복사하여 생성할 수도 있다. 이때 복사된 이미지에 한하여 getGraphics로 이미지의 내용의 변경이 가능하다. 이미지는 변경이 가능한 이미지 변경이 가능하지 않은 이미지로 분류된다. 변경이 가능한 이미지는 주로 프로그램에서 임의적으로 만드는 이미지 이며, 이미지 파일로부터 생성하는 이미지는 변경이 가능하지 않은 이미지 이다. 복사할 때에 애니메이션 이미지인 경우에는 이미지 복사가 되지 않으며, mask된 이미지인 경우에 mask부분이 흰색으로 변환되어 복사되며, 복사된 이미지는 더 이상 mask를 가지고 있지 않다. 현재 이미지는 gif(animated), png, bmp(RLE압축포함) 포맷을 지원한다. Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 필드 상세 설명 TRAN_ROT90 public static final int TRAN_ROT90 이미지를 오른쪽으로 90도 회전시키는 상수. 90으로 지정되어 있다. TRAN_ROT180 public static final int TRAN_ROT180 이미지를 오른쪽으로 180도 회전시키는 상수. 180으로 지정되어 있다. TRAN_ROT270 public static final int TRAN_ROT270 이미지를 오른쪽으로 270도 회전시키는 상수. 270으로 지정되어 있다. TRAN_MIR public static final int MIR 이미지 좌우 미러링을 나타내는 상수. -99으로 지정되어 있다. TRAN_MIR_ROT90 public static final int TRAN_MIR_ROT90 이미지를 좌우 미러링 후 오른쪽으로 90도 회전시키는 상수. -90으로 지정되어 있다. TRAN_MIR_ROT180 public static final int TRAN_MIR_ROT180 이미지를 좌우 미러링 후 오른쪽으로 180도 회전시키는 상수. -180으로 지정되어 있다. TRAN_MIR_ROT270 public static final int TRAN_MIR_ROT270 이미지를 좌우 미러링 후 오른쪽으로 180도 회전시키는 상수. -270으로 지정되어 있다. 생성자 상세 설명 Image protected Image() 메쏘드 상세 설명 createImage public static Image createImage(byte[] imagedata,int imageoffset, int imagelength) 지정된 이미지 데이타 어레이로 부터 이미지를 생성한다. 이미지 데이타가 지정하는 바이트 어레이의 imageoffset부터 imagelength까지의 내용으로 이미지를 생성한다. 이때 data의 내용은 각 플랫폼마다 다를 수 있다. imageoffset 이 0보다 작거나 imagedata의 길이 - 1 보다 큰 경우, imagelength가 0보다 작은 경우, imageoffset + imagelength 가 imagedata의 길이보다 큰 경우에 ArrayIndexOutOtBoundsException이 발생하고, imagelength가 0인 경우는 IllegalArgumentException이 발생한다. 이 함수로 생성된 이미지는 편집이 불가능하다.

**매개 변수**

- `imagedata` - 이미지 자료를 가지고 있는 어레이
- `imageoffset` - 어레이의 시작점
- `imagelength` - 이미지 자료의 길이

**반환 값**

생성된 이미지 Throws IllegalArgumentException 제대로 된 형식의 데이타가 아닌 경우 NullPointerException imagedata가 null인 경우. ArrayIndexOutOfBoundsException imageoffset와 imagelength가 지정하는 영역이 어레이의 유효한 영역을 벗어 날 때 loadImage public static Image loadImage(String str,ImageObserver io) 문자열이 지정하는 자료로 부터 이미지를 읽어들이다. 지정된 문자열은 해당 리소스의 경로명이다. 이 리소스로부터 자료를 읽어 들여 이미지를 생성한다. 이미지 생성하는 시점은 이 함수를 부르고 난 후 일정 시간 이후에 생성된다. 완성되는 시점에 ImageObserver의 notify 함수를 불러준다. 이 함수를 통해서 돌려진 이미지는 처음에는 아무런 내용이 없으며, 폭과 높이는 각각 0이 되고, 실제 이미지가 완성된 후(ImageObserver.notify가 불린 후)에야 제대로 된 폭과 높이를 얻어 올 수 있다. 한 이미지에 대해서는 하나의 ImageObserver만이 가능한다. 이 함수로 생성된 이미지는 편집이 불가능하다.

**매개 변수**

- `str` - 자료의 경로명을 지정하는 문자열
- `io` - 이미지 생성을 알려줄 ImageObserver

**반환 값**

새로 생성된 이미지; 초기에는 아무런 내용이 없음 Throws NullPointerException str이 null인 경우.

**참고 항목**

ImageObserver.notify(org.kwis.msp.lcdui.Image, int)

#### createImage

public static Image createImage(Image image) 지정된 이미지를 복사해서 다른 편집이 가능한 이미지를 생성한다. 이미지의 내용을 복사해서 다른 편집이 가능한 이미지를 생성한다. 이 이미지로부터 getGraphics()를 통해서 Graphics 개체를 가져온 후에 이미지를 편집할 수 있다. 단 Animation 이미지는 각 프레임이 존재하기 때문에 이미지를 복사할 수 없으므로 이 경우에는 IllegalArgumentException을 던져준다. 이 함수로 생성된 이미지는 편집 가능한다.

**매개 변수**

- `image` - 복사할 이미지

**반환 값**

새로 만들어진 이미지 Throws IllegalArgumentException 넘겨진 이미지가 animation인 경우 NullPointerException image가 null인 경우. createImage public static Image createImage(int width,int height) 지정된 높이와 폭의 편집 가능한 이미지를 생성한다. 이 이미지는 초기에 흰색으로 초기화 되어있다. 또한 getGraphics()함수를 통해서 Graphics 객체를 얻어 와서 이 객체를 통해 이미지 편집이 가능한다. 이 함수로 생성된 이미지는 편집 가능하다.

**매개 변수**

- `width` - 이미지의 폭.
- `height` - 이미지의 높이. Throws
- `IllegalArgumentException` - width와 height가 0이하인 경우 createImage
- `public` - static Image createImage(String name) throws IOException 지정된 리소스의 이미지를 생성한다. 클래스를 로드한 곳에서 지정된 경로명의 자원을 로드하여, 이미지로 만들어서 돌려준다. 이 함수로 생성된 이미지는 편집이 불가능하다.

**매개 변수**

- `name` - 자원 경로명

**반환 값**

이미지 Throws IllegalArugmentException 만일 이미지가 잘못된 포맷이거나 자원이 존재하지 않는 경우 NullPointerException name이 null인 경우.

**참고 항목**

Class.getResourceAsStream(java.lang.String)

#### getGraphics

public Graphics getGraphics() 이미지에 그릴 수 있는 그래픽을 돌려준다. 편집 가능한 이미지에 대해서 Graphics객체를 얻어 온다. 만일 편집 가능하지 않은 이미지라면 null을 돌려준다.

**반환 값**

이미지의 Graphics객체 getHeight public int getHeight() 이미지의 높이를 돌려준다.

**반환 값**

이미지의 높이 getWidth public int getWidth() 이미지의 폭을 돌려준다.

**반환 값**

이미지의 높이 isMutable public boolean isMutable() 이미지의 편집 가능 여부를 돌려준다.

**반환 값**

편집 가능한지의 여부 isAnimated public boolean isAnimated() Image가 Animation이 가능한지 여부를 돌려준다.

**반환 값**

Animation이 가능한지의 여부 play public void play(ImageObserver ob) 이미지의 움직임을 시작한다. 이미지가 Animation 이미지인 경우에 이 함수가 사용될 수 있다. Animation이 진행되는 동안 ImageObserver에 animation 진행 상황을 ImageObserver의 notify()함수를 호출함으로써 알려준다. Animation 이미지가 아닌 경우에 이 함수는 아무런 작업도 하지 않는다. 이 함수는 상당히 많은 computing시간을 요구한다. 새로운 프레임을 만들 때 마다, 이미지를 decode하기 때문이다. 또한 animation 이미지를 위해서 내부에 이미지 원본 내용을 그대로 저장하고 있기 때문에 메모리를 상당히 소모한다. 이 함수를 호출하고 나서 stop함수를 꼭 호출하도록 해야 한다. 그래야 메모리와 속도를 늘릴 수 있다. ob가 null일때 loadImage()에서 등록한 ImageObserver를 사용한다. 만약, loadImage()에서 등록한 ImageObserver와 ob가 다르면, 지금의 ob를 사용한다.

**매개 변수**

- `ob` - 이미지 Observer

**참고 항목**

ImageObserver

#### stop

public void stop() 애니메이션을 중지시킨다. 애니메이션을 멈춘다. 이미지가 Animation Gif와 같은 이미지인 경우에 이 함수가 사용될 수 있다. Animation 이미지가 아닌 경우에 아무런 작업도 하지 않는다. 이미지를 더 이상 사용하지 않으면 이 함수를 불러서 이미지의 레퍼런스를 없애야 한다. 그렇지 않으면, 사용하지 않은 이미지 레퍼런스를 가지게 되므로, 메모리를 낭비할 수 있다.

#### stopImage

public static void stopImage(ImageObserver io) ImageObserver에 대응하는 이미지를 읽기를 중단 시킨다. loadImage나 play로 "이미지 읽기 큐"에 쌓인 작업을 삭제한다. 삭제된 후에는 ImageObserver.notify는 더 이상 불리지 않는다. 응용 프로그램이 play함수로 애니메이션 이미지를 의 애니메이션을 시작하였다면, stop함수나 이 함수로 반드시 정지 시켜야 한다. 그렇지 않으면 내부적으로 계속 이미지 디코딩이 일어나므로 CPU 수행 시간과 메모리를 낭비하게 된다. io가 null이면 함수는 아무런 일도 하지 않는다.

**매개 변수**

- `io` - 삭제할 이미지에 대응하는 ImageObserver drawImage
- `public` - void drawImage(Image img, int srcX, int srcY, int srcWidth,
- `int` - srcHeight, int destX, int destY, int transform, int anchor)
- `img가` - 가리키는 이미지의 부분을 Rotate/Flip 변환 하여 지정된 위치에 그려준다. 변환은 <표 3-1-1-2>와 같이 이루어진다. <표 3-1-1-2> 변환관련 상수 설명
- `TRAN_ROT90` - 오른쪽으로 90도 회전
- `TRAN_ROT180` - 오른쪽으로 180도 회전
- `TRAN_ROT270` - 오른쪽으로 270도 회전
- `TRAN_MIR` - 좌우 미러링
- `TRAN_MIR_ROT90` - 좌우 미러링 후 오른쪽으로 90도 회전
- `TRAN_MIR_ROT180` - 좌우 미러링 후 오른쪽으로 180도 회전
- `TRAN_MIR_ROT270` - 좌우 미러링 후 오른쪽으로 270도 회전

**매개 변수**

- `img` - 원본 이미지 srcX,srcY 서브이미지의 (0,0)이 될 원본이미지의 좌표 srcWidth,srcHeight 서브이미지의 넓이 및 높이 destX,destY 앵커 포인트의 x,y축 좌표
- `transform` - 변환 방식을 지정
- `anchor` - 텍스트의 앵커 위치; 앵커를 참조 Throws
- `IllegalArgumentException` - anchor값이 유효한 값이 아닌 경우
- `NullPointerException` - img가 null인 경우

**참고 항목**

Image

#### createSubImage

public Image createSubImage(int x, int y, int width, int height, boolean bMutable); 서브이미지를 생성한다.

**매개 변수**

x,y 서브이미지의 (0,0)이 될 원본이미지의 좌표
width,height 서브이미지의 넓이 및 높이
- `bMutable` - 생성할 이미지를 편집가능하게 할려면 1, 아니면 0을 지정한다. Throws
- `IllegalArgumentException` - x,y,width,height가 원본이미지의 범위는 벗어난 경우

**참고 항목**

Image

#### setTransparentColor

public void setTransparentColor(int rgb); 지정한 색을 투명색으로 설정한다.

**매개 변수**

- `rgb` - 투명색으로 지정할 색. 이미지가 256색 이상을 지원하는 경우에 사용에 주의하여야 함

**참고 항목**

Image Class AnimateImage java.lang.Object | +--org.kwis.msp.lcdui.AnimateImage 이미지 중에 Animate를 지원하는 이미지가 있다. 이를 위해 Image와 다른 AnimateImage클래스를 추가한다. 지원하는 이미지는 SIS, GIF 등이 될 수 있으며 지원되는 포멧은 옵션 사항이다. 이와 더불어 Animated 타입이 아닌 image를 조합하여 필요한 Animated 효과를 구현하게 할 수 있다. 생성자 상세 설명

#### 생성자 없음

메쏘드 상세 설명

#### createAnimateImage

public static AnimateImage createAnimateImage (String imageName, boolean loaded) throws java.io.IOException Classpath에서 접근할 수 있는 Animate 이미지를 로딩하여 Animate Image를 생성한다. 이 함수로 생성된 이미지는 편집이 불가능하다.

**매개 변수**

- `imageName` - 로딩할 파일 이름
- `loaded` - AnimateImage 생성시 모든 프레임의 이미지를 디코딩 할 지를 설정한다. true 이면 모든 프레임이 이미지를 디코딩 해 두며, false면 디코딩 하지 않는다. Throws
- `NullPointerException` - name이 null일때 createAnimateImage
- `public` - static AnimateImage createAnimateImage(int frameNumber, int width, int height) 지정한 프레임 수와 가로, 세로의 크기를 갖는 Animated Image를 생성한다. 이 함수로 생성된 이미지는 편집이 가능하다.

**매개 변수**

- `frameNumber` - 프레임의 개수
- `width` - 생성할 이미지의 넓이
- `height` - 생성할 이미지의 높이 Throws
- `IllegalArgumentException` - 파라메터가 0이하 이거나 적절한 범위를 벗어나는 경우 isMutable
- `public` - boolean isMutable() 이미지의 편집 가능 여부를 돌려준다.

**반환 값**

편집 가능한지의 여부 setAnimationRate public void setAnimationRate(int delay, int n) n과 n+1 프레임 사이의 에니메이션 지연 시간을 설정한다. n이 0보다 작거나 getMaxFrame()보다 같거나 큰 경우에는 설정되지 않는다.

**매개 변수**

- `delay` - Frame간의 지연 시간을 설정한다. 밀리 세컨드 단위
- `n` - 지연 시간을 설정할 프레임을 지정한다. 즉, n과 n+1 프레임 사이의 지연 시간이 설정된다. Throws
- `IllegalArgumentException` - n이 0보다 작거나 getMaxFrame() 보다 크거나 같은 경우, 또는 immutable image 인 경우, 반복 설정이 되어 있지 않고 n이 마지막 frame( getMaxFrame() - 1 )일 경우 getAnimationRate
- `public` - int getAnimationRate()
- `Animation의` - 속도를 반환한다.

**반환 값**

첫번째와 두번째 프레임 사이의 지연시간을 반환한다. 밀리 세컨드 단위 public int getAnimationRate(int n) Animation의 속도를 반환한다.

**반환 값**

n과 n+1 프레임 사이의 지연 시간을 반환한다. 밀리 세컨드 단위 n 값이 마지막 frame (getMaxFrame()-1)을 나타내면 loop animation 시에 마지막 frame과 첫 frame의 지연 시간을 반환한다. Throws IllegalArgumentException n이 0보다 작거나 getMaxFrame() 보다 크거나 같은 경우, 반복 설정이 되어 있지 않고 n이 마지막 frame( getMaxFrame() - 1 )일 경우 getMaxFrame public int getMaxFrame()

**반환 값**

해당 AnimateImage의 최대 Frame수를 반환한다. getWidth public int getWidth() 이미지 프레임의 width를 얻어온다.

**반환 값**

프레임의 width getHeight public int getHeight() 이미지 프레임의 height를 얻어온다.

**반환 값**

프레임의 height getFrameImage public Image getFrameImage(int frame) 원하는 프레임의 Image로 반환한다.

**반환 값**

디코딩 과정에서 에러가 발생했을 때 또는 immutable 이미지 일 때 null을 반환한다. Throws IllegalArgumentException frame값이 0보다 작거나 getMaxFrame() 보다 크거나 같을 때 발생 setFrameImage public void setFrameImage(Image im, int frame) mutable의 이미지를 해당 Frame에 삽입한다.

**매개 변수**

- `im` - 삽입할 Image
- `frame` - 삽입될 Frame 번호, 0<=frame<getMaxFrame() Throws
- `IllegalArgumentException` - 삽입할 이미지의 크기와 AnimateImage의 크기와 다를 때와 frame이 0보다 작거나 getMaxFrame()보다 크거나 같을 때, immutable image 일 때 발생한다. play
- `public` - void play(org.kwis.msp.lcdui.Graphics g, int x, int y, int anchor,ImageObserver ob) 이미지의 움직임을 시작한다. Animation이 진행되는 동안 ImageObserver에 animation 진행 상황을 ImageObserver의 notify()함수를 호출함으로써 알려준다. 실제 화면에 보려주려면 ImageObserver에서 repaint()를 호출해 주어야 한다. 이 함수를 호출하고 나서 stop함수를 꼭 호출하여야 한다. 이 API는 non-blocking으로 동작한다. Frame
- `Image가` - 하나도 없을 경우 play 되지 않는다. 중간에 빠진 frame이 있으면 출력하지 않고 delay만 적용 시킨다. Delay가 설정되어 있지 않은 frame은 기본 delay 값을 500 millisecond로 설정한다.

**매개 변수**

- `g` - 그려질 graphics
- `x` - 앵커 포인트의 x축 좌표
- `y` - 앵커 포인트의 y축 좌표
- `anchor` - 텍스트의 앵커 위치; 앵커를 참조
- `ob` - 이미지 Observer Throws
- `NullPointerException` - Graphics가 null 일 경우 발생 play
- `public` - void play(mageObserver ob) 이미지의 움직임을 시작한다. Animation이 진행되는 동안 ImageObserver에 animation 진행 상황을 ImageObserver의 notify()함수를 호출함으로써 알려준다. 실제 화면에 보려주려면 ImageObserver에서 repaint()를 호출해 주어야 한다. 이 함수를 호출하고 나서 stop함수를 꼭 호출하여야 한다. 이 API는 non-blocking으로 동작한다. Frame
- `Image가` - 하나도 없을 경우 play 되지 않는다. 중간에 빠진 frame이 있으면 출력하지 않고 delay만 적용 시킨다. Delay가 설정되어 있지 않은 frame은 기본 delay 값을 500 millisecond로 설정한다.

**매개 변수**

- `ob` - 이미지 Observer stop
- `public` - void stop() 애니메이션을 중지시킨다. 이미지를 더이상 사용하지 않으면 이 함수를 불러서 이미지의 레퍼런스를 없애야 한다. 그렇지 않으면, 사용하지 않은 이미지 레퍼런스를 가지게 되므로, 메모리를 낭비할 수 있다. stopImage
- `public` - static void stopImage(ImageObserver io)
- `ImageObserver에` - 대응하는 이미지를 읽기를 중단 시킨다. play로 "이미지 읽기 큐"에 쌓인 작업을 삭제한다. 삭제된 후에는 ImageObserver.notify는 더이상 불리지 않는다. 응용 프로그램이 play함수로 애니메이션 이미지를 의 애니메이션을 시작하였다면,
- `stop함수나` - 이 함수로 반드시 정지 시켜야한다. 그렇지 않으면 내부적으로 계속 이미지 디코딩이 일어나므로 CPU 수행 시간과 메모리를 낭비하게 된다. io가
- `null이면` - 함수는 아무런 일도 하지 않는다.

**매개 변수**

- `io` - 삭제할 이미지에 대응하는 ImageObserver paintFrame
- `public` - boolean paintFrame(Graphics g, int frame, int x, int y)
- `frame에` - 해당하는 프레임을 Graphics 객체의 x, y 위치에 그린다.

**매개 변수**

- `g` - 그려질 graphics
- `frame` - 그려질 frame 번호
- `x` - 그려질 x축 좌표
- `y` - 그려질 y축 좌표

**반환 값**

true 정상적으로 화면에 출력되었을 경우 false play() 중에 이 함수가 호출 되었을 경우 화면에 출력 되지 않을 때 Throws NullPointerException g가 null일 때에 IllegalArgumentException 0 <= frame < getMaxFrame() 의 범위를 벗어날 때 setRepeat public boolean setRepeat(Boolean isRepeat) 에니메이션이 반복여부를 설정한다. 기본 값은 false 이다.

**매개 변수**

- `isRepeat` - true면 영원히 반복, false면 한번만 animate된다.

**반환 값**

true 정상적으로 반복 여부가 설정되었을 경우 false play() 중에 이 함수가 호출 되었을 경우 immutable 이미지일 경우 설정 값은 무시되 며 false를 반환 isRepeat public boolean isRepeat() AnimationImage의 반복 여부를 알아낸다.

**반환 값**

반복되는 것이면 true, 한번만 play되는 것이면 false이다. getImageType public String getImageType() AnimateImage의 타입을 알아낸다.

**반환 값**

AnimateImage의 타입을 알아낸다. AnimationImage의 타입은 MIME으로 표시한다. 예를 들어, GIF이미지의 경우, “anim/gif”가 될 것이고, SIS의 경우, “anim/sis”가 될 것이다. mutable 이미지인 경우 null이 반환된다. Class InputMethodHandler java.lang.Object | +--org.kwis.msp.lcdui.InputMethodHandler public class InputMethodHandler extends Object InputMethodHandler는 사용자 키 입력에 따른 문자처리를 담당하고 있다. 사용자의 키 입력을 처리하는 메소드는 notifyKeyInput(int keyCode)이다. 따라서 이 메소드를 호출하여 현재 입력된 키 값을 넘겨줘야 한다. 또한 키 입력에 따라 처리된 문자를 전달 받기 위해서 반드시 구현된 특정 InputMethodListener를 지정해야 한다. 지정된 InputMethodListener가 존재하지 않은 경우 notifyKeyInput(int)에서 false를 반환하고 아무런 일을 하지 않는다. InputMethodListener는 setInputMethodListener(org.kwis.msp.lcdui.InputMethodListener)를 통해 지정할 수 있다. Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait . 생성자 상세 설명 InputMethodHandler public InputMethodHandler(int constraint) 주어진 입력제한자로 InputMethodHandler의 인스턴스를 생성한다. 입력제한자는 TextComponent 서 정의한 값을 받게 되고, 입력 제한자에 따라 현재 오토마타에서 지원하는 모드들 중 입력 가능한 모드가 결정된다. Throws IllegalArgumentException 입력 제한자 값이 잘못된 경우. 메쏘드 상세 설명 getCurrentModeCode public String getCurrentModeCode() 현재 입력모드에 해당하는 표준언어코드를 얻어온다. 표준언어코드는 ISO 639에서 지정한 코드이다 언어가 대소문자를 구분하는 경우 각 코드에 "/S"나 "/L" 이 추가될 수도 있다. 예를 들어 영문자의 표준언어코드는 "EN"이고, 영소문자는 "EN/S"의 코드값을 가지게 된다.

**반환 값**

입력모드에 해당하는 언어코드 notifyKeyInput public final boolean notifyKeyInput(int keyCode,int type) InputMEthodHandler에서 키 입력을 처리해야 하는 경우 호출된다. 현재 문자입력모드에 따라 입력 키 값에 해당하는 문자를 처리하고 setInputMethodListener(org.kwis.msp.lcdui.InputMethodListener)메소드를 통해 등록된 InputMethodListener의 notifyTextChanged를 호출한다.

**매개 변수**

- `ekyCode` - 입력키값

**반환 값**

키 입력에 따른 문자 처리가 이루어진 경우 true, 그 외의 경우 false 반환. setInputMethodListener public void setInputMethodListener(InputMethodListener imListener) InputMethodHandler에서 키 입력에 따라 처리한 문자를 전달할 InputMethodListener를 지정한다. 여기서 지정된 InputMethodListener의 notifyTextChanged를 호출하여 입력 처리된 문자를 전달하게 된다. 따라서 키 입력에 따라 처리된 문자를 전달 받기 위해서 반드시 특정 InputMethodListener를 지정해야 한다. null값을 지정하는 경우 현재 등록된 InputMethodListener를 제거한다.

**매개 변수**

- `imListener` - InputMethodListener 혹은 null changeCurrentModeToNext
- `public` - void changeCurrentModeToNext() 현재 지정된 constraint에 따라 현재 입력모드를 기준으로 다음 입력 모드를 계산하여 현재 입력모드를 계산된 다음 입력모드로 변경한다. getCurrentMode
- `public` - int getCurrentMode () 현재 입력 모드를 얻어온다.

**반환 값**

입력모드 값 setCurrentMode public boolean setCurrentMode(int mode) 주어진 모드 값으로 현재 입력모드를 지정한다. 주어진 모드 값이 오토마타에서 지원하지 않는 모드인 경우 IllegalArgumentException이 발생한다.

**매개 변수**

- `Mode` - 새로 지정할 입력모드 값 Throws
- `IllegalArgumentException` - 주어진 모드값이 오토마타에서 지원하지 않는 모드일 경우 hideSymbolCard
- `public` - void hideSymbolCard() 현재 화면에서 CandidateWindow를 제거한다. setSymbolPosition
- `public` - void setSymbolPosition(int x,int y,int w, int h)
- `InputMethodHandler의` - 현재 입력 모드가 IM_SYMBOL 경우 화면에 특수문자카드를 출력할 위치와 넓이, 높이를 설정한다. 이때 x,y,w,h값은 '0'이하 값이 될 수 없고, '0'이하 값이 지정된 경우 IllegalArgumentException이 발생한다.

**매개 변수**

- `x` - x좌표 값.
- `y` - y좌표 값.
- `w` - width값
- `h` - height값. Throws
- `IllegalArgumentException` - x, y, w, h값이 '0'이하값인 경우
- `Class` - Jlet java.lang.Object | +--org.kwis.msp.lcdui.Jlet
- `public` - abstract class Jlet extends Object
- `MSP` - 응용 프로그램이다.
- `MSP를` - 이용하는 모든 응용 프로그램은 Jlet을 상속받아서 작성되어야 한다. MSP에서의 자원들은 모두 Jlet단위로 응용 프로그램의 자원이 관리된다. MSP에서 생성한 Thread와
- `Card들은` - Jlet이 종료될 때 시스템에서 사라 진다.
- `Jlet은` - 세 가지 상태를 가진다. Jlet을 생성 시키면 자동적으로 active상태가 되고, 응용프로그램 관리자에서 프로그램을 일시 정지하거나 프로그램이 사용자에 의해서 일시 정지시켜야 하는 경우에는 pause상태가 된다. 이 상태에서 응용프로그램 관리자나 사용자에 의해서 다시 active상태로 돌아 올 수 있다. 어떠한 상태던지 Jlet은 destroyed상태로 전이할 수 있으며, 이 때에는 Jlet은 프로그램을 종료해야 한다. 프로그램은 전이하는 상태에서 [그림 3-1-1-1]과 같이 각각 pauseApp()와 resumeApp(), startApp(), destroyApp() 함수가 불린다. [그림 3-1-1-1] Jlet 상태 전이 관계 프로그램을 처음에 startApp함수가 불린다. 이때에는 파라미터로 System.execute함수 호출 시 넘긴 파라미터가 넘어 온다.
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 필드 상세 설명 ACTIVE
- `public` - static final int ACTIVE DESTROYED
- `public` - static final int DESTROYED PAUSED
- `public` - static final int PAUSED 생성자 상세 설명 Jlet
- `protected` - Jlet() 새로운 Jlet을 생성한다. 메쏘드 상세 설명 setActiveJlet
- `public` - static void setActiveJlet(Jlet ql) 지정된 Jlet을 활성화 시킨다. 지정된 Jlet을 활성화 시킨다. getActiveJlet
- `public` - static Jlet getActiveJlet() 현재 활성화된 Jlet를 얻어 온다. 활성화된 Jlet이 없는 경우에는 null을 돌려준다.

**반환 값**

현재 상위에서 수행 중에 있는 Jlet getJletFromPID public static Jlet getJletFromPID(int id) 주어진id에 해당하는 Jlet를 얻어 온다. 주어진 Jlet이 없거나 잘못된 ID인 경우 경우에는 null을 돌려준다.

**반환 값**

ID에 해당하는 Jlet getCurrentJlet public static Jlet getCurrentJlet() 현재 수행중인 Jlet을 얻어 온다.

**반환 값**

현재 수행중인 Jlet getCurrentProgramID public int getCurrentProgramID() Jlet을 생성한 프로그램 id를 돌려준다. 프로그램 id는 시스템에서 지정한 유일한 정수가 된다.

**매개 변수**

- `id` - Jlet을 생성한 프로그램 id startApp
- `protected` - abstract void startApp(String[] args) 프로그램이 시작될 때 불려진다. 초기에 Jlet 생성되고 나서 이 함수가 불린다. 이 함수에서 필요한 시스템 자원을 할당하고, 화면에 카드를 넣을 수 있다. 이 함수는 수행 중에 단 한번만 불린다. Jlet에게 넘겨지는 인수가 args로 넘어 온다. 이때 args[0]은 Jlet 이름이 되고, args[1]부터 사용자가 넘겨주는 인수가 된다.

**매개 변수**

- `args` - 사용자가 넘기는 인수. pauseApp
- `protected` - void pauseApp() 프로그램을 정지하려고 하는 때 불려진다. 시스템에서 응용 프로그램에게 일시 정지를 요청할 때 이 함수를 부른다. 프로그램은 사용자의 인터렉션에 의해서 정지할 수도 있다. 정지하는 경우에 사용하고 있던 시스템 자원(네트웍, 시리얼 등)을 되돌려 줄 수 잇도록 구현해야 한다. resumeApp
- `protected` - void resumeApp() 정지된 프로그램을 다시 수행을 재개하려 할 때 불려진다. 시스템에서 응용 프로그램에게 수행 재기를 요청할 때 이 함수를 부른다. pauseApp함수로 정지했던
- `Jlet를` - 다시 기동시키며, 이 함수 내에서 pauseApp에서 돌려주었던 시스템 자원들(네트웍, 시리얼 등)을 다시 할당 받도록 함수를 구현해야 한다. destroyApp
- `protected` - abstract void destroyApp(boolean unconditional)
- `throws` - org.kwis.msp.lcdui.JletStateChangeException 프로그램이 종료 됨을 알려주는 함수이다. 프로그램이 어떤 상태이던, 이 함수를 불리면 프로그램이 종료 된다. 만일 unconditaional이 true를 주면, 프로그램은 무조건 종료해야 한다. false를 주면 프로그램은 상황에 따라서 JletStateChangeException 예외를 던짐으로써 프로그램이 종료되는 것을 막을 수가 있다. 이 함수에는 프로그램이 할당한 모든 자원을 시스템에게 돌려주고, 주요한 자료를 저장해야한다. 만일 이 함수 내에서 무한 루프를 돌면 종료되지 않은 상태가 될 수 있으므로 유의하십시오.

**매개 변수**

- `unconditonal` - 만일 true이면 프로그램이 무조건 종료가 되고, false일때에는
- `Jlet은` - JletStateChangeException을 던져서 프로그램 종료를 막을 수 있음 Throws org.kwis.msp.lcdui.JletStateChangeException 현재 상태에서 프로그램을 종료할 수 없는 경우. 만일
- `unconditional이` - true이면, 이 예외를 던진다 해도, 프로그램은 종료된다. notifyDestroyed
- `public` - final void notifyDestroyed() 프로그램을 종료 시킬 때 사용되는 함수. Jlet응용 프로그램을 종료할 때 이 함수를 부른다. 이 함수를 부르면 프로그램은 Destroyed상태로 들어가며, 차후에
- `destroyApp메쏘드를` - 호출한다. Jlet.destroyApp()를 호출함으로써 프로그램이 가지고 있는 모든 자원을 되돌려 준다. getAppProperty
- `public` - final String getAppProperty(String key) 응용 프로그램마다 지정되어 있는 프라퍼티를 돌려준다. 해당하는 key에 대응하는 프라퍼티 문자열을 돌려준다. 만일 대응 하는 프라퍼티가 없다면 null를 돌려준다.

**매개 변수**

- `key` - 찾을 프라퍼티에 대응하는 키

**반환 값**

해당하는 프라퍼티 getEventQueue public final EventQueue getEventQueue() Jlet과 연결된 이벤트 큐를 돌려준다.

**반환 값**

이벤트 큐
