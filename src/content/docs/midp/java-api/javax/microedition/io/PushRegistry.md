---
title: "Class PushRegistry"
---

`package javax.microedition.io`

```text
java.lang.Object
  |
  +--javax.microedition.io.PushRegistry
```

## 설명

**extends Object:**

`PushRegistry`는 인바운드 
연결 목록을 유지 관리합니다. 
응용 프로그램은 응용 프로그램 설명자 파일의 항목을 사용하거나 
`registerConnection` 메소드를 호출하여 동적으로 
인바운드 연결을 등록할 수 있습니다.

응용 프로그램은 실행되는 동안 인바운드 연결과 관련된 
모든 I/O 작업을 책임집니다. 
응용 프로그램을 실행하고 있지 않으면 
응용 프로그램 관리 소프트웨어(AMS)가 인바운드 알림 요청을 수신합니다. 
등록된 `MIDlet`에 대한 알림이 도착하면 
AMS는 `MIDlet.startApp` 메소드의 정상적 호출을 통해 
`MIDlet`을 
시작합니다.

### 선언된 연결 설치 처리

인바운드 일반 연결에서의 충돌을 피하려면 
`MIDlet` Suite에 필요한 정적 연결 정보가 
응용 프로그램 설명자 파일에 있어야 합니다. 

응용 프로그램 설명자에 있는 모든 정적 푸시 선언을 설치 중에 
이행할 수 없는 경우 사용자에게 충돌이 있으며 MIDlet Suite를 설치해서는 
안 된다고 알려야 합니다. 
(충돌 발생 시 보고되는 오류에 대해서는 
*Over The Air User Initiated Provisioning 사양*을 
참조하십시오.) 

선언을 이행할 수 없는 경우에는 
푸시 속성의 구문 오류, 
장치에서 이미 예약된 연결 종점에 대한 선언(예: 포트 번호), 장치에서 
푸시에 지원되지 않는 프로토콜에 대한 선언, 동일한 
응용 프로그램 설명자의 
`MIDlet-<n>` 속성에 
나열되지 않은 `MIDlet` 
클래스를 참조하는 선언 등이 있습니다. 

`MIDlet` Suite는 
푸시 등록을 이행할 수 없는 경우에도 
정상적으로 작동할 수 있을 경우 `PushRegistry`의 
동적 등록 메소드를 사용하여 푸시 연결을 등록해야 합니다.

충돌 없이 설치하면 요청된 각 연결은 Suite의 
`MIDlets` 전용으로 예약됩니다. 
Suite를 설치하는 동안 다른 
응용 프로그램이 예약된 연결 중 
하나를 열려고 시도하면 
`IOException`이 발생하며 실패합니다. 
Suite에 이미 열려 있는 연결이 없을 경우 
`MIDlet`에서 Suite에 예약된 연결에 대해 
`Connector.open()`을 
호출하면 항상 성공합니다.

두 개의 `MIDlet` Suite가 정적 푸시 연결을 
공유하면 함께 설치할 수 없으며 둘 다 정상적으로 작동합니다. 
일반적으로 최종 사용자가 다른 Suite를 성공적으로 설치할 수 있으려면 
먼저 기존 Suite를 제거해야 합니다.

### 푸시 등록 속성

각각의 푸시 등록 항목에는 다음 정보가 포함됩니다.

```java
MIDlet-Push-<n>: <ConnectionURL>, 
<MIDletClassName>, <AllowedSender>
```

 여기서 각 구성 요소가 의미하는 바는 다음과 같습니다.

- `MIDlet-Push-<n>` = 푸시 등록 속성 이름. 
`MIDlet` Suite 하나에서 
여러 푸시 등록을 제공할 수 있습니다. 
<n>의 숫자 값은 1부터 시작하며 추가 항목에 연속되는 서수를 
사용해야 합니다. 
첫 번째 누락된 항목이 발견되면 목록이 
종료되고 모든 추가 항목은 무시됩니다.
- `ConnectionURL` = `Connector.open()`에 
사용된 연결 문자열
- `MIDletClassName` = 연결을 책임지는 
`MIDlet`. 명명된 `MIDlet`을 
설명자 파일이나 `MIDlet-<n>` 레코드가 있는 
jar 파일 상세 목록에서 등록해야 합니다. 
(이 정보는 푸시 연결이 감지되거나 사용자가 
응용 프로그램에 대한 권한을 부여/취소할 때 
응용 프로그램에 대한 메시지를 
사용자에게 표시하는 데 필요합니다.) 
명명된 `MIDlet`이 Suite에 두 번 이상 나타나면 
처음 일치하는 항목이 사용됩니다.
- `AllowedSender` = 요청된 
`MIDlet`을 시작할 수 있는 보낸 사람을 제한하는 지정된 필터. 

