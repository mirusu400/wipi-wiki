# Class Manager

`package javax.microedition.media`

```text
java.lang.Object
  |
  +--javax.microedition.media.Manager
```

## 설명

**extends Object:**

`Manager`는 멀티미디어를 처리하는 
`Player`와 같은 시스템 종속 자원을 얻기 위한 
액세스 포인트입니다.

`Player`는 
데이터의 
내용 유형에 
적합한 미디어를 
제어하고 렌더링하는 데 
사용하는 객체입니다.

`Manager`에서는 `Player`를 
구성하기 위한 구현별 기법에 액세스할 수 있습니다.

편의상 `Manager`는 단순 톤을 생성하기 위한 
간소화된 메소드도 제공합니다.

**See Also:**
- ``Player``

## 필드 요약

- `static String TONE_DEVICE_LOCATOR` — 톤 시퀀스를 재생하기 위한 톤 Player 를 만드는 로케이터.

## 메서드 요약

- `static Player createPlayer ( InputStream stream, String type)` — InputStream 에서 미디어를 재생하기 위해 Player 를 만듭니다.
- `static Player createPlayer ( String locator)` — 입력 로케이터에서 Player 를 만듭니다.
- `static String [] getSupportedContentTypes ( String protocol)` — 주어진 프로토콜에 대해 지원되는 내용 유형 목록을 반환합니다.
- `static String [] getSupportedProtocols ( String content_type)` — 제공된 내용 유형을 지원하는 프로토콜의 목록을 반환합니다.
- `static void playTone (int note, int duration, int volume)` — 음표와 재생 시간에 의해 지정된 대로 톤을 재생합니다.

## 필드 상세

### TONE_DEVICE_LOCATOR

```java
public static final String TONE_DEVICE_LOCATOR
```

**See Also:**
- `Constant Field Values`

### getSupportedContentTypes

```java
public static String[] getSupportedContentTypes(String protocol)
```

**Parameters:**
- `protocol` - 지원되는 내용 유형의 입력 프로토콜

**Returns:**
- 주어진 프로토콜을 지원하는 내용 유형 목록

### getSupportedProtocols

```java
public static String[] getSupportedProtocols(String content_type)
```

**Parameters:**
- `content_type` - 지원되는 프로토콜의 내용 유형

**Returns:**
- 주어진 내용 유형을 지원하는 프로토콜 목록

### createPlayer

```java
public static Player createPlayer(String locator)
                           throws IOException,
                                  MediaException
```

**Parameters:**
- `locator` - 미디어 내용을 설명하는 
URI 구문의 로케이터 문자열

**Returns:**
- 새 `Player`

**Throws:**
- `SecurityException` - 호출자에게 `Player`를 
만들 보안 권한이 없는 경우 발생합니다.

### createPlayer

```java
public static Player createPlayer(InputStream stream,
                                  String type)
                           throws IOException,
                                  MediaException
```

**Parameters:**
- `type` - 미디어의 `ContentType`

**Returns:**
- 새 `Player`

**Throws:**
- `SecurityException` - 호출자에게 `Player`를 
만들 보안 권한이 없는 경우 발생합니다.

### playTone

```java
public static void playTone(int note,
                            int duration,
                            int volume)
                     throws MediaException
```

**Parameters:**
- `volume` - 오디오 볼륨은 
0 ~ 100 사이입니다.
100은 현재 하드웨어 수준에서 최대 볼륨을 표시합니다. 
볼륨을 0 미만의 값으로 설정하면 볼륨은 0으로 설정됩니다. 
볼륨을 100보다 큰 값으로 설정하면 
볼륨은 100으로 설정됩니다.

**Throws:**
- `MediaException` - 장치 관련 문제로 인해 톤을 재생할 수 없는 경우 
발생합니다.

## 메서드 상세

### getSupportedContentTypes

```java
public static String[] getSupportedContentTypes(String protocol)
```

**Parameters:**
- `protocol` - 지원되는 내용 유형의 입력 프로토콜

**Returns:**
- 주어진 프로토콜을 지원하는 내용 유형 목록

### getSupportedProtocols

```java
public static String[] getSupportedProtocols(String content_type)
```

**Parameters:**
- `content_type` - 지원되는 프로토콜의 내용 유형

**Returns:**
- 주어진 내용 유형을 지원하는 프로토콜 목록

### createPlayer

```java
public static Player createPlayer(String locator)
                           throws IOException,
                                  MediaException
```

**Parameters:**
- `locator` - 미디어 내용을 설명하는 
URI 구문의 로케이터 문자열

**Returns:**
- 새 `Player`

**Throws:**
- `SecurityException` - 호출자에게 `Player`를 
만들 보안 권한이 없는 경우 발생합니다.

### createPlayer

```java
public static Player createPlayer(InputStream stream,
                                  String type)
                           throws IOException,
                                  MediaException
```

**Parameters:**
- `type` - 미디어의 `ContentType`

**Returns:**
- 새 `Player`

**Throws:**
- `SecurityException` - 호출자에게 `Player`를 
만들 보안 권한이 없는 경우 발생합니다.

### playTone

```java
public static void playTone(int note,
                            int duration,
                            int volume)
                     throws MediaException
```

**Parameters:**
- `volume` - 오디오 볼륨은 
0 ~ 100 사이입니다.
100은 현재 하드웨어 수준에서 최대 볼륨을 표시합니다. 
볼륨을 0 미만의 값으로 설정하면 볼륨은 0으로 설정됩니다. 
볼륨을 100보다 큰 값으로 설정하면 
볼륨은 100으로 설정됩니다.

**Throws:**
- `MediaException` - 장치 관련 문제로 인해 톤을 재생할 수 없는 경우 
발생합니다.
