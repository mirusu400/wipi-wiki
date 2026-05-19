---
title: "Class MIDlet"
---

`package javax.microedition.midlet`

```text
java.lang.Object
  |
  +--javax.microedition.midlet.MIDlet
```

## 설명

**extends Object:**

`MIDlet`은 MID 프로필 응용 프로그램입니다. 
응용 프로그램은 이 클래스를 확장하여 
응용 프로그램 관리 소프트웨어가 
MIDlet을 제어하고 응용 프로그램 설명자에서 등록 정보를 검색하고 
상태 변경을 통지 및 요청할 수 있게 합니다. 
이 클래스의 메소드를 사용하면 응용 프로그램 관리 소프트웨어가 
MIDlet을 작성, 시작, 일시 중지 및 완전 삭제할 수 있습니다. 
`MIDlet`은 이 인터페이스를 통해 응용 프로그램 
관리 소프트웨어에서 실행 및 제어되도록 설계된 클래스 집합입니다. 
상태를 사용하면 응용 프로그램 관리 
소프트웨어가 런타임 환경의 
여러 `MIDlet` 작업을 관리할 수 있습니다. 
이를 통해 개별적으로 MIDlet을 시작 및 일시 중지시켰을 때 
주어진 시간에 어떤 `MIDlet`이 
활성 상태인지 선택할 수 있습니다. 
응용 프로그램 관리 소프트웨어는 `MIDlet`의 상태를 
관리하고 `MIDlet`의 메소드를 
호출하여 MIDlet의 상태 변경을 알립니다. 
`MIDlet`은 이러한 메소드를 구현하여 응용 프로그램 관리 
소프트웨어에서 지시하는 대로 해당 내부 작업 및 
자원 사용을 업데이트합니다. 
`MIDlet`은 자체적으로 몇 가지 상태 변경을 시작할 수 있으며 
적절한 메소드를 호출하여 응용 프로그램 관리 소프트웨어에 
이러한 상태 변경을 알립니다.

**주:** 이 인터페이스의 메소드가 상태 변경을 알립니다. 
상태 변경 메소드가 반환되어야 상태 변경이 
완료된 것으로 간주합니다. 
이는 이러한 메소드가 빨리 반환되게 하기 위함입니다.

## 생성자 요약

- `protected MIDlet ()` — 서브 클래스에 대해 보호된 구성자.

## 메서드 요약

- `int checkPermission ( String permission)` — 지정된 권한 상태를 가져옵니다.
- `protected abstract  void destroyApp (boolean unconditional)` — MIDlet 이 종료되어 완전 삭제 상태에 들어갔음을 알립니다.
- `String getAppProperty ( String key)` — 응용 프로그램 관리 소프트웨어에서 명명된 등록 정보를 검색하는 기법을 MIDlet 에 제공합니다.
- `void notifyDestroyed ()` — MIDlet 이 완전 삭제 상태에 들어갔다는 것을 응용 프로그램 관리 소프트웨어에 알릴 때 사용합니다.
- `void notifyPaused ()` — MIDlet이 활성화되지 않고 일시 중지 상태에 들어갔음을 응용 프로그램 관리 소프트웨어에 알립니다.
- `protected abstract  void pauseApp ()` — MIDlet 이 일시 중지 상태에 들어갔음을 알립니다.
- `boolean platformRequest ( String URL)` — 장치가 표시된 URL을 처리(예: 표시 또는 설치)하도록 요청합니다.
- `void resumeRequest ()` — MIDlet 이 활성 상태에 들어가려고 함을 표시하는 기법을 MIDlet에 제공합니다.
- `protected abstract  void startApp ()` — MIDlet 이 활성 상태로 들어갔음을 MIDlet에 알립니다.

## 생성자 상세

### MIDlet

```java
protected MIDlet()
```

- 서브 클래스에 대해 보호된 구성자. 
응용 프로그램 관리 소프트웨어에서 MIDlet 작성을 담당하며 
이 작업은 제한되어 있습니다. 
MIDlet에서 다른 MIDlet을 작성할 수 없습니다.

**Throws:**
- `SecurityException` - 응용 프로그램 
관리 소프트웨어에서 MIDlet을 작성하지 않은 경우

### startApp

```java
protected abstract void startApp()
                          throws MIDletStateChangeException
```

**Throws:**
- `MIDletStateChangeException` - `MIDlet`을 현재 시작할 수 없고 
나중에 시작할 수 있는 
경우 발생합니다.

### pauseApp

```java
protected abstract void pauseApp()
```

MIDlet 이 일시 중지 상태에 들어갔음을 알립니다. 일시 중지 상태의 MIDlet 은 
공유 자원을 해제하고 정지 상태가 되어야 합니다. 
이 메소드는 MIDlet 이 활성 상태인 
경우에만 호출됩니다. pauseApp 중 런타임 예외가 발생하면 
MIDlet은 즉시 완전 삭제됩니다. 
해당 destroyApp 가 호출되어 
MIDlet을 지웁니다.

