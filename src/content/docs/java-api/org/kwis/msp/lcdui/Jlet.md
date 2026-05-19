---
title: "Class Jlet"
---

`package org.kwis.msp.lcdui`

```text
java.lang.Object
  |
  +--org.kwis.msp.lcdui.Jlet
```

## 설명

**extends Object:**

WIPI 응용 프로그램입니다.

WIPI를 이용하는 모든 응용 프로그램은 `Jlet`을 상속받아서 
 작성되어야 합니다.

 WIPI에서의 자원들은 모두 `Jlet`단위로 응용 프로그램의 
 자원이 관리됩니다.

 WIPI에서 생성한 `Thread`와 Card들은 Jlet이 종료될 때
 시스템에서 사라 집니다.

Jlet은 세 가지 상태를 가집니다. Jlet을 생성 시키면 자동적으로
 *active*상태가 되고, JAM에서 프로그램을 일시 정지하거나 
 프로그램이 사용자에 의해서 일시 정지시켜야 하는 경우에는 
 *pause*상태가 됩니다. 이 상태에서 JAM이나 사용자에 의해서
 다시 *active*상태로 돌아 올 수 있습니다.

어떠한 상태던지 Jlet은 *destroyed*상태로 전이할 수 있으며,
 이 때에는 Jlet은 프로그램을 종료해야 합니다.

프로그램은 전이하는 상태에서 다음 그림과 같이 각각 `pauseApp()`와
 `resumeApp()`, `startApp()`, `destroyApp()`
 함수가 불립니다.

프로그램을 처음에 `startApp`함수가 불립니다. 이때에는
 파라미터로 `System.execute`함수 호출시 넘긴 파라미터가
 넘어 옵니다.

## 필드 요약

- `static int ACTIVE`
- `static int DESTROYED`
- `static int PAUSED`

## 생성자 요약

- `protected Jlet ()` — 새로운 Jlet을 생성합니다.

## 메서드 요약

- `protected abstract  void destroyApp (boolean unconditional)` — 프로그램이 종료 됨을 알려주는 함수입니다.
- `static Jlet getActiveJlet ()` — 현재 활성화된 Jlet 를 얻어 옵니다.
- `String getAppProperty ( String key)` — 응용 프로그램마다 지정되어 있는 프라퍼티를 돌려줍니다.
- `static Jlet getCurrentJlet ()` — 현재 수행중인 Jlet 을 얻어 옵니다.
- `int getCurrentProgramID ()` — Jlet을 생성한 프로그램 id를 돌려준다.
- `EventQueue getEventQueue ()` — Jlet 과 연결된 이벤트 큐를 돌려줍니다.
- `static Jlet getJletFromPID (int id)` — 주어진id에 해당하는 Jlet 를 얻어 옵니다.
- `void notifyDestroyed ()` — 프로그램을 종료 시킬때 사용되는 함수.
- `protected  void pauseApp ()` — 프로그램을 정지하려고 하는 때 불려집니다.
- `static void removeAllResource (int id)`
- `protected  void resumeApp ()` — 정지된 프로그램을 다시 수행을 재기하려할때 불려집니다.
- `static void setActiveJlet ( Jlet ql)` — 지정된 Jlet 을 활성화 시킵니다.
- `protected abstract  void startApp ( String [] args)` — 프로그램이 시작될 때 불려집니다.

## 필드 상세

### ACTIVE

```java
public static final int ACTIVE
```

### DESTROYED

```java
public static final int DESTROYED
```

### PAUSED

```java
public static final int PAUSED
```

### Jlet

```java
protected Jlet()
```

- 새로운 Jlet을 생성합니다.

### setActiveJlet

```java
public static void setActiveJlet(Jlet ql)
```

- 지정된 `Jlet`을 활성화 시킵니다.

 지정된 Jlet을 활성화 시킵니다.

### getActiveJlet

```java
public static Jlet getActiveJlet()
```

**Returns:**
- 현재 상위에서 수행중에 있는 `Jlet`

### getJletFromPID

```java
public static Jlet getJletFromPID(int id)
```

**Returns:**
- ID에 해당하는 `Jlet`

### getCurrentJlet

```java
public static Jlet getCurrentJlet()
```

**Returns:**
- 현재 수행중인 `Jlet`

### getCurrentProgramID

```java
public int getCurrentProgramID()
```

**Parameters:**
- `id` - Jlet을 생성한 프로그램 id

### startApp

```java
protected abstract void startApp(String[] args)
```

**Parameters:**
- `args` - 사용자가 넘기는 인수.

### pauseApp

```java
protected void pauseApp()
```

