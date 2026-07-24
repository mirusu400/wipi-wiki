---
title: "2.11. 매체 처리기"
---

사운드나 동영상 등의 모든 매체에 대해서 처리를 해주는 매체 처리기와 관련된 함 수와 톤 재생 및 음성녹음/녹화 및 볼륨 조절에 관련한 패키지 이다 사운드, 톤, 동영상 등의 모든 데이타는 클립(CLIP)으로 추상화되어 매체처리기에서 수행한다. 매체재생기에서 지원하는 타입은 `MC_knlGetSystemProperty`()의 "MEDIADEVICES"에 의해 구해진 타입들이다. 매체처리, 톤 재생, 녹음/녹화 등의 상태 변화는 등록하는 콜백 함수로 전달된다. 볼 륨 조절은 톤, 사운드, 녹음/녹화에 대해 각각 가능하다.

### MC_MDA_STATUS_ERROR

**프로토타입**

```c
#define MC_MDA_STATUS_ERROR
```

**설명**

오류로 인한 정지 상태.

### MC_MDA_STATUS_END_OF_DATA

**프로토타입**

```c
#define MC_MDA_STATUS_END_OF_DATA
```

**설명**

매체(혹은 톤)처리시 - 처리기가 매체(혹은 톤) 데이터의 마지막에 도달한 상태.

### MC_MDA_STATUS_START

**프로토타입**

```c
#define MC_MDA_STATUS_START
```

**설명**

매체(혹은 톤)처리시 - 매체(혹은 톤) 처리를 시작한 상태.

### MC_MDA_STATUS_STOP

**프로토타입**

```c
#define MC_MDA_STATUS_STOP
```

**설명**

매체(혹은 톤)처리시 - 매체(혹은 톤) 처리를 종료한 상태 녹음/녹화 시 – 녹음/녹화를 중단한 상태.

### MC_MDA_STATUS_PAUSE

**프로토타입**

```c
#define MC_MDA_STATUS_PAUSE
```

**설명**

매체(혹은 톤)처리시 - 매체(혹은 톤) 처리를 잠시 멈춘 상태 녹음/녹화 시 – 녹음/녹화를 잠시 멈춘 상태.

### MC_MDA_STATUS_RESUME

**프로토타입**

```c
#define MC_MDA_STATUS_RESUME
```

**설명**

매체(혹은 톤)처리시 - 잠시 멈춘 매체(혹은 톤) 처리를 재개한 상태 녹음/녹화 시 – 잠시 멈춘 녹음/녹화를 재개한 상태.

### MC_MDA_STATUS_RECORD

**프로토타입**

```c
#define MC_MDA_STATUS_RECORD
```

**설명**

녹음/녹화 시 – 녹음/녹화를 시작한 상태.

### MC_MDA_STATUS_FULL_OF_DATA

**프로토타입**

```c
#define MC_MDA_STATUS_FULL_OF_DATA
```

**설명**

녹음/녹화 시 – 클립내부버퍼가 완전히 채워진 상태.

### MC_MDA_STATUS_OEM_ERROR

**프로토타입**

```c
#define MC_MDA_STATUS_OEM_ERROR
```

**설명**

매체를 재생 혹은 녹음/녹화 중, 플랫폼이 백그라운드로 보내지면서, 재생 혹은 녹음/ 녹화 중이던 매체가 강제 종료될 때 발생한다.

#### 톤 노트값

