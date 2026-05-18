# Class Error

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Error
```

## 설명

**Direct Known Subclasses:**
- `VirtualMachineError`

**extends Throwable:**

Exception보다 중요한 오류 발생시 발생한다. 비정상적인 경우가 
 많슴니다.

## 생성자 요약

- Error () Error를 생성한다.
- Error ( String s) Error를 생성한다.

## 생성자 상세

### Error

```java
public Error()
```

- Error를 생성한다.

### Error

```java
public Error(String s)
```

**Parameters:**
- `s` - Error의 세부 메세지.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
