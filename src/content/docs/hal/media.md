---
title: "4.8. MEDIA"
---

미디어를 지원하기 위한 API 들이다. 미디어장치는 데이터를 스트립으로 생산/소 비하는 장치들을 말한다. 이런 장치에는 사운드장치, vocoder 장치, 카메라장치등 이 있을 수 있다.

관련 자료형
```c
typedef enum MH_mdaToneType {
    MH_SND_TONE_0 = 0,    /* DTMF for 0 key */
    MH_SND_TONE_1,        /* DTMF for 1 key */
    MH_SND_TONE_2,        /* DTMF for 2 key */
    MH_SND_TONE_3,        /* DTMF for 3 key */
    MH_SND_TONE_4,        /* DTMF for 4 key */
    MH_SND_TONE_5,        /* DTMF for 5 key */
    MH_SND_TONE_6,        /* DTMF for 6 key */
    MH_SND_TONE_7,        /* DTMF for 7 key */
    MH_SND_TONE_8,        /* DTMF for 8 key */
    MH_SND_TONE_9,        /* DTMF for 9 key */
    MH_SND_TONE_A,        /* DTMF for A key */
    MH_SND_TONE_B,        /* DTMF for B key */
    MH_SND_TONE_C,        /* DTMF for C key */
    MH_SND_TONE_D,        /* DTMF for D key */
    MH_SND_TONE_POUND,    /* DTMF for # key */
    MH_SND_TONE_STAR,     /* DTMF for * key */
    MH_SND_NOTE_A4,       /*  440.0 Hz  -Piano Notes- */
    MH_SND_NOTE_AS4,      /*  466.1 Hz */
    MH_SND_NOTE_B4,       /*  493.8 Hz */
    MH_SND_NOTE_C4,       /*  523.2 Hz */
    MH_SND_NOTE_CS4,      /*  554.3 Hz */
    MH_SND_NOTE_D4,       /*  587.3 Hz */
    MH_SND_NOTE_DS4,      /*  622.2 Hz */
    MH_SND_NOTE_E4,       /*  659.2 Hz */
    MH_SND_NOTE_F4,       /*  698.5 Hz */
    MH_SND_NOTE_FS4,      /*  739.9 Hz */
    MH_SND_NOTE_G4,       /*  784.0 Hz */
    MH_SND_NOTE_GS4,      /*  830.6 Hz */
    MH_SND_NOTE_A5,       /*  880.0 Hz */
    MH_SND_NOTE_AS5,      /*  932.2 Hz */
    MH_SND_NOTE_B5,       /*  987.7 Hz */
    MH_SND_NOTE_C5,       /* 1046.5 Hz */
    MH_SND_NOTE_CS5,      /* 1108.7 Hz */
    MH_SND_NOTE_D5,       /* 1174.6 Hz */
    MH_SND_NOTE_DS5,      /* 1244.3 Hz */
    MH_SND_NOTE_E5,       /* 1318.5 Hz */
    MH_SND_NOTE_F5,       /* 1397.0 Hz */
    MH_SND_NOTE_FS5,      /* 1479.9 Hz */
    MH_SND_NOTE_G5,       /* 1568.0 Hz */
    MH_SND_NOTE_GS5,      /* 1661.2 Hz */
    MH_SND_NOTE_A6,       /* 1760.0 Hz */
    MH_SND_NOTE_AS6,      /* 1864.7 Hz */
    MH_SND_NOTE_B6,       /* 1975.5 Hz */
    MH_SND_NOTE_C6,       /* 2093.1 Hz */
    MH_SND_NOTE_CS6,      /* 2217.4 Hz */
    MH_SND_NOTE_D6,       /* 2349.3 Hz */
    MH_SND_NOTE_DS6,      /* 2489.1 Hz */
    MH_SND_NOTE_E6,       /* 2637.0 Hz */
    MH_SND_NOTE_F6,       /* 2793.7 Hz */
    MH_SND_NOTE_FS6,      /* 2959.9 Hz */
    MH_SND_NOTE_G6,       /* 3135.9 Hz */
    MH_SND_NOTE_GS6,      /* 3322.4 Hz */
    MH_SND_NOTE_A7        /* 3520.0 Hz */
} MH_mdaToneType;

typedef enum MH_MdaDevInfo {
    MH_MDAINFO_STREAM_PLAY       = 0x0001,  /* STREAM 재생을 지원하는 장치 */
    MH_MDAINFO_CALL_BY_REFERENCE = 0x0002,  /* 전달하는 버퍼 내용을 복사하지 않고 그대로 사용함 */
    MH_MDAINFO_PAUSE_RESUME      = 0x0004,  /* pause/resume 을 지원하는 장치 */
    MH_MDAINFO_SEEK              = 0x0008,  /* seek 을 지원하는 장치 */
    MH_MDAINFO_STREAM_RECORD     = 0x0010   /* STREAM 녹음을 지원하는 장치 */
} MH_MdaDevInfo;

/* 사운드 이벤트 */
typedef enum MH_SUB_MEDIA_EVENT {
    MH_MDAEV_MEDIA_EMPTY = 0,  /* 미디어 장치 재생 버퍼가 비었음 */
    MH_MDAEV_TONE_EMPTY,       /* 톤 재생 버퍼가 비었음 */
    MH_MDAEV_MEDIA_FULL,       /* 녹음 버퍼가 full 되었음 */
    MH_MDAEV_MEDIA_ERROR,      /* 미디어 디바이스에 문제가 발생했음 */
    MH_MDAEV_TONE_ERROR        /* 톤 디바이스에 문제가 발생했음 */
} MH_SUB_MEDIA_EVENT;

/* 사운드 이벤트를 전달하는 구조체 */
typedef struct MH_MediaEvent {
    M_Int32 event;  /* MH_SUB_MEDIA_EVENT 타입의 값 */
    M_Int32 mdaID;  /* 이벤트를 발생시킨 미디어 장치 식별자 */
    M_Int32 size;   /* MH_MDAEV_MEDIA_EMPTY, MH_MDAEV_TONE_EMPTY 인 경우:
                       미디어 장치 내부 버퍼에 받아들일 수 있는 데이터 양.
                       MH_MDAEV_MEDIA_FULL 인 경우:
                       미디어 장치 내부 버퍼에 녹음된 데이터 양 */
} MH_MediaEvent;
```

