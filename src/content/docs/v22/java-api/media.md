---
title: "3.1.7. 매체 처리기"
---

---

## Class BaseClip

```text
java.lang.Object
  +--org.kwis.msp.media.BaseClip
```

```java
public abstract class BaseClip extends java.lang.Object
```

매체 처리기를 구현하기 위한 최상위 추상화 클래스이다.

*Methods inherited from class java.lang.Object: clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 메서드 상세

### allocPlayer

```java
protected int allocPlayer()
```

클립내의 미디어 데이타를 처리하기 위한 플레이어를 할당 받는다. 이 메소드는 클립의 미디어 데이타를 이용하여 재생하는 등의 실질적인 처리를 하기 이전에 반드시 불리워져야만 하는 메소드이다. 만약 이 메소드를 호출 하지 않고, 혹은 이 메소드가 실패 한 후에, play 등의 메소드가 불리워지면 에러값을 반환 받게 된다.

**매개 변수**

없음

**반환 값**

성공하면 0을 반환하고, 실패하면 음수 반환

### freePlayer

```java
protected int freePlayer()
```

allocPlayer() 메소드를 이용해서 할당 받았던 플레이어를 해제 시킨다.

**매개 변수**

없음

**반환 값**

성공하면 0을 반환하고, 실패하면 음수 반환

### free

```java
public void free()
```

클립 내의 사용한 모든 리소스를 해제한다. 이 메소드를 호출하지 않으면 사용된 클립 데이터나 리소스는 메모리에 남아 있을 수 있다.

**매개 변수**

없음

**반환 값**

없음

### mediaControl

```java
protected int mediaControl(int cmd, int[] buf1, int[] buf2)
```

매체의 일반적인 기능 이외에 제조사에서 지원해주는 특별한 기능 명령을 수행 시킬 때 사용되어 진다. 예를 들면, 제조사에서 현재 재생시간을 얻어올 수 잇는 제어 명령을 지원한다면, 그 명령을 이 함수를 이용해서 내릴 수 있다. 매개변수에 따라 타입이 맞는 메소드를 사용하면 된다.

**매개 변수**

- `cmd` - [in] 수행할 제어 명령
- `buf1` - [in] 컨트롤 명령에서 사용할 수 buf1
- `buf2` - [in/out] 컨트롤 명령에서 사용할 수 buf2

**반환 값**

성공 0 실패 음수 참고사항 [표 2-17-3]에 정의된 것 중 이 메쏘드에서 사용할 수 있는 제어 명령은 다음과 같다. MDACTRL_GET_MEDIA_TIME MDACTRL_SET_SYNC MDACTRL_GET_SYNC MDACTRL_SET_STOP_TIME MDACTRL_CAPTURE_IMAGE MDACTRL_PREVIEW_START MDACTRL_PREVIEW_STOP MDACTRL_GET_STOP_TIME [표 2-17-2] MIME TYPE 별 지원 가능한 미디어 컨트롤 명령 mime type 지원 가능한 미디어 컨트롤 명령 “Qualcomm_CMX” MDACTRL_GET_MEDIA_TIME, // 미디어의 현재 재생 시간 “Yamaha_MA1” MDACTRL_SET_SYNC, // 인스턴스간 동기 설정 “Yamaha_MA2” MDACTRL_GET_SYNC, // 동기되는 인스턴스 “Yamaha_MA3” 얻어옴 “Yamaha_MA5” MDACTRL_GET_STOP_TIME // 재생정지시점 “Yamaha_SMAF” 얻어옴. “Yamaha_SMAF-Phrase” MDACTRL_SET_STOP_TIME // 재생정지시점 설정함. “Yamaha_SMAF-Audio” MDACTRL_SET_MODE // 모드를 이름을 받아서 “audio/MIDI” 설정함. “audio/WAVE” “audio/MP3” “audio/TONE” “audio/FREQTONE" “IS96” “IS96A” “IS733” “IS127” “G.723.1” “audio/AAC” “audio/AAC+” “video/MPEG4” MDACTRL_GET_MEDIA_TIME, // 미디어의 현재 재생 시간 “video/H.263” MDACTRL_PREVIEW_START, // 카메라 프리뷰를 “video/H.264” 시작한다. “video/mjpeg” MDACTRL_PREVIEW_STOP, // 카메라 프리뷰를 “image/jpeg” 정지한다. MDACTRL_GET_STOP_TIME, // 재생정지시점 얻어옴. MDACTRL_SET_STOP_TIME // 재생정지시점 설정함. MDACTRL_CAPTURE_IMAGE // 정지 영상 캡쳐함. MDACTRL_GET_CAPTURE_IMAGE, // 캡쳐된 정지 영상 이미지 데이터를 얻어옴 MDACTRL_SET_MODE // 모드를 이름을 받아서 설정함. [표 2-17-3] 미디어 컨트롤 명령과 매개 변수에 대한 설명 Cmd MDACTRL_GET_MEDIA_TIME buf1 없음 [out] buf2 int buf2[0] = 현재 재생 시간(단위 millisecond) 설명 전체 재생 시간과 관계해서 현재 재생 시간(단위 millisecond)을 구한다. 비고 cmd MDACTRL_SET_SYNC buf1 [in] int buf1[0] = 동기화 할 슬레이브 미디어 인스턴스 식별자의 수 int buf1[1] = 동기화 할 첫번째 슬레이브 미디어 인스턴스 식별자 int buf1[2] = 동기화 할 두번째 슬레이브 미디어 인스턴스 식별자 …… 동기화 할 슬레이브 미디어 인스턴스 식별자의 수 만큼 반복 buf2 없음 멀티 채널에서 재생되는 미디어들 간의 채널 동기화를 설정한다. 설명 동기화 해제는 buf1[0] = 매체 처리기 인스턴스 식별자의 배열의 크기에 0을 넘겨 해제한다. 비고 cmd MDACTRL_GET_SYNC [in] buf1 int buf1[0] = 최대 멀티 채널 배열의 크기 int buf2[0] 기화된 첫번째슬레이브 미디어인스턴스식별자 buf2 int buf2[1] 된 두번째슬레이브 미디어인스턴스식별자 ……배열의 크기만큼 반복 설명 멀티 채널에서 재생되는 미디어들 간의 채널 동기화 정보를 얻어온다. 비고 cmd MDACTRL_SET_STOP_TIME [in] buf1 int buf1[0] 재생을 멈출 시점(milli second 단위) buf2 없음 설명 미디어의 전체 재생 시간과 관련하여, 재생을 멈출 시점을 설정한다. 비고 cmd MDACTRL_GET_CAPTURE_IMAGE [in] buf1 int buf1[0] – 이미지 데이터의 크기 buf2 [out] byte buf2[] – 캡쳐된 이미지가 저장될 버퍼 MDACTRL_CAPTURE_IMAGE 제어 명령을 이용해서 캡쳐한 이미지

