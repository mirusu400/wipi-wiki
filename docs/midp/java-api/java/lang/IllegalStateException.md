# Class IllegalStateException

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
                    +--java.lang.IllegalStateException
```

## 설명

**extends RuntimeException:**

메소드가 부적절하거나 
잘못된 시간에 호출되었음을 나타냅니다. 
즉, Java 환경이나 Java 응용 프로그램이 
요청된 작업에 적합한 상태가 아닙니다.

**Since:**
- MIDP 1.0

## 생성자 요약

- IllegalStateException () 세부 정보 메시지 없이 IllegalStateException을 구성합니다.
- IllegalStateException ( String s) 지정한 세부 정보 메시지를 사용하여 
IllegalStateException을 구성합니다.

## 생성자 상세

### IllegalStateException

```java
public IllegalStateException()
```

- 세부 정보 메시지 없이 IllegalStateException을 구성합니다.

### IllegalStateException

```java
public IllegalStateException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 
IllegalStateException을 구성합니다. 
세부 정보 메시지는 특정 예외를 설명하는 문자열입니다.

**Parameters:**
- `s` - 세부 정보 메시지가 포함되는 문자열
