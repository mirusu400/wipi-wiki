# Class Exception

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
```

## 설명

**Direct Known Subclasses:**
- `ClassNotFoundException`, `IllegalAccessException`, `InstantiationException`, `InterruptedException`, `IOException`, `RuntimeException`

**extends Throwable:**

`Exception` 클래스와 해당 서브 클래스는 합리적 
응용 프로그램이라면 파악해야 하는 동작을 나타내는 
`Throwable`의 한 형태입니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Error``

## 생성자 요약

- Exception () 지정한 세부 정보 메시지 없이 Exception 을 구성합니다.
- Exception ( String s) 지정한 세부 정보 메시지를 사용하여 Exception 을 구성합니다.

## 생성자 상세

### Exception

```java
public Exception()
```

- 지정한 세부 정보 메시지 없이 `Exception`을 구성합니다.

### Exception

```java
public Exception(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `Exception`을 구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
