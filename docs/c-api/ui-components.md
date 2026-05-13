# 5.1.11. 사용자 인터페이스 컴포넌트

사용자 인터페이스 컴포넌트로 텍스트 박스, 날짜/시간 컴포넌트, 메뉴 컴포넌트, 라벨 컴포넌트, 리스트 컴포넌트가 있다.

### 컴포넌트 생성/소멸

컴포넌트를 생성하기 위해서는 컴포넌트 클래스 구조체가 있어야 한다. 컴포넌트 클래스 구조체는 미리 정의되어 값들이 결정된 구조체로 MC_uicGetClass 함수를 통 하여 정의된 구조체를 가져올 수 있다. 컴포넌트 클래스 구조체는 각 컴포넌트 별 로 다르며, 이 컴포넌트 클래스 구조체를 매개 변수로 하여 MC_uicCreate 함수를 호출하면, 컴포넌트 클래스 구조체를 생성할 수 있다. 생성된 컴포넌트는 MC_uicDestroy로 파괴 된다.

### 좌표체계

컴포넌트의 위치와 크기는 화면 좌표 체계를 따른다. 왼쪽 상단이 원점(0, 0)이며, 오른쪽, 아래쪽으로 이동하면서 좌표값이 픽셀 단위로 증가한다.

### 이벤트 처리

"C"에서 제공하는 사용자 인터페이스 컴포넌트는 컨테이너를 제공하고 있지 않기 때문에 컨테이너가 하는 역할을 각 응용 프로그램에서 해주어야 한다. 즉 응용 프 로그램에서 컴포넌트 마다 각 이벤트를 처리하는 함수를 불러주어야 한다.

Clet 의 handleCletEvent 함수 내에서 생성된 각 컴포넌트를 매개 변수로 하여 MC_uicHandleEvent함수를 호출해 주어야 한다. MC_uicHandleEvent 는 이벤트를 적절 히 처리하고, 이벤트 처리 여부를 돌려준다.

Clet 의 paintClet 함수 내에서는 컴포넌트마다 각 MC_uicPaint 함수를 호출해 주 어야 한다.

### 콜백 함수와 이벤트 핸들러 함수

MC_uicHandleEvent 에 의해서 이벤트가 처리될때 사용자가 MC_uicSetEventHandler 함수에 의해서 지정한 이벤트 핸들러 함수를 먼저 호출해 준다. 이 호출된 함수가 돌려주는 값에 따라서, MC_uicHandleEvent 함수는 계속 이벤트를 처리할지 안할지 여부를 결정한다. 만일 이벤트를 처리하게 되면, MC_uicHandleEvent 는 이벤트를 처리한 후에 해당되는 이벤트의 MC_uicCallbackProc 를 호출하도록 한다. 어떤 이 벤트에 대해서 콜백 함수를 사용할 수 있는지에 대해서는 컴포넌트 마다 다르므로 컴포넌트에 대한 문서를 참조하십시요.

### 텍스트 박스 컴포넌트

텍스트 박스 컴포넌트는 MC_UicComponent 를 상속 받으며, 사용자에게 문자열을 보여주고, 해당 문자열을 변경할 수 있도록 해주는 컴포넌트이다. 텍스트 박스내 에 넣을수 있는 문자열은 MC_uicGetTextSize 로 알수가 있다. 기본적으로 저장할 수 있는 최대 값은 256바이트이며, MC_uicSetTextSize함수로 변경이 가능한다.

사용 가능한 함수는 다음과 같다.

MC_uicInsertText MC_uicDeleteText MC_uicGetMaxTextSize MC_uicSetMaxTextSize MC_uicGetTextSize MC_uicGetText

### 그외 컴포넌트에서 사용할 수 있는 함수

사용 가능한 콜백 함수는 다음과 같다.

MC_UIC_CHANGE_CALLBACK : 내부 문자열이 변경되었을 경우 MC_UIC_KEY_CALLBACK : 키가 눌러졌을 경우

### 그외 컴포넌트에서 사용할 수 콜백 함수

### 날짜/시간 컴포넌트

날짜/시간 컴포넌트는 MC_UicComponent 를 상속받으며, 사용자에게 날짜/시간을 보여주고, 그 날짜/시간을 입력받는 함수이다. MC_uicSetTime 함수에 의해서 날짜 /시간을 지정할 수 있으며, 지정하지 않는다면 날짜/시간 컴포넌트를 생성한 시간 으로 지정된다. 날짜/시간 컴포넌트는 날짜나 시간,혹은 두 항목다 화면에 출력할 수 있으며, 이는 MC_uicSetTimeMask함수로 가능한다.

사용 가능한 함수는 다음과 같다.

MC_uicSetTimeMask MC_uicSetTime MC_uicGetTime MC_uicSetTimeLong

### 그외 컴포넌트에서 사용할 수 있는 함수

사용 가능한 콜백 함수는 다음과 같다.

MC_UIC_CHANGE_CALLBACK : 내부 시간이 변경되었을 경우

### 그외 컴포넌트에서 사용할 수 콜백 함수

### 메뉴 컴포넌트

