# Class Object

`package java.lang`

```
java.lang.Object
```

## 설명

**public class Object:**

`Object` 클래스는 클래스 계층 구조의 루트입니다. 모든 클래스에는 수퍼 클래스인 `Object`가 있습니다. 배열을 포함한 모든 객체는 이 클래스의 메소드를 구현합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Class``

## 생성자 요약

- Object ()

## 메서드 요약

- `boolean equals ( Object obj)` — 다른 객체가 이 객체와 "같은지" 여부를 나타냅니다.
- `Class getClass ()` — 객체의 런타임 클래스를 반환합니다.
- `int hashCode ()` — 이 객체의 해시 코드 값을 반환합니다.
- `void notify ()` — 이 객체의 모니터에서 대기 중인 문자열 스레드를 실행 가능 상태로 만듭니다.
- `void notifyAll ()` — 이 객체의 모니터에서 대기 중인 모든 스레드를 실행 가능 상태로 만듭니다.
- `String toString ()` — 이 객체의 문자열 표현을 반환합니다.
- `void wait ()` — 다른 스레드가 이 객체의 `notify()` 메소드나 `notifyAll()` 메소드를 호출할 때까지 현재 스레드가 대기하도록 합니다.
- `void wait (long timeout)` — 다른 스레드가 이 객체의 `notify()` 메소드나 `notifyAll()` 메소드를 호출하거나 지정된 시간이 경과할 때까지 현재 스레드가 대기하도록 합니다.
- `void wait (long timeout, int nanos)` — 다른 스레드가 이 객체의 `notify()` 메소드나 `notifyAll()` 메소드를 호출하거나 다른 스레드가 현재 스레드를 중단하거나 특정 실제 시간이 경과할 때까지 현재 스레드가 대기하도록 합니다.

## 생성자 상세

### Object

```java
public Object()
```

### getClass

```java
public final Class getClass()
```

**Returns:**
- 객체의 런타임 클래스를 나타내는 `Class` 유형의 객체

### hashCode

```java
public int hashCode()
```

**Returns:**
- 이 객체의 해시 코드 값

**See Also:**
- ``equals(java.lang.Object)``, 
``Hashtable``

### equals

```java
public boolean equals(Object obj)
```

**Parameters:**
- `obj` - 비교할 참조 객체

**Returns:**
- 이 객체가 obj 인자와 동일하면 `true`, 다르면 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

### toString

```java
public String toString()
```

**Returns:**
- 객체의 문자열 표현

### notify

```java
public final void notify()
```

**Throws:**
- `IllegalMonitorStateException` - 현재 스레드가 객체 모니터의 소유자가 아닌 경우

**See Also:**
- ``notifyAll()``, 
``wait()``

### notifyAll

```java
public final void notifyAll()
```

**Throws:**
- `IllegalMonitorStateException` - 현재 스레드가 객체 모니터의 소유자가 아닌 경우

**See Also:**
- ``notify()``, 
``wait()``

### wait

```java
public final void wait(long timeout)
                throws InterruptedException
```

**Parameters:**
- `timeout` - 최대 대기 시간(밀리초)

**Throws:**
- `InterruptedException` - 다른 스레드가 현재 스레드를 중단한 경우 이 예외가 발생하면 현재 스레드의 *중단된 상태*가 지워집니다.

**See Also:**
- ``notify()``, 
``notifyAll()``

### wait

```java
public final void wait(long timeout,
                       int nanos)
                throws InterruptedException
```

**Parameters:**
- `nanos` - 추가 시간(0-999999 범위의 나노초)

**Throws:**
- `InterruptedException` - 다른 스레드가 현재 스레드를 중단한 경우 이 예외가 발생하면 현재 스레드의 *중단된 상태*가 지워집니다.

### wait

```java
public final void wait()
                throws InterruptedException
```

**Throws:**
- `InterruptedException` - 다른 스레드가 현재 스레드를 중단한 경우 이 예외가 발생하면 현재 스레드의 *중단된 상태*가 지워집니다.

**See Also:**
- ``notify()``, 
``notifyAll()``

## 메서드 상세

### getClass

```java
public final Class getClass()
```

**Returns:**
- 객체의 런타임 클래스를 나타내는 `Class` 유형의 객체

### hashCode

```java
public int hashCode()
```

**Returns:**
- 이 객체의 해시 코드 값

**See Also:**
- ``equals(java.lang.Object)``, 
``Hashtable``

### equals

```java
public boolean equals(Object obj)
```

**Parameters:**
- `obj` - 비교할 참조 객체

**Returns:**
- 이 객체가 obj 인자와 동일하면 `true`, 다르면 `false`

**See Also:**
- ``Boolean.hashCode()``, 
``Hashtable``

### toString

```java
public String toString()
```

**Returns:**
- 객체의 문자열 표현

### notify

```java
public final void notify()
```

**Throws:**
- `IllegalMonitorStateException` - 현재 스레드가 객체 모니터의 소유자가 아닌 경우

**See Also:**
- ``notifyAll()``, 
``wait()``

### notifyAll

```java
public final void notifyAll()
```

**Throws:**
- `IllegalMonitorStateException` - 현재 스레드가 객체 모니터의 소유자가 아닌 경우

**See Also:**
- ``notify()``, 
``wait()``

### wait

```java
public final void wait(long timeout)
                throws InterruptedException
```

**Parameters:**
- `timeout` - 최대 대기 시간(밀리초)

**Throws:**
- `InterruptedException` - 다른 스레드가 현재 스레드를 중단한 경우 이 예외가 발생하면 현재 스레드의 *중단된 상태*가 지워집니다.

**See Also:**
- ``notify()``, 
``notifyAll()``

### wait

```java
public final void wait(long timeout,
                       int nanos)
                throws InterruptedException
```

**Parameters:**
- `nanos` - 추가 시간(0-999999 범위의 나노초)

**Throws:**
- `InterruptedException` - 다른 스레드가 현재 스레드를 중단한 경우 이 예외가 발생하면 현재 스레드의 *중단된 상태*가 지워집니다.

### wait

```java
public final void wait()
                throws InterruptedException
```

**Throws:**
- `InterruptedException` - 다른 스레드가 현재 스레드를 중단한 경우 이 예외가 발생하면 현재 스레드의 *중단된 상태*가 지워집니다.

**See Also:**
- ``notify()``, 
``notifyAll()``
