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

메모리 부족으로 인해 새로운 객체를 생성할 수 없을 때 
 발생하는 에러 클래스.

## 생성자 요약

- OutOfMemoryError () OutOfMemoryError을 생성한다.
- OutOfMemoryError ( String s) OutOfMemoryError을 생성한다.

## 생성자 상세

### OutOfMemoryError

```java
public OutOfMemoryError()
```

- OutOfMemoryError을 생성한다.

### OutOfMemoryError

```java
public OutOfMemoryError(String s)
```

**Parameters:**
- `s` - OutOfMemoryError의 세부 메세지.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
