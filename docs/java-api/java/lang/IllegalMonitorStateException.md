# Class IllegalMonitorStateException

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
                    +--java.lang.IllegalMonitorStateException
```

## 설명

**extends RuntimeException:**

한 쓰레드가 소유하지 않은 모니터를 사용해서 wait아 notify를 할 때 
 발생하는 exception 클래스.

## 생성자 요약

- IllegalMonitorStateException () IllegalMonitorStateException을 생성한다.
- IllegalMonitorStateException ( String s) IllegalMonitorStateException을 생성한다.

## 생성자 상세

### IllegalMonitorStateException

```java
public IllegalMonitorStateException()
```

- IllegalMonitorStateException을 생성한다.

### IllegalMonitorStateException

```java
public IllegalMonitorStateException(String s)
```

**Parameters:**
- `s` - IllegalMonitorStateException의 세부 메세지.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
