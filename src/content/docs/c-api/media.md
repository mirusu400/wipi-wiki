---
title: "5.1.6. 매체 처리기"
---

사운드나 동영상등의 모든 Media 에 대해서 처리를 해주는 매체 처리기와 관련된 함수와 톤 재생 및 음성녹음 및 볼륨 조절에 관련한 패키지 이다

사운드, 톤, 동영상등의 모든 데이타는 클립(CLIP)으로 추상화되어 매체처리기에 서 수행한다. 매체재생기에서 지원하는 타입은 `MC_knlSetSystemProperty()`의 `"MEDIADEVICES"`에 의해 구해진 타입들이다.

매체처리, 톤 재생, 녹음 등의 상태 변화는 등록하는 콜백 함수로 전달된다. 볼륨 조절은 톤, 사운드, 녹음에 대해 각각 가능하다.

```c
MC_MDA_STATUS_ERROR
```

**설명**

오류로 인한 정지 상태. 상수값은 -1.

**프로토타입**

```c
#define MC_MDA_STATUS_ERROR (-1)
```

### MC_MDA_STATUS_END_OF_DATA

**설명**

매체(혹은 톤)처리시 - 처리기가 매체(혹은 톤) 데이터의 마지막에 도달한 상태. 상수값은 1.

**프로토타입**

```c
#define MC_MDA_STATUS_END_OF_DATA 1
```

### MC_MDA_STATUS_START

**설명**

매체(혹은 톤)처리시 - 매체(혹은 톤) 처리를 시작한 상태. 상수값은 2.

**프로토타입**

```c
#define MC_MDA_STATUS_STARTED 2
```

### MC_MDA_STATUS_STOPP

**설명**

매체(혹은 톤)처리시 - 매체(혹은 톤) 처리를 종료한 상태 녹음시 – 녹음을 중단한 상태. 상수값은 3

```c
MC_MDA_STATUS_PAUSE
```

**프로토타입**

```c
#define MC_MDA_STATUS_STOPP 3
```

**프로토타입**

```c
#define MC_MDA_STATUS_PAUSED 4
```

**설명**

매체(혹은 톤)처리시 - 매체(혹은 톤) 처리를 잠시 멈춘 상태 녹음시 – 녹음을 잠시 멈춘 상태. 상수값은 4

### MC_MDA_STATUS_RESUME

**설명**

매체(혹은 톤)처리시 - 잠시 멈춘 매체(혹은 톤) 처리를 재개한 상태 녹음시 – 잠시 멈춘 녹음을 재개한 상태. 상수값은 5

**프로토타입**

```c
#define MC_MDA_STATUS_RESUMED 5
```

### MC_MDA_STATUS_RECORD

**설명**

녹음시 – 녹음을 시작한 상태. 상수값은 6

**프로토타입**

```c
#define MC_MDA_STATUS_RECORDED 6
```

### MC_MDA_STATUS_FULL_OF_DATA

**설명**

녹음시 – 클립내부버퍼가 완전히 채워진 상태. 상수값은 7.

**프로토타입**

```c
#define MC_MDA_STATUS_FULL_OF_DATA 7
```

### MC_MDA_VOLSEL_CUR

**설명**

현재 볼륨값을 의미하는 상수. 상수값은 0.

**프로토타입**

```c
#define MC_MDA_VOLSEL_CUR 0
```

### MC_MDA_VOLSEL_MIN

**설명**

최소 볼륨값을 의미하는 상수. 상수값은 1.

**프로토타입**

```c
#define MC_MDA_VOLSEL_MIN 1
```

### MC_MDA_VOLSEL_MAX

**설명**

최대 볼륨값을 의미하는 상수. 상수값은 2.

**프로토타입**

```c
#define MC_MDA_VOLSEL_MAX 2
```

### (*MEDIACB)

**설명**

처리기의 상태가 변경될 때 불려지는 콜백함수. 상태 값은 매체 처리 상태를 참조.

**프로토타입**

```c
typedef void (*MEDIACB)(MC_MdaClip* clip, M_Int32 status)
```

**매개 변수**

- `clip` - ? 클립
- `status` ? 매체처리기 상태

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipCreate

**설명**

특정 타입의 CLIP 을 생성한다. 지원되는 타입은 `MC_knlSetSystemProperty()`의 "MEDIADEVICES"에 의해 구해진 타입들이다. 타입은 MIME 에서 지원하는 타입일 경 우 "audio/xxx", "video/xxx"와 같이 MIME 타입을 따른다.