### MH_mdaTonePlay

**설명**

여러 개의 Tone 을 순서에 따라 연주한다. 이 함수는 톤 배열을 운영체제의 톤 재생 버퍼에 싣고 그 실은 양을 리턴한다. 톤 재생버퍼의 데이터가 모두 비워지기 전 적절한 시점에 이벤트(`MH_MDAEV_TONE_EMPTY`)를 플랫폼에 전달해야 한다[적절한 시점이란 플랫폼이 이벤트(`MH_MDAEV_TONE_EMPTY`)를 받고 데이터를 톤 재생버퍼에 복사하는 시간이상의 데이터가 남아있는 시점]. 만일 재생중 문제가 발생한 경우 운영체제는 플랫폼에 `MH_MDAEV_TONE_ERROR` 이벤트를 전달해야 한다. 톤재생기는 mdaID number 0 을 사용하고, 이벤트(`MH_MDAEV_TONE_EMPTY`)를 플랫폼에 전달시 MH_MediaEvent 구조체의 mdaID field 가 0 으로 채워져야한다. pause/resume 을 지 원하는 톤재생기인 경우, `MH_mdaTonePlay` 는 데이터를 사운드장치에 복사후 일시 멈춤 상태가 되고, 재생은 `MH_mdaResume` 이 불린 시점부터 일어나야 한다. pause/resume 을 지원하지 않는 톤재생기일 경우에는 `MH_mdaTonePlay` 는 데이터를 사운드장치에 복사하고, 곧 바로 재생도 시작되어야한다. 스트리밍을 지원하지 않 는 톤재생기일 경우, 재생중 `MH_mdaTonePlay` 가 호출되면 에러값을 반환한다. 톤 재상기는 미디어 디바이스 식별자로 0 을 사용한다.

**프로토타입**

```c
M_Int32 MH_mdaTonePlay (MH_mdaToneType tone[], M_Int32 duration[], M_Int32 number)
```

**매개 변수**

- `tones` - [in] 연주할 톤 구조체 배열에 대한 포인터
- `duration` - [in] 연주할 시간에 대한 배열 포인터(시간 단위는 ms) 
- `number` - [in] 톤구조체의 개수

**반환 값**

성공

- 시스템 톤 재생 버퍼에 실린 톤 개수.

