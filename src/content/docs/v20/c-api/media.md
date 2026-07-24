---
title: "2.11. 매체 처리기"
---

사운드나 동영상 등의 모든 Media에 대해서 처리를 해주는 매체 처리기와 관련된 함수와 톤 재생 및 음성녹음 및 볼륨 조절에 관련한 패키지 이다 사운드, 톤, 동영상 등의 모든 데이타는 클립(CLIP)으로 추상화되어 매체처리기에서 수행한다. 매체재생기에서 지원하는 타입은 `MC_knlGetSystemProperty`()의 "MEDIADEVICES"에 의해 구해진 타입들이다. 매체처리, 톤 재생, 녹음 등의 상태 변화는 등록하는 콜백 함수로 전달된다. 볼륨 조 절은 톤, 사운드, 녹음에 대해 각각 가능하다.

### MC_MDA_STATUS_ERROR

**프로토타입**

```c
#define MC_MDA_STATUS_ERROR (-1)
```

**설명**

오류로 인한 정지 상태. 상수 값은 -1.

### MC_MDA_STATUS_END_OF_DATA

**프로토타입**

```c
#define MC_MDA_STATUS_END_OF_DATA 1
```

**설명**

매체(혹은 톤)처리시 - 처리기가 매체(혹은 톤) 데이터의 마지막에 도달한 상태. 상수 값은 1.

### MC_MDA_STATUS_START

**프로토타입**

```c
#define MC_MDA_STATUS_STARTED 2
```

**설명**

매체(혹은 톤)처리시 - 매체(혹은 톤) 처리를 시작한 상태. 상수 값은 2.

### MC_MDA_STATUS_STOP

**프로토타입**

```c
#define MC_MDA_STATUS_STOPP 3
```

**설명**

매체(혹은 톤)처리시 - 매체(혹은 톤) 처리를 종료한 상태 녹음 시 – 녹음을 중단한 상태. 상수 값은 3

### MC_MDA_STATUS_PAUSE

**프로토타입**

```c
#define MC_MDA_STATUS_PAUSED 4
```

**설명**

매체(혹은 톤)처리시 - 매체(혹은 톤) 처리를 잠시 멈춘 상태 녹음 시 – 녹음을 잠시 멈춘 상태. 상수 값은 4

### MC_MDA_STATUS_RESUME

**프로토타입**

```c
#define MC_MDA_STATUS_RESUMED 5
```

**설명**

매체(혹은 톤)처리시 - 잠시 멈춘 매체(혹은 톤) 처리를 재개한 상태 녹음 시 – 잠시 멈춘 녹음을 재개한 상태. 상수 값은 5

### MC_MDA_STATUS_RECORD

**프로토타입**

```c
#define MC_MDA_STATUS_RECORDED 6
```

**설명**

녹음 시 – 녹음을 시작한 상태. 상수 값은 6

### MC_MDA_STATUS_FULL_OF_DATA

**프로토타입**

```c
#define MC_MDA_STATUS_FULL_OF_DATA 7
```

**설명**

녹음 시 – 클립내부버퍼가 완전히 채워진 상태. 상수 값은 7.

### MC_MDA_STATUS_OEM_ERROR

**프로토타입**

```c
#define MC_MDA_STATUS_OEM_ERROR 8
```

**설명**

미디어를 재생 혹은 녹음 중, 플랫폼이 백그라운드로 보내지면서, 재생 혹은 녹음 중 이던 미디어가 강제 종료될 때 발생한다. 상수값은 8. (MEDIACB)

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

특정 타입의 CLIP을 생성한다. 지원되는 타입은 `MC_knlSetSystemProperty`()의 "MEDIADEVICES"에 의해 구해진 타입들이다. 타입은 MIME에서 지원하는 타입일 경 우 "audio/xxx", "video/xxx"와 같이 MIME타입을 따른다. Clip 의 버퍼 크기는 입력하고자 하는 데이터의 전체 크기만큼 생성해야 한다. 콜백함수가 설정되지 않으면 매채재생기의 상태변화가 전달되지 않는다.

**매개 변수**

- `mType` - [in] 미디어타입
- `bufSzie` - [in] 버퍼 크기(CLIP내에 생성될 버퍼크기)
- `cb` - [in] 클립을 매체처리기에서 처리하는중 상태변화를 알려 줄 콜백함수

**반환 값**

성공

MC_MdaClip객체 포인터
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

- `M_E_INUSE` - 클립을 재생중이거나 녹음중에 해제할려고 시도함
- `M_E_INVALID` - clip 이 `NULL` 이면 리턴

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipAllocPlayer

**프로토타입**

```c
M_Int32 MC_mdaClipAllocPlayer(MC_MdaClip* clip, M_Char* param)
```

**설명**

클립내의 미디어 데이타를 처리하기 위한 플레이어를 할당 받는다. 이 함수는 클립 의 미디어 데이타를 이용하여 재생하는 등의 실질적인 처리를 하기 이전에 반드시 불리워져야만 하는 함수이다. 만약 이 함수를 호출 하지 않고, 혹은 이 함수가 실패 한 후에, `MC_mdaPlay`(재생)등의 함수가 불리워지면 에러값을 반환 받게 된다. 만약 미디어 데이터를 어플리케이션단에서 내려보내 주는 것이 아니라 미디어 장치 가 직접 액세스 하는 경우라면, param 변수에 필요한 매개 변수를 전달 하여야 한다. 예를 들어 url 형식의 인자를 받는 스트리밍 재생방식을 지원하는 디바이스 장치가 존재한다면, url 주소 및 여러 가지 필요한 매개 변수가 있을 수 있는데, 그런 매개 변수를 param 매개변수를 통하여 전달할수 있다. 자세한 사항은 참고 항목을 참조한 다.

**매개 변수**

- `clip` - [in] 클립
- `param` - [in] 미디어 장치를 열 때에, 필요한 매개 변수 만약 매개변수가 필요하지 않은 경우에는 `NULL` 값을 입력합니다. 디바이스가 요구 하는 매개 변수에 따라서 매개 변수로 넘어오는 String의 맨 처음 키워드 부분이 달라 질 수 있다. (아래의 표 참조)

**반환 값**

성공

실패

- `M_E_ERROR` - 플레이어 할당 실패
- `M_E_INVALID` - CLIP이 NULL일때
- `M_E_NOTSUP` - 지원하지 않는 미디어 장치일 경우
- `M_E_INPROGRESS` - 최대 인스턴스 초과한 경우

**부작용**

없음

**참고 항목**

매개 변수 param 에 대한 설명 디바이스 설명 키워드 “-streamURL” 을 URL String 앞에 추가하여 전달 URL 형식의 스트 한다. 리밍 미디어 일 때 예1) –streamURL http://www.media.com/m.mp3 예2) –streamURL mms://www.media.com/m.mp3 파일을 직접 액세 키워드 “-file” 을 파일명 앞에 추가하여 전달한다. 스 하여 플레이 시 예1) –file media/sample.mp3 킬수 있는 장치 예2) –file sample.mov

