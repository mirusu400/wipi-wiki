---
title: "Class ArithmeticException"
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
                    +--java.lang.ArithmeticException
```

## 설명

**extends RuntimeException:**

예외적인 연산 조건에서 발생합니다. 
예를 들어, 정수를 "0으로 나누면" 
이 클래스의 인스턴스가 발생합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- ArithmeticException () 세부 정보 메시지 없이 ArithmeticException 을 
구성합니다.
- ArithmeticException ( String s) 지정한 세부 정보 메시지를 사용하여 ArithmeticException 을 
구성합니다.

## 생성자 상세

### ArithmeticException

```java
public ArithmeticException()
```

- 세부 정보 메시지 없이 `ArithmeticException`을 
구성합니다.

### ArithmeticException

```java
public ArithmeticException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `ArithmeticException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
