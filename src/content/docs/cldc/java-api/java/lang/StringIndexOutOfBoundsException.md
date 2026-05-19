---
title: "Class StringIndexOutOfBoundsException"
---

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
                          +--java.lang.StringIndexOutOfBoundsException
```

## 설명

**extends IndexOutOfBoundsException:**

색인이 음수이거나 문자열 크기보다 크거나 같다는 것을 나타내기 위해 
 `String` 클래스의 `charAt` 
 메소드와 다른 `String` 
 메소드에서 발생합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``String.charAt(int)``

## 생성자 요약

- StringIndexOutOfBoundsException () 세부 정보 메시지 없이 StringIndexOutOfBoundsException 을 
 구성합니다.
- StringIndexOutOfBoundsException (int index) 유효하지 않은 색인을 표시하는 인자를 사용하여 새로운 StringIndexOutOfBoundsException 클래스를 구성합니다.
- StringIndexOutOfBoundsException ( String s) 지정한 세부 정보 메시지를 사용하여 StringIndexOutOfBoundsException 을 
 구성합니다.

## 생성자 상세

### StringIndexOutOfBoundsException

```java
public StringIndexOutOfBoundsException()
```

- 세부 정보 메시지 없이 `StringIndexOutOfBoundsException`을 
 구성합니다.

**Since:**
- JDK1.0

### StringIndexOutOfBoundsException

```java
public StringIndexOutOfBoundsException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `StringIndexOutOfBoundsException`을 
 구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지

### StringIndexOutOfBoundsException

```java
public StringIndexOutOfBoundsException(int index)
```

- 유효하지 않은 색인을 표시하는 인자를 사용하여 새로운 
 `StringIndexOutOfBoundsException` 클래스를 구성합니다.

**Parameters:**
- `index` - 유효하지 않은 색인
