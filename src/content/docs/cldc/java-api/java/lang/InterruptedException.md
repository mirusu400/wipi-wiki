---
title: "Class InterruptedException"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.lang.InterruptedException
```

## 설명

**extends Exception:**

스레드가 대기 또는 휴면 상태이거나 오랫동안 중지되어 
다른 스레드가 이를 중단한 경우에 발생합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Object.wait()``, 
``Object.wait(long)``, 
``Object.wait(long, int)``, 
``Thread.sleep(long)``

## 생성자 요약

- InterruptedException () 세부 정보 메시지 없이 InterruptedException 을 구성합니다.
- InterruptedException ( String s) 지정한 세부 정보 메시지를 사용하여 InterruptedException 을 
구성합니다.

## 생성자 상세

### InterruptedException

```java
public InterruptedException()
```

- 세부 정보 메시지 없이 `InterruptedException`을 구성합니다.

### InterruptedException

```java
public InterruptedException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `InterruptedException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
