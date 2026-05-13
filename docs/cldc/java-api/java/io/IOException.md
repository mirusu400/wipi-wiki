# Class IOException

`package java.io`

```
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.io.IOException
```

## 설명

**Direct Known Subclasses:**
- `ConnectionNotFoundException`, `EOFException`, `InterruptedIOException`, `UnsupportedEncodingException`, `UTFDataFormatException`

**extends Exception:**

일종의 I/O 예외가 발생했음을 나타냅니다. 
이 클래스는 실패 또는 인터럽트된 I/O 작업에서 
생성되는 일반 예외 클래스입니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``InputStream``, 
``OutputStream``

## 생성자 요약

- IOException () null 을 오류 세부 정보 메시지로 사용하여 IOException 을 구성합니다.
- IOException ( String s) 지정한 세부 정보 메시지를 사용하여 IOException 을 구성합니다.

## 생성자 상세

### IOException

```java
public IOException()
```

- `null`을 오류 세부 정보 메시지로 사용하여 
`IOException`을 구성합니다.

### IOException

```java
public IOException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `IOException`을 구성합니다. 
오류 메시지 문자열 `s`는 나중에 `java.lang.Throwable` 클래스의 
`Throwable.getMessage()` 메소드로 
검색할 수 있습니다.

**Parameters:**
- `s` - 세부 정보 메시지