메뉴 컴포넌트는 MC_UicComponent 를 상속받으며, 화면에 메뉴를 출력하고, 사용 자로 부터 입력을 받다. 메뉴 상하/좌우키로 현재 선택 메뉴 항목을 변경하여 지 정하도록 한다.

사용 가능한 함수는 다음과 같다.

MC_uicAddMenuItem MC_uicGetMenuItem MC_uicRemoveMenuItem MC_uicSetActiveMenuItem MC_uicGetActiveMenuItem

### 그외 컴포넌트에서 사용할 수 있는 함수

사용 가능한 콜백 함수는 다음과 같다.

MC_UIC_CHANGE_CALLBACK : 내부 선택된 메뉴 항목이 변경되었을 경우

### 그외 컴포넌트에서 사용할 수 콜백 함수

### 라벨 컴포넌트

라벨 컴포넌트는 MC_UicComponent 를 상속받으며, 화면에 문자열을 출력해 주는 함수이다. 크기에 맞도록 문자열의 줄바꿈을 해준다. 이 컴포넌트는 다른 컴포넌 트와는 달리 이벤트에 대한 처리를 하지 않는다.

사용 가능한 함수는 다음과 같다.

MC_uicSetLabel

### 리스트 컴포넌트

리스트 컴포넌트는 MC_UicComponent 를 상속받으며, 화면에 리스트를 출력하고, 사용자로 부터 입력을 받다. 메뉴 상하키로 메뉴 항목을 변경하여 지정하도록 한 다.

사용 가능한 함수는 다음과 같다.

MC_uicAddListItem MC_uicGetListItem MC_uicRemoveListItem MC_uicSetActiveListItem MC_uicGetActiveListItem

### 그외 컴포넌트에서 사용할 수 있는 함수

사용 가능한 콜백 함수는 다음과 같다.

MC_UIC_CHANGE_CALLBACK : 내부 선택된 메뉴 항목이 변경되었을 경우

### 그외 컴포넌트에서 사용할 수 콜백 함수

### 컴포넌트

컴포넌트 가장 기본이되는 컴포넌트이며, 이벤트에 대한 처리도 하지 않는다.

사용 가능한 함수는 다음과 같다.

MC_uicDestory MC_uicRepaint MC_uicPaint MC_uicGetClassName MC_uicIsInstance MC_uicHandleEvent MC_uicConfigure MC_uicGetGeometry MC_uicSetEnable MC_uicSetExtData MC_uicGetExtData MC_uicSetCallback MC_uicSetEventHandler MC_uicSetFont MC_uicGetFont 사용 가능한 콜백 함수는 다음과 같다.

MC_UIC_SELECT_CALLBACK : 사용자가 "SELECT"버튼을 눌러서 무엇인가 선택했을 때 MC_UIC_PAINT_CALLBACK : 컴포넌트가 그려질때 MC_UIC_DESTORY_CALLBACK : 컴포넌

### 트가 소멸될때

**참고 항목**

없음

### MC_UicComponent

**프로토타입**

```c
typedef M_Int32 MC_UicComponent
```

**설명**

컴포넌트 식별자

### MC_UicClass

**프로토타입**

```c
typedef M_Int32 MC_UicClass
```

**설명**

컴포넌트 클래스 구조체 식별자

### MC_UicApplicationContext

**프로토타입**

```c
typedef M_Int32 MC_UicApplicationContext
```

**설명**

응용 프로그램 컨택스트 식별자

### MC_UicCallbackProc

**프로토타입**

```c
typedef void (*MC_UicCallbackProc)(MC_UicCom ponent cc, void* serverData,
M_Int32 clientData)
```

**설명**

콜백 함수 타입

**매개 변수**

- `cc` — 콜백 함수를 호출하는 컴포넌트
- `serverData` — 부르는 쪽에서 넘기는 데이타; 호출하는 쪽마다 다른다.
- `clientData` — 콜백 함수를
**부작용**

없음

**참고 항목**

없음

### MC_UicEventHandlerProc

**프로토타입**

```c
typedef M_Int32 (*MC_UicEventHandlerProc)(MC_UicComponent cc, M_Int32 type,
M_Int32 param1, M_Int32 param2)
```

**설명**

이벤트 핸들러 함수 타입.

**매개 변수**

- `cc` — 이벤트 핸들러를 호출하는 컴포넌트
- `type` — 이벤트 타입.
- `param1` — 이벤트 매개 변수1
- `param2` — 이벤트 매개 변수2
**반환 값**

이벤트 처리 여부 1이면 처리한 것이고, 0이면 처리하지 않음을 의미

**부작용**

없음

**참고 항목**

없음

### MC_UIC_MENU_COMPONENT

**프로토타입**

```c
#define MC_UIC_MENU_COMPONENT "MenuComponent"
```

**설명**

메뉴 컴포넌트 클래스의 문자열, "MenuComponent"로 정의 되어 있다.

### MC_UIC_DATE_TIME_COMPONENT

**프로토타입**

```c
#define MC_UIC_DATE_TIME_COMPONENT "DateTimeComponent"
```

**설명**

데이트, 타임 컴포넌트 클래스의 문자열, "DateTimeComponent"로 정의 되어 있다.

### MC_UIC_TEXT_COMPONENT

**프로토타입**

