# Class ArrayIndexOutOfBoundsException

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
                          |
                          +--java.lang.ArrayIndexOutOfBoundsException
```

## 설명

**extends IndexOutOfBoundsException:**

유효하지 않은 색인으로 배열을 액세스했음을 나타냅니다. 
색인이 음수이거나 배열 크기보다 
크거나 같습니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- ArrayIndexOutOfBoundsException () 세부 정보 메시지 없이 ArrayIndexOutOfBoundsException 을 
구성합니다.
- ArrayIndexOutOfBoundsException (int index) 유효하지 않은 색인을 나타내는 인자를 사용하여 새로운 ArrayIndexOutOfBoundsException 클래스를 구성합니다.
- ArrayIndexOutOfBoundsException ( String s) 지정한 세부 정보 메시지를 사용하여 ArrayIndexOutOfBoundsException 클래스를 
구성합니다.

## 생성자 상세

### ArrayIndexOutOfBoundsException

```java
public ArrayIndexOutOfBoundsException()
```

- 세부 정보 메시지 없이 `ArrayIndexOutOfBoundsException`을 
구성합니다.

### ArrayIndexOutOfBoundsException

```java
public ArrayIndexOutOfBoundsException(int index)
```

- 유효하지 않은 색인을 나타내는 인자를 사용하여 새로운 `ArrayIndexOutOfBoundsException` 
클래스를 구성합니다.

**Parameters:**
- `index` - 유효하지 않은 색인

### ArrayIndexOutOfBoundsException

```java
public ArrayIndexOutOfBoundsException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `ArrayIndexOutOfBoundsException` 클래스를 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