메모리 버퍼를 데이터로 입력하고자 하는 경우 `MC_mdaClipPutData()`를 통하고, file 로 데이터를 입력하고자 하는 경우 `MC_mdaClipPutDataByFile()` 을 통하여 재 생할 데이터를 입력한다.

Clip 의 버퍼 크기는 입력하고자 하는 데이터의 전체 크기만큼 생성해야 한다.

콜백함수가 설정되지 않으면 매채재생기의 상태변화가 전달되지 않는다.

**프로토타입**

```c
MC_MdaClip* MC_mdaClipCreate(M_Char* mType, M_Int32 bufSize, MEDIACB cb)
```

**매개 변수**

- `mType`  - [in] 미디어타입
- `bufSzie`  - [in] 버퍼 크기(CLIP 내에 생성될 버퍼크기)
- `cb`  - [in] 클립을 매체처리기에서 처리하는중 상태변화를 알려 줄 콜백함수

**반환 값**

성공

- `MC_MdaClip` 객체 포인터 0

실패

- 0

**부작용**

없음

**참고 항목**

없음


### MC_mdaClipFree

**설명**

클립에 할당된 모든 리소스를 해제한다.

**프로토타입**

```c
M_Int32 MC_mdaClipFree(MC_MdaClip* clip)
```

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

- 0

실패

- `M_E_INUSE` - 클립을 재생중이거나 녹음중에 해제할려고 시도함
- `M_E_INVALID` - `clip` 이 NULL 이면 리턴

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipGetType

**설명**

클립의 타입을 구한다.

**프로토타입**

```c
M_Int32 MC_mdaClipGetType(MC_MdaClip* clip, M_Byte* buf, M_Int32 bufSize)
```

**매개 변수**

- `clip` - [in] 클립
- `buf` – [out] 타입이 저장될 버퍼
- `bufSize` – [in] 복사할 버퍼 크기

**반환 값**

성공

- 0

실패

- `M_E_SHORTBUF` - 저장할 버퍼가 작음

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipPutData

**설명**

입력 할 미디어 데이터가 메모리에 저장되어 있을 때 클립에 미디어 데이타를 복 사한다. 미디어 데이타는 클립생성당시 설정한 타입의 데이타이어야 한다. 클립내 의 데이타는 매체재생기에서 재생되면 줄어들고, `MC_mdaClipPutData()`로 늘어나게 된다. 복사할 데이타가 크기가 클립내부버퍼가 수용할 데이타보다 크면 수용할 수 있는 만큼만 복사된다.

**프로토타입**

```c
M_Int32 MC_mdaClipPutData (MC_MdaClip* clip, M_Byte* buf, M_Int32 size)
```

**매개 변수**

- `clip`  - [in] 클립
- `buf` – [in] 직접버퍼
- `size` – [in] 복사할 버퍼 크기

**반환 값**

성공

- 복사된 크기

실패

- 없음

**부작용**

없음

**참고 항목**

없음


### MC_mdaClipPutDataByFile

**설명**

입력 할 미디어 데이터가 파일로 저장되어 있을 때, 클립에 미디어 데이타를 복사 한다. 미디어 데이타는 클립생성당시 설정한 타입의 데이타이어야 한다. 클립내의 데이타는 매체재생기에서 재생되면 줄어들고, `MC_mdaClipPutData()`로 늘어나게 된 다. 복사할 데이타가 크기가 클립내부버퍼가 수용할 데이타보다 크면 수용할 수 있는 만큼만 복사된다.

**프로토타입**

```c
M_Int32 MC_mdaClipPutData (MC_MdaClip* clip, M_Byte* filename, M_Int32 size, M_Int32 aMode)
```

**매개 변수**

- `clip`  - [in] 클립
- `filename` – [in] 복사해올 파일 이름
- `size` – [in] 복사할 버퍼 크기
- `aMode`
  - `MC_DIR_PRIVATE_ACCESS` - private 디렉토리에 접근
  - `MC_DIR_SHARED_ACCESS` - shared 디렉토리에 접근
  - `MC_DIR_SYSTEM_ACCESS` - system 디렉토리에 접근

**반환 값**

성공

- 복사된 크기

실패

- 없음

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipGetData

**설명**

