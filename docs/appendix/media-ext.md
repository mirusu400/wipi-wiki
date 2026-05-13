# 7.4. Media 관련 API

Media관련된 고급 기능은 선택적으로 제공할 수 있다. 이 기능을 제공하고자 하면, 다 음의 규격에따라 지원되어야 한다.

## 7.4.1. C API

### MC_MdaToneType

**프로토타입**

```c
typedef enum MC_MdaToneType {
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
MC_MDA_NOTE_A4 , //4400 Hz -Piano Notes-
MC_MDA_NOTE_AS4 , //4661 Hz
MC_MDA_NOTE_B4 , //4938 Hz
MC_MDA_NOTE_C4 , //5232 Hz
MC_MDA_NOTE_CS4 , //5543 Hz
MC_MDA_NOTE_D4 , //5873 Hz
MC_MDA_NOTE_DS4 , //6222 Hz
MC_MDA_NOTE_E4 , //6592 Hz
MC_MDA_NOTE_F4 , //6985 Hz
MC_MDA_NOTE_FS4 , //7399 Hz
MC_MDA_NOTE_G4 , //7840 Hz
MC_MDA_NOTE_GS4 , //8306 Hz
MC_MDA_NOTE_A5 , //8800 Hz
MC_MDA_NOTE_AS5 , //9322 Hz
MC_MDA_NOTE_B5 , //9877 Hz
MC_MDA_NOTE_C5 , //10465 Hz
MC_MDA_NOTE_CS5 , //11087 Hz
MC_MDA_NOTE_D5 , //11746 Hz
MC_MDA_NOTE_DS5 , //12443 Hz
MC_MDA_NOTE_E5 , //13185 Hz
MC_MDA_NOTE_F5 , //13970 Hz
MC_MDA_NOTE_FS5 , //14799 Hz
MC_MDA_NOTE_G5 , //15680 Hz
MC_MDA_NOTE_GS5 , //16612 Hz
MC_MDA_NOTE_A6 , //17600 Hz
MC_MDA_NOTE_AS6 , //18647 Hz
MC_MDA_NOTE_B6 , //19755 Hz
MC_MDA_NOTE_C6 , //20931 Hz
MC_MDA_NOTE_CS6 , //22174 Hz
MC_MDA_NOTE_D6 , //23493 Hz
MC_MDA_NOTE_DS6 , //24891 Hz
MC_MDA_NOTE_E6 , //26370 Hz
MC_MDA_NOTE_F6 , //27937 Hz
MC_MDA_NOTE_FS6 , //29599 Hz
MC_MDA_NOTE_G6 , //31359 Hz
MC_MDA_NOTE_GS6 , //33224 Hz
MC_MDA_NOTE_A7 , //35200 Hz
} MC_MdaToneType;
```

**설명**

TONE TYPE의 열거형 소리의 음계를 나타낸다

### MC_mdaSetWaterMark

**설명**

MC_MDA_STATUS_END_OF_DATA, MC_MDA_STATUS_FULL_OF_DATA 이벤트가 발생할 수위선 (WaterMark)를 지정한다. 쉬위선이 90%로 설정되었을 경우, 재생중이라면 저장데 이타의 90%이상이 재생되면 MC_MDA_STATUS_END_OF_DATA 이벤트가 발생하고, 녹음 중이라면 저장버퍼의 90%이상이 차면 MC_MDA_STATUS_FULL_OF_DATA 이벤트가 발생 하게 된다. 기본값은 100%이다.

**프로토타입**

```c
void MC_mdaSetWaterMark(MC_MdaClip* clip, M_Int32 percent)
```

**매개 변수**

- `clip` — [in] 클립
- `percent` — [in] 수위선(0-100)
**반환 값**

없음

**부작용**

없음

**참고 항목**

### MC_mdaClipPutToneData

**설명**

클립 타입이 "audio/TONE"인 경우에 클립에 미디어 데이타를 복사한다. 미디어 데 이타는 클립생성당시 설정한 타입의 데이타이어야 한다. 클립내의 데이타는 매체 재생기에서 재생되면 줄어들고, MC_mdaClipPutToneData()로 늘어나게 된다. 복사 할 데이타가 크기가 클립내부버퍼가 수용할 데이타보다 크면 수용할 수 있는 만큼 만 복사된다.

