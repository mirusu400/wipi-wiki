---
title: "2.17. 매체 처리기"
---

미디어를 지원하기 위한 API들이다. 미디어장치는 데이터를 스트립으로 생 산/소비하는 장치들을 말한다. 이런 장치에는 사운드장치, vocoder장치, 카메라장 치 등이 있을 수 있다.

#### 관련 자료형

// 톤 값

```c
typedef enum MH_mdaToneType {
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
    MH_SND_NOTE_C4, // 261.6 Hz -Piano Notes-
    MH_SND_NOTE_CS4, // 277.18 Hz
    MH_SND_NOTE_D4, // 293.6 Hz
    MH_SND_NOTE_DS4, // 311.1 Hz
    MH_SND_NOTE_E4, // 329.6 Hz
    MH_SND_NOTE_F4, // 349.2 Hz
    MH_SND_NOTE_FS4, // 369.9 Hz
    MH_SND_NOTE_G4, // 391.9 Hz
    MH_SND_NOTE_GS4, // 415.3 Hz
    MH_SND_NOTE_A4, // 440.0 Hz
    MH_SND_NOTE_AS4, // 466.1 Hz
    MH_SND_NOTE_B4, // 493.8 Hz
    MH_SND_NOTE_C5, // 523.2 Hz
    MH_SND_NOTE_CS5, // 554.3 Hz
    MH_SND_NOTE_D5, // 587.3 Hz
    MH_SND_NOTE_DS5, // 622.2 Hz
    MH_SND_NOTE_E5, // 659.2 Hz
    MH_SND_NOTE_F5, // 698.5 Hz
    MH_SND_NOTE_FS5, // 739.9 Hz
    MH_SND_NOTE_G5, // 784.0 Hz
    MH_SND_NOTE_GS5, // 830.6 Hz
    MH_SND_NOTE_A5, // 880.0 Hz
    MH_SND_NOTE_AS5, // 932.2 Hz
    MH_SND_NOTE_B5, // 987.7 Hz
    MH_SND_NOTE_C6, // 1046.5 Hz
    MH_SND_NOTE_CS6, // 1108.7 Hz
    MH_SND_NOTE_D6, // 1174.6 Hz
    MH_SND_NOTE_DS6, // 1244.3 Hz
    MH_SND_NOTE_E6, // 1318.5 Hz
    MH_SND_NOTE_F6, // 1397.0 Hz
    MH_SND_NOTE_FS6, // 1479.9 Hz
    MH_SND_NOTE_G6, // 1568.0 Hz
    MH_SND_NOTE_GS6, // 1661.2 Hz
    MH_SND_NOTE_A6, // 1760.0 Hz
    MH_SND_NOTE_AS6, // 1864.7 Hz
    MH_SND_NOTE_B6, // 1975.5 Hz
    MH_SND_NOTE_C7, // 2093.1 Hz
    MH_SND_NOTE_CS7, // 2217.4 Hz
    MH_SND_NOTE_D7, // 2349.3 Hz
    MH_SND_NOTE_DS7, // 2489.1 Hz
    MH_SND_NOTE_E7, // 2637.0 Hz
    MH_SND_NOTE_F7, // 2793.7 Hz
    MH_SND_NOTE_FS, // 2959.9 Hz
    MH_SND_NOTE_G7, // 3135.9 Hz
    MH_SND_NOTE_GS7, // 3322.4 Hz
    MH_SND_NOTE_A7, // 3520.0 Hz
} MH_mdaToneType;
```

// 미디어 장치의 특성 구조체

```c
typedef enum MH_MdaDevInfo {
    MH_MDAINFO_STREAM_PLAY = 0x0001, // 스트리밍 재생 지원
    // 전달하는 버퍼내용을 복사하지 않고 그대로 사용함
    MH_MDAINFO_CALL_BY_REFERENCE = 0x0002,
    // pause/resume을 지원하는 장치
    MH_MDAINFO_PAUSE_RESUME = 0x0004,
    MH_MDAINFO_SEEK = 0x0008, // seek을 지원하는 장치
    // 스트리밍 방식의 녹음 및 녹화를 지원하는 장치
    MH_MDAINFO_STREAM_RECORD = 0x0010,
    // 좌우 사운드 밸런스 지원
    MH_MDAINFO_BALANCE = 0x0020,
    MH_MDAINFO_MIXING = 0x0040, // 동시 연주 지원
    MH_MDAINFO_MIXING_SYNC = 0x080, // 동시 연주/동기 재생 지원
} MH_MdaDevInfo;
```

// 미디어 이벤트 구조체

```c
typedef enum MH_SUB_MEDIA_EVENT {
    MH_MDAEV_MEDIA_EMPTY = 0 // 미디어장치 재생버퍼가 비었음
    MH_MDAEV_TONE_EMPTY, // 톤 재생버퍼가 비었음
    MH_MDAEV_MEDIA_FULL, // 녹음버퍼가 full 되었음
    MH_MDAEV_MEDIA_ERROR, // 미디어 디바이스에 문제가 발생
    // 했음
    MH_MDAEV_TONE_ERROR, // 톤 디바이스에 문제가 발생했음
    MH_MDAEV_OEM_ERROR, // OEM에 의한 미디어 재생 또는
    // 녹음의 강제 종료가 발생했음
} MH_SUB_MEDIA_EVENT;
```

// 미디어 이벤트를 전달하는 구조체

```c
typedef struct MH_MediaEvent{
    M_Int32 event; // MH_SUB_MEDIA_EVENT타입의 값
    M_Int32 devID; // 이벤트를 발생시킨 미디어 장치 식별자
    M_Int32 mdaID; // 이벤트를 발생시킨 미디어 장치 인스턴스 식별자.
    M_Int32 size; // MH_MDAEV_MEDIA_EMPTY ,
    // MH_MDAEV_TONE_EMPTY 인 경우, 미디어장치
    // 내부 버퍼에 받아 들일 수 있는 데이터 양,
    // MH_MDAEV_MEDIA_FULL인 경우, 미디어장치 내부
    // 버퍼에 녹음된 데이터 양
} MH_MediaEvent;
```

// 미디어 컨트롤 커맨드 : `MH_mdaControl()` 함수에서 사용 될 미디어 컨트롤 커맨드 각 mimetype 별로 지원해야 할 미디어 컨트롤 커맨드의 리스트는 `MH_mdaControl()` 의 참고 항목을 참조한다.

```c
typedef enum MH_MdaControl {
    MH_MDACTRL_GET_MEDIA_TIME, // 미디어의 현재 재생
    // 시간을 얻는다.
    MH_MDACTRL_SET_SYNC, // 인스턴스간 동기 설정
    MH_MDACTRL_GET_SYNC, // 동기되는 인스턴스 얻어옴
    MH_MDACTRL_SET_STOP_TIME, // 비디오의 재생 정지
    // 지점을 설정한다.
    MH_MDACTRL_GET_CAPTURE_IMAGE, // 정지 영상을 캡쳐한다.
    MH_MDACTRL_PREVIEW_START, // 카메라 프리뷰를 시작한다.
    MH_MDACTRL_PREVIEW_STOP, // 카메라 프리뷰를 정지한다.
    MH_MDACTRL_SET_MODE // 모드를 설정한다.
}MH_MdaControl;
```

// 미디어 장치 컨트롤 커맨드 : `MH_mdaDevControl()` 함수에서 사용 될 미디어 장치 컨트롤 커맨드. 미디어 장치 컨트롤 커맨드는 미디어 장치 별로 적용되는 명령어이다. 각 mimetype 별로 지원해야 할 미디어 컨트롤 커맨드의 리스트는 `MH_mdaDevControl()` 의 참고 항목을 참조한다.

```c
typedef enum _MH_MdaDevControl {
    // 최대 지원 인스턴스의 개수
    MH_MDADEVCTRL_GET_INSTANCE_COUNT = 1001,
    // 카메라의 전원 상태를 얻어온다.
    MH_MDADEVCTRL_DEVICE_GET_STATUS,
    MH_MDADEVCTRL_DEVICE_DETECT,
    // 카메라의 장착 여부를 탐지한다.
    MH_MDADEVCTRL_DEVICE_MODEL, // 카메라의 모델명을 얻는다.
    // OEM 에서 지원하는 모드의 이름리스트를 얻는다.
    MH_MDADEVCTRL_GET_MODE_LIST } MH_MdaDevControl;
```