클립에서 버퍼로 미디어 데이타를 복사한다. 클립내의 데이타는 매체재생기에서 녹음되면 늘어나고, `MC_mdaClipGetData()`로 줄어들게 된다. 클립내부의 데이타가 전달한 버퍼보다 크면 버퍼크기만큼만 복사된다. 이 함수는 클립 타입이 `"MEDIADEVICES"`에서 얻어진 타입일때 사용된다.

**프로토타입**

```c
M_Int32 MC_mdaClipGetData(MC_MdaClip* clip, M_Byte* buf, M_Int32 size)
```

**매개 변수**

- `clip`  - [in] 클립
- `buf` – [in] 직접버퍼
- `size` – [in] 복사할 버퍼 크기

**반환 값**

성공

- 복사된 크기

실패

- 없음

**부작용**

없음

**참고 항목**

없음


### MC_mdaClipAvailableDataSize

**설명**

클립에서 이용가능한 데이타 크기(클립 내부버퍼 크기가 아님)

**프로토타입**

```c
M_Int32 MC_mdaClipAvailableDataSize(MC_MdaClip* clip)
```

**매개 변수**

- `clip`  - [in] 클립

**반환 값**

이용가능한 데이타 크기

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipClearData

**설명**

클립내의 이용가능한 데이타를 모두 버린다.

**프로토타입**

```c
M_Int32 MC_mdaClipClearData(MC_MdaClip* clip)
```

**매개 변수**

- `clip`  - [in] 클립

**반환 값**

성공

- 0

실패

- `M_E_ERROR` – 사운드 재생이나 일시정지 상태에서 이 함수가 호출 될 경우 발생함.

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipSetPosition

**설명**

재생을 시작할 위치를 설정한다. 재생위치 설정기능을 지원하지 않는 타입으로 생성된 클립에 이 함수를 호출할 경우, `M_E_NOTSUP` 가 반환된다.

**프로토타입**

```c
M_Int32 MC_mdaClipSetPosition(MC_MdaClip* clip, M_Int32 ms)
```

**매개 변수**

- `clip`  - [in] 클립
- `ms` –  [in] 클립 재생을 시작할 시작 시점(milli second)

**반환 값**

성공

- `0`

실패

- `M_E_NOTSUP` - ? 클립재생기가 재생위치 설정기능을 제공하지 않음
- `M_E_ERROR` – 설정 실패

**부작용**

없음

**참고 항목**

없음


### MC_mdaClipGetVolume

**설명**

클립 재생기의 볼륨을 읽어온다. 클립 재생기의 독립적인 볼륨 설정을 지원할 경우, 이 함수는 클립 재생기의 볼륨을 읽어온다. 지원하지 않을 경우는, 클립생성 타입이 달라도 같은 볼륨소스를 가리킬 수 있다.

볼륨의 최소값은 0, 최대값은 100 이다.

**프로토타입**

```c
M_Int32 MC_mdaClipGetVolume(MC_MdaClip* clip)
```

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

- 볼륨값

실패

- `M_E_NOTSUP` – 볼륨값이 존재하지 않는 미디어 장치부작용

**참고 항목**

없음

### MC_mdaClipSetVolume

**설명**

클립 재생기의 볼륨을 설정한다. 클립 재생기의 독립적인 볼륨 설정을 지원할 경 우, 이 함수는 클립 재생기의 볼륨을 설정한다. 지원하지 않을 경우는, 클립생성 타입이 달라도 같은 볼륨소스를 가리킬 수 있다. 볼륨값의 최소는 0, 최대는 100 이다.

**프로토타입**

```c
void MC_mdaClipSetVolume(MC_MdaClip* clip, M_Int32 level)
```

**매개 변수**

- `clip`  - [in] 클립
- `level` – [in] 볼륨 값(0-100사이의 볼륨값)

**반환 값**

- `M_E_NOTSUP` – 볼륨값 설정을 지원하지 않는 미디어 장치

**부작용**

없음

**참고 항목**

없음

### MC_mdaPlay

**설명**

클립의 데이타를 재생한다.

이 함수가 불려 매체처리를 시작하면 클립생성시 등록된 콜백 함수에 `MC_MDA_STATUS_STARTED` 상태가 전달된다. 이미 함수가 불려 매체를 처리하고 있었 다면 이 함수는 아무런 역할을 하지 않는다. 클립데이타가 소진되면 콜백함수에 `MC_MDA_STATUS_END_OF_DATA` 상태가 전달된다.

스트리밍 재생을 하고 싶은 경우에는 클립 데이타가 완전 소진되기 전에, 주기적 으로 `MC_mdaClipPutData()`로 클립 데이타를 채워주어야 한다.

