# 4.3. System

표준 플랫폼 커널(Kernel) 에서 단말기의 정보 또는 이벤트를 입수하여 다음 수행 동작을 결정하고, 커널의 동작 수행 상태를 확인 하기 위해 디버깅 하는 콘솔을 지원하는 함수와 크리티컬 섹션(Critical Section) 을 보호 하기 위해서 단말기 운영체제에서 지원하는 락(lock) 메커니즘을 구현한 함수와 커널이 사용할 메모리 영역을 잡아주는 함수 등으로 구성되어 있다.

### 관련 자료형

운영체제에서 발생한 이벤트 중 플랫폼에 필요한 모든 이벤트는 `MH_pltEvent()` 함수를 통하여 플랫폼으로 전달된다. enum _MH_Event 는 플랫폼에 전달될 이벤트들 을 정의한다. enum _MH_Event 에 정의되어 있는 이벤트 중 더 세분화된 이벤트가 전달될 필요가 있을 때에는 각 모듈에서 enum MH_SUB_XXX_EVENT 와 같이 세부 이 벤트를 정의 한다.

예) MH_SERIAL_EVENT 의 세부이벤트 정의

```c
enum _MH_SUB_SERIAL_EVENT {
    MH_SERIAL_READ = 0,  // READ 인터럽트가 발생한 경우
    MH_SERIAL_WRITE,  // SERIAL에 write 할 수 있다는 event
    MH_SERIAL_ERROR,    // 시리얼 H/W 에러
};
```

정의된 세부 이벤트의 전달방법은 해당 모듈설명을 참고한다.

```c
enum _MH_Event {
    MH_EXIT_EVENT = 1,  // 시스템을 종료시켜주는 이벤트
    MH_KEY_PRESSEVENT,  // 키가 눌려 질 때 알려 주는 이벤트 
    MH_KEY_RELEASEEVENT,  // 키가 떼어 질 때 알려 주는 이벤트 
    MH_KEY_REPEATEVENT,  // 키를 누르고 있을 때 알려 주는 이벤트
    MH_TIMER_EVENT,  // 타이머가 만료될 때 알려 주는 이벤트
    MH_SMS_EVENT,  // SMS 메시지가 수신되었음을 알려 주는 이벤트
    MH_CALL_EVENT,  // 전화가 왔음을 알려 주는 이벤트
    MH_ANN_EVENT  //어넌시에이터(Annunciator) 정보가 변경 되었을 때 알려 주는 Event
    MH_NETWORK_EVENT,
    MH_SERIAL_EVENT,
    MH_MEDIA_EVENT
};
```

| 이벤트 | 세부 이벤트 | 이벤트 발생 함수/상황 |
|---|---|---|
| `MH_EXIT_EVENT` | - | 플랫폼 종료를 위하여 운영체제에서 발생시킴 |
| `MH_KEY_PRESSEVENT` | - | Key Press |
| `MH_KEY_RELEASEEVENT` | - | Key Release |
| `MH_KEY_REPEATEVENT` | - | 일정 시간 이상 key press 시 |
| `MH_TIMER_EVENT` | - | `MH_timerSet()` |
| `MH_SMS_EVENT` | `MH_SMS_NEW` | SMS 도착 |
| `MH_SMS_EVENT` | `MH_SMS_SEND_NOTIFY` | `MH_smsSend()` |
| `MH_CALL_EVENT` | `MH_CALL_INCOMING` | 전화가 왔을 때 발생 |
| `MH_CALL_EVENT` | `MH_CALL_NOTIFY` | `MH_callPlace()` |
| `MH_ANN_EVENT` | - | Annunciator와 관련된 상태 변화 |
| `MH_NETWORK_EVENT` | `MH_PPP_OPEN` | `MH_netConnect()` |
| `MH_NETWORK_EVENT` | `MH_PPP_CLOSE` | `MH_netClose()` |
| `MH_NETWORK_EVENT` | `MH_SOCKET_CONNECT` | `MH_netSocketConnect()` |
| `MH_NETWORK_EVENT` | `MH_SOCKET_CLOSE` | `MH_netSocketClose()` |
| `MH_NETWORK_EVENT` | `MH_SOCKET_READ` | `MH_netSocketRead()` |
| `MH_NETWORK_EVENT` | `MH_SOCKET_WRITE` | `MH_netSocketWrite()` |
| `MH_SERIAL_EVENT` | `MH_SERIAL_READ` | `MH_serialRead()` |
| `MH_SERIAL_EVENT` | `MH_SERIAL_WRITE` | `MH_serialWrite()` |
| `MH_SERIAL_EVENT` | `MH_SERIAL_ERROR` | 시리얼 H/W 문제 |
| `MH_SERIAL_EVENT` | `MH_SERIAL_DTR` | 시리얼 케이블의 상태 변화 |
| `MH_MEDIA_EVENT` | `MH_MDAEV_MEDIA_EMPTY` | `MH_mdaWriteData()` |
| `MH_MEDIA_EVENT` | `MH_MDAEV_MEDIA_FULL` | `MH_mdaRecord()` |

