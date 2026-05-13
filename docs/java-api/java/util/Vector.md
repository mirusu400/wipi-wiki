# Class Vector

`package java.util`

```
java.lang.Object
  |
  +--java.util.Vector
```

## 설명

**Direct Known Subclasses:**
- `Stack`

**extends Object:**

크기가 유동적인 자바 객체 배열-벡터- 클래스 .

## 필드 요약

- `protected  int capacityIncrement`
- `protected  int elementCount`
- `protected Object [] elementData`

## 생성자 요약

- Vector () 버퍼의 초기 크기가 10인 객체를 생성한다.
- Vector (int initialCapacity) 특정 크기의 버퍼를 가진 객체를 생성한다.
- Vector (int initialCapacity,
 int capacityIncrement) 초기 크기와 벡터의 증가 단위를 지정해서 객체를 생성한다.

## 메서드 요약

- `void addElement ( Object obj)` — 벡터의 끝에 새로운 객체를 추가한다.
- `int capacity ()` — 현재 벡터내 버퍼의 크기를 구한다.
- `boolean contains ( Object elem)` — 특정 객체가 벡터 내에 있는지 여부를 구한다.
- `void copyInto ( Object [] anArray)` — 벡터를 객체 배열에 복사한다.
- `Object elementAt (int index)` — 벡터 내에 특정 위치에 있는 객체를 구한다.
- `Enumeration elements ()` — 벡터 내용을 Enumeration 객체로 구한다.
- `void ensureCapacity (int minCapacity)` — 벡터 버퍼의 크기를 특정 크기까지 확장한다.
- `Object firstElement ()` — 벡터의 첫번째 객체를 구한다.
- `int indexOf ( Object elem)` — 특정 객체의 첫번째 위치를 구한다.
- `int indexOf ( Object e, int index)` — 특정 객체의 특정 인덱스 이 후 첫번째 위치를 구한다.
- `void insertElementAt ( Object obj, int index)` — 특정 객체를 특정 위치에 삽입한다.
- `boolean isEmpty ()` — 벡터가 비었는지 여부를 구한다.
- `Object lastElement ()` — 벡터의 마지막 객체를 구한다.
- `int lastIndexOf ( Object elem)` — 벡터내 특정 객체의 마지막 위치를 구한다.
- `int lastIndexOf ( Object e, int index)` — 특정 객체의 특정위치 이전 마지막 위치를 구한다.
- `void removeAllElements ()` — 벡터내 모든 객체를 제거한다.
- `boolean removeElement ( Object obj)` — 특정 객체를 찾아 제거한다.
- `void removeElementAt (int index)` — 특정 위치의 객체를 제거한다.
- `void setElementAt ( Object obj, int index)` — 벡터 내 특정 위치에 특정 객체를 저장한다.
- `void setSize (int newSize)` — 벡터의 크기를 재 설정한다.
- `int size ()` — 벡터의 크기를 구한다.
- `String toString ()` — 현 객체를 나타낼 수 있는 문자열을 구한다.
- `void trimToSize ()` — 벡터를 저장하기 위한 버퍼에서 사용하지 않는 공간을 제거한다

## 필드 상세

### capacityIncrement

```java
protected int capacityIncrement
```

### elementCount

```java
protected int elementCount
```

### elementData

```java
protected Object[] elementData
```

### Vector

```java
public Vector()
```

- 버퍼의 초기 크기가 10인 객체를 생성한다.

### Vector

```java
public Vector(int initialCapacity)
```

**Parameters:**
- `initialCapacity` - 초기 크기.

### Vector

```java
public Vector(int initialCapacity,
              int capacityIncrement)
```

**Parameters:**
- `capacityIncrement` - 벡터의 증가 단위.

### addElement

```java
public void addElement(Object obj)
```

**Parameters:**
- `obj` - 추가할 객체.

### capacity

```java
public int capacity()
```

**Returns:**
- 벡터내 버퍼의 크기.

### contains

```java
public boolean contains(Object elem)
```

**Parameters:**
- `elem` - 찾을 객체.

**Returns:**
- 객체가 존재하면 true 아니면 false.

### copyInto

```java
public void copyInto(Object[] anArray)
```

**Parameters:**
- `anArray` - 벡터 내용을 복사할 객체 배열.

### elementAt

```java
public Object elementAt(int index)
```

**Parameters:**
- `index` - 구할 객체의 위치.

**Returns:**
- 벡터 내에 특정 위치에 있는 객체

### elements

```java
public Enumeration elements()
```

**Returns:**
- 벡터 내용을 모두 복사해 가진 Enumeration객체.

### ensureCapacity

```java
public void ensureCapacity(int minCapacity)
```

**Parameters:**
- `minCapacity` - 보장되야 할 벡터 크기.

