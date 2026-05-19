---
title: "Interface RecordComparator"
---

`package javax.microedition.rms`

```text
 RecordComparator c = new AddressRecordComparator();
 if (c.compare(recordStore.getRecord(rec1), recordStore.getRecord(rec2))
	 == RecordComparator.PRECEDES)
 return rec1;
```

## 설명

**Since:**
- MIDP 1.0

## 필드 요약

- `static int EQUIVALENT` — EQUIVALENT는 검색 또는 정렬 순서 관점에서 두 레코드가 동일하다는 것을 의미합니다.
- `static int FOLLOWS` — FOLLOWS는 검색 또는 정렬 순서 관점에서 왼쪽(첫 번째 매개 변수) 레코드가 오른쪽(두 번째 매개 변수) 레코드 뒤에 옴 을 의미합니다.
- `static int PRECEDES` — RECEDES는 검색 또는 정렬 순서 관점에서 왼쪽(첫 번째 매개 변수) 레코드가 오른쪽(두 번째 매개 변수) 레코드 앞에 옴 을 의미합니다.

## 메서드 요약

- `int compare (byte[] rec1, byte[] rec2)` — 정렬 순서상 rec1이 rec2 앞에 오면 RecordComparator.PRECEDES , 정렬 순서상 rec1이 rec2 뒤에 오면 RecordComparator.FOLLOWS , 정렬 순서상 rec1이 rec2와 동등하면 RecordComparator.EQUIVALENT 가 반환됩니다.

## 필드 상세

### EQUIVALENT

```java
public static final int EQUIVALENT
```

**See Also:**
- `Constant Field Values`

### FOLLOWS

```java
public static final int FOLLOWS
```

**See Also:**
- `Constant Field Values`

### PRECEDES

```java
public static final int PRECEDES
```

**See Also:**
- `Constant Field Values`

### compare

```java
public int compare(byte[] rec1,
                   byte[] rec2)
```

**Parameters:**
- `rec2` - 비교에 사용할 두 번째 레코드 메소드 내에서 
응용 프로그램은 이 매개 변수를 
읽기 전용으로 처리해야 합니다.

**Returns:**
- 정렬 순서상 rec1이 rec2 앞에 오면 
`RecordComparator.PRECEDES`, 
정렬 순서상 rec1이 rec2 뒤에 오면 
`RecordComparator.FOLLOWS`, 
정렬 순서상 rec1이 rec2와 동등하면
`RecordComparator.EQUIVALENT`

## 메서드 상세

### compare

```java
public int compare(byte[] rec1,
                   byte[] rec2)
```

**Parameters:**
- `rec2` - 비교에 사용할 두 번째 레코드 메소드 내에서 
응용 프로그램은 이 매개 변수를 
읽기 전용으로 처리해야 합니다.

**Returns:**
- 정렬 순서상 rec1이 rec2 앞에 오면 
`RecordComparator.PRECEDES`, 
정렬 순서상 rec1이 rec2 뒤에 오면 
`RecordComparator.FOLLOWS`, 
정렬 순서상 rec1이 rec2와 동등하면
`RecordComparator.EQUIVALENT`