**설명**

데이터를 얻어온다. return value 성공 : 캡쳐된 스크린 샷의 크기 비고 실패 : `M_E_NOTSUP` : 지원 안함 `M_E_ERROR` : 기타 에러 cmd MDACTRL_CAPTURE_IMAGE buf1 없음 buf2 [out] int buf1[0] = 이미지 데이터의 크기 플레이 되고 있는 동영상의 스크린 샷을 캡쳐 한다. 이 명령은 단지 스크린 샷을 캡쳐하는 기능만 한다. 스크린 샷된 설명 이미지를 얻어오고 싶을 때에는 이 명령으로 얻어온 이미지 크기 만큼 버퍼를 생성하여, `MH_MDACTRL_GET_CAPTURE_IMAGE` 명령을 이용하여 이 생성한 버퍼를 전달하여 얻어올 수 있도록 한다. 비고 cmd MDACTRL_PREVIEW_START buf1 없음 buf2 없음 현재 설정된 화면 모드와 화면 사이즈에 따라 프리뷰 재생을 시작한다.

**설명**

이미 프리뷰가 재생 중이라면 아무런 일도 하지 않는다. 비고 cmd MDACTRL_PREVIEW_STOP buf1 없음 buf2 없음 프리뷰 재생을 하고 있는 상태에서 프리뷰 재생을 멈춘다. 만약 프리뷰가

**설명**

재생 중이 아니면 아무런 일도 하지 않는다. 비고 이 함수는 무조건 성공해야 한다. cmd MDACTRL_SET_MODE [in] buf1 String buf1 : 모드 이름 buf2 없음 설명 buf1 로 넘어오는 모드 이름으로 모드를 설정한다. 비고 cmd MDACTRL_GET_STOP_TIME buf1 없음 [out] buf2

```c
int buf2[0] : 현재 설정되어 있는 중지 시점
현재 설정되어 있는 일시 중지 시킬 시점을 mili-second 단위로
```

설명 전달한다. 만약 일시 중지 시점이 설정이 되어 있지 않은 상태라면, -1 값을 매개변수 buf2으로 전달한다. 비고

### mediaControl

```java
protected int mediaControl(int cmd, int[] buf1, byte[] buf2)
```

매체의 일반적인 기능 이외에 제조사에서 지원해주는 특별한 기능 명령을 수행 시킬 때 사용되어 진다. 예를 들면, 제조사에서 현재 재생시간을 얻어올 수 잇는 제어 명령을 지원한다면, 그 명령을 이 함수를 이용해서 내릴 수 있다. 매개변수에 따라 타입이 맞는 메소드를 사용하면 된다.

**매개 변수**

- `cmd` - [in] 수행할 제어 명령
- `buf1` - [in] 컨트롤 명령에서 사용할 수 buf1
- `buf2` - [in/out] 컨트롤 명령에서 사용할 수 buf2

**반환 값**

성공 0 실패 음수 참고사항 [표 2-17-3]에 정의된 것 중 이 메쏘드에서 사용할 수 있는 제어 명령은 다음과 같다. MDACTRL_GET_CAPTURE_IMAGE