```c
#define MC_UIC_TEXT_COMPONENT "TextComponent"
```

**설명**

텍스트 컴포넌트 클래스의 문자열, "TextComponent"로 정의한다.

### MC_UIC_LABEL_COMPONENT

**프로토타입**

```c
#define MC_UIC_LABEL_COMPONENT "LabelComponent"
```

**설명**

라벨 컴포넌트 클래스의 문자열, "LabelComponent"로 정의한다.

### MC_UIC_LIST_COMPONENT

**프로토타입**

```c
#define MC_UIC_LIST_COMPONENT "ListComponent"
```

**설명**

리스트 컴포넌트 클래스의 문자열, "ListComponent"로 정의한다.

### MC_UIC_DESTROY_CALLBACK

**프로토타입**

```c
#define MC_UIC_DESTORY_CALLBACK 1
```

**설명**

컴포넌트가 소멸될 때 불리는 콜백 함수의 인덱스 1

### MC_UIC_PAINT_CALLBACK

**프로토타입**

```c
#define MC_UIC_PAINT_CALLBACK 2
```

**설명**

컴포넌트가 칠해질 때 불리는 콜백 함수의 인덱스, 상수 2로 정의한다.

### MC_UIC_SELECT_CALLBACK

**프로토타입**

```c
#define MC_UIC_SELECT_CALLBACK 3
```

**설명**

컴포넌트의 특정 내용이 선택될 때 불리는 콜백 함수의 인덱스, 상수 3 으로 정의 한다.

### MC_UIC_CHANGE_CALLBACK

**프로토타입**

```c
#define MC_UIC_CHANGE_CALLBACK 4
```

**설명**

컴포넌트의 내부 내용이 변경될 때 불리는 콜백 함수의 인덱스, 상수 4 로 정의한 다.

### MC_UIC_KEY_CALLBACK

**프로토타입**

```c
#define MC_UIC_KEY_CALLBACK 5
```

**설명**

컴포넌트에 사용자가 키를 눌렀을 때 불리는 콜백 함수의 인덱스, 상수 5 로 정의 한다

### MC_GRP_GRAY_TYPE

**프로토타입**

```c
#define MC_GRP_GRAY_TYPE(1 << 1)
```

**설명**

흑백 타입. 상수값 (1 << 1).

### MC_GRP_COLOR_TYPE

**프로토타입**

```c
#define MC_GRP_COLOR_TYPE(1 << 2)
```

**설명**

컬러 타입. 상수값 (1 << 2).

### MC_ALIGN_LEFT

**프로토타입**

```c
#define MC_ALIGN_LEFT 0
```

**설명**

라벨컴포넌트의 좌측정렬. 상수값 0.

### MC_ALIGN_RIGHT

**프로토타입**

```c
#define MC_ALIGN_RIGHT 1
```

**설명**

라벨컴포넌트의 우측정렬. 상수값 1.

### MC_ALIGN_CENTER

**프로토타입**

```c
#define MC_ALIGN_CENTER 2
```

**설명**

라벨컴포넌트의 중앙정렬. 상수값 2.

### MC_uicCreateApplicationContext

**프로토타입**

```c
MC_UicApplicationContext MC_uicCreateApplicationContext()
```

**설명**

응용프로그램 컨텍스트를 생성한다.

**매개 변수**

없음

**반환 값**

생성된 응용프로그램 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_uicGetClass

**프로토타입**

```c
MC_UicClass MC_uicGetClass(M_Uint8* psz)
```

**설명**

컴포넌트 클래스 구조체를 가져온다.

문자열에 대응하는 컴포넌트 클래스 구조체를 가져 온다. 현재 지원하는 컴포넌트 클래스 구조체의 문자열은 MC_UIC_MENU_COMPONENT, MC_UIC_DATE_TIME_COMPONENT, MC_UIC_TEXT_COMPONENT, MC_UIC_LABEL_COMPONENT, MC_UIC_LIST_COMPONENT 가 있다.

**매개 변수**

- `psz` — [in] 컴포넌트 클래스를 나타내는 문자열
**반환 값**

컴포넌트 클래스 구조체 매개변수(psz)값이 지원되는 컴포넌트 클래스 구조체의 문자열이 아닌 경우 M_E_ERROR값을 반환

**부작용**

없음

**참고 항목**

없음

### MC_uicCreate

**프로토타입**

```c
MC_UicComponent MC_uicCreate(MC_UicApplicationContext pac, MC_UicClass cls)
```

**설명**

컴포넌트를 생성한다.

지정한 컴포넌트 클래스로부터 컴포넌트를 생성한다. MC_uicCreateApplicationContext 함수로 부 터 생성한 응용 프로그램 컨택스트(Application Context)와 MC_uicGetClass 함수로 가져온 클래스 구조체를 매개 변수로 넘긴다.

**매개 변수**

- `pac` — [in] 응용 프로그램 컨텍스트
- `cls` — [in] 응용 프로그램 컨텍스트
**반환 값**

새로 생성된 컴포넌트 클래스 실패시 M_E_ERROR : 부적합한 매개변수값 사용 및 기타 에러 발생시 MC_UIC_E_OUT_OF_MEM : 메모리 부족시

