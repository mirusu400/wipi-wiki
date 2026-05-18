# Class TimerTask

`package java.util`

```text
java.lang.Object
  |
  +--java.util.TimerTask
```

## 설명

**All Implemented Interfaces:**
- `Runnable`

**implements Runnable:**

`Timer`에서 한 번 실행되거나 반복 실행되도록 
예약할 수 있는 작업

**Since:**
- MIDP 1.0

**See Also:**
- ``Timer``

## 생성자 요약

- `protected TimerTask ()` — 새로운 타이머 작업을 만듭니다.

## 메서드 요약

- `boolean cancel ()` — 이 타이머 작업을 취소합니다.
- `abstract  void run ()` — 이 타이머 작업으로 수행되는 작업
- `long scheduledExecutionTime ()` — 이 작업의 최근 실제 실행의 예약된 실행 시간을 반환합니다.

## 생성자 상세

### TimerTask

```java
protected TimerTask()
```

- 새로운 타이머 작업을 만듭니다.

### run

```java
public abstract void run()
```

**Specified by:**
- `run` in interface `Runnable`

**See Also:**
- ``Thread.run()``

### cancel

```java
public boolean cancel()
```

**Returns:**
- 이 작업이 한 번 실행되도록 예약되었지만 실행되지 않았거나 
 반복 실행되도록 예약된 경우 true. 
 작업이 한 번 실행되도록 예약되었으며 
 이미 실행되었거나 작업이 아직 예약되지 않았거나 
 이미 취소된 경우에는 false를 반환합니다. 
 즉, 이 메소드는 하나 이상의 예약된 실행을 수행할 수 없는 경우 
 `true`를 반환합니다.

### scheduledExecutionTime

```java
public long scheduledExecutionTime()
```

**Returns:**
- 이 작업의 최근 실행이 
 예약된 시간(Date.getTime()에서 반환된 형식). 
 작업이 아직 첫 번째 실행을 시작하지 않은 경우에는 
 반환 값이 정의되지 않습니다.

**See Also:**
- ``Date.getTime()``

## 메서드 상세

### run

```java
public abstract void run()
```

**Specified by:**
- `run` in interface `Runnable`

**See Also:**
- ``Thread.run()``

### cancel

```java
public boolean cancel()
```

**Returns:**
- 이 작업이 한 번 실행되도록 예약되었지만 실행되지 않았거나 
 반복 실행되도록 예약된 경우 true. 
 작업이 한 번 실행되도록 예약되었으며 
 이미 실행되었거나 작업이 아직 예약되지 않았거나 
 이미 취소된 경우에는 false를 반환합니다. 
 즉, 이 메소드는 하나 이상의 예약된 실행을 수행할 수 없는 경우 
 `true`를 반환합니다.

### scheduledExecutionTime

```java
public long scheduledExecutionTime()
```

**Returns:**
- 이 작업의 최근 실행이 
 예약된 시간(Date.getTime()에서 반환된 형식). 
 작업이 아직 첫 번째 실행을 시작하지 않은 경우에는 
 반환 값이 정의되지 않습니다.

**See Also:**
- ``Date.getTime()``
