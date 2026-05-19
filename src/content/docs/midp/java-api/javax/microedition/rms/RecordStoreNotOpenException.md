---
title: "Class RecordStoreNotOpenException"
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
                    +--javax.microedition.rms.RecordStoreNotOpenException
```

## 설명

**extends RecordStoreException:**

닫힌 레코드 저장소에서 작업을 시도하였음을 표시하기 위해 발생합니다.

**Since:**
- MIDP 1.0

## 생성자 요약

- RecordStoreNotOpenException () 세부 정보 메시지 없이 새 RecordStoreNotOpenException 을 
구성합니다.
- RecordStoreNotOpenException ( String message) 지정된 세부 정보 메시지로 
새 RecordStoreNotOpenException 을 구성합니다.

## 생성자 상세

### RecordStoreNotOpenException

```java
public RecordStoreNotOpenException(String message)
```

- 지정된 세부 정보 메시지로 
새 `RecordStoreNotOpenException`을 구성합니다.

**Parameters:**
- `message` - 세부 정보 메시지

### RecordStoreNotOpenException

```java
public RecordStoreNotOpenException()
```

- 세부 정보 메시지 없이 새 `RecordStoreNotOpenException`을 
구성합니다.
