---
title: "Class Thread"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Thread
```

## 설명

**extends Object:**

VM에서 사용하는 쓰레드에 관한 클래스.

## 필드 요약

- `static int MAX_PRIORITY` — 쓰레드 우선 순위 최대값.
- `static int MIN_PRIORITY` — 쓰레드 우선 순위 최소값.
- `static int NORM_PRIORITY` — 쓰레드 우선 순위 디폴트 값.

## 생성자 요약

- Thread () 쓰레드객체를 생성한다.
- Thread ( Runnable toRun) 쓰레드에서 실제로 기동시킬 대상을 지정해서 쓰레드 객체를 생성한다.

## 메서드 요약

- `static int activeCount ()` — VM내의 active한 쓰레드 갯수를 구한다.
- `static Thread currentThread ()` — 현재 실행되고 있는 쓰레드를 구한다.
- `int getPriority ()` — 현 쓰레드의 우선순위를 구한다.
- `boolean isAlive ()` — 현 쓰레드가 살아있는 지 여부를 구한다.
- `void join ()` — 현재 실행되는 쓰레드가 현 쓰레드 객체가 죽기 까지 기다리게 한다.
- `void run ()` — 현 쓰레드가 시작되면 먼저 이메소드가 호출된다.
- `void setPriority (int newPriority)` — 현 쓰레드의 우선 순위를 바꾼다.
- `static void sleep (long millis)` — 현재 수행 중인 쓰레드가 특정 시간 만큼 동작을 멈춘다.
- `void start ()` — 쓰레드가 동작을 시작한다.
- `String toString ()` — 현 쓰레드를 나타내는 문자열을 구한다.
- `static void yield ()` — 현재 수행되는 쓰레드가 다른 쓰레드가 실행되도록 자신의 순번을 양보한다.

## 필드 상세

### MAX_PRIORITY

```java
public static final int MAX_PRIORITY
```

- 쓰레드 우선 순위 최대값.

### NORM_PRIORITY

```java
public static final int NORM_PRIORITY
```

- 쓰레드 우선 순위 디폴트 값.

### MIN_PRIORITY

```java
public static final int MIN_PRIORITY
```

- 쓰레드 우선 순위 최소값.

### Thread

```java
public Thread()
```

- 쓰레드객체를 생성한다.

### Thread

```java
public Thread(Runnable toRun)
```

**Parameters:**
- `toRun` - 쓰레드에서 기동 시킬 대상이며 Runnable 인터페이스를 구현해야 함.

### activeCount

```java
public static int activeCount()
```

**Returns:**
- VM내에서 active한 쓰레드 갯수.

### currentThread

```java
public static Thread currentThread()
```

**Returns:**
- 현재 실행되고 있는 쓰레드.

### getPriority

```java
public final int getPriority()
```

**Returns:**
- 현 쓰레드 우선순위.

### isAlive

```java
public final boolean isAlive()
```

**Returns:**
- 현 쓰레드가 살아있으면 true 아니면 false.

### join

```java
public final void join()
                throws InterruptedException
```

**Throws:**
- `InterruptedException` - 다른 쓰레드에서 join상태인 쓰레드에 
 Interrput을 걸었을 때 발생.

### run

```java
public void run()
```

- 현 쓰레드가 시작되면 먼저 이메소드가 호출된다.

### setPriority

```java
public final void setPriority(int newPriority)
```

**Parameters:**
- `newPriority` - 바뀔 우선 순위.

### sleep

```java
public static void sleep(long millis)
                  throws InterruptedException
```

**Parameters:**
- `millis` - 동작이 정지되는 시간.

**Throws:**
- `InterruptedException` - 다른 쓰레드에서 sleep상태인 쓰레드에 
 Interrput을 걸었을 때 발생.

### start

```java
public void start()
```

- 쓰레드가 동작을 시작한다.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 쓰레드를 나타내는 문자열.

### yield

```java
public static void yield()
```

- 현재 수행되는 쓰레드가 다른 쓰레드가 실행되도록 자신의
 순번을 양보한다.## 생성자 상세

### Thread

```java
public Thread()
```

- 쓰레드객체를 생성한다.

### Thread

```java
public Thread(Runnable toRun)
```

**Parameters:**
- `toRun` - 쓰레드에서 기동 시킬 대상이며 Runnable 인터페이스를 구현해야 함.

### activeCount

```java
public static int activeCount()
```

**Returns:**
- VM내에서 active한 쓰레드 갯수.

### currentThread

```java
public static Thread currentThread()
```

**Returns:**
- 현재 실행되고 있는 쓰레드.

### getPriority

```java
public final int getPriority()
```

**Returns:**
- 현 쓰레드 우선순위.

### isAlive

```java
public final boolean isAlive()
```

**Returns:**
- 현 쓰레드가 살아있으면 true 아니면 false.

### join

```java
public final void join()
                throws InterruptedException
```

**Throws:**
- `InterruptedException` - 다른 쓰레드에서 join상태인 쓰레드에 
 Interrput을 걸었을 때 발생.

### run

```java
public void run()
```

- 현 쓰레드가 시작되면 먼저 이메소드가 호출된다.

### setPriority

```java
public final void setPriority(int newPriority)
```

**Parameters:**
- `newPriority` - 바뀔 우선 순위.

### sleep

```java
public static void sleep(long millis)
                  throws InterruptedException
```

**Parameters:**
- `millis` - 동작이 정지되는 시간.

**Throws:**
- `InterruptedException` - 다른 쓰레드에서 sleep상태인 쓰레드에 
 Interrput을 걸었을 때 발생.

### start

```java
public void start()
```

- 쓰레드가 동작을 시작한다.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 쓰레드를 나타내는 문자열.

### yield

```java
public static void yield()
```

- 현재 수행되는 쓰레드가 다른 쓰레드가 실행되도록 자신의
 순번을 양보한다.## 메서드 상세

### activeCount

```java
public static int activeCount()
```

**Returns:**
- VM내에서 active한 쓰레드 갯수.

### currentThread

```java
public static Thread currentThread()
```

**Returns:**
- 현재 실행되고 있는 쓰레드.

### getPriority

```java
public final int getPriority()
```

**Returns:**
- 현 쓰레드 우선순위.

### isAlive

```java
public final boolean isAlive()
```

**Returns:**
- 현 쓰레드가 살아있으면 true 아니면 false.

### join

```java
public final void join()
                throws InterruptedException
```

**Throws:**
- `InterruptedException` - 다른 쓰레드에서 join상태인 쓰레드에 
 Interrput을 걸었을 때 발생.

### run

```java
public void run()
```

- 현 쓰레드가 시작되면 먼저 이메소드가 호출된다.

### setPriority

```java
public final void setPriority(int newPriority)
```

**Parameters:**
- `newPriority` - 바뀔 우선 순위.

### sleep

```java
public static void sleep(long millis)
                  throws InterruptedException
```

**Parameters:**
- `millis` - 동작이 정지되는 시간.

**Throws:**
- `InterruptedException` - 다른 쓰레드에서 sleep상태인 쓰레드에 
 Interrput을 걸었을 때 발생.

### start

```java
public void start()
```

- 쓰레드가 동작을 시작한다.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 쓰레드를 나타내는 문자열.

### yield

```java
public static void yield()
```

- 현재 수행되는 쓰레드가 다른 쓰레드가 실행되도록 자신의
 순번을 양보한다.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
