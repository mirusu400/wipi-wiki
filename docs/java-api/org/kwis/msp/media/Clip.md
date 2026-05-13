# Class Clip

`package org.kwis.msp.media`

```
java.lang.Object
  |
  +--org.kwis.msp.media.Clip
```

## 설명

**extends Object:**

이 클래스는 Player에 의해 재생되는 클립을 구현한다.

## 필드 요약

- `protected  byte[] buf`
- `protected  int bufLength`
- `protected  int[] duration`
- `protected  int eventParm`
- `protected  int front`
- `protected  int[] hiFreq`
- `protected  boolean isNotifyWM`
- `protected  int left`
- `protected  int[] lowFreq`
- `protected  int magicID`
- `protected  int playerID`
- `protected  int prgID`
- `protected  int rear`
- `protected  int[] tone`
- `protected  int waterMarkLength`

## 생성자 요약

- Clip ( String type) 특정 타입의 클립을 생성한다.
- Clip ( String type,
 byte[] buf) 이미 데이타가 저장되어 있는 매개변수를 받아들여 클립을 생성한다.
- Clip ( String type,
 int bufSize) 특정 타입의 CLIP을 생성한다.
- Clip ( String type, String resourceName)

## 메서드 요약

- `protected  void atomicGetUpdate (int getSize)`
- `protected  void atomicPutUpdate (int putSize)`
- `int availableDataSize ()` — 클립에서 이용가능한 데이타 크기(클립 내부버퍼 크기가 아님)
- `void clearData ()` — 클립내의 이용가능한 데이타를 모두 버린다.
- `protected static int control (int playerID, int cmd, Object buf1, Object buf2)` — HAL단의 MH_mdaControl()에 연결되는 함수이다.
- `int getData (byte[] buf, int off, int len)` — 클립에서 buf로 미디어 데이타를 복사한다.
- `protected  int getPlayerID ( String type)`
- `String getType ()` — 클립의 Type을 구한다.
- `int getVolume ()` — 클립 재생기의 볼륨을 읽어온다.
- `protected  int mediaFreeze ()`
- `protected  int mediaReadData ()`
- `protected  int mediaWriteData ()`
- `protected  boolean playStart (boolean repeat)` — Player.play(Clip clip, boolean repeat)메쏘드안에서 실제 재생함수를 부르기전 repeat값을 매개변수로 불러준다.
- `boolean playUpdate (int event, int parm)` — 클립 재생시 상태변화를 알린다.
- `int putData (byte[] buf, int off, int len)` — 클립에 미디어 데이타를 복사한다.
- `protected  boolean recordStart ()` — Player.record(Clip clip)메쏘드안에서 실제 record함수를 부르기전 불러준다.
- `boolean setBuffer (byte[] buf, int dataSize)` — 클립의 내부버퍼을 설정한다.
- `void setListener ( PlayListener listener)` — 클립 재생시 상태변화를 알려줄 listener를 등록한다.
- `boolean setPosition (int ms)` — 재생을 시작할 위치를 설정한다.
- `boolean setVolume (int level)` — 클립 재생기의 볼륨을 설정한다.

## 필드 상세

### prgID

```java
protected int prgID
```

### playerID

```java
protected int playerID
```

### buf

```java
protected byte[] buf
```

### tone

```java
protected int[] tone
```

### hiFreq

```java
protected int[] hiFreq
```

### lowFreq

```java
protected int[] lowFreq
```

### duration

```java
protected int[] duration
```

### bufLength

```java
protected int bufLength
```

### left

```java
protected int left
```

### front

```java
protected int front
```

### rear

```java
protected int rear
```

### waterMarkLength

```java
protected int waterMarkLength
```

### isNotifyWM

```java
protected boolean isNotifyWM
```

### magicID

```java
protected int magicID
```

### eventParm

```java
protected int eventParm
```

### Clip

```java
public Clip(String type,
            int bufSize)
```

**Parameters:**
- `bufSize` - 클립내부에 생성될 버퍼의 크기(바이트 단위)

### Clip

```java
public Clip(String type)
```

**Parameters:**
- `type` - 리소스 타입

### Clip

```java
public Clip(String type,
            byte[] buf)
```

**Parameters:**
- `buf` - 데이타가 들어 있는 버퍼

### Clip

```java
public Clip(String type,
            String resourceName)
```

### getPlayerID

```java
protected int getPlayerID(String type)
```

### atomicPutUpdate

