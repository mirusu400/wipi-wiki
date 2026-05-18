# Class ShellComponent

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.ContainerComponent
              |
              +--org.kwis.msp.lwc.ShellComponent
```

## 설명

**Direct Known Subclasses:**
- `AnnunciatorComponent`, `DialogComponent`

**extends ContainerComponent:**

Card와의 연결을 해주며, 제목과 명령 입력 컴포넌트와 작업 컴포넌
 트를 가집니다.

 UI컴포넌트를 화면에 보여주기 위해서 맨 상단에는 이 컴포넌트를 사용해야
 합니다. `ShellComponent`는 `AddComponent`를
 통해서 하나의 작업 컴포넌트 만을 가질 수 있습니다.

 이 컴포넌트는 lcdui의 ``Card``에 연결하여
 카드로 부터 들어오는 이벤트를 해당 컴포넌트에게 전달해 주는 역활을
 합니다.

또한 화면에 타이틀과 프레임을 보여줍니다.

## 필드 요약

- `protected Card cd`
- `protected Component cmpCommand`
- `protected Component cmpTitle`
- `protected Component cmpWork`
- `protected static int RESIZE_MASK`

## 생성자 요약

- ShellComponent () 쉘 컴포넌트를 생성합니다.
- ShellComponent (boolean inflate) 쉘 컴포넌트를 생성합니다.
- ShellComponent (boolean inflate,
 boolean bTrans)
- ShellComponent (int x,
 int y,
 int w,
 int h) 쉘 컴포넌트를 생성합니다.
- ShellComponent (int x,
 int y,
 int w,
 int h,
 boolean bTrans)

## 메서드 요약

- `int addComponent ( Component cmp)` — 자식 컴포넌트를 하나 추가합니다.
- `void addComponent (int index, Component cmp)` — 자식 컴포넌트를 하나 추가합니다.
- `void configure (int x, int y, int w, int h, int mask)` — 컴포넌트의 위치나 크기를 변경합니다.
- `protected  void controlInset (boolean flag)` — ContainerComponent 에서 사용할 테두리 두께값을 제어합니다.
- `Card getCard ()` — 현재 컴포넌트에 연결된 카드를 돌려줍니다.
- `Component getCommand ()` — 지정된 커맨드 컴포넌트를 돌려줍니다.
- `protected Component getNextTraversalComponent ()` — 포커스 가질 수 있는 다음 컴포넌트를 돌려줍니다.
- `protected Component getPrevTraversalComponent ()` — 포커스 가질 수 있는 이전 컴포넌트를 돌려줍니다.
- `Component getTitle ()` — 지정된 타이틀을 돌려줍니다.
- `Component getWorkComponent ()` — 지정된 Component 돌려줍니다.
- `int getX ()` — x축의 좌표를 돌려줍니다.
- `int getY ()` — y축의 좌표를 돌려줍니다.
- `void grabKey (int key)` — 특정 키코드를 그랩(Grab)하여 GrabKeyListener에게 보냅니다.
- `void hide ()` — 컴포넌트를 감춥니다.
- `boolean isShown ()` — 현재 컴포넌트가 보이는지 안보이는지 여부를 돌려줍니다.
- `protected  boolean keyNotify (int type, int chr)` — 키 입력을 받으면 호출됩니다.
- `void layout ()` — 하위 컴포넌트의 크기와 위치를 결정합니다.
- `protected  boolean processEvent (int type, int subtype, int param1, int param2)` — 이벤트를 처리합니다.
- `void removeAllComponents ()` — 모든 컴포넌트를 삭제합니다.
- `void removeComponent ( Component cmp)` — 지정된 컴포넌트를 삭제합니다.
- `void repaint (int x, int y, int w, int h)` — 화면의 내용을 갱신할 필요가 있을때 부릅니다.
- `void serviceRepaints ()` — 갱신된 내용을 즉시 화면에 출력해줍니다. repaint에 의한 paint를 나중에 부르는 것이 아니라, 직접 paint함수를 불러서 화면에 출력합니다.
- `void setCommand ( Component cmp, boolean bGrab)` — 커맨드를 지정합니다.
- `void setGrabKeyListener ( GrabKeyListener listener, Object obj)` — 그랩 키 리스너를 등록합니다.
- `void setTitle ( Component cmp)` — 타이틀을 지정합니다.
- `void setTitle ( String str)` — 타이틀 문자열을 지정합니다.
- `void setWorkComponent ( Component cmp)` — Component를 설정 합니다
- `void show ()` — 컴포넌트를 화면상에 보여줍니다.
- `void showNotify (boolean b)` — 화면의 내용이 보이면 호출됩니다.
- `void ungrabKey (int key)` — 특정키에 대한 그랩(Grab)을 해제 합니다.

## 필드 상세

### cd

```java
protected Card cd
```

### cmpTitle

```java
protected
```
