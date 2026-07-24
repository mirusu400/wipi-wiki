---
title: "3.1.8. 매체 처리기"
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

미디어 디바이스를 구현하기 위한 최상위 추상화 클래스이다.

*Methods inherited from class java.lang.Object: clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 메서드 상세

### allocPlayer

```java
protected int allocPlayer()
```

클립내의 미디어 데이타를 처리하기 위한 플레이어를 할당 받는다. 이 메소드는 클 립의 미디어 데이타를 이용하여 재생하는 등의 실질적인 처리를 하기 이전에 반드시 불리워져야만 하는 메소드이다. 만약 이 메소드를 호출 하지 않고, 혹은 이 메소드 가 실패 한 후에, play 등의 메소드가 불리워지면 에러값을 반환 받게 된다.

**매개 변수**

없음

**반환 값**

성공하면 0을 반환하고, 실패하면 음수 반환 freePlayer()
```java
protected int freePlayer()
```

allocPlayer() 메소드를 이용해서 할당 받았던 플레이어를 해제 시킨다.

**매개 변수**

없음

**반환 값**

성공하면 0을 반환하고, 실패하면 음수 반환

### mediaWriteData

```java
protected int mediaWriteData()
```

클립내의 미디어 데이타를 OEM미디어 디바이스 데이터버퍼로 복사한다. 클립이 가 지고 있는 최대 크기의 미디어 데이터 쓰기(write)를 시도하고 실제 쓰여(write)진 크기가 반환된다.

**매개 변수**

없음

**반환 값**

쓰여(write)진 크기

### mediaReadData

```java
protected int mediaReadData()
```

OEM미디어 디바이스에 있는 데이터를 클립내의 버퍼로 복사한다. 클립이 가질수 있 는 최대 크기의 미디어 데이터 읽기(read)를 시도하고, 실제 읽어(read)진 크기가 반환된다.

**매개 변수**

없음

**반환 값**

읽어(read)진 크기 mediaControl protected static int mediaControl(int mediaID, int cmd, Object buf1, Object buf2); HAL의 `MH_mdaControl`()함수를 부른다. 전달값과 반환값의 의미는 `MH_mdaControl`()함수와 일치한다.

**매개 변수**

`MH_mdaControl`()함수 참조

**반환 값**

`MH_mdaControl`()함수 참조 mediaModeControl public int mediaModeControl(int mdaID, String modeName, int cmd, int pID, Object buf); HAL의 `MH_mdaModeControl`()함수를 부른다. 전달값과 반환값의 의미는 `MH_mdaModeControl`()함수와 일치한다.

**매개 변수**

`MH_mdaModeControl`()함수 참조

**반환 값**

`MH_mdaModeControl`()함수 참조 mediaDeviceControl protected static int mediaDeviceControl(int deviceID, int cmd, Object buf1, Object buf2); HAL의 `MH_mdaDevControl`()함수를 부른다. 전달값과 반환값의 의미는 `MH_mdaDevControl`()함수와 일치한다.

**매개 변수**

`MH_mdaDevControl`()함수 참조

**반환 값**

`MH_mdaDevControl`()함수 참조 mediaInfo public static int mediaInfo(int mediaID); HAL의 `MH_mdaGetDeviceInfo`()함수를 부른다. 반환값은 `MH_mdaGetDeviceInfo`(`M_Int32` devID, `M_Int32`* rtnInfo)에서 rtnInfo로 반 환되는 값의 의미와 일치한다.

**매개 변수**

`MH_mdaGetDeviceInfo`()참조

**반환 값**

`MH_mdaGetDeviceInfo`()참조

### setWaterMark

```java
public void setWaterMark(int percent)
```

PlayListener.END_OF_DATA, PlayListener.FULL_OF_DATA 이벤트가 발생할 수위선 (WaterMark)을 지정한다. 수위선이 90%로 설정되었을 경우, 재생 중이라면 클립내 저장 데이타의 90% 이상이 재생되면 PlayListener.END_OF_DATA 이벤트가 발생하고, 녹음 중이라면 클립내 저장 버퍼의 90% 이상이 차면 PlayListener.FULL_OF_DATA 이 벤트가 발생하게 된다. 설정된 수위선(WaterMark)이 넘어 이벤트가 발생할 경우, 이 벤트는 한번만 발생하고 수위선(WaterMark) 설정은 자동 정지(disable)된다. 즉 재 생중 수위선이 90%로 설정되어 있는 경우, 재생이 90%가 넘었을 때 이벤트가 한번 발생하면, 재생이 93%, 95%가 되어도 더 이상 이벤트가 발생하지 않는다. 이벤트를 다시 발생시킬려면 reaciveWaterMark()를 불러주어야 한다. 기본값은 0%이다

**매개 변수**

- `percent` - [in] 수위선(0-100)

**반환 값**

없음

### reactiveWaterMark

```java
public void reactiveWaterMark()
```

정지(disable)된 수위선 설정을 재개(enable)한다. 이미 설정(enable)되어 있으면 아무역할도 하지 않는다. 수위선이 넘을 때 발생하는 이벤트는 이 함수가 수행되고 수위선이 넘는 조건을 만족하면 발생한다.

**매개 변수**

없음

**반환 값**

없음

### setBuffer

```java
public boolean setBuffer(byte[] buf, int dataSize)
```

클립의 내부버퍼를 설정한다. 패러미터로 전달되는 buf가 BaseClip내부버퍼로 사용 되게 된다.이 함수는 BaseClip생성시 버퍼를 생성하지 않았을 때 BaseClip object생 성 후 내부버퍼를 설정하기 위하여 사용된다.

