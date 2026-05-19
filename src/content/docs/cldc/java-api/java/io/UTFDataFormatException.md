---
title: "Class UTFDataFormatException"
---

`package java.io`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.io.IOException
                    |
                    +--java.io.UTFDataFormatException
```

## 설명

**extends IOException:**

데이터 입력 스트림이나 데이터 입력 스트림을 구현하는 클래스에서 
형식이 잘못된 UTF-8 문자열을 읽었음을 나타냅니다. 
UTF-8 문자열을 읽고 쓰는 형식에 대해서는 `writeUTF` 
메소드를 참조하십시오.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``DataInput``, 
``DataInputStream.readUTF(java.io.DataInput)``, 
``IOException``

## 생성자 요약

- UTFDataFormatException () null 을 오류 세부 정보 메시지로 사용하여 UTFDataFormatException 을 구성합니다.
- UTFDataFormatException ( String s) 지정한 세부 정보 메시지를 사용하여 UTFDataFormatException 을 구성합니다.

## 생성자 상세

### UTFDataFormatException

```java
public UTFDataFormatException()
```

- `null`을 오류 세부 정보 메시지로 사용하여 
`UTFDataFormatException`을 구성합니다.

### UTFDataFormatException

```java
public UTFDataFormatException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 
`UTFDataFormatException`을 구성합니다. 
문자열 `s`는 나중에 `java.lang.Throwable` 
클래스의 `Throwable.getMessage()` 메소드로 
검색할 수 있습니다.

**Parameters:**
- `s` - 세부 정보 메시지