**프로토타입**

```c
M_Int32 MC_mdaClipPutToneData (MC_MdaClip* clip, MC_MdaToneType tone[] ,
M_Int duration[], M_Int32 number)
```

**매개 변수**

- `clip` — [in] 클립
- `tone` — [in] 재생할 톤의 배열
- `duration` — [in] 재생할 톤의 시간에 대한 배열
- `number` — [in] 복사할 갯수
**반환 값**

성공 복사된 갯수 실패 없음

**부작용**

없음

**참고 항목**

없음

### MC_mdaClipPutFreqToneData

**설명**

클립 타입이 "audio/FREQTONE"인 경우에 클립에 미디어 데이타를 복사한다. 미디 어 데이타는 클립생성당시 설정한 타입의 데이타이어야 한다. 클립내의 데이타는 매체재생기에서 재생되면 줄어들고, MC_mdaClipPutFreqToneData()로 늘어나게 된 다. 복사할 데이타가 크기가 클립내부버퍼가 수용할 데이타보다 크면 수용할 수 있는 만큼만 복사된다.

**프로토타입**

```c
M_Int32 MC_mdaClipPutFreqToneData (MC_MdaClip* clip, M_Int32 hiFreq[],
M_Int32 lowFreq[], M_Int32 duration, M_Int32 number)
```

**매개 변수**

- `clip` — [in] 클립
- `hiFreq` — [in] 재생할 고주파 HZ 배열
- `lowFreq` — [in] 재생할 저주파 HZ 배열
- `duration` — [in] 재생할 톤의 시간에 대한 배열
- `number` — [in] 복사할 갯수
**반환 값**

성공 복사된 갯수 실패 없음

**부작용**

없음

**참고 항목**

없음

## 7.4.2. Java API

가 Media (org.kwis.msp.media) Class Clip java.lang.Object | +--org.kwis.msp.media.Clip public class Clip extends java.lang.Object 이 클래스는 Player 에 의해 재생되는 클립을 구현한다.

Methods inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait

### 필드 상세 설명

### SND_TONE_0

public static final int SND_TONE_0 DTMF for 0 key. 값은 0 이다.

### SND_TONE_1

public static final int SND_TONE_1 DTMF for 1 key. 값은 1 이다.

### SND_TONE_2

public static final int SND_TONE_2 DTMF for 2 key. 값은 2 이다.

### SND_TONE_3

public static final int SND_TONE_3 DTMF for 3 key. 값은 3 이다.

### SND_TONE_4

public static final int SND_TONE_4 DTMF for 4 key. 값은 4 이다.

### SND_TONE_5

public static final int SND_TONE_5 DTMF for 5 key. 값은 4 이다.

### SND_TONE_6

public static final int SND_TONE_6 DTMF for 6 key. 값은 6 이다.

### SND_TONE_7

public static final int SND_TONE_7 DTMF for 7 key. 값은 7 이다.

### SND_TONE_8

public static final int SND_TONE_8 DTMF for 8 key. 값은 8 이다.

### SND_TONE_9

public static final int SND_TONE_9 DTMF for 9 key. 값은 9 이다.

### SND_TONE_A

public static final int SND_TONE_A DTMF for A key. 값은 10 이다.

### SND_TONE_B

public static final int SND_TONE_B DTMF for B key. 값은 11 이다.

### SND_TONE_C

public static final int SND_TONE_C DTMF for C key. 값은 12 이다.

### SND_TONE_D

public static final int SND_TONE_D DTMF for D key. 값은 13 이다.

### SND_TONE_POUND

public static final int SND_TONE_POUND DTMF for # key. 값은 14 이다.

### SND_TONE_STAR

public static final int SND_TONE_STAR DTMF for * key. 값은 15 이다.

### SND_NOTE_A4

public static final int SND_NOTE_A4 440.0 Hz -Piano Notes-. 값은 16 이다.