### firstElement

```java
public Object firstElement()
```

**Returns:**
- 벡터의 첫번째 객체.

### indexOf

```java
public int indexOf(Object elem)
```

**Parameters:**
- `elem` - 찾을 객체.

**Returns:**
- 특정 객체의 첫번째 위치.

### indexOf

```java
public int indexOf(Object e,
                   int index)
```

**Parameters:**
- `index` - 검색 시작 위치.

**Returns:**
- 특정 객체의 첫번째 위치 없으면 -1.

### insertElementAt

```java
public void insertElementAt(Object obj,
                            int index)
```

**Parameters:**
- `index` - 삽입할 위치.

### isEmpty

```java
public boolean isEmpty()
```

**Returns:**
- 벡터가 비었으면 true 아니면 false.

### lastElement

```java
public Object lastElement()
```

**Returns:**
- 벡터의 마지막 객체.

### lastIndexOf

```java
public int lastIndexOf(Object e,
                       int index)
```

**Parameters:**
- `index` - 인덱스 0부터 index까지 찾슴니다.

**Returns:**
- 객체가 존재하면 위치 아니면 -1.

### lastIndexOf

```java
public int lastIndexOf(Object elem)
```

**Parameters:**
- `elem` - 찾을 객체.

**Returns:**
- 객체가 존재하면 위치 아니면 -1.

### removeAllElements

```java
public void removeAllElements()
```

- 벡터내 모든 객체를 제거한다.

### removeElementAt

```java
public void removeElementAt(int index)
```

**Parameters:**
- `index` - 제거할 위치.

### removeElement

```java
public boolean removeElement(Object obj)
```

**Parameters:**
- `obj` - 찾을 객체.

**Returns:**
- 객체를 찾아 제거했으면 true 아니면 false.

### setElementAt

```java
public void setElementAt(Object obj,
                         int index)
```

**Parameters:**
- `index` - 저장할 위치.

### setSize

```java
public void setSize(int newSize)
```

**Parameters:**
- `newSize` - 변경할 벡터의 크기.

### size

```java
public int size()
```

**Returns:**
- 벡터의 크기.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체를 나타낼 수 있는 문자열.

### trimToSize

```java
public void trimToSize()
```

- 벡터를 저장하기 위한 버퍼에서 사용하지 않는 공간을 제거한다

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 생성자 상세

### Vector

```java
public Vector()
```

- 버퍼의 초기 크기가 10인 객체를 생성한다.

### Vector

```java
public Vector(int initialCapacity)
```

**Parameters:**
- `initialCapacity` - 초기 크기.

### Vector

```java
public Vector(int initialCapacity,
              int capacityIncrement)
```

**Parameters:**
- `capacityIncrement` - 벡터의 증가 단위.

### addElement

```java
public void addElement(Object obj)
```

**Parameters:**
- `obj` - 추가할 객체.

### capacity

```java
public int capacity()
```

**Returns:**
- 벡터내 버퍼의 크기.

### contains

```java
public boolean contains(Object elem)
```

**Parameters:**
- `elem` - 찾을 객체.

**Returns:**
- 객체가 존재하면 true 아니면 false.

### copyInto

```java
public void copyInto(Object[] anArray)
```

**Parameters:**
- `anArray` - 벡터 내용을 복사할 객체 배열.

### elementAt

```java
public Object elementAt(int index)
```

**Parameters:**
- `index` - 구할 객체의 위치.

**Returns:**
- 벡터 내에 특정 위치에 있는 객체

### elements

```java
public Enumeration elements()
```

**Returns:**
- 벡터 내용을 모두 복사해 가진 Enumeration객체.

### ensureCapacity

```java
public void ensureCapacity(int minCapacity)
```

**Parameters:**
- `minCapacity` - 보장되야 할 벡터 크기.

### firstElement

```java
public Object firstElement()
```

**Returns:**
- 벡터의 첫번째 객체.

### indexOf

```java
public int indexOf(Object elem)
```

**Parameters:**
- `elem` - 찾을 객체.

**Returns:**
- 특정 객체의 첫번째 위치.

### indexOf

```java
public int indexOf(Object e,
                   int index)
```

**Parameters:**
- `index` - 검색 시작 위치.

**Returns:**
- 특정 객체의 첫번째 위치 없으면 -1.

### insertElementAt

```java
public void insertElementAt(Object obj,
                            int index)
```

**Parameters:**
- `index` - 삽입할 위치.

### isEmpty

```java
public boolean isEmpty()
```

**Returns:**
- 벡터가 비었으면 true 아니면 false.

### lastElement

```java
public Object lastElement()
```

**Returns:**
- 벡터의 마지막 객체.

### lastIndexOf

```java
public int lastIndexOf(Object e,
                       int index)
```

