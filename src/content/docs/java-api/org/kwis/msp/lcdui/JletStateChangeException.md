---
title: "Class JletStateChangeException"
---

`package org.kwis.msp.lcdui`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--org.kwis.msp.lcdui.JletStateChangeException
```

## 설명

**extends Exception:**

Jlet의 상태를 변경할 수 없는 경우에 생성되는 예외 클래스입니다.

프로그램에 의해서 resumeApp나 destroyApp함수 내부에서 던질 수 있는
 예외 클래스입니다.

## 생성자 요약

- JletStateChangeException () 상세 메시지 없이 예외를 생성한다.
- JletStateChangeException ( String str) 상세 메시지를 가지는 예외를 생성한다.

## 생성자 상세

### JletStateChangeException

```java
public JletStateChangeException()
```

- 상세 메시지 없이 예외를 생성한다.

### JletStateChangeException

```java
public JletStateChangeException(String str)
```

**Parameters:**
- `str` - 상세 메시지 문자열

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
