# Class EmptyStackException

`package java.util`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.lang.RuntimeException
                    |
                    +--java.util.EmptyStackException
```

## 설명

**extends RuntimeException:**

스택이 비어 있음을 나타내기 위해 `Stack` 
클래스의 메소드에서 발생합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Stack``

## 생성자 요약

- EmptyStackException () null 을 오류 메시지 문자열로 사용하여 새로운 EmptyStackException 을 
구성합니다.

## 생성자 상세

### EmptyStackException

```java
public EmptyStackException()
```

- `null`을 오류 메시지 문자열로 사용하여 새로운 `EmptyStackException`을 
구성합니다.