```c
typedef enum _MC_MdaToneType {
MC_MDA_TONE_0 = 0 //DTMF for 0 key
MC_MDA_TONE_1 , //DTMF for 1 key
MC_MDA_TONE_2 , //DTMF for 2 key
MC_MDA_TONE_3 , //DTMF for 3 key
MC_MDA_TONE_4 , //DTMF for 4 key
MC_MDA_TONE_5 , //DTMF for 5 key
MC_MDA_TONE_6 , //DTMF for 6 key
MC_MDA_TONE_7 , //DTMF for 7 key
MC_MDA_TONE_8 , //DTMF for 8 key
MC_MDA_TONE_9 , //DTMF for 9 key
MC_MDA_TONE_A , //DTMF for A key
MC_MDA_TONE_B , //DTMF for B key
MC_MDA_TONE_C , //DTMF for C key
MC_MDA_TONE_D , //DTMF for D key
MC_MDA_TONE_POUND , //DTMF for # key
MC_MDA_TONE_STAR , //DTMF for * key
MC_MDA_NOTE_A4, // 440.0 Hz -Piano Notes-
MC_MDA_NOTE_AS4, // 466.1 Hz
MC_MDA_NOTE_B4, // 493.8 Hz
MC_MDA_NOTE_C4, // 523.2 Hz
MC_MDA_NOTE_CS4, // 554.3 Hz
MC_MDA_NOTE_D4, // 587.3 Hz
MC_MDA_NOTE_DS4, // 622.2 Hz
MC_MDA_NOTE_E4, // 659.2 Hz
MC_MDA_NOTE_F4, // 698.5 Hz
MC_MDA_NOTE_FS4, // 739.9 Hz
MC_MDA_NOTE_G4, // 784.0 Hz
MC_MDA_NOTE_GS4, // 830.6 Hz
MC_MDA_NOTE_A5, // 880.0 Hz
MC_MDA_NOTE_AS5, // 932.2 Hz
MC_MDA_NOTE_B5, // 987.7 Hz
MC_MDA_NOTE_C5, // 1046.5 Hz
MC_MDA_NOTE_CS5, // 1108.7 Hz
MC_MDA_NOTE_D5, // 1174.6 Hz
MC_MDA_NOTE_DS5, // 1244.3 Hz
MC_MDA_NOTE_E5, // 1318.5 Hz
MC_MDA_NOTE_F5, // 1397.5 Hz
MC_MDA_NOTE_FS5, // 1479.9 Hz
MC_MDA_NOTE_G5, // 1568.0 Hz
MC_MDA_NOTE_GS5, // 1661.2 Hz
MC_MDA_NOTE_A6, // 1760.0 Hz
MC_MDA_NOTE_AS6, // 1864.7 Hz
MC_MDA_NOTE_B6, // 1975.5 Hz
MC_MDA_NOTE_C6, // 2093.1 Hz
MC_MDA_NOTE_CS6, // 2217.4 Hz
MC_MDA_NOTE_D6, // 2349.3 Hz
MC_MDA_NOTE_DS6, // 2489.1 Hz
MC_MDA_NOTE_E6, // 2637.5 Hz
MC_MDA_NOTE_F6, // 2793.7 Hz
MC_MDA_NOTE_FS6, // 2959.9 Hz
MC_MDA_NOTE_G6, // 3135.9 Hz
MC_MDA_NOTE_GS6, // 3322.4 Hz
MC_MDA_NOTE_A7, // 3520.0 Hz
MC_MDA_NOTE_AS7, // 3729.3 Hz
MC_MDA_NOTE_B7, // 3951.0 Hz
MC_MDA_NOTE_C7 // 4186.0 Hz
} MC_MdaToneType;
```

톤 노트값의 열거형 소리의 음계를 나타낸다.

#### 매체 처리기의 특성 구조체

```c
typedef enum _MC_MdaDevInfo {
MC_MDAINFO_STREAM_PLAY,
MC_MDAINFO_CALL_BY_REFERENCE,
MC_MDAINFO_PAUSE_RESUME,
MC_MDAINFO_SEEK ,
MC_MDAINFO_STREAM_RECORD,
MC_MDAINFO_BALANCE,
MC_MDAINFO_MIXING,
MC_MDAINFO_MIXING_SYNC,
MC_MDAINFO_RECORD‟
MC_MDAINFO_PLAY_PAUSE_RESUME
MC_MDAINFO_RECORD_PAUSE_RESUME
} MC_MdaDevInfo;
```