### destroyApp

```java
protected abstract void destroyApp(boolean unconditional)
                            throws MIDletStateChangeException
```

**Parameters:**
- `unconditional` - 이 메소드가 호출될 때 true이면 
`MIDlet`이 정리되고 모든 자원을 해제해야 합니다. 
반대로 false이면 `MIDlet`이 `MIDletStateChangeException`을 발생시켜 
지금은 완전 삭제되지 않을 것임을 표시합니다.

**Throws:**
- `MIDletStateChangeException` - `MIDlet`이 
실행을 계속하지 않으려는 경우 발생합니다(*완전 삭제* 상태에 
들어가지 않음). 
이 예외는 `unconditional`이 
`true`인 경우에는 무시됩니다.

### notifyDestroyed

```java
public final void notifyDestroyed()
```

MIDlet 이 완전 삭제 상태에 들어갔다는 것을 응용 프로그램 
관리 소프트웨어에 알릴 때 사용합니다. 
이 경우 응용 프로그램 관리 소프트웨어는 MIDlet의 destroyApp 메소드를 호출하지 않고 MIDlet 이 보유한 
모든 자원을 다시 사용할 수 있는 것으로 
간주합니다. MIDlet.destroyApp() 가 호출되면 MIDlet 은 동일한 작업(정리 및 자원 해제 등)을 
수행해야 합니다.

### notifyPaused

```java
public final void notifyPaused()
```

MIDlet이 활성화되지 않고 일시 중지 상태에 들어갔음을 
응용 프로그램 관리 소프트웨어에 알립니다. MIDlet 이 
완전 삭제되었거나 
아직 시작되지 않은 경우에는 
이 메소드를 호출해도 아무 효과가 없습니다. MIDlet 이 활성 상태에 있으면 
MIDlet에 의해 이 메소드가 호출될 수 있습니다. MIDlet 이 notifyPaused() 를 호출하면 나중에 startApp() 메소드가 호출되어 
MIDlet을 다시 활성화할 수도 있고 destroyApp() 메소드가 호출되어 완전 삭제할 수도 있습니다. 응용 프로그램 자체적으로 일시 중지되면 resumeRequest 를 호출하여 활성 상태에 다시 들어가도록 요청해야 합니다.

### getAppProperty

```java
public final String getAppProperty(String key)
```

**Parameters:**
- `key` - 등록 정보 이름

**Returns:**
- 등록 정보 값을 가진 문자열. 
키에 사용 가능한 값이 없는 경우 
`null`이 반환됩니다.

**Throws:**
- `NullPointerException` - 키가 `null`인 경우 발생합니다.

### resumeRequest

```java
public final void resumeRequest()
```

MIDlet 이 활성 상태에 들어가려고 
함을 표시하는 기법을 MIDlet에 제공합니다. 
응용 프로그램 관리 소프트웨어는 
이 메소드를 호출하여 활성 상태로 이동할 응용 프로그램을 
결정할 수 있습니다. 응용 프로그램 관리 소프트웨어가 
이 응용 프로그램을 활성화할 때 startApp 메소드가 호출됩니다. 이 메소드가 호출되는 경우 응용 프로그램은 일반적으로 일시 중지 상태입니다. 
응용 프로그램은 일시 중지 상태에서도 타이머 또는 콜백과 같은 
비동기 이벤트를 처리할 수 있습니다.

### platformRequest

```java
public final boolean platformRequest(String URL)
                              throws ConnectionNotFoundException
```

**Parameters:**
- `URL` - 플랫폼에서 로드할 URL. 공백 문자열(null 아님)은 
보류 중인 요청을 취소합니다.

**Returns:**
- 내용을 가져오기 전에 먼저 MIDlet Suite를 
종료해야 하는 경우 true

**Throws:**
- `ConnectionNotFoundException` - 플랫폼이 요청된 URL을 처리할 수 없는 경우

**Since:**
- MIDP 2.0

### checkPermission

```java
public final int checkPermission(String permission)
```

**Parameters:**
- `permission` - 거부, 허용 또는 알 수 없음인지 확인

**Returns:**
- 권한이 거부되면 0, 권한이 허용되면 1, 
알려지지 않은 상태이면 -1

**Since:**
- MIDP 2.0

## 메서드 상세

### startApp

```java
protected abstract void startApp()
                          throws MIDletStateChangeException
```

**Throws:**
- `MIDletStateChangeException` - `MIDlet`을 현재 시작할 수 없고 
나중에 시작할 수 있는 
경우 발생합니다.

### pauseApp