```c
enum _MH_KeyCode {
    MH_KEY_0         = '0',
    MH_KEY_1         = '1',
    MH_KEY_2         = '2',
    MH_KEY_3         = '3',
    MH_KEY_4         = '4',
    MH_KEY_5         = '5',
    MH_KEY_6         = '6',
    MH_KEY_7         = '7',
    MH_KEY_8         = '8',
    MH_KEY_9         = '9',
    MH_KEY_ASTERISK  = '*',
    MH_KEY_POUND     = '#',

    MH_KEY_UP        = -1,
    MH_KEY_DOWN      = -2,
    MH_KEY_LEFT      = -3,
    MH_KEY_RIGHT     = -4,
    MH_KEY_SELECT    = -5,
    MH_KEY_SOFT1     = -6,
    MH_KEY_SOFT2     = -7,
    MH_KEY_SOFT3     = -8,
    MH_KEY_SEND      = -10,
    MH_KEY_END       = -11,
    MH_KEY_POWER     = -12,
    MH_KEY_SIDE_UP   = -13,
    MH_KEY_SIDE_DOWN = -14,
    MH_KEY_SIDE_SEL  = -15,
    MH_KEY_CLEAR     = -16,
    MH_KEY_FLIPDOWN  = -17,
    MH_KEY_FLIPUP    = -18,
    MH_KEY_INVALID   = 0
};

enum MH_CallState {
    MH_CS_IDLE = 0,
    MH_CS_CALLING,
    MH_CS_CALLED,
    MH_CS_CALLREJECTED,
    MH_CS_INCOMMING,     /* 이때, 발신 번호가 매개변수로 전달되어야 함.(?) */
    MH_CS_OTHERCALL,     /* 통화 중 대기 */
    MH_CS_TRANSFERCALL,  /* 대기 통화로 전환 */
    MH_CS_END
};

enum _MH_Annunciator {
    MH_ANN_RSSI,        /* 현재 RSSI 수준이 갱신 (열거형의 경우 시작값 명시) */
    MH_ANN_BATT,        /* 현재 배터리 수준이 갱신 */
    MH_ANN_NOSERVICE,   /* 통화권 이탈 */
    MH_ANN_SILENTMODE,  /* 진동, 벨소리 모드 */
    MH_ANN_ALARM        /* 알람 설정 유무 */
};
typedef enum _MH_Annunciator MH_Annunciator;

struct _MH_AnnInfo {
    MH_Annunciator type;  /* Annunciator info type */
    M_Int32        data;  /* */
};
typedef struct _MH_AnnInfo MH_AnnInfo;
```

### MH_sysGetHeapBlock

**설명**

이 함수는 플랫폼이 사용할 휘발성 메모리의 크기와 시작번지를 얻어오는 함수 이 다.

이 메모리는 고정되어야 하며, 플랫폼을 제외한 타 소프트웨어 모듈이 메모리를 사용해서는 안된다.

**프로토타입**

```c
void MH_sysGetHeapBlock (M_Uint32* start, M_Uint32* size)
```

**매개 변수**

- `start` - [out] Heap 의 시작 번지 반환
- `size` - [out] Heap 의 사이즈 반환

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_sysGetInformation

**설명**

이 함수는 단말기의 시스템 정보를 얻어오는 함수이다.

반환할 값이 정수일 때는 10 진수 string 으로 변환하여 버퍼를 통하여 반환한다. 제조사나 이통사가 플랫폼에서 정의되지 않은 정보를 확장하고 싶은 경우, command 값을 추가하여 확장한다.

함수 사용 예)

```c
M_Char buf[16];
MH_sysGetInformation(”ESN”, buf, sizeof(buf));
```

**프로토타입**

```c
M_Int32 MH_sysGetInformation (M_Char* command, M_Char* buf, M_Int32 bufSize)
```

**매개 변수**

