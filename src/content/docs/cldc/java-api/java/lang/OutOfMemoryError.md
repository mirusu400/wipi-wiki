---
title: "Class OutOfMemoryError"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Error
              |
              +--java.lang.VirtualMachineError
                    |
                    +--java.lang.OutOfMemoryError
```

## 설명

**extends VirtualMachineError:**

Java 가상 머신이 메모리 부족으로 객체를 할당할 수 없으며 가비지 컬렉터에서 추가 메모리를 제공할 수 없는 경우에 발생합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- OutOfMemoryError () 세부 정보 메시지 없이 OutOfMemoryError 를 구성합니다.
- OutOfMemoryError ( String s) 지정한 세부 정보 메시지를 사용하여 OutOfMemoryError 를 구성합니다.

## 생성자 상세

### OutOfMemoryError

```java
public OutOfMemoryError()
```

- 세부 정보 메시지 없이 `OutOfMemoryError`를 구성합니다.

### OutOfMemoryError

```java
public OutOfMemoryError(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `OutOfMemoryError`를 구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