**프로토타입**

```c
M_Int32 MC_mdaPlay(MC_MdaClip* clip, M_Boolean repeat)
```

**매개 변수**

- `clip`  - [in] 클립
- `repeat`  - [in] 0 이면 한번, 1 이면 반복 재생

**반환 값**

성공

- `0`

실패

- `M_E_INUSE` – 클립재생기가 이미 다른 클립을 재생하고 있음
- `M_E_ERROR` – 이미 같은 클립을 재생중에 있음

**부작용**

없음

**참고 항목**

없음

### MC_mdaPause

**설명**

매체 처리(재생/녹음)를 일시적으로 멈춘다.

이 함수가 불려 매체처리 일시 정지하게 되면 클립생성시 등록한 콜백 함수에 `MC_MDA_STATUS_PAUSED` 상태가 전달된다. 일시로 멈추어 있거나, 정지되어 있는 처리기에 대해서 이 함수를 다시 부르면, 이 함수는 아무런 역할을 하지 않는다.

**프로토타입**

```c
M_Int32 MC_mdaPause(MC_MdaClip* clip)
```

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

- 0

실패

- `M_E_NOTSUP` – paue 를 지원하지 않는 클립재생기
- `M_E_ERROR` - 이미 멈추어 있거나, 정지되어 있음

**부작용**

없음

**참고 항목**

없음

### MC_mdaResume

**설명**

일시 정지한 매체처리(재생/녹음)를 재개한다.

이 함수가 불려 매체처리를 재개하면 클립생성시 등록한 콜백 함수에 `MC_MDA_STATUS_RESUMED` 상태가 전달된다. 매채처리중인 처리기에 대해서 이 함수 를 다시 부르면, 이 함수는 아무런 역활을 하지 않는다.

**프로토타입**

```c
M_Int32 MC_mdaResume(MC_MdaClip* clip)
```

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

- 0

실패

- `M_E_NOTSUP` – resume 를 지원하지 않는 클립재생기
- `M_E_ERROR` - 이미 매체처리중

**부작용**

없음

**참고 항목**

없음

### MC_mdaStop

**설명**

매체처리(재생/녹음)를 종료한다.

이 함수가 불려 매체처리를 종료하면 클립생성시 등록한 콜백 함수에 `MC_MDA_STATUS_STOPPED` 상태가 전달된다. 정지되어 있는 처리기에 대해서 이 함수를 다시 부르면, 이 함수는 아무런 역활을 하지 않는다.

**프로토타입**

```c
M_Int32 MC_mdaStop(MC_MdaClip* clip)
```

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

- 0
실패

- `M_E_ERROR` - 이미 정지되어 있음

**부작용**

없음

**참고 항목**

없음

### MC_ mdaRecord

**설명**

녹음을 시작한다.

녹음을 지원하지 않는 타입으로 생성된 클립으로 녹음을 시도할 경우, 아무기능도 하지 않는다. 이 함수가 불려 매체처리를 시작하면 클립생성시 등록된 콜백 함수에 `MC_MDA_STATUS_RECORDED` 상태가 전달된다. 이미 함수가 불려 녹음중이었다면, 이 함수는 아무런 역할을 하지 않는다. 녹음 중, 클립 내부버퍼가 완전히 차면 콜 백함수에 `MC_MDA_STATUS_FULL` 상태가 전달된다.

스트리밍 녹음을 하고 싶은 경우에는 클립 내부버퍼가 완전히 차기전에, 주기적으로 `MC_mdaClipGetData()`로 클립 내부버퍼를 비워주어야 한다.

**프로토타입**

```c
M_Int32 MC_mdaRecord(MC_MdaClip* clip)
```

**매개 변수**

- `clip` - [in] 클립

**반환 값**

성공

- 0

실패

- `M_E_INUSE` – 이미녹음중인 다른클립이 있음
- `M_E_ERROR` – 이미 같은 클립을 녹음중에 있음

**부작용**

없음

**참고 항목**

없음


### MC_mdaGetVolume

**설명**