실패

- `M_E_INUSE` – 이미 재생중에 있음
- `M_E_ERROR` - 기타 에러가 발생할 경우

**부작용**

없음

**참고항목**

없음


### MH_mdaFreqTonePlay

**설명**
여러 개의 Tone 을 순서에 따라 연주한다. 이 함수는 톤 배열을 운영체제의 톤 재생 버퍼에 싣고 그 실은 양을 리턴한다. 톤 재생버퍼의 데이터가 모두 비워지기 전 적절한 시점에 이벤트(`MH_MDAEV_TONE_EMPTY`)를 플랫폼에 전달해야 한다[적절한 시점이란 플랫폼이 이벤트(`MH_MDAEV_TONE_EMPTY`)를 받고 데이터를 톤 재생버퍼에 복사하는 시간이상의 데이터가 남아있는 시점]. 만일 재생중 문제가 발생한 경우 운영체제는 플랫폼에 `MH_MDAEV_TONE_ERROR` 이벤트를 전달해야 한다. 프리퀀시톤재 생기는 mdaID number 0 을 사용하고, 이벤트(`MH_MDAEV_TONE_EMPTY`)를 플랫폼에 전달시 `MH_MediaEvent` 구조체의 mdaID field 가 0 로 채워져야한다. pause/resume 을 지원하는 톤재생기인 경우, `MH_mdaTonePlay` 는 데이터를 사운드장치에 복사후 일 시멈춤 상태가 되고, 재생은 `MH_mdaResume` 이 불린 시점부터 일어나야 한다. pause/resume 을 지원하지 않는 톤재생기일 경우에는 `MH_mdaFreqTonePlay` 는 데이터를 사운드장치에 복사하고, 곧 바로 재생도 시작되어야한다. 스트리밍을 지원하 지 않는 톤재생기일 경우, 재생중 `MH_mdaFreqTonePlay` 가 호출되면 에러값을 반환한다. 프리퀀시 톤재생기는 미디어 디바이스 식별자로 0 을 사용한다.


**프로토타입**

```c
M_Int32 MH_mdaFreqTonePlay (M_Int32 hiFreq[], M_Int32 lowFreq[], M_Int32 duration[], M_Int32 number)
```

**매개 변수**

- `hiFreq` -[in] 연주할 고주파 톤 구조체 배열에 대한 포인터
- `lowFreq` - [in] 연주할 저주파 톤 구조체 배열에 대한 포인터
- `duration` - [in] 연주할 시간에 대한 배열 포인터 (시간 단위는 ms)
- `number` - [in] 톤구조체의 개수

**반환 값**

성공

- 시스템 톤 재생 버퍼에 실린 톤 개수.

실패

- `M_E_INUSE` – 이미 재생중에 있음
- `M_E_ERROR` - 기타 에러가 발생할 경우

**부작용**

없음

**참고항목**

없음

### MH_mdaGetDeviceID

**설명**

미디어 장치의 식별자를 구한다. 운영체제에서 지원하는 미디어 장치 이름들은 `MH_sysGetInformation()`으로 구할 수 있다. `MH_sysGetInformation` 의 command 매개 변수 중 “MEDIADEVICES” 로 얻어진 문자열이 이름으로 사용될 수 있다. 톤재생기와 프리퀀시 톤 재생기는 mdaID number 0 을 사용하므로 이 함수에서 부여하는 mdaID number 는 0 보다 큰 숫자를 부여해야 한다.

**프로토타입**

```c
M_Int32 MH_mdaGetDeviceID(M_Char* devName)
```

**매개 변수**

- `devName` - [in] 사운드 장치 이름

**반환 값**

성공

- 미디어 장치 식별자

실패

- `M_E_NOTSUP` – 지원하지 않는 장치 이름

**부작용**

없음

**참고항목**

`MH_sysGetInformation`

### MH_mdaGetDeviceInfo

**설명**

미디어 장치의 특성을 구한다. 장치 식별자 0 은, 프리퀀시 톤재생기를 나타낸다.

