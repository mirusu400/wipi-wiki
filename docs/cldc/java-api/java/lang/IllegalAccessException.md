# Class IllegalAccessException

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.lang.IllegalAccessException
```

## 설명

**extends Exception:**

응용 프로그램이 클래스를 로드하려고 시도하지만 
클래스가 공용이 아니고 
다른 패키지에 있기 때문에 현재 실행 중인 메소드가 지정된 
클래스의 정의에 액세스할 수 없을 때 발생합니다.

이 클래스의 인스턴스는 응용 프로그램이 
`Class` 클래스의 `newInstance` 
메소드를 사용하여 클래스의 인스턴스를 만들려고 시도하지만 
인자가 0인 해당 구성자를 현재 메소드가 액세스할 수 없는 경우에도 
발생할 수 있습니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Class.forName(java.lang.String)``, 
``Class.newInstance()``

## 생성자 요약

- IllegalAccessException () 세부 정보 메시지 없이 IllegalAccessException 을 
구성합니다.
- IllegalAccessException ( String s) 세부 정보 메시지를 사용하여 IllegalAccessException 을 구성합니다.

## 생성자 상세

### IllegalAccessException

```java
public IllegalAccessException()
```

- 세부 정보 메시지 없이 `IllegalAccessException`을 
구성합니다.

### IllegalAccessException

```java
public IllegalAccessException(String s)
```

- 세부 정보 메시지를 사용하여 `IllegalAccessException`을 구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