- `command` - [in] String 값
- `buf` - [out] 버퍼
- `butSize` - [out] 버퍼 크기

#### command 목록

| command | 비고 |
|---|---|
| `"ESN"` | ESN 번호 |
| `"NID"` | 네트워크 식별 (Network Identification) |
| `"SID"` | 시스템 식별 (System Identification) |
| `"BASEID"` | 기본 스테이션 식별 (Base station Identification) |
| `"BASELAT"` | 기본 스테이션 위도 (Base station Latitude) |
| `"BASELONG"` | 기본 스테이션 경도 (Base station longitude) |
| `"CURRENTCH"` | 현재 채널 번호 (Current Channel number) |
| `"PHONENUMBER"` | 전화 번호 |
| `"RSSILEVEL"` | 현재 RSSI 레벨 |
| `"BATTERYLEVEL"` | 현재 배터리 레벨 |
| `"MAXRSSILEVEL"` | 최대 RSSI 레벨 |
| `"MAXBATTLEVEL"` | 최대 배터리 레벨 |
| `"MAXSERIALNUM"` | 최대 지원되는 시리얼 포트 개수 |
| `"MAXSOCKETNUM"` | 최대 지원되는 소켓 개수 |
| `"MEDIADEVICES"` | 지원하는 미디어 device의 문자열. 여러 개일 경우 `,`로 구분함. 지원되는 device가 없으면 `M_E_NOTSUP`를 반환. (미리 정의된 문자열은 아래 별도 표 참조) |
| `"DNS"` | 도메인 네임 서버를 지정한다. IP 주소 문자열. 예) `"127.0.0.1"` |
| `"TIMEZONE"` | `"GMT+시:분"`, `"GMT-시:분"`과 같은 형태로 현재의 time zone을 반환한다. 시, 분은 각각 두 자리 문자열을 사용한다. 예) `"GMT+09:30"`, `"GMT-12:00"` |
| `"PHONEMODEL"` | 단말기의 모델 ID string (폰 모델) |
| `"KEYREPEAT"` | `"반복시작시간:반복주기시간"`, 단위는 ms이다. 지원하지 않으면 `M_E_NOTSUP` 반환할 수 있다. 예) `"600:250"` - 버튼이 눌려지고 600ms 후에 `MH_KEYREPEAT_EVENT`가 처음 발생한 후, 250ms마다 주기적으로 버튼이 떼어질 때까지 발생한다. |
| `"VIBRATORLEVEL"` | 하드웨어가 지원하는 진동 세기의 단계를 반환한다. (최소 0, 최대 100) 예) `"3"` 3단계 지원, `"1"` 1단계 지원 |
| `"VOLUMELEVEL"` | 하드웨어가 지원하는 볼륨 세기의 단계를 반환한다. (최소 0, 최대 100) 예) `"10"` 10단계 지원, `"4"` 4단계 지원 |

#### `MEDIADEVICES` - 미리 정의된 문자열

| 문자열 | device |
|---|---|
| `"Qualcomm_CMX"` | Qualcomm CMX |
| `"Yamaha_MA1"` | Yamaha MA1 |
| `"Yamaha_MA2"` | Yamaha MA2 |
| `"Yamaha_MA3"` | Yamaha MA3 |
| `"audio/MIDI"` | MIDI 포맷을 play할 수 있는 디바이스일 경우 |
| `"audio/MP3"` | MP3 포맷을 play할 수 있는 디바이스일 경우 |
| `"IS96"` | QCELP-8K |
| `"IS96A"` | QCELP-8K |
| `"IS733"` | QCELP-13K |
| `"IS127"` | EVRC-8K |

> **참고:** 디바이스가 미리 정의된 문자열을 지원할 시에는 정의된 문자열을 반환하고, 그렇지 않을 경우에는 벤더나 이통사에서 정의하여 확장한다. 지원되는 포맷이 하드웨어 종속적이 아닌 경우에는 `"audio/xxx"`와 MIME 타입에 따라 확장한다. 예) 운영체제가 CMX, MA1, EVRC-8K을 지원할 경우, 반환되는 문자열은 `"Qualcomm_CMX, Yamaha_MA1"`.

- `buf` - [out] 해당 데이터 정보를 저장할 버퍼. 모든 값은 string 으 로 반환된다.
- `bufSize` - [in] buf size

**반환 값**

성공

- 0

실패

- `M_E_INVALID` - 지원하지 않는 command 값
- `M_E_NOTSUP` - command 값에 대하여 반환할 문자열이 존재하지 않음
- `M_E_SHORTBUF` - 저장할 버퍼가 작음

