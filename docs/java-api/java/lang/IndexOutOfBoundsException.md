# Class IndexOutOfBoundsException

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
                    +--java.lang.IndexOutOfBoundsException
```

## 설명

**Direct Known Subclasses:**
- `ArrayIndexOutOfBoundsException`, `StringIndexOutOfBoundsException`

**extends RuntimeException:**

Vector나 문자열, 배열 같이 인데스를 통해 접근가는한 객체에 
 범위 밖의 인덱스를 사용할 때 발생하는 exception 클래스.

## 생성자 요약

- IndexOutOfBoundsException () IndexOutOfBoundsException을 생성한다.
- IndexOutOfBoundsException ( String s) IndexOutOfBoundsException을 생성한다.

## 생성자 상세

### IndexOutOfBoundsException

```java
public IndexOutOfBoundsException()
```

- IndexOutOfBoundsException을 생성한다.

### IndexOutOfBoundsException

```java
public IndexOutOfBoundsException(String s)
```

**Parameters:**
- `s` - IndexOutOfBoundsException의 세부 메세지.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