### MC_mdaClipFreePlayer

**프로토타입**

```c
M_Int32 MC_mdaClipAllocPlayer(MC_MdaClip* clip)
```

**설명**

`MC_mdaClipAllocPlayer()` 메소드를 이용해서 할당 받았던 플레이어를 해제 시킨다. 이 함수가 불리우지 않고, `MC_mdaClipFree()` 함수가 불리울 때에, 자동으로 이 클립 에 할당된 플레이어는 해제 되어야 한다.

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

실패

- `M_E_INVALID` - CLIP이 NULL일 때

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

### MC_mdaClipGetInfo

**프로토타입**

```c
M_Int32 MC_mdaClipGetInfo(MC_MdaClip* clip, M_Int32 *rtnInfo)
```

**설명**

단말이 지원하는 매체 처리기에서 클립의 미디어 타입에 따라 지원 가능한 미디어 특성을 얻어온다. 반환되는 미디어 특성에 대한 정보는 아래와 같다. 매체 특성 정보 값 설 명 `MC_MDAINFO_STREAM_PLAY` 0x0001 STREAM 재생을 지원 `MC_MDAINFO_CALL_BY_REFERENCE` 0x0002 전달하는 버퍼내용을 복사하지 않고 그대로 사용 `MC_MDAINFO_PAUSE_RESUME` 0x0004 PAUSE/RESUME을 지원 `MC_MDAINFO_SEEK` 0x0008 SEEK를 지원 `MC_MDAINFO_STREAM_RECORD` 0x0010 STREAM 녹음을 지원 `MC_MDAINFO_VALANCE` 0x0020 좌우 사운드 밸런스 제어를 지원 `MC_MDAINFO_MULTIASYNC` 0x0040 멀티 채널 비동기 재생을 지원 `MC_MDAINFO_MULTISYNC` 0x0080 멀티 채널 동기 재생을 지원

**매개 변수**

- `clip` - [in] 클립
- `rtnInfo` - [out] MC_mdaGetInfo의 bit OR 값

**반환 값**

성공

실패

- `M_E_ERROR` - 미디어 특성을 얻어오는데 실패
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipDevControl

**프로토타입**

```c
M_Int32 MC_mdaClipDevControl(MC_MdaClip* clip, M_Int32t cmd, void* buf1, void* buf2)
```

**설명**

클립의 장치 컨트롤(control) 명령을 수행시킨다. 미디어의 일반적인 기능(재생, 정지, 일시정지) 이외에 제조사에서 지원해주는 장치적인 기능 명령을 수행 시킬 때 사용 되어 진다. 예를 들면 제조사에서 카메라의 전원을 키는 명령을 지원한다면, 이 함수 를 이용하여 그 명령을 수행 할 수 있다. 제조사에서 지원하는 컨트롤 명령이 미디 어 장치 별로 수행이 되어야 하는 경우에는 이 함수를 사용하여 명령어가 수행되게 하고, 미디어 컨텐츠 별로 수행이 되어야 하는 경우에는 `MC_mdaClipControl()` 함수 를 사용한다. 전자에 해당하는 명령어에는 카메라의 전원을 켜거나 끄는 명령어가 있을 수 있고, 후자에 해당하는 명령어에는 현재 재생되고 있는 미디어 컨텐츠의 현 재 재생시간을 얻어오는 명령어가 있을 수 있다.

**매개 변수**

- `clip` - [in] 클립
- `cmd` - [in] 컨트롤(control) 명령
- `buf1` - [in] 컨트롤 명령에서 사용할 수 buf1
- `buf2` - [in] 컨트롤 명령에서 사용할 수 buf2

**반환 값**

성공

실패

`M_E_ERROR`
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

1. 클립의 타입별로 지원 가능한 미디어 장치 컨트롤 커맨드 mime type 지원 가능한 미디어 장치 컨트롤 커맨드 “Qualcomm_CMX” `MC_MDADEVCTRL_GET_INSTANCE_COUNT`, // 최대 “Yamaha_MA1” 지원 인스턴스의 개수 “Yamaha_MA2” “Yamaha_MA3” “Yamaha_SMAF” “Yamaha_SMAF- Phrase” “Yamaha_SMAF-Audio” “audio/ONEPOLY” “audio/GVMONEPOLY” “audio/MIDI” “audio/WAVE” “audio/MP3” “audio/TONE” “audio/FREQTONE" “IS96” “IS96A” “IS733” “IS127” “G.723.1” “audio/AAC” “audio/AAC+” “video/MPEG4” “VOD_URL” “video/H.263” “video/H.264” “video/MJPEG” `MC_MDADEVCTRL_GET_INSTANCE_COUNT`, // 최대 ‘image/JPEG” 지원 인스턴스의 개수 `MC_MDADEVCTRL_DEVICE_ON`, // 카메라의 전원을 켠다. `MC_MDADEVCTRL_DEVICE_OFF`, // 카메라의 전원을 끈다. `MC_MDADEVCTRL_DEVICE_GET_STATUS`, // 카메라 의 전원 상태를 얻어온다. `MC_MDADEVCTRL_DEVICE_DETECT`, // 카메라의 장 착 여부를 탐지한다. `MC_MDADEVCTRL_DEVICE_MODEL`, // 카메라의 모 델명을 얻는다. 2. 미디어 장치 컨트롤 커맨드와 매개 변수에 대한 설명 cmd `MC_MDADEVCTRL_GET_INSTANCE_COUNT` buf1 없음 [out] buf2 *(`M_Int32`*) buf2 : 지원하는 인스턴스의 개수 설명 이 장치에서 지원하는 인스턴스의 개수를 구한다. 비고 최소한 한 개는 지원을 해야 한다. cmd `MC_MDADEVCTRL_DEVICE_ON` buf1 없음 [out] buf2 성공 : *(`M_Int32`*) buf2 = 0 실패 : *(`M_Int32`*) buf2 = `M_E_ERROR` : 기타 에러 설명 카메라의 전원을 켠다 비고 cmd `MC_MDADEVCTRL_DEVICE_OFF` buf1 없음 buf2 없음 설명 카메라의 전원을 끈다 비고 이 명령은 반드시 성공을 해야 한다 cmd `MC_MDADEVCTRL_DEVICE_DETECT` buf1 없음 [out] buf2 성공 : *(`M_Int32`*) buf2 = 0 실패 : *(`M_Int32`*) buf2 = `M_E_ERROR` 설명 내/외장 카메라를 디텍트(DETECT)한다. 비고 cmd `MC_MDADEVCTRL_DEVICE_MODEL` [in] buf1 *(`M_Int32`*) buf1 : 카메라 모델명의 길이 [out] 성공 : (`M_Char`*) buf2 = 카메라 모델명 buf2 실패 : *(`M_Int32`) buf2 = `M_E_LONGNAME` 모델명의 길이가 길 경우 *(`M_Int32`) buf2 = `M_E_ERROR` 모델명을 알아올 수 없음 설명 카메라의 모델명을 얻는다 비고 비고 최소 한 개는 지원을 해야만 한다.

