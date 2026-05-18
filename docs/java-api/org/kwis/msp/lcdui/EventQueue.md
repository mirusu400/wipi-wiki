# Class EventQueue

`package org.kwis.msp.lcdui`

```text
java.lang.Object
  |
  +--org.kwis.msp.lcdui.EventQueue
```

## 설명

**extends Object:**

시스템에서 발생하는 이벤트를 관리하는 큐 클래스입니다.

 응용 프로그램(`Jlet`) 하나에는 이벤트를 관리하는
 `EventQueue` 객체가
 하나 존재하게 됩니다.
 응용 프로그램에 발생한 모든 이벤트는 이 객체에 일단 저장하고.

 응용 프로그램은 발생한 이벤트를 하나씩 가져와서 적절히 처리하면,
 응용 프로그램이 동작합니다. `Jlet`안에는 이벤트를
 가져와서 처리하는 쓰레드가 내부에 존재 합니다.

이벤트를 가져오거나
 새로운 이벤트를 넣을 때에는 `EVENT_SIZE`가
 지정한 갯수 이상의 정수 어레이를 사용합니다.
 이 어레이에 들어가는 내용은 이벤트 타입에 따라서 다릅니다.

각 이벤트 타입에 따른 저장되는 내용은 다음과 같습니다.

event[0] event[1] event[2] event[3] KEY_EVENT KEY_PRESSED | KEY_RELEASED | KEY_REPEATED | KEY_TYPED 키 값(ITU키인 경우에는 ascii값이 아니면 음수) 0 POINTER_EVENT POINTER_PRESSED | POINTER_RELEASED | POINTER_DRAGGED 포인터의 화면상 x축 값 포인터의 화면상 y축 값 TIMER_EVENT 타이머 값

``Main``에서 `getNextEvent`와
 `dispatchEvent`를 무한히 수행하도록 되어 있으며, 그 수행 코드는
 다음과 같습니다.

```java
int event[] = new int[EventQueue.EVENT_SIZE]; 
 while(true){ 
   eq.getNextEvent(event); 
   eq.dispatchEvent(event); 
 }
```

키 코드는 시스템에 따라서 다릅니다. 그러나, ITU-키인 경우에는 '0'
 에서 부터 '9', '*', '#'가 들어오며, 그외에 아스키 코드값에
 대응되는 키가 들어오게 됩니다.

 파워키나 방향키와 같은 제어키는 음수값으로 들어 오며, 그
 값은 플랫폼마다 다를 수 있습니다. 플랫폼 마다 다른 제어키를
 처리하기 위헤서 `getGameAction`와 `getKeyCode`함수가
 존재 합니다. 특정 키가 들어 왔을때 어떤 제어키인지를
 알기 위해서 `getGameAction`함수를 사용합니다.
 물론 시스템에 따라서 숫자키가 제어키로 사용할 수도 있습니다.
 현재 `getGameAction`에 반대되는 함수인
 `getKeyCode`함수가 존재하게 됩니다.

## 필드 요약

