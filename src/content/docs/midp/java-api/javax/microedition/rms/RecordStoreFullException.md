---
title: "Class RecordStoreFullException"
---

`package javax.microedition.rms`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--javax.microedition.rms.RecordStoreException
                    |
                    +--javax.microedition.rms.RecordStoreFullException
```

## 설명

**extends RecordStoreException:**

레코드 저장 시스템 저장소가 가득 차서 작업을 완료할 수 없음을 
표시하기 위해 발생합니다.

**Since:**
- MIDP 1.0

## 생성자 요약

- RecordStoreFullException () 세부 정보 메시지 없이 새 RecordStoreFullException 을 
구성합니다.
- RecordStoreFullException ( String message) 지정된 세부 정보 메시지로 새 RecordStoreFullException 을 
구성합니다.

## 생성자 상세

### RecordStoreFullException

```java
public RecordStoreFullException(String message)
```

- 지정된 세부 정보 메시지로 새 `RecordStoreFullException`을 
구성합니다.

**Parameters:**
- `message` - 세부 정보 메시지

### RecordStoreFullException

```java
public RecordStoreFullException()
```

- 세부 정보 메시지 없이 새 `RecordStoreFullException`을 
구성합니다.