**매개 변수**

- `buf` - 버퍼
- `dataSize` - 버퍼 안에 들어있는 데이타 크기

**반환 값**

성공

true
실패

false 이미 버퍼가 설정되어 있음

### putData

```java
public int putData(byte[] buf, int off, int len)
```

클립에 미디어 데이타를 복사한다. 미디어 데이타는 클립생성 당시 설정한 타입의 데이타이어야 한다. 클립내의 데이타는 매체재생기에서 재생되면 줄어들고, putData(byte[] buf, int off, int len)로 늘어나게 된다. 복사할 데이터 값의 크기 가 클립내부버퍼가 수용할 데이타보다 크면 수용할 수 있는 만큼만 복사된다

**매개 변수**

- `buf` - 데이터 버퍼
- `off` - 버퍼 offset
- `len` - 복사할 크기

**반환 값**

복사된 크기

### getData

```java
public int getData(byte[] buf, int off, int len)
```

클립에서 buf로 미디어 데이타를 복사한다. 클립내의 데이타는 매체재생기에서 녹음 되면 늘어나고, getData(byte[] buf, int off, int len)로 줄어들게 된다. 클립내부 의 데이타가 전달한 버퍼보다 크면 버퍼크기만큼만 복사된다.

**매개 변수**

- `buf` - 클립내부의 데이타가 복사될 버퍼
- `off` - 복사될 시작위치
- `len` - 복사될 크기

**반환 값**

복사된 크기

### clearData

```java
public void clearData()
```

클립내의 이용가능한 데이타를 모두 버린다.

**매개 변수**

없음

**반환 값**

없음

### availableDataSize

```java
public int availableDataSize()
```

클립에서 이용가능한 데이타 크기(클립 내부버퍼 크기가 아님)

**매개 변수**

없음

**반환 값**

이용가능한 데이타 크기

### playStart

```java
protected boolean playStart (boolean repeat)
```

Player.play(Clip clip, boolean repeat)메쏘드 안에서 실제 재생함수를 부르기 전 repeat값을 매개변수로 불러준다. 실제 미디어 play가 읽어나기 전에 해야 할 일이 있으면 여기서 설정한다.

**매개 변수**

- `repeat` - Player.play()에 전달된 repeat값

**반환 값**

true Player.play()함수 수행이 정상적으로 수행됨 false Player.play()함수가 더 이상 수행되지 않고 false로 반환됨

### recordStart

```java
protected boolean recordStart()
```

Player.record(BaseClip clip)메쏘드 안에서 실제 record함수를 부르기 전 불러준다. 실제 미디어 record가 읽어나기 전에 해야 할 일이 있으면 여기서 설정한다.

**매개 변수**

없음

**반환 값**

true Player.record()함수 수행이 정상적으로 수행됨 false Player.record()함수가 더 이상 수행되지 않고 false로 반환됨

### playUpdate

```java
public boolean playUpdate(int event, int parm)
```

클립 재생 시 상태변화를 알린다. 전달되는 이벤트는 PlayListener.playUpdate()와 같다.

**매개 변수**

- `event` - 상태값
- `parm` - 각 event에 추가 전달 값이 있을 경우 사용
- `Class` - Clip java.lang.Object | +--org.kwis.msp.media.BaseClip +--org.kwis.msp.media.Clip
- `public` - class Clip extends Clip 이 클래스는 Player 에 의해 재생되는 클립을 구현한다.
- `Methods` - inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 필드 상세 설명 생성자 상세설명 Clip

### Clip

```java
public Clip(String type, byte[] buf)
```

이미 데이타가 저장되어 있는 매개변수를 받아들여 클립을 생성한다. 그 외는 Clip(String type, int bufSize)과 같다

**매개 변수**

- `type` - 리소스 타입
- `buf` - 데이타가 들어 있는 버퍼 Clip

### Clip

```java
public Clip(String type, String resourceName)
```

이미 데이타가 저장되어 있는 리소스이름을 받아들여 클립을 생성한다. 그 외는 Clip(String type, byte[] buf)과 같다

**매개 변수**

- `type` - 리소스 타입
- `resourceName` - 데이타가 들어 있는 리소스이름 메쏘드 상세설명 getType

### getType

```java
public java.lang.String getType()
```

클립의 Type을 구한다

**반환 값**

Type 문자열

### setPosition

```java
public boolean setPosition(int ms)
```

지원하지 않는 타입으로 생성된 클립에 이 함수를 호출할 경우, MediaUnsupportedException이 발생한다.

**매개 변수**

- `ms` - 클립 재생을 시작할 시작 시점(milli second)

**반환 값**

true
성공

false 설정 실패

### getVolume

```java
public final int getVolume()
```

클립 재생기의 볼륨을 읽어온다. 클립 재생기의 독립적인 볼륨 설정을 지원할 경우, 이 함수는 클립 재생기의 볼륨을 읽어온다. 지원하지 않을 경우는, 클립생성 타입이 달라도 같은 볼륨소스를 가리킬 수 있다. 볼륨의 최소값은 0 이고, 최대값은 100이 다.

**매개 변수**

없음

**반환 값**

성공

볼륨 값 (0-100 사이의 볼륨 값)

### setVolume

```java
public final boolean setVolume(int level)
```

클립 재생기의 볼륨을 설정한다. 클립 재생기의 독립적인 볼륨 설정을 지원할 경우, 이 함수는 클립 재생기의 볼륨을 설정한다. 지원하지 않을 경우는, 클립생성 타입이 달라도 같은 볼륨소스를 가리킬 수 있다. 설정할 볼륨의 최소값은 0 이고, 최대값은 100이다.