### SND_NOTE_AS4

public static final int SND_NOTE_AS4 466.1 Hz. 값은 17 이다.

### SND_NOTE_B4

public static final int SND_NOTE_B4 493.8 Hz . 값은 18 이다.

### SND_NOTE_C4

public static final int SND_NOTE_C4 523.2 Hz. 값은 19 이다.

### SND_NOTE_CS4

public static final int SND_NOTE_CS4 554.3 Hz. 값은 20 이다.

### SND_NOTE_D4

public static final int SND_NOTE_D4 587.3 Hz. 값으 21 이다.

### SND_NOTE_DS4

public static final int SND_NOTE_DS4 622.2 Hz. 값은 22 이다.

### SND_NOTE_E4

public static final int SND_NOTE_E4 659.2 Hz . 값은 23 이다.

### SND_NOTE_F4

public static final int SND_NOTE_F4 698.5 Hz . 값은 24 이다.

### SND_NOTE_FS4

public static final int SND_NOTE_FS4 739.9 Hz . 값은 25 이다.

### SND_NOTE_G4

public static final int SND_NOTE_G4 784.0 Hz . 값은 26 이다.

### SND_NOTE_GS4

public static final int SND_NOTE_GS4 830.6 Hz. 값은 27 이다.

### SND_NOTE_A5

public static final int SND_NOTE_A5 880.0 Hz . 값은 28 이다.

### SND_NOTE_AS5

public static final int SND_NOTE_AS5 932.2 Hz. 값은 29 이다.

### SND_NOTE_B5

public static final int SND_NOTE_B5 987.7 Hz . 값은 30 이다.

### SND_NOTE_C5

public static final int SND_NOTE_C5 1046.5 Hz . 값은 31 이다.

### SND_NOTE_CS5

public static final int SND_NOTE_CS5 1108.7 Hz . 값은 32 이다.

### SND_NOTE_D5

public static final int SND_NOTE_D5 1174.6 Hz . 값은 33 이다.

### SND_NOTE_DS5

public static final int SND_NOTE_DS5 1244.3 Hz . 값은 34 이다.

### SND_NOTE_E5

public static final int SND_NOTE_E5 1318.5 Hz . 값은 35 이다.

### SND_NOTE_F5

public static final int SND_NOTE_F5 1397.0 Hz . 값은 36 이다.

### SND_NOTE_FS5

public static final int SND_NOTE_FS5 1479.9 Hz . 값은 37 이다.

### SND_NOTE_G5

public static final int SND_NOTE_G5 1568.0 Hz . 값은 38 이다.

### SND_NOTE_GS5

public static final int SND_NOTE_GS5 1661.2 Hz . 값은 39 이다.

### SND_NOTE_A6

public static final int SND_NOTE_A6 1760.0 Hz . 값은 40 이다.

### SND_NOTE_AS6

public static final int SND_NOTE_AS6 1864.7 Hz . 값은 41 이다.

### SND_NOTE_B6

public static final int SND_NOTE_B6 1975.5 Hz . 값은 42 이다.

### SND_NOTE_C6

public static final int SND_NOTE_C6 2093.1 Hz . 값은 43 이다.

### SND_NOTE_CS6

public static final int SND_NOTE_CS6 2217.4 Hz . 값은 44 이다.

### SND_NOTE_D6

public static final int SND_NOTE_D6 2349.3 Hz . 값은 45 이다.

### SND_NOTE_DS6

public static final int SND_NOTE_DS6 2489.1 Hz . 값은 46 이다.

### SND_NOTE_E6

public static final int SND_NOTE_E6 2637.0 Hz . 값은 47 이다.

### SND_NOTE_F6

public static final int SND_NOTE_F6 2793.7 Hz . 값은 48 이다.

### SND_NOTE_FS6

public static final int SND_NOTE_FS6 2959.9 Hz . 값은 49 이다.

### SND_NOTE_G6

public static final int SND_NOTE_G6 3135.9 Hz . 값은 50 이다.

### SND_NOTE_GS6

public static final int SND_NOTE_GS6 3322.4 Hz . 값은 51 이다.

