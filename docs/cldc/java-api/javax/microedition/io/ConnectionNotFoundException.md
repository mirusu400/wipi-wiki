# Class ConnectionNotFoundException

`package javax.microedition.io`

```
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.io.IOException
                    |
                    +--javax.microedition.io.ConnectionNotFoundException
```

## 설명

**extends IOException:**

이 클래스는 연결 대상을 찾을 수 없거나 
프로토콜 유형이 지원되지 않음을 나타내는 데 사용됩니다.

**Since:**
- CLDC 1.0

## 생성자 요약

- ConnectionNotFoundException () 세부 정보 메시지 없이 ConnectionNotFoundException을 
구성합니다.
- ConnectionNotFoundException ( String s) 지정한 세부 정보 메시지를 사용하여 ConnectionNotFoundException을 
구성합니다.

## 생성자 상세

### ConnectionNotFoundException

```java
public ConnectionNotFoundException()
```

- 세부 정보 메시지 없이 ConnectionNotFoundException을 
구성합니다.

### ConnectionNotFoundException

```java
public ConnectionNotFoundException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 ConnectionNotFoundException을 
구성합니다. 세부 정보 메시지는 특정 예외를 
설명하는 문자열입니다.

**Parameters:**
- `s` - 세부 정보 메시지