**매개 변수**

- `level` - 볼륨 값 (0-100사이의 볼륨 값) setListener

### setListener

```java
public void setListener(PlayListener listener)
```

클립 재생 시 상태변화를 알려줄 listener를 등록한다.

**매개 변수**

- `listener` - 새로운 listener, 만일 null 이면 기존 것을 제거함
- `Class` - Player java.lang.Object | +--org.kwis.msp.media.Player
- `public` - class Player extends java.lang.Object 이 클래스는 미디어를 재생하기 위한 static 메쏘드를 포함하는 클래스이다.
- `Methods` - inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 메쏘드 상세설명 pause

### pause

```java
public static boolean pause(BaseClip clip)
```

매체 처리(재생/녹음)를 일시적으로 멈춘다. 이 함수가 불려 매체처리가 일시 정지 하게 되면 클립에 등록한 이벤트 listener함수에 PAUSE 상태가 전달된다. 일시로 멈 추어 있거나, 정지되어 있는 처리기에 대해서 이 함수를 다시 부르면, 이 함수는 아 무런 역할을 하지 않는다 pause를 지원하지 않는 타입으로 생성된 클립으로 pause을 시도할 경우, MediaUnsupportedException이 발생한다.

**매개 변수**

- `clip` - 일시 중지시킬 클립

**반환 값**

true
성공

false 이미 멈추어 있거나, 정지되어 있음

### stop

```java
public static boolean stop(BaseClip clip)
```

매체처리(재생/녹음)를 종료한다. 이 함수가 불려 매체처리를 종료하면 클립에 등록 한 이벤트 listener함수에 STOP상태가 전달된다. 정지되어 있는 처리기에 대해서 이 함수를 다시 부르면, 이 함수는 아무런 역할을 하지 않는다.

**매개 변수**

- `clip` - 종료시킬 클립

**반환 값**

true
성공

false 이미 정지되어 있음

### resume

```java
public static boolean resume(BaseClip clip)
```

일시 정지한 매체처리(재생/녹음)를 재개한다. 이 함수가 불려 매체처리를 재개하면 클립에 등록한 이벤트 listener함수에 RESUME상태가 전달된다. 매체처리중인 처리기 에 대해서 이 함수를 다시 부르면 이 함수는 아무런 역할을 하지 않는다. resume를 지원하지 않는 타입으로 생성된 클립으로 resume을 시도할 경우, MediaUnsupportedException이 발생한다.

**매개 변수**

- `clip` - 재개시킬 클립

**반환 값**

true
성공

false 이미 매체처리 중

### play

```java
public static boolean play(BaseClip clip, boolean repeat)
```

클립의 데이타를 재생한다. 이 함수가 불려 매체처리를 시작하면 클립에 등록된 이 벤트 listener함수에 START상태가 전달된다. 이미 재생되고 있는 클립이 있어 전달 된 클립을 재생할 수 없다면 UnavailableException이 발생한다. 재생중인 클립으로 다시 재생하려고 하면 이 함수는 아무런 역할도 하지 않는다. 클립데이타가 소진되 면 이벤트 listener함수에 END_OF_DATA상태가 전달된다. 스트리밍 재생을 하고 싶은 경우에는 클립 데이타가 완전 소진되기 전에, 주기적으로 Clip.putData()로 클립 데 이타를 채워주어야 한다.

**매개 변수**

- `clip` - 재생할 클립
- `repeat` - false이면 1회 재생, true는 반복 재생

**반환 값**

true
성공

false 이미 재생 중

### record

```java
public static boolean record(BaseClip clip)
```

녹음을 시작한다. 녹음을 지원하지 않는 타입으로 생성된 클립으로 녹음을 시도할 경우, MediaUnsupportedException이 발생한다. 이 함수가 불려 매체처리를 시작하면 클립생성시 등록된 이벤트 listener함수에 RECORD상태가 전달된다. 이미 녹음중인 클립이 있어, 녹음을 할 수 없다면 UnavailableException이 발생한다. 녹음중인 클 립으로 다시 녹음하려고 하면 이 함수는 아무런 역할도 하지 않는다. 녹음 중, 클립 내부버퍼가 완전히 차면 이벤트 listener함수에 FULL_OF_DATA상태가 전달된다. 스트 리밍 녹음을 하고 싶은 경우에는 클립 내부버퍼가 완전히 차기 전에, 주기적으로 Clip.GetData()로 클립 내부버퍼를 비워주어야 한다

**매개 변수**

- `clip` - 녹음데이타를 저장할 클립

**반환 값**

true
성공

false 이미 녹음 중

---

## Interface PlayerListener

```java
public interface PlayerListener
```

이 인터페이스는 미디어 재생기의 상태변화를 알고자 하는 응용프로그램에서 쓰인다.

## 필드 상세

ERROR public static final int ERROR 에러가 발생 값은 -1 이다. END_OF_DATA public static final int END_OF_DATA 재생데이타의 마지막에 도달함 값은 1 이다. STARTED public static final int START 재생을 시작 값은 2 이다. STOPPED public static final int STOP 재생/녹음이 멈춤 값은 3 이다. PAUSED public static final int PAUSE 재생/녹음이 일시 정지 값은 4 이다. RESUMED public static final int RESUME 일시 정지된 데이타의 재생 재개 값은 5 이다. RECORDED public static final int RECORD 녹음 시작 값은 6 이다. FULL_OF_DATA public static final int FULL_OF_DATA 녹음 버퍼가 완전히 채워져서 더 이상 녹음할 수 없음, 값은 7 이다.