`AllowedSender` 필드의 구문과 의미는 
프로토콜에 사용된 주소 지정 형식에 따라 달라집니다. 

하지만 이 필드의 모든 구문은 와일드카드 문자 "*"와 "?" 사용을 지원해야 합니다. 
와일드카드의 의미는 다음과 같습니다.

"*"는 빈 문자열을 포함하여 모든 문자열과 일치합니다.
"?" 는 모든 단일 문자와 일치합니다.

이 필드 값이 와일드카드 문자 "*"로만 이루어져 있으면 
모든 소스로부터의 연결이 승인됩니다. 

`datagram` 및 `socket` URL
(플랫폼에서 지원되는 경우)을 사용한 푸시 속성의 경우, 
이 필드에는 IPv4와 IPv6에 대해 해당 URL에 사용되는 것과 
동일한 형식의 숫자 IP 주소가 포함됩니다. 
IP 주소에 와일드카드를 사용할 수도 있습니다. 

예를 들어, "129.70.40.*"는 서브넷 확인을 허용합니다. 
포트 번호는 `datagram` 및 
`socket` 연결 필터에 
포함되지 않습니다.

MIDP 2.0 사양에서는 `datagram` 및 
`socket` 인바운드 연결 구문을 정의합니다. 
다른 사양에서 추가 연결 유형에 대한 
푸시 의미를 정의할 경우 
필터 필드의 예상 구문과 연결 
URL 문자열의 예상 형식도 정의해야 합니다.

