# Class MediaException

`package javax.microedition.media`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--javax.microedition.media.MediaException
```

## 설명

**extends Exception:**

`MediaException`은 메소드에 예기치 않은 
오류 조건이 있음을 나타냅니다.

## 생성자 요약

- MediaException () null 을 오류 세부 정보 메시지로 사용하여 MediaException 을 구성합니다.
- MediaException ( String reason) 지정한 세부 정보 메시지를 사용하여 MediaException 을 구성합니다.

## 생성자 상세

### MediaException

```java
public MediaException()
```

- `null`을 오류 세부 정보 메시지로 사용하여 
`MediaException`을 구성합니다.

### MediaException

```java
public MediaException(String reason)
```

- 지정한 세부 정보 메시지를 사용하여 `MediaException`을 구성합니다. 
오류 메시지 문자열 `s`는 나중에 
`java.lang.Throwable` 클래스의 
`Throwable.getMessage()` 메소드로 
검색할 수 있습니다.

**Parameters:**
- `reason` - 세부 정보 메시지