#### 모드 컨트롤 커맨드

모드란 디바이스 장치별 속성 정보로 이루어진 구조체를 말하며, 단말제조 사는 이 모드를 최소한 한 개 이상은 지원하여야 한다.

```c
typedef enum MH_MdaModeControl {
    MH_MDAMODECTRL_GET,
    MH_MDAMODECTRL_SET
} MH_MdaModeControl;
```

#### 모드 컨트롤 커맨드에서 사용되는 속성 식별자

: `MH_mdaModeControl()` 함수에서 사용되는 속성 식별자

```c
typedef enum MH_MdaModePID{
    MH_MDAMODEPID_FORMAT_CODE,
    MH_MDAMODEPID_N_SAMPLE_PER_SEC,
    MH_MDAMODEPID_N_AVG_BYTES_PER_SEC,
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
} MH_MdaModePID;
```

#### 볼륨 카테고리

디폴트 볼륨과 뮤트 설정시 사용되는 볼륨의 카테고리

```c
typedef enum MH_MdaVolumeCategory {
    MH_MDAVOLCATE_GENERAL, // 일반 어플리케이션 음량
    MH_MDAVOLCATE_VOICE, // 통화 음량
    MH_MDAVOLCATE_RING, // 착신 벨 음량
    MH_MDAVOLCATE_KEYTION, // 키톤 음량
    MH_MDAVOLCATE_MESSAGE, // 메시지 착신 음량
    MH_MDAVOLCATE_ALARM, // 알람 음량
    MH_MDAVOLCATE_ALERT, // 경고음 음량
    MH_MDAVOLCATE_MMEDIA, // 멀티미디어 음량
    MH_MDAVOLCATE_GAME, // 게임 음량
} MH_MdaVolumeCategory;
```

### MH_mdaTonePlay

**프로토타입**

```c
M_Int32 MH_mdaTonePlay (MH_mdaToneType tone[], M_Int32 duration[], M_Int32 number, M_Boolean repeat)
```

**설명**

여러 개의 Tone을 순서에 따라 연주한다. 이 함수는 톤 배열을 운영체제의 톤 재생 버퍼에 싣고 그 실은 양을 반환한다. 톤 재생버퍼의 데이터가 모두 비워지기 전 적절 한 시점에 이벤트(`MH_MDAEV_TONE_EMPTY`)를 플랫폼에 전달해야 한다[적절한 시 점이란 플랫폼이 이벤트(`MH_MDAEV_TONE_EMPTY`)를 받고 데이터를 톤 재생버퍼 에 복사하는 시간이상의 데이터가 남아있는 시점]. 만일 재생 중 문제가 발생한 경우 운영체제는 플랫폼에 `MH_MDAEV_TONE_ERROR` 이벤트를 전달해야 한다. 톤 재생 기는 mdaID를 0으로 사용하고, 이벤트(`MH_MDAEV_TONE_EMPTY`)를 플랫폼에 전달 시에, MH_MediaEvent구조체의 mdaID field가 0으로 채워 져야 한다. pause/resume을 지원하는 톤 재생기인 경우, `MH_mdaTonePlay` 는 데이터를 사운드장치에 복사 후 일 시 멈춤 상태가 되고, 재생은 MH_mdaResume이 불린 시점부터 일어나야 한다. pause/resume을 지원하지 않는 톤 재생기일 경우에는 `MH_mdaTonePlay` 는 데이터 를 사운드장치에 복사하고, 곧 바로 재생도 시작 되어야 한다. 스트리밍을 지원하지 않는 톤 재생기일 경우, 재생 중 `MH_mdaTonePlay` 가 호출되면 에러 값을 반환한다. 톤 재생기는 미디어 디바이스 식별자로 0을 사용한다.

**매개 변수**

- `tones` - [in] 연주할 톤 구조체 배열에 대한 포인터
- `duration` - [in] 연주할 시간에 대한 배열 포인터(시간 단위는 ms)
- `number` - [in] 톤구조체의 개수
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
M_Int32 MH_mdaFreqTonePlay (M_Int32 hiFreq[], M_Int32 lowFreq[],
M_Int32 duration[], M_Int32 number, M_Boolean repeat)
```

**설명**

여러 개의 Frequency Tone을 순서에 따라 연주한다. 이 함수는 프리퀀시 톤 배열을 운영체제의 프리퀀시 톤 재생 버퍼에 싣고 그 실은 양을 리턴 한다. 프리퀀시 톤 재 생버퍼의 데이터가 모두 비워지기 전 적절한 시점에 이벤트 (`MH_MDAEV_TONE_EMPTY`)를 플랫폼에 전달해야 한다[적절한 시점이란 플랫폼이 이벤트(`MH_MDAEV_TONE_EMPTY`)를 받고 데이터를 프리퀀시 톤 재생버퍼에 복사 하는 시간이상의 데이터가 남아있는 시점]. 만일 재생 중 문제가 발생한 경우 운영체 제는 플랫폼에 `MH_MDAEV_TONE_ERROR` 이벤트를 전달해야 한다. 프리퀀시 톤 재 생기는 mdaID number 0을 사용하고, 이벤트(`MH_MDAEV_TONE_EMPTY`)를 플랫폼에 전달 시, MH_MediaEvent구조체의 mdaID field가 0로 채워져야한다. pause/resume을 지원하는 프리퀀시 톤 재생기인 경우, `MH_mdaFreqTonePlay` 는 데이터를 사운드장치 에 복사 후 일시 멈춤 상태가 되고, 재생은 MH_mdaResume이 불린 시점부터 일어나 야 한다. pause/resume을 지원하지 않는 프리퀀시 톤 재생기일 경우 `MH_mdaFreqTonePlay` 는 데이터를 사운드장치에 복사하고, 곧 바로 재생도 시작되 어야 한다. 스트리밍을 지원하지 않는 프리퀀시 톤 재생기일 경우, 재생 중 `MH_mdaFreqTonePlay` 가 호출되면 에러 값을 반환한다. 프리퀀시 톤 재생기는 미디 어 디바이스 식별자로 0을 사용한다.

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

미디어 장치의 식별자를 구한다. 운영체제에서 지원하는 미디어 장치 이름들은 `MH_sysGetInformation`()으로 구할 수 있다. MH_sysGetInformation의 command매개변 수 중 “MEDIADEVICES” 로 얻어진 문자열이 미디어 장치 이름으로 사용될 수 있다. 톤재생기와 프리퀀시톤재생기는 devID number 0을 사용하므로 이 함수에서 부여하는 devID number는 0보다 큰 숫자를 부여해야 한다. 현재 WIPI 2.0 플랫폼에서 지원하 는 매체의 이름을 참고 항목의 [표 2-17-1] 에 정의해 놓았으며, 아래의 정의된 매체 이외의 것을 지원할 경우에는 제조사에서 임의로 장치 이름을 정의해서 사용할 수 있 다. 매개 변수로 전달되는 미디어 장치 이름들은 MIME TYPE 형태를 지닌다.

**매개 변수**

- `devName` - [in] 지원을 묻는 미디어 장치 이름

**반환 값**

성공

미디어 장치 식별자
실패

- `M_E_NOTSUP` - 지원하지 않는 장치 이름

**부작용**

없음

**참고 항목**

`MH_sysGetInformation` [표 2-17-1] 플랫폼에서 지원하는 매체의 이름 mime type 설명 “Qualcomm_CMX” Qualcomm CMX “Yamaha_MA1” Yamaha MA1 “Yamaha_MA2” Yamaha MA2 “Yamaha_MA3” Yamaha MA3 Single Channel Format “Yamaha_MA5” “Yamaha_SMAF” Yamaha Single Channel Format “Yamaha_SMAF-Phrase” Yamaha Multi Channel Format “Yamaha_SMAF-Audio” Yamaha Audio Format “audio/MIDI” MIDI “audio/WAVE” WAVE “audio/MP3” MP3 “audio/TONE” Tone “audio/FREQTONE" Frequency Tone “IS96” QCELP-8K “IS96A” QCELP-8K “IS733” QCELP-13K “IS127” EVRC-8K “G.723.1” G.723.1 “audio/AAC” AAC “audio/AAC+” AAC+ “video/MPEG4” Mpeg4 “video/H.263” H.263 “video/H.264” H.264 “video/MJPEG” MJPEG “image/JPEG” JPEG

### MH_mdaGetDeviceInfo

**프로토타입**

```c
M_Int32 MH_mdaGetDeviceInfo(M_Int32 devID, M_Int32* rtnInfo)
```

**설명**

미디어 장치의 특성을 구한다. 장치 식별자 0은, 프리퀀시 톤재생기 혹은 톤 재생기 를 나타낸다. 1) `MH_MDAINFO_STREAM_PLAY` bit : 미디어 장치 스트리밍 방식으로 재생을 하는 것을 지원하는 것을 말한 다. 이것은 미디어 재생 중에 `MH_mdaWriteData`(장치 식별자가 0인 경우, `MH_mdaTonePlay`, `MH_mdaFreqTonePlay`)로 새로운 데이터를 미디어 장 치에 복사할 수 있는 것을 말하며, 미디어 장치는 기존 데이타에 연속적으 로 새로운 데이터를 재생할 수 있어 야 한다. 스트리밍을 지원할 경우에는 `MH_MDAINFO_CALL_BY_REFERENCE` bit가 설정되어서는 안 된다. 2) `MH_MDAINFO_CALL_BY_REFERENCE` bit : `MH_mdaWriteData`(장치 식별자가 0인 경우, `MH_mdaTonePlay`, `MH_mdaFreqTonePlay`)로 전달되는 데이터버퍼를 미디어장치가 내부버퍼에 복사하지 않고 그대로 사용함을 의미한다. 이 bit가 설정되지 않으면 전달되는 데이터가 내부버 퍼에 복사되어 사용됨을 의미한다. 3) `MH_MDAINFO_PAUSE_RESUME` bit : 미디어 장치가 pause/resume기능을 지원함을 의미한다. 4) `MH_MDAINFO_SEEK` bit : 미디어 장치가 seek기능을 지원함을 의미한다. 5) `MH_MDAINFO_STREAM_RECORD` bit : 미디어 장치가 스트리밍 녹음을 지원하는 것을 말한다. 이것은 녹음 중 에 MH_mdaCopy로 녹음장치내의 버퍼에서 녹음된 데이터를 플랫폼의 버퍼로 복사해 올 수 있는 것을 말하며, 녹음장치는 비워진 버퍼에 계속해서 연속적으로 데이터를 녹음 할 수 있어야 한다. 6) `MH_MDAINFO_BALANCE` bit : 미디어 장치가 좌우 사운드 밸런스 조절 기능을 제공할 경우 설정된다. 50을 기준 으로, 0이면 좌측 사운드만 활성화되고, 100이면 우측 사운드만 활성화된다. 7) `MH_MDAINFO_MIXING` bit : 미디어 장치가 동시에 여러 개의 미디어 데이터를 재생할 수 있음을 의미한다. 동시 연주를 지원하지 않을 시에, 같은 타입의 미디어 장치에서 여러 개의 미디어 장치 인 스턴스를 생성하려고 하면, 해당 에러(`M_E_INPROGRESS`)를 반환해야 한다. 8) `MH_MDAINFO_MIXING_SYNC` bit : 멀티 채널 동기 재생 기능을 말한다. 즉, 미디어 장치의 각 채널에서 여러 파일이 동기를 맞춘 상태에서 재생 가능할 경우 셋팅된다.

**매개 변수**

- `devID` - [in] `MH_mdaGetDeviceID()` 로 부터 반환 받은 미디어 장치 식별자
- `rtnInfo` - [out] MH_MdaDevInfo의 bit OR값

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
M_Int32 MH_mdaOpenDevice(M_Int32 devID, M_char* param);
```