### MC_mdaClipControl

**프로토타입**

```c
M_Int32 MC_mdaClipControl(MC_MdaClip* clip, int cmd, void* buf1, void* buf2)
```

**설명**

클립의 컨트롤(control) 명령을 수행시킨다. 미디어의 일반적인 기능(재생, 정지, 일시 정지) 이외에 제조사에서 지원해주는 특별한 기능 명령을 수행 시킬 때 사용되어 진 다. 예를 들면 제조사에서 현재 재생 시간을 얻어올 수 있는 컨트롤 명령을 지원한 다면, 그 명령을 이 함수를 이용해서 내릴 수 있다.

**매개 변수**

- `clip` - [in] 클립
- `cmd` - [in] 컨트롤(control) 명령
- `buf1` - [in] 컨트롤 명령에서 사용할 수 buf1
- `buf2` - [in] 컨트롤 명령에서 사용할 수 buf2

**반환 값**

성공

실패

`M_E_ERROR`
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

1. 클립의 타입별로 지원 가능한 미디어 컨트롤 커맨드 mime type 지원 가능한 미디어 컨트롤 커맨드 “Qualcomm_CMX” `MC_MDACTRL_GET_MEDIA_TIME`, // 미디어의 현재 “Yamaha_MA1” 재생 시간 “Yamaha_MA2” `MC_MDACTRL_SET_SYNC`, // 미디어간 동기 설정 “Yamaha_MA3” `MC_MDACTRL_GET_SYNC`, // 동기되는 미디어들을 “Yamaha_SMAF” 얻어옴 “Yamaha_SMAF- `MC_MDACTRL_SET_MODE` // 모드를 이름을 받아서 Phrase” 설정함. “Yamaha_SMAF-Audio” “audio/ONEPOLY” “audio/GVMONEPOLY” “audio/MIDI” “audio/WAVE” “audio/MP3” “audio/TONE” “audio/FREQTONE" “IS96” “IS96A” “IS733” “IS127” “G.723.1” “audio/AAC” “audio/AAC+” “video/MPEG4” `MC_MDACTRL_GET_MEDIA_TIME`, // 미디어의 현재 “VOD_URL” 재생 시간 “video/H.263” `MC_MDACTRL_SET_SYNC`, // 클립간 동기 설정 “video/H.264” `MC_MDACTRL_GET_SYNC`, // 동기되는 미디어들을 “video/mjpeg” 얻어옴 ‘image/jpeg” `MC_MDACTRL_CAPTURE_IMAGE`, // 정지 영상을 캡 쳐한다. `MC_MDACTRL_SET_MODE` // 모드를 이름을 받아서 설정함. `MC_MDACTRL_PREVIEW_START`, // 카메라 프리뷰를 시작한다. `MC_MDACTRL_PREVIEW_STOP`, // 카메라 프리뷰를 정지한다. 2. 미디어 컨트롤 커맨드와 매개 변수에 대한 설명 cmd `MC_MDACTRL_GET_MEDIA_TIME` buf1 없음 [out] 성공 : *(M_int32*) buf2 = 현재 재생 시간(단위 millisecond) buf2 실패 : *(`M_Int32`*) buf2 = `M_E_ERROR` 기타 에러 *(`M_Int32`*) buf2 = `M_E_NOTSUP` 지원안함 전체 재생 시간과 관계해서 현재 재생 시간(단위 millisecond)을 구한

**설명**

다. 비고 cmd `MC_MDACTRL_SET_SYNC` [in] *(`M_Int32`*) buf1[0] = 미디어 장치 인스턴스 식별자의 배열의 크기 *(`M_Int32`*) buf1[1] = 동기화 할 첫번째 슬레이브 미디어 인스턴스 식 buf1 별자 *(`M_Int32`*) buf1[2] = 동기화 할 두번째 슬레이브 미디어 인스턴스 식 별자 …… 배열의 크기만큼 반복 [out] 성공 : *(M_int32*) buf2 = 0 buf2 실패 : *(`M_Int32`*) buf2 = `M_E_ERROR` 기타 에러 *(`M_Int32`*) buf2 = `M_E_NOTSUP` 지원안함 멀티 채널에서 재생되는 미디어들 간의 채널 동기화를 설정한다. 동기

**설명**

화 해제는 *(`M_Int32`*) buf1[0] 에 0 을 넘겨 해제한다. 비고 cmd `MC_MDACTRL_GET_SYNC` [in] buf1 *(`M_Int32`*) buf1 = 최대 멀티 채널 배열의 크기 [out] 성공 : *((`M_Int32`*)buf2+0) = 동기화된 첫번째슬레이브 미디어인스턴스 식별자 *((`M_Int32`*)buf2+1) = 동기화된 두번째슬레이브 미디어인스턴 buf2 스식별자 ……배열의 크기만큼 반복 실패 : *(`M_Int32`*)buf2 = `M_E_NOTSUP` : 동기화를 지원하지 않음 *(`M_Int32`*)buf2 = `M_E_ERROR` : 기타 에러 설명 멀티 채널에서 재생되는 미디어들 간의 채널 동기화 정보를 얻어온다. 비고 cmd `MC_MDACTRL_SET_STOP_TIME` (단위 second) [in] buf1 *(`M_Int32`*) buf1 = 재생을 멈출 시점(SECOND 단위) [out] 성공 : *(`M_Int32`*) buf2 = 0 buf2 실패 : *(`M_Int32`*) buf2 = `M_E_NOTSUP` : 지원 안함 *(`M_Int32`*) buf2 = `M_E_ERROR` : 기타 에러 설명 미디어의 전체 재생 시간과 관련하여, 재생을 멈출 시점을 설정한다. 비고 cmd `MC_MDACTRL_SET_MODE` [in] buf1 *(`M_Char`*) buf1 : 모드 이름 [out] 성공 : *(`M_Int32`*) buf2 = 0 buf2 실패 : *(`M_Int32`*) buf2 = `M_E_ERROR` 기타 에러 *(`M_Int32`*) buf2 = `M_E_NOTSUP` 지원되지 않는 모드 이름 *(`M_Int32`*) buf2 = `M_E_INVALID` 잘못된 모드 이름 설명 buf1 로 넘어오는 모드 이름으로 모드를 설정한다. 비고 cmd `MC_MDACTRL_CAPTURE_IMAGE` [in] buf1 (`M_Char`*) buf1 = 캡쳐한 스크린 샷을 저장할 버퍼 [in] buf2 *(`M_Int32`*) buf2 = 캡쳐한 스크린 샷을 저장할 버퍼의 크기 설명 플레이 되고 있는 동영상의 스크린 샷을 캡쳐 한다. return value 성공 : 캡쳐된 스크린 샷의 크기 비고 실패 : `M_E_NOTSUP` : 지원 안함 `M_E_ERROR` : 기타 에러 cmd `MC_MDACTRL_PREVIEW_START` buf1 없음 [out] buf2 성공 : *(`M_Int32`*) buf2 = 0 실패 : *(`M_Int32`*) buf2 = `M_E_ERROR` 기타 에러 현재 설정된 화면 모드와 화면 사이즈에 따라 프리뷰 재생을 시작한다.

