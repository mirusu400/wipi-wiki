# Class Error

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Error
```

## 설명

**Direct Known Subclasses:**
- `NoClassDefFoundError`, `VirtualMachineError`

**extends Throwable:**

`Error`는 합리적 응용 프로그램이라면 파악하려고 
시도해서는 안 되는 심각한 문제를 나타내는 `Throwable`의 
서브 클래스입니다. 대부분의 이러한 오류는 비정상적 동작입니다.

메소드는 `throws` 절에 `Error`의 서브 
클래스를 선언할 필요가 없습니다. 이러한 오류는 발생해서는 안 되는 
비정상적 동작이기 때문에 메소드 실행 중에 발생할 수는 있지만 
파악되지 않습니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- Error () 지정한 세부 정보 메시지 없이 Error 를 구성합니다.
- Error ( String s) 지정한 세부 정보 메시지를 사용하여 Error를 구성합니다.

## 생성자 상세

### Error

```java
public Error()
```

- 지정한 세부 정보 메시지 없이 `Error`를 구성합니다.

### Error

```java
public Error(String s)
```

- 지정한 세부 정보 메시지를 사용하여 Error를 구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
