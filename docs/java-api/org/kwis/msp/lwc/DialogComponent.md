# Class DialogComponent

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.ContainerComponent
              |
              +--org.kwis.msp.lwc.ShellComponent
                    |
                    +--org.kwis.msp.lwc.DialogComponent
```

## 설명

**extends ShellComponent:**

`DialogComponent`는 다양한 형태의 다이알로그박스를 지원하기 위해서
 만들어진 컴포넌트입니다.

기본적으로 `DialogComponent`는 타이틀영역과 데이타 영역,
 버튼영역으로 구성되어있습니다.
 타이틀영역을 다이알로그박스의 타이틀이 존재하는 경우 타이틀을 출력해주는 영역이고,
 데이타 영역을 사용자에 의해서 주가된 여러 형태의 컴포넌트를 출력해주는 영역이며,
 버튼영역은 각 타입에 따라 사용되는 버튼을 출력해주는 영역입니다.
 각 영역의 위치는 변경할 수 없으며, 단지 각 영역의 문자 데이타나 컴포넌트만을 변경할
 수 있습니다.

의 데이타 영역에는 한개의

만을
 추가 할 수 있습니다. 따라서 여러개의

를 가지는 다이알로그를
 만들려면

를 활용하여 데이타 영역에 추가합니다.

`DialogComponent`에서는 기본적으로 3가지 타입을 지원하고 있습니다.
 확인기능을 제공하는 `TYPE_OK`타입과 확인과 취소기능을 제공하는
 `TYPE_OK_CANCEL` 타입,일정 시간동안 화면에 데이타를 출력해주는
 기능을 제공하는 `TYPE_NONE`입니다.

`TYPE_NONE`의 경우 기본적으로 화면에 출력되는 시간은
 3초이며, 이 시간값을 ``setTimeout(int)``메소드를 통해서 사용자가 지정할 수 있습니다.
 타입이 `TYPE_NONE`인경우 `TIMEOUT_INFINITE`값을
 `timeout`값으로 지정하면 `TYPE_OK`로 타입이 변경됩니다.

타입값이 잘못 지정된 경우, 즉 `TYPE_NONE,TYPE_OK,TYPE_OK_CANCEL`이외의
 값이 지정된 경우, `IllegalArgumentException`발생됩니다.

## 필드 요약

- `protected  int actionState` — 현재 어떤 액션(이벤트)이 발생한 것인지를 기억하는 필드.
- `static int CANCEL_BUTTON` — CANCEL 버튼타입.
- `static int DLG_CANCEL` — doModal 시 리턴되는 값으로 CANCEL 버튼이 선택되었음을 나타냄.
- `static int DLG_OK` — doModal 시 리턴되는 값으로 OK 버튼이 선택되었음을 나타냄.
- `static int DLG_TIMEOUT` — doModal 시 리턴되는 값으로 TIMEOUT 되어 종료된것을 나타냄.
- `static int OK_BUTTON` — OK 버튼타입.
- `static int TIMEOUT_INFINITE` — timeout 값 중 무한대의 값을 나타냄.
- `static int TYPE_NONE` — 버튼이 없는 형태의 다이알로그타입.
- `static int TYPE_OK` — OK 버튼만 있는 형태의 다이알로그타입.
- `static int TYPE_OK_CANCEL` — OK ,CANCEL 버튼이 있는 형태의 다이알로그타입.

## 생성자 요약

- DialogComponent ( Component cmp, String title,
 int type) 새로운 DialogComponent 의 인스턴스를 생성합니다.
- DialogComponent ( Component cmp, String ttl,
 int type,
 int x,
 int y,
 int w,
 int h) 새로운 DialogComponent 의 인스턴스를 생성합니다.
- DialogComponent (int type) 데이타 컴포넌트와 타이들이 없고 주어진 타입을 가지는 새로운 DialogComponent 의 인스턴스를 생성합니다.

## 메서드 요약

- `int doModal ()` — DialogComponent 를 화면에 나타나게 합니다.
- `int getActionState ()` — DialogComponent 에서 발생한 마지막 액션을 얻어옵니다.
- `int getTimeout ()` — 현재 설정되어 있는 타임아웃값을 얻어옵니다.
- `void layout ()` — 하위 컴포넌트의 크기와 위치를 결정합니다.
- `protected  void paintFrame ( Graphics g)` — useFrame 의 인수를 true 으로 호출하는 경우에 화면을 그릴때 호출됩니다.
- `void setButtonString (int buttonType, String buttonStr)` — 버튼의 문자를 지정합니다.
- `void setTimeout (int timeout)` — DialogComponent 를 화면에 보여줄 타임아웃 시간을 지정합니다.
- `void setType (int type)` — DialogComponent 의 타입을 지정합니다.
- `void show ()` — 컴포넌트를 화면상에 보여줍니다.
