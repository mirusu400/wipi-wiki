# Class DataFilterInteger

`package org.kwis.msp.db`

```
java.lang.Object
  |
  +--org.kwis.msp.db.DataFilterInteger
```

## 설명

**All Implemented Interfaces:**
- `DataFilter`

**implements DataFilter:**

정렬에 사용할 레코드를 한정합니다.

정수로 정렬할 때 사용합니다.
 레코드의 데이터인 바이트 어레이에서, 
 특정 오프셋에 저장된 데이터가 정수(int)라 가정하고,
 이 값이 일정 범위(min, max로 지정된)에 속한 레코드만
 정렬에 포함합니다.

`sortRecord` 메쏘드를 호출할 때 사용합니다.

## 필드 요약

- `protected  int max` — 최대값
- `protected  int min` — 최소값
- `protected  int offset` — 비교할 오프셋

## 생성자 요약

- DataFilterInteger (int offset,
 int min,
 int max) 정렬에 사용할 레코드를 한정합니다.

## 메서드 요약

- `boolean filter (byte[] data)` — 정렬에 사용할 레코드를 제한하는 메쏘드입니다.

## 필드 상세

### offset

```java
protected int offset
```

- 비교할 오프셋

### min

```java
protected int min
```

- 최소값

### max

```java
protected int max
```

- 최대값

### DataFilterInteger

```java
public DataFilterInteger(int offset,
                         int min,
                         int max)
                  throws IllegalArgumentException
```

**Parameters:**
- `max` - 최대값. `Integer.MAX_VALUE` 이면 
 `min` 이상을 의미

**Throws:**
- `IllegalArgumentException` - `offset`이 음수이거나
 `min`, `max`가 제대로 주어지지 않은 경우

### filter

```java
public boolean filter(byte[] data)
```

- **Description copied from interface: `DataFilter`**

**Specified by:**
- `filter` in interface `DataFilter`
- Following copied from interface: `org.kwis.msp.db.DataFilter`

**Parameters:**
- `data` - 레코드에 저장된 데이터를 나타내는 바이트 어레이

**Returns:**
- 해당 레코드가 정렬에 포함된다면 true, 아니면 false

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 생성자 상세

### DataFilterInteger

```java
public DataFilterInteger(int offset,
                         int min,
                         int max)
                  throws IllegalArgumentException
```

**Parameters:**
- `max` - 최대값. `Integer.MAX_VALUE` 이면 
 `min` 이상을 의미

**Throws:**
- `IllegalArgumentException` - `offset`이 음수이거나
 `min`, `max`가 제대로 주어지지 않은 경우

### filter

```java
public boolean filter(byte[] data)
```

- **Description copied from interface: `DataFilter`**

**Specified by:**
- `filter` in interface `DataFilter`
- Following copied from interface: `org.kwis.msp.db.DataFilter`

**Parameters:**
- `data` - 레코드에 저장된 데이터를 나타내는 바이트 어레이

**Returns:**
- 해당 레코드가 정렬에 포함된다면 true, 아니면 false

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 메서드 상세

### filter

```java
public boolean filter(byte[] data)
```

- **Description copied from interface: `DataFilter`**

**Specified by:**
- `filter` in interface `DataFilter`
- Following copied from interface: `org.kwis.msp.db.DataFilter`

**Parameters:**
- `data` - 레코드에 저장된 데이터를 나타내는 바이트 어레이

**Returns:**
- 해당 레코드가 정렬에 포함된다면 true, 아니면 false

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
