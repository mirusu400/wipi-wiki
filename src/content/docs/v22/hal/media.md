---
title: "2.17. 매체 처리기"
---

사운드나 동영상 등의 모든 매체를 처리할 수 있는 매체 처리기를 지원하기 위한 API 다.. 매체 처리기에는 사운드장치, vocoder장치, 카메라장치 등이 있을 수 있다.

#### 관련 자료형

// 톤 값

```c
typedef enum _MH_mdaToneType {
MH_SND_TONE_0 = 0, // DTMF for 0 key
MH_SND_TONE_1, // DTMF for 1 key
MH_SND_TONE_2, // DTMF for 2 key
MH_SND_TONE_3, // DTMF for 3 key
MH_SND_TONE_4, // DTMF for 4 key
MH_SND_TONE_5, // DTMF for 5 key
MH_SND_TONE_6, // DTMF for 6 key
MH_SND_TONE_7, // DTMF for 7 key
MH_SND_TONE_8, // DTMF for 8 key
MH_SND_TONE_9, // DTMF for 9 key
MH_SND_TONE_A, // DTMF for A key
MH_SND_TONE_B, // DTMF for B key
MH_SND_TONE_C, // DTMF for C key
MH_SND_TONE_D, // DTMF for D key
MH_SND_TONE_POUND, // DTMF for # key
MH_SND_TONE_STAR, // DTMF for * key
MH_SND_NOTE_A4, // 440.0 Hz -Piano Notes-
MH_SND_NOTE_AS4, // 466.1 Hz
MH_SND_NOTE_B4, // 493.8 Hz
MH_SND_NOTE_C4, // 261.6 Hz
MH_SND_NOTE_CS4, // 277.18 Hz
MH_SND_NOTE_D4, // 293.6 Hz
MH_SND_NOTE_DS4, // 311.1 Hz
MH_SND_NOTE_E4, // 329.6 Hz
MH_SND_NOTE_F4, // 349.2 Hz
MH_SND_NOTE_FS4, // 369.9 Hz
MH_SND_NOTE_G4, // 391.9 Hz
MH_SND_NOTE_GS4, // 415.3 Hz
MH_SND_NOTE_A5, // 880.0 Hz
MH_SND_NOTE_AS5, // 932.2 Hz
MH_SND_NOTE_B5, // 987.7 Hz
MH_SND_NOTE_C5, // 523.2 Hz
MH_SND_NOTE_CS5, // 554.3 Hz
MH_SND_NOTE_D5, // 587.3 Hz
MH_SND_NOTE_DS5, // 622.2 Hz
MH_SND_NOTE_E5, // 659.2 Hz
MH_SND_NOTE_F5, // 698.5 Hz
MH_SND_NOTE_FS5, // 739.9 Hz
MH_SND_NOTE_G5, // 784.0 Hz
MH_SND_NOTE_GS5, // 830.6 Hz
MH_SND_NOTE_A6, // 1760.0 Hz
MH_SND_NOTE_AS6, // 1864.7 Hz
MH_SND_NOTE_B6, // 1975.5 Hz
MH_SND_NOTE_C6, // 1046.5 Hz
MH_SND_NOTE_CS6, // 1108.7 Hz
MH_SND_NOTE_D6, // 1174.6 Hz
MH_SND_NOTE_DS6, // 1244.3 Hz
MH_SND_NOTE_E6, // 1318.5 Hz
MH_SND_NOTE_F6, // 1397.0 Hz
MH_SND_NOTE_FS6, // 1479.9 Hz
MH_SND_NOTE_G6, // 1568.0 Hz
MH_SND_NOTE_GS6, // 1661.2 Hz
MH_SND_NOTE_A7, // 3520.0 Hz
MH_MDA_NOTE_AS7, // 3729.3 Hz
MH_MDA_NOTE_B7, // 3951.0 Hz
MH_SND_NOTE_C7, // 2093.1 Hz
MH_SND_NOTE_CS7, // 2217.4 Hz
MH_SND_NOTE_D7, // 2349.3 Hz
MH_SND_NOTE_DS7, // 2489.1 Hz
MH_SND_NOTE_E7, // 2637.0 Hz
MH_SND_NOTE_F7, // 2793.7 Hz
MH_SND_NOTE_FS, // 2959.9 Hz
MH_SND_NOTE_G7, // 3135.9 Hz
MH_SND_NOTE_GS7, // 3322.4 Hz
} MH_mdaToneType;
```

