---
title: "2. VGI 관련 API"
---

## 2.1. VGI 개요

#### API 범위

VGI (Vector Graphic Image) 표준은 WIPI 2.0상에서 Vector Graphic Image관련 매체의 처리를 위한 단일의 API규격이다. 현재 이 API를 통해 지원되는 매체는 디지탈아리 아의 Mobile Flash와 네오엠텔의 SIS3가 있다. 정의되는 VGI Open API 규격에 따라 앞으로 벡터그래픽 관련 솔루션 회사들은 각자 의 매체를 지원하기 위한 라이브러리를 제공할 수 있다.

#### 공통 API

WIPI 2.0 에서 VGI에 관한 하나의 표준 API를 정하기 위해서, 디지탈아리아의 Mobile Flash Open API 및 네오엠텔의 SIS3 API를 기반으로 하여 필요한 부분을 공 통 API로 정한다.

#### Naming 법칙

WIPI 2.0의 VGI 공통 API는 함수의 경우 `MC_vgiXXX` 와 구조체의 경우 `MC_VgiXXX` 형태 prefix를 가지도록 정의한다.

## 2.2. VGI 재생기의 동작

Vector Graphic Image에 대해서 처리를 해주는 재생기와 관련된 함수 패키지 이다 파일 또는 메모리에 저장된 VGI컨텐트 데이터는 VGI Instance로 추상화되어 VGI재 생기에서 수행한다. .

#### VGI Application Context 생성/소멸

VGI인터페이스 함수를 사용하기 위해서는 먼저 MC_vgiInitialize함수를 통해 Application Context를 생성하여야 한다. 한 어플리케이션은 한 개의 Application Context만 가질 수 있으며 MC_vgiFinalize함수를 호출할 때 까지 유효하다.

#### VGI Instance 생성/소멸

VGI컨텐트를 재생하기 위해서는 MC_vgiCreateInstance함수로 VGI인스턴스를 생성 하여야 한다. VGI인스턴스 생성시 VGI Application Context를 인수로 사용한다. 이후 사용되는 재생제어 함수들은 VGI인스턴스를 첫번째 인수로 하여 호출된다. 하나의 Application Context에 대해서, VGI 인스턴스는 여러 개를 생성하여 재생할 수 있으나, 메모리 사용량은 커진다.

#### 콜백 함수와 상태 이벤트

VGI컨텐트의 재생 종료와 재생시 발생하는 에러, 재생시 컨텐트에 의해 행해지는 고 유동작들은 MC_vgiCreateInstance시 등록한 콜백함수 또는 이벤트를 이용하여 어플 리케이션으로 전달된다.

#### VGI 관련 재생 영역 정의

VGI컨텐트의 재생 시 관련되는 영역의 정의는 다음 그림과 같다. 먼저 `MC_vgiInitialize` 함수를 통해 정의되는 영역은 그림의 “application” 영역에 해당하며, 이는 application LCD전체 영역과 동일할 수 있으나, 일부분을 사용할 경우를 위하여 정의 된다. 또한 `MC_vgiPlay` 함수에 의해 정의되는 영역은 실제 content가 재생될 크기를 지정하는데 사용된다. 마지막으로 MC_vgiSetViewport에 의해서 정의되는 영 역은 application영역 중 실제 화면이 display되어질 cliping영역을 설정하는데 사용된 다. 일례로 그림에서와 같이 영역이 설정되어 있다면, 실제 화면은 파란색 테두리의 영역에만 VGI컨텐츠가 재생된다. 한편 MC_vgiSetViewPosition은 VGI 컨텐츠를 재생 하는 도중 재생위치를 변경하고 싶을 때, 즉 (x, y)의 position을 바꾸는데 사용될 수 있다. 이와 같은 영역의 정의에 따라, 각 VGI 라이브러리 제공사에 의해 아래와 같 은 재생영역 설정이될 수 있도록 영역설정과 관련되 함수들의 사용법이 제공될 수 있다. [그림 2-2-1 재생 영역 설정 예]

## 2.3. VGI 메시지 및 타입 정의문

### MC_VGI_ZOOMIN

**프로토타입**

```c
#define MC_VGI_ZOOMIN 0
```

**설명**

`MC_vgiZoom` 함수에서 사용하는 상수. 컨텐츠를 ZOOMIN하여 디스플레이 하고자 할 때 사용한다.

### MC_VGI_ZOOMOUT

**프로토타입**

```c
#define MC_VGI_ZOOMOUT 1
```

**설명**

`MC_vgiZoom` 함수에서 사용하는 상수. 컨텐츠를 ZOOMOUT하여 디스플레이 하고자 할 때 사용한다.

### MC_VGI_ZOOM100

**프로토타입**

```c
#define MC_VGI_ZOOM100 2
```

**설명**

`MC_vgiZoom` 함수에서 사용하는 상수. 컨텐츠를 원래 비율대로 디스플레이 하고자 할 때 사용한다.

### MC_VGI_PANLEFT

**프로토타입**

```c
#define MC_VGI_PANLEFT 0
```

**설명**

`MC_vgiPan` 함수에서 사용하는 상수.

### MC_VGI_PANRIGHT

**프로토타입**

```c
#define MC_VGI_PANRIGHT 1
```

**설명**

`MC_vgiPan` 함수에서 사용하는 상수

### MC_VGI_PANUP

**프로토타입**

```c
#define MC_VGI_PANUP 2
```

**설명**

`MC_vgiPan` 함수에서 사용하는 상수

### MC_VGI_PANDOWN

**프로토타입**

```c
#define MC_VGI_PANDOWN 3
```

**설명**

`MC_vgiPan` 함수에서 사용하는 상수

### MC_VGI_EVENT

**프로토타입**

```c
#define MC_VGI_EVENT MV_VGI_EVENT
```

**설명**

콜백함수에서 사용하는 메시지.

### MC_VGI_NOTIFY

**프로토타입**

```c
#define MC_VGI_NOTIFY MV_VGI_NOTIFY
```

**설명**

상태처리

### MC_VgiAppContext

**프로토타입**

```c
typedef void* MC_VgiAppContext
```

**설명**

VGI 인터페이스 사용을 위한 어플리케이션 컨텍스트

### MC_VgiInstance

**프로토타입**

```c
typedef void* MC_VgiInstance
```

**설명**

VGI 인스턴스 핸들

### MC_VGIEvent

**프로토타입**

```c
typedef struct _MC_VGIEvent{ M_Int32 notify; M_Char* nData;}
MC_VGIEvent;
```

**설명**