**부작용**

없음

**참고 항목**

MC_uicCreateApplicationContext

### MC_uicDestroy

**프로토타입**

```c
void MC_uicDestroy(MC_UicComponent cc)
```

**설명**

지정한 컴포넌트를 소멸시킨다.

삭제한 cc는 더이상 사용되서는 안된다.

**매개 변수**

- `cc` — [in] 삭제할 컴포넌트
**부작용**

없음

**참고 항목**

없음

### MC_uicRepaint

**프로토타입**

```c
void MC_uicRepaint(MC_UicComponent cc, M_Int32 x, M_Int32 y, M_Int32 w,
M_Int32 h)
```

**설명**

지정한 컴포넌트에 대해서 그리기 이벤트를 생성한다.

지정한 컴포넌트 영역에 대해서 paintClet 함수가 호출될 수 있도록 내부 이벤트 를 생성한다. 만일 w, h가 -1이면, 지정된 (x, y)좌표에서 컴포넌트의 오른쪽 하 단부분까지가 그리기 이벤트가 발생하는 영역이된다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `x` — [in] 컴포넌트 내의 영역의 x축 좌표(컴포넌트 좌표 체계)
- `y` — [in] 컴포넌트 내의 영역의 y축 좌표(컴포넌트 좌표 체계)
- `w` — [in] 컴포넌트 내의 영역의 폭
- `h` — [in] 컴포넌트 내의 영역의 높이
**부작용**

없음

**참고 항목**

MC_grpRepaint MC_uicPaint

### MC_uicPaint

**프로토타입**

```c
void MC_uicPaint(MC_UicComponent cc, MC_GrpContext *pgc)
```

**설명**

지정한 컴포넌트를 그린다.

실제 화면 프레임 버퍼에 컴포넌트의 내용을 그려준다. 이 함수는 응용 프로그램 의 paintClet 함수에서 각각의 컴포넌트 별로 호출되어야 한다. pgc 가 지정하는 클리핑 영역은 변경하지 않고 pgc 의 일부 내용은 컴포넌트에 따라서 변경 될 수 있다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `pgc` — [in] 사용할 그래픽 컨텍스트
**부작용**

없음

**참고 항목**

없음

### MC_uicGetClassName

**프로토타입**

```c
M_Uint8* MC_uicGetClassName(MC_UicComponent cc)
```

**설명**

컴포넌트의 클래스 이름을 얻어 온다.

cc 가 가리키는 컴포넌트에 대응하는 클래스 이름을 "C"문자열로 돌려받다. 돌려 받은 값은 변경될 수 없다.

**매개 변수**

- `cc` — [in] 컴포넌트
**반환 값**

컴포넌트의 클래스 이름 부적합한 매개변수값의 사용으로 인한 반환되는 에러값으로 NULL값을 반환한다.

**부작용**

없음

**참고 항목**

없음

### MC_uicIsInstance

**프로토타입**

```c
M_Uint32 MC_uicIsInstance(MC_UicComponent cc, M_Uint8* pcls)
```

**설명**

컴포넌트가 지정된 클래스에 상속 받은 클래스인지 여부를 돌려준다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `pcls` — [in] 컴포넌트 클래스 이름 문자열
**반환 값**

컴포넌트가 지정된 클래스의 인스턴스이면 1, 그렇지 않으면 0

**부작용**

없음

**참고 항목**

없음

### MC_uicHandleEvent

**프로토타입**

```c
M_Int32 MC_uicHandleEvent(MC_UicCompeont cc, M_Int32 type, M_Int32 param1,
M_Int32 param2)
```

**설명**

컴포넌트 별로 이벤트를 처리한다.

지정한 컴포넌트에게 이벤트를 처리할 것을 요청한다. 이벤트가 처리되었다면 1 을 돌려주고 그렇지 않으면 0을 돌려준다.

type 과 param1, param2 는 handleCletEvent 함수에서 넘어오는 이벤트 관련 매개 변수를 그대로 넘긴다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `type` — [in] 이벤트 타입
- `param1` — [in] 이벤트 매개 변수1
- `param2` — [in] 이벤트 매개 변수2
**반환 값**

컴포넌트 내에서 처리 여부

**부작용**

없음

**참고 항목**

없음

### MC_uicConfigure

**프로토타입**

```c
void MC_uicConfigure(MC_UicComponent cc, M_Int32 x, M_Int32 y, M_Int32 w,
M_Int32 h, M_Int32 mask)
```

**설명**

컴포넌트의 크기를 위치와 지정한다.

지정된 컴포넌트를 (x, y)가 가르치는 위치에 두고,폭 w, 높이 h 로 크기를 결정 한다.mask & MC_UIC_POS_MASK가 0 이 아니면 (x, y)에 가르치는 위치로 이동이 되 며, mask & MC_UIC_SIZE_MASK가 0이 아니면 크기 (w, h)로 지정된다.

w나 h가 0이하인 경우는 이 함수는 작동하지 않는다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `x` — [in] 컴포넌트의 화면상에서의 x축 좌표
- `y` — [in] 컴포넌트의 화면상에서의 y축 좌표
- `w` — [in] 컴포넌트의 폭
- `h` — [in] 컴포넌트의 높이
- `mask` — [in] 컴포넌트 크기만 변경할 것인지 높이만 변경할 것인지 여부;
MC_UIC_SIZE_MASK나 MC_UIC_POS_MASK나 두 값이 OR된 값

