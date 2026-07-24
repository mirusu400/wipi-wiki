---
title: "2.2. 플랫폼이 제공하는 API"
---

다음은 실제로 플랫폼이 해당 API를 구현하여, HAL 또는 타 태스크에서 사 용하는 함수들이다. 주로, 타 태스크에서 플랫폼 태스크로 이벤트를 전달 하거 나, 플랫폼을 시작하기 위해서 필요하다. HAL 포팅 시 구현해야 할 API가 아니 며 제공하는 플랫폼 라이브러리에 포함되어 있어야 한다.

### MH_pltEvent

**프로토타입**

```c
M_Boolean MH_pltEvent(MH_Event event, void *param)
```

**설명**

타 태스크에서 플랫폼으로 이벤트를 넘겨 줄 때 사용하는 함수이다. 함수를 호출할 때 함께 넘겨줄 이벤트에 대한 세부 정보는 하단 표의 매개변수 필드를 참조하면 된 다.

> **<표 2-2-1>HAL에서 전달 받는 이벤트에 대한 매개 변수**

이벤트 매개변수


- `MH_KEY_PRESSEVENTMH_KeyCode`
- `MH_KEY_RELEASEEVENT`
- `MH_KEY_REPEATEVENT` - `MH_EXIT_EVENT` `NULL` `MH_TIMER_EVENT` `NULL`
- `MH_SMS_EVENTMH_SMSEvent의포인터`
- `MH_ANN_EVENTMH_AnnInfo의포인터`
- `MH_CALL_EVENTMH_CallEvent의포인터` - `MH_NETWORK_EVENT` MH_NetEvent의 포인터
- `MH_SERIAL_EVENTMH_SerialEvent의포인터` - MH_ MEDIA _EVENT MH_MediaEvent의 포인터
- `MH_KEY_PRESSEVENT` - 단말기 버튼이 눌렸을 때 해당 버튼의 KeyCode값을 MH_KeyCode에 정의된 키로 변 경시킨 후 이 함수를 통해서 전달해야 한다.
- `MH_KEY_RELEASEEVENT` - 단말기 버튼이 떼어졌을 때 해당 버튼의 KeyCode값을 MH_KeyCode에 정의된 키로 변경시킨 후 이 함수를 통해서 전달한다.
- `MH_KEY_REPEATEVENT` - 단말기 버튼이 일정시간이상 눌려져 있으면, 일정시간 이후부터 주기적으로 MH_KEYREPEAT_EVENT를 단발기 버튼이 떼어질 때까지 플랫폼에 보낼 수 있다. 운영체제가 MH_KEYREPEAT_EVENT를 지원하면 `MH_sysGetInformation` ()에서 key repeat첫 발생시간과, 발생 주기(시간값)를 반환해야 한다.
- `MH_EXIT_EVENT` - 플랫폼의 수행을 종료할 때 전달한다.
- `MH_TIMER_EVENT` - `MH_timerSet`()에 의해 설정된 타이머가 만료될 때 전달한다.
- `MH_SMS_EVENT` - 새로운 SMS 메시지가 도착 할 때 전달한다.
- `MH_ANN_EVENT` - 단말기 표시 장치(Annunciator)의 정보가 갱신되는 경우 전달한다.
- `MH_CALL_EVENT` - 전화가 왔을 때 전달한다.
- `MH_NETWORK_EVENT` - 네트워크 이벤트를 전달한다.
- `MH_SERIAL_EVENT` - 시리얼 이벤트를 전달한다.
- `MH_MEDIA_EVENT` - 사운드 이벤트를 전달한다.

**매개 변수**

- `event` - [in] 플랫폼에게 넘겨주는 event
- `param` - [in] 해당 event에 대한 세부 정보값. 표의 매개변수 필드 참조.

**반환 값**

성공

- `TRUE`
실패

- `FALSE` - 지원하지 않는 이벤트이거나, 이벤트를 수신하는 큐가 full이다.

**부작용**

`MH_EXIT_EVENT` 이벤트가 전달되면 `MH_pltStart`()함수를 반환하고 플랫폼은 종료된다.

**참고 항목**

없음

### MH_pltStart

**프로토타입**

```c
M_Int32 MH_pltStart(M_Int32 JavaC, M_Char* programID, M_Char* path,
M_Char* args)
```

**설명**

HAL 에서 플랫폼을 시작하기 위한 함수이다. 이 함수가 호출되면 플랫폼이 수행되고, `MH_EXIT_EVENT` 이벤트를 받기 전 까지는 반환 되지 않는다. 매개변수는 플랫폼이 최초로 구동시킬 프로그램을 지정한다. 예) 애플리케이션 매니저가 자바로 구현되고, Main class이름이 “org.kwis.am.Main”이며 폰이미지에 같이 있을 경우 - `MH_pltStart`(0, “org.kwis.am.Main”, 0, 0); 예) 애플리케이션 매니저가 자바로 구현되고, Main class이름이 “org.kwis.am.Main”이며 /test/appManager.jar라는 독립된 파일로 존재할 경우 - `MH_pltStart`(0, “org.kwis.am.Main”, “/test/appManager.jar”, 0);

**매개 변수**

- `JavaC` - [in] 0이면 Java, 1이면 C프로그램
- `programID` - [in] java인 경우, 수행시킬 프로그램의 main class이름을 가리킨다. C인 경우, 수행시킬 프로그램을 지정할 수 있는 ID
- `path` - [in] path값은 수행시킬 프로그램의 독립된 file을 가리킨다. null이면 수행시킬 프로그램이 폰이미지 안에 같이 포함되어 있는 것을 의미한다.
- `args` - [in] 실행시킬 프로그램에 전달할 매개변수(전달할 매개변 수가 없으면 0)

**반환 값**

음수면 비정상 종료임

**부작용**

없음

**참고 항목**

없음