**설명**

매개 변수로 넘어오는 미디어 장치 식별자와 연관이 있는 미디어 장치를 디폴트 설정 값으로 초기화 하고 연다. 그리고 해당 미디어 장치의 인스턴스의 식별자를 생성하여 반환한다. 이 때 반환되는 미디어 장치 인스턴스의 식별자는 매개 변수로 넘어오는 미디어 장치 식별자와 연관이 있음을 반드시 기억해 놓아야 한다. 이 미디어 장치 인 스턴스 식별자를 이용해서 `MH_mdaPlay()`, `MH_mdaPause()`.. 등등의 미디어 HAL API 에 접근을 할 시에 해당 미디어 장치 식별자를 알아야만 각 API 가 미디어 장치 별 로 동작을 할 수 있기 때문이다. 미디어 장치는 미디어 장치 인스턴스를 최소한 한 개는 가지고 있어야 하며, 만약 미디어 장치가 동시 연주를 지원한다면, 미디어 장치 인스턴스를 한 개 이상 가질 수 있다. 매개 변수 param 은 디바이스 장치를 열 때에 필요한 매개 변수가 전달 될 수 있다. 카메라의 경우, 이 함수를 통해 장치가 ON 되어야 한다.

**매개 변수**

- `devID` - [in] `MH_mdaGetDeviceID()` 에서 반환 받은 미디어 장치 식별자
- `param` - [in] 미디어 장치를 열 때에, 필요한 매개 변수. 만약 매개변수가 필 요 하지 않은 경우에는 `NULL` 값을 입력합니다. 디바이스가 요구 하는 매개 변수에 따라서 매개 변수로 넘어오는 String의 맨 처음 키워드 부분이 달라 질 수 있다. (아래의 표 참조) 이 매개 변 수는 미디어 장치의 속성 정보를 의미하는 것은 아니다. 미디어 장 치를 열 때에는 단말에서 디폴트로 설정한 속성 값을 이용하여 장치 를 열고, 그 속성 정보를 변경하고 싶다면, `MH_mdaControl` 함수 를 이용하여 설정 한다. 자세한 사항은 참고항목을 참조한다.

**반환 값**

성공

미디어 장치 인스턴스 식별자
실패

- `M_E_ERROR` - 에러가 발생한 경우
- `M_E_NOTSUP` - 지원하지 않는 미디어 장치
- `M_E_INPROGRESS` - 최대 인스턴스 개수를 초과하였을 때

**부작용**

없음

**참고 항목**


### MH_mdaCloseDevice

**프로토타입**

```c
M_Int32 MH_mdaCloseDevice (M_Int32 mdaID)
```

**설명**

매개 변수로 넘어오는 미디어 장치 인스턴스 식별자와 연관이 있는 미디어 장치 인스 턴스의 리소스를 해제한다. 해당 미디어 장치에 대한 인스턴스가 더 이상 존재 하지 않으면 미디어 장치를 해제하고 닫는다. 이미 닫혀있는 다바이스에 이 함수를 부를 경우, 아무 역할도 하지 않는다. 이 함수는 반드시 성공해야 한다 카메라의 경우, 이 함수를 통해 OFF되어야 한다.

**매개 변수**

- `mdaID` - [in] `MH_mdaOpenDevice`()에서 구해진 미디어 장치 인스턴스 식별 자

**반환 값**

성공

실패

- `M_E_INVALID` - 미디어 장치 인스턴스 식별자가 잘못된 경우
- `M_E_ERROR` - 기타 에러가 발생할 경우

**참고 항목**

`MH_mdaOpenDevice`

### MH_mdaWriteData

**프로토타입**

```c
M_Int32 MH_mdaWriteData (M_Int32 mdaID, void *buf, M_Int32 size)
```

**설명**

미디어 디바이스 내부버퍼에 연주할 데이터를 복사한다. 미디어 디바이스는 내부버퍼 가 비워지기전 적절한 시점에 이벤트(`MH_MDAEV_MEDIA_EMPTY`)를 플랫폼에 전달 해야 한다[적절한 시점이란 플랫폼이 이벤트(`MH_MDAEV_MEDIA_EMPTY`)를 받고 데 이터를 미디어 디바이스 내부버퍼에 복사하는 시간이상의 데이터가 남아있는 시점]. `MH_mdaStop`()가 수행되지 않고 디바이스 내부버퍼가 비워지게되면 미디어 디바이스 가 적절한 처리(묵음처리 등)를 해야 한다. 디바이스 내부버퍼가 수용할 수 있는 양보 다 많은 양의 데이터를 복사하려 할 때는 내부버퍼가 수용할 수 있는 양만큼 복사하 고 복사한 양을 반환한다. 만일 재생중 문제가 발생하면 `MH_MDAEV_MEDIA_ERROR` 이벤트를 플랫폼에 전달해야 한다. 스트리밍을 지원하 지 않는 미디어장치일 경우, 재생중 MH_mdaWriteData가 호출되면 에러 값을 반환한 다.

