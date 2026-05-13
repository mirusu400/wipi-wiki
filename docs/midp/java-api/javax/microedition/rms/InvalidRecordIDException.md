# Class InvalidRecordIDException

`package javax.microedition.rms`

```
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--javax.microedition.rms.RecordStoreException
                    |
                    +--javax.microedition.rms.InvalidRecordIDException
```

## 설명

**extends RecordStoreException:**

레코드 ID가 유효하지 않아 작업이 완료될 수 없음을 
표시하기 위해 발생합니다.

**Since:**
- MIDP 1.0

## 생성자 요약

- InvalidRecordIDException () 세부 정보 메시지 없이 새 InvalidRecordIDException 을 구성합니다.
- InvalidRecordIDException ( String message) 지정된 세부 정보 메시지로 새 InvalidRecordIDException 을 구성합니다.

## 생성자 상세

### InvalidRecordIDException

```java
public InvalidRecordIDException(String message)
```

- 지정된 세부 정보 메시지로 새 
`InvalidRecordIDException`을 구성합니다.

**Parameters:**
- `message` - 세부 정보 메시지

### InvalidRecordIDException

```java
public InvalidRecordIDException()
```

- 세부 정보 메시지 없이 새 
`InvalidRecordIDException`을 구성합니다.
