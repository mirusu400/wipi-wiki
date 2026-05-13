# Class Thread

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Thread
```

## 설명

**All Implemented Interfaces:**
- `Runnable`

**implements Runnable:**

*Thread*는 프로그램의 실행 스레드입니다. Java 
 가상 머신을 통해 응용 프로그램은 여러 개의 실행 스레드를 
 동시에 실행할 수 있습니다.

모든 스레드에는 우선 순위가 있습니다. 높은 우선 순위를 가진 
 스레드가 낮은 우선 순위를 가진 스레드보다 먼저 실행됩니다.

새로운 실행 스레드는 두 가지 방법으로 만들 수 있습니다. 한 가지 
 방법은 클래스를 `Thread`의 서브 클래스로 
 선언하는 것입니다. 이 서브 클래스는 `Thread` 클래스의 
 `run` 메소드를 무시합니다. 이 경우 서브 클래스의 
 인스턴스를 할당하고 시작할 수 있습니다. 예를 들어, 시작 값보다 
 큰 소수를 계산하는 스레드는 다음과 같이 작성할 수 있습니다.

다음 코드는 스레드를 만들고 실행을 시작합니다.

스레드를 만드는 두 번째 방법은 
 `Runnable` 인터페이스를 구현하는 클래스를 
 선언하는 것입니다. 이 클래스는 `run` 메소드를 
 구현합니다. 이 경우 클래스의 인스턴스를 할당하고 
 `Thread`를 만들 때 인자로 전달하여 시작할 수 있습니다. 
 이 방법으로 작성된 동일한 예는 다음과 같이 나타납니다.

다음 코드는 스레드를 만들고 실행을 시작합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Runnable``, 
``Runtime.exit(int)``, 
``run()``

## 필드 요약

- `static int MAX_PRIORITY` — 스레드가 가질 수 있는 최대 우선 순위
- `static int MIN_PRIORITY` — 스레드가 가질 수 있는 최소 우선 순위
- `static int NORM_PRIORITY` — 스레드에 할당되는 기본 우선 순위

## 생성자 요약

- Thread () 새로운 Thread 객체를 할당합니다.
- Thread ( Runnable target) run 메소드가 호출되는 특정 대상 객체를 가진 
 새로운 Thread 객체를 
 할당합니다.
- Thread ( Runnable target, String name) 지정된 대상과 이름을 가진 새로운 Thread 객체를 할당합니다.
- Thread ( String name) 지정된 이름을 가진 새로운 Thread 객체를 
 할당합니다.

## 메서드 요약

- `static int activeCount ()` — 가상 머신에서 현재 활성 상태인 스레드 수를 반환합니다.
- `static Thread currentThread ()` — 현재 실행 중인 Thread 객체의 참조를 반환합니다.
- `String getName ()` — 이 스레드의 이름을 반환합니다.
- `int getPriority ()` — 이 스레드의 우선 순위를 반환합니다.
- `void interrupt ()` — 이 스레드를 중단합니다.
- `boolean isAlive ()` — 이 스레드가 활성 상태인지 테스트합니다.
- `void join ()` — 이 스레드가 종료될 때까지 기다립니다.
- `void run ()` — 별도의 Runnable 실행 객체를 사용하여 스레드를 구성한 경우 이 Runnable 객체의 run 메소드가 호출됩니다.
- `void setPriority (int newPriority)` — 이 스레드의 우선 순위를 변경합니다.
- `static void sleep (long millis)` — 현재 실행 중인 스레드가 지정된 밀리초 수 동안 중지(일시적으로 실행 중단)되게 합니다.
- `void start ()` — 이 스레드의 실행을 시작하게 합니다.
- `String toString ()` — 스레드의 이름과 우선 순위를 포함하여 이 스레드의 문자열 표현을 반환합니다.
- `static void yield ()` — 현재 실행 중인 스레드 객체가 일시적으로 중지되어 다른 스레드를 실행할 수 있게 합니다.

## 필드 상세

### MIN_PRIORITY

```java
public static final int MIN_PRIORITY
```

**See Also:**
- `Constant Field Values`

### NORM_PRIORITY

```java
public static final int NORM_PRIORITY
```

**See Also:**
- `Constant Field Values`

### MAX_PRIORITY

```java
public static final int MAX_PRIORITY
```

**See Also:**
- `Constant Field Values`

### Thread

```java
public Thread()
```

- 새로운 `Thread` 객체를 할당합니다.

이런 방식으로 만들어진 스레드는 실제로 어떤 작업을 수행하기 위해 
 `run()` 메소드를 무시했을 것입니다.

**See Also:**
- ``Runnable``

### Thread

```java
public Thread(String name)
```

- 지정된 이름을 가진 새로운 `Thread` 객체를 
 할당합니다. 
 
 이런 방식으로 만들어진 스레드는 실제로 어떤 작업을 수행하기 위해 
 `run()` 메소드를 무시했을 것입니다.

**Parameters:**
- `name` - 새로운 스레드의 이름

### Thread

```java
public Thread(Runnable target)
```

- `run` 메소드가 호출되는 특정 대상 객체를 가진 
 새로운 `Thread` 객체를 
 할당합니다.

**Parameters:**
- `target` - `run` 메소드가 호출되는 객체

### Thread

```java
public Thread(Runnable target,
              String name)
