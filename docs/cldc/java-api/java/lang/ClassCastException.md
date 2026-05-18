# Class ClassCastException

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
                    +--java.lang.ClassCastException
```

## 설명

**extends RuntimeException:**

코드가 객체를 인스턴스가 아닌 서브 클래스로 캐스트하려고 시도했음을 
나타냅니다. 예를 들어, 다음 코드는 `ClassCastException`을 
생성합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- ClassCastException () 세부 정보 메시지 없이 ClassCastException 을 구성합니다.
- ClassCastException ( String s) 지정한 세부 정보 메시지를 사용하여 ClassCastException 을 
구성합니다.

## 생성자 상세

### ClassCastException

```java
public ClassCastException()
```

- 세부 정보 메시지 없이 `ClassCastException`을 구성합니다.

### ClassCastException

```java
public ClassCastException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `ClassCastException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
