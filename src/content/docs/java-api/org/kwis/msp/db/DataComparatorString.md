---
title: "Class DataComparatorString"
---

`package org.kwis.msp.db`

```text
java.lang.Object
  |
  +--org.kwis.msp.db.DataComparatorString
```

## 설명

**All Implemented Interfaces:**
- `DataComparator`

**implements DataComparator:**

두개의 레코드를 문자열로 비교하는 클래스입니다.
 데이터베이스의 `sortRecord`메쏘드를 호출할 때 필요합니다.

Fields inherited from interface org.kwis.msp.db. DataComparator EQUIVALENT , FOLLOWS , PRECEDES

Constructor Summary DataComparatorString (int offset) 두개의 레코드를 문자열로 비교하는 클래스입니다.

Method Summary int compare (byte[] data1,
 byte[] data2) 레코드를 비교하는 메쏘드(비교자, comparator)입니다.

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , toString , wait , wait , wait

Constructor Detail

### DataComparatorString

**Parameters:**
- `offset` - 레코드에서 비교할 문자열이 시작되는 바이트 오프셋

Method Detail

### compare

- **Description copied from interface: `DataComparator`**

**Specified by:**
- `compare` in interface `DataComparator`
- Following copied from interface: `org.kwis.msp.db.DataComparator`

**Parameters:**
- `data2` - 비교할 레코드의 데이터

**Returns:**
- 두 레코드가 순서상 같으면 
 `DataComparator.EQUIVALENT`,
 `data2`다음에 `data1`이 오는 순서이면 
 (즉 `data1`이 `data2`를 따르는 순서이면)
 `DataComparator.FOLLOWS`,
 `data1` 다음에 `data2`가 오는 순서이면 
 `DataComparator.PRECEDES`## 생성자 요약

- DataComparatorString (int offset) 두개의 레코드를 문자열로 비교하는 클래스입니다.

## 메서드 요약

- `int compare (byte[] data1, byte[] data2)` — 레코드를 비교하는 메쏘드(비교자, comparator)입니다.

## 생성자 상세

### DataComparatorString

```java
public DataComparatorString(int offset)
```

**Parameters:**
- `offset` - 레코드에서 비교할 문자열이 시작되는 바이트 오프셋

### compare

```java
public int compare(byte[] data1,
                   byte[] data2)
```

- **Description copied from interface: `DataComparator`**

**Specified by:**
- `compare` in interface `DataComparator`
- Following copied from interface: `org.kwis.msp.db.DataComparator`

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

- **Description copied from interface: `DataComparator`**

**Specified by:**
- `compare` in interface `DataComparator`
- Following copied from interface: `org.kwis.msp.db.DataComparator`

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