- 프로그램을 정지하려고 하는 때 불려집니다.

 시스템에서 응용 프로그램에게 일시 정지를 요청할때 이 함수를 부릅니다.
 프로그램은 사용자의 인터렉션에 의해서 정지할 수도 있습니다.
 정지하는 경우에 사용하고 있던 시스템 자원(네트웍, 시리얼등)을 
 되돌려 줄수 잇도록 구현하셔야 합니다.

### resumeApp

```java
protected void resumeApp()
```

- 정지된 프로그램을 다시 수행을 재기하려할때 불려집니다.

 시스템에서 응용 프로그램에게 수행 재기를 요청할때 이 함수를 부릅니다.
 `pauseApp`함수로 정지했던 `Jlet`를 다시
 기동시키며, 이 함수내에서 `pauseApp`에서 돌려주었던 
 시스템 자원들(네트웍, 시리얼등)을
 다시 할당 받도록 함수를 구현하셔야 합니다.

### destroyApp

```java
protected abstract void destroyApp(boolean unconditional)
                            throws JletStateChangeException
```

**Parameters:**
- `unconditonal` - 만일 true이면 프로그램이 무조건 종료가 되고, 
 false일때에는 `Jlet`은 
 `JletStateChangeException`을 던져서 프로그램 종료를 막을 
 수 있음

**Throws:**
- `JletStateChangeException` - 현재 상태에서 프로그램을 종료할 수 
 없는 경우. 만일 `unconditional`이 `true`이면, 이 예외를 던진다 해도,
 프로그램은 종료됩니다.

### notifyDestroyed

```java
public final void notifyDestroyed()
```

- 프로그램을 종료 시킬때 사용되는 함수.

 `Jlet`응용 프로그램을 종료할 때 이 함수를 부릅니다.
 이 함수를 부르면 프로그램은 *Destoryed*상태로 들어가며,
 차후에 `destroyApp`메써드를 호출합니다.
 

`Jlet.destroyApp()`를 호출함으로써 프로그램이 가지고 있는
 모든 자원을 되돌려 줍니다.

### getAppProperty

```java
public final String getAppProperty(String key)
```

**Parameters:**
- `key` - 찾을 프라퍼티에 대응하는 키

**Returns:**
- 해당하는 프라퍼티

### getEventQueue

```java
public final EventQueue getEventQueue()
```

**Returns:**
- 이벤트 큐

### removeAllResource

```java
public static void removeAllResource(int id)
```## 생성자 상세

### Jlet

```java
protected Jlet()
```

- 새로운 Jlet을 생성합니다.

### setActiveJlet

```java
public static void setActiveJlet(Jlet ql)
```

- 지정된 `Jlet`을 활성화 시킵니다.

 지정된 Jlet을 활성화 시킵니다.

### getActiveJlet

```java
public static Jlet getActiveJlet()
```

**Returns:**
- 현재 상위에서 수행중에 있는 `Jlet`

### getJletFromPID

```java
public static Jlet getJletFromPID(int id)
```

**Returns:**
- ID에 해당하는 `Jlet`

### getCurrentJlet

```java
public static Jlet getCurrentJlet()
```

**Returns:**
- 현재 수행중인 `Jlet`

### getCurrentProgramID

```java
public int getCurrentProgramID()
```

**Parameters:**
- `id` - Jlet을 생성한 프로그램 id

### startApp

```java
protected abstract void startApp(String[] args)
```

**Parameters:**
- `args` - 사용자가 넘기는 인수.

### pauseApp

```java
protected void pauseApp()
```

- 프로그램을 정지하려고 하는 때 불려집니다.

 시스템에서 응용 프로그램에게 일시 정지를 요청할때 이 함수를 부릅니다.
 프로그램은 사용자의 인터렉션에 의해서 정지할 수도 있습니다.
 정지하는 경우에 사용하고 있던 시스템 자원(네트웍, 시리얼등)을 
 되돌려 줄수 잇도록 구현하셔야 합니다.

### resumeApp

```java
protected void resumeApp()
```

- 정지된 프로그램을 다시 수행을 재기하려할때 불려집니다.

 시스템에서 응용 프로그램에게 수행 재기를 요청할때 이 함수를 부릅니다.
 `pauseApp`함수로 정지했던 `Jlet`를 다시
 기동시키며, 이 함수내에서 `pauseApp`에서 돌려주었던 
 시스템 자원들(네트웍, 시리얼등)을
 다시 할당 받도록 함수를 구현하셔야 합니다.

### destroyApp

```java
protected abstract void destroyApp(boolean unconditional)
                            throws JletStateChangeException
```

**Parameters:**
- `unconditonal` - 만일 true이면 프로그램이 무조건 종료가 되고, 
 false일때에는 `Jlet`은 
 `JletStateChangeException`을 던져서 프로그램 종료를 막을 
 수 있음

