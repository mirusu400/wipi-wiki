---
title: "Class VirtualMachineError"
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
```

## 설명

**Direct Known Subclasses:**
- `OutOfMemoryError`

**extends Error:**

Java 가상 머신에 장애가 발생했거나 계속 작동하는 데 
 필요한 자원이 떨어졌음을 나타냅니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- VirtualMachineError () 세부 정보 메시지 없이 VirtualMachineError 를 구성합니다.
- VirtualMachineError ( String s) 지정한 세부 정보 메시지를 사용하여 VirtualMachineError 를 
 구성합니다.

## 생성자 상세

### VirtualMachineError

```java
public VirtualMachineError()
```

- 세부 정보 메시지 없이 `VirtualMachineError`를 구성합니다.

### VirtualMachineError

```java
public VirtualMachineError(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `VirtualMachineError`를 
 구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
