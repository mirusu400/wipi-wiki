---
title: "Class Exception"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
```

## 설명

**Direct Known Subclasses:**
- `ClassNotFoundException`, `DataBaseException`, `DataBaseRecordException`, `IllegalAccessException`, `InstantiationException`, `InterruptedException`, `IOException`, `JletStateChangeException`, `RuntimeException`

**extends Throwable:**

application에서 대응할 수 있는 오류를 나타낼 때 사용한다.

## 생성자 요약

- Exception () Exception을 생성한다.
- Exception ( String s) Exception을 생성한다.

## 생성자 상세

### Exception

```java
public Exception()
```

- Exception을 생성한다.

### Exception

```java
public Exception(String s)
```

**Parameters:**
- `s` - Exception의 세부 메세지.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
