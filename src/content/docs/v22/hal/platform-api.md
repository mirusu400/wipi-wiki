---
title: "2.2. 플랫폼이 제공하는 API"
---

다음은 실제로 플랫폼이 해당 API를 구현하여, HAL 또는 타 태스크에서 사용하는 함 수들이다. 주로, 타 태스크에서 플랫폼 태스크로 이벤트를 전달 하거나, 플랫폼을 시 작하기 위해서 필요하다. HAL 포팅 시 구현해야 할 API가 아니며 제공하는 플랫폼 라 이브러리에 포함되어 있어야 한다.

> **<표 2-2-1>HAL에서 전달 받는 이벤트에 대한 매개 변수**

이벤트 매개변수


- `MH_KEY_PRESSEVENTMH_KeyCode`
- `MH_KEY_RELEASEEVENT`
- `MH_KEY_REPEATEVENT` - `MH_EXIT_EVENT` `NULL` `MH_TIMER_EVENT` `NULL`
- `MH_SMS_EVENTMH_SMSEvent의포인터`
- `MH_ANN_EVENTMH_AnnInfo의포인터`
- `MH_CALL_EVENTMH_CallEvent의포인터` - `MH_NETWORK_EVENT` MH_NetEvent의 포인터
- `MH_SERIAL_EVENTMH_SerialEvent의포인터` - MH_ MEDIA _EVENT MH_MediaEvent의 포인터 `MH_IODEV_EVENT` MH_IODevEvent의 포인터 `MH_GPS_EVENT` MH_GPSEvent의 포인터
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
- `MH_IODEV_EVENT` - IO 장치의 이벤트를 전달한다.
- `MH_GPS_EVENT` - GPS 장치의 이벤트를 전달한다.

#### 관련 자료형

운영체제에서 발생한 이벤트 중 플랫폼에 필요한 모든 이벤트는 `MH_pltEvent()` 함수를 통하여 플랫폼으로 전달된다. enum _MH_Event는 플랫폼에 전달될 이벤트들을 정의한 다. enum _MH_Event에 정의되어 있는 이벤트 중 더 세분화된 이벤트가 전달될 필요가 있을 때에는 각 모듈에서 enum MH_SUB_XXX_EVENT와 같이 세부 이벤트를 정의 한 다. 예) MH_SERIAL_EVENT의 세부이벤트 정의

```c
enum _MH_SUB_SERIAL_EVENT{
    MH_SERIAL_READ = 0, // READ 인터럽트가 발생한 경우
    MH_SERIAL_WRITE, // SERIAL에 write할 수 있다는 event
    MH_SERIAL_ERROR, // 시리얼 H/W 에러
};
```

정의된 세부 이벤트의 전달방법은 해당 모듈설명을 참고한다.

```c
enum _MH_Event {
    MH_EXIT_EVENT = 1, // 시스템을 종료시켜주는 이벤트.
    MH_KEY_PRESSEVENT, // 키가 눌려 질 때 알려 주는 이벤트
    MH_KEY_RELEASEEVENT, // 키가 떼어 질 때 알려 주는 이벤트
    MH_KEY_REPEATEVENT, // 키를 누르고 있을 때 알려 주는 이벤트
    MH_TIMER_EVENT, // 타이머가 만료될 때 알려 주는 이벤트
    MH_SMS_EVENT, // SMS 메시지가 수신되었음을 알려 주는 이벤트
    MH_CALL_EVENT, // 전화가 왔음을 알려 주는 이벤트
    MH_ANN_EVENT, // 화면 표시 장치 정보가 변경 되었을 때
    // 알려주는 Event
    MH_NETWORK_EVENT, // 네트워크또는소켓의연결과 해제, 데이터
    // 쓰기 읽기 완료를 통지해 주는이벤트
    MH_SERIAL_EVENT, // 시리얼 읽기, 쓰기 및 에러 상태을 통지해
    // 주는 이벤트
    MH_MEDIA_EVENT, // 미디어 관련 버퍼의 상태 또는 재생
    // 상태를 통지해 주는 이벤트
    MH_IODEV_EVENT, // IO 장치의 연결과 해제,
    //데이터 쓰기 읽기완료를 통지해 주는이벤트.
    MH_GPS_EVENT // GPS 장치의 정보 수신 및
    // 상태를 통지해 주는 이벤트.
};
```

> **<표 2-2-2> 시스템 관련 이벤트**

이벤트 세부이벤트 이벤트 발생 함수/상황
`MH_EXIT_EVENT` 플랫폼 종료를 위하여 운
영체제에서 발생시킴