**부작용**

없음

**참고 항목**

없음


### MH_sysSetInformation

**설명**

시스템 정보 값을 변경할 때 사용하는 함수이다. HAL 구현시 단말기 기본 소프트 웨어에 따라 변경 불가한 정보가 있을 수 있다.

**프로토타입**

```c
M_Int32 MH_sysSetInformation(M_Char* cmd, M_Char* value)
```

**매개 변수**

- `cmd` - [in] 변경하고자 하는 정보명.
- `value` - [in] cmd 에 해당하는 정보값을 나타내는 문자열

**반환 값**

성공

- 0

실패

- `M_E_ACCESS` - 변경할 수 없는 정보임.
- `M_E_INVALID` - cmd 값이나 value 값이 잘못됨.

**부작용**

없음

**참고 항목**

없음.

### MH_sysLock

**설명**

크리티컬 섹션(Critical Section)을 보호하기 위한 함수 이다.

플랫폼 외부 문맥(external context)의 진입을 금지하는 영역의 시작을 지정한다. `MH_sysUnlock` 에서 진입을 허용한다.

`MH_pltEvent()` 같은 함수는 운영체제가 플랫폼에 이벤트를 전달하기 위하여 부른 다. 운영체제가 `MH_pltEvent()` 를 부를 때는 운영체제 ISR(interrupt service routine)에서 부를 수도 있고, 플랫폼 태스크가 아닌 다른 태스그에서 부를 수도 있다. 이때 호출된 `MH_pltEvent()` 함수와 플랫폼의 context 에서 사용하는 영역간 에 크리티컬 섹션(Critical Section)이 발생한다. 포팅자는 `MH_sysLock()` 이 불려진 경우에는 `MH_sysUnlock()`이 불려질 때까지 운영체제가 `MH_pltEvent()`를 부르지 않도록 HAL 을 구현해야 한다.

`MH_sysLock()`, `MH_sysUnlock` 은 nested 되게 불릴 수 있다. 이때 맨 처음 `MH_sysLock()`이 불려질 때 lock 이 되고, 맨 마지막 `MH_sysUnlock` 이 불려질 때 lock 이 해제 되어야 한다.

**프로토타입**

```c
void MH_sysLock (void)
```

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MH_sysUnlock`

### MH_sysUnlock

**설명**

`MH_sysLock` 에서 진입 금지한 상태를 해제 한다.

**프로토타입**

```c
void MH_sysUnlock (void)
```

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MH_sysLock`

### MH_sysHalInit

**설명**

Hal 초기화 루틴 이다.

이 함수는 어떤 HAL API 도 사용되기 이전에 최초 호출 되어야 한다. HAL 에서 지원하는 API 중 초기화가 필요한 API 는 여기서 초기화 과정을 수행하도록 한다.

**프로토타입**

```c
void MH_sysHalInit (void)
```

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_sysHalExit

**설명**

플랫폼 종료시 호출되는 함수이다. HAL 계층에서 사용된 자원 해제 등 HAL 에 맞는 플랫폼 종료시 취해야 할 작업을 정의한다.

**프로토타입**

```c
void MH_sysHalExit()
```

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_sysWait

**설명**

Binary semaphore wait 기능이다.

플랫폼은 내부적으로 더 이상 처리할 일이 없을 때 이 함수를 부른다. HAL 은 이 함수가 불리면 태스크를 blocking 시켜 CPU power 를 소비하지 않도록 구현해야 한다.

**프로토타입**

```c
void MH_sysWait (void)
```

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_sysSignal

**설명**

Binary semaphore signal 기능이다.

이 함수가 불리면 `MH_sysWait()`에서 blocking 된 태스크를 깨워주어야 한다.

이 함수는 주로 `MH_pltEvent()`내에서 주로 사용한다. `MH_sysSignal()`은 ISR 안에서 불려도 동작하게 포팅 해야 한다.

**프로토타입**

```c
void MH_sysSignal (void)
```

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_debugPutChar

**설명**

플랫폼의 디버깅정보를 출력한다. 플랫폼의 표준출력은 모두 이 API 로 오게된다. HAL 구현자는 이 API 를 시리얼, 네트웍, 콘솔(console)등 적절한 곳으로 연결하여 메시지를 볼수 있다.

**프로토타입**

```c
void MH_debugPutChar(M_Char ch);
```

**매개 변수**

- `ch` - [in] 출력한 문자

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음
