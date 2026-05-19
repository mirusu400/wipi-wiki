---
title: "Class SecurityException"
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
                    +--java.lang.SecurityException
```

## 설명

**extends RuntimeException:**

보안 위반을 나타내기 위해 시스템에서 발생합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- SecurityException () 세부 정보 메시지 없이 SecurityException 을 구성합니다.
- SecurityException ( String s) 지정한 세부 정보 메시지를 사용하여 SecurityException 을 
구성합니다.

## 생성자 상세

### SecurityException

```java
public SecurityException()
```

- 세부 정보 메시지 없이 `SecurityException`을 구성합니다.

### SecurityException

```java
public SecurityException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `SecurityException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
