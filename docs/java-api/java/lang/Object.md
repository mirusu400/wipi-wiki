# Class Object

`package java.lang`

```
java.lang.Object
```

## 설명

**public class Object:**

Java 클래스 계층의 루트 클래스.

## 생성자 요약

- Object ()

## 메서드 요약

- `boolean equals ( Object o)` — 현 객체와 매개변수로 전달된 객체 값이 일치함을 검사한다.
- `Class getClass ()` — 현 객체의 클래스를 구한다.
- `int hashCode ()` — 현 객체의 해쉬코드 값을 구한다.
- `void notify ()` — 현 객체에 대해 wait하고 있는 쓰레드들 중 하나를 깨운다.
- `void notifyAll ()` — 현 객체에 대해 wait하고 있는 쓰레드를 모두 깨운다.
- `String toString ()` — 현 객체를 나타내는 문자열을 구한다.
- `void wait ()` — 다른 쓰레드가 notify나 notifyAll할 때 까지 wait한다.
- `void wait (long ms)` — 다른 쓰레드가 notify나 notifyAll할 때 까지 wait한다.
- `void wait (long ms, int ns)` — 다른 쓰레드가 notify나 notifyAll할 때 까지 wait한다.

## 생성자 상세

### Object

```java
public Object()
```

### equals

```java
public boolean equals(Object o)
```

**Parameters:**
- `obj` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### getClass

```java
public final Class getClass()
```

**Returns:**
- java.lang.Class형인 현 객체의 클래스 객체.

### hashCode

```java
public int hashCode()
```

**Returns:**
- 현 객체의 정수형 해쉬코드.

### notify

```java
public final void notify()
```

- 현 객체에 대해 wait하고 있는 쓰레드들 중 하나를 깨운다.

### notifyAll

```java
public final void notifyAll()
```

- 현 객체에 대해 wait하고 있는 쓰레드를 모두 깨운다.

### toString

```java
public String toString()
```

**Returns:**
- 현 객체를 나타내는 문자열.

### wait

```java
public final void wait()
                throws IllegalMonitorStateException,
                       InterruptedException
```

**Throws:**
- `InterruptedException` - 다른 쓰레드가 현 쓰레드를 interrupt했을 때 발생.

### wait

```java
public final void wait(long ms)
                throws IllegalMonitorStateException,
                       InterruptedException
```

**Parameters:**
- `ms` - Long타입의 timeout milliseconds 시간.

**Throws:**
- `InterruptedException` - 다른 쓰레드가 현 쓰레드를 interrupt했을 때 발생.

### wait

```java
public final void wait(long ms,
                       int ns)
                throws IllegalMonitorStateException,
                       InterruptedException
```

**Parameters:**
- `ns` - Int타입의 timeout nanoseconds 시간.

**Throws:**
- `InterruptedException` - 다른 쓰레드가 현 쓰레드를 interrupt했을 때 발생.## 메서드 상세

### equals

```java
public boolean equals(Object o)
```

**Parameters:**
- `obj` - 비교할 대상.

**Returns:**
- 두 객체가 모두 같은 값을 가지면 참 아니면 거짓.

### getClass

```java
public final Class getClass()
```

**Returns:**
- java.lang.Class형인 현 객체의 클래스 객체.

### hashCode

```java
public int hashCode()
```

**Returns:**
- 현 객체의 정수형 해쉬코드.

### notify

```java
public final void notify()
```

- 현 객체에 대해 wait하고 있는 쓰레드들 중 하나를 깨운다.

### notifyAll

```java
public final void notifyAll()
```

- 현 객체에 대해 wait하고 있는 쓰레드를 모두 깨운다.

### toString

```java
public String toString()
```

**Returns:**
- 현 객체를 나타내는 문자열.

### wait

```java
public final void wait()
                throws IllegalMonitorStateException,
                       InterruptedException
```

**Throws:**
- `InterruptedException` - 다른 쓰레드가 현 쓰레드를 interrupt했을 때 발생.

### wait

```java
public final void wait(long ms)
                throws IllegalMonitorStateException,
                       InterruptedException
```

**Parameters:**
- `ms` - Long타입의 timeout milliseconds 시간.

**Throws:**
- `InterruptedException` - 다른 쓰레드가 현 쓰레드를 interrupt했을 때 발생.

### wait

```java
public final void wait(long ms,
                       int ns)
                throws IllegalMonitorStateException,
                       InterruptedException
```

**Parameters:**
- `ns` - Int타입의 timeout nanoseconds 시간.

**Throws:**
- `InterruptedException` - 다른 쓰레드가 현 쓰레드를 interrupt했을 때 발생.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