**Parameters:**
- `index` - 인덱스 0부터 index까지 찾슴니다.

**Returns:**
- 객체가 존재하면 위치 아니면 -1.

### lastIndexOf

```java
public int lastIndexOf(Object elem)
```

**Parameters:**
- `elem` - 찾을 객체.

**Returns:**
- 객체가 존재하면 위치 아니면 -1.

### removeAllElements

```java
public void removeAllElements()
```

- 벡터내 모든 객체를 제거한다.

### removeElementAt

```java
public void removeElementAt(int index)
```

**Parameters:**
- `index` - 제거할 위치.

### removeElement

```java
public boolean removeElement(Object obj)
```

**Parameters:**
- `obj` - 찾을 객체.

**Returns:**
- 객체를 찾아 제거했으면 true 아니면 false.

### setElementAt

```java
public void setElementAt(Object obj,
                         int index)
```

**Parameters:**
- `index` - 저장할 위치.

### setSize

```java
public void setSize(int newSize)
```

**Parameters:**
- `newSize` - 변경할 벡터의 크기.

### size

```java
public int size()
```

**Returns:**
- 벡터의 크기.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체를 나타낼 수 있는 문자열.

### trimToSize

```java
public void trimToSize()
```

- 벡터를 저장하기 위한 버퍼에서 사용하지 않는 공간을 제거한다

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 메서드 상세

### addElement

```java
public void addElement(Object obj)
```

**Parameters:**
- `obj` - 추가할 객체.

### capacity

```java
public int capacity()
```

**Returns:**
- 벡터내 버퍼의 크기.

### contains

```java
public boolean contains(Object elem)
```

**Parameters:**
- `elem` - 찾을 객체.

**Returns:**
- 객체가 존재하면 true 아니면 false.

### copyInto

```java
public void copyInto(Object[] anArray)
```

**Parameters:**
- `anArray` - 벡터 내용을 복사할 객체 배열.

### elementAt

```java
public Object elementAt(int index)
```

**Parameters:**
- `index` - 구할 객체의 위치.

**Returns:**
- 벡터 내에 특정 위치에 있는 객체

### elements

```java
public Enumeration elements()
```

**Returns:**
- 벡터 내용을 모두 복사해 가진 Enumeration객체.

### ensureCapacity

```java
public void ensureCapacity(int minCapacity)
```

**Parameters:**
- `minCapacity` - 보장되야 할 벡터 크기.

### firstElement

```java
public Object firstElement()
```

**Returns:**
- 벡터의 첫번째 객체.

### indexOf

```java
public int indexOf(Object elem)
```

**Parameters:**
- `elem` - 찾을 객체.

**Returns:**
- 특정 객체의 첫번째 위치.

### indexOf

```java
public int indexOf(Object e,
                   int index)
```

**Parameters:**
- `index` - 검색 시작 위치.

**Returns:**
- 특정 객체의 첫번째 위치 없으면 -1.

### insertElementAt

```java
public void insertElementAt(Object obj,
                            int index)
```

**Parameters:**
- `index` - 삽입할 위치.

### isEmpty

```java
public boolean isEmpty()
```

**Returns:**
- 벡터가 비었으면 true 아니면 false.

### lastElement

```java
public Object lastElement()
```

**Returns:**
- 벡터의 마지막 객체.

### lastIndexOf

```java
public int lastIndexOf(Object e,
                       int index)
```

**Parameters:**
- `index` - 인덱스 0부터 index까지 찾슴니다.

**Returns:**
- 객체가 존재하면 위치 아니면 -1.

### lastIndexOf

```java
public int lastIndexOf(Object elem)
```

**Parameters:**
- `elem` - 찾을 객체.

**Returns:**
- 객체가 존재하면 위치 아니면 -1.

### removeAllElements

```java
public void removeAllElements()
```

- 벡터내 모든 객체를 제거한다.

### removeElementAt

```java
public void removeElementAt(int index)
```

**Parameters:**
- `index` - 제거할 위치.

### removeElement

```java
public boolean removeElement(Object obj)
```

**Parameters:**
- `obj` - 찾을 객체.

**Returns:**
- 객체를 찾아 제거했으면 true 아니면 false.

### setElementAt

```java
public void setElementAt(Object obj,
                         int index)
```

**Parameters:**
- `index` - 저장할 위치.

### setSize

```java
public void setSize(int newSize)
```

**Parameters:**
- `newSize` - 변경할 벡터의 크기.

### size

```java
public int size()
```

**Returns:**
- 벡터의 크기.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체를 나타낼 수 있는 문자열.

### trimToSize

```java
public void trimToSize()
```

- 벡터를 저장하기 위한 버퍼에서 사용하지 않는 공간을 제거한다

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
