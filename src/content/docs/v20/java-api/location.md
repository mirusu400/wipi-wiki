---
title: "3.1.10. 위치 정보"
---

---

## Class StationLocationInfo

```text
java.lang.Object
  +--org.kwis.msp.handset.StationLocationInfo
```

```java
public class StationLocationInfo extends java.lang.Object
```

기지국 방식에 의한 위치 정보를 제공 한다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 생성자 상세

없음

## 메서드 상세

### getBaseID

```java
public int getBaseID()
```

기지국 ID 를 읽어 온다

**반환 값**

기지국 ID

### getBaseLat

```java
public int getBaseLat()
```

기지국 위도를 읽어 온다

**반환 값**

기지국 위도

### getBaseLong

```java
public int getBaseLong()
```

기지국 경도를 읽어 온다

**반환 값**

기지국 경도

### isValid

```java
public boolean isValid()
```

기지국 위치 정보가 유효한지 여부를 읽어 온다

**반환 값**

true 일 때 유효, false 일때 무효

### getLocationInfo

```java
public final int getLocationInfo (void)
```

단말이 통신중인 기지국의 위치 정보를 요청하는 API 이다. 성공하면 class 의 baseID, baseLat, baseLong field 에 요청한 값이 저장 되고, stationInfoValid 가 true 가 된다.

**매개 변수**

없음

**반환 값**

정보의 획득에 성공하면 0 실패하면 exception 발생 Throws IOException 위치정보를 읽어오는데 실패 했을 때 발생

---

## Class GPSConfig

```text
java.lang.Object
  +--org.kwis.msp.handset.GPSConfig
```

```java
public class GPSConfig extends java.lang.Object
```

GPS 에 의한 위치 정보를 제공 한다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 생성자 상세

### GPSConfig

```java
public GPSConfig(int mode, int optimization, int qos, int transport, int pde_addr, int pde_port) throws IllegalArgumentException,
```

GPSException 주어진 GPS configuration 으로 GPS 장치를 초기화 하기 위하여 GPSConfig class 를 생성 한다.

**매개 변수**

- `mode` - gpsOne™ 위치정보 수신모드
- `optimization` - gpsOne™ 동작 최적화 방식
- `qos` - gpsOne™ 품질 수준
- `transport` - gpsOne™ 정보 전송 계층
- `pdeAddr` - PDE 서버 주소
- `pdePort` - PDE 서버 포트 Throws
- `IllegalArgumentException` - 주어진 configuration 값이 올바르지 않을 때 발생 필드 상세 설명 OPT_SPEED
- `public` - static final int OPT_SPEED 동작 최적화 설정을 속도로 설정한다. 값은 0 이다. OPT_ACCURACY
- `public` - static final int OPT_ACCURACY 동작 최적화 설정을 정확도로 설정한다. 값은 1 이다. SERVER_TCPIP
- `public` - static final int SERVER_TCPIP 동작 최적화 설정을 속도로 설정한다. 값은 0 이다. SERVER_DBURST
- `public` - static final int SERVER_DBURST 동작 최적화 설정을 정확도로 설정한다. 값은 1 이다. `MS_ASSISTED`
- `public` - static final int `MS_ASSISTED` 동작 최적화 설정을 속도로 설정한다. 값은 0 이다. `MS_BASED`
- `public` - static final int `MS_BASED` 동작 최적화 설정을 정확도로 설정한다. 값은 1 이다. 메쏘드 상세 설명 getMode

### getMode

```java
public int getMode()
```

gpsOne™ 위치 수신 모드를 읽어 온다

**반환 값**

gpsOne™ 위치 수신 모드

### getOptimization

```java
public int getOptimization()
```

gpsOne™ 동작 최적화 방식을 읽어 온다

**반환 값**

gpsOne™ 동작 최적화 방식

### getQos

```java
public int getQos()
```

gpsOne™ 품질 수준을 읽어 온다

**반환 값**

gpsOne™ 품질 수준

### getTransport

```java
public int getTransport()
```

gpsOne™ 정보 전송 계층을 읽어 온다

**반환 값**

gpsOne™ 정보 전송 계층

### getPdeAddr

```java
public int getPdeAddr()
```

PDE 서버 주소를 읽어 온다