## 메서드 상세

### playerUpdate

```java
public void playerUpdate(Clip clip, int event, int parm)
```

클립재생 시 상태가 변할 때 불리는 메쏘드이다.

**매개 변수**

- `Clip` - 상태변화가 일어난 클립
- `event` - 상태값
- `parm` - 각 event에 추가 전달 값이 있을 경우 사용
- `Class` - UnavailableException java.lang.Object | +--java.lang.Throwable | +--java.lang.Exception | +--java.lang.RuntimeException | +-- org.kwis.msp.media.UnavailableException
- `public` - class UnavailableException extends RuntimeException 리소스를 얻을 수 없을 때 발생하는 exception클래스.
- `Methods` - inherited from class java.lang.Throwable getMessage, printStackTrace, toString
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세설명 UnavailableException

### UnavailableException

```java
public UnavailableException()
```

- `UnavailableException을` - 생성한다. UnavailableException

### UnavailableException

```java
public UnavailableException(String s)
```

- `UnavailableException을` - 생성한다.

**매개 변수**

- `s` - UnavailableException의 세부 메세지
- `Class` - Vibrator java.lang.Object | +--org.kwis.msp.media.Vibrator
- `public` - class Vibrator extends java.lang.Object 핸드 셋의 진동기를 제어하는 클래스이다.
- `Methods` - inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 메쏘드 상세설명 on

### on

```java
public static void on(int level, int duration)
```

이 메쏘드가 리턴된 후에는 진동기가 정해진 시간 동안 진동해야 한다. 이 메쏘드가 불리기전에 이미 진동하고 있었다면 진동을 초기화하고 매개변수 duration 으로 주 어진 시간 동안 진동한다. 매개변수 level값이 0보다 큰 경우만 timeout 값이 유효 하다. level값 0은 vibrator가 꺼지는 것을 의미한다 진동강도는 매개변수 level값 으로 정해지고 0-100사이의 값이 올 수 있다. 100은 하드웨어가 지원하는 가장 강한 진동을 0은 가장 약한 진동을 의미한다. 0-100사이 값을 어느 정도의 진동세기와 일 치시키는가는 아래의 예처럼 하드웨어가 지원하는 진동단계를 백분율로 일치시킨 것 에 따른다. 하드웨어가 몇 단계의 진동세기를 지원하는가는 HandsetProperty.getSystemProperty("VIBRATORLEVEL")로 알 수 있다. 예) 진동세기가 하나인 하드웨어 => 1-100 : 진동 진동세기가 강, 약 두개인 하드웨어 => 1-50 : 약 진동, 51-100 : 강진 동 진동세기가 강,중,약 세 개인 하드웨어 => 1-33:약 진동, 34-66:중진 동, 67- 100:강진 동

**매개 변수**

- `level` - 0이면 off, 1-100이면 운영체제에서 일치시킨 진동세기로 진동
- `duration` - 진동할 시간(milliseconds), 0이면 무한 진동
- `Class` - Volume java.lang.Object | +--org.kwis.msp.media.Volume
- `public` - class Volume extends java.lang.Object 소리의 볼륨을 조절하는 메쏘드를 모은 클래스입니다
- `Methods` - inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 필드 상세 설명 VOLTYPE_VOICE
- `protected` - static final int VOLTYPE_VOICE 통화음량을 의미한다. 값은 1이다. VOLTYPE_RING
- `protected` - static final int VOLTYPE_RING 착신벨음량을 의미한다. 값은 2이다. VOLTYPE_KEYTONE
- `protected` - static final int VOLTYPE_KEYTONE 키톤 음량을 의미한다. 값은 3이다. VOLTYPE_MESSAGE
- `protected` - static final int VOLTYPE_MESSAGE
- `SMS` - 메시지 착신 음량을 의미한다. 값은 4이다. VOLTYPE_ALARM
- `protected` - static final int VOLTYPE_ALARM 알람 음량을 의미한다. 값은 5이다. VOLTYPE_ALERT
- `protected` - static final int VOLTYPE_ALERT 경고음 음량을 의미한다. 값은 6이다. VOLTYPE_MMEDIA
- `protected` - static final int VOLTYPE_MMEDIA 모든 멀티미디어 장치의 마스터 음량을 의미한다. 값은 7이다. VOLTYPE_GAME
- `protected` - static final int VOLTYPE_GAME 게임의 음량을 의미한다. 값은 8이다. 메쏘드 상세설명 get

### get

```java
public static int get()
```

볼륨의 값을 리턴한다. 각 디바이스마다 독립적인 볼륨이 설정되었을 경우, 이 값은 정확하지 않을 수 있다. 그럴 경우, 정확한 각 디바이스의 볼륨은 Clip.getVolume() 으로 읽어와야 한다. 반환되는 볼륨값은 0 – 100사이의 값으로 환산하여 반환되어야 한다. 0-100사이 값 을 어느 정도의 볼륨세기와 일치시키는가는 아래의 예처럼 하드웨어가 지원하는 볼 륨단계를 백분율로 일치시킨 것에 따른다. 하드웨어가 몇 단계의 볼륨세기를 지원하 는가는 HandsetProperty.getSystemProperty("VOLUMELEVEL")에서 반환한다. 예) 볼륨세기가 강, 약 두개인 하드웨어 => 1-50 : 약 볼륨 51-100 : 강 볼륨 볼륨세기가 강,중,약 세 개인 하드웨어 => 1-33:약 볼륨, 34-66:중 볼륨, 67-100:강 볼륨

