---
title: "Class MIDletStateChangeException"
---

`package javax.microedition.midlet`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--javax.microedition.midlet.MIDletStateChangeException
```

## 설명

**extends Exception:**

요청된 `MIDlet` 상태 변경 신호가 실패했습니다. 
이 예외는 `MIDlet` 인터페이스를 통한 응용 프로그램으로의 
상태 변경 호출에 대한 응답으로 
`MIDlet`에 의해 발생합니다.

**Since:**
- MIDP 1.0

**See Also:**
- ``MIDlet``

## 생성자 요약

- MIDletStateChangeException () 세부 정보 메시지를 지정하지 않고 예외를 구성합니다.
- MIDletStateChangeException ( String s) 세부 정보 메시지를 지정하여 예외를 구성합니다.

## 생성자 상세

### MIDletStateChangeException

```java
public MIDletStateChangeException()
```

- 세부 정보 메시지를 지정하지 않고 예외를 구성합니다.

### MIDletStateChangeException

```java
public MIDletStateChangeException(String s)
```

- 세부 정보 메시지를 지정하여 예외를 구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
