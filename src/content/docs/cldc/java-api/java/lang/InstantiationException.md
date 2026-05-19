---
title: "Class InstantiationException"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.lang.InstantiationException
```

## 설명

**extends Exception:**

응용 프로그램이 `Class` 클래스의 
`newInstance` 메소드를 사용하여 
클래스의 인스턴스를 만들려고 시도하지만 지정된 클래스 객체가 
인터페이스이거나 추상 클래스여서 인스턴스화할 수 없을 때 발생합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Class.newInstance()``

## 생성자 요약

- InstantiationException () 세부 정보 메시지 없이 InstantiationException 을 구성합니다.
- InstantiationException ( String s) 지정한 세부 정보 메시지를 사용하여 InstantiationException 을 
구성합니다.

## 생성자 상세

### InstantiationException

```java
public InstantiationException()
```

- 세부 정보 메시지 없이 `InstantiationException`을 구성합니다.

### InstantiationException

```java
public InstantiationException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `InstantiationException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
