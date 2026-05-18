# Class NumberFormatException

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
                          +--java.lang.NumberFormatException
```

## 설명

**extends IllegalArgumentException:**

응용 프로그램이 문자열을 숫자 유형 중 하나로 변환하려고 
시도했지만 해당 문자열의 형식이 
잘못되었음을 나타냅니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Integer.toString()``

## 생성자 요약

- NumberFormatException () 세부 정보 메시지 없이 NumberFormatException 을 구성합니다.
- NumberFormatException ( String s) 지정한 세부 정보 메시지를 사용하여 NumberFormatException 을
구성합니다.

## 생성자 상세

### NumberFormatException

```java
public NumberFormatException()
```

- 세부 정보 메시지 없이 `NumberFormatException`을 구성합니다.

### NumberFormatException

```java
public NumberFormatException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `NumberFormatException`을
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