**반환 값**

PDE 서버 주소

### getPdePort

```java
public int getPdePort()
```

PDE 서버 포트를 읽어 온다

**반환 값**

PDE 서버 포트

### setMode

```java
public static int setMode(int mode)
```

gpsOne™ 위치 수신 모드를 설정 한다. 이때 GPS 장치도 설정한 값으로 변경 된다.

**매개 변수**

- `mode` - gpsOne™ 위치 수신 모드

**반환 값**

성공시 0 Throws IllegalArgumentException 올바르지 않은 설정 값일 경우 GPSException GPS 장치 관련 오류 발생시

### setOptimization

```java
public static int setOptimization(int optimization)
```

gpsOne™ 동작 최적화 방식을 설정 한다. 이때 GPS 장치도 설정한 값으로 변경 된다.

**매개 변수**

- `optimization` - gpsOne™ 동작 최적화 방식

**반환 값**

성공시 0 Throws IllegalArgumentException 올바르지 않은 설정 값일 경우 GPSException GPS 장치 관련 오류 발생시

### setQos

```java
public static int setQos(int qos)
```

gpsOne™ 품질 수준을 설정 한다. 이때 GPS 장치도 설정한 값으로 변경 된다.

**매개 변수**

- `qos` - gpsOne™ 품질 수준

**반환 값**

성공시 0 Throws IllegalArgumentException 올바르지 않은 설정 값일 경우 GPSException GPS 장치 관련 오류 발생시

### setTransport

```java
public static int setTransport(int transport)
```

gpsOne™ 정보 전송 계층 을 설정 한다. 이때 GPS 장치도 설정한 값으로 변경 된다.

**매개 변수**

- `transport` - gpsOne™ 정보 전송 계층

**반환 값**

성공시 0 Throws IllegalArgumentException 올바르지 않은 설정 값일 경우 GPSException GPS 장치 관련 오류 발생시

### setPdeAddr

```java
public static int setPdeAddr (int pdeAddr)
```

PDE 서버 주소를 설정 한다. 이때 GPS 장치도 설정한 값으로 변경 된다.

**매개 변수**

- `pdeAddr` - PDE 서버 주소

**반환 값**

성공시 0 Throws IllegalArgumentException 올바르지 않은 설정 값일 경우 GPSException GPS 장치 관련 오류 발생시

### setPdePort

```java
public static int setPdePort (int pdePort)
```

PDE 서버 포트를 설정 한다. 이때 GPS 장치도 설정한 값으로 변경 된다.

**매개 변수**

- `pdePort` - PDE 서버 포트

**반환 값**

성공시 0 Throws IllegalArgumentException 올바르지 않은 설정 값일 경우 GPSException GPS 장치 관련 오류 발생시

---

## Class GPSLocationInfo

```text
java.lang.Object
  +--org.kwis.msp.handset.GPSLocationInfo
```

```java
public class GPSLocationInfo extends java.lang.Object
```

GPS 에 의한 위치 정보를 제공 한다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 메서드 상세

### getLatitude

```java
public int getLatitude()
```

GPS 위치정보의 위도 값을 읽어 온다

**반환 값**

위도 값

### getLongitude

```java
public int getLongitude()
```

GPS 위치정보의 경도 값을 읽어 온다

**반환 값**

경도 값

### getAltitude

```java
public int getAltitude()
```

GPS 위치정보의 고도 값을 읽어 온다

**반환 값**

고도 값

### getHeading

```java
public int getHeading ()
```

GPS 위치정보의 방향 값을 읽어 온다

**반환 값**

방향

### getHorizontalVelocity

```java
public int getHorizontalVelocity()
```

GPS 위치정보의 수평 속도 값을 읽어 온다

**반환 값**

수평 속도 값 getVerticalVelocity
```java
public int getVelocityVer()
```

GPS 위치정보의 수직 속도 값을 읽어 온다

**반환 값**

수직 속도 값

### getAccuracy

```java
public int getAccuracy()
```

GPS 위치정보의 정확도 값을 읽어 온다

**반환 값**

정확도 값

### getTimeStamp

```java
public String getTimeStamp()
```

GPS 위치정보의 타임스탬프 값을 읽어 온다

**반환 값**

타임스탬프 문자열

