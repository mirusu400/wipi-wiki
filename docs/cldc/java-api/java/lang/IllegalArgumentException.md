# Class IllegalArgumentException

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
```

## 설명

**Direct Known Subclasses:**
- `IllegalThreadStateException`, `NumberFormatException`

**extends RuntimeException:**

메소드에 유효하지 않거나 잘못된 인자가 
전달되었음을 나타냅니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Thread.setPriority(int)``

## 생성자 요약

- IllegalArgumentException () 세부 정보 메시지 없이 IllegalArgumentException 을 
구성합니다.
- IllegalArgumentException ( String s) 지정한 세부 정보 메시지를 사용하여 IllegalArgumentException 을 
구성합니다.

## 생성자 상세

### IllegalArgumentException

```java
public IllegalArgumentException()
```

- 세부 정보 메시지 없이 `IllegalArgumentException`을 
구성합니다.

### IllegalArgumentException

```java
public IllegalArgumentException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `IllegalArgumentException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
