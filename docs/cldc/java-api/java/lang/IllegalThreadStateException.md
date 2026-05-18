# Class IllegalThreadStateException

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.lang.RuntimeException
                    |
                    +--java.lang.IllegalArgumentException
                          |
                          +--java.lang.IllegalThreadStateException
```

## 설명

**extends IllegalArgumentException:**

스레드가 요청된 작업에 적합한 상태가 아님을 나타냅니다. 
예를 들어, `Thread` 클래스의 
`suspend` 및 `resume` 
메소드를 참조하십시오.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- IllegalThreadStateException () 세부 정보 메시지 없이 IllegalThreadStateException 을 
구성합니다.
- IllegalThreadStateException ( String s) 지정한 세부 정보 메시지를 사용하여 IllegalThreadStateException 을 
구성합니다.

## 생성자 상세

### IllegalThreadStateException

```java
public IllegalThreadStateException()
```

- 세부 정보 메시지 없이 `IllegalThreadStateException`을 
구성합니다.

### IllegalThreadStateException

```java
public IllegalThreadStateException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `IllegalThreadStateException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