다음은 포트 79에 스트림 소켓을, 포트 50000에 데이터그램 연결을 
예약하는 샘플 설명자 파일입니다. 
(포트 번호는 IANA에서 유지 관리되며 
잘 알려진 사용자 등록 및 
동적 포트 번호를 다룹니다.) 
[[IANA Port Number Registry](http://www.iana.org/numbers.html#P) 참조]

### 버퍼된 메시지

메시지 버퍼링에 대한 요구 사항은 
푸시에 사용된 프로토콜에 따라 다르며 
각 프로토콜에 대해 별도로 정의됩니다. 
버퍼링과 관련하여 모든 프로토콜에 
적용되는 일반 요구 사항은 없습니다. 
구현 시 메시지를 버퍼할 경우 `MIDlet`을 시작하고 
푸시에 등록된 관련 `Connection`이 열릴 때 
`MIDlet`에 이 메시지를 제공해야 합니다.

데이터그램 연결이 푸시에 지원되면 구현 시 
데이터그램 푸시에 등록된 `MIDlet`이 
수신 데이터그램에 대한 응답으로 시작될 때 
최소한 `MIDlet`을 시작하게 한 데이터그램은 구현 시 버퍼되어, 
`MIDlet`이 시작 후 `UDPDatagramConnection`을 
열 때 `MIDlet`이 
사용할 수 있도록 해야 합니다.

소켓 연결이 푸시에 지원되면 
구현 시 소켓 푸시에 등록된 
`MIDlet`가 수신 소켓 연결에 대한 
응답으로 시작될 때 
연결이 시간 초과되지 않았을 경우 `MIDlet`이 시작 후 
`ServerSocketConnection`을 열어 
이 연결을 승인할 수 있도록 해야 합니다.

### 연결 및 푸시 등록 지원

모든 일반 연결이 푸시 응용 프로그램 전송으로 
사용하기에 적합한 것은 아닙니다. 
어떤 프로토콜이 인바운드 연결 유형으로 장치에서 지원된다고 해서 
반드시 유효한 푸시 기법으로 사용 가능하게 할 필요는 없습니다. 
예를 들어, 어떤 플랫폼은 `MIDlet`에서 
서버 소켓 연결을 지원하지만 인바운드 소켓 연결에 대한 푸시 시작 기능을 
지원하지 않을 수도 있습니다. 
플랫폼이 이 선택 기능을 지원하지 않으면 
`registerConnection` 및 
`registerAlarm` 메소드에서 
`ConnectionNotFoundException`이 발생합니다.

### AMS 연결 전달

등록된 푸시 연결에 대한 책임은 인바운드 연결에 대한 
I/O 작업을 처리하는 
`MIDlet`과 AMS가 공유합니다. 
데이터 손실을 방지하기 위해 한 응용 프로그램이 
`Connector.open()` 호출 시부터 
`Connection.close()` 호출 시까지 
연결에 대한 모든 I/O 작업을 책임집니다.

AMS는 인바운드 연결 알림을 수신합니다. 
새로운 인바운드 데이터를 찾는 
원시 콜백 또는 폴링 기법을 통해 
이 작업을 처리할 수도 있습니다. 
AMS는 `PushRegistry 보안`을 
시행하고 MIDlet Suite를 호출하기 전에 알림(있는 경우)을 
사용자에게 제공할 책임이 있습니다.

AMS는 푸시 `MIDlet` 메소드를 호출하기 전에 
실행 중인 모든 응용 프로그램을 
종료해야 합니다(필요한 경우).

AMS가 푸시 응용 프로그램을 시작한 후 
`MIDlet`은 연결을 열어야 하며 
이후의 모든 I/O 작업을 책임집니다. 
차단 I/O 작업을 수행해야 하는 응용 프로그램은 
대화식 사용자 작업을 허용하는 
별도의 스레드를 사용하는 것이 좋습니다. 
응용 프로그램을 시작하고 
연결이 열리면 AMS는 해당 연결에 대한 
푸시 알림을 수신할 필요가 없습니다. 
응용 프로그램이 모든 인바운드 
데이터 읽기를 책임집니다.

응용 프로그램은 모든 인바운드 데이터에 대해 작업을 마친 후 
해당 연결에 대해 `close()`를 호출할 수도 있습니다. 
연결이 닫히면 AMS와 응용 프로그램 
모두 푸시 알림을 수신하지 않습니다. 
응용 프로그램이 모든 데이터가 
수신되기 전에 연결을 닫으면 
인바운드 데이터가 손실될 수 있습니다.

응용 프로그램이 삭제되면 AMS가 인바운드 
연결을 감시할 책임을 다시 맡습니다.

푸시 응용 프로그램은 푸시 기법을 통해 
비동기 데이터를 처리할 때 
예상 가능한 방식으로 작동하는 것이 좋습니다. 
응용 프로그램은 데이터가 처리되었음을 사용자에게 알리는 것이 좋습니다. 
(사용자에게 보이는 인터페이스를 사용하지 않는 응용 프로그램을 작성할 수는 
있지만 이렇게 할 경우 최종 사용자가 백그라운드 기능만 수행하는 
응용 프로그램을 시작하게 되므로 
혼란을 줄 수 있습니다.)

### 실행 중인 MIDlet에서 등록된 동적 연결

IANA에 등록된 잘 알려진 포트를 
정의할 필요가 없는 경우도 있습니다. 
간단한 응용 프로그램은 `MIDlet`과 서버 응용 프로그램 사이에 
개인 프로토콜을 사용하여 데이터를 교환할 수도 있습니다.

이러한 유형의 응용 프로그램을 수용하기 위해 
동적으로 연결을 할당하고, 응용 프로그램이 설치된 경우 알려진 정보처럼 
해당 정보를 등록하는 기법이 제공됩니다. 
이 정보는 네트워크 상의 에이전트로 전송되어 
등록된 `MIDlet`과의 통신 기법으로 
사용될 수 있습니다.

예를 들어, ``UDPDatagramConnection``이 열리고 
포트 번호가 지정되어 있지 않으면 
응용 프로그램은 현재 사용 가능한 포트에서 
동적 포트를 할당하도록 요청합니다. 
`MIDlet`은 
`PushRegistry.registerConnection()`을 호출하여 
`MIDlet`이 삭제된 후에도 
자신이 인바운드 통신 대상이라는 것을 
AMS에 알립니다
("삭제됨" 상태 정의는 `MIDlet` 라이프사이클 참조) 
전화기에서 응용 프로그램을 
삭제하면 동적 통신 연결이 
자동으로 등록 취소됩니다.

### AMS 런타임 처리 - 구현 시 주의 사항

잘 알려진 주소에서 인바운드 통신을 예상하는 
각 `MIDlet`은 설치 중에 
상세 목록이나 응용 프로그램 설명자 
파일의 푸시 등록 속성 정보를 
AMS에서 기록하게 합니다. 
설치가 완료되면 `MIDlet`이 푸시 알림 이벤트와 
같은 인바운드 통신을 수신할 수도 있습니다. 
설치 완료에 대한 OTA 권장 방법은 
*설치 알림 메시지*가 성공적으로 
전송되었을 때 응용 프로그램이 
공식적으로 설치된 것으로 간주합니다.

AMS를 시작하면 등록된 연결 목록을 검사하고 
인바운드 통신 수신을 시작합니다. 
알림이 도착하면 AMS는 등록된 `MIDlet`을 시작합니다. 
그러면 `MIDlet`이 
`Connector.open()` 메소드를 
사용하여 연결을 열고 특정 연결 유형에 
필요한 I/O 작업을 수행합니다. 
예를 들어, 서버 소켓의 경우 응용 프로그램은 
`acceptAndOpen()`을 사용하여 소켓을 연결하고 
데이터그램 연결의 경우에는 `receive()`를 사용하여 
전달된 메시지를 읽습니다.

메시지 지향적 전송의 경우 AMS가 인바운드 메시지를 읽어 
`MIDlet`이 데이터 읽기를 요청하면 전달하기 위해 
저장할 수 있습니다. 
스트림 지향적 전송에서는 
연결 요청의 서버측이 시간 초과되기 전에 
연결이 승인되지 않으면 손실될 수도 있습니다.

등록된 푸시 연결 알림에 대한 응답으로 
`MIDlet`을 시작할 때 
현재 실행 중인 응용 프로그램이 어떻게 될지는 플랫폼에 따라 다릅니다. 
`MIDlet` 라이프사이클은 중단된 
`MIDlet`이 `pauseApp()` 또는 
`destroyApp()` 호출을 통해 확인할 수 있는 예상 동작을 정의합니다.

**사용 시나리오 1:**
Suite에는 잘 알려진 통신 포트가 있는 
`MIDlet`이 포함되어 있습니다. 
`startApp` 처리 중에 
수신 데이터를 처리하는 
스레드가 시작됩니다. 차단 I/O 작업과 정상적 
사용자 상호 작용 이벤트 사이의 충돌을 피하기 위해 별도의 
스레드를 사용하는 것이 권장됩니다. 
스레드는 `MIDlet`이 삭제될 때까지 
계속 메시지를 수신합니다.

이 샘플에서 설명자 파일에는 
정적 푸시 연결 등록이 포함되어 있습니다. 
또한 인바운드 푸시 메시지에 
데이터그램 연결을 사용할 수 있는 
권한이 이 `MIDlet`에 
필요하다고 표시합니다. 
(`MIDlet` 사용 권한에 대한 자세한 내용은 
패키지 개요의 `푸시 함수 보안`을 
참조하십시오.) 
**주:** 이 샘플은 데이터그램이 급증할 때 적합합니다. 
연결에 대해 루프되면서 
수신된 메시지를 처리하도록 
작성됩니다.

**사용 시나리오 2:**
Suite에는 처음 시작될 때 
동적으로 포트를 할당하는 
`MIDlet`이 포함되어 있습니다.

이 샘플에서 설명자 파일에는 
인바운드 푸시 메시지에 대해 데이터그램 연결을 사용할 수 있는 
권한이 응용 프로그램에 
필요함을 나타내는 항목이 포함되어 있습니다. 
처음 구성자를 실행하면 구성자에서 동적 연결이 할당됩니다. 
이 세션 중에 열린 연결이 사용되며 
인바운드 연결 알림에 대한 응답으로 
이후 세션에서 다시 열릴 수 있습니다.

**Since:**
- MIDP 2.0

## 메서드 요약

- `static String getFilter ( String connection)` — 요청된 연결에 등록된 필터를 검색합니다.
- `static String getMIDlet ( String connection)` — 요청된 연결에 등록된 MIDlet 을 검색합니다.
- `static String [] listConnections (boolean available)` — 현재 MIDlet Suite에 대해 등록된 연결 목록을 반환합니다.
- `static long registerAlarm ( String midlet, long time)` — 지정된 응용 프로그램을 시작할 시간을 등록합니다.
- `static void registerConnection ( String connection, String midlet, String filter)` — 응용 프로그램 관리 소프트웨어를 사용하여 동적 연결을 등록합니다.
- `static boolean unregisterConnection ( String connection)` — 동적 연결 등록을 제거합니다.

## 메서드 상세

### registerConnection

```java
public static void registerConnection(String connection,
                                      String midlet,
                                      String filter)
                               throws ClassNotFoundException,
                                      IOException
```

**Parameters:**
- `filter` - 보낸 사람이 `MIDlet`이 
 시작되게 할 수 있음을 나타내는 연결 URL 문자열

**Throws:**
- `SecurityException` - `MIDlet`에 
 연결을 등록할 수 있는 권한이 없는 경우

**See Also:**
- ``unregisterConnection(java.lang.String)``

### unregisterConnection

```java
public static boolean unregisterConnection(String connection)
```

**Parameters:**
- `connection` - 일반 연결 *프로토콜*, 
 *호스트* 및 *포트 번호*

**Returns:**
- 등록 취소에 성공하면 `true`, 
 연결이 등록되지 않았거나 연결 인자가 `null`인 경우 
 `false`

**Throws:**
- `SecurityException` - 다른 `MIDlet` 
 Suite에서 
 연결을 등록한 경우

**See Also:**
- ``registerConnection(java.lang.String, java.lang.String, java.lang.String)``

### listConnections

```java
public static String[] listConnections(boolean available)
```

**Parameters:**
- `available` - `true`이면 입력을 
 사용할 수 있는 연결 목록만 반환되고, 그렇지 않으면 현재 
 `MIDlet` Suite에 대해 등록된 
 전체 연결 목록을 반환합니다.

**Returns:**
- 등록된 연결 문자열 배열. 여기서 각 연결은 일반 연결 
 *프로토콜*, *호스트* 및 
 *포트 번호* ID로 표현됩니다.

### getMIDlet

```java
public static String getMIDlet(String connection)
```

**Parameters:**
- `connection` - 일반 연결 *프로토콜*, 
 *호스트* 및 *포트 번호*(옵션 매개 변수는 
 세미콜론(;)으로 구분하여 
 포함할 수 있습니다.)

**Returns:**
- 새 외부 데이터를 사용할 수 있을 때 시작되는 
 `MIDlet`의 클래스 이름 또는 
 현재 `MIDlet` Suite에서 연결을 
 등록하지 않았거나 연결 인자가 `null`인 경우 
 `null`

**See Also:**
- ``registerConnection(java.lang.String, java.lang.String, java.lang.String)``

### getFilter

```java
public static String getFilter(String connection)
```

**Parameters:**
- `connection` - 일반 연결 *프로토콜*, 
 *호스트* 및 *포트 번호*(옵션 매개 변수는 
 세미콜론(;)으로 구분하여 
 포함할 수 있습니다.)

**Returns:**
- 보낸 사람이 `MIDlet`이 시작되게 할 수 있음을 나타내는 
 필터 문자열 또는 현재 `MIDlet` Suite에서 
 연결을 등록하지 않았거나 
 연결 인자가 `null`인 경우 
 `null`

**See Also:**
- ``registerConnection(java.lang.String, java.lang.String, java.lang.String)``

### registerAlarm

```java
public static long registerAlarm(String midlet,
                                 long time)
                          throws ClassNotFoundException,
                                 ConnectionNotFoundException
```

**Parameters:**
- `time` - `MIDlet`이 `Date.getTime()`에서 
 반환된 형식으로 실행되는 시간

**Returns:**
- 이 `MIDlet`의 최근 실행이 예약된
 시간(`Date.getTime()`에서 
 반환된 형식)

**Throws:**
- `SecurityException` - `MIDlet`에 경보를 
 등록할 수 있는 권한이 없는 경우

**See Also:**
- ``Date.getTime()``, 
``Timer``, 
``TimerTask``