// 매체 처리기의 특성 구조체

```c
typedef enum _MH_MdaDevInfo {
// 스트리밍 재생 지원
MH_MDAINFO_STREAM_PLAY,
// 전달하는 버퍼내용을 복사하지 않고 그대로 사용함
MH_MDAINFO_CALL_BY_REFERENCE,
// 재생 혹은 녹음/녹화 중 pause/resume을 지원하는 매체 처리기
MH_MDAINFO_PAUSE_RESUME,
// seek을 지원하는 매체 처리기
MH_MDAINFO_SEEK,
// 스트리밍 방식의 녹음 및 녹화를 지원하는 매체 처리기
MH_MDAINFO_STREAM_RECORD,
// 좌우 사운드 밸런스 지원
MH_MDAINFO_BALANCE ,
// 동시 연주 지원
MH_MDAINFO_MIXING,
// 동시 연주/동기 재생 지원
MH_MDAINFO_MIXING_SYNC
// 스트리밍 방식이 아닌 녹음/녹화를 지원
MH_MDAINFO_RECORD
// 재생 중 pause/resume을 지원하는 매체 처리기
MH_MDAINFO_PLAY_PAUSE_RESUME
// 녹음/녹화 중 pause/resume을 지원하는 매체 처리기
MH_MDAINFO_RECORD_PAUSE_RESUME
} MH_MdaDevInfo;
```

// 미디어 이벤트 구조체

```c
typedef enum MH_SUB_MEDIA_EVENT {
MH_MDAEV_MEDIA_EMPTY, // 매체 처리기 재생버퍼가 비었음
MH_MDAEV_TONE_EMPTY, // 톤 재생버퍼가 비었음
MH_MDAEV_MEDIA_FULL, // 녹음/녹화 매체 처리기버퍼가
// 다 찼음 MH_MDAEV_MEDIA_ERROR, //
매체 처리기 문제가 발생
// 했음
MH_MDAEV_TONE_ERROR, // 톤 매체 재생기에 문제가 발생했음
MH_MDAEV_OEM_ERROR, // OEM에 의한 매체 재생 또는
// 녹음/녹화의 강제 종료가 발생했음
MH_MDAEV_MEDIA_END // 매체 처리기 내부 버퍼의 데이터
// 를 전부 재생하였음
// MH_MDACTRL_SET_STOP_TIME에 의해 설정된 지점에서 멈춤
MH_MDAEV_MEDIA_STOPED_AT_TIME
} MH_SUB_MEDIA_EVENT;
```

// 미디어 이벤트를 전달하는 구조체

```c
typedef struct MH_MediaEvent{
M_Int32 event; // MH_SUB_MEDIA_EVENT타입의 값
M_Int32 devID; // 이벤트를 발생시킨 매체 처리기 식별자
M_Int32 mdaID; // 이벤트를 발생시킨 매체 처리기 인스턴스 식별자.
M_Int32 size; // MH_MDAEV_MEDIA_EMPTY ,
// MH_MDAEV_TONE_EMPTY 인 경우, 매체 처리기
// 내부 버퍼에 받아 들일 수 있는 데이터 양,
// MH_MDAEV_MEDIA_FULL인 경우, 매체 처리기 내부
// 버퍼에 녹음/녹화된 데이터 양
} MH_MediaEvent;
```

// 미디어 컨트롤 명령 `MH_mdaControl()` 함수에서 사용 될 미디어 컨트롤 명령 각 mimetype 별로 지원해야 할 미디어 컨트롤 명령의 리스트는 `MH_mdaControl()` 의 참고 항목을 참조한다.

