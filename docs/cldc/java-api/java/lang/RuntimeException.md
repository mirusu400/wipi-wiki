# Class RuntimeException

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.lang.RuntimeException
```

## 설명

**Direct Known Subclasses:**
- `ArithmeticException`, `ArrayStoreException`, `ClassCastException`, `EmptyStackException`, `IllegalArgumentException`, `IllegalMonitorStateException`, `IndexOutOfBoundsException`, `NegativeArraySizeException`, `NoSuchElementException`, `NullPointerException`, `SecurityException`

**extends Exception:**

`RuntimeException`은 Java 
가상 머신의 정상 작동 중에 
발생할 수 있는 예외 수퍼 클래스입니다.

메소드는 해당 메소드 실행 중에 발생할 수는 있지만 파악되지 않는 
`RuntimeException`의 서브 클래스를 `throws` 절에 
선언할 필요가 없습니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- RuntimeException () 세부 정보 메시지 없이 RuntimeException 을 구성합니다.
- RuntimeException ( String s) 지정한 세부 정보 메시지를 사용하여 RuntimeException 을 
구성합니다.

## 생성자 상세

### RuntimeException

```java
public RuntimeException()
```

- 세부 정보 메시지 없이 `RuntimeException`을 구성합니다.

### RuntimeException

```java
public RuntimeException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `RuntimeException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
