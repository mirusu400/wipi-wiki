# Class NullPointerException

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
                    +--java.lang.NullPointerException
```

## 설명

**extends RuntimeException:**

객체가 요구되는 경우에 응용 프로그램이 `null`을 사용하려고 
시도하면 발생합니다. 다음과 같은 경우가 포함됩니다.

- `null` 객체의 인스턴스 메소드를 호출하는 경우
- `null` 객체의 필드를 액세스하거나 수정하는 경우
- 배열처럼 `null` 길이를 사용하는 경우
- 배열처럼 `null` 슬롯을 액세스하거나 
 수정하는 경우
- `Throwable` 값처럼 `null`을 
 발생시키는 경우

응용 프로그램은 이 클래스의 인스턴스를 발생시켜 
`null` 객체의 다른 유효하지 않은 사용을 표시합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- NullPointerException () 세부 정보 메시지 없이 NullPointerException 을 구성합니다.
- NullPointerException ( String s) 지정한 세부 정보 메시지를 사용하여 NullPointerException 을 
구성합니다.

## 생성자 상세

### NullPointerException

```java
public NullPointerException()
```

- 세부 정보 메시지 없이 `NullPointerException`을 구성합니다.

### NullPointerException

```java
public NullPointerException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `NullPointerException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
