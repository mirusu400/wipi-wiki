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

배열 참조시 배열 범위를 벋어나는 인덱스를 사용할 때 발생하는
 Exception 클래스.

## 생성자 요약

- ArrayIndexOutOfBoundsException () ArrayIndexOutOfBoundsException을 생성한다.
- ArrayIndexOutOfBoundsException (int index) ArrayIndexOutOfBoundsException을 생성한다.
- ArrayIndexOutOfBoundsException ( String s) ArrayIndexOutOfBoundsException을 생성한다.

## 생성자 상세

### ArrayIndexOutOfBoundsException

```java
public ArrayIndexOutOfBoundsException()
```

- ArrayIndexOutOfBoundsException을 생성한다.

### ArrayIndexOutOfBoundsException

```java
public ArrayIndexOutOfBoundsException(String s)
```

**Parameters:**
- `s` - ArrayIndexOutOfBoundsException의 세부 메세지.

### ArrayIndexOutOfBoundsException

```java
public ArrayIndexOutOfBoundsException(int index)
```

**Parameters:**
- `index` - ArrayIndexOutOfBoundsException을 발생시킨 인덱스.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