**매개 변수**

- `mdaID` - [in] `MH_mdaOpenDevice`()에서 구해진 미디어 장치 인스턴스 식별
- `buf` - [in] 데이터 버퍼
- `size` - [in] 복사할 길이

**반환 값**

성공

미디어 내부버퍼로 복사된 크기
실패

- `M_E_INUSE` - 이미 재생중에 있음
- `M_E_ERROR` - 기타 에러가 발생할 경우
- `M_E_NOTSUP` - 재생을 지원하지 않는 미디어 장치

**부작용**

없음

**참고 항목**

없음

### MH_mdaPlay

**프로토타입**

```c
M_Int32 MH_mdaPlay(M_Int32 mdaID, M_Boolean repeat)
```

**설명**

재생을 시작 한다. 미디어 디바이스는 `MH_mdaPlay`()함수가 호출되면 백그라운드 (background)로 재생을 시작한다. 내부버퍼가 일정량이상 비워지면 버퍼가 완전히 비 기전에 이벤트(`MH_MDAEV_MEDIA_EMPTY`)를 플랫폼에 전달하여 플랫폼이 계속해서 재생할 데이터를 미디어 디바이스에 복사할 수 있도록 한다. 만일 재생중에 문제가 발생할 경우 플랫폼에 `MH_MDAEV_MEDIA_ERROR` 이벤트가 전달되어야 한다. 미디 어 디바이스에서 재생하는 속도가 재생데이타를 플랫폼이 미디어 디바이스에 복사하 는 속도보다 빠르면 버퍼가 완전히 비게되는 상황이 발생할 수 있으나, 데이터가 다 시 복사되면 정상 동작하여야 한다.

**매개 변수**

- `mdaID` - [in] `MH_mdaOpenDevice`()에서 구해진 미디어 장치 인스턴스 식별자
- `repeat` - [in] `TRUE` : 반복연주 `FALSE` : 한번만 연주

**반환 값**

성공

실패

- `M_E_INPROGRESS` - 미디어장치가 이미 사용중인 경우
- `M_E_ERROR` - 기타 이유로 인한 실패
- `M_E_NOTSUP` - 재생을 지원하지 않는 미디어 장치

**부작용**

없음

**참고 항목**

없음

### MH_mdaPause

**프로토타입**

```c
M_Int32 MH_mdaPause(M_Int32 mdaID)
```

**설명**

재생중인 미디어를 일시 중지시킨다. 미디어 장치는 일시 중지시 MH_mdaResume가 불리면 재생을 재개할 수 있도록 내부상태(state)를 유지해야 한다. 이 함수 호출시 미디어장치가 재생상태가 아니면 `M_E_ERROR` 에러값을 반환해야 하고, pause/resume를 지원하지 않는 경우에는 에러 값(`M_E_NOTSUP`)을 반환한다.

**매개 변수**

- `mdaID` - [in] `MH_mdaOpenDevice`()에서 구해진 미디어 장치 인스턴스 식별자

**반환 값**

성공

실패

- `M_E_NOTSUP` - pause/resume을 지원하지 않는 미디어 장치
- `M_E_ERROR` - 미디어 장치가 재생 상태가 아닐 때 호출 되었을 경우

**부작용**

없음

**참고 항목**

없음

### MH_mdaResume

**프로토타입**

```c
M_Int32 MH_mdaResume(M_Int32 mdaID)
```

**설명**

일시 중지된 미디어재생을 재개한다. 이 함수 호출 시 일시 중지 상태가 아니면 `M_E_ERROR` 에러를 반환해야 하고, pause/resume를 지원하지 않는 경우에는 에러 값(`M_E_NOTSUP`)을 반환한다.

**매개 변수**

- `mdaID` - [in] `MH_mdaOpenDevice`()에서 구해진 미디어 장치 인스턴스 식별자

**반환 값**

성공

실패

- `M_E_NOTSUP` - pause/resume을 지원하지 않는 미디어 장치
- `M_E_ERROR` - 미디어 장치가 일시 중지 상태가 아닐 경우에, 이 함수가 호출되었을 경우

**부작용**

없음

**참고 항목**

없음

### MH_mdaSeek

**프로토타입**

```c
M_Int32 MH_mdaSeek(M_Int32 mdaID, M_Int32 seekTime)
```

**설명**

milli second단위로 재생을 시작할 지점을 설정한다. 이 함수 호출 시 pause상태가 아 니면 `M_E_ERROR` 에러를 반환해야 하고, seek를 지원하지 않는 미디어 장치인 경우 에는 에러 값을 반환한다.

**매개 변수**

- `mdaID` - [in] `MH_mdaOpenDevice`()에서 구해진 미디어 장치 인스턴스 식별자
- `seekTime` - [in] 연주할 지점 시간(ms), 0보다 작으면 시작점으로 지점이 설정되고, 데이터의 전체연주시간보다 큰 값이면 끝점으로 지점이 설정된다.

**반환 값**

성공

실패

- `M_E_NOTSUP` - seek을 지원하지 않는 미디어 장치
- `M_E_ERROR` - 미디어 장치가 일시 정지 상태가 아닌 경우에, 이 함수가 호출되었을 경우

**부작용**

없음

**참고 항목**

없음

### MH_mdaStop

**프로토타입**

```c
M_Int32 MH_mdaStop (M_Int32 mdaID)
```

**설명**

재생/녹음중인 미디어를 중지시킨다. 미디어 장치가 어떤 상태에 있던지 이 함수가 불 리면 재생중인 미디어가 중지된다. 중지되어 있는 미디어에 이 함수가 불리면 아무 역할도 하지 않는다. 이 함수는 항상 성공하여야 한다.

**매개 변수**

- `mdaID` - [in] `MH_mdaOpenDevice`()에서 구해진 미디어 장치 인스턴스 식별자

**반환 값**

성공

재생 중이 었을 경우 0 녹음 중이 었을 경우 그때까지 내부버퍼에 녹음된 데이터의 양
실패

- `M_E_ERROR` - 기타 이유로 인한 실패

**부작용**

없음

**참고 항목**

없음

### MH_mdaGetVolume

**프로토타입**

```c
M_Int32 MH_mdaGetVolume (M_Int32 devID)
```

**설명**

볼륨 소스로부터 볼륨 값을 읽어 온다. 미디어 장치마다 볼륨설정이 가능한 것은 미 디어 장치마다 볼륨값을 읽어오고, 그렇지 않은 것은 미디어장치 식별자가 서로 달라 도 같은 볼륨소스를 가리킬 수 있다. 볼륨의 최소값은 0, 최대값은 100이다. 반환되 는 볼륨값은 0 – 100사이의 값으로 환산하여 반환되어야 한다. 0-100사이값을 어느정 도의 볼륨세기와 일치시키는가는 아래의 예처럼 하드웨어가 지원하는 볼륨단계를 백 분율로 일치시킨것에 따른다. 하드웨어가 몇단계의 볼륨세기를 지원하는가는 `MH_sysGetInformation`()에서 반환한다. 예) 볼륨세기가 강, 약 두개인 하드웨어 => 1-50 : 약볼륨 51-100 : 강볼륨 볼륨세기가 강,중,약 세개인 하드웨어 => 1-33:약볼륨, 34-66:중볼륨, 67-100:강볼륨

**매개 변수**

- `devID` - [in] `MH_mdaGetDeviceID()` 로부터의 반환값인 미디어 장치 식별자

**반환 값**

성공

볼륨값
실패

- `M_E_NOTSUP` - 볼륨 값이 존재하지 않는 미디어 장치

**부작용**

없음

**참고 항목**

없음

### MH_mdaSetVolume

**프로토타입**

```c
M_Int32 MH_mdaSetVolume (M_Int32 devID, M_Int32 value)
```

**설명**

볼륨 소스에 값을 설정한다. 만약 볼륨 값이 최소볼륨 보다 작으면 최소볼륨으로 최 대보다 크면 최대 볼륨으로 설정된다. . 볼륨값의 최소는 0, 최대는 100이다. 미디어 장치마다 볼륨설정이 가능한 것은 미디어 장치마다 설정되고, 그렇지 않은 것은 미디 어장치 식별자가 서로 달라도 같은 볼륨소스를 가리킬 수 있다.