미디어 특성 설명 `MC_MDAINFO_STREAM_PLAY` 매체 처리기가 스트리밍 방식으로 재생을 하는 것을 지원하는 것을 말한다. 스트리밍 방식의 재생을 지원 할 경우에는 `MC_MDAINFO_CALL_BY_REFERENCE` bit가 설정되어서는 안 된다 `MC_MDAINFO_CALL_BY_REFE` 미디어 데이터를 매체 처리기가 내부 버퍼에 복사하지 RENCE 않고 그대로 사용함을 의미한다. 이 bit가 설정되지 않 으면 전달되는 데이터가 내부버퍼에 복사되어 사용됨 을 의미한다. `MC_MDAINFO_PAUSE_RESUM` 매체 처리기가 재생 혹은 녹음/녹화 중 일시정지/재개 E (pause/resume)기능을 지원함을 의미한다. `MC_MDAINFO_SEEK` 매체 처리기가 seek기능을 지원함을 의미한다. `MC_MDAINFO_STREAM_RECO` 매체 처리기가 스트리밍 방식의 녹음/녹화를 지원하는 RD 것을 말한다. 이것은 녹음/녹화 중에 매체 처리기 내 부 버퍼에서 녹음/녹화된 데이터를 플랫폼의 버퍼로 복사해 올 수 있는 것을 말하며, 매체 처리기는 비워 진 버퍼에 계속해서 연속적으로 데이터를 녹음/녹화할 수 있어야 한다. `MC_MDAINFO_BALANCE` 매체 처리기가 좌우 사운드 밸런스 조절 기능을 제공 할 경우 설정된다. 50을 기준으로, 0이면 좌측 사운드 만 활성화되고, 100이면 우측 사운드만 활성화된다. `MC_MDAINFO_MIXING` 매체 처리기가 동시에 여러 개의 미디어 데이터를 재 생할 수 있음을 의미한다. 동시 연주를 지원하지 않을 시에, 같은 타입의 매체 처리기에서 여러 개의 매체 처리기 인스턴스를 생성하려고 하면, 해당 에러 (`M_E_INPROGRESS`)를 반환해야 한다 `MC_MDAINFO_MIXING_SYNC` 멀티 채널 동기 재생 기능을 말한다. 즉, 매체 처리기 의 각 채널에서 여러 파일이 동기를 맞춘 상태에서 재 생 가능할 경우 설정된다 `MC_MDAINFO_RECORD` 스트리밍 방식이 아닌 녹음/녹화를 지원하는 것을 말 한다. 이것은 녹음/녹화 중에 매체 처리기 내부 버퍼 에서 녹음/녹화된 데이터를 버퍼로 복사해 올 수 없으 며, 녹음/녹화 작업이 마쳐져야지만 데이터를 복사해 올 수가 있다. `MC_MDAINFO_PLAY_PAUSE_` 매체 처리기가 play 중 일시정지/재개(pause/resume) RESUME 기능을 지원함을 의미한다. `MC_MDAINFO_RECORD_PAU` 매체 처리기가 record 중 일시정지/재개 SE_RESUME (pause/resume)기능을 지원함을 의미한다.

#### 매체 처리기 컨트롤 명령

```c
typedef enum _MC_MdaDevControl {
MC_MDADEVCTRL_GET_INSTANCE_COUNT = 1001,
MC_MDADEVCTRL_DEVICE_GET_STATUS,
MC_MDADEVCTRL_DEVICE_DETECT,
MC_MDADEVCTRL_DEVICE_MODEL,
MC_MDADEVCTRL_GET_MODE_LIST
} MC_MdaDevControl;
```

