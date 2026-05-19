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

문자열내 문자 배열 범위를 벋어나는 영역를 접근하려 할 때 발생하는
 exception 클래스.

## 생성자 요약

- StringIndexOutOfBoundsException () StringIndexOutOfBoundsException객체를 생성한다.
- StringIndexOutOfBoundsException (int index) StringIndexOutOfBoundsException객체를 생성한다.
- StringIndexOutOfBoundsException ( String s) StringIndexOutOfBoundsException객체를 생성한다.

## 생성자 상세

### StringIndexOutOfBoundsException

```java
public StringIndexOutOfBoundsException()
```

- StringIndexOutOfBoundsException객체를 생성한다.

### StringIndexOutOfBoundsException

```java
public StringIndexOutOfBoundsException(String s)
```

**Parameters:**
- `s` - StringIndexOutOfBoundsException의 세부 메세지.

### StringIndexOutOfBoundsException

```java
public StringIndexOutOfBoundsException(int index)
```

**Parameters:**
- `index` - exception을 발생하게 한 인덱스.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