1. `MH_MDAINFO_STREAM_PLAY` bit 는 미디어 장치기 스트리밍 재생을 지원하는 것을 말한다. 이것은 미디어 재생중에 `MH_mdaWriteData`(장치 식별자가 0 인경우, `MH_mdaTonePlay`, `MH_mdaFreqTonePlay`)로 새로운 데이터를 사운드 장치에 복사할 수 있는 것을 말하며, 사운드 장치는 기존데이타에 연속적 으로 새로운 데이터를 재생할 수 있어야 한다. 스트리밍을 지원할 경우에는 `MH_MDAINFO_CALL_BY_REFERENCE` bit 가 설정되어서는 안된다.

2. `MH_MDAINFO_CALL_BY_REFERENCE` bit는 `MH_mdaWriteData`(장치 식별자가 0인경우, `MH_mdaTonePlay`, `MH_mdaFreqTonePlay`)로 전달되는 데이터버퍼를 미디어장치가 내부버퍼에 복사하지 않고 그대로 사용함을 의미한다. 이 bit가 설정되지 않으면 전달되는 데이터가 내부버퍼에 복사 되어 사용됨을 의미한다.

3. `MH_MDAINFO_PAUSE_RESUME` bit는 미디어 장치가 pause/resume기능 을 지원함을 의미한다.

4. `MH_MDAINFO_SEEK` bit 는 사운드 장치가 seek 기능을 지원함을 의미한다.

5. `MH_MDAINFO_STREAM_RECORD` bit 는 미디어 장치기 스트리밍 녹음을 지원하는 것을 말한다. 이것은 녹음중에 MH_mdaCopy 로 녹음장치내의 버퍼에서 녹음된 데이터를 플랫폼의 버퍼로 복사해 올 수 있는 것을 말하며, 녹음 장치는 비워진 버퍼에 계속해서 연속적으로 데이터를 녹음할 수 있어야 한다.

**프로토타입**

```c
M_Int32 MH_mdaGetDeviceInfo(M_Int32 mdaID, M_Int32* rtnInfo)
```

**매개 변수**

- `mdaID` - [in] 미디어 장치 식별자
- `rtnInfo` - [out] `MH_MdaDevInfo` 의 bit OR 값

**반환 값**

성공

- 0

실패

- `M_E_ERROR` – 에러

**부작용**

없음

**참고항목**

없음

### MH_mdaWriteData

**설명**

미디어 디바이스 내부버퍼에 연주할 데이터를 복사한다. 미디어 디바이스는 내부 버퍼가 비워지기전 적절한 시점에 이벤트(`MH_MDAEV_MEDIA_EMPTY`)를 플랫폼에 전달해야 한다 [적절한 시점이란 플랫폼이 이벤트(`MH_MDAEV_MEDIA_EMPTY`)를 받고 데이 터를 미디어 디바이스 내부버퍼에 복사하는 시간이상의 데이터가 남아있는 시점]. `MH_mdaStop`()가 수행되지 않고 디바이스 내부버퍼가 비워지게되면 미디어 디바이 스가 적절한 처리(묵음처리등)를 해야 한다. 디바이스 내부버퍼가 수용할 수 있는 양보다 많은 양의 데이터를 복사하려 할 때는 내부버퍼가 수용할 수 있는 양만큼 복사하고 복사한 양을 반환한다. 만일 재생중 문제가 발생하면 `MH_MDAEV_MEDIA_ERROR` 이벤트를 플랫폼에 전달해야 한다. 스트리밍을 지원하지 않 는 미디어장치일 경우, 재생중 `MH_mdaWriteData` 가 호출되면 에러값을 반환한다.

**프로토타입**

```c
M_Int32 MH_mdaWriteData (M_Int32 mdaID, void *buf, M_Int32 size)
```

**매개 변수**

- `mdaId` - [in] 미디어 장치 식별자
- `buf` - [in] 데이터 버퍼
- `size` - [in] 복사할 길이

**반환 값**

성공

- 미디어 내부버퍼로 복사된 크기

실패

- `M_E_INUSE` – 이미 재생중에 있음
- `M_E_ERROR` – 기타 에러가 발생할 경우
- `M_E_NOTSUP` – 재생을 지원하지 않는 미디어 장치

### MH_mdaPlay

**설명**

