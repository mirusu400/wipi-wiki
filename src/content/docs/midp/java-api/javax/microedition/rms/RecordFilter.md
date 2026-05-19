---
title: "Interface RecordFilter"
---

`package javax.microedition.rms`

```text
 RecordFilter f = new DateRecordFilter(); // class implements RecordFilter
 if (f.matches(recordStore.getRecord(theRecordID)) == true)
   DoSomethingUseful(theRecordID);
```

## 설명

**Since:**
- MIDP 1.0

## 메서드 요약

- `boolean matches (byte[] candidate)` — 후보가 구현된 기준에 일치하면 true를 반환합니다.

## 메서드 상세

### matches

```java
public boolean matches(byte[] candidate)
```

**Parameters:**
- `candidate` - 고려할 레코드. 
메소드 내에서 응용 프로그램은 
이 매개 변수를 읽기 전용으로 처리해야 합니다.

**Returns:**
- 후보가 구현된 기준에 일치하면 true
