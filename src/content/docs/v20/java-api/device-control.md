---
title: "3.1.11. 부가 장치 제어"
---

---

## Class HandsetProperty

```text
java.lang.Object
  +--org.kwis.msp.handset.HandsetProperty
```

```java
public class HandsetProperty extends Object
```

단말기에 특화된 값들을 관리하는 클래스이다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 생성자 상세

### HandsetProperty

public HandsetProperty()

## 메서드 상세

### getSystemProperty

```java
public static String getSystemProperty (String id) throws IllegalArgumentException
```

단말기에 특화된 값을 읽어 온다. 패러미터로 올 수 있는 id문자열은 HAL문서 API중 `MH_sysGetInformation`()에서 사용하는 문자열에 준하고, 또한 각 이통사나 벤더에 따라 추가 확장될 수 있다.

**매개 변수**

- `id` - 특화된 값에 대한 식별 문자열

**반환 값**

특화된 값 Throws IllegalArgumentException 인식할 수 없는 식별 문자열 일 경우

### setSystemProperty

```java
public static boolean setSystemProperty(String id, String val) throws IllegalArgumentException
```

단말기에 특화된 값을 설정 한다. 패러미터로 올 수 있는 id문자열은 HAL문서 API중 `MH_sysSetInfortmaion`()에서 사용하는 문자열에 준하고, 또한 각 이통사나 벤더에 따라 추가 확장될 수 있다.

**매개 변수**

- `id` - 특화된 값에 대한 식별 문자열
- `val` - 설정 할 값.

**반환 값**

true 설정 성공 flase 설정에 실패할 경우 Throws IllegalArgumentException 인식할 수 없는 식별 문자열 일 경우

---

## Class BackLight

```text
java.lang.Object
  +--org.kwis.msp.handset.BackLight
```

```java
public class BackLight extends Object
```

LCD 의 백라이트를 조절하는 클래스이다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 메서드 상세

### on

```java
public static void on(int id, int color, int duration) throws IOException
```

백라이트를 제어하는 함수 이다. 단말기에서 초기에 설정된 백라이트 설정이 존재 한다. 이 설정된 값은 키가 눌려 질 때 몇 초 동안 그 상태를 유지 하게 되어 있다. 이 함수는 그 설정된 값을 무효화 시켜야 하며 어플리케이션에서 사용 후 원 상태로 돌리고 싶다면 before()함수를 호출한다. 타임아웃 되면 Backlight는 자동으로 꺼진 다. 백라이트 번호는 0 이면 주 LCD 의 백라이트이고 1 이면 보조 LCD 의 백라이트 를 가리킨다. 만약 백라이트가 색상을 지정할 수 있을 경우 색상은 매개변수 color 로 지정하는데 color 값의 형식은 0xYYRRGGBB(네트웍 바이트 순서(network byte ordering)이다) 형태이다. 여기서 YY 는 무시되면 RR 은 빨강(Red), GG 는 녹색 (Green), BB 는 파랑(Blue) 범위를 지정한다

**매개 변수**

- `id` - 백라이트 번호
- `color` - 백라이트 색상
- `duration` - 백라이트가 켜져 있는 시간을 (msec 단위로)설정한다. Throws
- `IOException` - 에러 발생시 off

### off

```java
public static void off() throws IOException
```

백라이트를 끈다. Throws
- `IOException` - 에러 발생시 before

### before

```java
public static void before() throws IOException
```

백라이트를 프로그램 실행 이전 상태로 유지한다. Throws
- `IOException` - 에러 발생시 alwaysOn

### alwaysOn

```java
public static void alwaysOn() throws IOException
```

백라이트를 계속해서 킨다. Throws
- `IOException` - 에러 발생시
- `Class` - Call java.lang.Object | +--org.kwis.msp.handset.Call
- `public` - class Call extends Object 전화 통화에 관련된 클래스이다.
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 생성자 상세 설명 Call

### Call

```java
public Call()
```

메쏘드 상세 설명 accept

### accept

```java
public static void accept() throws IOException
```

걸려온 전화를 받다. Throws
- `IOException` - 응용 프로그램 관리자 이외의 프로그램에서 불릴 경우나 기타 에러 발생시 던져진다. reject

### reject

```java
public static void reject() throws IOException
```

걸려온 전화를 거부한다. Throws
- `IOException` - 응용 프로그램 관리자 이외의 프로그램에서 불릴 경우나 기타 에러 발생시 던져진다. end

### end

```java
public static void end() throws IOException
```

전화 거는 중 혹은 현재 통화하고 있는 중에 통화를 종료 한다 Throws
- `IOException` - 응용 프로그램 관리자 이외의 프로그램에서 불릴 경우나 기타 에러 발생시 던져진다. place

### place

```java
public static void place(String phonenumber) throws IOException
```

전화를 건다.

**매개 변수**

- `phonenumber` - 전화번호 Throws
- `IOException` - 응용 프로그램 관리자 이외의 프로그램에서 불릴 경우나 기타 에러 발생시 던져진다.
- `Class` - LED java.lang.Object | +--org.kwis.msp.handset.LED
- `public` - class LED extends Object LED(Light Emitting Diodes) 를 조절하는 클래스이다.
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 생성자 상세 설명 LED

### LED

```java
public LED()
```

메쏘드 상세 설명 getCount

### getCount

```java
public static int getCount() throws IOException
```

시스템의 LED 개수를 리턴한다. Throws
- `IOException` - 에러 발생시 set

### set

```java
public static int set(int leds) throws IOException
```

- `LED` - on/off를 설정한다. 각bit가 1이면 on, 0이면 off를 나타낸다. 예) 외장 LED가 4개 존재한다면 LSB BIT 부터 4개를 사용한다. 31 bit ... 0 ... set(0x3) 0번, 1번 led 2개를 켜고, 2번, 3번 led 두개를 끈다. 단, 칼라가 지원되는 단말기인 경우 단말회사가 설정한 가장 밝은 값으로 설정된다.

**매개 변수**

- `leds` - 비트가 1 이면 해당 LED 가 on 되고 0 이면 off 된다.

**반환 값**

설정된 값 Throws IOException 에러 발생시

### get

```java
public static int get() throws IOException
```

LED의 on/off상태를 읽어온다

**반환 값**

각 led의 on/off상태의 bit OR값 Throws IOException 에러 발생시

### getSupportColor

```java
public static int[] getSupportColor(int led) throws IOException
```

단말기에서 해당 led가 제공하는 칼라 목록을 가지고 온다.

**매개 변수**

- `led` - 제어할 led

**반환 값**

제공하는 칼라 목록 Throws IOException 에러 발생시

### getColor

```java
public static int getColor(int led) throws IOException
```

현재 해당 led에 지정되어 있는RGB 값을 가져온다.

**매개 변수**

- `led` - 제어할 led

**반환 값**

RGB값 Throws IOException 에러 발생시

### setColor

```java
public static int setColor(int led, int rgb) throws IOException
```

단말기에서 해당 led에 RGB 값을 지정한다. 단, 인자로 받은 RGB값이 없을 경우 근 사값으로 설정된다.

**매개 변수**

- `led` - 제어할 led
- `rgb` - RGB값

**반환 값**

설정된 RGB 값 Throws IOException 에러 발생시 3.2. MIDP MIDP 규격은 Sun Microsystems사의 규격 2.0을 기준으로 동일한 기능을 제공해야 한다. 참조 웹사이트 : http://jcp.org/aboutJava/communityprocess/final/jsr118/index.html 4. 확장 유니 코드