**매개 변수**

없음

**반환 값**

볼륨값

### set

```java
public static void set(int level)
```

볼륨을 설정한다. 볼륨을 설정할 수 있는 모든 디바이스의 볼륨을 설정한다. 각 디 바이스마다 독립적인 불륨을 설정할 경우, Clip에 있는 볼륨 API을 이용하도록 한다. 설정할 볼륨의 최소값은 0 이고, 최대값은 100이다.

**매개 변수**

- `level` - 볼륨값(0-100사이의 볼륨값) setMute

### setMuteState

```java
public static void setMuteState(int volType, boolean mute)
```

throw IllegalArgumentException 단말기의 볼륨 타입별 소리 발생 방지를 설정한다. volType의 값에 따라 볼륨 타입 별 소리 발생 방지를 설정한다. volType의 값으로는 VOLTYPE_VOICE, VOLTYPE_RING, VOLTYPE_KEYTON, VOLTYPE_MESSAGE, VOLTYPE_ALARM, VOLTYPE_ALERT, VOLTYPE_MMEDIA 의 값들이 올수 있다. 만약 이 의외의 값이 volType으로 전달 된다면,
- `IllegalArgumentException을` - 발생한다.

**매개 변수**

- `volType` - [in] VOLTYPE_VOICE VOLTYPE_RING VOLTYPE_KEYTON VOLTYPE_MESSAGE VOLTYPE_ALARM VOLTYPE_ALERT VOLTYPE_MMEDIA VOLTYPE_GAME 중의 하나
- `mute` - [in] 소리발생 방지 설정 `TRUE` 소리 발생 방지 `FALSE` 소리 발생 허용 Throws IllegalArgumentException volType 이 VOLTYPE_VOICE VOLTYPE_RING VOLTYPE_KEYTON VOLTYPE_MESSAGE VOLTYPE_ALARM VOLTYPE_ALERT VOLTYPE_MMEDIA VOLTYPE_GAME 중의 하나가 아닌경우 getMute public static boolean getMute(int volType) throw IllegalArgumentException 단말기의 볼륨타입별 소리 발생 방지 설정 상태를 얻는다. volType 의 값에 따라 볼 륨 타입별 소리 발생 방지 설정 상태를 얻는다. volType의 값으로는 VOLTYPE_VOICE, VOLTYPE_RING, VOLTYPE_KEYTON, VOLTYPE_MESSAGE, VOLTYPE_ALARM, VOLTYPE_ALERT, VOLTYPE_MMEDIA 의 값들이 올수 있다. 만약 이 의외의 값이 volType으로 전달 된다 면, IllegalArgumentException을 발생한다.

**매개 변수**

- `volType` - [in] VOLTYPE_VOICE VOLTYPE_RING VOLTYPE_KEYTON VOLTYPE_MESSAGE VOLTYPE_ALARM VOLTYPE_ALERT VOLTYPE_MMEDIA VOLTYPE_GAME 중의 하나

**반환 값**

- `TRUE`
성공

- `FALSE`
실패

Throws IllegalArgumentException volType 이 VOLTYPE_VOICE VOLTYPE_RING VOLTYPE_KEYTON VOLTYPE_MESSAGE VOLTYPE_ALARM VOLTYPE_ALERT VOLTYPE_MMEDIA VOLTYPE_GAME 중의 하나가 아닌경우

### setDefaultVolume

```java
public static void setDefaultVolume(int volTVype, int vol)
```

throw IllegalArgumentException 단말기의 볼륨 타입별 디폴트 볼륨을 설정한다.. volType의 값에 따라 볼륨 타입별 디폴트 볼륨을 설정한다. volType의 값으로는 VOLTYPE_GENERAL, VOLTYPE_VOICE, VOLTYPE_RING, VOLTYPE_KEYTON, VOLTYPE_MESSAGE, VOLTYPE_ALARM, VOLTYPE_ALERT, VOLTYPE_MMEDIA, VOLTYPE_GAME 의 값들이 올수 있다. 만약 이 의외의 값이 volType 으로 전달 된다면, IllegalArgumentException을 발생한다.

**매개 변수**

- `volType` - [in] VOLTYPE_VOICE VOLTYPE_RING VOLTYPE_KEYTON VOLTYPE_MESSAGE VOLTYPE_ALARM VOLTYPE_ALERT VOLTYPE_MMEDIA VOLTYPE_GAME 중의 하나
- `vol` - [in] 볼륨값 (0-100 사이의 값) Throws IllegalArgumentException volType 이 VOLTYPE_VOICE VOLTYPE_RING VOLTYPE_KEYTON VOLTYPE_MESSAGE VOLTYPE_ALARM VOLTYPE_ALERT VOLTYPE_MMEDIA VOLTYPE_GAME 중의 하나가 아닌경우 getDefaultVolume public static int getDefaultVolume(int volType) throw IllegalArgumentException 단말기의 볼륨타입별 디폴트 볼륨을 얻는다. volType 의 값에 따라 볼륨 타입별 디 폴트 볼륨을 얻는다. volType의 값으로는 VOLTYPE_GENERAL, VOLTYPE_VOICE, VOLTYPE_RING, VOLTYPE_KEYTON, VOLTYPE_MESSAGE, VOLTYPE_ALARM, VOLTYPE_ALERT, VOLTYPE_MMEDIA, VOLTYPE_GAME 의 값들이 올수 있다. 만약 이 의외의 값이 volType 으로 전달 된다면, IllegalArgumentException을 발생한다.

**매개 변수**