### SND_NOTE_A7

public static final int SND_NOTE_A7 3520.0 Hz . 값은 52 이다.

### 생성자 상세설명

### Clip

public Clip(String type, int bufSize) 특정 타입의 CLIP 을 생성한다. 지원되는 타입은 HandsetProperty.getSystemProperty()의 "SOUNDDEVICES", "MEDIADEVICES"에 의해 구해진 타입들이다. 타입은 MIME에서 지원하는 타입일 경우 "audio/xxx", "video/xxx"와 같이 MIME타입을 따른다. "audio/TONE"인 경우에는 putData(int[] tone, int[] duration, int off, int len)로 데이타가 입력되어야 한다. 타입이 "audio/FREQTONE"인 경우에는 putData(int[] hiFreq, int[] lowFreq, int[] duration, int off, int len)로 데이타가 입력되어야 한다. 그외의 타입인 경우에는 putData(byte[] buf, int off, int len)를 통하여 CLIP 버퍼에 재생할 데이타를 입력한다. CLIP 내부 버퍼 크기는 재생하고자 하는 데이터의 크기만큼 생성 해야 한다.

CLIP 내부 버퍼크기는 CLIP 이 생성될때 만들어져 고정된다. 이벤트 listener함수가 설정되지 않으면 클립재생/녹음시의 상태변화가 전달되지 않는다. 지원되지 않는 타입의 CLIP object를 생성할려고 하면 IllegalArgumentException 이 발생한다.

Parameters:

### type - 리소스 타입

bufSize - 클립내부에 생성될 버퍼의 크기 1. 타입이 "audio/TONE"인 경우에 크기가 3이라면 putData(int[] tone, int[] duration, int off, int len)에서 int[3] tone, int[3] duration이 저장될수 있는 크기이다.

2. 타입이 "audio/FREQTONE"인 경우에 크기가 3이라면 putData(int[] hiFreq, int[] lowFreq, int[] duration, int off, int len)에서 int[3] hiFreq, int[3] lowFreq, int[3] duration가 저장될 수 있는 크기이다.

3. 그외의 타입인 경우 크기가 3이라면, putData(byte[] buf, int off, int len) 에서 byte[3] buf가 저장될 수 있는 크기이다.

### Clip

public Clip(String type) 특정 타입의 클립을 생성한다. Clip(String type, int bufSize)와 같으나, 내부버퍼을 생 성하지 않고 클립을 생성하는 것이 다른다. 이 생성자는 클립 생성시 내부버퍼크기를 모르고, 나중에 버퍼가 설정될 경우에 사용한다. 클립생성후 버퍼를 설정할 경우에는 setBuffer()을 사용한다.

Parameters:

### type - 리소스 타입

### Clip

public Clip(String type, byte[] buf) "audio/TONE", "audio/FREQTONE"타입외의 이미 데이타가 저장되어 있는 매개변수를 받아들여 클립을 생성한다. 그외는 Clip(String type, int bufSize)과 같다 Parameters:

### type - 리소스 타입

### buf - 데이타가 들어 있는 버퍼

### Clip

public Clip(int[] tone, int[] duration) "audio/TONE"타입의 이미 데이타가 저장되어 있는 매개변수를 받아들여 클립을 생성 한다. 그외는 Clip(String type, int bufSize)과 같다 Parameters:

### tone - 톤 데이타가 들어 있는 버퍼

duration - 시간 데이타가 들어 있는 버퍼

### Clip

public Clip(int[] hiFreq, int[] lowFreq, int[] duration) "audio/FREQTONE"타입의 이미 데이타가 저장되어 있는 매개변수를 받아들여 클립을 생성한다. 그외는 Clip(String type, int bufSize)과 같다 Parameters:

### hiFreq - 고주파데이타가 들어 있는 버퍼

lowFreq - 저주파데이타가 들어 있는 버퍼 duration - 시간 데이타가 들어 있는 버퍼

### Clip

public Clip(String type, String filename) 이미 데이타가 저장되어 있는 파일 이름을 받아들여 클립을 생성한다. 그외는 Clip(String type, byte[] buf)과 같다 Parameters:

### type - 리소스 타입

### filename - 데이타가 들어 있는 버퍼

### 메쏘드 상세설명

### getType

public java.lang.String getType()

### 클립의 Type을 구한다

Returns:

### Type 문자열

### setBuffer

public boolean setBuffer(byte[] buf, int dataSize) 클립의 내부버퍼을 설정한다.

Parameters:

### buf - 버퍼

dataSize - 버퍼안에 들어있는 데이타 크기 Returns: true : 버퍼 설정 성공, false : 이미 버퍼가 설정되어 있음

### setBuffer

public boolean setBuffer(int[] tone, int[] duration, int dataSize) 클립의 내부버퍼을 설정한다. "audio/TONE"타입의 데이타를 저장하는 내부버퍼를 설 정한다.

Parameters:

### buf - 버퍼

dataSize - 버퍼안에 들어있는 데이타 크기 Returns: true : 버퍼 설정 성공, false : 이미 버퍼가 설정되어 있음

### setBuffer

public boolean setBuffer(int[] hiFreq, int[] lowFreq, int[] duration, int dataSize) 클립의 내부버퍼을 설정한다. "audio/FREQTONE"타입의 데이타를 저장하는 내부버퍼 를 설정한다.

Parameters:

### buf - 버퍼

dataSize - 버퍼안에 들어있는 데이타 크기 Returns: true : 버퍼 설정 성공, false : 이미 버퍼가 설정되어 있음

### setWaterMark

public void setWaterMark(int percent) END_OF_DATA, FULL_OF_DATA 이벤트가 발생할 수위선(WaterMark)를 지정한다.

쉬위선이 90%로 설정되었을 경우, 재생중이라면 저장버퍼의 90%이상이 재생되면 END_OF_DATA이벤트가 발생하고, 녹음중이라면 저장버퍼의 90%이상이 차면 FULL_OF_DATA 이벤트가 발생하게 된다. 기본값은 100%이다.

Parameters: percent - 수위선(0-100)

### putData

public int putData(byte[] buf, int off, int len) 클립타입이 "audio/TONE", "a udio/FREQTONE"외의 경우에 클립에 미디어 데이타를 복사한다. 미디어 데이타는 클립생성당시 설정한 타입의 데이타이어야 한다. 클립내의 데이타는 매체재생기에서 재생되면 줄어들고, putData(byte[] buf, int off, int len)로 늘 어나게 된다. 복사할 데이타가 크기가 클립내부버퍼가 수용할 데이타보다 크면 수용할

### 수 있는 만큼만 복사된다

Parameters:

### buf - 데이타 버퍼

### off - 버퍼 offset

### len - 복사할 크기

Returns:

### 복사된 크기

### putData

public int putData(int[] buf, int off, int len) 클립타입이 "audio/TONE", "audio/FREQTONE" 외의 경우에 클립에 미디어 데이타를 복사한다. 미디어 데이타는 클립생성당시 설정한 타입의 데이타이어야 한다. 클립내의 데이타는 매체재생기에서 재생되면 줄어들고, putData(int[] buf, int off, int len)로 늘어 나게 된다. 복사할 데이타가 크기가 클립내부버퍼가 수용할 데이타보다 크면 수용할

### 수 있는 만큼만 복사된다

Parameters:

### buf - 데이타 버퍼

### off - 버퍼 offset

### len - 복사할 크기

Returns:

### 복사된 크기

### putData

public int putData(int[] tone, int[] duration, int off, int len) 클립 타입이 "audio/TONE"인 경우에 클립에 미디어 데이타를 복사한다. 미디어 데이 타는 클립생성당시 설정한 타입의 데이타이어야 한다. 클립내의 데이타는 매체재생기 에서 재생되면 줄어들고, putData(int[] tone, int[] duration, int off, int len)()로 늘어나 게 된다. 복사할 데이타가 크기가 클립내부버퍼가 수용할 데이타보다 크면 수용할 수

### 있는 만큼만 복사된다

Parameters: tone - SND_TONE_XXX, SNT_NOTE_XXX값의 배열