**부작용**

없음

**참고 항목**

없음

### MC_uicGetGeometry

**프로토타입**

```c
void MC_uicGetGeometry(MC_UicComponent cc, M_Int32* px, M_Int32* py,
M_Int32* pw, M_Int32* ph)
```

**설명**

컴포넌트의 크기와 위치를 가져온다.

지정된 컴포넌트의 위치를 px, py 가 가리키는 변수에 저장하고, pw, ph 에 크기를 저장한다. 만일 파라미터 중 하나가 NULL이면, 해당하는 값을 복사하지 않는다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `px` — [out] 컴포넌트의 화면상의 x값을 저장할 포인터
- `py` — [out] 컴포넌트의 화면상의 y값을 저장할 포인터
- `pw` — [out] 컴포넌트의 폭을 저장할 포인터
- `ph` — [out] 컴포넌트의 높이를 저장할 포인터
**부작용**

없음

**참고 항목**

없음

### MC_uicSetEnable

**프로토타입**

```c
void MC_uicSetEnable(MC_UicComponent cc, M_Int32 enable)
```

**설명**

컴포넌트를 입력가능/불가능하게 만든다.

enable에 따라서 컴포넌트가 입력을 받거나 받을 수 없도록 한다.

기본적으로 컴포넌트가 생성되면 입력을 받지 않는(Enable 이 FALSE 설정됨) 상태 로 생성 된다. 그러므로 입력을 받게 하려면 이 함수를 이용하여 활성화 시켜야 한다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `enable` — [in] 1이면 입력가능, 0이면 입력 불가능
**부작용**

없음

**참고 항목**

없음

### MC_uicSetCallback

**프로토타입**

```c
MC_UicCallbackProc MC_uicSetCallback( MC_UicComponent cc, M_Int32 idx,
MC_UicCallbackProc proc, M_Int32 clientData)
```

**설명**

컴포넌트에 콜백 함수를 지정한다.

특정 이벤트가 발생하면, 이벤트를 컴포넌트에서 다 처리하고 난 후에 콜백 함수 를 호출한다.

clientData는 콜백 함수의 세번째 매개 변수가 된다. 콜백 함수가 불려질 특정 이벤 트는 다음과 같다.

MC_UIC_DESTROY_CALLBACK MC_UIC_PAINT_CALLBACK MC_UIC_SELECT_CALLBACK MC_UIC_CHANGE_CALLBACK MC_UIC_KEY_CALLBACK

**매개 변수**

- `cc` — [in] 컴포넌트
- `idx` — [in] 콜백 함수가 불려질 특정 이벤트 MC_UIC_PAINT_CALLBACK,
MC_UIC_SELECT_CALLBACK

- `proc` — [in] 콜백 함수의 포인터
- `clientData` — [in] 콜백 함수의 매개 변수
**반환 값**

이전에 지정되었던 콜백 함수. 만일 이전에 지정된 내용이 없다면, NULL 을 돌려 준다.

**부작용**

없음

**참고 항목**

없음

### MC_uicSetEventHandler

**프로토타입**

```c
MC_UicEventHandlerProc MC_uicSetEventHandler( MC_UicComponent cc,
MC_UicEventHandlerProc handler)
```

**설명**

컴포넌트에 이벤트 핸들러를 지정한다.

이벤트 핸들러가 지정되어 있으면, 컴포넌트의 모든 이벤트에 대해서 이벤트 핸들 러를 호출해 준다. 이벤트 핸들러의 결과 값에 따라서 이벤트를 계속 처리할지 안 할지 여부를 결정한다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `handler` — [in] 이벤트 핸들러
**반환 값**

이전에 지정되었던 이벤트 핸들러. 만일 이전에 지정된 내용이 없다면 NULL 을 돌 려준다.

**부작용**

없음

**참고 항목**

없음

### MC_uicSetFont

**프로토타입**

```c
M_Int32 MC_uicSetFont(MC_UicComponent cc, M_Int32 fontid)
```

**설명**

컴포넌트의 폰트를 지정한다.

fontid가 지정하는 폰트 아이디로 컴포넌트의 폰트를 지정한다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `fontid` — [in] MC_grpGetFont의 반환 값으로 폰트 식별자.
**반환 값**

이전에 지정되었던 폰트 식별자.

**부작용**

없음

**참고 항목**

없음

### MC_uicGetFont

**프로토타입**

```c
M_Int32 MC_uicGetFont(MC_UicComponent cc)
```

**설명**

컴포넌트의 폰트를 돌려준다.

**매개 변수**

- `cc` — [in] 컴포넌트
**반환 값**

현재 지정된 폰트 식별자.

**부작용**

없음

**참고 항목**

없음

### MC_uicSetFgColor

**프로토타입**

```c
void MC_uicSetFgColor(MC_UicComponent cc, M_Int32 nColor);
```

**설명**

컴포넌트의 Foreground 색상을 설정합니다 를 설정합니다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `nColor` — 색상값(0xRRGGBB)
**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MC_uicSetBgColor

