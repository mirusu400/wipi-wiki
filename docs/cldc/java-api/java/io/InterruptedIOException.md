# Class InterruptedIOException

`package java.io`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.io.IOException
                    |
                    +--java.io.InterruptedIOException
```

## 설명

**extends IOException:**

I/O 작업이 중단되었음을 나타냅니다. 
`InterruptedIOException`이 발생하여 
입력 또는 출력 전송을 수행하는 스레드가 종료되어 
전송 작업이 종료되었음을 나타냅니다. ``bytesTransferred`` 필드는 
작업이 중단되기 전에 성공적으로 
전송된 바이트 수를 표시합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``InputStream``, 
``OutputStream``

## 필드 요약

- `int bytesTransferred` — 작업이 중단되기 전에 I/O 작업의 일부로 전송된 바이트 수를 보고합니다.

## 생성자 요약

- InterruptedIOException () null 을 오류 세부 정보 메시지로 사용하여 InterruptedIOException 을 구성합니다.
- InterruptedIOException ( String s) 지정한 세부 정보 메시지를 사용하여 InterruptedIOException 을 구성합니다.

## 필드 상세

### bytesTransferred

```java
public int bytesTransferred
```

- 작업이 중단되기 전에 I/O 작업의 일부로 
전송된 바이트 수를 보고합니다.

### InterruptedIOException

```java
public InterruptedIOException()
```

- `null`을 오류 세부 정보 메시지로 사용하여
`InterruptedIOException`을 구성합니다.

### InterruptedIOException

```java
public InterruptedIOException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 
`InterruptedIOException`을 구성합니다. 
문자열 `s`는 나중에 `java.lang.Throwable` 클래스의 
`Throwable.getMessage()` 
메소드로 검색할 수 있습니다.

**Parameters:**
- `s` - 세부 정보 메시지

## 생성자 상세

### InterruptedIOException

```java
public InterruptedIOException()
```

- `null`을 오류 세부 정보 메시지로 사용하여
`InterruptedIOException`을 구성합니다.

### InterruptedIOException

```java
public InterruptedIOException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 
`InterruptedIOException`을 구성합니다. 
문자열 `s`는 나중에 `java.lang.Throwable` 클래스의 
`Throwable.getMessage()` 
메소드로 검색할 수 있습니다.

**Parameters:**
- `s` - 세부 정보 메시지