`MC_mdaClipDevControl()` 함수에서 사용 될 매체 처리기 컨트롤 명령 열거 구조체 매체 처리기 컨트롤 명령은 매체 처리기 별로 적용되는 명령어이다. 각 매체 처리기별로 지원해야 할 매체 처리기 컨트롤 명령의 종류는 `MC_mdaClipDevControl()` 의 참고 항목에 기술되어 있다.

#### 모드 컨트롤 명령

```c
typedef enum _MC_MdaModeControl {
MC_MDAMODECTRL_GET = 0,
MC_MDAMODECTRL_SET
} MC_MdaModeControl;
```

`MC_mdaClipModeControl()` 함수에서 사용되는 컨트롤 명령

#### 모드 컨트롤 명령에서 사용되는 속성 식별자

`MC_mdaClipModeControl()` 함수에서 사용되는 속성 식별자

```c
typedef enum _MC_MdaModePID{
MC_MDAMODEPID_N_SAMPLE_PER_SEC,
MC_MDAMODEPID_N_CHANNELS,
MC_MDAMODEPID_N_BIT_PER_SAMPLE,
MC_MDAMODEPID_BALANCE,
MC_MDAMODEPID_POSITION_X,
MC_MDAMODEPID_POSITION_Y,
MC_MDAMODEPID_WIDTH,
MC_MDAMODEPID_HEIGHT,
MC_MDAMODEPID_AXIS,
MC_MDAMODEPID_BRIGHT,
MC_MDAMODEPID_MAGPOWER,
MC_MDAMODEPID_RESOLUTION_X
MC_MDAMODEPID_RESOLUTION_Y
MC_MDAMODEPID_YUV_RESOLUTION_X,
MC_MDAMODEPID_YUV_RESOLUTION Y,
MC_MDAMODEPID_FRAMERATE,
MC_MDAMODEPID_AXIS_PREVIEW,
MC_MDAMODEPID_AXIS_RECORD
} MC_MdaModePID;
```

(다만, 각 속성 정보의 디폴트 값은 단말기에서의 특성에 따라 달라질 수 있다.) 속성이름 설명 `MC_MDAMODEPID_N_SA` 오디오 샘플 속도. 디폴트 값은 8000KHz 이다. MPLE_PER_SEC `MC_MDAMODEPID_N_BI` 오디오 샘플 크기. 디폴트 값은 8비트 이다. T_PER_SAMPLE 채널의 개수 ( 모노 / 스테레오 ), 디폴드 값은 모노 `MC_MDAMODEPID_N_CH` 이다. 모노이면 1의 값을 가지며, 스테레오이면 2 값 ANNELS 을 가진다. 사운드 밸런스. 50을 기준으로 50 보다 작은 값이면 `MC_MDAMODEPID_BALA` 좌측 사운드가 더 커지고, 50 보다 큰 값이면 우측 사 NCE 운드가 더 커진다. 밸런스 값의 영역은 0 에서 100 사이이다. 디폴트 값은 50이다. `MC_MDAMODEPID_POSI` 화면의 X 좌표 (픽셀단위) TION_X 디폴트 값은 0. `MC_MDAMODEPID_POSI` 화면의 Y 좌표 (픽셀단위) TION_Y 디폴트 값은 0. `MC_MDAMODEPID_WIDT` 화면의 너비(픽셀단위) H 디폴트 값은 전체 화면의 너비이다. `MC_MDAMODEPID_HEIG` 화면의 높이 (픽셀단위) HT 디폴트 값은 전체 화면의 높이이다. AXIS_PREVIEW PREVIEW 화면의 회전/반전 값, AXIS_RECORD 촬영시의 회전/반전 값, AXIS 촬영이 후의 재생화면의 회전/반전 값 (화면의 회전/반전 값은 구조체MH_MdaCameraSetAxis 를 참고한다.) 디폴트 값은 정상 화면이다.