- `static int ANN_EVENT` — 단말기 indicator Notify 이벤트 상수. 8로 지정되어 있습니다.
- `static int ANNUNCIATOR_CHANGE_EVENT` — 상위 지시자가 변경된 이벤트 상수. 103으로 지정되어 있습니다.
- `static int APP_ACTIVE` — 현재 Active된 프로그램을 자기 자신으로 변경합니다.
- `static int APP_DESTROY` — 응용프로그램 종료 이벤트; APP_EVENT 의 서브타입입니다. 3로 지정되어 있습니다.
- `static int APP_EVENT` — 응용 프로그램 이벤트 상수. 100으로 지정되어 있습니다.
- `static int APP_RESUME` — 응용프로그램 지속 이벤트; APP_EVENT 의 서브타입입니다. 2로 지정되어 있습니다.
- `static int APP_STOP` — 응용프로그램 정지 이벤트; APP_EVENT 의 서브타입입니다. 1로 지정되어 있습니다.
- `static int BATT_EVENT`
- `static int CALL_EVENT` — 단말기 Call Notify 이벤트 상수. 7로 지정되어 있습니다.
- `static int CALL_SERIALLY_EVENT` — 내부 call serially 이벤트 상수.
- `static int CHILDSTART_EVENT` — 하위 프로그램 시작 이벤트 상수. 101로 지정되어 있습니다.
- `static int CHILDSTOP_EVENT` — 하위 프로그램 종료 이벤트 상수. 102로 지정되어 있습니다.
- `static int CLEAR` — CLEAR 게임 키를 지정하는 상수. 99로 지정되어 있습니다.
- `static int DOWN` — DOWN 게임 키를 지정하는 상수. 6로 지정되어 있습니다.
- `static int EVENT_SIZE` — 이벤트 하나가 저장되는 단위크기. 4로 지정되어 있으며, getNextEvent 함수 호출시에 적어도 이 크기 이상의 정수 어레이를 넘겨야만 합니다.
- `static int FIRE` — FIRE 게임 키를 지정하는 상수. 8로 지정되어 있습니다.
- `static int GAME_A` — GAME_A 게임 키를 지정하는 상수. 9로 지정되어 있습니다.
- `static int GAME_B` — GAME_B 게임 키를 지정하는 상수. 10로 지정되어 있습니다.
- `static int GAME_C` — GAME_C 게임 키를 지정하는 상수. 11로 지정되어 있습니다.
- `static int GAME_D` — GAME_D 게임 키를 지정하는 상수. 12로 지정되어 있습니다.
- `static int KEY_EAR_PIECE`
- `static int KEY_EVENT` — 키 이벤트 상수. 1로 지정되어 있습니다.
- `static int KEY_NUM0` — ITU-T '0' 키를 지정하는 상수. 48('0')로 지정되어 있습니다.
- `static int KEY_NUM1` — ITU-T '1' 키를 지정하는 상수. 49('1')로 지정되어 있습니다.
- `static int KEY_NUM2` — ITU-T '2' 키를 지정하는 상수. 50('2')으로 지정되어 있습니다.
- `static int KEY_NUM3` — ITU-T '3' 키를 지정하는 상수. 51('3')로 지정되어 있습니다.
- `static int KEY_NUM4` — ITU-T '4' 키를 지정하는 상수. 52('4')로 지정되어 있습니다.
- `static int KEY_NUM5` — ITU-T '5' 키를 지정하는 상수. 53('5')으로 지정되어 있습니다.
- `static int KEY_NUM6` — ITU-T '6' 키를 지정하는 상수. 54('6')로 지정되어 있습니다.
- `static int KEY_NUM7` — ITU-T '7' 키를 지정하는 상수. 55('7')로 지정되어 있습니다.
- `static int KEY_NUM8` — ITU-T '8' 키를 지정하는 상수. 56('8')으로 지정되어 있습니다.
- `static int KEY_NUM9` — ITU-T '9' 키를 지정하는 상수. 57('9')로 지정되어 있습니다.
- `static int KEY_POUND` — ITU-T '#' 키를 지정하는 상수. 35('#')로 지정되어 있습니다.
- `static int KEY_PRESSED` — 키 누름 이벤트 타입 상수. 1로 지정되어 있습니다.
- `static int KEY_RELEASED` — 키 떼임 이벤트 타입 상수. 2로 지정되어 있습니다.
- `static int KEY_REPEATED` — 키 반복 이벤트 타입 상수. 3로 지정되어 있습니다.
- `static int KEY_SEND`
- `static int KEY_STAR` — ITU-T '*' 키를 지정하는 상수. 42('*')로 지정되어 있습니다.
- `static int KEY_TYPED` — 키 입력 이벤트 타입 상수. 4로 지정되어 있습니다.
- `static int LEFT` — LEFT 게임 키를 지정하는 상수. 2로 지정되어 있습니다.
- `static int MEDIA_EVENT`
- `static int POINT_DRAGGED` — 포인터 기기 드래그 이벤트 타입 상수. 5로 지정되어 있습니다.
- `static int POINT_PRESSED` — 포인터 기기 누름 이벤트 타입 상수. 1로 지정되어 있습니다.
- `static int POINT_RELEASED` — 포인터 기기 떼임 이벤트 타입 상수. 2로 지정되어 있습니다.
- `static int POINTER_EVENT` — 포인터 이벤트 상수. 2로 지정되어 있습니다.
- `static int REPAINT_EVENT`
- `static int RIGHT` — RIGHT 게임 키를 지정하는 상수. 5로 지정되어 있습니다.
- `static int RSSI_EVENT`
- `static int SIDE_DOWN` — SIDE_DOWN 게임 키를 지정하는 상수. 97로 지정되어 있습니다.
- `static int SIDE_SEL` — SIDE_SEL 게임 키를 지정하는 상수. 98로 지정되어 있습니다.
- `static int SIDE_UP` — SIDE_UP 게임 키를 지정하는 상수. 96로 지정되어 있습니다.
- `static int SMS_EVENT` — SMS 이벤트 상수. 4로 지정되어 있습니다.
- `static int SOFT1` — SOFT1 게임 키를 지정하는 상수. 90으로 지정되어 있습니다.
- `static int SOFT2` — SOFT2 게임 키를 지정하는 상수. 91로 지정되어 있습니다.
- `static int SOFT3` — SOFT3 게임 키를 지정하는 상수. 92로 지정되어 있습니다.
- `static int SYSTEM_EVENT_END`
- `static int SYSTEM_USER_EVENT`
- `static int TIMER_EVENT` — 타이머 이벤트 상수.
- `static int UP` — UP 게임 키를 지정하는 상수. 1로 지정되어 있습니다.
- `static int USER_EVENT` — 사용자 이벤트 상수. 0x5000으로 지저오디어 있습니다.

## 메서드 요약

- `void dispatchEvent (int[] event)` — 이벤트를 처리해 줍니다.
- `void getNextEvent (int[] event)` — 발생한 새 이벤트를 가져옵니다.
- `static void hookEvent (int id, JletEventListener lst)`
- `boolean postEvent (int[] event)` — 새로운 이벤트를 넣습니다.
