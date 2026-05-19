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

자원 부족같이 VM정상 동작하기 어려울 때 발생하는 에러 클래스.

## 생성자 요약

- VirtualMachineError () VirtualMachineError객체를 생성한다.
- VirtualMachineError ( String s) VirtualMachineError객체를 생성한다.

## 생성자 상세

### VirtualMachineError

```java
public VirtualMachineError()
```

- VirtualMachineError객체를 생성한다.

### VirtualMachineError

```java
public VirtualMachineError(String s)
```

**Parameters:**
- `s` - VirtualMachineError의 세부 메세지.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
