# Class IndexOutOfBoundsException

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
                    +--java.lang.IndexOutOfBoundsException
```

## 설명

**Direct Known Subclasses:**
- `ArrayIndexOutOfBoundsException`, `StringIndexOutOfBoundsException`

**extends RuntimeException:**

배열, 문자열 또는 벡터 등에 대한 색인이 
범위를 벗어났음을 나타냅니다.

응용 프로그램은 유사한 예외를 나타내기 위해 이 클래스의 서브 클래스를 구성할 수 있습니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- IndexOutOfBoundsException () 세부 정보 메시지 없이 IndexOutOfBoundsException 을 
구성합니다.
- IndexOutOfBoundsException ( String s) 지정한 세부 정보 메시지를 사용하여 IndexOutOfBoundsException 을 
구성합니다.

## 생성자 상세

### IndexOutOfBoundsException

```java
public IndexOutOfBoundsException()
```

- 세부 정보 메시지 없이 `IndexOutOfBoundsException`을 
구성합니다.

### IndexOutOfBoundsException

```java
public IndexOutOfBoundsException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `IndexOutOfBoundsException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