재생을 시작한다. 미디어 디바이스는 `MH_mdaPlay()`함수가 호출되면 백그라운드 (background)로 재생을 시작한다. 내부버퍼가 일정량이상 비워지면 버퍼가 완전히 비기전에 이벤트(`MH_MDAEV_MEDIA_EMPTY`)를 플랫폼에 전달하여 플랫폼이 계속해서 재생할 데이터를 미디어 디바이스에 복사할 수 있도록 한다. 만일 재생중에 문제가 발생할 경우 플랫폼에 `MH_MDAEV_MEDIA_ERROR` 이벤트가 전달되어야 한다. 미디 어 디바이스에서 재생하는 속도가 재생데이타를 플랫폼이 미디어 디바이스에 복사 하는 속도보다 빠르면 버퍼가 완전히 비게되는 상황이 발생할 수 있으나, 데이터 가 다시 복사되면 정상동작하여야 한다.

**프로토타입**

```c
M_Int32 MH_mdaPlay(M_Int32 mdaID, M_Boolean repeat)
```

**매개 변수**

- `mdaId` - [in] 사운드 장치 식별자(`MH_mdaGetDeviceID` 의 반환 값)
- `repeat` - [in] TRUE : 반복연주, FALSE : 한번만 연주

**반환 값**

성공

- 0

실패

- `M_E_INPROGRESS` - 미디어장치가 이미 사용중인 경우
- `M_E_ERROR` - 기타 이유로 인한 실패
- `M_E_NOTSUP` - 재생을 지원하지 않는 미디어 장치

**부작용**

없음

**참고 항목**

없음

### MH_mdaPause

**설명**

재생중인 미디어를 일시 중지시킨다. 미디어 장치는 일시 중지시 `MH_mdaResume` 가 불리면 재생을 재개할 수 있도록 내부상태(state)를 유지해야 한다. 이 함수 호출 시 미디어장치가 재생상태가 아니면 무시되고, pause/resume 를 지원하지 않는 경 우에는 에러값을 반환한다.

**프로토타입**

```c
M_Int32 MH_mdaPause(M_Int32 mdamdID)
```

**매개 변수**

- `mdaID` - [in] 미디어 장치 식별자

**반환 값**

성공

- 0 

실패

- `M_E_NOTSUP` – pause/resume 을 지원하지 않는 미디어 장치

**부작용**

없음

**참고항목**

없음

### MH_mdaResume

**설명**

일시중지된 미디어재생을 재개한다. 이 함수 호출시 일시중지상태가 아니면 무시 되고, pause/resume 를 지원하지 않는 경우에는 에러값을 반환한다.

**프로토타입**

```c
M_Int32 MH_mdaResume(M_Int32 mdaID)
```

**매개 변수**

- `mdaID` - [in] 미디어 장치 식별자

**반환 값**

성공

- 0

실패

- `M_E_NOTSUP` – pause/resume 을 지원하지 않는 미디어 장치

**부작용**

없음

**참고항목**

없음

### MH_mdaSeek

**설명**

milli second 단위로 재생을 시작할 지점을 설정한다. 이 함수 호출시 pause 상태 가 아니면 무시되고, seek 를 지원하지 않는 미디어 장치인 경우에는 에러값을 반환한다

**프로토타입**

```c
M_Int32 MH_mdaSeek(M_Int32 mdaID, M_Int32 seekTime)
```

**매개 변수**

- `mdaId` - [in] 미디어 장치 식별자
- `seekTime` - [in] seekTime 연주할 지점 시간(ms), 0 보다 작으면 시작점으로 지점이 설정 되고, 데이터의 전체 연주시간보다 큰값이면 끝점으로 지점이 설정된다.

**반환 값**

성공

- 0

실패

- `M_E_NOTSUP` – seek 을 지원하지 않는 미디어 장치

**부작용**

없음

**참고항목**

없음

### MH_mdaRecordFreeze

**설명**

녹음/녹화중 `MH_mdaStop()`이 불리기 전에 불릴 수 있다. 이 함수가 불린이후에는 `MH_mdaStop()`이나 `MH_mdaRecordFreeze()`만이 다시 불일 수 있고, 그 외의 함수는 불릴 수 없다.

**프로토타입**

```c
M_Int32 MH_mdaRecordFreeze(M_Int32 mdaID)
```

**매개 변수**

- `mdaId` - [in] 미디어 장치 식별자

**반환 값**

성공

- 이 함수가 불릴시점까지 미디어 디바이스 내부버퍼에 녹음/녹화된 데이 타 크기(0 보다 같거나 큼)

실패

- `M_E_ERROR` – 녹음/녹화중 이외에 이 함수가 불릴 경우

**부작용**

