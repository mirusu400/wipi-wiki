# Class UnsupportedEncodingException

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
                    +--java.io.UnsupportedEncodingException
```

## 설명

**extends IOException:**

문자 인코딩은 지원되지 않습니다.

**Since:**
- JDK1.1, CLDC 1.0

## 생성자 요약

- UnsupportedEncodingException () 세부 정보 메시지 없이 UnsupportedEncodingException을 구성합니다.
- UnsupportedEncodingException ( String s) 세부 정보 메시지를 사용하여 UnsupportedEncodingException을 구성합니다.

## 생성자 상세

### UnsupportedEncodingException

```java
public UnsupportedEncodingException()
```

- 세부 정보 메시지 없이 UnsupportedEncodingException을 구성합니다.

### UnsupportedEncodingException

```java
public UnsupportedEncodingException(String s)
```

- 세부 정보 메시지를 사용하여 UnsupportedEncodingException을 구성합니다.

**Parameters:**
- `s` - 예외 이유를 설명합니다.