```c
typedef enum MH_MdaControl {
MH_MDACTRL_GET_MEDIA_TIME, // 미디어의 현재 재생
// 시간을 얻는다.
MH_MDACTRL_SET_SYNC, // 인스턴스간 동기 설정
MH_MDACTRL_GET_SYNC, // 동기되는 인스턴스 얻어옴
NH_MDACTRL_GET_STOP_TIME // 정지 재생 시점 얻어옴
MH_MDACTRL_SET_STOP_TIME, // 비디오의 재생 정지
// 지점을 설정한다.
MH_MDACTRL_CAPTURE_IMAGE // 정지 영상을 캡쳐한다.
MH_MDACTRL_GET_CAPTURE_IMAGE, // 캡쳐된 이미지 데이터를
// 얻어온다.
MH_MDACTRL_PREVIEW_START, // 카메라 프리뷰를 시작한다.
MH_MDACTRL_PREVIEW_STOP, // 카메라 프리뷰를 정지한다.
MH_MDACTRL_SET_MODE // 모드를 설정한다.
}MH_MdaControl;
```

// 매체 처리기 컨트롤 명령 `MH_mdaDevControl()` 함수에서 사용 될 매체 처리기 컨트롤 명령. 매체 처리기 컨트롤 명령은 매체 처리기 별로 적용되는 명령어이다. 각 mimetype 별로 지원해야 할 미디어 컨트롤 명령의 리스트는 `MH_mdaDevControl()` 의 참고 항목을 참조한다.

```c
typedef enum _MH_MdaDevControl {
// 최대 지원 인스턴스의 개수
MH_MDADEVCTRL_GET_INSTANCE_COUNT = 1001,
// 카메라의 전원 상태를 얻어온다.
MH_MDADEVCTRL_DEVICE_GET_STATUS,
// 카메라의 장착 여부를 탐지한다.
MH_MDADEVCTRL_DEVICE_DETECT,
// 카메라의 모델명을 얻는다
MH_MDADEVCTRL_DEVICE_MODEL,.
// OEM 에서 지원하는 모드의 이름리스트를 얻는다.
MH_MDADEVCTRL_GET_MODE_LIST } MH_MdaDevControl;
```

#### 모드 컨트롤 명령

모드란 매체 처리기 별 속성 정보로 이루어진 구조체를 말하며, 단말제조사는 이 모드 를 최소한 한 개 이상은 지원하여야 한다.

```c
typedef enum _MH_MdaModeControl {
MH_MDAMODECTRL_GET,
MH_MDAMODECTRL_SET
} MH_MdaModeControl;
```

#### 모드 컨트롤 명령에서 사용되는 속성 식별자

`MH_mdaModeControl()` 함수에서 사용되는 속성 식별자

```c
typedef enum _MH_MdaModePID{
MH_MDAMODEPID_N_SAMPLE_PER_SEC,
MH_MDAMODEPID_N_CHANNELS,
MH_MDAMODEPID_N_BIT_PER_SAMPLE,
MH_MDAMODEPID_BALANCE,
MH_MDAMODEPID_POSITION_X,
MH_MDAMODEPID_POSITION_Y,
MH_MDAMODEPID_WIDTH,
MH_MDAMODEPID_HEIGHT,
MH_MDAMODEPID_AXIS,
MH_MDAMODEPID_BRIGHT,
MH_MDAMODEPID_MAGPOWER,
MH_MDAMODEPID_RESOLUTION_X
MH_MDAMODEPID_RESOLUTION_Y
MH_MDAMODEPID_YUV_RESOLUTION_X,
MH_MDAMODEPID_YUV_RESOLUTION Y,
MH_MDAMODEPID_FRAMERATE,
MH_MDAMODEPID_AXIS_PREVIEW,
MH_MDAMODEPID_AXIS_RECORD
} MH_MdaModePID;
```

### MH_mdaTonePlay

**프로토타입**

```c
M_Int32 MH_mdaTonePlay (MH_mdaToneType tone[], M_Int32 duration[],
M_Int32 number)
```