**프로토타입**

```c
void MC_uicSetBgColor(MC_UicComponent cc, M_Int32 nColor);
```

**설명**

컴포넌트의 Background 색상을 설정합니다 를 설정합니다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `nColor` — 색상값(0xRRGGBB)
**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MC_uicSetLabel

**프로토타입**

```c
void MC_uicSetLabel(MC_UicComponent cc, M_Uint8 *psz)
```

**설명**

라벨컴포넌트의 문자열을 변경 합니다.

지정된 컴포넌트가 레이블 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `psz` — [in] 변경될 문자열
**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MC_uicGetLabel

**프로토타입**

```c
M_Uint8* MC_uicGetLabel(MC_UicComponent cc)
```

**설명**

라벨 컴포넌트의 문자열을 얻어옵니다.

지정된 컴포넌트가 라벨 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `cc` — [in] 컴포넌트
**반환 값**

현재 지정되어있는 문자열.

**부작용**

없음

**참고 항목**

없음

### MC_uicSetlabelAlignment

**프로토타입**

```c
M_Int32 MC_uicSetlabelAlignment(MC_UicComponent cc, M_Int32 align)
```

**설명**

라벨콤포넌트의 문자열 정렬방식을 설정합니다.

MC_ALIGN_LEFT, MC_ALIGN_RIGHT, MC_ALIGN_CENTER 중 하나의 값을 사용할 수 있으 며 각각 좌측정렬, 우측정렬, 중앙정렬을 의미 합니다.

지정된 컴포넌트가 라벨 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `align` — [in] 라벨 컴포넌트의 문자열의 정렬방식 MC_ALIGN_LEFT, MC_ALIGN_RIGHT,
MC_ALIGN_CENTER중 하나를 사용합니다.

**반환 값**

이전에 지정된 값이 넘어 온다.

**부작용**

없음

**참고 항목**

없음

### MC_uicSetTimeMask

**프로토타입**

```c
M_Int32 MC_uicSetTimeMask(MC_UicComponent cc, M_Int32 mask)
```

**설명**

타임 컴포넌트 형태를 지정한다.

(mask & MC_UIC_ TIME_MASK)이 0 이 아니면 시간이 출력되고, (mask & MC_UIC_DATE_MASK)이 0이 아니면 날짜가 출력된다.

지정된 컴포넌트가 타임 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `mask` — [in] 타임 컴포넌트의 매스크, MC_UIC_TIME_MASK나 MC_UIC_DATE_MASK혹은
둘을 OR한 값.

**반환 값**

이전에 지정된 값이 넘어 온다.

**부작용**

없음

**참고 항목**

없음

### MC_uicSetTime

**프로토타입**

```c
void MC_uicSetTime(MC_UicComponent cc, struct tm* pd)
```

**설명**

타임 컴포넌트에 시간을 지정한다.

지정된 컴포넌트가 타임 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는다.

이때 pd는 표준 C라이브러리 time.h에서 정의된 tm 구조체 이다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `pd` — [in] 지정할 날짜. time.h참조
**부작용**

없음

**참고 항목**

없음

### MC_uicSetTimeLong

**프로토타입**

```c
void MC_uicSetTimeLong(MC_UicComponent cc, time_t time)
```

**설명**

타임 컴포넌트에 시간을 지정한다.

지정된 컴포넌트가 타임 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는다.

이때 time 은 표준 C 라이브러리의 time.h 에서 정의된 time()함수에서 구해진 time_t형태의 값이다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `time` — [in] 지정할 날짜와 시간. time.h참조
**부작용**

없음

**참고 항목**

없음

### MC_uicGetTime

**프로토타입**

```c
void MC_uicGetTime(MC_UicComponet cc, struct tm* pd)
```

**설명**

타임 컴포넌트에서 시간/날짜를 얻어 온다.

전달하는 포인터에 각각 내용을 채워준다. 만일 포인터가 NULL 을 가리키면 해당 되는 값은 복사되지 않는다.

지정된 컴포넌트가 타임 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는다.

받아오는 날짜는 표준 C라이브러리의 time.h에 정의된 tm구조체의 형태이다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `pd` — [out] 받아올 날짜.
**부작용**

없음

**참고 항목**

없음

### MC_uicAddMenuItem

**프로토타입**

```c
M_Int32 MC_uicAddMenuItem(MC_Component cc, M_Uint8* psz, MC_GrpImage img)
```

**설명**

메뉴 컴포넌트에 메뉴 아이템을 하나 추가한다.

지정된 컴포넌트가 메뉴 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는다.

넘기는 이미지는 메뉴 항목이 삭제될때 내부에서 파괴한다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `psz` — [in] 메뉴 아이템을 나타내는 문자열
- `img` — [in] 메뉴 아이템의 이미지
**반환 값**

메뉴의 인덱스(0부터 시작된다.)

**부작용**

없음

**참고 항목**

없음

### MC_uicGetMenuItem

**프로토타입**

```c
M_Int32 MC_uicGetMenuItem(MC_Component cc, M_Uint32 idx, M_Uint8* psz,
M_Int32 buflen, MC_GrpImage* img)
```