**매개 변수**

- `devID` - [in] `MH_mdaGetDeviceID()` 로부터의 반환값인 미디어 장치 식별자
- `value` - [in] 볼륨 값 (0-100사이의 볼륨값)

**반환 값**

성공

실패

- `M_E_NOTSUP` - 볼륨값 설정을 지원하지 않는 미디어 장치

**부작용**

없음

**참고 항목**

없음

### MH_mdaControl

**프로토타입**

```c
M_Int32 MH_mdaControl(M_Int32 mdaID, M_Int32 cmd, void* buf1, void* buf2);
```

**설명**

미디어장치 인스턴스에 컨트롤(control) 명령을 수행시킨다. 미디어 장치 인스턴스들에 대해 HAL 에서 제공하는 기능 의외에 새로운 기능을 사용 해야 할 경우가 있을 수 있을 것이다. 새로운 미디어장치가 플랫폼에 장착될 경우나 기존에 장착되어 있던 미디어 장치에 HAL 에서 정의되어 있지 않은 새로운 기능이 추가 되어 질 수 있다. 이러한 경우에는, 벤더가 제시하는 새로운 기능을 사용자 정의 함수로서 추가 해야 할 필요가 있다. 이 함수는 HAL 에서 정의 되어 있지 않은 새로 운 사용자 정의 함수를 추가해서 사용할 수 있도록 해준다. mime type 별 지원 가능한 미디어 컨트롤 커맨드는 아래와 같다. [표 2-17-2] MIME TYPE 별 지원 가능한 미디어 컨트롤 커맨드 mime type 지원 가능한 미디어 컨트롤 커맨드 “Qualcomm_CMX” `MH_MDACTRL_GET_MEDIA_TIME`, // 미디어의 현 재 재생 시간 “Yamaha_MA1” `MH_MDACTRL_SET_SYNC`, // 인스턴스간 동기 설 “Yamaha_MA2” 정 “Yamaha_MA3” `MH_MDACTRL_GET_SYNC`, // 동기되는 인스턴스 “Yamaha_MA5” 얻어옴 “Yamaha_SMAF” `MH_MDACTRL_SET_MODE` // 모드를 이름을 받아 서 설정함. “Yamaha_SMAF-Phrase” “Yamaha_SMAF-Audio” “audio/MIDI” “audio/WAVE” “audio/MP3” “audio/TONE” “audio/FREQTONE" “IS96” “IS96A” “IS733” “IS127” “G.723.1” “audio/AAC” “audio/AAC+” “video/MPEG4” `MH_MDACTRL_GET_MEDIA_TIME`, // 미디어의 현 재 재생 시간 “video/H.263” `MH_MDACTRL_PREVIEW_START`, // 카메라 프리뷰 “video/H.264” 를 시작한다. “video/MJPEG” `MH_MDACTRL_PREVIEW_STOP`, // 카메라 프리뷰 “image/JPEG” 를 정지한다. `MH_MDACTRL_GET_CAPTURE_IMAGE`, // 정지 영 상을 캡쳐한다. `MH_MDACTRL_SET_MODE` // 모드를 이름을 받아 서 설정함.

**매개 변수**

- `mdaID` - [in] `MH_mdaOpenDevice`()로부터 반환되는 디바이스 인스턴스 식별
- `cmd` - [in] 컨트롤(control) 명령
- `buf1` - [in] 컨트롤 명령에서 사용할 수 buf1
- `buf2` - [in/out] 컨트롤 명령에서 사용할 수 buf2

**반환 값**

성공

실패

- `M_E_ERROR` - 지원하지 않는 command이거나, command 수행에 실패하였음

**부작용**

없음

**참고 항목**

[표 2-17-3] 미디어 컨트롤 커맨드와 매개 변수에 대한 설명 Cmd `MH_MDACTRL_GET_MEDIA_TIME` buf1 없음 [out] 성공 : *(M_int32*) buf2 = 현재 재생 시간(단위 millisecond) buf2 실패 : *(`M_Int32`*) buf2 = `M_E_ERROR` 기타 에러 *(`M_Int32`*) buf2 = `M_E_NOTSUP` 지원안함 전체 재생 시간과 관계해서 현재 재생 시간(단위 millisecond)을 구

**설명**

한다. 비고 cmd `MH_MDACTRL_SET_SYNC` [in] *(`M_Int32`*) buf1[0] = 미디어 장치 인스턴스 식별자의 배열의 크기 *(`M_Int32`*) buf1[1] = 동기화 할 첫번째 슬레이브 미디어 인스턴스 buf1 식별자 *(`M_Int32`*) buf1[2] = 동기화 할 두번째 슬레이브 미디어 인스턴스 식별자 …… 배열의 크기만큼 반복 [out] 성공 : *(M_int32*) buf2 = 0 buf2 실패 : *(`M_Int32`*) buf2 = `M_E_ERROR` 기타 에러 *(`M_Int32`*) buf2 = `M_E_NOTSUP` 지원안함 멀티 채널에서 재생되는 미디어들 간의 채널 동기화를 설정한다. 설명 동기화 해제는 *(`M_Int32`*) buf1[0] = 미디어 장치 인스턴스 식별자 의 배열의 크기에 0을 넘겨 해제한다. 비고 cmd `MH_MDACTRL_GET_SYNC` [in] buf1 *(`M_Int32`*) buf1 = 최대 멀티 채널 배열의 크기 [out] 성공 : *((`M_Int32`*)buf2+0) = 동기화된 첫번째슬레이브 미디어인스 턴스식별자 *((`M_Int32`*)buf2+1) = 동기화된 두번째슬레이브 미디어인스 buf2 턴스식별자 ……배열의 크기만큼 반복 실패 : *(`M_Int32`*)buf2 = `M_E_NOTSUP` : 동기화를 지원하지 않음 *(`M_Int32`*)buf2 = `M_E_ERROR` : 기타 에러 멀티 채널에서 재생되는 미디어들 간의 채널 동기화 정보를 얻어온

**설명**

다. 비고 cmd `MH_MDACTRL_SET_STOP_TIME` (단위 milli second) [in] buf1 *(`M_Int32`*) buf1 = 재생을 멈출 시점(milli second 단위) [out] 성공 : *(`M_Int32`*) buf2 = 0 buf2 실패 : *(`M_Int32`*) buf2 = `M_E_NOTSUP` : 지원 안함 *(`M_Int32`*) buf2 = `M_E_ERROR` : 기타 에러 미디어의 전체 재생 시간과 관련하여, 재생을 멈출 시점을 설정한

**설명**

다. 비고 cmd `MH_MDACTRL_CAPTURE_IMAGE` [in] buf1 (`M_Char`*) buf1 = 캡쳐한 스크린 샷을 저장할 버퍼 [in] buf2 *(`M_Int32`*) buf2 = 캡쳐한 스크린 샷을 저장할 버퍼의 크기 설명 플레이 되고 있는 동영상의 스크린 샷을 캡쳐 한다. return value 성공 : 캡쳐된 스크린 샷의 크기 비고 실패 : `M_E_NOTSUP` : 지원 안함 `M_E_ERROR` : 기타 에러 cmd `MH_MDACTRL_PREVIEW_START` buf1 없음 [out] buf2 성공 : *(`M_Int32`*) buf2 = 0 실패 : *(`M_Int32`*) buf2 = `M_E_ERROR` 기타 에러 현재 설정된 화면 모드와 화면 사이즈에 따라 프리뷰 재생을 시작한

**설명**

다. 이미 프리뷰가 재생 중이라면 아무런 일도 하지 않는다. 비고 cmd `MH_MDACTRL_PREVIEW_STOP` buf1 없음 buf2 없음 프리뷰 재생을 하고 있는 상태에서 프리뷰 재생을 멈춘다. 만약 프

**설명**

리뷰가 재생 중이 아니면 아무런 일도 하지 않는다. 비고 이 함수는 무조건 성공해야 한다. cmd `MH_MDACTRL_SET_MODE` [in] buf1 *(`M_Char`*) buf1 : 모드 이름 [out] 성공 : *(`M_Int32`*) buf2 = 0 buf2 실패 : *(`M_Int32`*) buf2 = `M_E_ERROR` 기타 에러 *(`M_Int32`*) buf2 = `M_E_NOTSUP` 지원되지 않는 모드 이름 *(`M_Int32`*) buf2 = `M_E_INVALID` 잘못된 모드 이름 설명 buf1 로 넘어오는 모드 이름으로 모드를 설정한다. 비고