**설명**

이미 프리뷰가 재생 중이라면 아무런 일도 하지 않는다. 비고 cmd `MC_MDACTRL_PREVIEW_STOP` buf1 없음 buf2 없음 프리뷰 재생을 하고 있는 상태에서 프리뷰 재생을 멈춘다. 만약 프리뷰

**설명**

가 재생 중이 아니면 아무런 일도 하지 않는다. 비고 이 함수는 무조건 성공해야 한다.

### MC_mdaClipGetModeList

**프로토타입**

```c
M_Int32 MC_mdaClipGetModeList(MC_MdaClip* clip, M_Char* modeList,
M_Int32 size)
```

**설명**

단말에서 지원하는 모드의 이름 리스트를 구한다. 모드란 클립의 속성 데이터 값을 모아논 구조체로, 제조사나 이통사에서는 1개 이상 지원을 하도록 되어 있다. 필수적 으로 제공되는 모드의 이름은 “DEFAULT_MODE” 로 정해져 있으며, 이 모드가 가지 는 속성 값들은 `MC_mdaClipModeControl()` 함수의 컨트롤 커맨드를 이용하여 내용을 얻어올 수도 있고, 수정도 할 수 있다. 제조사나 이동사에서 모드 아이디 이름이 “DEFAULT_MODE” 이외의 다른 이름을 가지는 모드를 지원 한다면, 모드 내부의 속 성 값들에 대한 정보를CP 에게 제공 하여야 한다. 지원되는 모드가 여러가지일 경우, 모드 이름과 이름 사이의 구분자는 ‘,’ 이 된다. 예 : “DEFAULT_MODE,SKT_MODE,LG_MODE”

**매개 변수**

- `clip` - [in] 클립
- `modeList` - [out] 제조사에서 지원하는 모드의 이름 리스트, 모드 이름들은 ‘,’ 로 구분이 되어진다.
- `size` - [in] 제조사에서 지원하는 모드의 이름 리스트를 받아올 버퍼의 사이즈

**반환 값**

성공

실패

`M_E_ERROR`
- `M_E_INVALID` - CLIP이 NULL일 때
- `M_E_SORTBUF` - 버퍼의 크기가 작음

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipModeControl

**프로토타입**

```c
M_Int32 MC_mdaClipModeControl(MC_MdaClip* clip, M_Char* modeName,
M_Int32 cmd, M_Int32 pID, void* buf)
```

**설명**

클립의 특정 모드를 구성하는 속성 정보에 대한 컨트롤 커맨드를 적용한다. 클립의 타입에 따라서 지원될 수 있는 모드 속성 정보의 종류는 아래와 같다. 만약 클립에 서 지원하지 않은 모드 속성 정보에 대한 커맨드 컨트롤을 시도할 경우에 해당 에러 값인 (`M_E_ERROR`) 를 반환받는다. 현재 설정되어 있는 모드의 속성 정보를 수정할 경우에는, 수정된 내용이 바로 적용이 되지만, 그렇지 않은 모드의 속성 정보를 수정 할 경우에는, 그 모드의 이름을 매개변수로 하여 `MC_mdaClipControl()` 함수의 `MC_MDACTRL_SET_MODE` 컨트롤 커맨드가 불리워져야지만 수정된 내용이 적용이 된다.

**매개 변수**

- `clip` - [in] 클립
- `modeName` - [in] 모드 이름. 단말에서 지원되는 모드의 이름 리스트는 `MC_mdaClipGetModeList` 함수를 통해서 얻을 수 있 으며, 이 모드의 이름 리스트 중에서 속성 데이터 값의 내용을 읽어오거나 수정하기를 원할 경우의 그 모드의 이름을 의미한다.
- `cmd` - [in] 컨트롤(control) 명령 `MC_MDAMODECTL_GET` / `MC_MDAMODECTL_SET`
- `pID` - [in] 컨트롤 명령을 수행할 속성 아이디
- `buf` - [in/out] 컨트롤 명령에서 사용할 수 buf 컨트롤 명령이 `MC_MDAMODECTL_SET` 일 경우에는 [in] 컨트롤 명령이 `MC_MDAMODECTL_GET` 일 경우에는 [out]

**반환 값**

성공

실패

- `M_E_ERROR` - 기타 알 수 없는 이유
- `M_E_NOTSUP` - 클립의 타입, 혹은 단말에서 해당 모드 설정 정보를 지원하지 않음
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

1. 모드 이름 규칙 모든 모드는 다른 모드와 구별되게 할 수 있는 이름을 가진다. 모드 이름은 개발자 임의 로 정하는 것이 아니라, 아래의 이름 규칙에 따라서 정해진다. ① 모드는 최소한 한 개 이상은 지원해야 하며, 그 모드의 이름은 “DEFAULT_MODE” 이다 ② 이통사나 제조사에서 제공하는 모드일 경우에는, 아래의 규칙에 따른다. (이통사/제조사이름)_MODE_(인덱스) Ex) SKT 에서 세가지의 모드를 지원한다고 하면, 각 세가지 모드의 이름은, SKT_MODE_0, SKT_MODE_1, SKT_MODE_2 가 된다. 2. DEFAULT_MODE의 속성 인자 “DEFAULT_MODE” 라는 이름을 가지는 모드는, 단말에서 무조건 제공을 하여야 하는 모드 이다. 이 모드는 각 미디어 장치가 일반적으로 가지고 있는 속성 인자들로 구성되 어 있다. 3. 미디어 타입별 DEFAULT_MODE 가 가지게 되는 속성 인자 미디어 장치 속성 정보 ring tone “audio/ONEPOLY” “audio/GVMONEPOLY” “audio/MIDI” “audio/TONE” “audio/FREQTONE" “Qualcomm_CMX” “Yamaha_MA1” “Yamaha_MA2” “Yamaha_MA3” “Yamaha_SMAF” “Yamaha_SMAF- Phrase” “Yamaha_SMAF-Audio” vocoder “IS96” “IS96A” “IS733” “IS127” “G.723.1” “AMR-WB” “AMR-NB” general “audio/WAVE” Sample Per Second sound “audio/MP3” Significant bits per sample “audio/AAC” Number of Channels “audio/AAC+” Balance video “video/MPEG4” Location ( x position, y position ) “VOD_URL” Size( width, height ) “video/H.263” Axis “video/H.264” Bright video “video/MJPEG” MagPower capture ‘image/JPEG” Resolution ( x , y ) YUV Resolution ( x , y ) FrameRate 4. DEFAULT_MODE 가 가지게 되는 속성 아이디의 상세 설명 미디어 속성이름 설명 장치 ring tone vocoder 오디오 샘플 속도. 디폴트 값은 8000KHz 이 Sample Per Second 다. Significant bits per 오디오 샘플 크기. 디폴트 값은 8비트 이다. sample 채널의 개수 ( 모노 / 스테레오 ), 디폴드 값은 Number of Channels 모노 이다. 사운드 밸런스. 50을 기준으로 50 보다 작은 값이면 좌측 사운드가 더 커지고, 50 보다 큰 Balance 값이면 우측 사운드가 더 커진다. 밸런스값의 영역은 0 에서 100 사이이다. 디폴트 값은 50 이다. video Location ( x position, y 화면의 X 좌표 와 Y 좌표 (픽셀단위) video position ) 디폴트 값은 X 좌표는 0, Y 좌표는 0 이다 capture 화면의 너비와 높이 (픽셀단위) Size( width, height ) 디폴트 값은 전체 화면의 크기이다. 화면의 회전/반전 값 (화면의 회전/반전 값은 Axis 구조체MH_MdaCameraSetAxis 를 참고한다.) 디폴트 값은 정상 화면이다. 화면의 밝기.(퍼센트단위). 디폴트 값은 50이 Bright 다. 화면의 배율. (퍼센트단위, 100이면 보통 비 MagPower 율 , 200이면 2배율, 400이면 4배율, 150 이면 1.5 배율) 디폴트 값은 100이다. 해상도의 가로값과 세로값.(픽셀단위) 디폴트 Resolution ( x , y ) 값은 320*240 이다. YUV해상도의 가로값과 세로값.(픽셀단위) YUV Resolution ( x , y ) 디폴트 값은 320*240이다. FrameRate 초당 프레임의 개수. 디폴트 값은 10 이다.