**설명**

여러 개의 톤 음 순서에 따라 연주한다. 톤 음 배열을 운영체제의 톤 재생 버퍼에 쓰고 복사된 톤 음의 개수를 반환한다. 톤 재생버퍼의 데이터가 모두 비워지기 전 적 절한 시점에 이벤트 `MH_MDAEV_TONE_EMPTY` 이벤트를 플랫폼에 전달해야 한다. 여기에서 적절한 시점이란 플랫폼이 이벤트 `MH_MDAEV_TONE_EMPTY` 이벤트를 받 고 데이터를 톤 재생버퍼에 복사하는 시간이상의 데이터가 남아있는 시점을 말한다. 만일 재생 중 문제가 발생한 경우 운영체제는 플랫폼에 `MH_MDAEV_TONE_ERROR` 이벤트를 전달해야 한다. 톤 재생기는 매체 처리기 식별자로 0을 사용한다. 그러므로 `MH_MDAEV_TONE_EMPTY` 이벤트를 플랫폼에 전달 시에, MH_MediaEvent구조체의 mdaID 필드가 0으로 채워 져야 한다. 일시정지/재개(pause/resume) 기능을 지원하는 톤 재생기인 경우, `MH_mdaTonePlay`()는 데이터를 톤 재생기 내부 버퍼에 복사 후 일 시 멈춤 상태가 되고, 재생은 MH_mdaResume이 불린 시점부터 일어나야 한다. 일시 정지/재개(pause/resume) 기능을 지원하지 않는 톤 재생기일 경우에는 `MH_mdaTonePlay()` 는 데이터를 톤 재생기 내부 버퍼에 복사하고, 곧 바로 재생도 시작 되어야 한다. 스트리밍 방식의 재생을 지원하지 않는 톤 재생기일 경우, 재생 중 `MH_mdaTonePlay` 가 호출되면 에러 값을 반환한다. 톤 재생기는 매체 처리기 식별자 로 0을 사용한다.

**매개 변수**

- `tones` - [in] 연주할 톤 음 배열에 대한 포인터, `MH_mdaToneType` 의 정의된 값이 올 수 있다.
- `duration` - [in] 연주할 시간에 대한 배열 포인터(시간 단위는 ms)
- `number` - [in] 연주할 톤 음의 개수
- `repeat` - [in] `TRUE` : 반복 연주 `FALSE` : 한번만 연주

**반환 값**

성공

시스템 톤 재생 버퍼에 실린 톤 개수
실패

- `M_E_INUSE` - 이미 재생 중에 있음
- `M_E_ERROR` - 기타 에러가 발생할 경우

**부작용**

없음

**참고 항목**

없음

### MH_mdaFreqTonePlay

**프로토타입**

```c
M_Int32 MH_mdaFreqTonePlay (M_Int32 hiFreq[], M_Int32 lowFreq[], M_Int32 duration[], M_Int32 number)
```

**설명**