없음

**참고항목**

없음

### MH_mdaStop

**설명**

재생/녹음중인 미디어를 중지시킨다. 미디어 장치가 어떤 상태에 있던지 이 함수 가 불리면 재생중인 미디어가 중지된다. 중지되어 있는 미디어에 이 함수가 불리 면 아무 역할도 하지 않는다. 이 함수는 항상 성공하여야 한다.

**프로토타입**

```c
M_Int32 MH_mdaStop (M_Int32 mdaID)
```

**매개 변수**

- `mdaId` - [in] mdaID 미디어 장치 식별자

**반환 값**

성공

**부작용**

없음

**참고항목**

없음

### MH_mdaGetVolume

**설명**

볼륨 소스로부터 볼륨 값을 읽어 온다. 미디어 장치마다 볼륨설정이 가능한 것은 미디어 장치마다 볼륨값을 읽어오고, 그렇지 않은 것은 미디어장치 식별자가 서로 달라도 같은 볼륨소스를 가리킬 수 있다. 볼륨의 최소값은 0, 최대값은 100 이다. 반환되는 볼륨값은 0 – 100 사이의 값으로 환산하여 반환되어야 한다. 0-100 사이 값을 어느정도의 볼륨세기와 일치시키는가는 아래의 예처럼 하드웨어가 지원하는 볼륨단계를 백분율로 일치시킨것에 따른다. 하드웨어가 몇단계의 볼륨세기를 지원 하는가는 `MH_sysGetInformation`()에서 반환한다.

> 예)
> 볼륨세기가 강, 약 두개인 하드웨어 => 1-50: 약볼륨 51-100: 강볼륨
> 볼륨세기가 강,중,약 세개인 하드웨어 => 1-33: 약볼륨, 34 -66: 중볼륨, 67-100: 강볼륨

**프로토타입**

```c
M_Int32 MH_mdaGetVolume (M_Int32 mdaID)
```

**매개 변수**

- `mdaId` - [in] 볼륨값을 구할 디바이스 식별자

**반환 값**

성공

- 볼륨값

실패

- `M_E_NOTSUP` – 볼륨값이 존재하지 않는 미디어 장치

**부작용**

없음

**참고항목**

없음

### MH_mdaSetVolume 

**설명**

볼륨 소스에 값을 설정한다. 만약 볼륨 값이 최소볼륨 보다 작으면 최소볼륨으로 최대보다 크면 최대 볼륨으로 설정된다. 볼륨값의 최소는 0, 최대는 100 이다. 미디어 장치마다 볼륨설정이 가능한 것은 미디어 장치마다 설정되고, 그렇지 않은 것은 미디어장치 식별자가 서로 달라도 같은 볼륨소스를 가리킬 수 있다.

**프로토타입**

```c
void MH_mdaSetVolume (M_Int32 mdaID, M_Int32 value)
```

**매개 변수**

- `mdaID` - [in] 볼륨값을 설정할 디바이스 식별자
- `value` - [in] 볼륨 값 (0-100 사이의 볼륨값)

**반환 값**

성공

- 0

실패

- `M_E_NOTSUP` – 볼륨값 설정을 지원하지 않는 미디어 장치

**부작용**

없음

**참고항목**

없음

### MH_mdaControl

**설명**

미디어장치에 컨트롤(control) 명령을 수행시킨다. 새로운 미디어장치가 플랫폼에 장착될 경우, HAL 에서 정의되지 않은 기능들을 설정하거나 사용해야 할 경우가 있을 수 있다. 이 함수는 벤더가 새로운 미디어장치를 플랫폼에 장착할 경우, 벤더가 새로운 미디어장치를 프로그램이 사용할 수 있도록 cmd 을 정의하여 확장한 다.

**프로토타입**

```c
M_Int32 MH_mdaControl(M_Int32 mdaID, M_Int32 cmd, void* buf1, void* buf2);
```

**매개 변수**

- `mdaId` - [in] 디바이스 식별자
- `cmd` - [in] 컨트롤(control) 명령
- `buf1` - [in] 컨트롤 명령에서 사용할 수 buf1
- `buf2` - [in] 컨트롤 명령에서 사용할 수 buf2

**반환 값**

성공

- 0

실패

- `M_E_ERROR` – 지원하지 않는 command 이거나, command 수행에 실패하였음

**부작용**