### MH_mdaDevControl

**프로토타입**

```c
M_Int32 MH_mdaDevControl(M_Int32 devID, M_Int32 cmd, void* buf1,
void* buf2);
```

**설명**

미디어장치에 컨트롤(control) 명령을 수행시킨다. 새로운 미디어장치가 플랫폼에 장착될 경우, HAL에서 정의되지 않은 새로운 기능들을 설정하거나 사용해야 할 경우가 있을 수 있다. 또는 기존에 장착되어 있던 미디어 장 치에 HAL 에서 정의되어 있지 않은 새로운 기능이 추가 되어 질 수 있다. 이러한 경 우에는, 벤더가 제시하는 새로운 기능을 사용자 정의 함수로서 추가 해야 할 필요가 있다. 이 함수는 HAL 에서 정의 되어 있지 않은 새로운 사용자 정의 함수를 추가해 서 사용할 수 있도록 해준다. 컨트롤 명령이 미디어 장치 별로 수행이 되어야 하는 경우에는 이 함수를 사용하여 명령어가 수행되게 하고, 미디어 장치 인스턴스 별로 수행이 되어야 하는 경우에는 `MH_mdaControl()` 함수를 사용한다. 전자에 해당하는 명령어에는 카메라의 전원을 켜 거나 끄는 명령어가 있을 수 있고, 후자에 해당하는 명령어에는 현재 재생되고 있는 미디어 컨텐츠의 현재 재생시간을 얻어오는 명령어가 있을 수 있다. mime type 별 지 원 가능한 미디어 장치 컨트롤 커맨드는 아래와 같다. [표 2-17-4] MIME TYPE 별 지원 가능한 미디어 장치 컨트롤 커맨드 mime type 지원 가능한 미디어 장치 컨트롤 커맨드 “Qualcomm_CMX” `MH_MDADEVCTRL_GET_INSTANCE_COUNT`, // 최 대 지원 인스턴스의 개수 “Yamaha_MA1” `MH_MDADEVCTRL_GET_MODE_LIST` // OEM 에서 “Yamaha_MA2” 지원하는 모드의 이름 리스트를 얻는다. “Yamaha_MA3” “Yamaha_MA5” “Yamaha_SMAF” “Yamaha_SMAF-Phrase” “Yamaha_SMAF-Audio” “audio/MIDI” “audio/WAVE” “audio/MP3” “audio/TONE” “audio/FREQTONE" “IS96” “IS96A” “IS733” “IS127” “G.723.1” “audio/AAC” “audio/AAC+” “video/MPEG4” “video/H.263” “video/H.264” “video/MJPEG” `MH_MDADEVCTRL_GET_INSTANCE_COUNT`, // 최 대 지원 인스턴스의 개수 ‘image/JPEG” `MH_MDADEVCTRL_DEVICE_GET_STATUS`, // 카메 라의 전원 상태를 얻어온다. `MH_MDADEVCTRL_DEVICE_DETECT`, // 카메라의 장착 여부를 탐지한다. `MH_MDADEVCTRL_DEVICE_MODEL`, // 카메라의 모델명을 얻는다. `MH_MDADEVCTRL_GET_MODE_LIST` // OEM 에서 지원하는 모드의 이름 리스트를 얻는다.

**매개 변수**

- `devID` - [in] `MH_mdaGetDeviceID()` 로 부터의 반환값인 디바이스 장치 식별자
- `cmd` - [in] 컨트롤(control) 명령
- `buf1` - [in] 컨트롤 명령에서 사용할 수 buf1
- `buf2` - [in/out] 컨트롤 명령에서 사용할 수 buf2

**반환 값**

성공

실패

- `M_E_ERROR` - 지원하지 않는 command이거나, command 수행에 실패하였음

**부작용**

없음

**참고 항목**

[표 2-17-5] 미디어 장치 컨트롤 커맨드와 매개 변수에 대한 설명 cmd `MH_MDADEVCTRL_GET_INSTANCE_COUNT` buf1 없음 [out] buf2 *(`M_Int32`*) buf2 : 지원하는 인스턴스의 개수 설명 이 장치에서 지원하는 인스턴스의 개수를 구한다. 비고 최소한 한 개는 지원을 해야 한다. cmd `MH_MDADEVCTRL_DEVICE_GET_STATUS` buf1 없음 [out] buf2 *(`M_Boolean`*) buf2 : `TRUE` : 미디어 장치의 전원이 켜져있음 *(`M_Boolean`*) buf2 : `FALSE` : 미디어 장치의 전원이 꺼져있음 설명 이 장치에 전원 상태를 얻어 온다. 비고 cmd `MH_MDADEVCTRL_DEVICE_DETECT` buf1 없음 [out] buf2 성공 : *(`M_Int32`*) buf2 = 0 실패 : *(`M_Int32`*) buf2 = `M_E_ERROR` 설명 내/외장 카메라를 디텍트(DETECT)한다. 비고 cmd `MH_MDADEVCTRL_DEVICE_MODEL` [in] buf1 *(`M_Int32`*) buf1 : 카메라 모델명의 길이 [out] 성공 : (`M_Char`*) buf2 = 카메라 모델명 buf2 실패 : *(`M_Int32`) buf2 = `M_E_LONGNAME` 모델명의 길이가 길 경 우 *(`M_Int32`) buf2 = `M_E_ERROR` 모델명을 알아올 수 없음 설명 카메라의 모델명을 얻는다 비고 cmd `MH_MDADEVCTRL_GET_MODE_LIST` 제조사에서 지원하는 모드의 이름리스트를 얻어오기위해 사용될 버 buf1 퍼의 사이즈 [out] 성공 : (`M_Char`*) buf2 = 제조사에서 지원하는 모드의 이름 리스트 buf2 실패 : *(`M_Int32`) buf2 = `M_E_ERROR` 기타 에러 *(`M_Int32`) buf2 = `M_E_SHORTBUF` 버퍼의 크기가 작음 제조사에서 지원하는 모드의 이름 리스트를 얻어온다. 여기에서 모 드란 미디어 디바이스의 일반적인 속성 데이터로 구성되어진 구조체 를 의미하며, 모드 구조체의 값을 얻어오거나, 수정할 때에는 `MH_mdaModeControl()` 함수를 이용해서 할 수 있다. 디바이스 장 설명 치별 일반적인 속성들은 이미 정의 되어 있으며, 이통사나 제조사의 필요에 의해 특정 속성들을 추가하여 사용할 수도 있다. 지원되는 모드가 여러가지일 경우, 모드 이름과 이름 사이의 ‘,’ 을 삽입하여 모드 이름을 구분할 수 있도록 한다. 예 :“DEFAULT_MODE,SKT_MODE,LG_MODE” 비고 모드는 최소 한 개는 지원을 해야만 하며, 그 모드의 이름은 “DEFAULT_MODE” 이다

### MH_mdaModeControl

**프로토타입**

```c
M_Int32 MH_mdaModeControl(M_Int32 mdaID, M_Char* modeName,
M_Int32 cmd, M_Int32 pID, void* buf);
```

**설명**

