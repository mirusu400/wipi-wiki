---
title: "Class ClassNotFoundException"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.lang.ClassNotFoundException
```

## 설명

**extends Exception:**

응용 프로그램이 `Class` 클래스의 `forName` 
메소드를 사용하여 문자열 이름을 통해 클래스를 로드하려고 
시도하지만 지정된 이름을 가진 클래스 정의를 찾을 수 없을 때 발생합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Class.forName(java.lang.String)``

## 생성자 요약

- ClassNotFoundException () 세부 정보 메시지 없이 ClassNotFoundException 을 구성합니다.
- ClassNotFoundException ( String s) 지정한 세부 정보 메시지를 사용하여 ClassNotFoundException 을
구성합니다.

## 생성자 상세

### ClassNotFoundException

```java
public ClassNotFoundException()
```

- 세부 정보 메시지 없이 `ClassNotFoundException`을 구성합니다.

### ClassNotFoundException

```java
public ClassNotFoundException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `ClassNotFoundException`을
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