여러 개의 프리퀀시 톤을 순서에 따라 연주한다. 이 함수는 프리퀀시 톤 배열을 운 영체제의 프리퀀시 톤 재생 버퍼에 싣고 그 실은 양을 반환 한다. 프리퀀시 톤 재생 버퍼의 데이터가 모두 비워지기 전 적절한 시점에 `MH_MDAEV_TONE_EMPTY` 이벤 트를 플랫폼에 전달해야 한다. 여기에서 적절한 시점이란 플랫폼이 `MH_MDAEV_TONE_EMPTY` 이벤트를 받고 데이터를 프리퀀시 톤 재생버퍼에 복사하 는 시간이상의 데이터가 남아있는 시점을 말한다. 만일 재생 중 문제가 발생한 경우 운영체제는 플랫폼에 `MH_MDAEV_TONE_ERROR` 이벤트를 전달해야 한다. 프리퀀시 톤 재생기는 매체 처리기 식별자로 0을 사용한다. 그러므로 `MH_MDAEV_TONE_EMPTY` 이벤트를 플랫폼에 전달 시, MH_MediaEvent구조체의 mdaID 필드가 0으로 채워져야 한다. 일시정지/재개(pause/resume) 기능을 지원하는 프리퀀시 톤 재생기인 경우, `MH_mdaFreqTonePlay()` 는 데이터를 프리퀜스 톤 재생기 의 내부 버퍼에 복사 후 일시 멈춤 상태가 되고, 재생은 MH_mdaResume이 불린 시 점부터 일어나야 한다. 일지정지/재개(pause/resume) 기능을 지원하지 않는 프리퀀시 톤 재생기일 경우 `MH_mdaFreqTonePlay`()는 데이터를 프리뭔스 톤 재생기의 내부 버 퍼에 복사하고, 곧 바로 재생이 시작되어야 한다. 스트리밍 방식의 재생을 지원하지 않는 프리퀀시 톤 재생기일 경우, 재생 중 `MH_mdaFreqTonePlay()` 가 호출되면 에러 값을 반환한다. 프리퀀시 톤 재생기는 매체 처리기 식별자로 0을 사용한다.

**매개 변수**

- `hiFreq` - [in] 연주할 고주파 톤 구조체 배열에 대한 포인터
- `lowFreq` - [in] 연주할 저주파 톤 구조체 배열에 대한 포인터
- `duration` - [in] 연주할 시간에 대한 배열 포인터 (시간 단위는 ms)
- `number` - [in] 톤 구조체의 개수
- `repeat` - [in] `TRUE` : 반복 연주 `FALSE` : 한번만 연주

**반환 값**

성공

시스템 톤 재생 버퍼에 실린 톤 개수
실패

- `M_E_INUSE` - 이미 재생 중에 있음
- `M_E_ERROR` - 기타 에러가 발생할 경우

**부작용**

없음

**참고 항목**

없음

### MH_mdaGetDeviceID

**프로토타입**

```c
M_Int32 MH_mdaGetDeviceID(M_Char* devName)
```

**설명**

매체 처리기의 식별자를 구한다. 운영체제에서 지원하는 매체 처리기 이름들은 `MH_sysGetInformation`()으로 구할 수 있다. `MH_sysGetInformation()` 함수의 매개변수 중 command의 값을 “MEDIADEVICES” 로 전달하여 얻어진 문자열이 매체 처리기 이름으로 사용될 수 있다. 톤재생기와 프리퀀시톤재생기는 매체 처리기 식별자를 0으 로 사용하므로 이 함수에서 부여하는 매체 처리기 식별자는 0보다 큰 숫자를 부여해 야 한다. 현재 WIPI 2.0 플랫폼에서 지원하는 매체의 이름을 참고 항목의 [표 2-17-1] 에 정의해 놓았으며, 아래의 정의된 매체 이외의 것을 지원할 경우에는 제조사에서 임의로 매체 처리기 이름을 정의해서 사용할 수 있다. 매개 변수로 전달되는 매체 처 리기 이름들은 MIME TYPE 형태를 지닌다.

**매개 변수**

- `devName` - [in] 지원을 묻는 매체 처리기 이름

**반환 값**

성공

매체 처리기 식별자
실패

- `M_E_NOTSUP` - 지원하지 않는 장치 이름

**부작용**

없음

**참고 항목**

`MH_sysGetInformation` [표 2-17-1] 플랫폼에서 지원하는 매체의 이름 mime type 설명 “Qualcomm_CMX” Qualcomm CMX “Yamaha_MA1” Yamaha MA1 “Yamaha_MA2” Yamaha MA2 “Yamaha_MA3” Yamaha MA3 Single Channel Format “Yamaha_MA5” “Yamaha_SMAF” Yamaha Single Channel Format “Yamaha_SMAF-Phrase” Yamaha Multi Channel Format “Yamaha_SMAF-Audio” Yamaha Audio Format “audio/MIDI” MIDI “audio/WAVE” WAVE “audio/MP3” MP3 “audio/TONE” Tone “audio/FREQTONE" Frequency Tone “IS96” QCELP-8K “IS96A” QCELP-8K “IS733” QCELP-13K “IS127” EVRC-8K “G.723.1” G.723.1 “audio/AAC” AAC “audio/AAC+” AAC+ “video/MPEG4” Mpeg4 “video/H.263” H.263 “video/H.264” H.264 “video/mjpeg” MJPEG “image/jpeg” JPEG