`MC_vgiCreateInstance` 호출시 cbevent_enable 인수를 TRUE로 설정하면 재생기의 상 태변화를 MV_VGI_EVENT , MV_VGI_NOTIFY 이벤트로 어플리케이션으로 전달해 준다. EVENT의 첫번째 파라메터는 `MC_VgiInstance` 이며 두번째 파라메터는 MC_VGIEvent형 의 구조체 포인터를 전달한다. (*`MC_VgiCallback`) 콜백함수와 같은 기능을 하므로, 이벤트를 사용할지, 콜백함수를 사용할지는, 용도에 맞게 선택적으로 사용하면 된다. `MC_grpPostEvent`( `MC_knlGetCurProgramID()`, MV_VGI_EVENT, `MC_VgiInstance` hVgi, `MC_VGIEvent`* pVgiEvent) 인자 이벤트 설명 notify nData VGI 컨텐트 재생시 `M_E_NOMEMORY` x 메모리 부족 VGI 컨텐트 포멧이 `M_E_INVALID` x 잘못되었음 MV_VGI_EVEN 다른 이유로 에러 T `M_E_ERROR` x 발생 VGI 컨텐트의 재생 `MC_VGI_PLAYEND` x 이 정상종료 되었 을 때 발생 VGI 컨텐트에서 MV_VGI_NOTIF phone 번호로 전 `MC_VGI_CALL` `M_Char`* phone Y 화를 걸었음을 알 려줌 VGI 컨텐트에서 phone 번호로 메 `MC_VGI_SMS` `M_Char`* phone 시지를 보냈음을 알려줌 VGI 컨텐트에서 url 로 브라우저를 `MC_VGI_URL` `M_Char`* url 이용하여 이동하도 록 전달하였음을 알려줌 VGI 컨텐트의 각 `MC_VGI_TICK` x 프레임이 렌더링 된 후 발생

## 2.4. C API

### MC_VgiCallback

**프로토타입**

```c
typedef void (*MC_vgiCallback)( MC_VgiInstance hVgi,
M_Int32 type,M_Int32 param1,M_Int32 param2 )
```

**설명**

VGI라이브러리의 상태가 변경될 때 불려지는 콜백함수. `MC_VGIEvent` 이벤트와 같은 기능을 하므로, 이벤트를 사용할지, 콜백함수를 사용할 지는, 용도에 따라서 선택적으로 사용하면 된다.

**매개 변수**

- `hVgi` - VGI 인스턴스
- `type` - 메시지 종류 (MV_VGI_EVENT 또는 MV_VGI_NOTIFY) param1 param2 인자
- `type` - 설명
- `Param1` - Param2
- `VGI` - 컨텐트 재생시
- `M_E_NOMEMORY` - x 메모리 부족
- `VGI` - 컨텐트 포멧이
- `M_E_INVALID` - x 잘못되었음 `MC_VGI_EVEN` 다른 이유로 에러 T
- `M_E_ERROR` - x 발생
- `VGI` - 컨텐트의 재생
- `MC_VGI_PLAYEND` - x 이 정상종료 되었 을 때 발생
- `VGI` - 컨텐트에서
- `MC_VGI_NOTIF` - phone 번호로 전
- `MC_VGI_CALL` - `M_Char`* phone
- `Y` - 화를 걸었음을 알 려줌
- `VGI` - 컨텐트에서
- `phone` - 번호로 메
- `MC_VGI_SMS` - `M_Char`* phone 시지를 보냈음을 알려줌
- `VGI` - 컨텐트에서
- `url` - 로 브라우저를
- `MC_VGI_URL` - `M_Char`* url 이용하여 이동하도 록 알려줌
- `VGI` - 컨텐트의 각
- `MC_VGI_TICK` - x 프레임이 렌더링 된 후 발생

**부작용**

없음

**참고 항목**

`MC_vgiCreateInstance`, `MC_vgiCreateInstanceByFile`

### MC_vgiGetContentInfoByFile

**프로토타입**

```c
M_Int32 MC_vgiGetContentInfoByFile(M_Int32 fd, M_Byte* command,
M_Byte* rtnBuf, M_Int32 bufsize )
```

**설명**

컨텐츠의 정보를 파일에서 직접 읽어온다. 반환할 값이 정수일 때는 10진수 문자열 로 변환하여 버퍼를 통하여 반환한다. 컨텐츠가 어떤 타입인지를 단순하게 알려면, 파일의 시그니처를 직접 이용하는 것도 하나의 방법이다.

**매개 변수**

- `fd` - [in] 파일 식별자
- `command` - [in] 읽어오고자 하는 정보의 키 값 Command 비고 “TYPE” 컨텐츠가 어떤 형태인지 구별하여 반환한다. VIS의 경우 “VIS” 반환, Mobile Flash의 경우 “DMF” 반환 “WIDTH” 가로 “HEIGHT” 세로 “VERSION” 버전 “TOTAL_FRAME” 전체 프레임수
- `rtnBuf` - [out] 반환 정보가 반환되는 버퍼
- `bufSize` - [in] 반환값이 저장될 버퍼 크기

**반환 값**

성공

실패

- `M_E_SHORTBUF` - 반환되는 문자열보다 전달한 버퍼크기가 작을 때 발생
- `M_E_INVALID` - 전달한 매개 변수가 잘못되었음

**부작용**

없음

**참고 항목**

`MC_vgiGetContentInfo`

### MC_vgiGetContentInfo

**프로토타입**

```c
M_Int32 MC_vgiGetContentInfo (MC_VgiInstance hVgi, M_Byte* command,
M_Byte* rtnBuf, M_Int32 bufsize )
```

**설명**

컨텐츠의 정보를 읽어온다. 반환할 값이 정수일 때는 10진수 문자열로 변환하여 버 퍼를 통하여 반환한다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `command` - [in] 읽어오고자 하는 정보의 키 값 command 비고 “TYPE” 컨텐츠가 어떤 형태인지 구별하여 반환한다. VIS의 경우 “VIS” 반환, Mobile Flash의 경우 “DMF” 반환 “WIDTH” 가로. 단위는 PIXEL임 “HEIGHT” 세로. 단위는 PIXEL임 “VERSION” 버전 “TOTAL_FRAME” 전체 프레임수
- `rtnBuf` - [out] 반환 정보가 반환되는 버퍼
- `bufSize` - [in] 반환값이 저장될 버퍼 크기

**반환 값**

성공

실패

- `M_E_SHORTBUF` - 반환되는 문자열보다 전달한 버퍼크기가 작을 때 발생
- `M_E_INVALID` - 전달한 매개 변수가 잘못되었음

**부작용**

없음

**참고 항목**

없음

### MC_vgiSetContentInfo

**프로토타입**

```c
M_Int32 MC_vgiSetContentInfo (MC_VgiInstance hVgi, M_Byte* command,
void* value )
```

**설명**

컨텐츠의 다양한 정보를 메모리상에서 변경시킨다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `command` - [in] 변경하고자 하는 정보명
- `value` - [in] cmd에 해당하는 정보값을 나타내는 문자열 Command Value “LOOP” “ON” 이면 컨텐츠를 반복해서 재생한다. “OFF” 이면 컨텐츠를 1번 재생한다. 이외의 command는 업체별로 상이하다.

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

없음

### MC_vgiInitialize

**프로토타입**

```c
MC_VgiAppContext MC_vgiInitialize ( M_Int32 x, M_Int32 y,M_Int32 width,
M_Int32 height)
```