### MC_mdaClipPutData

**프로토타입**

```c
M_Int32 MC_mdaClipPutData (MC_MdaClip* clip, M_Byte* buf, M_Int32 size)
```

**설명**

입력 할 미디어 데이터가 메모리에 저장되어 있을 때 클립에 미디어 데이타를 복사 한다. 미디어 데이타는 클립생성당시 설정한 타입의 데이타이어야 한다. 클립내의 데 이타는 매체재생기에서 재생되면 줄어들고, `MC_mdaClipPutData`()로 늘어나게 된다. 복사할 데이타가 크기가 클립내부버퍼가 수용할 데이타보다 크면 수용할 수 있는 만 큼만 복사된다.

**매개 변수**

- `clip` - [in] 클립
- `buf` - [in] 직접버퍼
- `size` - [in] 복사할 버퍼 크기

**반환 값**

성공

복사된 크기
실패

없음

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipGetData

**프로토타입**

```c
M_Int32 MC_mdaClipGetData(MC_MdaClip* clip, M_Byte* buf, M_Int32 size)
```

**설명**

클립에서 버퍼로 미디어 데이타를 복사한다. 클립내의 데이타는 매체재생기에서 녹 음되면 늘어나고, `MC_mdaClipGetData`()로 줄어들게 된다. 클립내부의 데이타가 전달 한 버퍼보다 크면 버퍼크기만큼만 복사된다. 이 함수는 클립 타입이 "MEDIADEVICES"에서 얻어진 타입일때 사용된다.

**매개 변수**

- `clip` - [in] 클립
- `buf` - [in] 직접버퍼
- `size` - [in] 복사할 버퍼 크기

**반환 값**

성공

복사된 크기
실패

없음

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipAvailableDataSize

**프로토타입**

```c
M_Int32 MC_mdaClipAvailableDataSize(MC_MdaClip* clip)
```

**설명**

클립에서 이용가능한 데이타 크기(클립 내부버퍼 크기가 아님)

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

이용가능한 데이타 크기
실패

- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipClearData

**프로토타입**

```c
M_Int32 MC_mdaClipClearData (MC_MdaClip* clip)
```

**설명**

클립내의 이용가능한 데이타를 모두 버린다.

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

실패

- `M_E_ERROR` - 사운드 재생이나 일시정지 상태에서 이 함수가 호출 될 경우 발생함.
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipSetPosition

**프로토타입**

```c
M_Int32 MC_mdaClipSetPosition(MC_MdaClip* clip, M_Int32 ms)
```

**설명**

재생을 시작할 위치를 설정한다. 재생위치 설정기능을 지원하지 않는 타입으로 생성 된 클립에 이 함수를 호출할 경우, M_E_NOTSUP가 반환된다.

**매개 변수**

- `clip` - [in] 클립
- `ms` - [in] 클립 재생을 시작할 시작 시점(milli second)

**반환 값**

성공

실패

- `M_E_NOTSUP` - 클립재생기가 재생위치 설정기능을 제공하지 않음
- `M_E_ERROR` - 설정 실패
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipGetVolume

**프로토타입**

```c
M_Int32 MC_mdaClipGetVolume(MC_MdaClip* clip)
```

**설명**

클립 재생기의 볼륨을 읽어온다. 클립 재생기의 독립적인 볼륨 설정을 지원할 경우, 이 함수는 클립 재생기의 볼륨을 읽어온다. 지원하지 않을 경우는, 클립생성 타입이 달라도 같은 볼륨소스를 가리킬 수 있다. 볼륨의 최소값은 0, 최대값은 100이다.

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

볼륨 값
실패

- `M_E_NOTSUP` - 볼륨 값이 존재하지 않는 미디어 장치부작용
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipSetVolume

**프로토타입**

```c
void MC_mdaClipSetVolume(MC_MdaClip* clip, M_Int32 level)
```

**설명**

클립 재생기의 볼륨을 설정한다. 클립 재생기의 독립적인 볼륨 설정을 지원할 경우, 이 함수는 클립 재생기의 볼륨을 설정한다. 지원하지 않을 경우는, 클립생성 타입이 달라도 같은 볼륨소스를 가리킬 수 있다. 볼륨 값의 최소는 0, 최대는 100이다.

**매개 변수**

- `clip` - [in] 클립
- `level` - [in] 볼륨 값(0-100사이의 볼륨 값)

**반환 값**

성공

실패

- `M_E_NOTSUP` - 볼륨 값 설정을 지원하지 않는 미디어 장치
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaPlay

**프로토타입**

```c
M_Int32 MC_mdaPlay(MC_MdaClip* clip, M_Boolean repeat)
```

**설명**

