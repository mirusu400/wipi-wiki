# Class RecordStoreException

`package javax.microedition.rms`

```
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--javax.microedition.rms.RecordStoreException
```

## 설명

**Direct Known Subclasses:**
- `InvalidRecordIDException`, `RecordStoreFullException`, `RecordStoreNotFoundException`, `RecordStoreNotOpenException`

**extends Exception:**

레코드 저장소 작업에서 일반 예외가 발생했음을 표시하기 위해 발생합니다.

**Since:**
- MIDP 1.0

## 생성자 요약

- RecordStoreException () 세부 정보 메시지 없이 새 RecordStoreException 을 
구성합니다.
- RecordStoreException ( String message) 지정된 세부 정보 메시지로 새 RecordStoreException 을 
구성합니다.

## 생성자 상세

### RecordStoreException

```java
public RecordStoreException(String message)
```

- 지정된 세부 정보 메시지로 새 `RecordStoreException`을 
구성합니다.

**Parameters:**
- `message` - 세부 정보 메시지

### RecordStoreException

```java
public RecordStoreException()
```

- 세부 정보 메시지 없이 새 `RecordStoreException`을 
구성합니다.