**설명**

메뉴 아이템을 가져 온다.

지정된 컴포넌트가 메뉴 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `idx` — [in] 가져올 메뉴 아이템의 인덱스
- `psz` — [out] 메뉴 아이템을 나타나는 문자열이 복사될 버퍼
- `buflen` — [in] 버퍼의 크기
- `img` — [out] 메뉴 아이템의 이미지
**반환 값**

1이면 성공 0 이하면 실패 M_E_SHOFTBUF: psz으로 넘기는 버퍼 크기가 작은 경우

**부작용**

없음

**참고 항목**

없음

### MC_uicRemoveMenuItem

**프로토타입**

```c
M_Int32 MC_uicRemoveMenuItem(MC_Component cc, M_Uint32 idx)
```

**설명**

지정된 메뉴 아이템을 삭제한다.

idx가 가리키는 메뉴 아이템을 삭제한다.

지정된 컴포넌트가 메뉴 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `idx` — [in] 삭제할 메뉴 아이템의 인덱스
**반환 값**

1이면 성공 0 이면 실패

**부작용**

없음

**참고 항목**

없음

### MC_uicSetActiveMenuItem

**프로토타입**

```c
M_Int32 MC_uicSetActiveMenuItem(MC_Component cc, M_Int32 idx)
```

**설명**

지정된 메뉴 아이템을 활성화시킨다.

지정된 컴포넌트가 메뉴 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는다.

만일 idx 값이 메뉴 항목의 범위를 벗어 나면, 이 함수는 아무런 역할을 하지 않 는다. 만일 선택되지 않은 상태로 두려면 idx을 -1로 지정하시면 된다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `idx` — [in] 메뉴 아이템의 인덱스
**반환 값**

이전에 활성화되었던 메뉴의 인덱스를 넘겨준다.

**부작용**

없음

**참고 항목**

없음

### MC_uicGetActiveMenuItem

**프로토타입**

```c
M_Int32 MC_uicGetActiveMenuItem(MC_Component cc)
```

**설명**

활성화된 메뉴 아이템을 인덱스를 돌려준다.

지정된 컴포넌트가 메뉴 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `cc` — [in] 컴포넌트
**반환 값**

활성화된 메뉴 아이템의 인덱스 -1 : 활성화된 메뉴가 없는 경우

**부작용**

없음

**참고 항목**

없음

### MC_uicInsertText

**프로토타입**

```c
M_Int32 MC_uicInsertText(MC_Component cc, M_Int32 idx, M_Uint8* psz, M_Int32
len)
```

**설명**

텍스트 컴포넌트에 문자열을 추가한다.

cc 가 가리키는 텍스트 컴포넌트의 idx 부분부터 시작하여 psz 의 내용을 len 만큼 삽입한다. idx 가 0 이하 이면 맨 앞이 추가되고, M_CuicGetMaxTextSize()로 넘어 오는 값 이상 이면 맨 뒤에 추가가 된다.

문자열은 내부에서 복사되므로 이 함수가 종료되고 나서 psz 가 가리키는 내용은 변경되어도 된다.

지정된 컴포넌트가 텍스트 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `idx` — [in] 문자열을 입력할 위치; 0부터 맨 마지막 문자열까지 된다.
- `psz` — [in] 복사될 문자열
- `len` — [in] 문자열의 길이
**반환 값**

컴포넌트에 복사된 문자열의 길이 메모리가 부족한 경우 len보다 작은 값이 나올 수 있다.

**부작용**

없음

**참고 항목**

없음

### MC_uicDeleteText

**프로토타입**

```c
void MC_uicDeleteText(MC_Component cc, M_Int32 idx, M_Int32 len)
```

**설명**

텍스트 컴포넌트의 특정 부분의 문자열을 삭제한다.

cc가 가리키는 텍스트 컴포넌트의 idx 부분부터 시작하여 길이가 len만큼을 삭제한 다.

만일 len이 -1이면 idx부터 문장 끝부분 까지가 삭제된다.

idx 가 내부 문자열의 범위를 벗어 나거나 len이 0 보다 작으면 이 함수는 아무런 역할을 하지 않는다.

지정된 컴포넌트가 텍스트 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `idx` — [in] 삭제할 문자열의 시작 위치
- `len` — [in] 문자열의 길이
**부작용**

없음

**참고 항목**

없음

### MC_uicGetMaxTextSize

**프로토타입**

```c
M_Int32 MC_uicGetMaxTextSize(MC_Component cc)
```

**설명**

텍스트 컴포넌트의 최대 문자열 크기를 얻어 온다.

바이트 단위의 최대 문자열 크기를 돌려준다.

지정된 컴포넌트가 텍스트 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다.

**매개 변수**

- `cc` — [in] 컴포넌트
**반환 값**

최대 문자열 크기

**부작용**

없음

**참고 항목**

없음

### MC_uicSetMaxTextSize

**프로토타입**

```c
M_Int32 MC_uicSetMaxTextSize(MC_Component cc, M_Int32 max)
```

**설명**

텍스트 컴포넌트의 최대 문자열 크기를 지정한다.

바이트 단위의 최대 문자열 크기를 지정한다.