```c
typedef enum MH_MdaCameraSetAxis {
MH_MDACAMERASETAXIS_NORMAL=0, //정상화면
MC_MDAMODEPID_AXIS
MH_MDACAMERASETAXIS_HORZ_REVERSE,//수평반전
MH_MDACAMERASETAXIS_VERT_REVERSE,//수직반전
MH_MDACAMERASETAXIS_BOTH_REVERSE,//수평수직반전
MH_MDACAMERASETAXIS_ROTATE90,//시계방향 90도 회전
MH_MDACAMERASETAXIS_ROTATE180,//시계방향180도회전
MH_MDACAMERASETAXIS_ROTATE270//시계방향270도회전
} MH_MdaCameraSetAxis;
```

`MC_MDAMODEPID_BRIG` 화면의 밝기.(퍼센트단위). 디폴트 값은 50이다. HT 화면의 배율. ( 퍼센트 단위, 100이면 보통 비율 , 200 `MC_MDAMODEPID_MAG` 이면 2배율, 400이면 4배율, 150 이면 1.5 배율) 디폴 POWER 트 값은 100이다. `MC_MDAMODEPID_RES` 해상도의 가로 값. (픽셀단위) OLUTION_X 해상도의 디폴트 값은 320*240 이다. `MC_MDAMODEPID_RES` 해상도의 세로 값.(픽셀단위) OLUTION_Y 해상도의 디폴트 값은 320*240 이다. `MC_MDAMODEPID_YUV_` YUV해상도의 가로.(픽셀단위) RESOLUTION_X 해상도의 디폴트 값은 320*240이다. `MC_MDAMODEPID_YUV_` YUV해상도의 세로 값.(픽셀단위) RESOLUTION_Y 해상도의 디폴트 값은 320*240이다. `MC_MDAMODEPID_FRA` 초당 프레임의 개수. 디폴트 값은 10 이다. MERATE `MC_MDAMODEPID_AXIS` _PREVIEW `MC_MDAMODEPID_AXIS` _RECORD (`MC_MdaClip`)

**프로토타입**

```c
typedef void MC_MdaClip
```

**설명**

매체 클립에 대한 식별

### MC_MDA_STATUS_END_OF_MEDIA

**프로토타입**

```c
#define MC_MDA_STATUS_END_OF_MEDIA
```

**설명**

매체 전체 데이터를 연주가 끝난 상태.

### MC_MDA_STATUS_STOPPED_AT_TIME

**프로토타입**

```c
#define MC_MDA_STATUS_STOPPED_AT_TIME
```

**설명**

`MC_MDACTRL_SET_STOP_TIME` 제어 명령을 이용해서 설정한 중지 시점에 매체가 중지 되었음 (MEDIACB)

**프로토타입**

```c
typedef void (*MEDIACB)(MC_MdaClip* clip, M_Int32 status)
```

**설명**

처리기의 상태가 변경될 때 불려지는 콜백함수. 상태 값은 매체 처리 상태를 참조.

**매개 변수**

- `clip` - 클립
- `status` - 매체처리기 상태

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipCreate

**프로토타입**

```c
MC_MdaClip* MC_mdaClipCreate(M_Char* mType, M_Int32 bufSize,
MEDIACB cb)
```

**설명**

특정 타입의 CLIP을 생성한다. 지원되는 타입은 `MC_knlGetSystemProperty`()의 "MEDIADEVICES"에 의해 구해진 타입들이다. 타입은 MIME에서 지원하는 타입일 경 우 "audio/xxx", "video/xxx"와 같이 MIME타입을 따른다. Clip 의 버퍼 크기는 입력하고자 하는 데이터의 전체 크기만큼 생성해야 한다. 콜백함수가 설정되지 않으면 매체 재생기의 상태변화가 전달되지 않는다.

**매개 변수**

- `mType` - [in] 매체타입
- `bufSzie` - [in] 버퍼 크기(CLIP내에 생성될 버퍼크기)
- `cb` - [in] 클립을 매체처리기에서 처리하는중 상태변화를 알려 줄 콜백함수

**반환 값**

