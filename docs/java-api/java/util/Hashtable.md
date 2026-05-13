# Class Hashtable

`package java.util`

```
java.lang.Object
  |
  +--java.util.Hashtable
```

## 설명

**extends Object:**

해쉬 테이블을 지원하는 클래스.

## 생성자 요약

- Hashtable () 디폴트로 크기가 11인 해쉬 테이블을 가진 객체를 생성한다.
- Hashtable (int capacity) 특정 크기의 해쉬 테이블을 가진 객체를 생성한다.

## 메서드 요약

- `void clear ()` — 해쉬테이블을 비운다.
- `boolean contains ( Object value)` — 매개변수로 넘어온 객체와 동일한 value가 해쉬테이블내에 있는지 검사한다.
- `boolean containsKey ( Object key)` — 매개변수로 넘어온 객체와 동일한 Key가 해쉬테이블내에 있는지 검사한다.
- `Enumeration elements ()` — 해쉬테이블의 value를 Enumeration 형태로 구한다.
- `Object get ( Object key)` — 특정 Key에 해당하는 value를 구한다.
- `boolean isEmpty ()` — 현재 해쉬테이블이 비었는지 여부를 구한다..
- `Enumeration keys ()` — 해쉬테이블의 key를 Enumeration 형태로 구한다..
- `Object put ( Object key, Object value)` — 해쉬 테이블에 특정 key와value를 추가한다.
- `protected  void rehash ()` — 해쉬테이블 크기가 커질 때 해쉬테이블에 등록된 객체들을 모두 재휘쉬한다.
- `Object remove ( Object key)` — 특정 key에 해당하는 HashtableEntry 객체를 제거한다.
- `int size ()` — 현재 해쉬테이블에 저장된 객체의 갯수를 구한다.
- `String toString ()` — 현 객체를 나타내기 위한 문자열을 구한다.

## 생성자 상세

### Hashtable

```java
public Hashtable(int capacity)
```

**Parameters:**
- `capacity` - 초기 해쉬테이블의 크기.

### Hashtable

```java
public Hashtable()
```

- 디폴트로 크기가 11인 해쉬 테이블을 가진 객체를 생성한다.

### size

```java
public int size()
```

**Returns:**
- 현재 해쉬테이블에 저장된 객체의 갯수.

### isEmpty

```java
public boolean isEmpty()
```

**Returns:**
- 해쉬테이블이 비었으면 true 아니면 false.

### keys

```java
public Enumeration keys()
```

**Returns:**
- 해쉬테이블의 key로 이루어진 Enumeration.

### elements

```java
public Enumeration elements()
```

**Returns:**
- 해쉬테이블의 value로 이루어진 Enumeration.

### contains

```java
public boolean contains(Object value)
```

**Returns:**
- 객체가 존재하면 true 아니면 false.

### containsKey

```java
public boolean containsKey(Object key)
```

**Returns:**
- 객체가 존재하면 true 아니면 false.

### get

```java
public Object get(Object key)
```

**Parameters:**
- `key` - 찾고자하는 value에 대한 Key.

**Returns:**
- key에 대응하는 value 값 없으면 null.

### rehash

```java
protected void rehash()
```

- 해쉬테이블 크기가 커질 때 해쉬테이블에 등록된 객체들을 모두 재휘쉬한다.

### put

```java
public Object put(Object key,
                  Object value)
```

**Parameters:**
- `value` - 추가할 value.

**Returns:**
- 이미 key에 해당하는 value가 존재하면 기 존재하던 value를 아니면
 null.

### remove

```java
public Object remove(Object key)
```

**Parameters:**
- `key` - 제거할 대상의 key값.

**Returns:**
- 제거된 대상의 value값 제거 대상이 없으면 null.

### clear

```java
public void clear()
```

- 해쉬테이블을 비운다.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체를 나타내기 위한 문자열.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 메서드 상세

### size

```java
public int size()
```

**Returns:**
- 현재 해쉬테이블에 저장된 객체의 갯수.

### isEmpty

```java
public boolean isEmpty()
```

**Returns:**
- 해쉬테이블이 비었으면 true 아니면 false.

### keys

```java
public Enumeration keys()
```

**Returns:**
- 해쉬테이블의 key로 이루어진 Enumeration.

### elements

```java
public Enumeration elements()
```

**Returns:**
- 해쉬테이블의 value로 이루어진 Enumeration.

### contains

```java
public boolean contains(Object value)
```

**Returns:**
- 객체가 존재하면 true 아니면 false.

### containsKey

```java
public boolean containsKey(Object key)
```

**Returns:**
- 객체가 존재하면 true 아니면 false.

### get

```java
public Object get(Object key)
```

**Parameters:**
- `key` - 찾고자하는 value에 대한 Key.

**Returns:**
- key에 대응하는 value 값 없으면 null.

### rehash

```java
protected void rehash()
```

- 해쉬테이블 크기가 커질 때 해쉬테이블에 등록된 객체들을 모두 재휘쉬한다.

### put

```java
public Object put(Object key,
                  Object value)
```

**Parameters:**
- `value` - 추가할 value.

**Returns:**
- 이미 key에 해당하는 value가 존재하면 기 존재하던 value를 아니면
 null.

### remove

```java
public Object remove(Object key)
```

**Parameters:**
- `key` - 제거할 대상의 key값.

**Returns:**
- 제거된 대상의 value값 제거 대상이 없으면 null.

### clear

```java
public void clear()
```

- 해쉬테이블을 비운다.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체를 나타내기 위한 문자열.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
