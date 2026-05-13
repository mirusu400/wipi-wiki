# Class IllegalThreadStateException

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
                    +--java.lang.IllegalArgumentException
                          |
                          +--java.lang.IllegalThreadStateException
```

## 설명

**extends IllegalArgumentException:**

쓰레드의 현 상태가 주어진 동작을 취하기에 적절치않은 경우에
 발생하는 exception 클래스.

## 생성자 요약

- IllegalThreadStateException () IllegalThreadStateException을 생성한다.
- IllegalThreadStateException ( String s) IllegalThreadStateException을 생성한다.

## 생성자 상세

### IllegalThreadStateException

```java
public IllegalThreadStateException()
```

- IllegalThreadStateException을 생성한다.

### IllegalThreadStateException

```java
public IllegalThreadStateException(String s)
```

**Parameters:**
- `s` - IllegalThreadStateException의 세부 메세지.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
