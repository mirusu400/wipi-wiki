# Class IllegalMonitorStateException

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.lang.RuntimeException
                    |
                    +--java.lang.IllegalMonitorStateException
```

## 설명

**extends RuntimeException:**

스레드가 객체의 모니터에서 대기하거나, 
지정된 모니터를 소유하지 않고 객체의 모니터에서 대기 중인 
다른 스레드에게 알리려고 시도했음을 나타냅니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Object.notify()``, 
``Object.notifyAll()``, 
``Object.wait()``, 
``Object.wait(long)``, 
``Object.wait(long, int)``

## 생성자 요약

- IllegalMonitorStateException () 세부 정보 메시지 없이 IllegalMonitorStateException 을 
구성합니다.
- IllegalMonitorStateException ( String s) 지정한 세부 정보 메시지를 사용하여 IllegalMonitorStateException 을 
구성합니다.

## 생성자 상세

### IllegalMonitorStateException

```java
public IllegalMonitorStateException()
```

- 세부 정보 메시지 없이 `IllegalMonitorStateException`을 
구성합니다.

### IllegalMonitorStateException

```java
public IllegalMonitorStateException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `IllegalMonitorStateException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