성공

`MC_MdaClip` 객체 포인터
실패


**부작용**

없음

**참고 항목**

없음

### MC_mdaClipFree

**프로토타입**

```c
M_Int32 MC_mdaClipFree(MC_MdaClip* clip)
```

**설명**

클립에 할당된 모든 리소스를 해제한다.

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

실패

- `M_E_INUSE` - 클립을 재생중이거나 녹음/녹화중에 해제할려 고 시도함
- `M_E_INVALID` - clip 이 `NULL` 이면 반환

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipGetType

**프로토타입**

```c
M_Int32 MC_mdaClipGetType(MC_MdaClip* clip, M_Char* buf, M_Int32 bufSize)
```

**설명**

클립의 타입을 구한다.

**매개 변수**

- `clip` - [in] 클립
- `buf` - [out] 타입이 저장될 버퍼
- `bufSize` - [in] 복사할 버퍼 크기

**반환 값**

성공

실패

- `M_E_SHORTBUF` - 저장할 버퍼가 작음
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaGetInfo

**프로토타입**

```c
M_Int32 MC_mdaGetInfo(M_Char* type, M_Int32 *rtnInfo)
```

**설명**

단말이 지원하는 매체 처리기에서 클립의 매체 타입에 따라 지원 가능한 매체 특성 을 얻어온다.

**매개 변수**

- `type` - [in] 마임타입
- `rtnInfo` - [out] 매체 처리기 특성 구조체 (`MC_MdaDevInfo`)의 Bit Mask의 OR 연산값

**반환 값**

성공

실패

- `M_E_ERROR` - 매체 특성을 얻어오는데 실패
- `M_E_INVALID` - type 이 NULL일 때

**부작용**

없음

**참고 항목**

매체 처리기 특성 구조체(`MC_MdaDevInfo`)

### MC_mdaClipDevControl

**프로토타입**

```c
M_Int32 MC_mdaClipDevControl(MC_MdaClip* clip, MC_MdaDevControl cmd,
void* buf1, void* buf2)
```

**설명**

클립의 매체 처리기 제어 명령을 수행시킨다. 매체의 일반적인 기능(재생, 정지, 일시 정지) 이외에 제조사에서 지원해주는 장치적인 기능 명령을 수행 시킬 때 사용되어 진다. 예를 들면 제조사에서 카메라의 전원을 키는 명령을 지원한다면, 이 함수를 이 용하여 그 명령을 수행 할 수 있다. 제조사에서 지원하는 제어 명령이 매체 처리기 별로 수행이 되어야 하는 경우에는 이 함수를 사용하여 명령어가 수행되게 하고, 매 체 컨텐츠 별로 수행이 되어야 하는 경우에는 `MC_mdaClipControl()` 함수를 사용한다. 전자에 해당하는 명령어에는 카메라의 전원을 켜거나 끄는 명령어가 있을 수 있고, 후자에 해당하는 명령어에는 현재 재생되고 있는 매체 컨텐츠의 현재 재생시간을 얻 어오는 명령어가 있을 수 있다.

**매개 변수**

- `clip` - [in] 클립
- `cmd` - [in] 제어 명령
- `buf1` - [in] 제어 명령에서 사용할 수 있는 buf1
- `buf2` - [out] 제어 명령에서 사용할 수 있는 buf2

**반환 값**

성공

실패

- `M_E_ERROR` - command 수행에 실패하였음
- `M_E_NOTSUP` - 지원하지 않는 command
- `M_E_INVALID` - 잘못된 매개변수를 전달하였음
- `M_E_SHORTBUF` - 버퍼가 작음

**부작용**

단말 상황에 따라 함수 호출 반환값이 성공이더라도 바로 미디어 장치에 정보 가 적용되지 못할 수도 있다. 이 경우에 미디어 장치의 실제 사용 시점 이후 에 적용된 정보를 확인할 수 있다.

**참고 항목**