```java
protected void atomicPutUpdate(int putSize)
```

### mediaWriteData

```java
protected int mediaWriteData()
```

### atomicGetUpdate

```java
protected void atomicGetUpdate(int getSize)
```

### mediaReadData

```java
protected int mediaReadData()
```

### mediaFreeze

```java
protected int mediaFreeze()
```

### control

```java
protected static int control(int playerID,
                             int cmd,
                             Object buf1,
                             Object buf2)
```

- HAL단의 MH_mdaControl()에 연결되는 함수이다.
함수의 의미는 이통사나 제조사에 따른다.

### setBuffer

```java
public boolean setBuffer(byte[] buf,
                         int dataSize)
```

**Parameters:**
- `dataSize` - 버퍼안에 들어있는 데이타 크기

**Returns:**
- true : 버퍼 설정 성공
 
false : 이미 버퍼가 설정되어 있음

### putData

```java
public int putData(byte[] buf,
                   int off,
                   int len)
```

**Parameters:**
- `len` - 복사할 크기

**Returns:**
- 복사된 크기

### getData

```java
public int getData(byte[] buf,
                   int off,
                   int len)
```

**Parameters:**
- `len` - 복사될 크기

**Returns:**
- 복사된 크기

### availableDataSize

```java
public int availableDataSize()
```

**Returns:**
- 이용가능한 데이타 크기

### clearData

```java
public void clearData()
```

- 클립내의 이용가능한 데이타를 모두 버린다.

### getType

```java
public String getType()
```

**Returns:**
- Type 문자열

### setPosition

```java
public boolean setPosition(int ms)
```

**Parameters:**
- `ms` - 클립 재생을 시작할 시작 시점(milli second)

**Returns:**
- ture : 성공
 
false : 설정 실패

### getVolume

```java
public final int getVolume()
```

**Returns:**
- 성공 : 볼륨 값(0-100사이의 볼륨값)

### setVolume

```java
public final boolean setVolume(int level)
```

**Parameters:**
- `level` - 볼륨값

### setListener

```java
public void setListener(PlayListener listener)
```

**Parameters:**
- `listener` - 새로운 listener, 만일 null 이면 기존 것을 제거함

### playStart

```java
protected boolean playStart(boolean repeat)
```

**Parameters:**
- `repeat` - Player.play()에 전달된 repeat값

### recordStart

```java
protected boolean recordStart()
```

**Returns:**
- true : Player.record()함수 수행이 정상적으로 수행됨
 
false : Player.record()함수가 더이상 수행되지 않고 false로 반환됨

### playUpdate

```java
public boolean playUpdate(int event,
                          int parm)
```

**Parameters:**
- `parm` - 각 event에 추가 전달값이 있을 경우 사용

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 생성자 상세

### Clip

```java
public Clip(String type,
            int bufSize)
```

**Parameters:**
- `bufSize` - 클립내부에 생성될 버퍼의 크기(바이트 단위)

### Clip

```java
public Clip(String type)
```

**Parameters:**
- `type` - 리소스 타입

### Clip

```java
public Clip(String type,
            byte[] buf)
```

**Parameters:**
- `buf` - 데이타가 들어 있는 버퍼

### Clip

```java
public Clip(String type,
            String resourceName)
```

### getPlayerID

```java
protected int getPlayerID(String type)
```

### atomicPutUpdate

```java
protected void atomicPutUpdate(int putSize)
```

### mediaWriteData

```java
protected int mediaWriteData()
```

### atomicGetUpdate

```java
protected void atomicGetUpdate(int getSize)
```

### mediaReadData

```java
protected int mediaReadData()
```

### mediaFreeze

```java
protected int mediaFreeze()
```

### control

```java
protected static int control(int playerID,
                             int cmd,
                             Object buf1,
                             Object buf2)
```

- HAL단의 MH_mdaControl()에 연결되는 함수이다.
함수의 의미는 이통사나 제조사에 따른다.

### setBuffer

```java
public boolean setBuffer(byte[] buf,
                         int dataSize)
```

**Parameters:**
- `dataSize` - 버퍼안에 들어있는 데이타 크기

**Returns:**
- true : 버퍼 설정 성공
 
false : 이미 버퍼가 설정되어 있음

### putData

```java
public int putData(byte[] buf,
                   int off,
                   int len)
```

**Parameters:**
- `len` - 복사할 크기

**Returns:**
- 복사된 크기

### getData

```java
public int getData(byte[] buf,
                   int off,
                   int len)
```