클립의 데이타를 재생한다. 이 함수가 불려 매체처리를 시작하면 클립생성시 등록된 콜백 함수에 `MC_MDA_STATUS_STARTED` 상태가 전달된다. 이미 함수가 불려 매체를 처리하고 있었다면 이 함수는 아무런 역할을 하지 않는다. 클립데이타가 소진되면 콜백함수에 MC_MDA_STATUS_END_OF_DATA상태가 전달된다. 스트리밍 재생을 하고 싶은 경우에는 클립 데이타가 완전 소진되기 전에, 주기적으 로 `MC_mdaClipPutData`()로 클립 데이타를 채워주어야 한다.

**매개 변수**

- `clip` - [in] 클립
- `repeat` - [in] 0이면 한번, 1이면 반복 재생

**반환 값**

성공

실패

- `M_E_INUSE` - 클립재생기가 이미 다른 클립을 재생하고 있음
- `M_E_ERROR` - 이미 같은 클립을 재생 중에 있음
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaPause

**프로토타입**

```c
M_Int32 MC_mdaPause(MC_MdaClip* clip)
```

**설명**

매체 처리(재생/녹음)를 일시적으로 멈춘다. 이 함수가 불려 매체처리 일시 정지하게 되면 클립생성시 등록한 콜백 함수에 `MC_MDA_STATUS_PAUSED` 상태가 전달된다. 일시로 멈추어 있거나, 정지되어 있 는 처리기에 대해서 이 함수를 다시 부르면, 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

실패

- `M_E_NOTSUP` - paue를 지원하지 않는 클립재생기
- `M_E_ERROR` - 이미 멈추어 있거나, 정지되어 있음
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaResume

**프로토타입**

```c
M_Int32 MC_mdaResume(MC_MdaClip* clip)
```

**설명**

일시 정지한 매체처리(재생/녹음)를 재개한다. 이 함수가 불려 매체처리를 재개하면 클립생성시 등록한 콜백 함수에 `MC_MDA_STATUS_RESUMED` 상태가 전달된다. 매체처리중인 처리기에 대해서 이 함수를 다시 부르면, 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

실패

- `M_E_NOTSUP` - resume를 지원하지 않는 클립재생기
- `M_E_ERROR` - 이미 매체처리 중
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaStop

**프로토타입**

```c
M_Int32 MC_mdaStop(MC_MdaClip* clip)
```

**설명**

매체처리(재생/녹음)를 종료한다. 이 함수가 불려 매체처리를 종료하면 클립생성시 등록한 콜백 함수에 `MC_MDA_STATUS_STOPPED` 상태가 전달된다. 정지되어 있는 처리기에 대해서 이 함수를 다시 부르면, 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

실패

- `M_E_ERROR` - 이미 정지되어 있음
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaRecord

**프로토타입**

```c
M_Int32 MC_mdaRecord(MC_MdaClip* clip)
```

**설명**

녹음을 시작한다. 녹음을 지원하지 않는 타입으로 생성된 클립으로 녹음을 시도할 경우, 아무 기능도 하지 않는다. 이 함수가 불려 매체처리를 시작하면 클립생성시 등록된 콜백 함수에 MC_MDA_STATUS_RECORDED상태가 전달된다. 이미 함수가 불려 녹음 중이었다 면, 이 함수는 아무런 역할을 하지 않는다. 녹음 중, 클립 내부버퍼가 완전히 차면 콜백함수에 MC_MDA_STATUS_FULL상태가 전달된다. 스트리밍 녹음을 하고 싶은 경우에는 클립 내부버퍼가 완전히 차기 전에, 주기적으 로 `MC_mdaClipGetData`()로 클립 내부버퍼를 비워주어야 한다.

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

실패

- `M_E_INUSE` - 이미 녹음중인 다른 클립이 있음
- `M_E_ERROR` - 이미 같은 클립을 녹음 중에 있음
- `M_E_INVALID` - CLIP이 NULL일 때

**부작용**

없음

**참고 항목**

없음

### MC_mdaGetVolume

**프로토타입**

```c
M_int32 MC_mdaGetVolume()
```

**설명**

볼륨의 값을 리턴한다. 각 디바이스마다 독립적인 볼륨이 설정되었을 경우, 이 값은 정확하지 않을 수 있다. 그럴 경우, 정확한 각 디바이스의 볼륨은 `MC_mdaClipGetVolume` ()으로 읽어와야 한다 반환되는 볼륨 값은 0 – 100사이의 값 으로 환산하여 반환되어야 한다. 0-100사이 값을 어느 정도의 볼륨세기와 일치시키는 가는 아래의 예처럼 하드웨어가 지원하는 볼륨단계를 백분율로 일치시킨 것에 따른 다. 하드웨어가 몇 단계의 볼륨세기를 지원하는가는 `MC_knlGetSystemProperty`()에서 반환한다. 예) 볼륨세기가 강, 약 두 개인 하드웨어 => 1-50 : 약 볼륨 51-100 : 강 볼륨 볼륨세기가 강,중,약 세 개인 하드웨어 => 1-33:약 볼륨, 34-66:중 볼륨, 67-100: 강 볼륨

**매개 변수**

없음

**반환 값**

성공

볼륨 값
실패

- `M_E_NOTSUP` - 볼륨 설정을 지원하지 않음

**부작용**

없음

**참고 항목**

없음

### MC_mdaSetVolume

**프로토타입**

```c
void MC_mdaSetVolume(M_Int32 value)
```

**설명**

볼륨을 설정한다. 볼륨을 설정할 수 있는 모든 디바이스의 볼륨을 설정한다. 각 디바 이스마다 독립적인 불륨을 설정할 경우, Clip에 있는 볼륨 API을 이용하도록 한다. 설 정할 볼륨의 최소값은 0 이고, 최대값은 100이다.

**매개 변수**

- `value` - [in] 볼륨 값(0-100사이의 볼륨 값)

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MC_mdaVibrator

**프로토타입**

```c
M_Int32 MC_mdaVibrator(M_Int32 level, M_Int32 timeout)
```

**설명**

Vibrator를 제어 한다. 지정한 시간 동안 on시킨 후 자동으로 꺼진다. 매개변수 level값이 0보다 큰 경우만 timeout 값이 유효하다. level값 0은 vibrator가 꺼지는 것을 의미한다. 진동강도는 매개변수 level값으로 정해지고 0-100사이의 값이 올 수 있다. 100은 하드웨어가 지원하는 가장 강한 진동을 0은 가장 약한 진동을 의 미한다. 0-100사이 값을 어느 정도의 진동세기와 일치시키는가는 아래의 예처럼 하드 웨어가 지원하는 진동단계를 백분율로 일치시킨 것에 따른다. 하드웨어가 몇 단계의 진동세기를 지원하는가는 `MC_knlGetSystemProperty`(“VIBRATORLEVEL”)에서 알 수 있다. 예) 진동세기가 하나인 하드웨어 => 1-100 : 진동 진동세기가 강, 약 두 개인 하드웨어 => 1-50 : 약 진동, 51-100 : 강진 동 진동세기가 강,중,약 세 개인 하드웨어 => 1-33:약 진동, 34-66:중진 동, 67-100: 강진 동

**매개 변수**

