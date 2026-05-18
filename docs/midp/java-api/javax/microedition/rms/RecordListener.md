# Interface RecordListener

`package javax.microedition.rms`

```text
public void recordAdded(RecordStore recordStore,
                        int recordId)
```

## 설명

**Parameters:**
- `recordId` - 추가된 레코드의 recordId

### recordChanged

**Parameters:**
- `recordId` - 변경된 레코드의 recordId

### recordDeleted

**Parameters:**
- `recordId` - 삭제된 레코드의 recordId

## 메서드 요약

- `void recordAdded ( RecordStore recordStore, int recordId)` — 레코드가 레코드 저장소에 추가되었을 때 호출됩니다.
- `void recordChanged ( RecordStore recordStore, int recordId)` — 레코드 저장소의 레코드가 변경된 후 호출됩니다.
- `void recordDeleted ( RecordStore recordStore, int recordId)` — 레코드가 레코드 저장소에서 삭제된 후 호출됩니다.

## 메서드 상세

### recordAdded

```java
public void recordAdded(RecordStore recordStore,
                        int recordId)
```

**Parameters:**
- `recordId` - 추가된 레코드의 recordId

### recordChanged

```java
public void recordChanged(RecordStore recordStore,
                          int recordId)
```

**Parameters:**
- `recordId` - 변경된 레코드의 recordId

### recordDeleted

```java
public void recordDeleted(RecordStore recordStore,
                          int recordId)
```

**Parameters:**
- `recordId` - 삭제된 레코드의 recordId
