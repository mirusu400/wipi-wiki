# Class Timer

`package java.util`

```
java.lang.Object
  |
  +--java.util.Timer
```

## 설명

**extends Object:**

스레드가 백그라운드 스레드에서 나중에 실행할 작업을 예약할 수 있는 기능입니다. 
작업은 한 번 실행되거나 정기적인 간격으로 
반복 실행되도록 예약할 수 있습니다.

각 `Timer` 객체에는 모든 타이머 작업을 순차적으로 
실행하는 데 사용되는 단일 백그라운드 스레드가 있습니다. 
타이머 작업은 신속하게 완료해야 합니다. 
타이머 작업을 완료하는 데 시간이 너무 오래 걸리면 이 타이머의 
작업 실행 스레드가 "호그"됩니다. 
이 경우 이후 작업의 실행도 지연되므로 위반 작업이 최종적으로 완료되면 
모든 작업이 "쌓여서" 연속적으로 빠르게 실행될 수도 있습니다.

`Timer` 객체에 대한 마지막 라이브 참조가 사라지고 
아직 해결되지 않은 모든 작업의 실행이 완료되면 타이머의 
작업 실행 스레드가 정상적으로 종료되고 가비지 컬렉션이 적용됩니다. 
하지만 이렇게 되기까지 오랜 시간이 걸릴 수 있습니다. 
기본적으로 작업 실행 스레드는 *데몬 스레드*로 실행되지 않으므로 
응용 프로그램이 종료되지 않도록 방지할 수 있습니다. 
타이머의 작업 실행 스레드를 신속하게 종료하려면 호출자는 
타이머의 `cancel` 메소드를 호출해야 합니다.

타이머의 작업 실행 스레드가 
예상치 않게 종료된 경우 이후에 
타이머에서 작업을 예약하려고 시도하면 
타이머의 `cancel` 메소드를 
호출한 것처럼 `IllegalStateException`이 발생합니다.

이 클래스는 스레드 안정성이 높으므로 다수의 스레드가 
외부 동기화 없이도 단일 `Timer` 객체를 공유할 수 있습니다.

또한 이 클래스는 실시간 보증을 제공하지 *않으므로*
`Object.wait(long)` 메소드를 사용하여 작업을 예약합니다. 
타이머는 구현 및 장치별로 다르게 결정됩니다.

타이머는 단일 가상 머신 내에서만 작동하며 가상 머신을 종료하면 취소됩니다. 
가상 머신을 시작할 때 타이머가 없으면 
응용 프로그램 요청에 의해서만 만들어집니다.

**Since:**
- MIDP 1.0

**See Also:**
- ``TimerTask``, 
``Object.wait(long)``

## 생성자 요약

- Timer () 새로운 타이머를 만듭니다.

## 메서드 요약

- `void cancel ()` — 이 타이머를 종료하고 현재 예약된 모든 작업을 삭제합니다.
- `void schedule ( TimerTask task, Date time)` — 지정된 시간에 지정된 작업이 실행되도록 예약합니다.
- `void schedule ( TimerTask task, Date firstTime, long period)` — 지정된 시간부터 지정된 작업이 고정 지연 실행 을 반복하도록 예약합니다.
- `void schedule ( TimerTask task, long delay)` — 지정된 지연 후에 지정된 작업이 실행되도록 예약합니다.
- `void schedule ( TimerTask task, long delay, long period)` — 지정된 지연 후부터 지정된 작업이 고정 지연 실행 을 반복하도록 예약합니다.
- `void scheduleAtFixedRate ( TimerTask task, Date firstTime, long period)` — 지정된 시간부터 지정된 작업이 고정 속도 실행 을 반복하도록 예약합니다.
- `void scheduleAtFixedRate ( TimerTask task, long delay, long period)` — 지정한 지연 후부터 지정한 작업이 고정 속도 실행 을 반복하도록 예약합니다.

## 생성자 상세

### Timer

```java
public Timer()
```

- 새로운 타이머를 만듭니다. 
연결된 스레드는 데몬 스레드로 실행되지 *않으므로* 응용 프로그램이 종료되지 않도록 방지할 수 있습니다.

**See Also:**
- ``Thread``, 
``cancel()``

### schedule

```java
public void schedule(TimerTask task,
                     long delay)
```

**Parameters:**
- `delay` - 작업이 실행되기 전의 지연(밀리초) 
 타이머는 구현 및 장치별로 다르게 결정되기 때문에 
 실제 지연은 요청된 시간과 
 다를 수도 있습니다.

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소된 경우