- `level` - [in] 0이면 off, 1-100이면 운영체제에서 일치시킨 진동세기로 진동
- `timeout` - [in] 진동시간, 밀리 초 단위

**반환 값**

성공

실패

- `M_E_INUSE` - 현재 요청한 vibrator가 사용중인 경우
- `M_E_ERROR` - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음

### MC_mdaSetMuteState

**프로토타입**

```c
M_Int32 MC_mdaSetMuteState(M_int32 cateID, M_Boolean bmute)
```

**설명**

단말기의 볼륨 카테고리 별로 소리 발생 방지를 설정한다. 단말에서 지원하는 볼륨의 카테고리를 아래와 같이 분류한다. 카테고리 아이디 설명 Default volume 예 `MC_M` 음성의 재생/녹음 특성을 갖는 단말기 DA_VOLCAT 다. 의 통화 음량 E_VOICE `MC_M` 착신 벨 특성을 갖는다. 예를 단말기 DA_VOLCAT 들어 현재 착신 벨이 진동으로 되어 의 착신 벨 음 E_RING 있다면, play 시 소리가 나지 않고 량 진동이 발생한다. 별도의 멜로디용 speaker가 따로 있다면 이를 통해 소리가 발생한다. 즉, 단말기에 전화 가 왔을 때의 특성 그대로 행동 한 다. `MC_M` 키 톤의 특성을 갖는다. 단말기 DA_VOLCAT 의 키 톤 음량 E_KEYTONE `MC_M` SMS message 도착 경고음 SMS 메 DA_VOLCAT 특성을 갖는다. 시지 음량 E_MESSAG E `MC_M` 알람 경고음 특성을 갖는다. 알람 음 DA_VOLCAT 량 E_ALARM `MC_M` No service, low battery 각종 경고음 DA_VOLCAT 경고음 특성을 갖는다. 음량 E_ALERT `MC_M` 멀티미디어 장치의 음량을 말 멀티미 DA_VOLCAT 한다. 여기에서 멀티미디어 장치의 디어 음량 E_MMEDIA 음량이란, 플랫폼에서 지원하는 모든 멀티미디어 장치의 마스터 볼륨을 지칭하며, 이 마스터 볼륨은 모든 멀 티미디어 장치의 영향을 미친다. 각 미디어 장치별로 볼륨을 설정하고 싶을 시에는 `MC_mdaClipGetVolume`/`MC_mdaCli` pSetVolume 함수를 사용한다.

**매개 변수**

- `cateID` - [in] 볼륨 카테고리 아이디
- `bmute` - [in] 소리발생 방지 설정 `TRUE` 소리 발생 방지 `FALSE` 소리 발생 허용

**반환 값**

성공

실패

- `M_E_ERROR` - 실패
- `M_E_INVALID` - 존재하지 않는 카테고리 아이디

**부작용**

없음

**참고 항목**

없음

### MC_mdaGetMuteState

**프로토타입**

```c
M_Int32 MC_mdaGetMuteState(M_int32 cateID)
```

**설명**

단말기의 볼륨 카테고리 별로 소리 발생 방지 상태를 얻어온다. 단말에서 지원하는 볼륨의 카테고리를 아래와 같이 분류한다. 카테고리 아이디 설명 Default volume 예 `MC_M` 음성의 재생/녹음 특성을 갖는 단말기 DA_VOLCAT 다. 의 통화 음량 E_VOICE `MC_M` 착신 벨 특성을 갖는다. 예를 단말기 DA_VOLCAT 들어 현재 착신 벨이 진동으로 되어 의 착신 벨 음 E_RING 있다면, play 시 소리가 나지 않고 량 진동이 발생한다. 별도의 멜로디용 speaker가 따로 있다면 이를 통해 소리가 발생한다. 즉, 단말기에 전화 가 왔을 때의 특성 그대로 행동 한 다. `MC_M` 키 톤의 특성을 갖는다. 단말기 DA_VOLCAT 의 키 톤 음량 E_KEYTONE `MC_M` SMS message 도착 경고음 SMS 메 DA_VOLCAT 특성을 갖는다. 시지 음량 E_MESSAG E `MC_M` 알람 경고음 특성을 갖는다. 알람 음 DA_VOLCAT 량 E_ALARM `MC_M` No service, low battery 각종 경고음 DA_VOLCAT 경고음 특성을 갖는다. 음량 E_ALERT `MC_M` 멀티미디어 장치의 음량을 말 멀티미 DA_VOLCAT 한다. 여기에서 멀티미디어 장치의 디어 음량 E_MMEDIA 음량이란, 플랫폼에서 지원하는 모든 멀티미디어 장치의 마스터 볼륨을 지칭하며, 이 마스터 볼륨은 모든 멀 티미디어 장치의 영향을 미친다. 각 미디어 장치별로 볼륨을 설정하고 싶을 시에는 `MC_mdaClipGetVolume`/`MC_mdaCli` pSetVolume 함수를 사용한다.

**매개 변수**

- `cateID` - [in] 볼륨카테고리 아이디

**반환 값**

성공

- `M_E_SUCCESS` - 성공 실패
- `M_E_ERROR` - 실패
- `M_E_NOTSUP` - 디폴트 볼륨값 설정을 지원하지 않을 경우
- `M_E_INVALID` - 존재하지 않는 카테고리 아이디

**부작용**

없음

**참고 항목**

없음

### MC_mdaSetDefaultVolume

**프로토타입**

```c
M_Int32 MC_mdaSetDefaultVolume(M_int32 cateID, M_Int32 vol)
```

**설명**

단말에 디폴트 볼륨을 설정한다. 디폴트 볼륨의 설정은 CP(Contents Provider) 레 벨의 보안 수준을 가진 어플리케이션에서만 가능하다. 단말에서 지원하는 볼륨의 카테고리를 아래와 같이 분류한다. 카테고리 아이디 설명 Default volume 예 `MC_M` 일반적인 application에서 사용 단말기 DA_VOLCAT 되는 특성을 갖는다. 의 application E_GENERAL 음량 `MC_M` 음성의 재생/녹음 특성을 갖는 단말기 DA_VOLCAT 다. 의 통화 음량 E_VOICE `MC_M` 착신 벨 특성을 갖는다. 예를 단말기 DA_VOLCAT 들어 현재 착신 벨이 진동으로 되어 의 착신 벨 음 E_RING 있다면, play 시 소리가 나지 않고 량 진동이 발생한다. 별도의 멜로디용 speaker가 따로 있다면 이를 통해 소리가 발생한다. 즉, 단말기에 전화 가 왔을 때의 특성 그대로 행동 한 다. `MC_M` 키 톤의 특성을 갖는다. 단말기 DA_VOLCAT 의 키 톤 음량 E_KEYTONE `MC_M` SMS message 도착 경고음 SMS 메 DA_VOLCAT 특성을 갖는다. 시지 음량 E_MESSAG E `MC_M` 알람 경고음 특성을 갖는다. 알람 음 DA_VOLCAT 량 E_ALARM `MC_M` No service, low battery 각종 경고음 DA_VOLCAT 경고음 특성을 갖는다. 음량 E_ALERT `MC_M` 멀티미디어 장치의 음량을 말 멀티미 DA_VOLCAT 한다. 여기에서 멀티미디어 장치의 디어 음량 E_MMEDIA 음량이란, 플랫폼에서 지원하는 모든 멀티미디어 장치의 마스터 볼륨을 지칭하며, 이 마스터 볼륨은 모든 멀 티미디어 장치의 영향을 미친다. 각 미디어 장치별로 볼륨을 설정하고 싶을 시에는 `MC_mdaClipGetVolume`/`MC_mdaCli` pSetVolume 함수를 사용한다. `MC_M` 게임 시 재생되는 특성을 갖 게임 음 DA_VOLCAT 는다. 량 E_GAME

