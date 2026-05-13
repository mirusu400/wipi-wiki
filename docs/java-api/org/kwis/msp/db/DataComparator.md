# Interface DataComparator

`package org.kwis.msp.db`

```
public static final int EQUIVALENT
```

## 설명

- 레코드 정렬이나 검색시 파라미터로 받은
 두개의 레코드가 순서상 같다는 의미입니다.

### FOLLOWS

- 레코드 정렬이나 검색시 파라미터로 받은
 첫번째 레코드가 두번째 레코드 다음에 온다는 의미입니다.

### PRECEDES

- 레코드 정렬이나 검색시 파라미터로 받은 
 두번째 레코드가 첫번째 레코드 다음에 온다는 의미입니다.

Method Detail

### compare

**Parameters:**
- `data2` - 비교할 레코드의 데이터

**Returns:**
- 두 레코드가 순서상 같으면 
 `DataComparator.EQUIVALENT`,
 `data2`다음에 `data1`이 오는 순서이면 
 (즉 `data1`이 `data2`를 따르는 순서이면)
 `DataComparator.FOLLOWS`,
 `data1` 다음에 `data2`가 오는 순서이면 
 `DataComparator.PRECEDES`## 필드 요약

- `static int EQUIVALENT` — 레코드 정렬이나 검색시 파라미터로 받은 두개의 레코드가 순서상 같다는 의미입니다.
- `static int FOLLOWS` — 레코드 정렬이나 검색시 파라미터로 받은 첫번째 레코드가 두번째 레코드 다음에 온다는 의미입니다.
- `static int PRECEDES` — 레코드 정렬이나 검색시 파라미터로 받은 두번째 레코드가 첫번째 레코드 다음에 온다는 의미입니다.

## 메서드 요약

- `int compare (byte[] data1, byte[] data2)` — 레코드를 비교하는 메쏘드(비교자, comparator)입니다.

## 필드 상세

### EQUIVALENT

```java
public static final int EQUIVALENT
```

- 레코드 정렬이나 검색시 파라미터로 받은
 두개의 레코드가 순서상 같다는 의미입니다.

### FOLLOWS

```java
public static final int FOLLOWS
```

- 레코드 정렬이나 검색시 파라미터로 받은
 첫번째 레코드가 두번째 레코드 다음에 온다는 의미입니다.

### PRECEDES

```java
public static final int PRECEDES
```

- 레코드 정렬이나 검색시 파라미터로 받은 
 두번째 레코드가 첫번째 레코드 다음에 온다는 의미입니다.

### compare

```java
public int compare(byte[] data1,
                   byte[] data2)
```

**Parameters:**
- `data2` - 비교할 레코드의 데이터

**Returns:**
- 두 레코드가 순서상 같으면 
 `DataComparator.EQUIVALENT`,
 `data2`다음에 `data1`이 오는 순서이면 
 (즉 `data1`이 `data2`를 따르는 순서이면)
 `DataComparator.FOLLOWS`,
 `data1` 다음에 `data2`가 오는 순서이면 
 `DataComparator.PRECEDES`## 메서드 상세

### compare

```java
public int compare(byte[] data1,
                   byte[] data2)
```

**Parameters:**
- `data2` - 비교할 레코드의 데이터

**Returns:**
- 두 레코드가 순서상 같으면 
 `DataComparator.EQUIVALENT`,
 `data2`다음에 `data1`이 오는 순서이면 
 (즉 `data1`이 `data2`를 따르는 순서이면)
 `DataComparator.FOLLOWS`,
 `data1` 다음에 `data2`가 오는 순서이면 
 `DataComparator.PRECEDES`

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