### mediaControl

```java
protected int mediaControl(int cmd, String buf1, int[] buf2)
```

매체의 일반적인 기능 이외에 제조사에서 지원해주는 특별한 기능 명령을 수행 시킬 때 사용되어 진다. 예를 들면, 제조사에서 현재 재생시간을 얻어올 수 잇는 제어 명령을 지원한다면, 그 명령을 이 함수를 이용해서 내릴 수 있다. 매개변수에 따라 타입이 맞는 메소드를 사용하면 된다.

**매개 변수**

- `cmd` - [in] 수행할 제어 명령
- `buf1` - [in] 컨트롤 명령에서 사용할 수 buf1
- `buf2` - [in/out] 컨트롤 명령에서 사용할 수 buf2

**반환 값**

성공 0 실패 음수 참고사항 [표 2-17-3]에 정의된 것 중 이 메쏘드에서 사용할 수 있는 제어 명령은 다음과 같다. MDACTRL_SET_MODE

### mediaModeControl

```java
public int mediaModeControl(String modeName, int cmd, int pID, int[] buf)
```

mediaDeviceControl 의 MDADEVCTRL_GET_MODE_LIST 컨트롤 명령을 이용하면 현재 제조사에서 지원하는 매체 처리기의 모드의 이름 리스트를 얻어 올 수 있다. 모드란 매체 처리기가 가지고 있는 일반적인 속성을 추상화 하여 구조체로 정의해 놓은 것을 말한다. 모드란 개념의 도입 이유는, Contents Provider(이하 CP)가 매체 처리기를 이용하는 어플리케이션을 구현하고자 할 때에, 매체 처리기의 속성 인자를 개별적으로 설정할 필요 없이, 제조사나 이통사가 정의해 놓은 모드를 이용하여 한번에 설정할 수 있도록 함으로서 CP 들이 매체 처리기를 이용한 어플리케이션을 개발 할 때에 편의성을 제공하기 위해서 이다. 단말에서는 “DEFAULT_MODE” 라는 이름을 가지는 최소한 한 개의 모드는 지원을 하여야 한다. “DEFAULT_MODE” 이외의 제조사나 이통사에서 제공되는 모드는 “DEFAULT_MODE” 내의 속성 인자를 그대로 가져와서 사용하여도 되고, 새로운 속성 정보를 추가하여 사용할 수도 있다. “DEFAULT_MODE” 라는 이름을 갖는 모드의 속성 값들은 디폴트 값으로 설정되어 있으며, 속성 값들을 읽어 오거나 수정이 가능하다. 그 이외에 제조사나 이통사에서 별도로 정의한 지원하는 모드들의 속성 데이타 값의 경우에는 제조사나 이통사에서 읽기 및 쓰기 기능에 대한 권한을 설정할 수 있다. 제조사나 이통사에서 지원하는 모드들에 설정되어 있는 속성값은 제조사나 이통사에 문의 하도록 한다. mediaModeControl() 함수는 이 모드들에 속성값을 읽어 올수도 있으며, 모드의 이름이 “DEFAULT_MODE” 인 모드의 속성값의 경우에는 쓰기도 가능하다. 모드의 이름이 “DEFAULT_MODE” 이외의 다른 이름의 속성데이타의 경우, 제조사나 이통사에서 쓰기 기능에 대한 권한이 주어졌으면, 그 속성 데이터에 한에서 쓰기가 가능하다. 모드의 속성 값은 각 매체 처리기의 일반 적인 속성 값의 이름들은 아래의 표와 같이 이미 정의 되어 있고, 제조사나 이통사에서 추가하고 싶은 속성이 있다면, 추가가 가능하다. 주의할 점은 현재 설정되어 있는 모드 이름의 속성값을 수정하였을 경우에는, 바로 수정된 값이 적용이 되어지지만, 현재 설정되어 있지 않은 다른 이름의 모드의 속성값을 수정하였을 경우에는, 바로 그 수정값이 적용되는 것이 아니고, 그 모드 이름을 매개변수로 하여 mediaControl()의 MDACTRL_SET_MODE 컨트롤 명령이 불리워 져야 비로소 수정된 값이 적용이 된다. buf로 반환되는 값의 타입에 맞는 메소드를 호출하여 사용하면 된다.

**매개 변수**

- `modeName` - [in] 모드 이름 : 단말에서 지원되는 모드의 이름 리스트는 mediaDeviceControl의 MDADEVCTRL_GET_MODE_LIST 커맨드 컨트롤에 의해서 얻을 수 있으며, 이 모드의 이름 리스트 중에서 속성 데이터 값의 내용을 읽어오거나 수정하기를 원할 경우의 그 모드의 이름을 의미한다.
- `cmd` - [in] 컨트롤 명령 (MDAMODECTRL_GET / MDAMODECTRL_SET)
- `pID` - [in] 컨트롤 명령을 수행할 속성 아이디
- `buf` - [in/out]

**반환 값**

성공 0 실패 음수

**참고 항목**

