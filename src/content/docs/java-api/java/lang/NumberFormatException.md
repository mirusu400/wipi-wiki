---
title: "Class NumberFormatException"
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
                    +--java.lang.IllegalArgumentException
                          |
                          +--java.lang.NumberFormatException
```

## 설명

**extends IllegalArgumentException:**

문자열을 정수나 Long형으로 변환할 때 문자열이 변환될 수 없을 때 
 발생하는 exception 클래스.

## 생성자 요약

- NumberFormatException () NumberFormatException을 생성한다.
- NumberFormatException ( String s) NumberFormatException을 생성한다.

## 생성자 상세

### NumberFormatException

```java
public NumberFormatException()
```

- NumberFormatException을 생성한다.

### NumberFormatException

```java
public NumberFormatException(String s)
```

**Parameters:**
- `s` - NumberFormatException의 세부 메세지.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
