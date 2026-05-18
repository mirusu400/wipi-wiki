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

A task that can be scheduled for one-time or repeated execution by a
 `Timer`.

**Since:**
- 1.3

**See Also:**
- ``Timer``

## 생성자 요약

- `protected TimerTask ()`

## 메서드 요약

- `boolean cancel ()`
- `abstract  void run ()` — Thread.start에 의해 run메소스가 호출된다.
- `long scheduledExecutionTime ()`

## 생성자 상세

### TimerTask

```java
protected TimerTask()
```

### run

```java
public abstract void run()
```

- **Description copied from interface: `Runnable`**

**Specified by:**
- `run` in interface `Runnable`

### cancel

```java
public boolean cancel()
```

### scheduledExecutionTime

```java
public long scheduledExecutionTime()
```## 메서드 상세

### run

```java
public abstract void run()
```

- **Description copied from interface: `Runnable`**

**Specified by:**
- `run` in interface `Runnable`

### cancel

```java
public boolean cancel()
```

### scheduledExecutionTime

```java
public long scheduledExecutionTime()
```

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