**설명**

응용프로그램 컨텍스트를 생성한다. 지정 영역은 VGI application의 LCD display영 역을 의미한다.

**매개 변수**

- `x` - [in] VGI Application 이 사용할 디스플레이 영역의 x 시작점
- `y` - [in] VGI Application 이 사용할 디스플레이 영역의 y 시작점
- `width` - [in] VGI Application 이 사용할 디스플레이 영역의 width
- `height` - [in] VGI Application 이 사용할 디스플레이 영역의 height

**반환 값**

성공

생성된 VGI 응용프로그램 컨텍스트
실패


**부작용**

MC_vgiPlay에서 사용하는 x, y, width, height와 값과는 의미가 다르다.

**참고 항목**

`MC_vgiPlay`

### MC_vgiFinalize

**프로토타입**

```c
M_Int32 MC_vgiFinalize (MC_VgiAppContext VgiAc)
```

**설명**

생성된 VGI 응용프로그램 컨텍스트를 해제한다.

**매개 변수**

- `VgiAc` - [in] 응용프로그램 컨텍스트

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

없음

### MC_vgiCreateInstance

**프로토타입**

```c
MC_VgiInstance MC_vgiCreateInstance( MC_VgiAppContext VgiAc,
M_Byte* buf,M_int32 bufsize, MC_vgiCallback cbproc,
M_Boolean cbevent_enable, void* extra );
```

**설명**

메모리에 저장된 컨텐트 데이터로부터 VGI 인스턴스를 생성한다.

**매개 변수**

- `VgiAc` - [in] 응용프로그램 컨텍스트
- `buf` - [in] 컨텐트 데이터가 저장된 메모리 포인터
- `bufsize` - [in] 컨텐트 데이터가 저장된 크기
- `cbevent_enable` - [in] 재생상태의 변화를 이벤트로 받으려면 `TRUE`, 그렇지 않으면 `FALSE`
- `extra` - [in] 추가적인 정보를 주어 세밀한 제어를 할 경우 사용한 다. 업체별로 상이. [예제] “loop=1” 컨텐트를 무한 반복 재생하는 경우 “loop=0” 컨텐트를 1회만 반복 하는 경우 “bksound_off=1” 컨텐트의 배경사운드를 재생하지 않는 경우 “bksound_off=0” 컨텐트의 배경사운드를 재생하는 경우 “mem_limit=400” 메모리 제한 값이 400KB일 경우의 예제이다. 생성되는 VGI 인스턴스는 이 메모리 제한 값 내에서 컨텐트를 재생한다 “performance=300” CPU 사용 시간 제한 값. 밀리세컨드 단위로 CPU 사용 량을 지정한다. VGI 디코더는 이 시간 간격 마다 다른 태스크를 위하여 CPU 점유를 놓는다

**반환 값**

성공

생성된 VGI 인스턴스
실패


**부작용**

없음

**참고 항목**

`MC_VGIEvent`, `MC_vgiCreateInstanceByFile`

### MC_vgiCreateInstanceByFile

**프로토타입**

```c
MC_VgiInstance MC_vgiCreateInstanceByFile( MC_VgiAppContext VgiAc,
M_Byte* filename, M_Int32 aMode, MC_vgiCallback cbproc,
M_Boolean cbevent_enable void* extra);
```

**설명**

컨텐트 파일로부터 VGI 인스턴스를 생성한다.

**매개 변수**