### MH_mdaGetDeviceInfo

**프로토타입**

```c
M_Int32 MH_mdaGetDeviceInfo(M_Int32 devID, M_Int32* rtnInfo)
```

**설명**

매체 처리기의 특성을 구한다. 매체 처리기 식별자 0은, 프리퀀시 톤재생기 혹은 톤 재생기를 나타낸다. 매체 처리기에서 지원할 수 있는 특성을 매개변수 rtnInfo 로 매 체 처리기 특성 열거 구조체(`MH_MdaDevInfo`)의 Bit Mask 의 OR 연산값으로 전달한 다. 1) `MH_MDAINFO_STREAM_PLAY` bit 매체 처리기 스트리밍 방식으로 재생을 하는 것을 지원하는 것을 말한다. 이것은 미 디어 재생 중에 `MH_mdaWriteData`(매체 처리기 식별자가 0인 경우, `MH_mdaTonePlay`, `MH_mdaFreqTonePlay` 함수)로 새로운 데이터를 매체 처리기 내부 버퍼에 복사할 수 있는 것을 말하며, 매체 처리기는 기존 데이타에 연속적으로 새로 운 데이터를 재생할 수 있어야 한다. 스트리밍 방식의 재생을 지원할 경우에는 `MH_MDAINFO_CALL_BY_REFERENCE` bit가 설정되어서는 안 된다. 2) `MH_MDAINFO_CALL_BY_REFERENCE` bit `MH_mdaWriteData`(매체 처리기 식별자가 0인 경우, `MH_mdaTonePlay`, `MH_mdaFreqTonePlay`)로 전달되는 데이터버퍼를 매체 처리기가 내부버퍼에 복사하 지 않고 그대로 사용함을 의미한다. 이 bit가 설정되지 않으면 전달되는 데이터가 내 부버퍼에 복사해야만 사용할 수 있다. 3) `MH_MDAINFO_PAUSE_RESUME` bit 매체 처리기가 재생 혹은 녹음/녹화 중 일시정지/재개(pause/resume)기능을 지원함을 의미한다. 4) `MH_MDAINFO_SEEK` bit 매체 처리기가 seek기능을 지원함을 의미한다. 5) `MH_MDAINFO_STREAM_RECORD` bit 매체 처리기가 스트리밍 방식의 녹음/녹화를 지원하는 것을 말한다. 이것은 녹음/녹화 중 에 MH_mdaCopy로 녹음/녹화 매체 처리기 내의 버퍼에서 녹음/녹화된 데이터를 플랫폼의 버퍼로 복사해 올 수 있는 것을 말하며, 녹음/녹화 매체 처리기는 비워진 버 퍼에 계속해서 연속적으로 데이터를 녹음/녹화할 수 있어야 한다. 6) `MH_MDAINFO_BALANCE` bit 매체 처리기가 좌우 사운드 밸런스 조절 기능을 제공할 경우 설정된다. 50을 기준 으로, 0이면 좌측 사운드만 활성화되고, 100이면 우측 사운드만 활성화된다. 7) `MH_MDAINFO_MIXING` bit 매체 처리기가 동시에 여러 개의 미디어 데이터를 재생할 수 있음을 의미한다. 동시 연주를 지원하지 않을 시에, 같은 타입의 매체 처리기에서 여러 개의 매체 처리기 인 스턴스를 생성하려고 하면, 해당 에러(`M_E_INPROGRESS`)를 반환해야 한다. 8) `MH_MDAINFO_MIXING_SYNC` bit 멀티 채널 동기 재생 기능을 말한다. 즉, 매체 처리기의 각 채널에서 여러 파일이 동 기를 맞춘 상태에서 재생 가능할 경우 셋팅된다 9) `MH_MDAINFO_RECORD` bit 스트리밍 방식이 아닌 녹음/녹화를 지원하는 것을 말한다. 이것은 녹음/녹화 중에 `MH_mdaCopy` 로 매체 처리기 내부 버퍼에서 녹음/녹화된 데이터를 버퍼로 복사해 올 수 없으며, 녹음/녹화 작업이 마쳐져야지만 데이터를 복사해 올 수가 있다. 10) `MH_MDAINFO_PLAY_PAUSE_RESUME` bit 매체 처리기가 재생 중 일시정지/재개(pause/resume)기능을 지원함을 의미한다. 11) `MH_MDAINFO_RECORD_PAUSE_RESUME` bit 매체 처리기가 녹음/녹화 중 일시정지/재개(pause/resume)기능을 지원함을 의미한다.

