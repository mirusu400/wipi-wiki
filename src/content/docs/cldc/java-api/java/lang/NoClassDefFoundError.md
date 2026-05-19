---
title: "Class NoClassDefFoundError"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Error
              |
              +--java.lang.NoClassDefFoundError
```

## 설명

**extends Error:**

Java 가상 머신이 클래스 정의를 정상적인 메소드 호출의 일부나 
`new` 표현식을 사용한 
새 인스턴스 작성 과정의 일부로 로드하려고 
시도하지만 클래스 정의를 찾을 수 없는 경우에 발생합니다.

현재 실행 중인 클래스를 컴파일했을 경우 
찾고 있던 클래스 정의가 있지만 
해당 정의는 찾을 수 없습니다.

**Since:**
- JDK1.0, CLDC 1.1

## 생성자 요약

- NoClassDefFoundError () 세부 정보 메시지 없이 NoClassDefFoundError 를 구성합니다.
- NoClassDefFoundError ( String s) 지정한 세부 정보 메시지를 사용하여 NoClassDefFoundError 를 
구성합니다.

## 생성자 상세

### NoClassDefFoundError

```java
public NoClassDefFoundError()
```

- 세부 정보 메시지 없이 `NoClassDefFoundError`를 구성합니다.

### NoClassDefFoundError

```java
public NoClassDefFoundError(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `NoClassDefFoundError`를 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