`MH_mdaDevControl` 의 `MH_MDADEVCTRL_GET_MODE_LIST` 컨트롤 커맨드를 이용 하면 현재 제조사에서 지원하는 미디어 장치의 모드의 이름 리스트를 얻어 올 수 있 다. 모드란 미디어 장치가 가지고 있는 속성을 추상화 하여 구조체로 정의해 놓은 것 을 말한다. 모드란 개념의 도입 이유는, Contents Provider(이하 CP)가 미디어 장치를 이용하는 어플리케이션을 구현하고자 할 때에, 미디어 장치의 속성 인자를 개별적으 로 설정할 필요 없이, 제조사나 이통사가 정의해 놓은 모드를 이용하여 한번에 설정 할 수 있도록 함으로서 CP 들이 미디어 장치를 이용한 어플리케이션을 개발 할 때에 편의성을 제공하기 위해서 이다. 단말에서는 “DEFAULT_MODE” 라는 이름을 가지는 최소한 한 개의 모드는 지원을 하여야 한다. “DEFAULT_MODE” 이외의 제조사나 이 통사에서 제공되는 모드는 “DEFAULT_MODE” 내의 속성 인자를 그대로 가져와서 사용하여도 되고, 새로운 속성 정보를 추가하여 사용할 수도 있다. “DEFAULT_MODE” 라는 이름을 갖는 모드의 속성 값들은 디폴트 값으로 설정되어 있으며, 읽어 오기 및 쓰기가 가능하다. 그 이외에 제조사나 이통사에서 지원하는 모 드들의 속성 데이타는 제조사나 이통사에서 읽기 및 쓰기 옵션을 설정할 수 있다. 제 조사나 이통사에서 지원하는 모드들에 설정되어 있는 속성값은 제조사나 이통사에 문 의 하도록 한다. `MH_mdaModeControl()` 함수는 이 모드들에 속성값을 읽어 올수도 있 으며, 모드의 이름이 “DEFAULT_MODE” 인 모드의 속성값의 경우에는 쓰기도 가능 하다. 모드의 이름이 “DEFAULT_MODE” 이외의 다른 이름의 속성데이타의 경우, 제 조사나 이통사에서 쓰기 옵션을 주어졌으면, 그 속성 데이터에 한에서 쓰기가 가능하 다. 모드의 속성 값은 각 미디어 장치의 일반 적인 속성 값의 이름들은 아래의 표와 같이 이미 정의 되어 있고, 제조사나 이통사에서 추가하고 싶은 속성이 있다면, 추가 가 가능하다. 주의할 점은 현재 설정되어 있는 모드 이름의 속성값을 수정하였을 경 우에는, 바로 수정된 값이 적용이 되어지지만, 현재 설정되어 있지 않은 다른 이름의 모드의 속성값을 수정하였을 경우에는, 바로 그 수정값이 적용되는 것이 아니고, 그 모드 이름을 매개변수로 하여 `MH_mdaControl`()의 `MH_MDACTRL_SET_MODE` 컨트 롤 커맨드가 불리워 져야 비로소 수정된 값이 적용이 된다.

**매개 변수**

- `mdaID` - [in] `MH_mdaOpenDevice`()로부터 반환되는 디바이스 인스턴스 식별자
- `modeName` - [in] 모드 이름 : 단말에서 지원되는 모드의 이름 리스트는 MH_mdaDevControl의 `MH_MDADEVCTRL_GET_MODE_LIST` 커맨트 컨트롤에 의해서 얻을 수 있으며, 이 모드의 이름 리스트 중에서 속성 데이터 값의 내용을 읽어오거나 수정하기를 원할 경우의 그 모드의 이름을 의미한다.
- `cmd` - [in] 컨트롤(control) 명령 `MH_MDAMODECTL_GET` / `MH_MDAMODECTL_SET`
- `pID` - [in] 컨트롤 명령을 수행할 속성 아이디
- `buf` - [in/out] 컨트롤 명령에서 사용할 수 buf 컨트롤 명령이 `MH_MDAMODECTL_SET` 일 경우에는 [in] 컨트롤 명령이 `MH_MDAMODECTL_GET` 일 경우에는 [out]

**반환 값**

성공

실패

- `M_E_ERROR` - 지원하지 않는 command이거나, command 수행에 실패하였음

**부작용**

없음

**참고 항목**

1. 모드 이름 규칙 모든 모드는 다른 모드와 구별되게 할 수 있는 이름을 가진다. 모드 이름은 개 발자 임의로 정하는 것이 아니라, 아래의 이름 규칙에 따라서 정해진다. ① 모드는 최소한 한 개 이상은 지원해야 하며, 그 모드의 이름은 “DEFAULT_MODE” 이다 ② 이통사나 제조사에서 제공하는 모드일 경우에는, 아래의 규칙에 따른다. (이통사/제조사이름)_MODE_(인덱스) Ex) SKT 에서 세가지의 모드를 지원한다고 하면, 각 세가지 모드의 이 름은, SKT_MODE_0, SKT_MODE_1, SKT_MODE_2 가 된다. 2. DEFAULT_MODE의 속성 인자 “DEFAULT_MODE” 라는 이름을 가지는 모드는, 단말에서 무조건 제공을 하 여야 하는 모드 이다. 이 모드는 각 미디어 장치가 일반적으로 가지고 있는 속성 인 자들로 구성되어 있다. 3. 미디어 타입별 DEFAULT_MODE 가 가지게 되는 속성 인자 [표 2-17-6] 미디어 타입별 DEFAULT_MODE 가 가지게 되는 속성 인자 미디어 장치 속성 정보 “audio/MIDI” “audio/TONE” “audio/FREQTONE" “Qualcomm_CMX” “Yamaha_MA1” Balance “Yamaha_MA2” “Yamaha_MA3” “Yamaha_MA5” “Yamaha_SMAF” “ Yamaha_SMAF- Phrase” “Yamaha_SMAF-Audio” Vocoder “IS96” “IS96A” “IS733” “IS127” “G.723.1” “AMR-WB” “AMR-NB” general “audio/WAVE” Sample Per Second sound “audio/MP3” Significant bits per sample “audio/AAC” Number of Channels “audio/AAC+” Balance Video “video/MPEG4” Location ( x position, y position ) “video/H.263” Size( width, height ) “video/H.264” Axis video “video/MJPEG” Bright capture ‘image/JPEG” MagPower Resolution ( x , y ) YUV Resolution ( x , y ) FrameRate 4. DEFAULT_MODE 가 가지게 되는 속성 아이디의 상세 설명 [표 2-17-7] DEFAULT_MODE 가 가지게 되는 속성 아이디의 상세 설명 미디 어 속성이름 설명 장치 ring tone Vocoder 오디오 샘플 속도. 디폴트 값은 8000KHz 이 Sample Per Second 다. Significant bits per 오디오 샘플 크기. 디폴트 값은 8비트 이다. sample 채널의 개수 ( 모노 / 스테레오 ), 디폴드 값은 general Number of Channels 모노 이다. sound 사운드 밸런스. 50을 기준으로 50 보다 작은 값이면 좌측 사운드가 더 커지고, 50 보다 큰 Balance 값이면 우측 사운드가 더 커진다. 밸런스값의 영역은 0 에서 100 사이이다. 디폴트 값은 50 이다. Location ( x position, 화면의 X 좌표 와 Y 좌표 (픽셀단위) y position ) 디폴트 값은 X 좌표는 0, Y 좌표는 0 이다 화면의 너비와 높이 (픽셀단위) Size( width, height ) 디폴트 값은 전체 화면의 크기이다. 화면의 회전/반전 값 (화면의 회전/반전 값은 Axis 구조체MH_MdaCameraSetAxis 를 참고한다.) 디폴트 값은 정상 화면이다. video 화면의 밝기.(퍼센트단위). 디폴트 값은 50이 Bright video 다. capture 화면의 배율. ( 퍼센트 단위, 100이면 보통 비 MagPower 율 , 200이면 2배율, 400이면 4배율, 150 이면 1.5 배율) 디폴트 값은 100이다. 해상도의 가로값과 세로값.(픽셀단위) 디폴트 Resolution ( x , y ) 값은 320*240 이다. YUV Resolution ( x , YUV해상도의 가로값과 세로값.(픽셀단위) y ) 디폴트 값은 320*240이다. FrameRate 초당 프레임의 개수. 디폴트 값은 10 이다.

### MH_mdaRecord

**프로토타입**

```c
M_Int32 MH_mdaRecord (M_Int32 mdaID)
```

**설명**

녹음을 시작 한다. 미디어 디바이스는 `MH_mdaRecord`()함수가 호출되면 백그라운드 (background)로 녹음을 시작하여 미디어 디바이스 내부버퍼로 sampling된 데이터를 복사한다. 내부버퍼가 일정량이상 채워지면 버퍼가 full되기 전에 이벤트 (`MH_MDAEV_MEDIA_FULL`)를 플랫폼에 전달하여 플랫폼이 녹음된 데이터를 복사할 수 있도록 한다. 만일 녹음 중에 문제가 발생할 경우 플랫폼에 `MH_MDAEV_MEDIA_ERROR` 이벤트가 전달되어야 한다. 플랫폼에서 녹음 데이타를 복사하는 속도가 미디어 디바이스가 녹음하는 속도보다 늦으면 내부버퍼 full이 발생 한다. 내부버퍼가 full된 경우에 미디어 디바이스는 플랫폼이 데이터를 복사하기 전까 지 녹음되는 데이터는 버리도록 한다. 스트리밍 녹음을 지원하지 않는 장치는 내부버 퍼가 full이 난 경우, stop하도록 한다.