### schedule

```java
public void schedule(TimerTask task,
                     Date time)
```

**Parameters:**
- `time` - 작업이 실행되는 시간

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소되었거나 타이머 스레드가 종료된 경우

### schedule

```java
public void schedule(TimerTask task,
                     long delay,
                     long period)
```

**Parameters:**
- `period` - 연속 작업 실행 사이의 시간(밀리초)

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소되었거나 타이머 스레드가 종료된 경우

### schedule

```java
public void schedule(TimerTask task,
                     Date firstTime,
                     long period)
```

**Parameters:**
- `period` - 연속 작업 실행 사이의 시간(밀리초)

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소되었거나 타이머 스레드가 종료된 경우

### scheduleAtFixedRate

```java
public void scheduleAtFixedRate(TimerTask task,
                                long delay,
                                long period)
```

**Parameters:**
- `period` - 연속 작업 실행 사이의 시간(밀리초)

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소되었거나 타이머 스레드가 종료된 경우

### scheduleAtFixedRate

```java
public void scheduleAtFixedRate(TimerTask task,
                                Date firstTime,
                                long period)
```

**Parameters:**
- `period` - 연속 작업 실행 사이의 시간(밀리초)

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소되었거나 타이머 스레드가 종료된 경우

### cancel

```java
public void cancel()
```

이 타이머를 종료하고 현재 예약된 모든 작업을 삭제합니다. 
현재 실행 중인 작업은 중단하지 않습니다. 
타이머가 종료되면 해당 실행 스레드도 함께 종료되어 
더 이상 작업을 예약할 수 없습니다. 이 타이머에서 호출한 타이머 작업의 run 메소드 내에서 
이 메소드를 호출하면 현재 실행 중인 작업이 
이 타이머에서 실행되는 
마지막 작업이 됩니다. 이 메소드는 반복해서 호출할 수 있지만 
두 번째 및 이후 호출 시에는 어떤 변화도 없습니다.

## 메서드 상세

### schedule

```java
public void schedule(TimerTask task,
                     long delay)
```

**Parameters:**
- `delay` - 작업이 실행되기 전의 지연(밀리초) 
 타이머는 구현 및 장치별로 다르게 결정되기 때문에 
 실제 지연은 요청된 시간과 
 다를 수도 있습니다.

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소된 경우

### schedule

```java
public void schedule(TimerTask task,
                     Date time)
```

**Parameters:**
- `time` - 작업이 실행되는 시간

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소되었거나 타이머 스레드가 종료된 경우

### schedule

```java
public void schedule(TimerTask task,
                     long delay,
                     long period)
```

**Parameters:**
- `period` - 연속 작업 실행 사이의 시간(밀리초)

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소되었거나 타이머 스레드가 종료된 경우

### schedule

```java
public void schedule(TimerTask task,
                     Date firstTime,
                     long period)
```

**Parameters:**
- `period` - 연속 작업 실행 사이의 시간(밀리초)

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소되었거나 타이머 스레드가 종료된 경우

### scheduleAtFixedRate

```java
public void scheduleAtFixedRate(TimerTask task,
                                long delay,
                                long period)
```

**Parameters:**
- `period` - 연속 작업 실행 사이의 시간(밀리초)

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소되었거나 타이머 스레드가 종료된 경우

### scheduleAtFixedRate

```java
public void scheduleAtFixedRate(TimerTask task,
                                Date firstTime,
                                long period)
```

**Parameters:**
- `period` - 연속 작업 실행 사이의 시간(밀리초)

**Throws:**
- `IllegalStateException` - 작업이 이미 예약 또는 취소되었거나 
 타이머가 취소되었거나 타이머 스레드가 종료된 경우

### cancel

```java
public void cancel()
```

이 타이머를 종료하고 현재 예약된 모든 작업을 삭제합니다. 
현재 실행 중인 작업은 중단하지 않습니다. 
타이머가 종료되면 해당 실행 스레드도 함께 종료되어 
더 이상 작업을 예약할 수 없습니다. 이 타이머에서 호출한 타이머 작업의 run 메소드 내에서 
이 메소드를 호출하면 현재 실행 중인 작업이 
이 타이머에서 실행되는 
마지막 작업이 됩니다. 이 메소드는 반복해서 호출할 수 있지만 
두 번째 및 이후 호출 시에는 어떤 변화도 없습니다.