지정된 컴포넌트가 텍스트 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다. 기본 크기는 256바이트 이다.

만일 이함수를 부를때 내부 문자열이 새로 정의된 max 보다 작다면, 내부 버퍼의 내용은 max크기로 짤려진다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `max` — [in] 최대 문자열 크기(바이트 단위)
**반환 값**

이전의 최대 문자열 크기; 메모리가 부족할때 M_E_NOMEMORY가 돌려짐

**부작용**

없음

**참고 항목**

없음

### MC_uicGetTextSize

**프로토타입**

```c
M_Int32 MC_uicGetTextSize(MC_Component cc)
```

**설명**

텍스트 컴포넌트의 내부의 문자열 길이를 얻어 온다.

지정된 컴포넌트가 텍스트 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다.

**매개 변수**

- `cc` — [in] 컴포넌트
**반환 값**

현재 문자열 길이

**부작용**

없음

**참고 항목**

없음

### MC_uicGetText

**프로토타입**

```c
M_Int32 MC_uicGetText(MC_Component cc, M_Int32 idx, M_Uint8* pszBuf, M_Int32
len)
```

**설명**

텍스트 컴포넌트의 내부의 문자열을 돌려준다.

cc가 가리키는 컴포넌트의 내부 문자열의 idx의 부분 부터 pszBuf 에 len 만큼 복 사해준다.

idx는 문자열의 범위를 벗어 나지 못하며, 만일 idx가 0보다 작은 경우에는 0으 로 보정되며, idx가 문자열 보다 큰경우에는 아무런 내용도 복사하지 않으며 0을 돌려준다.

지정된 컴포넌트가 텍스트 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `idx` — [in] 문자열의 시작 인덱스
- `psz` — [out] 복사될 버퍼
- `len` — [in] 버퍼의 크기
**반환 값**

복사된 문자열의 길이

**부작용**

없음

**참고 항목**

없음

### MC_uicAddListItem

**프로토타입**

```c
M_Int32 MC_uicAddListItem(MC_Component cc, M_Uint8* psz, MC_GrpImage img)
```

**설명**

리스트 컴포넌트에 리스트 아이템을 하나 추가한다.

지정된 컴포넌트가 리스트 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다.

넘기는 이미지는 리스트 항목이 삭제될 때 내부에서 파괴한다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `psz` — [in] 리스트 아이템을 나타내는 문자열
- `img` — [in] 리스트 아이템의 이미지
**반환 값**

리스트의 인덱스(0부터 시작된다.)

**부작용**

없음

**참고 항목**

없음

### MC_uicGetListItem

**프로토타입**

```c
M_Int32 MC_uicGet ListItem(MC_Component cc, M_Uint32 idx, M_Uint8* psz,
M_Int32 buflen, MC_GrpImage* img)
```

**설명**

리스트 아이템을 가져 온다.

지정된 컴포넌트가 리스트 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `idx` — [in] 가져올 리스트 아이템의 인덱스
- `psz` — [out] 리스트 아이템을 나타나는 문자열이 복사될 버퍼
- `buflen` — [in] 버퍼의 크기
- `img` — [out] 리스트 아이템의 이미지
**반환 값**

1이면 성공 0 이하면 실패 M_E_SHOFTBUF: psz으로 넘기는 버퍼 크기가 작은 경우

**부작용**

없음

**참고 항목**

없음

### MC_uicRemoveListItem

**프로토타입**

```c
M_Int32 MC_uicRemoveListItem(MC_Component cc, M_Uint32 idx)
```

**설명**

지정된 리스트 아이템을 삭제한다.

idx가 가리키는 리스트 아이템을 삭제한다.

지정된 컴포넌트가 리스트 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `idx` — [in] 삭제할 리스트 아이템의 인덱스
**반환 값**

1이면 성공 0 이면 실패

**부작용**

없음

**참고 항목**

없음

### MC_uicSetActiveListItem

**프로토타입**

```c
M_Int32 MC_uicSetActiveListItem(MC_Component cc, M_Int32 idx)
```

**설명**

지정된 리스트 아이템을 활성화시킨다.

지정된 컴포넌트가 리스트 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다. 만일 idx 값이 리스트 항목의 범위를 벗어 나면, 이 함수는 아무런 역할을 하 지 않는다. 만일 선택되지 않은 상태로 두려면 idx을 -1로 지정하시면 된다.

**매개 변수**

- `cc` — [in] 컴포넌트
- `idx` — [in] 리스트 아이템의 인덱스
**반환 값**

이전에 활성화되었던 리스트의 인덱스를 넘겨준다.

**부작용**

없음

**참고 항목**

없음

### MC_uicGetActiveListItem

**프로토타입**

```c
M_Int32 MC_uicGetActiveListItem(MC_Component cc)
```

**설명**

활성화된 리스트 아이템을 인덱스를 돌려준다.

지정된 컴포넌트가 리스트 컴포넌트가 아니면 이 함수는 아무런 역할을 하지 않는 다.

**매개 변수**

- `cc` — [in] 컴포넌트
**반환 값**

활성화된 리스트 아이템의 인덱스 -1 : 활성화된 리스트가 없는 경우

**부작용**

없음

**참고 항목**

없음