**매개 변수**

- `cateID` - [in] 볼륨카테고리 아이디
- `vol` - [in] 볼륨값 (0-100 사이의 값)

**반환 값**

성공

실패

- `M_E_NOTSUP` - 디폴트 볼륨값 설정을 지원하지 않을 경우
- `M_E_ERROR` - 기타 에러
- `M_E_INVALID` - 존재하지 않는 카테고리 아이디

**부작용**

없음

**참고 항목**

없음

### MC_mdaGetDefaultVolume

**프로토타입**

```c
M_Int32 MC_mdaGetDefaultVolume(M_int32 cateID)
```

**설명**

단말이 설정한 디폴트 볼륨을 얻는다. 단말에서 지원하는 볼륨의 카테고리를 아래와 같이 분류한다. 카테고리 아이디 설명 Default volume 예 `MC_M` 일반적인 application에서 사용 단말기 DA_VOLCAT 되는 특성을 갖는다. 의 application E_GENERAL 음량 `MC_M` 음성의 재생/녹음 특성을 갖는 단말기 DA_VOLCAT 다. 의 통화 음량 E_VOICE `MC_M` 착신 벨 특성을 갖는다. 예를 단말기 DA_VOLCAT 들어 현재 착신 벨이 진동으로 되어 의 착신 벨 음 E_RING 있다면, play 시 소리가 나지 않고 량 진동이 발생한다. 별도의 멜로디용 speaker가 따로 있다면 이를 통해 소리가 발생한다. 즉, 단말기에 전화 가 왔을 때의 특성 그대로 행동 한 다. `MC_M` 키 톤의 특성을 갖는다. 단말기 DA_VOLCAT 의 키 톤 음량 E_KEYTONE `MC_M` SMS message 도착 경고음 SMS 메 DA_VOLCAT 특성을 갖는다. 시지 음량 E_MESSAG E `MC_M` 알람 경고음 특성을 갖는다. 알람 음 DA_VOLCAT 량 E_ALARM `MC_M` No service, low battery 각종 경고음 DA_VOLCAT 경고음 특성을 갖는다. 음량 E_ALERT `MC_M` 멀티미디어 장치의 음량을 말 멀티미 DA_VOLCAT 한다. 멀티미디어 장치의 음량을 말 디어 음량 E_MMEDIA 한다. 여기에서 멀티미디어 장치의 음량이란, 플랫폼에서 지원하는 모든 멀티미디어 장치의 마스터 볼륨을 지칭하며, 이 마스터 볼륨은 모든 멀 티미디어 장치의 영향을 미친다. 각 미디어 장치별로 볼륨을 설정하고 싶을 시에는 `MC_mdaClipGetVolume`/`MC_mdaCli` pSetVolume 함수를 사용한다. `MC_M` 게임 시 재생되는 특성을 갖 게임 음 DA_VOLCAT 는다. 량 E_GAME

**매개 변수**

- `cateID` - [in] 볼륨카테고리 아이디

**반환 값**

성공

볼륨 값 (0-100 사이의 값)
실패

- `M_E_ERROR` - 실패
- `M_E_NOTSUP` - 디폴트 볼륨값 설정을 지원하지 않을 경우
- `M_E_INVALID` - 존재하지 않는 카테고리 아이디

**부작용**

없음

**참고 항목**

없음

### MC_mdaSetClipArea

**프로토타입**

```c
M_Int32 MC_mdaSetClipArea(M_Int32 screen, M_Int32 x, M_Int32 y, M_Int32 w, M_Int32 h)
```

**설명**

특정 LCD에 업데이트 방지 영역을 설정한다. 설정된 영역은 매체 재생기를 통해 비디오 미디어를 재생할 경우, 비디오 미디어를 재생하는 장치에 의해 업데이트되지 않는다.

**매개 변수**

- `screen` - [in] 0인 경우에 주 LCD 이고, 1인 경우에는 외부 보조 LCD.
- `x` - [in] x 좌표
- `y` - [in] y좌표
- `w` - [in] 가로 크기
- `h` - [in] 세로 크기

**반환 값**

성공

영역 고유 ID
실패

- `M_E_INUSE` - 지정 영역이 이미 할당되어있음.
- `M_E_NOTSUP` - 해당 기능을 지원하지 않는 경우
- `M_E_ERROR` - 알 수 없는 이유로 실패

**부작용**

없음

**참고 항목**

없음

### MC_mdaReleaseClipArea

**프로토타입**

```c
M_Int32 MC_mdaReleaseClipArea(M_Int32 regionID)
```

**설명**

설정된 업데이트 방지 영역을 해제한다.

**매개 변수**

- `regionID` - [in] 영역 고유 ID

**반환 값**

성공

실패

- `M_E_NOTEXIST` - 잘못되거나 등록되어있지 않은 ID
- `M_E_INUSE` - 지정 영역이 이미 할당되어있음.
- `M_E_NOTSUP` - 해당 기능을 지원하지 않는 경우
- `M_E_ERROR` - 알 수 없는 이유로 실패

**부작용**

없음

**참고 항목**

없음

### MC_mdaUpdateClipArea

**프로토타입**

```c
M_Int32 MC_mdaUpdateClipArea (M_Int32 regionID, M_Int32 x, M_Int32 y,
M_Int32 w, M_Int32 h)
```

**설명**

이미 설정된 업데이트 방지 영역의 위치/크기를 변경한다.

**매개 변수**

- `regionID` - [in] 영역 고유 ID
- `x` - [in] x 좌표
- `y` - [in] y좌표
- `w` - [in] 가로 크기
- `h` - [in] 세로 크기

**반환 값**

성공

실패

- `M_E_NOTEXIST` - 잘못되거나 등록되어있지 않은 ID
- `M_E_INUSE` - 지정 영역이 이미 할당되어있음.
- `M_E_NOTSUP` - 해당 기능을 지원하지 않는 경우
- `M_E_ERROR` - 알 수 없는 이유로 실패

**부작용**

없음

**참고 항목**

없음