- `volType` - [in] VOLTYPE_VOICE VOLTYPE_RING VOLTYPE_KEYTON VOLTYPE_MESSAGE VOLTYPE_ALARM VOLTYPE_ALERT VOLTYPE_MMEDIA VOLTYPE_GAME 중의 하나

**반환 값**

볼륨값 Throws IllegalArgumentException volType 가 VOLTYPE_VOICE VOLTYPE_RING VOLTYPE_KEYTON VOLTYPE_MESSAGE VOLTYPE_ALARM VOLTYPE_ALERT VOLTYPE_MMEDIA VOLTYPE_GAME 중의 하나가 아닌경우

### setMute

```java
public static void setMute(int volType, boolean mute)
```

throw IllegalArgumentException 단말기의 음원별 소리 발생 방지를 설정한다. volType의 값에 따라 음원별 소리 발 생 방지를 설정한다. volType의 값으로는 VOLTYPE_GENERAL, VOLTYPE_VOICE, VOLTYPE_RING, VOLTYPE_KEYTON, VOLTYPE_MESSAGE, VOLTYPE_ALARM, VOLTYPE_ALERT, VOLTYPE_MMEDIA, VOLTYPE_GAME 의 값들이 올수 있다. 만약 이 의외의 값이 volType 으로 전달 된다면, IllegalArgumentException을 발생한다.

**매개 변수**

- `volType` - [in] VOLTYPE_VOICE VOLTYPE_RING VOLTYPE_KEYTON VOLTYPE_MESSAGE VOLTYPE_ALARM VOLTYPE_ALERT VOLTYPE_MMEDIA VOLTYPE_GAME 중의 하나
- `mute` - [in] 소리발생 방지 설정 `TRUE` 소리 발생 방지 `FALSE` 소리 발생 허용 Throws IllegalArgumentException volType가 VOLTYPE_VOICE VOLTYPE_RING VOLTYPE_KEYTON VOLTYPE_MESSAGE VOLTYPE_ALARM VOLTYPE_ALERT VOLTYPE_MMEDIA VOLTYPE_GAME 중의 하나가 아닌경우 getMute public static boolean getMute(int volType) throw IllegalArgumentException 단말기의 음원별 소리 발생 방지 설정 상태를 얻는다. volType의 값에 따라 음원별 소리 발생 방지 설정 상태를 얻는다. volType의 값이 VOLTYPE_TONE, VOLTYPE_SOUND, VOLTYPE_RECORDER 값 중의 하나가 아닐 때는 IllegalArgumentException을 발생한다.

**매개 변수**

- `volType` - [in] VOLTYPE_VOICE VOLTYPE_RING VOLTYPE_KEYTON VOLTYPE_MESSAGE VOLTYPE_ALARM VOLTYPE_ALERT VOLTYPE_MMEDIA VOLTYPE_GAME 중의 하나

**반환 값**

True 소리 발생 방지

---

## Class MediaUnsupportedException

```text
java.lang.Object
  +--java.lang.Throwable
    +--java.lang.Exception
      +--org.kwis.msp.media.MediaUnsupportedException
```

```java
public class MediaUnsupportedException extends Exception
```

지원되지 않는 기능을 사용하려고 했을 때 발생하는 exception 클래스.

*Methods inherited from class java.lang.Throwable: getMessage, printStackTrace, toString*

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, wait, wait, wait*

## 생성자 상세

### MediaUnsupportedException

```java
public MediaUnsupportedException()
```

MediaUnsupportedException객체를 생성한다.

### MediaUnsupportedException

```java
public MediaUnsupportedException(String s)
```

MediaUnsupportedException객체를 생성한다.

**매개 변수**

- `s` - IOException의 세부 메세지. Camera java.lang.Object | +--org.kwis.msp.media.Camera
- `public` - class Camera extends Object 카메라 디바이스를 제어하기 위한 Camera 클래스를 다음과 같이 정의한다. 필드 상세 설명 DETECT
- `protected` - static final int DETECT 카메라 감지 컨트롤 커맨드, 값은 0이다. MODEL
- `protected` - static final int MODEL 모델명을 알아오는 컨트롤 커맨드. 값은 1이다. GET_MODE_LIST
- `protected` - static final int GET_MODE_LIST 모드의 이름 리스트를 얻어오는 컨트롤 커맨드. 값은 2이다. SET_MODE
- `protected` - static final int SET_MODE 모드를 설정하는 컨트롤 커맨드. 값은 3이다. SET_AXIS
- `protected` - static final int SET_AXIS 화면을 회전/반전시키는 컨트롤 커맨드. 값은 4이다. PREVIEW_START
- `protected` - static final int PREVIEW_START 프리뷰를 시작하는 컨트롤 커맨드. 값은 5이다. PREVIEW_STOP
- `protected` - static final int PREVIEW_STOP 프리뷰를 정지하는 컨트롤 커맨드. 값은 6이다. CAPTRUE_INTERVAL
- `protected` - static final int CAPTRUE_INTERVAL 동영상 플레이어나 저장시에 프레임과 프레임 사이의 시간을 설정하는 커맨드 컨트 롤. 값은 7이다. NORMAL
- `public` - static final int NORMAL 정상 화면. 값은 0이다. HORZ_REVERSE
- `public` - static final int HORZ_REVERSE 수평 반전. 값은 1이다. VERT_REVERSE
- `public` - static final int VERT_REVERSE 수평 반전. 값은 2이다.
- `BOTH` - _REVERSE
- `public` - static final int BOTH_REVERSE 수평, 수직 모두 반전. 값은 3이다. ROTATE90
- `public` - static final int ROTATE90 오른쪽으로 90도 회전. 값은 4이다. ROTATE180
- `public` - static final int ROTATE180 오른쪽으로 180도 회전. 값은 5이다. ROTATE270
- `public` - static final int ROTATE270 오른쪽으로 180도 회전. 값은 6이다. 생성자 상세설명 Camera(String type)