- `VgiAc` - [in] 응용프로그램 컨텍스트
- `filename` - [in] 컨텐트의 파일 경로/이름 aMode `MC_DIR_PRIVATE_ACCESS` private 디렉토리에 접근 `MC_DIR_SHARED_ACCESS` shared 디렉토리에 접근 `MC_DIR_SYSTEM_ACCESS` system 디렉토리에 접근
- `cbproc` - [in] 재생이 종료되었을 때나 에러가 발생하여 재생이 중지 되었을 때 호출되는 콜백함수를 등록한다. NULL을 등 록 하는 경우 콜백함수를 사용하지 않는다.
- `cbevent_enable` - [in] 재생상태의 변화를 이벤트로 받으려면 `TRUE`, 그렇지 않으면 `FALSE`
- `extra` - [in] 추가적인 정보를 주어 세밀한 제어를 할 경우 사용한 다. 업체별로 상이. [예제] “loop=1” 컨텐트를 무한 반복 재생하는 경우 “loop=0” 컨텐트를 1회만 반복 하는 경우 “bksound_off=1” 컨텐트의 배경사운드를 재생하지 않는 경우 “bksound_off=0” 컨텐트의 배경사운드를 재생하는 경우 “mem_limit=400” 메모리 제한 값이 400KB일 경우의 예제이다. `생성되 는 VGI 인스턴스는 이 메모리 제한 값 내에서 컨텐트를 재생 한다 “performance=300” CPU 사용 시간 제한 값. 밀리세컨드 단위로 CPU 사용 량을 지정한다. VGI 디코더는 이 시간 간격 마다 다른 태스크를 위하여 CPU 점유를 놓는다

**반환 값**

성공

생성된 VGI 인스턴스
실패


**부작용**

없음

**참고 항목**

`MC_VGIEvent`, `MC_vgiCreateInstance`

### MC_vgiPlay

**프로토타입**

```c
M_Int32 MC_vgiPlay (MC_VgiInstance hVgi, M_Int32 x, M_Int32 y,
M_Int32 width, M_int32 height)
```

**설명**

컨텐트의 재생을 시작한다. 컨텐트를 재생도중 중지시키기 위해서는 `MC_vgiStop` 함 수를 호출한다. 이 함수를 통해 지정되는 영역은 LCD display상에서 컨텐트의 재생 영역을 의미 한다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `x` - [in] VGI 컨텐트를 출력시킬 영역의 x좌표
- `y` - [in] VGI 컨텐트를 출력시킬 영역의 y좌표
- `width` - [in] VGI 컨텐트를 출력시킬 영역의 폭, 0을 지정하면 컨텐트의 기본크기 사용
- `height` - [in] VGI 컨텐트를 출력시킬 영역의 높이, 0을 지정하면 컨텐트의 기본크기 사용

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

MC_vgiInitialize에서 사용하는 x, y, width, height와 의미가 다르다.

**참고 항목**

없음

### MC_vgiStop

**프로토타입**

```c
M_Int32 MC_vgiStop (MC_VgiInstance hVgi)
```

**설명**

`MC_vgiPlay` 함수를 호출하여 컨텐트를 재생시키고 재생이 끝나기 전에 중지 시키고 싶다면 `MC_vgiStop` 함수를 호출한다. 이 함수를 호출하면 재생에 사용된 리소스를 모두 해제한 뒤 콜백함수 또는 이벤트로 컨텐츠가 정지되었음을 알린다.

**매개 변수**

[in][out] hVgi VGI 인스턴스

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

`MC_vgiPlay`

### MC_vgiPause

**프로토타입**

```c
M_Int32 MC_vgiPause (MC_VgiInstance hVgi)
```

**설명**

`MC_vgiPause` 함수를 호출하여 컨텐트의 재생을 일시중지시킬 수 있다. 컨텐트의 재 생을 계속하기 위해서는 `MC_vgiResume` 함수를 호출한다

**매개 변수**

- `hVgi` - [in] VGI 인스턴스

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

`MC_vgiPlay`, `MC_vgiResume`

### MC_vgiResume

**프로토타입**

```c
M_Int32 MC_vgiResume (MC_VgiInstance hVgi)
```

**설명**

`MC_vgiPause` 함수를 호출하여 컨텐트의 재생을 일시적으로 멈춘 경우 `MC_vgiResume` 함수를 호출하여 재생을 계속할 수 있다

**매개 변수**

- `hVgi` - [in] VGI 인스턴스

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

`MC_vgiPause`

### MC_vgiReplay

**프로토타입**

```c
M_Int32 MC_vgiReplay (MC_VgiInstance hVgi)
```

**설명**

`MC_vgiPlay` 함수를 호출하여 컨텐트를 재생하는 도중 MC_vgiReplay함수를 호출하면 컨텐츠를 처음부터 다시 재생하게 된다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

`MC_vgiPlay`

### MC_vgiLoopOn

**프로토타입**

```c
M_Int32 MC_vgiLoopOn (MC_VgiInstance hVgi)
```

**설명**

컨텐트의 반복재생 여부를 결정할 때 사용한다. MC_vgiCreateInstance의 인수로 컨 텐트의 반복재생 여부를 설정하지만 이 함수를 이용하면 컨텐트 재생 중에도, 반복 재생 옵션을 변경할 수 있다. 단 컨텐트 재생이 이미 종료된 상태에서는 사용하지 못한다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

`MC_vgiLoopOff`

### MC_vgiLoopOff

**프로토타입**

```c
M_Int32 MC_vgiLoopOff (MC_VgiInstance hVgi)
```

**설명**

MC_vgiLoopOn함수에 의해 설정된 컨텐트의 반복재생 여부를 해제 할 때 사용한다. MC_vgiCreateInstance의 인수로 컨텐트의 반복재생 여부를 설정하지만 이 함수를 이 용하면 컨텐트 재생 중에 반복재생 옵션을 변경할 수 있다. 단 컨텐트 재생이 이미 종료된 상태에서는 사용하지 못한다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

`MC_vgiLoopOn`

### MC_vgiSoundOn

**프로토타입**

```c
M_Int32 MC_vgiSoundOn (MC_VgiInstance hVgi)
```

**설명**

`MC_vgiSoundOff` 함수를 호출하여 컨텐트의 사운드를 끈 경우에 `MC_vgiSoundOn` 함수 를 호출하여 사운드를 다시 켤 수 있다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패
- `M_E_INVALIDSTATUS` - 사운드를 사용할 수 없는 상태

**부작용**

없음

**참고 항목**

`MC_vgiSoundOff`

### MC_vgiSoundOff

**프로토타입**

```c
M_Int32 MC_vgiSoundOff (MC_VgiInstance hVgi)
```

**설명**

컨텐트의 사운드를 끄기 위해서 `MC_vgiSoundOff` 함수를 호출할 수 있다. 꺼진 사운 드를 다시 켜기 위해서는 `MC_vgiSoundOn` 함수를 호출한다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

`MC_vgiSoundOn`

### MC_vgiSetVolume

**프로토타입**

```c
M_Int32 MC_vgiSetVolume (MC_VgiInstance hVgi, M_Int32 volume)
```

**설명**

MC_vgiPlay를 통해 컨텐트의 MC_vgiSetVolume함수를 통해 재생되고 있는 사운드의 볼륨을 주어진 절대값으로 변경한다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `volume` - [in] 0(최저) ~ 100(최대) 사이의 값으로 설정할 볼륨세기 의 절대값을 입력한다.

**반환 값**

성공

실패

- `M_E_NOTSUP` - 설정기능을 제공하지 않음
- `M_E_ERROR` - 설정실패

**부작용**

없음

**참고 항목**

`MC_vgiGetVolume`

### MC_vgiGetVolume

**프로토타입**

```c
M_Int32 MC_vgiGetVolume (MC_VgiInstance hVgi, M_Int32 volume)
```

**설명**

MC_vgiPlay를 통해 컨텐트의 MC_vgiSetVolume함수를 통해 재생되고 있는 사운드의 볼륨을 반환한다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스

**반환 값**

성공

볼륨 레벨 ( 0 ~ 100 )
실패

- `M_E_NOTSUP` - 해당기능을 제공하지 않음
- `M_E_ERROR` - 설정실패 M_E_ INVALIDSTATUS 사운드를 사용할 수 없는 상태

**부작용**

없음

### MC_vgiZoom

**프로토타입**

```c
M_Int32 MC_vgiZoom (MC_VgiInstance hVgi, M_Int32 mode)
```

**설명**

MC_vgiPlay를 통해 컨텐츠가 재생시 `MC_vgiZoomIn` 함수의 호출될 때 마다 확대/축소 가 진행된다. 원래의 크기로 돌아갈 수도 있다. 최대 확대 비율은 3배이다. 비율은 100%, 200%, 300% 즉 2,3배씩 단계적으로 일어난다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `mode` - [in] `MC_VGI_ZOOMIN` ZOOMIN `MC_VGI_ZOOMOUT` ZOOMOUT `MC_VGI_ZOOM100` ZOOM100, 원래의 크기

**반환 값**

성공

실패

- `M_E_NOTSUP` - 설정기능을 제공하지 않음
- `M_E_ERROR` - 설정실패

**부작용**

없음

**참고 항목**

`MC_vgiPan`

### MC_vgiPan

**프로토타입**

```c
M_Int32 MC_vgiPan (MC_VgiInstance hVgi, M_Int32 mode )
```

**설명**

MC_vgiPlay를 통해 컨텐츠가 재생시 `MC_vgiZoomIn`,함수의 호출에 의해 확대된 상태 의 재생 시 MC_vgiPan함수를 호출하여 재생되는 화면을 상하좌우로 panning 시킬 수 있다. 이 함수의 반복적인 호출을 통해 컨텐츠의 경계에 이를 때 까지 계속 panning 을 반복할 수 있다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `mode` - [in] `MC_VGI_PANLEFT` PANLEFT `MC_VGI_PANRIGHT` PANRIGHT `MC_VGI_PANUP` PANUP `MC_VGI_PANDOWN` PANDOWN

**반환 값**

성공

실패

- `M_E_NOTSUP` - 설정기능을 제공하지 않음
- `M_E_ERROR` - 설정실패

**부작용**

없음

**참고 항목**

`MC_vgiZoom`

### MC_vgiHandleKeyEvent

**프로토타입**

```c
M_Int32 MC_vgiHandleKeyEvent (MC_VgiInstance hVgi, M_Int32 eventcode, M_Int32 keycode)
```

**설명**

사용자로부터 키 입력이 발생되고 그 키가 단말기가 특별하게 처리해야 하는 키 값 이 아니라면 VGI 디코더에게 그 키 값이 전달되어야 한다. 키 값을 전달하기 위해서 `MC_vgiHandleKeyEvent` 함수를 호출한다. 전달되는 인자는 이벤트 코드 값으로 MV_KEY_PRESS_EVENT, MV_KEY_RELEASE_EVENT, MV_KEY_REPEAT_EVENT를 사용하고, 키 코드 값으로는 MH_keyCode에 있는 KEY 코드를 사용한다

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `eventcode` - [in] 입력된 이벤트 코드
- `keycode` - [in] 입력된 키 코드

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

없음

### MC_vgiSetViewPosition

**프로토타입**

```c
M_Int32 MC_vgiSetViewPosition (MC_VgiInstance hVgi, M_Int32 x,
M_Int32 y)
```

**설명**

컨텐츠의 표시위치를 설정한다. 이 함수는 VGI 인스턴스 생성 후에는 컨텐트 재생 중 아무때나 사용하여 표시위치를 변경할 수 있다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `x` - [in] VGI 컨텐트를 출력시킬 영역의 x좌표
- `y` - [in] VGI 컨텐트를 출력시킬 영역의 y좌표

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

`MC_vgiPlay`, `MC_vgiRedraw`, `MC_vgiSetViewport`

### MC_vgiRedraw

**프로토타입**

```c
M_Int32 MC_vgiRedraw (MC_VgiInstance hVgi,M_Int32 x,M_Int32 y,
M_Int32 width, M_Int32 height )
```

**설명**

재생중인 컨텐트를 redraw해야 할 필요가 있을 때 사용한다. Redraw되는 영역은 입 력되는 인수에 의해 정해지는 영역이다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `x` - [in] redraw할 영역의 x 시작점
- `y` - [in] redraw할 영역의 y 시작점
- `width` - [in] redraw할 영역의 폭
- `height` - [in] redraw할 영역의 높이

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

`MC_vgiPlay`

### MC_vgiSetViewport

**프로토타입**

```c
M_Int32 MC_vgiSetViewport (MC_VgiInstance hVgi,M_Int32 x,M_Int32 y,
M_Int32 width,M_Int32 height )
```

**설명**

클리핑 사각형 영역을 지정한다. 컨텐트는 클리핑 영역 밖에는 그려지지 않는다. 사 각형의 시작점은 (x, y) 에서 시작하며, 폭은 width이며, 높이는 height가 된다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `x` - [in] 클리핑 영역의 x 시작점
- `y` - [in] 클리핑 영역의 y 시작점
- `wight` - [in] 클리핑 영역의 폭
- `height` - [in] 클리핑 영역의 높이

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

없음 `MC_vgiGetFrameOne`[디지털아리아]

**프로토타입**

```c
M_Int32 MC_vgiGetFrameOne (MC_VgiInstance hVgi,
MC_GrpFrameBuffer fb, M_Int32 sx,M_Int32 sy, M_Int32 frame_number )
```

**설명**

특정한 위치에 있는 1개의 프레임만 디코딩 해서, 프레임 버퍼에 저장한다. 타이머 를 호출하지 않고, 직접적으로 특정위치 프레임의 내용을 버퍼에 저장하고자 할 때 사용한다. 디코딩할 프레임 이미지의 sx, sy 부터 프레임버퍼의 가로 / 세로 크기만 큼 디코딩 한다. 디코딩할 프레임 이미지의 크기가 더 크다면, 프레임버퍼의 크기만 큼만 디코딩 하고, 프레임버퍼의 크기가 더 크다면, 프레임 이미지 크기만큼 디코딩 한다. 인수로 전달되는 `MC_VgiInstance` 타입의 instance는 MC_vgiCreateInstance를 새로 호출하여 할당을 한후 사용을 해야 한다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `fb` - [out] 프레임 버퍼
- `sx` - [in] 프레임 영역의 x축 좌표
- `sy` - [in] 프레임 영역의 y축 높이
- `frame_number` - [in] 얻고자 하는 프레임 번호

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

없음 `MC_vgiGetFrameOne`[네오엠텔]

**프로토타입**

```c
M_Int32 MC_vgiGetFrameOne (MC_VgiInstance hVgi,M_Byte* buf,
M_Int32 width,M_Int32 height,M_Int32 frame_number )
```

**설명**

특정한 위치에 있는 1개의 프레임만 디코딩 해서, 버퍼에 저장한다. 타이머를 호출 하지 않고, 직접적으로 특정위치 프레임의 내용을 버퍼에 저장하고자 할 때 사용한 다. 인수로 전달되는 `MC_VgiInstance` 타입의 instance는 MC_vgiCreateInstance를 새 로 호출하여 할당을 한후 사용을 해야 한다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `buf` - [out] 프레임 버퍼
- `width` - [in] 프레임 버퍼의 넓이
- `height` - [in] 프레임 버퍼의 높이
- `frame_number` - [in] 얻고자 하는 프레임 번호

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

없음

### MC_vgiGetFrameMulti

**프로토타입**

```c
M_Int32 MC_vgiGetFrameMulti( C_VgiInstance hVgi,M_Byte* buf,
M_Int32 width,M_Int32 height,M_Int32 frame_number,M_Int32 next_frame)
```

**설명**

특정한 위치에 있는 여러 개의 프레임만 디코딩 해서, 버퍼에 저장한다. 타이머를 호출하지 않고, 직접적으로 특정위치 프레임의 내용을 버퍼에 저장하고자 할 때 사 용한다. 인수로 전달되는 `MC_VgiInstance` 타입의 instance는 `MC_vgiCreateInstance` 를 새로 호출하여 할당을 한후 사용을 해야 한다.

**매개 변수**

- `hVgi` - [in] VGI 인스턴스
- `buf` - [out] 프레임 버퍼
- `width` - [in] 프레임 버퍼의 넓이
- `height` - [in] 프레임 버퍼의 높이
- `frame_number` - [in] 얻고자 하는 프레임 번호
- `next_frame` - [in] 다음 프레임을 계속 얻고자, `MC_vgiGetFrameMulti`()를 계속 호출해야 할 때는 1로, 아닐 경우는 0으로 한다.

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패

**부작용**

없음

**참고 항목**

`MC_vgiGetFrameOne`

## 2.5. Java API (org.kwis.msp.vgi)

Interface VgiEventListener public interface VgiEventListner VGI라이브러리의 상태가 변경을 알려주는 인터페이스이다. 필드 상세 설명

#### VGI_NOMEMORY

public static final int VGI_NOMEMORY VGI 컨텐트 재생시 메모리 부족을 알리는 상수

#### VGI_INVALID

public static final int VGI _INVALID VGI 컨텐트 포멧이 잘못되었음을 알리는 상수.

#### VGI_ERROR

public static final int VGI _ERROR 다른 이유로 에러발생을 알리는 상수.

#### VGI_PLAYEND

public static final int VGI_PLAYEND VGI 컨텐트의 재생이 정상종료 되었을 때 발생을 알리는 상수.

#### VGI_STARTED

public static final int VGI_STARTED VGI 컨텐트의 재생의 시작을 알리는 상수.

#### VGI_STOPPED

public static final int VGI_STOPPED VGI 컨텐트의 재생의 멈춤을 알리는 상수.

#### VGI_PAUSED

public static final int VGI_PAUSED VGI 컨텐트의 재생의 일시 정지를 알리는 상수

#### VGI_RESUMED

public static final int VGI_RESUMED VGI 컨텐트의 일시 정지된 재생을 재게하는 것을 알리는 상수

#### VGI_REPLAYED

public static final int VGI_REPLAYED VGI 컨텐트의 처음부터 다시 재생을 알리는 상수

#### VGI_CALL

public static final int VGI_CALL VGI 컨텐트에서 phone 번호로 전화를 걸었음을 알리는 상수

#### VGI_SMS

public static final int VGI_SMS VGI 컨텐트에서 phone 번호로 메시지를 보냈음을 알리는 상수

#### VGI_URL

public static final int VGI_URL VGI 컨텐트에서 url 로 브라우저를 이용하여 이동하도록 알리는 상수

#### VGI_TICK

public static final int VGI_TICK VGI 컨텐트의 각 프레임이 렌더링 되었음을 알리는 상수 메쏘드 상세설명

#### notifyVgiEvent

public void notifyVgiEvent(VgiClip clip, int event, char[] param) vgi 클립 재생 시 상태가 변할 때 불리는 메쏘드이다.

**매개 변수**

- `Clip` - 상태변화가 일어난 클립
- `event` - 상태값
- `param` - 각 event에 추가 전달 값이 있을 경우 사용
- `event` - param 설명
- `VGI` - 컨텐트에서 phone 번호로 전화를 걸
- `VGI_CALL` - char[] phone 었음을 알려줌
- `VGI` - 컨텐트에서 phone 번호로 메시지를
- `VGI_SMS` - char[] phone 보냈음을 알려줌
- `VGI` - 컨텐트에서 url 로 브라우저를 이용하
- `VGI_URL` - char[] url 여 이동하도록 알려줌

**참고 항목**

VgiClip.VgiClip(VgiBaseClip vBaseClip, byte[] buf, int bufsize, Boolean loop, Boolean bksound_off, VgiEventListener cbproc, Boolean cbevent_enable, byte[] extra), VgiClip.setListener(VgiClip hVgi, vgiEventListener listener) Class VgiBaseClip java.lang.Object | +--org.kwis.msp.vgi.VgiBaseClip public class VgiBaseClip extends java.lang.Object 미디어 디바이스를 구현하기 위한 최상위 클래스이다. Methods inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 필드 상세 설명 생성자 상세설명

#### VgiBaseClip

public VgiBaseClip(int x, int y, int width, int height)

**매개 변수**

- `x` - VGI Application 이 사용할 디스플레이 영역의 x 시작점
- `y` - VGI Application 이 사용할 디스플레이 영역의 y 시작점
- `width` - VGI Application 이 사용할 디스플레이 영역의 width
- `height` - VGI Application 이 사용할 디스플레이 영역의 height
- `VgiClip에서` - 사용하는 x, y, width, height와 값과는 의미가 다르다. 메쏘드 상세설명
- `Class` - VgiClip java.lang.Object | +--org.kwis.msp.vgi.VgiClip
- `public` - class VgiClip extends java.lang.Object 이 클래스는 VgiPlayer에 의해 재생되는 클립을 구현한다.
- `Methods` - inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 필드 상세 설명 생성자 상세설명 VgiClip
- `public` - VgiClip(VgiBaseClip vBaseClip, byte[] buf, int bufsize,
- `VgiEventListener` - cbproc, Boolean cbevent_enable, byte[] extra )

**매개 변수**

- `vBaseClip` - vgi base 클립
- `buf` - 컨텐트 데이터가 저장된 메모리 포인터
- `bufsize` - 컨텐트 데이터가 저장된 크기
- `cbproc` - 재생이 종료되었을 때나 에러가 발생하여 재생이 중지되었을 때 호출되는 콜백함수를 등록한다. NULL을 등록하는 경우 콜백함수를 사용하지 않는다.
- `cbevent_enable` - 재생상태의 변화를 이벤트로 받으려면 `TRUE`, 그렇지 않으면 `FALSE`
- `extra` - 추가적인 정보를 주어 세밀한 제어를 할 경우 사용한다. 업체별로 상이 [예제] “loop=1” 컨텐트를 무한 반복 재생하는 경우 “loop=0” 컨텐트를 1회만 반복 하는 경우 “bksound_off=1” 컨텐트의 배경사운드를 재생하지 않는 경우 “bksound_off=0” 컨텐트의 배경사운드를 재생하는 경우 “mem_limit=400” 메모리 제한 값. 생성되는 VGI 인스턴스는 이 메모리 제한 값 내에서 컨텐트를 재생한다 “performance=300” CPU 사용 시간 제한 값. 밀리세컨드 단위로 CPU 사용량을 지정한다. VGI 디코더는 이 시간 간격 마다 다른 태스크를 위하여 CPU 점유를 놓는다 VgiClip
- `public` - VgiClip(VgiBaseClip vBaseClip, byte[] filename, int aMode,
- `VgiEventListener` - cbproc, Boolean cbevent_enable, byte[] extra )

**매개 변수**

- `vBaseClip` - vgi Base 클립
- `filename` - 컨텐트의 파일 경로/이름
- `aMode` - `MC_DIR_PRIVATE_ACCESS` private 디렉토리에 접근
- `MC_DIR_SHARED_ACCESS` - shared 디렉토리에 접근
- `MC_DIR_SYSTEM_ACCESS` - system 디렉토리에 접근
- `loop` - 컨텐트를 무한 반복 재생하는 경우 `TRUE`, 그렇지 않은 경우FALSE.
- `bksound_off` - 컨텐트의 배경사운드를 재생하지 않는 경우 `TRUE`, 그렇지 않은 경우 `FALSE`
- `cbproc` - 재생이 종료되었을 때나 에러가 발생하여 재생이 중지되었을 때 호출되는 Listener함수를 등록한다. NULL을 등록하는 경우
- `Listener함수` - 사용하지 않는다.
- `cbevent_enable` - 재생상태의 변화를 이벤트로 받으려면 `TRUE`, 그렇지 않으면 `FALSE`
- `extra` - 추가적인 정보를 주어 세밀한 제어를 할 경우 사용한다. 업체별로 상이 [예제] “loop=1” 컨텐트를 무한 반복 재생하는 경우 “loop=0” 컨텐트를 1회만 반복 하는 경우 “bksound_off=1” 컨텐트의 배경사운드를 재생하지 않는 경우 “bksound_off=0” 컨텐트의 배경사운드를 재생하는 경우 “mem_limit=400” 메모리 제한 값. 생성되는 VGI 인스턴스는 이 메모리 제한 값 내에서 컨텐트를 재생한다 “performance=300” CPU 사용 시간 제한 값. 밀리세컨드 단위로 CPU 사용량을 지정한다. VGI 디코더는 이 시간 간격 마다 다른 태스크를 위하여 CPU 점유를 놓는다 메쏘드 상세설명
- `Class` - VgiPlayer java.lang.Object | +--org.kwis.msp.vgi.VgiPlayer
- `public` - class VgiPlayer extends java.lang.Object 이 클래스는 vgi 미디어를 재생하기 위한 메쏘드를 포함하는 클래스이다.
- `Methods` - inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 필드 상세 설명 E_SHORTBUF
- `public` - static final int E_SHORTBUF
- `command` - 에 따라 리턴 될 데이터의 버퍼가 작을 때 를 표시하는 error 상수 E_INVALID
- `public` - static final int E_INVALID
- `command` - 가 잘못 되었을때를 표시하는 error 상수 E_NOTSUP
- `public` - static final int E_NOTSUP 함수를 지원하지 않을 때 표시하는 error 상수 E_ERROR
- `public` - static final int E_ERROR
- `error` - 상수 VGI_ZOOMIN
- `public` - static final int VGI_ZOOMIN
- `vgiZoom` - 상수. 컨텐츠를 ZOOMIN하여 디스플레이 하고자 할 때 사용한다. VGI_ZOOMOUT
- `public` - static final int VGI_ZOOMOUT
- `vgiZoom` - 상수. 컨텐츠를 ZOOMOUT하여 디스플레이 하고자 할 때 사용한다. VGI_ZOOM100
- `public` - static final int VGI_ZOOM100
- `vgiZoom` - 상수. 컨텐츠를 원래 비율대로 디스플레이 하고자 할 때 사용한다. VGI_PANLEFT
- `public` - static final int VGI_PANLEFT
- `vgiPan` - 상수 VGI_PANRIGHT
- `public` - static final int VGI_PANRIGHT
- `vgiPan` - 상수 VGI_PANUP
- `public` - static final int VGI_PANUP
- `vgiPan` - 상수 VGI_PANDOWN
- `public` - static final int VGI_PANDOWN
- `vgiPan` - 상수 생성자 상세설명 메쏘드 상세설명 notifyEvent
- `public` - boolean notifyEvent(VgiClip hVgi, int event, char[] param) 클립 재생시 상태변화를 알린다. 전달되는 이벤트는 VgiEventListener.notifyVgiEvent()와 같다.

**매개 변수**

- `hVgi` - vgi 클립
- `event` - 상태값
- `param` - 각 event에 추가 전달값이 있을 경우 사용 setListener
- `public` - int setListener(VgiClip hVgi, VgiEventListener listener) 클립 재생시 상태변화를 알려줄 listener를 등록한다.

**매개 변수**

- `hVgi` - vgi 클립
- `listener` - 새로운 listener, 만일 null 이면 기존 것을 제거함

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 getContentInfo public int getContentInfo(VgiClip hVgi, byte[] command, byte[] rtnBuf, int bufsize) 컨텐츠의 정보를 읽어온다. 반환할 값이 정수일 때는 10진수 문자열로 변환하여 버퍼를 통하여 반환한다.

**매개 변수**

- `hVgi` - vgi 클립
- `command` - [in] 읽어오고자 하는 정보의 키 값 command 비고 “TYPE” 컨텐츠가 어떤 형태인지 구별하여 반환한다. VIS의 경우 “VIS” 반환, Mobile Flash의 경우 “DMF” 반환 “WIDTH” 가로 “HEIGHT” 세로 “VERSION” 버전 “TOTAL_FRAME” 전체 프레임수
- `rtnBuf` - [out] 반환 정보가 반환되는 버퍼
- `bufSize` - [in] 반환값이 저장될 버퍼 크기

**반환 값**

성공

실패

E_SHORTBUF 반환되는 문자열보다 전달한 버퍼크기가 작을 때 발생 E_INVALID 전달한 매개 변수가 잘못되었음 SetContentInfo public int SetContentInfo (VgiClip hVgi, byte[] command, byte[] value) PLAY되고 있는 컨텐츠의 다양한 정보를 메모리상에서 변경시킨다.

**매개 변수**

- `hVgi` - vgi 클립
- `command` - [in] 변경하고자 하는 정보명
- `value` - [in] cmd에 해당하는 정보값을 나타내는 문자열 Command Value “LOOP” “ON” 이면 컨텐츠를 반복해서 재생한다. “OFF” 이면 컨텐츠를 1번 재생한다.

**반환 값**

성공

실패

E_SHORTBUF 반환되는 문자열보다 전달한 버퍼크기가 작을 때 발생 E_INVALID 전달한 매개 변수가 잘못되었음 play public int play(VgiClip hVgi, int x, int y, int width, int height) 클립의 데이타를 재생한다. 이 함수가 불려 매체처리를 시작하면 클립에 등록된 이벤트 listener함수에 START상태가 전달된다. 재생중인 클립으로 다시 재생할려고 하면 이 함 수는 아무런 역할도 하지 않는다. Play가 종료되면, 이벤트 listener함수에 VGI_PLAYEND 상태가 전달된다.

**매개 변수**

- `hVgi` - 재생할 클립
- `repeat` - false이면 1회재생, true는 반복 재생

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 stop public int stop(VgiClip hvgi) 매체재생을 종료한다. 이 함수가 불려 매체처리를 종료하면 클립에 등록한 이벤트 listener함수에 STOP상태가 전달된다. 정지되어 있는 처리기에 대해서 이 함수를 다시 부르면, 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `hvgi` - 종료시킬 클립

**반환 값**

성공

실패

- `M_E_NOTSUP` - 기능을 제공하지 않음
- `M_E_ERROR` - 실패 pause public int pause(VgiClip hvgi) 매체 재생을 일시적으로 멈춘다. 이 함수가 불려 매체처리가 일시 정지하게 되면 클립에 등록한 이벤트 listener함수에 PAUSE 상태가 전달된다. 일시로 멈추어 있거나, 정지되어 있는 처리기에 대해서 이 함수를 다시 부르면, 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `hvgi` - 일시 중지시킬 클립

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 resume public int resume(VgiClip hvgi) 일시 정지한 매체재생을 재개한다. 이 함수가 불려 매체처리를 재개하면 클립에 등록한 이벤트 listener함수에 RESUME상태가 전달된다. 매채처리중인 처리기에 대해서 이 함수 를 다시 부르면 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `hvgi` - 재개시킬 클립

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 replay public int replay(VgiClip hvgi) vgiPlay 메쏘드를 호출하여 컨텐트를 재생하는 도중 vgiReplay메쏘드를 호출하면 컨텐츠 를 처음부터 다시 재생하게 된다.

**매개 변수**

- `hVgi` - vgi 클립

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 loopOn public int loopOn(VgiClip hvgi) 컨텐트의 반복재생 여부를 결정할 때 사용한다. VgiClip 생성시의 인수로 컨텐트의 반복 재생 여부를 설정하지만 이 함수를 이용하면 컨텐트 재생 중에 반복재생 옵션을 변경할 수 있다. 단 컨텐트 재생이 이미 종료된 상태에서는 사용하지 못한다.

**매개 변수**

- `hVgi` - vgi 클립

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 loopOff public int loopOff(VgiClip hvgi) MC_vgiLoopOn함수에 의해 설정된 컨텐트의 반복재생 여부를 해제 할 때 사용한다. MC_vgiCreateInstance의 인수로 컨텐트의 반복재생 여부를 설정하지만 이 함수를 이용 하면 컨텐트 재생 중에 반복재생 옵션을 변경할 수 있다. 단 컨텐트 재생이 이미 종료 된 상태에서는 사용하지 못한다.

**매개 변수**

- `hVgi` - vgi 클립

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 soundOn public int soundOn(VgiClip hVgi) SoundOff 함수를 호출하여 재생되고 있는 컨텐트의 사운드를 끈 경우에 SoundOn 함수 를 호출하여 사운드를 다시 켤 수 있다.

**매개 변수**

- `hVgi` - vgi 클립

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 E_INVALIDSTATUS 사운드를 사용할 수 없는 상태 soundOff public int soundOff(VgiClip hVgi) 컨텐트의 사운드를 끄기 위해서 soundOff 함수를 호출할 수 있다. 꺼진 사운드를 다시 켜기 위해서는 soundOn 함수를 호출한다.

**매개 변수**

- `hVgi` - vgi 클립

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 setVolume public int setVolume(VgiClip hvgi) 컨텐트의 사운드의 볼륨을 변경한다.

**매개 변수**

- `hVgi` - vgi 클립

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 zoom public int zoom(VgiClip hvgi, int mode) play를 통해 컨텐츠가 재생시 zoom 함수의 호출될 때 마다 확대/축소가 진행된다. 원래 의 크기로 돌아갈 수도 있다. 최대 확대 비율은 3 배이고, 최소 축소비율은 100%이다. 비율은 100%, 200%, 300% 즉 2,3배씩 단계적으로 일어난다.

**매개 변수**

- `hVgi` - vgi 클립 mode
- `VGI_ZOOMIN` - ZOOMIN
- `VGI_ZOOMOUT` - ZOOMOUT
- `VGI_ZOOM100` - ZOOM100, 원래의 크기

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 pan public int pan(VgiClip hvgi, int mode) play를 통해 컨텐츠가 재생시 zoom함수의 호출에 의해 확대된 상태의 재생 시 pan함수 를 호출하여 재생되는 화면을 상하좌우로 panning 시킬 수 있다. 이 함수의 반복적인 호 출을 통해 컨텐츠의 경계에 이를 때 까지 계속 panning을 반복할 수 있다.

**매개 변수**

- `hVgi` - vgi 클립 mode
- `VGI_PANLEFT` - PANLEFT
- `VGI_PANRIGHT` - PANRIGHT
- `VGI_PANUP` - PANUP
- `VGI_PANDOWN` - PANDOWN

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 handleKeyEvent public int handleKeyEvent(VgiClip hvgi, int eventcode, int keycode) 사용자로부터 키 입력이 발생되고 그 키가 단말기가 특별하게 처리해야 하는 키 값이 아 니라면 VGI 디코더에게 그 키 값이 전달되어야 한다. 키 값을 전달하기 위해서 handleKeyEvent 함수를 호출한다. 전달되는 인자는 이벤트 코드 값으로 MV_KEY_XXX 를, 키 코드 값으로 MC_KEY_XXX를 사용한다.

**매개 변수**

- `hVgi` - vgi 클립
- `eventcode` - 이벤트 코드
- `keycode` - 입력된 키 코드

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 setViewPosition public void setViewPosition(VgiClip hvgi, int x, int y) 컨텐츠의 표시위치를 설정한다. 이 함수는 VGI 인스턴스 생성 후에는 컨텐트 재생중 아 무때나 사용하여 표시위치를 변경할 수 있다.

**매개 변수**

- `hVgi` - vgi 클립
- `x` - VGI 컨텐트를 출력시킬 영역의 x좌표
- `y` - VGI 컨텐트를 출력시킬 영역의 y좌표

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 reDraw public int reDraw(VgiClip hvgi, int x, int y, int width, int height) 재생중인 컨텐트를 redraw해야 할 필요가 있을 때 사용한다. Redraw되는 영역은 입력되 는 인수에 의해 정해지는 영역이다.

**매개 변수**

- `hVgi` - vgi 클립
- `x` - redraw할 영역의 x 시작점
- `y` - redraw할 영역의 y 시작점
- `width` - redraw할 영역의 폭
- `height` - redraw할 영역의 높이

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 setViewport public int setViewPort(VgiClip hvgi, int x, int y, int width, int height) 클리핑 사각형 영역을 지정한다. 컨텐트는 클리핑 영역 밖에는 그려지지 않는다.

**매개 변수**

- `hVgi` - vgi 클립
- `x` - 클리핑 영역의 x 시작점
- `y` - 클리핑 영역의 y 시작점
- `width` - 클리핑 영역의 폭
- `height` - 클리핑 영역의 높이

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 getFrameOne public int getFrameOne(VgiClip hvgi, byte[] buf, int width, int height, int frame_number) 특정한 위치에 있는 1개의 프레임만 디코딩 해서, 버퍼에 저장한다. 타이머를 호출하지 않고, 직접적으로 특정위치 프레임의 내용을 버퍼에 저장하고자 할 때 사용한다. 인수로 전달되는 VgiClip 타입의 instance는 새로 할당을 한후 사용을 해야 한다.

**매개 변수**

- `hVgi` - vgi 클립
- `buf` - 프레임 버퍼
- `sx` - 프레임 영역의 x축 좌표
- `sy` - 프레임 영역의 y축 좌표
- `frame_number` - 얻고자 하는 프레임 번호

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패 getFrameMulti public int getFrameMulti(VgiClip hvgi, byte[] buf, int width, int height, int frame_number, int next_frame) 특정한 위치에 있는 여러 개의 프레임만 디코딩 해서, 버퍼에 저장한다. 타이머를 호출하 지 않고, 직접적으로 특정위치 프레임의 내용을 버퍼에 저장하고자 할 때 사용한다. 인수 로 전달되는 VgiClip 타입의 instance는 새로 할당을 한후 사용을 해야 한다.

**매개 변수**

- `hVgi` - vgi 클립
- `buf` - 프레임 버퍼
- `width` - 프레임 버퍼의 넓이
- `height` - 프레임 버퍼의 높이
- `frame_number` - 얻고자 하는 프레임 번호
- `next_frame` - 다음 프레임을 계속 얻고자, getFrameMulti()를 계속 호출해야 할 때는 1로, 아닐 경우는 0으로 한다.

**반환 값**

성공

실패

E_NOTSUP 기능을 제공하지 않음 E_ERROR 실패
