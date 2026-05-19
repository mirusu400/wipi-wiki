---
title: "Class RecordStoreNotFoundException"
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
                    +--javax.microedition.rms.RecordStoreNotFoundException
```

## 설명

**extends RecordStoreException:**

레코드 저장소를 찾을 수 없어 
작업을 완료할 수 없음을 표시하기 위해 발생합니다.

**Since:**
- MIDP 1.0

## 생성자 요약

- RecordStoreNotFoundException () 세부 정보 메시지 없이 새 RecordStoreNotFoundException 을 
구성합니다.
- RecordStoreNotFoundException ( String message) 지정된 세부 정보 메시지로 새 RecordStoreNotFoundException 을 
구성합니다.

## 생성자 상세

### RecordStoreNotFoundException

```java
public RecordStoreNotFoundException(String message)
```

- 지정된 세부 정보 메시지로 새 `RecordStoreNotFoundException`을 
구성합니다.

**Parameters:**
- `message` - 세부 정보 메시지

### RecordStoreNotFoundException

```java
public RecordStoreNotFoundException()
```

- 세부 정보 메시지 없이 새 `RecordStoreNotFoundException`을 
구성합니다.