### duration - 재생할 시간에 대한 배열

### off - 버퍼 offset

### len - 복사할 크기

Returns:

### 복사된 크기

### putData

public int putData(int[] hiFreq, int[] lowFreq, int[] duration, int off, int len) 클립 타입이 "audio/FREQTONE"인 경우에 클립에 미디어 데이타를 복사한다. 미디어 데이타는 클립생성당시 설정한 타입의 데이타이어야 한다. 클립내의 데이타는 매체재 생기에서 재생되면 줄어들고, putData(int[] hiFreq, int[] lowFreq, int[] duration, int off, int len)로 늘어나게 된다. 복사할 데이타가 크기가 클립내부버퍼가 수용할 데이타

### 보다 크면 수용할 수 있는 만큼만 복사된다

Parameters:

### hiFreq - 고주파HZ 값의 배열

### lowFreq - 저주파HZ 값의 배열

### duration - 재생할 시간에 대한 배열

### off - 버퍼 offset

### len - 복사할 크기

Returns:

### 복사된 크기

### getData

public int getData(byte[] buf, int off, int len) 클립에서 버퍼로 미디어 데이타를 복사한다. 클립내의 데이타는 매체재생기에서 녹음 되면 늘어나고, getData(byte[] buf, int off, int len)로 줄어들게 된다. 클립내부의 데이 타가 전달한 버퍼보다 크면 버퍼크기만큼만 복사된다. 이 함수는 클립 타입이 "VOCODERDEVICES"에서 얻어진 타입일때 사용된다 Parameters:

### buf - 클립내부의 데이타가 복사될 버퍼

### off - 복사될 시작위치

### len - 복사될 크기

Returns:

### 복사된 크기

### availableDataSize

public int availableDataSize() 클립에서 이용가능한 데이타 크기(클립 내부버퍼 크기가 아님) Returns:

### 이용가능한 데이타 크기

### clearData

public void clearData() 클립내의 이용가능한 데이타를 모두 버린다.

### setPosition

public boolean setPosition(int ms) 재생을 시작을 위치를 설정한다. 재생위치 설정기능을 지원하지 않는 타입으로 생성된 클립에 이 함수를 호출할 경우, MediaUnsupportedException이 발생한다.

Parameters: ms - 클립 재생을 시작할 시작 시점(milli second) Returns: ture : 성공 false : 설정 실패

### getVolume

클립 재생기의 볼륨을 읽어온다. 클립 재생기의 독립적인 볼륨 설정을 지원할 경우, 이 함수는 클립 재생기의 볼륨을 읽어온다. 지원하지 않을 경우는, 클립생성 타입이 달라도 같은 볼륨소스를 가리킬 수 있다. 볼륨의 최소값은 0 이고, 최대값은 100이다.

Parameters: Returns: 성공 : 볼륨 값 (0-100 사이의 볼륨값)

### setVolume

public final boolean setVolume(int level) 클립 재생기의 볼륨을 설정한다. 클립 재생기의 독립적인 볼륨 설정을 지원할 경우, 이 함수는 클립 재생기의 볼륨을 설정한다. 지원하지 않을 경우는, 클립생성 타입이 달라도 같은 볼륨소스를 가리킬 수 있다. 설정할 볼륨의 최소값은 0 이고, 최대값은 100이다.

Parameters: level - 볼륨값 (0-100사이의 볼륨값)

### setListener

public void setListener(PlayListener listener) 클립 재생시 상태변화를 알려줄 listener를 등록한다.

Parameters: listener - 새로운 listener, 만일 null 이면 기존 것을 제거함

### playStart

protected void playStart(boolean repeat) Player.play(Clip clip, boolean repeat)메쏘드안에서 실제 재생함수를 부르기전 repeat 값을 매개변수로 불러준다.

Parameters: repeat - Player.play()에 전달된 repeat값

### playUpdate

public void playUpdate(int event, int parm) 클립 재생시 상태변화를 알린다. 전달되는 이벤트는 PlayListener.playUpdate()와 같다.

Parameters:

### event - 상태값

parm - 각 event에 추가 전달값이 있을 경우 사용