**매개 변수**

- `devID` - [in] `MH_mdaGetDeviceID()` 로 부터 반환 받은 매체 처리기 식별자
- `rtnInfo` - [out] 매체 처리기 특성 구조체(`MH_MdaDevInfo`)의 bit mask의 OR 연산 값

**반환 값**

성공

실패

- `M_E_ERROR` - 에러

**부작용**

없음

**참고 항목**

없음

### MH_mdaOpenDevice

**프로토타입**

```c
M_Int32 MH_mdaOpenDevice(M_Int32 devID, M_char* param)
```

**설명**

매개 변수로 넘어오는 매체 처리기 식별자와 연관이 있는 매체 처리기를 디폴트 설정 값으로 초기화 하고 연다. 그리고 해당 매체 처리기의 인스턴스의 식별자를 생성하여 반환한다. 이 때 반환되는 매체 처리기 인스턴스의 식별자는 매개 변수로 넘어오는 매체 처리기 식별자와 연관이 있음을 반드시 기억해 놓아야 한다. 이 매체 처리기 인 스턴스 식별자를 이용해서 `MH_mdaPlay()`, `MH_mdaPause()`.. 등등의 미디어 HAL API 에 접근을 할 시에 해당 매체 처리기 식별자를 알아야만 각 API 가 매체 처리기 별 로 동작을 할 수 있기 때문이다. 매체 처리기는 매체 처리기 인스턴스를 최소한 한 개는 가지고 있어야 하며, 만약 매체 처리기가 동시 연주를 지원한다면, 매체 처리기 인스턴스를 한 개 이상 가질 수 있다. 매개 변수 param 은 디바이스 장치를 열 때에 필요한 매개 변수가 전달 될 수 있다. 카메라의 경우, 이 함수를 통해 카메라의 전원이 켜져야 한다.

**매개 변수**

- `devID` - [in] `MH_mdaGetDeviceID()` 에서 반환 받은 매체 처리기 식별자
- `param` - [in] 매체 처리기를 열 때에, 필요한 매개 변수. 만약 매개변수가 필요하지 않은 경우에는 `NULL` 값을 입력합니다. 매체 처리기가 요구 하는 매개 변수에 따라서 매개 변수로 넘어오는 문자열의 접두어가 달라 질 수 있다. (아래의 표 참조) 이 매개 변수는 매체 처리기의 속성 정보를 의미하는 것은 아니다. 매체 처리기를 열 때에는 단말에서 디 폴트로 설정한 속성 값을 이용하여 장치를 열고, 그 속성 정보를 변 경하고 싶다면, `MH_mdaControl` 함수를 이용하여 설정 한다. 자세한 사항은 참고항목을 참조한다.

**반환 값**

성공

매체 처리기 인스턴스 식별자
실패

- `M_E_ERROR` - 에러가 발생한 경우
- `M_E_NOTSUP` - 지원하지 않는 매체 처리기
- `M_E_INPROGRESS` - 최대 인스턴스 개수를 초과하였을 때

**부작용**

없음

**참고 항목**