```

- 지정된 대상과 이름을 가진 새로운 `Thread` 
 객체를 할당합니다.

**Parameters:**
- `name` - 새로운 스레드의 이름

### currentThread

```java
public static Thread currentThread()
```

**Returns:**
- 현재 실행 중인 스레드

### yield

```java
public static void yield()
```

현재 실행 중인 스레드 객체가 일시적으로 중지되어 
 다른 스레드를 실행할 수 있게 합니다.

### sleep

```java
public static void sleep(long millis)
                  throws InterruptedException
```

**Parameters:**
- `millis` - 중지 시간(밀리초)

**Throws:**
- `InterruptedException` - 다른 스레드가 현재 스레드를 
 중단한 경우. 이 예외가 발생하면 현재 스레드의 
 *중단된 상태*가 지워집니다.

**See Also:**
- ``Object.notify()``

### start

```java
public void start()
```

**Throws:**
- `IllegalThreadStateException` - 스레드를 이미 시작한 
 경우

**See Also:**
- ``run()``

### run

```java
public void run()
```

**Specified by:**
- `run` in interface `Runnable`

**See Also:**
- ``start()``, 
``Runnable.run()``

### interrupt

```java
public void interrupt()
```

**Since:**
- JDK 1.0, CLDC 1.1

### isAlive

```java
public final boolean isAlive()
```

**Returns:**
- 스레드가 활성 상태이면 `true`, 그렇지 않으면 
 `false`

### setPriority

```java
public final void setPriority(int newPriority)
```

**Parameters:**
- `newPriority` - 이 스레드에 설정할 우선 순위

**Throws:**
- `IllegalArgumentException` - 우선 순위가 
 `MIN_PRIORITY`에서 
 `MAX_PRIORITY` 사이의 범위에 없는 경우

**See Also:**
- ``getPriority()``, 
``MAX_PRIORITY``, 
``MIN_PRIORITY``

### getPriority

```java
public final int getPriority()
```

**Returns:**
- 이 스레드의 우선 순위

**See Also:**
- ``setPriority(int)``

### getName

```java
public final String getName()
```

**Returns:**
- 이 스레드의 이름

### activeCount

```java
public static int activeCount()
```

**Returns:**
- 현재 활성 상태인 스레드 수

### join

```java
public final void join()
                throws InterruptedException
```

**Throws:**
- `InterruptedException` - 다른 스레드가 
 현재 스레드를 중단한 경우 이 예외가 
 발생하면 현재 스레드의 *중단된 상태*가 지워집니다.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 스레드의 문자열 표현

## 생성자 상세

### Thread

```java
public Thread()
```

- 새로운 `Thread` 객체를 할당합니다.

이런 방식으로 만들어진 스레드는 실제로 어떤 작업을 수행하기 위해 
 `run()` 메소드를 무시했을 것입니다.

**See Also:**
- ``Runnable``

### Thread

```java
public Thread(String name)
```

- 지정된 이름을 가진 새로운 `Thread` 객체를 
 할당합니다. 
 
 이런 방식으로 만들어진 스레드는 실제로 어떤 작업을 수행하기 위해 
 `run()` 메소드를 무시했을 것입니다.

**Parameters:**
- `name` - 새로운 스레드의 이름

### Thread

```java
public Thread(Runnable target)
```

- `run` 메소드가 호출되는 특정 대상 객체를 가진 
 새로운 `Thread` 객체를 
 할당합니다.

**Parameters:**
- `target` - `run` 메소드가 호출되는 객체

### Thread

```java
public Thread(Runnable target,
              String name)
```

- 지정된 대상과 이름을 가진 새로운 `Thread` 
 객체를 할당합니다.

**Parameters:**
- `name` - 새로운 스레드의 이름

### currentThread

```java
public static Thread currentThread()
```

**Returns:**
- 현재 실행 중인 스레드

### yield

```java
public static void yield()
```

현재 실행 중인 스레드 객체가 일시적으로 중지되어 
 다른 스레드를 실행할 수 있게 합니다.

### sleep

```java
public static void sleep(long millis)
                  throws InterruptedException