### Camera

```java
protected Camera(String type)
```

카메라 장치를 사용할 클립을 생성하여 반환한다.

**매개 변수**

- `type` - 리소스 타입 Camera(String type, int bufSize)

### Camera

```java
protected Camera(String type, int bufSize)
```

카메라 장치를 사용할 클립을 생성하여 반환한다.

**매개 변수**

- `type` - 리소스 타입
- `buf` - 데이타가 들어 있는 버퍼 메쏘드 상세설명 detect

### detect

```java
public static boolean detect()
```

카메라 장착여부를 탐지한다.

**반환 값**

true 카메라 탐지 성공 false 카메라 탐지 실패

### getModel

```java
public static String getModel()
```

카메라 모델명을 구한다.

**반환 값**

카메라 모델명

### setMode

```java
public boolean setMode(int mode)
```

클립을 재생/녹화를 위한 카메라의 모드를 설정한다. 모드에는 화질, 해상도, LCD에 서 디스플레이 위치등을 포괄한다. 각 모드에 대한 정보는 폰마다 HAL을 포팅하는 방법에 따라 다를 수 있다.

**매개 변수**

- `mode` - 0부터 지원하는 모드번호, 4개의 모드가 지원된다면 각 모드번호는 0~3까지이다 0은 항상 default mode를 가리킨다.

**반환 값**

true 모드 설정 성공 false 모드 설정 실패

### getModeCount

```java
public int getModeCount()
```

지원하는 모드 갯수를 구한다.

**반환 값**

모드 갯수(3이면 지원하는 모든는 0, 1, 2임)

### setProperty

```java
public boolean setProperty(int property)
```

녹화/재생시의 property를 설정한다.

**매개 변수**

- `property` - NORMAL, HORZ_REVERSE, VERT_REVERSE, BOTH_REVERSE, ROTATE90, ROTATE180, ROTATE270값이 올수 있다.

**반환 값**

true 설정 성공 false 설정 실패

### setSize

```java
public boolean setSize(int x,int y,int width,int height)
```

현재의 설정된 모드의 대하여 사용자 정의 OEM 디스플레이 영역을 지정한다. 각 좌 표가 LCD표시 영역을 벗어난 경우에는 MAX LCD표시 영역값이 적용된다.

**매개 변수**

- `x` - 사용자 정의 영역 x좌표
- `y` - 사용자 정의 영역 y좌표
- `width` - 사용자 정의 영역 넓이
- `height` - 사용자 정의 영역 높이

**반환 값**

true
성공

false 사용자 정의 영역 지정을 지원하지 않음 enableOEMDisplayArea public void enableOEMDisplayArea() 각 모드에 정의된 OEM 디스플레이(카메라 디스플레이) 영역을 enable시킨다. 이 함 수를 부르지 않을 경우, 카메라에서 표시하는 영역과 플랫폼이 표시하는 영역이 겹 쳐서 디스플레이될수 있다. 이 함수가 enable되면 플랫폼에서 어떻게 하던 상관없이 카메라 디스플레이 영역은 카메라에서 만이 디스플레이 할수 있다. 반대로 플랫폼이 카메라 디스플레이 영역에 무엇가를 그리고 싶다면 disableOEMDisplayArea()함수를 불러준 다음에 그려야 그릴수 있다. previewStart public void previewStart() 카메라 프리뷰를 시작한다. previewStop public void previewStop() 카메라 프리뷰를 정지한다. StillClip java.lang.Object | +--org.kwis.msp.media.Camera | +--StillClip 카메라 디바이스를 제어하여 정지 영상을 캡쳐하고, 재생하는 StillClip 클래스를 다음과 같이 정의한다.

## 생성자 상세

StillClip(String type)
```java
protected StillClip(String type)
```

정지영상 클립을 생성한다.

**매개 변수**

- `type` - 리소스 타입 StillClip(String type, int bufSize)

### StillClip

```java
protected StillClip (String type, int bufSize)
```

클립내부 버퍼크기가 bufSize로 정지영상 클립을 생성한다.

**매개 변수**

- `type` - 리소스 타입
- `buf` - 데이타가 들어 있는 버퍼 메쏘드 상세설명 snapshot

### snapshot

```java
public boolean snapshot(PlayListener listener)
```

카메라로 정지영상을 촬영한다. 이 함수가 불리면 카메라 디바이스는 백그라운드 (background)로 촬영을 시작하여 클립 내부버퍼로 촬영한 이미지를 복사한다. 촬영 한 이미지가 내부버퍼에 완전히 복사된 시점을 알기위하여는 리스너(listener)를 패 러미터로 전달한다. 촬영한 이미지가 클립내부버퍼에 완전히 복사되면 리스너의 playUpdate()함수에 FULL_OF_DATA가 전달된다. 촬영을 시작하기전에 clearData()함 수를 이용하여 클립내부버퍼를 비워두어야 한다.

**매개 변수**

- `listener` - 리스너

**반환 값**

true 촬영 시작 성공 false 촬영 시작 실패

### view

```java
public boolean view(PlayListener listener)
```