**매개 변수**

- `mdaID` - [in] `MH_mdaOpenDevice`()로부터 반환되는 디바이스 인스턴스 식 별자

**반환 값**

성공

실패

- `M_E_INPROGRESS` - 미디어장치가 이미 사용중인 경우
- `M_E_ERROR` - 기타 이유로 인한 실패
- `M_E_NOTSUP` - 녹음을 지원하지 않는 미디어 장치

**부작용**

없음

**참고 항목**

없음

### MH_mdaCopy

**프로토타입**

```c
M_Int32 MH_mdaCopy(M_Int32 mdaID, void* buf, M_Int32 size)
```

**설명**

미디어장치 내부버퍼에 녹음된 데이터를 복사해 온다. 스트리밍 녹음을 지원하 지 않는 장치일 경우, 녹음중 MH_mdaCopy가 호출되면 에러값을 반환한다.

**매개 변수**

- `mdaID` - [in] `MH_mdaOpenDevice`()로부터 반환되는 디바이스 인스턴스 식별자
- `buf` - [out] 녹음 데이타가 복사될 버퍼
- `size` - [in] 복사할 크기

**반환 값**

성공

실제 복사된 크기
실패

- `M_E_ERROR` - 스트리밍 녹음을 지원하지 않는 장치에 녹음중 호출됨
- `M_E_NOTSUP` - 녹음을 지원하지 않는 미디어 장치

**부작용**

없음

**참고 항목**

없음

### MH_mdaSetMuteState

**프로토타입**

```c
M_Int32 MH_mdaSetMuteState(M_int32 cateID, M_Boolean bmute)
```

**설명**

단말기의 볼륨 카테고리 별로 소리 발생 방지를 설정한다. 단말에서 지원하는 볼륨의 카테고리는 참고 항목의 [표 2-17-8] 을 참조한다.

**매개 변수**

- `cateID` - [in] 볼륨 카테고리 아이디
- `bmute` - [in] 소리발생 방지 설정 `TRUE` 소리 발생 방지 `FALSE` 소리 발생 허용

**반환 값**

성공

- `M_E_SUCCESS` - 성공 실패
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

[표 2-17-8] 단말에서 지원하는 볼륨의 카테고리 카테고리 Default

**설명**

아이디 volume 예 `MH_MDAVOLCA` 음성의 재생/녹음 특성을 갖는다. 단말기의 통화 음 TE_VOICE 량 `MH_MDAVOLCA` 착신 벨 특성을 갖는다. 예를 들어 현재 단말기의 착신 벨 TE_RING 착신 벨이 진동으로 되어 있다면, play 음량 시 소리가 나지 않고 진동이 발생한다. 별도의 멜로디용 speaker가 따로 있다면 이를 통해 소리가 발생한다. 즉, 단말기 에 전화가 왔을 때의 특성 그대로 행동 한다. `MH_MDAVOLCA` 키 톤의 특성을 갖는다. 단말기의 키 톤 음 TE_KEYTONE 량 `MH_MDAVOLCA` SMS message 도착 경고음 특성을 갖는 SMS 메시지 음량 TE_MESSAGE 다. `MH_MDAVOLCA` 알람 경고음 특성을 갖는다. 알람 음량 TE_ALARM `MH_MDAVOLCA` No service, low battery 각종 경고음 특 경고음 음량 TE_ALERT 성을 갖는다. `MH_MDAVOLCA` 멀티미디어 장치의 음량을 말한다. 여기 멀티미디어 음량 TE_MMEDIA 에서 멀티미디어 장치의 음량이란, 플랫 폼에서 지원하는 모든 멀티미디어 장치 의 마스터 볼륨을 지칭하며, 이 마스터 볼륨은 모든 멀티미디어 장치의 영향을 미친다. 각 미디어 장치별로 볼륨을 설 정하고 싶을 시에는 `MH_mdaGetVolume`/`MH_mdaSetVolume` 함수를 사용한다.

### MH_mdaGetMuteState

**프로토타입**

```c
M_Boolean MH_mdaGetMuteState(M_Int32 cateID)
```

**설명**

단말기의 볼륨 카테고리별로 소리 발생 방지 설정 상태를 얻는다. 단말에서 지원하는 볼륨의 카테고리는 `MH_mdaSetMuteState` 함수의 참고 항목의 [표 2-17-8] 을 참조한다.

**매개 변수**

- `cateID` - [in] 볼륨 카테고리 아이디

**반환 값**

- `TRUE` - 소리 발생 방지
- `FALSE` - 소리 발생 허용

**부작용**

없음

**참고 항목**

없음

### MH_mdaGetDefaultVolume

**프로토타입**

```c
M_Int32 MH_mdaGetDefaultVolume (M_Int32 cateID)
```

**설명**

단말이 설정한 볼륨의 카테고리 별로 디폴트 볼륨을 얻는다. 단말에서 지원하는 볼륨의 카테고리는 참고 항목의 [표 2 -17-9] 를 참조한다.

**매개 변수**

- `cateID` - [in] 볼륨 카테고리 아이디

**반환 값**

성공

볼륨 값 (0-100 사이의 값)
실패

- `M_E_ERROR` - 기타 이유로 실패
- `M_E_INVALID` - 존재하지 않는 카테고리 아이디

**부작용**

없음

**참고 항목**

[표 2-17-9] 단말에서 지원하는 볼륨의 카테고리 카테고리 Default

**설명**

아이디 volume 예 `MH_MDAVOLCA` 일반적인 application에서 사용되는 특성 단말기의 TE_GENERAL 을 갖는다. application 음량 `MH_MDAVOLCA` 음성의 재생/녹음 특성을 갖는다. 단말기의 통화 음 TE_VOICE 량 `MH_MDAVOLCA` 착신 벨 특성을 갖는다. 예를 들어 현재 단말기의 착신 벨 TE_RING 착신 벨이 진동으로 되어 있다면, play 음량 시 소리가 나지 않고 진동이 발생한다. 별도의 멜로디용 speaker가 따로 있다면 이를 통해 소리가 발생한다. 즉, 단말기 에 전화가 왔을 때의 특성 그대로 행동 한다. `MH_MDAVOLCA` 키 톤의 특성을 갖는다. 단말기의 키 톤 음 TE_KEYTONE 량 `MH_MDAVOLCA` SMS message 도착 경고음 특성을 갖는 SMS 메시지 음량 TE_MESSAGE 다. `MH_MDAVOLCA` 알람 경고음 특성을 갖는다. 알람 음량 TE_ALARM `MH_MDAVOLCA` No service, low battery 각종 경고음 특 경고음 음량 TE_ALERT 성을 갖는다. `MH_MDAVOLCA` 멀티미디어 장치의 음량을 말한다. 여기 멀티미디어 음량 TE_MMEDIA 에서 멀티미디어 장치의 음량이란, 플랫 폼에서 지원하는 모든 멀티미디어 장치 의 마스터 볼륨을 지칭하며, 이 마스터 볼륨은 모든 멀티미디어 장치의 영향을 미친다. 각 미디어 장치별로 볼륨을 설 정하고 싶을 시에는 `MH_mdaGetVolume`/`MH_mdaSetVolume` 함수를 사용한다. `MH_MDAVOLCA` 게임 시 재생되는 특성을 갖는다. 게임 음량 TE_GAME

### MH_mdaSetDefaultVolume

**프로토타입**

```c
M_Int32 MH_mdaSetDefaultVolume (M_Int32 cateID, M_Int32 value)
```

**설명**

단말이 설정한 볼륨의 카테고리 별 디폴트 볼륨을 설정한다.. 단말에서 지원하는 볼륨의 카테고리는 `MH_mdaGetDefaultVolume` 함수의 참고 항 목 의 [표 2 -17-9] 를 참조한다.

**매개 변수**

- `cateID` - [in] 볼륨 카테고리 아이디
- `value` - [in] 볼륨 값 (0-100사이의 볼륨값)

**반환 값**

성공

실패

- `M_E_ERROR` - 기타 이유로 실패
- `M_E_NOTSUP` - 볼륨 값 설정을 지원하지 않는 미디어 장치

**부작용**

없음

**참고 항목**

없음
