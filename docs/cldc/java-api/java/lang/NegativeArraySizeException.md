# Class NegativeArraySizeException

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
                    +--java.lang.NegativeArraySizeException
```

## 설명

**extends RuntimeException:**

응용 프로그램이 음수 크기를 사용하여 배열을 만들려고 시도하면 발생합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- NegativeArraySizeException () 세부 정보 메시지 없이 NegativeArraySizeException 을 
구성합니다.
- NegativeArraySizeException ( String s) 지정한 세부 정보 메시지를 사용하여 NegativeArraySizeException 을 
구성합니다.

## 생성자 상세

### NegativeArraySizeException

```java
public NegativeArraySizeException()
```

- 세부 정보 메시지 없이 `NegativeArraySizeException`을 
구성합니다.

### NegativeArraySizeException

```java
public NegativeArraySizeException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `NegativeArraySizeException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