버퍼에 저장된 내용을 화면에 출력한다. 이 함수가 불리면 카메라 디바이스는 백그 라운드(background)로 재생을 시작하여 클립 내부버퍼에서 카메라 디바이스로 촬영 한 이미지를 복사한다. 촬영한 이미지가 카메라 디바이스에서 완전히 재생된 시점을 알기위하여는 리스너(listener)를 패러미터로 전달한다. 촬영한 이미지가 미디어 디 바이스에서 완전히 재생되면 리스너의 playUpdate()함수에 END_OF_DATA가 전달된다. 재생후에도 클립내부버퍼에는 데이타가 그대로 저장되어 있다.

**매개 변수**

- `listener` - 리스너

**반환 값**

true 재생 시작 성공 false 재생 시작 실패

### getData

```java
public byte[] getData()
```

버퍼에 저장된 데이타를 얻는다. 이 함수가 불린이후에는 버퍼에 저장된 데이타는 삭제된다.

**반환 값**

byte array 성공 null 클립 내부버퍼에 저장된 데이타가 없음

### playStart

```java
protected boolean playStart (boolean repeat)
```

Player.play(Clip clip, boolean repeat)메쏘드안에서 실제 재생함수를 부르기전 repeat값을 매개변수로 불러준다. 실제 미디어 play가 읽어나기 전에 해야할 일이 있으면 여기서 설정한다.

**매개 변수**

- `repeat` - Player.play() 에 전달된 repeat 값

**반환 값**

true Player.play()함수 수행이 정상적으로 수행됨 false Player.play()함수가 더이상 수행되지 않고 false로 반환됨

### playUpdate

```java
public boolean playUpdate(int event,int parm)
```

이하 메소스 설명은 Clip 클래스에서 복사되었음 클립 재생시 상태변화를 알린다. 전달되는 이벤트는 PlayListener.playUpdate()와 같다. Overrides playUpdate in class Clip Following copied from class: org.kwis.msp.media.Clip

**매개 변수**

- `event` - 상태값
- `parm` - 각 event에 추가 전달값이 있을 경우 사용 VideoClip java.lang.Object | +--org.kwis.msp.media.Camera | +--VideoClip 카메라 디바이스를 제어하여 동영상 영상을 녹화하고, 재생하는 VideoClip 클래스를 다 음과 같이 정의한다. 생성자 상세설명 VideoClip(String type)

### VideoClip

```java
protected VideoClip(String type)
```

동영상 클립을 생성한다.

**매개 변수**

- `type` - 리소스 타입 VideoClip(String type, int bufSize)

### VideoClip

```java
protected VideoClip(String type, int bufSize)
```

클립내부 버퍼크기가 bufSize로 동영상 클립을 생성한다.

**매개 변수**

- `type` - 리소스 타입
- `buf` - 데이타가 들어 있는 버퍼 메쏘드 상세설명 record

### record

```java
public boolean record(PlayListener listener)
```

녹화를 시작한다. 이 함수가 불리면 백그라운드(background)도 녹화가 시작되고, 카 메라 디바이스에서 촬영한 데이타가 클립내부버퍼로 복사된다. 클립내부버퍼가 다 차면 그 이후부터 촬영된 데이타는 버려지게 된다. 카메라 디바이스 내부버퍼가 완 전히 채워질때까지 stop()이 불리지 않으면, 패러미터로 전달된 리스너의 playUpdate()함수에 FULL_OF_DATA가 전달된다.

**반환 값**

true 녹화 시작 성공 false 녹화 시작 실패

### pause

```java
public boolean pause()
```

녹화/재생을 일시 멈춘다.

**반환 값**

true 일시 중지 성공 false 일시 중지 실패

### resume

```java
public boolean resume()
```

일시 멈추어진 녹화/재생을 재개한다.

**반환 값**

true 재개 성공 false 재개 실패

### stop

```java
public boolean stop()
```

녹화/재생을 멈춘다.

**반환 값**

true 멈춤 성공 false 멈춤 실패

### play

```java
public boolean play(PlayListener listener)
```

재생을 시작한다. 이 함수가 불리면 백그라운드(background)도 재생이 시작되고, 클 립내부버퍼의 데이타가 카메라 디바이스로 복사된다. 클립내부버퍼가 다 비면 그 이 후부터의 재생화면 표시는 폰에 종속적이다. 카메라 내부버퍼의 데이타가 완전히 재 생될때까지 stop()이 불리지 않으면, 패러미터로 전달된 리스너의 playUpdate()함수 에 END_OF_DATA가 전달된다. 재생후에도 클립내부버퍼에는 데이타가 그대로 저장되 어 있다.

**매개 변수**

- `listener` - 리스너

**반환 값**

true 재생 시작 성공 false 재생 시작 실패

### playStart

```java
protected boolean playStart (boolean repeat)
```

Player.play(Clip clip, boolean repeat)메쏘드안에서 실제 재생함수를 부르기전 repeat값을 매개변수로 불러준다. 실제 미디어 play가 읽어나기 전에 해야할 일이 있으면 여기서 설정한다.

**매개 변수**

- `repeat` - Player.play()에 전달된 repeat값

**반환 값**

true Player.play()함수 수행이 정상적으로 수행됨 false Player.play()함수가 더이상 수행되지 않고 false로 반환됨

### playUpdate

```java
public boolean playUpdate(int event, int parm)
```

이하 메소스 설명은 Clip 클래스에서 복사되었음 클립 재생시 상태변화를 알린다. 전달되는 이벤트는 PlayListener.playUpdate()와 같다. Overrides playUpdate in class Clip Following copied from class: org.kwis.msp.media.Clip

**매개 변수**

- `event` - 상태값
- `parm` - 각 event에 추가 전달값이 있을 경우 사용
