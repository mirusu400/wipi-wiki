# Class NoSuchElementException

`package java.util`

```
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.lang.RuntimeException
                    |
                    +--java.util.NoSuchElementException
```

## 설명

**extends RuntimeException:**

열거에 더 이상 요소가 없음을 나타내기 위해 
`Enumeration`의 `nextElement` 
메소드에서 발생합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Enumeration``, 
``Enumeration.nextElement()``

## 생성자 요약

- NoSuchElementException () null 을 오류 메시지 문자열로 사용하여 NoSuchElementException 을 구성합니다.
- NoSuchElementException ( String s) 오류 메시지 문자열 s 의 참조를 저장하여 
나중에 getMessage 메소드로 검색할 수 있도록 NoSuchElementException 을 구성합니다.

## 생성자 상세

### NoSuchElementException

```java
public NoSuchElementException()
```

- `null`을 오류 메시지 문자열로 사용하여 
`NoSuchElementException`을 구성합니다.

### NoSuchElementException

```java
public NoSuchElementException(String s)
```

- 오류 메시지 문자열 `s`의 참조를 저장하여 
나중에 `getMessage` 메소드로 검색할 수 있도록 
`NoSuchElementException`을 구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