```

**Parameters:**
- `millis` - 중지 시간(밀리초)

**Throws:**
- `InterruptedException` - 다른 스레드가 현재 스레드를 
 중단한 경우. 이 예외가 발생하면 현재 스레드의 
 *중단된 상태*가 지워집니다.

**See Also:**
- ``Object.notify()``

### start

```java
public void start()
```

**Throws:**
- `IllegalThreadStateException` - 스레드를 이미 시작한 
 경우

**See Also:**
- ``run()``

### run

```java
public void run()
```

**Specified by:**
- `run` in interface `Runnable`

**See Also:**
- ``start()``, 
``Runnable.run()``

### interrupt

```java
public void interrupt()
```

**Since:**
- JDK 1.0, CLDC 1.1

### isAlive

```java
public final boolean isAlive()
```

**Returns:**
- 스레드가 활성 상태이면 `true`, 그렇지 않으면 
 `false`

### setPriority

```java
public final void setPriority(int newPriority)
```

**Parameters:**
- `newPriority` - 이 스레드에 설정할 우선 순위

**Throws:**
- `IllegalArgumentException` - 우선 순위가 
 `MIN_PRIORITY`에서 
 `MAX_PRIORITY` 사이의 범위에 없는 경우

**See Also:**
- ``getPriority()``, 
``MAX_PRIORITY``, 
``MIN_PRIORITY``

### getPriority

```java
public final int getPriority()
```

**Returns:**
- 이 스레드의 우선 순위

**See Also:**
- ``setPriority(int)``

### getName

```java
public final String getName()
```

**Returns:**
- 이 스레드의 이름

### activeCount

```java
public static int activeCount()
```

**Returns:**
- 현재 활성 상태인 스레드 수

### join

```java
public final void join()
                throws InterruptedException
```

**Throws:**
- `InterruptedException` - 다른 스레드가 
 현재 스레드를 중단한 경우 이 예외가 
 발생하면 현재 스레드의 *중단된 상태*가 지워집니다.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 스레드의 문자열 표현

## 메서드 상세

### currentThread

```java
public static Thread currentThread()
```

**Returns:**
- 현재 실행 중인 스레드

### yield

```java
public static void yield()
```

현재 실행 중인 스레드 객체가 일시적으로 중지되어 
 다른 스레드를 실행할 수 있게 합니다.

### sleep

```java
public static void sleep(long millis)
                  throws InterruptedException
```

**Parameters:**
- `millis` - 중지 시간(밀리초)

**Throws:**
- `InterruptedException` - 다른 스레드가 현재 스레드를 
 중단한 경우. 이 예외가 발생하면 현재 스레드의 
 *중단된 상태*가 지워집니다.

**See Also:**
- ``Object.notify()``

### start

```java
public void start()
```

**Throws:**
- `IllegalThreadStateException` - 스레드를 이미 시작한 
 경우

**See Also:**
- ``run()``

### run

```java
public void run()
```

**Specified by:**
- `run` in interface `Runnable`

**See Also:**
- ``start()``, 
``Runnable.run()``

### interrupt

```java
public void interrupt()
```

**Since:**
- JDK 1.0, CLDC 1.1

### isAlive

```java
public final boolean isAlive()
```

**Returns:**
- 스레드가 활성 상태이면 `true`, 그렇지 않으면 
 `false`

### setPriority

```java
public final void setPriority(int newPriority)
```

**Parameters:**
- `newPriority` - 이 스레드에 설정할 우선 순위

**Throws:**
- `IllegalArgumentException` - 우선 순위가 
 `MIN_PRIORITY`에서 
 `MAX_PRIORITY` 사이의 범위에 없는 경우

**See Also:**
- ``getPriority()``, 
``MAX_PRIORITY``, 
``MIN_PRIORITY``

### getPriority

```java
public final int getPriority()
```

**Returns:**
- 이 스레드의 우선 순위

**See Also:**
- ``setPriority(int)``

### getName

```java
public final String getName()
```

**Returns:**
- 이 스레드의 이름

### activeCount

```java
public static int activeCount()
```

**Returns:**
- 현재 활성 상태인 스레드 수

### join

```java
public final void join()
                throws InterruptedException
```

**Throws:**
- `InterruptedException` - 다른 스레드가 
 현재 스레드를 중단한 경우 이 예외가 
 발생하면 현재 스레드의 *중단된 상태*가 지워집니다.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 스레드의 문자열 표현