- `MH_KEY_PRESSEVENTKeyPress`
- `MH_KEY_RELEASEEVENTKeyRelease`
- `MH_KEY_REPEATEVENT일정시간이상keypress시` - `MH_TIMER_EVENT` `MH_timerSet()`
- `MH_SMS_EVENTMH_SMS_NEWSMS도착` - `MH_SMS_SEND_NOTIFY` `MH_smsSend()`
- `MH_CALL_EVENTMH_CALL_INCOMING전화가왔을때발생` - `MH_CALL_NOTIFY` `MH_callPlace()`
- `MH_ANN_EVENTAnnunciator와관련된상` - 태변화 `MH_NETWORK_EVENT` `MH_NETEV_NETWORK_OPEN` `MH_netConnect()` MH_ NETEV_NETWORK_CLOSE `MH_netClose()` MH_ NETEV_SOCKET_CONNECT `MH_netSocketConnect()` MH_ NETEV_SOCKET_CLOSE `MH_netSocketClose()` `MH_NETEV_SOCKET_READ` `MH_netSocketRead()` `MH_NETEV_SOCKET_WRITE` `MH_netSocketWrite()` `MH_SERIAL_EVENT` `MH_SERIAL_READ` `MH_serialRead()` `MH_SERIAL_WRITE` `MH_serialWrite()` `MH_SERIAL_ERROR` 시리얼 H/W 문제
- `MH_SERIAL_DTR시리얼케이블의상태변화` - `MH_MEDIA_EVENT` `MH_MDAEV_MEDIA_EMPTY` `MH_mdaWriteData()` `MH_mdaPlay()` `MH_MDAEV_MEDIA_FULL` `MH_mdaRecord()` `MH_MDAEV_TONE_EMPTY` `MH_mdaTonePlay()` `MH_mdaFreqTonePlay()` `MH_MDAEV_TONE_ERROR` `MH_mdaTonePlay()` `MH_mdaFreqTonePlay()` `MH_IODEV_EVENT` `MH_IODEVICEEV_CONNECT` (*DEVOPENFUN)()
- `MH_IODEVICEEV_TIMEROUT` - `MH_IODEVICEEV_READ` (*DEVREADFUN)() `MH_IODEVICEEV_WRITE` (*DEVWRITEFUN)() `MH_IODEVICEEV_CLOSE` (*DEVCLOSEFUN)()
- `MH_IODEVICEEV_ERROR`
- `MH_IODEVICEEV_OEMERROR` - `MH_GPS_EVENT` `MH_GPSEV_SUCCESS` GPS 정보 수신 성공
- `MH_GPSEV_FAILEDGPS정보수신실패`
- `MH_GPSEV_NOTAVAILABLEGPS장치없음`
- `MH_GPSEV_NOTACKNOWLEDGGPS인증실패` - ED

```c
enum _MH_KeyCode{
    MH_KEY_0 = '0',
    MH_KEY_1 = '1',
    MH_KEY_2 = '2',
    MH_KEY_3 = '3',
    MH_KEY_4 = '4',
    MH_KEY_5 = '5',
    MH_KEY_6 = '6',
    MH_KEY_7 = '7',
    MH_KEY_8 = '8',
    MH_KEY_9 = '9',
    MH_KEY_ASTERISK = '*',
    MH_KEY_POUND = '#',
    MH_KEY_UP = -1,
    MH_KEY_DOWN = -2,
    MH_KEY_LEFT = -3,
    MH_KEY_RIGHT = -4,
    MH_KEY_SELECT = -5,
    MH_KEY_SOFT1 = -6,
    MH_KEY_SOFT2 = -7,
    MH_KEY_SOFT3 = -8,
    MH_KEY_SEND = -10,
    MH_KEY_END = -11,
    MH_KEY_POWER = -12,
    MH_KEY_SIDE_UP = -13,
    MH_KEY_SIDE_DOWN = -14,
    MH_KEY_SIDE_SEL = -15,
    MH_KEY_CLEAR = -16,
    MH_KEY_FLIPDOWN = -17,
    MH_KEY_FLIPUP = -18,
    MH_KEY_CAMERA = -19,
    MH_KEY_INVALID = 0
};
enum MH_CallState {
    MH_CS_IDLE = 0,
    MH_CS_CALLING,
    MH_CS_CALLED,
    MH_CS_CALLREJECTED,
    MH_CS_INCOMING, // 이때, 발신 번호가 매개변수로 전달 되어야 함
    MH_CS_OTHERCALL, // 통화 중 대기
    MH_CS_TRANSFERCALL, // 대기 통화로 전환
    MH_CS_END
}
enum _MH_Annunciator{
    MH_ANN_RSSI, // 현재 RSSI 수준이 갱신 열거형의 경우 시작값 명시
    MH_ANN_BATT, // 현재 배터리 수준이 갱신
    MH_ANN_NOSERVICE, // 통화권 이탈
    MH_ANN_SILENTMODE, // 진동, 벨소리 모드
    MH_ANN_ALARM // 알람 설정 유무
}
typedef _MH_Annunciator MH_Annunciator;
struct _MH_AnnInfo{
    MH_Annunciator type; //Annunciator info type
    M_Int32 data;
}
typedef struct _MH_AnnInfo MH_AnnInfo;
```

### MH_pltEvent

**프로토타입**

```c
M_Boolean MH_pltEvent(MH_Event event, void *param)
```

**설명**

타 태스크에서 플랫폼으로 이벤트를 넘겨 줄 때 사용하는 함수이다. 함수를 호출할 때 함께 넘겨줄 이벤트에 대한 세부 정보는 하단 표의 매개변수 필드를 참조하면 된 다.

**매개 변수**

- `event` - [in] 플랫폼에게 넘겨주는 event
- `param` - [in] 해당 event에 대한 세부 정보값. 표의 매개변수 필드 참조.

**반환 값**

성공

- `TRUE`
실패

- `FALSE` - 지원하지 않는 이벤트이거나, 이벤트를 수신하는 큐가 full이다.

**부작용**

`MH_EXIT_EVENT` 이벤트가 전달되면 `MH_pltStart`()함수를 반환하고 플랫폼은 종 료된다.

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


### MH_pltRegIODevice

**프로토타입**

```c
M_Int32 MH_pltRegIODevice(MH_IODevice *dev)
```

**설명**

Generic I/O 장치를 플랫폼에 등록한다.

**매개 변수**

- `dev` - [in] 플랫폼에 등록할 장치의 정보 및 오퍼레이션이 저장된 구조체

**반환 값**

성공

실패

- `M_E_ERROR` - 등록 실패

**부작용**

없음

**참고 항목**

Generic I/O HAL API 관련 자료형 설명 부분의 `MH_IODevice` 구조체