**Throws:**
- `JletStateChangeException` - 현재 상태에서 프로그램을 종료할 수 
 없는 경우. 만일 `unconditional`이 `true`이면, 이 예외를 던진다 해도,
 프로그램은 종료됩니다.

### notifyDestroyed

```java
public final void notifyDestroyed()
```

- 프로그램을 종료 시킬때 사용되는 함수.

 `Jlet`응용 프로그램을 종료할 때 이 함수를 부릅니다.
 이 함수를 부르면 프로그램은 *Destoryed*상태로 들어가며,
 차후에 `destroyApp`메써드를 호출합니다.
 

`Jlet.destroyApp()`를 호출함으로써 프로그램이 가지고 있는
 모든 자원을 되돌려 줍니다.

### getAppProperty

```java
public final String getAppProperty(String key)
```

**Parameters:**
- `key` - 찾을 프라퍼티에 대응하는 키

**Returns:**
- 해당하는 프라퍼티

### getEventQueue

```java
public final EventQueue getEventQueue()
```

**Returns:**
- 이벤트 큐

### removeAllResource

```java
public static void removeAllResource(int id)
```## 메서드 상세

### setActiveJlet

```java
public static void setActiveJlet(Jlet ql)
```

- 지정된 `Jlet`을 활성화 시킵니다.

 지정된 Jlet을 활성화 시킵니다.

### getActiveJlet

```java
public static Jlet getActiveJlet()
```

**Returns:**
- 현재 상위에서 수행중에 있는 `Jlet`

### getJletFromPID

```java
public static Jlet getJletFromPID(int id)
```

**Returns:**
- ID에 해당하는 `Jlet`

### getCurrentJlet

```java
public static Jlet getCurrentJlet()
```

**Returns:**
- 현재 수행중인 `Jlet`

### getCurrentProgramID

```java
public int getCurrentProgramID()
```

**Parameters:**
- `id` - Jlet을 생성한 프로그램 id

### startApp

```java
protected abstract void startApp(String[] args)
```

**Parameters:**
- `args` - 사용자가 넘기는 인수.

### pauseApp

```java
protected void pauseApp()
```

- 프로그램을 정지하려고 하는 때 불려집니다.

 시스템에서 응용 프로그램에게 일시 정지를 요청할때 이 함수를 부릅니다.
 프로그램은 사용자의 인터렉션에 의해서 정지할 수도 있습니다.
 정지하는 경우에 사용하고 있던 시스템 자원(네트웍, 시리얼등)을 
 되돌려 줄수 잇도록 구현하셔야 합니다.

### resumeApp

```java
protected void resumeApp()
```

- 정지된 프로그램을 다시 수행을 재기하려할때 불려집니다.

 시스템에서 응용 프로그램에게 수행 재기를 요청할때 이 함수를 부릅니다.
 `pauseApp`함수로 정지했던 `Jlet`를 다시
 기동시키며, 이 함수내에서 `pauseApp`에서 돌려주었던 
 시스템 자원들(네트웍, 시리얼등)을
 다시 할당 받도록 함수를 구현하셔야 합니다.

### destroyApp

```java
protected abstract void destroyApp(boolean unconditional)
                            throws JletStateChangeException
```

**Parameters:**
- `unconditonal` - 만일 true이면 프로그램이 무조건 종료가 되고, 
 false일때에는 `Jlet`은 
 `JletStateChangeException`을 던져서 프로그램 종료를 막을 
 수 있음

**Throws:**
- `JletStateChangeException` - 현재 상태에서 프로그램을 종료할 수 
 없는 경우. 만일 `unconditional`이 `true`이면, 이 예외를 던진다 해도,
 프로그램은 종료됩니다.

### notifyDestroyed

```java
public final void notifyDestroyed()
```

- 프로그램을 종료 시킬때 사용되는 함수.

 `Jlet`응용 프로그램을 종료할 때 이 함수를 부릅니다.
 이 함수를 부르면 프로그램은 *Destoryed*상태로 들어가며,
 차후에 `destroyApp`메써드를 호출합니다.
 

`Jlet.destroyApp()`를 호출함으로써 프로그램이 가지고 있는
 모든 자원을 되돌려 줍니다.

### getAppProperty

```java
public final String getAppProperty(String key)
```

**Parameters:**
- `key` - 찾을 프라퍼티에 대응하는 키

**Returns:**
- 해당하는 프라퍼티

### getEventQueue

```java
public final EventQueue getEventQueue()
```

**Returns:**
- 이벤트 큐

### removeAllResource

```java
public static void removeAllResource(int id)
```

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