### isValid

```java
public int isValid()
```

GPS 정보(latitude, longitude, altitude, heading, velocityHor, velocityVer, accuracy, timeStamp 등) 가 유효한지의 여부. 초기값은 false 이며 GPS 정보를 올 바로 획득 했을 때 true로 설정된다.

**반환 값**

true 일 때 유효, false 일때 무효

---

## Class GPSProvider

```text
java.lang.Object
  +--org.kwis.msp.handset.GPSProvider
```

```java
public final class GPSProvider implements SystemEventListener
```

GPS 에 의한 위치 정보를 제공 한다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 필드 상세

REQUEST_ONCE public static final int REQUEST_ONCE GPS 위치 정보 조회를 1회 수행한다. 값은 0 이다. REQUEST_STOP public static final int REQUEST_STOP GPS 위치 정보 반복 조회를 정지한다. 값은 –1 이다.

## 메서드 상세

### available

```java
public int available(void)
```

GPS 장치가 사용 가능한지를 문의하는 API 이다.

**매개 변수**

없음

**반환 값**

성공시 0 Throws GPSException GPS 장치 관련 오류시 발생. 장치가 없거나 다른 app 가 사용중일 때

### requestLocationInfo

```java
public int requestLocationInfo(int repeat)
```

gpsOne 에 의한 위치 정보를 요청하는 API 이다. 이 API 는 asynchronous 하게 동작 하며, 그 결과는 EVENT 로 통보될 것이고, EVENT 가 왔을 때 getResult() 에 의해서 상세 정보를 얻어낼 수 있다. EVENT 는 LocationInfoListener 를 통해 전달 된다.

**매개 변수**

- `repeat` - GPS_REQUEST_STOP 시 반복 조회 정지, GPS_REQUEST_ONCE 일때 한번 요청, 1 이상의 숫자는 매 repeat 초마다 보고(가능한한)

**반환 값**

성공시 0 Throws IllegalArgumentException argument 가 올바르지 않을 때 GPSException GPS 장치 관련 오류시 발생시. 장치가 없거 나 다른 app 가 사용중, 사용자 인증 실패, 서버 접속 실패 등의 경우가 있음.

### getGPSConfig

```java
public static GPSConfig getGPSConfig (void)
```

gpsOne™ 설정 정보를 얻어온다.

**반환 값**

성공시 GPSConfig Throws GPSException GPS 장치 관련 오류 발생시

### setGPSConfig

```java
public static void setGPSConfig (GPSConfig config)
```

gpsOne™ 정보를 설정한다.

**매개 변수**

- `config` - GPSConfig Throws
- `GPSException` - GPS 장치 관련 오류 발생시 setLocationInfoListener

### setLocationInfoListener

```java
public static void setLocationInfoListener (GPSListener listener)
```

- `GPSListener` - 를 등록한다. 플랫폼에서 등록할 수 있는 listener는 1개로 제한 되며,
- `listener로` - 등록한 어플리케이션이 종료될때, listener가 해제 된다.

**매개 변수**

- `listener` - 등록할 GPSListener
- `Class` - GPSExceptionGPSException java.lang.Object | +--java.lang.Throwable | +--java.lang.Exception | +--org.kwis.msp.handset.GPSException
- `public` - class GPSException extends Exception
- `GPS` - 장치와 관련된 일반적인 예외 상황에서 발생한다.
- `Methods` - inherited from class java.lang.Throwable getMessage, printStackTrace, toString
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명 GPSException

### GPSException

```java
public GPSException(String str)
```

새 인스턴스를 메시지와 함께 생성한다.

**매개 변수**

- `message` - 예외에 대한 자세한 메시지. GPSException

### GPSException

```java
public GPSException()
```

새 GPSException 인스턴스를 생성한다.
- `Interface` - GPSListener
- `public` - interface GPSListener
- `GPS` - 정보가 수신 완료 된 경우 이벤트 발생을 알려주는 인터페이스이다. 메쏘드 상세 설명 LocationInfoReceived

### LocatinInfoReceived

```java
public void LocatinInfoReceived(GPSLocationInfo info)
```

- `GPS` - 이벤트가 발생하면 불린다.

**매개 변수**

- `info` - GPSLocationInfo 정보