없음

**참고항목**

없음

### MH_mdaRecord

**설명**

녹음을 시작 한다. 미디어 디바이스는 `MH_mdaRecord()`함수가 호툴되면 백그라운드 (background)로 녹음을 시작하여 미디어 디바이스 내부버퍼로 sampling 된 데이터 를 복사한다. 내부버퍼가 일정량이상 채워지면 버퍼가 full 되기전에 이벤트 (`MH_MDAEV_MEDIA_FULL`)를 플랫폼에 전달하여 플랫폼이 녹음된 데이터를 복사할 수 있도록 한다. 만일 녹음중에 문제가 발생할 경우 플랫폼에 `MH_MDAEV_MEDIA_ERROR` 이벤트가 전달되어야 한다. 플랫폼에서 녹음데이타를 복사하는 속도가 미디어 디 바이스가 녹음하는 속도보다 늦으면 내부버퍼 full 이 발생한다. 내부버퍼가 full 된 경우에 미디어 디바이스는 플랫폼이 데이터를 복사하기 전까지 녹음되는 데이 터는 버리도록 한다. 스트리밍 녹음을 지원하지 않는 장치는 내부버퍼가 full 이 난 경우, stop 하도록 한다.

**프로토타입**

```c
M_Int32 MH_mdaRecord (M_Int32 mdaID)
```

**매개 변수**

- `mdaId` - [in] 사운드 장치 식별자(`MH_mdaGetDeviceID` 의 반환 값)

**반환 값**

성공

- 0

실패

- `M_E_INPROGRESS` – 미디어장치가 이미 사용중인 경우
- `M_E_ERROR` - 기타 이유로 인한 실패
- `M_E_NOTSUP` – 녹음을 지원하지 않는 미디어 장치

**부작용**

없음

**참고 항목**

없음

### MH_mdaCopy

**설명**

미디어장치 내부버퍼에 녹음된 데이터를 복사해 온다. 스트리밍 녹음을 지원하지 않는 장치일 경우, 녹음중 `MH_mdaCopy` 가 호출되면 에러값을 반환한다.

**프로토타입**

```c
M_Int32 MH_mdaCopy(M_Int32 mdaID, void* buf, M_Int32 size)
```

**매개 변수**

- `mdaId` - [in] mdaID 미디어 장치 식별자(`MH_mdaGetDeviceID` 의 반환 값)
- `buf` - [in] 녹음 데이타가 복사될 버퍼
- `size` - [in] 복사할 크기

**반환 값**

성공

- 실제 복사된 크기

실패

- `M_E_ERROR` – 스트리밍 녹음을 지원하지 않는 장치에 녹음중 호출됨
- `M_E_NOTSUP` – 녹음을 지원하지 않는 미디어 장치

**부작용**

없음

**참고 항목**

없음

### MH_mdaSetMuteState

**설명**

단말기의 음원별 소리 발생 방지를 설정한다.

**프로토타입**

```c
M_Int32 MH_mdaSetMuteState(M_int32 source, M_Boolean bmute)
```

**매개 변수**

- `source` - [in] 볼륨소스 `MC_MDA_VOLTYPE_TONE`, `MC_MDA_VOLTYPE_SOUND`, `MC_MDA_VOLTYPE_RECORDER` 중의 하나가 될 수 있다 
- `bmute` – [in] 소리발생 방지 설정. TRUE : 소리 발생 방지 FALSE : 소리 발생 허용

**반환 값**

성공

- `M_E_SUCCESS` – 성공

실패

- `M_E_ERROR` – 실패
- `M_E_INVALIDSOURCE` – 잘못된 볼륨 소스

**부작용**

없음

**참고 항목**

없음

### MH_mdaGetMuteState 

**설명**

단말기의 음원별 소리 발생 방지 설정 상태를 얻는다.

**프로토타입**

```c
M_Boolean MH_mdaGetMuteState(M_int32 source)
```

**매개 변수**

- `source` - [in] 볼륨소스. `MC_MDA_VOLTYPE_TONE`, `MC_MDA_VOLTYPE_SOUND`, `MC_MDA_VOLTYPE_RECORDER` 중의 하나가 될 수 있다

**반환 값**

- TRUE : 소리 발생 방지
- FALSE : 소리 발생 허용

**부작용**

없음

**참고 항목**

```c
없음
```