```java
protected abstract void pauseApp()
```

MIDlet 이 일시 중지 상태에 들어갔음을 알립니다. 일시 중지 상태의 MIDlet 은 
공유 자원을 해제하고 정지 상태가 되어야 합니다. 
이 메소드는 MIDlet 이 활성 상태인 
경우에만 호출됩니다. pauseApp 중 런타임 예외가 발생하면 
MIDlet은 즉시 완전 삭제됩니다. 
해당 destroyApp 가 호출되어 
MIDlet을 지웁니다.

### destroyApp

```java
protected abstract void destroyApp(boolean unconditional)
                            throws MIDletStateChangeException
```

**Parameters:**
- `unconditional` - 이 메소드가 호출될 때 true이면 
`MIDlet`이 정리되고 모든 자원을 해제해야 합니다. 
반대로 false이면 `MIDlet`이 `MIDletStateChangeException`을 발생시켜 
지금은 완전 삭제되지 않을 것임을 표시합니다.

**Throws:**
- `MIDletStateChangeException` - `MIDlet`이 
실행을 계속하지 않으려는 경우 발생합니다(*완전 삭제* 상태에 
들어가지 않음). 
이 예외는 `unconditional`이 
`true`인 경우에는 무시됩니다.

### notifyDestroyed

```java
public final void notifyDestroyed()
```

MIDlet 이 완전 삭제 상태에 들어갔다는 것을 응용 프로그램 
관리 소프트웨어에 알릴 때 사용합니다. 
이 경우 응용 프로그램 관리 소프트웨어는 MIDlet의 destroyApp 메소드를 호출하지 않고 MIDlet 이 보유한 
모든 자원을 다시 사용할 수 있는 것으로 
간주합니다. MIDlet.destroyApp() 가 호출되면 MIDlet 은 동일한 작업(정리 및 자원 해제 등)을 
수행해야 합니다.

### notifyPaused

```java
public final void notifyPaused()
```

MIDlet이 활성화되지 않고 일시 중지 상태에 들어갔음을 
응용 프로그램 관리 소프트웨어에 알립니다. MIDlet 이 
완전 삭제되었거나 
아직 시작되지 않은 경우에는 
이 메소드를 호출해도 아무 효과가 없습니다. MIDlet 이 활성 상태에 있으면 
MIDlet에 의해 이 메소드가 호출될 수 있습니다. MIDlet 이 notifyPaused() 를 호출하면 나중에 startApp() 메소드가 호출되어 
MIDlet을 다시 활성화할 수도 있고 destroyApp() 메소드가 호출되어 완전 삭제할 수도 있습니다. 응용 프로그램 자체적으로 일시 중지되면 resumeRequest 를 호출하여 활성 상태에 다시 들어가도록 요청해야 합니다.

### getAppProperty

```java
public final String getAppProperty(String key)
```

**Parameters:**
- `key` - 등록 정보 이름

**Returns:**
- 등록 정보 값을 가진 문자열. 
키에 사용 가능한 값이 없는 경우 
`null`이 반환됩니다.

**Throws:**
- `NullPointerException` - 키가 `null`인 경우 발생합니다.

### resumeRequest

```java
public final void resumeRequest()
```

MIDlet 이 활성 상태에 들어가려고 
함을 표시하는 기법을 MIDlet에 제공합니다. 
응용 프로그램 관리 소프트웨어는 
이 메소드를 호출하여 활성 상태로 이동할 응용 프로그램을 
결정할 수 있습니다. 응용 프로그램 관리 소프트웨어가 
이 응용 프로그램을 활성화할 때 startApp 메소드가 호출됩니다. 이 메소드가 호출되는 경우 응용 프로그램은 일반적으로 일시 중지 상태입니다. 
응용 프로그램은 일시 중지 상태에서도 타이머 또는 콜백과 같은 
비동기 이벤트를 처리할 수 있습니다.

### platformRequest

```java
public final boolean platformRequest(String URL)
                              throws ConnectionNotFoundException
```

**Parameters:**
- `URL` - 플랫폼에서 로드할 URL. 공백 문자열(null 아님)은 
보류 중인 요청을 취소합니다.

**Returns:**
- 내용을 가져오기 전에 먼저 MIDlet Suite를 
종료해야 하는 경우 true

**Throws:**
- `ConnectionNotFoundException` - 플랫폼이 요청된 URL을 처리할 수 없는 경우

**Since:**
- MIDP 2.0

### checkPermission

```java
public final int checkPermission(String permission)
```

**Parameters:**
- `permission` - 거부, 허용 또는 알 수 없음인지 확인

**Returns:**
- 권한이 거부되면 0, 권한이 허용되면 1, 
알려지지 않은 상태이면 -1

**Since:**
- MIDP 2.0