볼륨의 값을 리턴한다. 각 디바이스마다 독립적인 볼륨이 설정되었을 경우, 이 값 은 정확하지 않을 수 있다. 그럴경우, 정확한 각 디바이스의 볼륨은 `MC_mdaClipGetVolume()`으로 읽어와야 한다 반환되는 볼륨값은 0 – 100 사이의 값으로 환산하여 반환되어야 한다. 0-100 사이값을 어느정도의 볼륨세기와 일치시 키는가는 아래의 예처럼 하드웨어가 지원하는 볼륨단계를 백분율로 일치시킨것에 따른다. 하드웨어가 몇단계의 볼륨세기를 지원하는가는 `MC_knlGetSystemProperty()`에서 반환한다.

> 예) 볼륨세기가 강, 약 두개인 하드웨어 => 1-50 : 약볼륨 51-100 : 강볼륨
> 볼륨세기가 강,중,약 세개인 하드웨어 => 1-33:약볼륨, 34 -66:중볼륨, 67-100:강볼륨

**프로토타입**

```c
M_int32 MC_mdaGetVolume()
```

**매개 변수**

**반환 값**

볼륨 값

**부작용**

없음

**참고 항목**

없음

### MC_mdaSetVolume

**설명**

볼륨을 설정한다. 볼륨을 설정할 수 있는 모든 디바이스의 볼륨을 설정한다. 각 디바이스마다 독립적인 불륨을 설정할 경우, Clip 에 있는 볼륨 API 을 이용하도록 한다. 설정할 볼륨의 최소값은 0 이고, 최대값은 100 이다.

**프로토타입**

```c
void MC_mdaSetVolume(M_Int32 value)
```

**매개 변수**

- `value` - [in] 볼륨값(0-100 사이의 볼륨값)

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MC_mdaVibrator

**설명**

Vibrator 를 제어 한다. 지정한 시간 동안 on 시킨 후 자동으로 꺼진다.

매개변수 level값이 0보다 큰 경우만 timeout 값이 유효하다. level값 0은 virbrator 가 꺼지는 것을 의미한다. 진동강도는 매개변수 level값으로 정해지고 0-100사이의 값 이 올수 있다. 100은 하드웨어가 지원하는 가장 강한 진동을 0은 가장 약한 진동을 의 미한다. 0-100사이값을 어느정도의 진동세기와 일치시키는가는 아래의 예처럼 하드웨 어가 지원하는 진동단계를 백분율로 일치시킨것에 따른다. 하드웨어가 몇단계의 진동 세기를 지원하는가는 `MC_knlGetSystemProperty(“VIBRATORLEVEL”)` 에서 알수 있다.

> 예) 진동세기가 하나인 하드웨어 => 1-100 : 진동
> 진동세기가 강, 약 두개인 하드웨어 => 1-50 : 약진동, 51-100 : 강진동
> 진동세기가 강,중,약 세개인 하드웨어 => 1-33:약진동, 34-66:중진동, 67-100:강진동

**프로토타입**

```c
void MC_mdaVibrator(M_Int32 level, M_Int32 timeout)
```

**매개 변수**

- `level` - [in] 0 이면 off, 1-100 이면 운영체제에서 일치시킨 진동세기로 진동
- `timeout` - [in] 진동시간, 밀리초 단위

**부작용**

없음

**참고 항목**

없음

### MC_mdaSetMuteState

**설명**

단말기의 음원별 소리 발생 방지를 설정한다.

**프로토타입**

```c
M_Int32 MC_mdaSetMuteState(M_int32 source, M_Boolean bmute)
```

**매개 변수**

- `source` – [in] 볼륨소스. `MC_MDA_VOLTYPE_TONE`, `MC_MDA_VOLTYPE_SOUND`,`MC_MDA_VOLTYPE_RECORDER` 중의 하나가 될 수 있다
- `bmute` – [in] 소리발생 방지 설정
  - `TRUE` - 소리 발생 방지
  - `FALSE` - 소리 발생 허용

**반환 값**

성공

- `M_E_SUCCESS` – 성공

실패

- `M_E_ERROR` – 실패

**부작용**

없음

**참고 항목**

없음

### MC_mdaGetMuteState

**설명**

단말기의 음원별 소리 발생 방지 설정 상태를 얻는다.

**프로토타입**

```c
M_Boolean MC_mdaGetMuteState(M_int32 source)
```

**매개 변수**

- `source` – [in] 볼륨소스. `MC_MDA_VOLTYPE_TONE`, `MC_MDA_VOLTYPE_SOUND`,`MC_MDA_VOLTYPE_RECORDER` 중의 하나가 될 수 있다

**반환 값**

- `TRUE` - 소리 발생 방지
- `FALSE` - 소리 발생 허용

**부작용**

없음

**참고 항목**

없음