**Parameters:**
- `len` - 복사될 크기

**Returns:**
- 복사된 크기

### availableDataSize

```java
public int availableDataSize()
```

**Returns:**
- 이용가능한 데이타 크기

### clearData

```java
public void clearData()
```

- 클립내의 이용가능한 데이타를 모두 버린다.

### getType

```java
public String getType()
```

**Returns:**
- Type 문자열

### setPosition

```java
public boolean setPosition(int ms)
```

**Parameters:**
- `ms` - 클립 재생을 시작할 시작 시점(milli second)

**Returns:**
- ture : 성공
 
false : 설정 실패

### getVolume

```java
public final int getVolume()
```

**Returns:**
- 성공 : 볼륨 값(0-100사이의 볼륨값)

### setVolume

```java
public final boolean setVolume(int level)
```

**Parameters:**
- `level` - 볼륨값

### setListener

```java
public void setListener(PlayListener listener)
```

**Parameters:**
- `listener` - 새로운 listener, 만일 null 이면 기존 것을 제거함

### playStart

```java
protected boolean playStart(boolean repeat)
```

**Parameters:**
- `repeat` - Player.play()에 전달된 repeat값

### recordStart

```java
protected boolean recordStart()
```

**Returns:**
- true : Player.record()함수 수행이 정상적으로 수행됨
 
false : Player.record()함수가 더이상 수행되지 않고 false로 반환됨

### playUpdate

```java
public boolean playUpdate(int event,
                          int parm)
```

**Parameters:**
- `parm` - 각 event에 추가 전달값이 있을 경우 사용

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 메서드 상세

### getPlayerID

```java
protected int getPlayerID(String type)
```

### atomicPutUpdate

```java
protected void atomicPutUpdate(int putSize)
```

### mediaWriteData

```java
protected int mediaWriteData()
```

### atomicGetUpdate

```java
protected void atomicGetUpdate(int getSize)
```

### mediaReadData

```java
protected int mediaReadData()
```

### mediaFreeze

```java
protected int mediaFreeze()
```

### control

```java
protected static int control(int playerID,
                             int cmd,
                             Object buf1,
                             Object buf2)
```

- HAL단의 MH_mdaControl()에 연결되는 함수이다.
함수의 의미는 이통사나 제조사에 따른다.

### setBuffer

```java
public boolean setBuffer(byte[] buf,
                         int dataSize)
```

**Parameters:**
- `dataSize` - 버퍼안에 들어있는 데이타 크기

**Returns:**
- true : 버퍼 설정 성공
 
false : 이미 버퍼가 설정되어 있음

### putData

```java
public int putData(byte[] buf,
                   int off,
                   int len)
```

**Parameters:**
- `len` - 복사할 크기

**Returns:**
- 복사된 크기

### getData

```java
public int getData(byte[] buf,
                   int off,
                   int len)
```

**Parameters:**
- `len` - 복사될 크기

**Returns:**
- 복사된 크기

### availableDataSize

```java
public int availableDataSize()
```

**Returns:**
- 이용가능한 데이타 크기

### clearData

```java
public void clearData()
```

- 클립내의 이용가능한 데이타를 모두 버린다.

### getType

```java
public String getType()
```

**Returns:**
- Type 문자열

### setPosition

```java
public boolean setPosition(int ms)
```

**Parameters:**
- `ms` - 클립 재생을 시작할 시작 시점(milli second)

**Returns:**
- ture : 성공
 
false : 설정 실패

### getVolume

```java
public final int getVolume()
```

**Returns:**
- 성공 : 볼륨 값(0-100사이의 볼륨값)

### setVolume

```java
public final boolean setVolume(int level)
```

**Parameters:**
- `level` - 볼륨값

### setListener

```java
public void setListener(PlayListener listener)
```

**Parameters:**
- `listener` - 새로운 listener, 만일 null 이면 기존 것을 제거함

### playStart

```java
protected boolean playStart(boolean repeat)
```

**Parameters:**
- `repeat` - Player.play()에 전달된 repeat값

### recordStart

```java
protected boolean recordStart()
```

**Returns:**
- true : Player.record()함수 수행이 정상적으로 수행됨
 
false : Player.record()함수가 더이상 수행되지 않고 false로 반환됨

### playUpdate

```java
public boolean playUpdate(int event,
                          int parm)
```

**Parameters:**
- `parm` - 각 event에 추가 전달값이 있을 경우 사용

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
