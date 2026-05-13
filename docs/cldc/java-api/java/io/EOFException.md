# Class EOFException

`package java.io`

```
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.io.IOException
                    |
                    +--java.io.EOFException
```

## 설명

**extends IOException:**

입력 중에 예기치 않게 파일 또는 
스트림의 끝에 도달하였음을 나타냅니다.

이 예외는 주로 데이터 입력 스트림에서 사용됩니다. 
일반적으로 데이터 입력 스트림은 특정 형식의 이진 파일을 예상하며 
스트림의 끝에 도달하는 경우는 거의 없습니다. 
다른 입력 스트림은 대부분 스트림의 끝에서 특수 값을 반환합니다.

파일의 끝에 도달할 때 예외를 발생시키지 않고 
고유 값(예: `-1`)을 
반환하는 입력 작업도 있습니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``DataInputStream``, 
``IOException``

## 생성자 요약

- EOFException () null 을 오류 세부 정보 메시지로 사용하여 EOFException 을 구성합니다.
- EOFException ( String s) 지정한 세부 정보 메시지를 사용하여 EOFException 을 구성합니다.

## 생성자 상세

### EOFException

```java
public EOFException()
```

- `null`을 오류 세부 정보 메시지로 사용하여 
`EOFException`을 구성합니다.

### EOFException

```java
public EOFException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 
`EOFException`을 구성합니다. 
문자열 `s`는 나중에 `java.lang.Throwable` 클래스의 
`Throwable.getMessage()` 메소드로 검색할 수 있습니다.

**Parameters:**
- `s` - 세부 정보 메시지
