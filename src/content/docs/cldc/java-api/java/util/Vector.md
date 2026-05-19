---
title: "Class Vector"
---

`package java.util`

```text
java.lang.Object
  |
  +--java.util.Vector
```

## 설명

**Direct Known Subclasses:**
- `Stack`

**extends Object:**

`Vector` 클래스는 확장 가능한 객체 배열을 
 구현합니다. 배열과 마찬가지로 정수 색인을 사용하여 액세스할 수 있는 
 구성 요소가 포함되어 있습니다. 그러나 
 `Vector`의 크기는 `Vector`가 만들어진 이후의 
 항목 추가 및 제거에 따라 필요한 경우 확장되거나 축소될 수 있습니다.

각 벡터는 `capacity`와 `capacityIncrement`를 
 유지하여 저장소 관리를 최적화하려고 합니다. 
 `capacity`는 항상 벡터 크기보다 크거나 같으며, 
 구성 요소를 벡터에 추가하면 벡터 저장소가 
 `capacityIncrement` 크기도 증가시키기 때문에 
 대체로 벡터 크기보다 큽니다. 응용 프로그램은 
 다수의 구성 요소를 삽입하기 전에 벡터 용량을 증가시킬 수 있습니다. 
 이렇게 하면 증분 재할당 양이 감소합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 필드 요약

- `protected  int capacityIncrement` — 벡터 크기가 용량보다 커짐에 따른 벡터 용량의 자동 증분.
- `protected  int elementCount` — 유효한 벡터 구성 요소 수.
- `protected Object [] elementData` — 벡터 구성 요소가 저장되는 배열 버퍼.

## 생성자 요약

- Vector () 빈 벡터를 구성합니다.
- Vector (int initialCapacity) 지정된 초기 용량을 사용하여 빈 벡터를 구성합니다.
- Vector (int initialCapacity,
 int capacityIncrement) 지정된 초기 용량과 용량 증분을 사용하여 
 빈 벡터를 구성합니다.

## 메서드 요약

- `void addElement ( Object obj)` — 지정된 구성 요소를 이 벡터의 끝에 추가하여 크기를 1만큼 증가시킵니다.
- `int capacity ()` — 이 벡터의 현재 용량을 반환합니다.
- `boolean contains ( Object elem)` — 지정된 객체가 이 벡터의 구성 요소인지 테스트합니다.
- `void copyInto ( Object [] anArray)` — 이 벡터의 구성 요소를 지정된 배열에 복사합니다.
- `Object elementAt (int index)` — 지정된 색인의 구성 요소를 반환합니다.
- `Enumeration elements ()` — 이 벡터의 구성 요소 열거를 반환합니다.
- `void ensureCapacity (int minCapacity)` — 필요한 경우 적어도 최소 용량 인자로 지정된 구성 요소 수를 포함할 수 있도록 이 벡터의 용량을 증가시킵니다.
- `Object firstElement ()` — 이 벡터의 첫 구성 요소를 반환합니다.
- `int indexOf ( Object elem)` — equals 메소드로 균등성을 테스트하여 지정된 인자의 첫 항목을 검색합니다.
- `int indexOf ( Object elem, int index)` — index 에서 검색을 시작하고 equals 메소드로 균등성을 테스트하여 지정된 인자의 첫 항목을 검색합니다.
- `void insertElementAt ( Object obj, int index)` — 지정된 객체를 지정된 index 의 구성 요소로 이 벡터에 삽입합니다.
- `boolean isEmpty ()` — 이 벡터에 어떤 구성 요소도 없는지 테스트합니다.
- `Object lastElement ()` — 벡터의 마지막 구성 요소를 반환합니다.
- `int lastIndexOf ( Object elem)` — 이 벡터에서 지정된 객체의 마지막 항목 색인을 반환합니다.
- `int lastIndexOf ( Object elem, int index)` — 지정된 색인부터 시작하여 역순으로 지정된 객체를 검색하고 해당 색인을 반환합니다.
- `void removeAllElements ()` — 이 벡터의 모든 구성 요소를 제거하고 벡터 크기를 0으로 설정합니다.
- `boolean removeElement ( Object obj)` — 인자의 첫 항목을 이 벡터에서 제거합니다.
- `void removeElementAt (int index)` — 지정된 색인의 구성 요소를 삭제합니다.
- `void setElementAt ( Object obj, int index)` — 지정된 객체가 이 벡터의 지정된 index 에 위치하도록 설정합니다.
- `void setSize (int newSize)` — 이 벡터의 크기를 설정합니다.
- `int size ()` — 이 벡터의 구성 요소 수를 반환합니다.
- `String toString ()` — 이 벡터의 문자열 표현을 반환합니다.
- `void trimToSize ()` — 벡터의 현재 크기로 이 벡터의 용량을 줄입니다.

## 필드 상세

### elementData

```java
protected Object[] elementData
```

**Since:**
- JDK1.0

### elementCount

```java
protected int elementCount
```

**Since:**
- JDK1.0

### capacityIncrement

```java
protected int capacityIncrement
```

**Since:**
- JDK1.0

### Vector

```java
public Vector(int initialCapacity,
              int capacityIncrement)
```

- 지정된 초기 용량과 용량 증분을 사용하여 
 빈 벡터를 구성합니다.

**Parameters:**
- `capacityIncrement` - 벡터에 오버플로가 발생할 때 
 용량이 증가하는 양

**Throws:**
- `IllegalArgumentException` - 지정된 초기 용량이 
 음수인 경우

### Vector

```java
public Vector(int initialCapacity)
```

- 지정된 초기 용량을 사용하여 빈 벡터를 구성합니다.

**Parameters:**
- `initialCapacity` - 벡터의 초기 용량

**Since:**
- JDK1.0

### Vector

```java
public Vector()
```

- 빈 벡터를 구성합니다.

**Since:**
- JDK1.0

### copyInto

```java
public void copyInto(Object[] anArray)
```

**Parameters:**
- `anArray` - 구성 요소가 복사되는 배열

**Since:**
- JDK1.0

### trimToSize

```java
public void trimToSize()
```

**Since:**
- JDK1.0

### ensureCapacity

```java
public void ensureCapacity(int minCapacity)
```

**Parameters:**
- `minCapacity` - 최소 필요 용량

**Since:**
- JDK1.0

### setSize

```java
public void setSize(int newSize)
```

**Parameters:**
- `newSize` - 이 벡터의 새 크기

**Throws:**
- `ArrayIndexOutOfBoundsException` - 새 크기가 음수인 경우

**Since:**
- JDK1.0

### capacity

```java
public int capacity()
```

**Returns:**
- 이 벡터의 현재 용량

**Since:**
- JDK1.0

### size

```java
public int size()
```

**Returns:**
- 이 벡터의 구성 요소 수

**Since:**
- JDK1.0

### isEmpty

```java
public boolean isEmpty()
```

**Returns:**
- 이 벡터에 어떤 구성 요소도 없으면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### elements

```java
public Enumeration elements()
```

**Returns:**
- 이 벡터의 구성 요소 열거

**Since:**
- JDK1.0

**See Also:**
- ``Enumeration``

### contains

```java
public boolean contains(Object elem)
```

**Parameters:**
- `elem` - 객체

**Returns:**
- 지정된 객체가 이 벡터의 구성 요소이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### indexOf

```java
public int indexOf(Object elem)
```

**Parameters:**
- `elem` - 객체

**Returns:**
- 이 벡터에서 인자의 첫 항목 색인 또는 객체가 없는 경우 
 `-1`

**Since:**
- JDK1.0

**See Also:**
- ``Object.equals(java.lang.Object)``

### indexOf

```java
public int indexOf(Object elem,
                   int index)
```

**Parameters:**
- `index` - 검색이 시작되는 색인

**Returns:**
- 이 벡터의 `index` 이상의 위치에서 
 인자의 첫 항목 색인 또는 
 객체가 없는 경우 `-1`

**Since:**
- JDK1.0

**See Also:**
- ``Object.equals(java.lang.Object)``

### lastIndexOf

```java
public int lastIndexOf(Object elem)
```

**Parameters:**
- `elem` - 필요한 구성 요소

**Returns:**
- 이 벡터에서 지정된 객체의 마지막 항목 색인 또는 
 객체가 없는 경우 `-1`

**Since:**
- JDK1.0

### lastIndexOf

```java
public int lastIndexOf(Object elem,
                       int index)
```

**Parameters:**
- `index` - 검색이 시작되는 색인

**Returns:**
- 이 벡터의 `index`보다 작은 위치에서 
 지정된 객체의 마지막 항목 색인 또는 
 객체가 없는 경우 `-1`

**Throws:**
- `IndexOutOfBoundsException` - `index`가 
 이 벡터의 현재 크기보다 크거나 같은 경우

**Since:**
- JDK1.0

### elementAt

```java
public Object elementAt(int index)
```

**Parameters:**
- `index` - 이 벡터의 색인

**Returns:**
- 지정된 색인의 구성 요소

**Throws:**
- `ArrayIndexOutOfBoundsException` - 유효하지 않은 색인이 
 지정된 경우

**Since:**
- JDK1.0

### firstElement

```java
public Object firstElement()
```

**Returns:**
- 이 벡터의 첫 구성 요소

**Throws:**
- `NoSuchElementException` - 이 벡터에 어떤 구성 요소도 없는 경우

**Since:**
- JDK1.0

### lastElement

```java
public Object lastElement()
```

**Returns:**
- 벡터의 마지막 구성 요소(예: 색인 
 `size() - 1`의 구성 요소)

**Throws:**
- `NoSuchElementException` - 이 벡터가 비어 있는 경우

**Since:**
- JDK1.0

### setElementAt

```java
public void setElementAt(Object obj,
                         int index)
```

**Parameters:**
- `index` - 지정된 색인

**Throws:**
- `ArrayIndexOutOfBoundsException` - 색인이 유효하지 않은 경우

**Since:**
- JDK1.0

**See Also:**
- ``size()``

### removeElementAt

```java
public void removeElementAt(int index)
```

**Parameters:**
- `index` - 제거할 객체의 색인

**Throws:**
- `ArrayIndexOutOfBoundsException` - 색인이 유효하지 않은 경우

**Since:**
- JDK1.0

**See Also:**
- ``size()``

### insertElementAt

```java
public void insertElementAt(Object obj,
                            int index)
```

**Parameters:**
- `index` - 새 구성 요소를 삽입할 위치

**Throws:**
- `ArrayIndexOutOfBoundsException` - 색인이 유효하지 않은 경우

**Since:**
- JDK1.0

**See Also:**
- ``size()``

### addElement

```java
public void addElement(Object obj)
```

**Parameters:**
- `obj` - 추가되는 구성 요소

**Since:**
- JDK1.0

### removeElement

```java
public boolean removeElement(Object obj)
```

**Parameters:**
- `obj` - 제거되는 구성 요소

**Returns:**
- 인자가 이 벡터의 구성 요소이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### removeAllElements

```java
public void removeAllElements()
```

**Since:**
- JDK1.0

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 벡터의 문자열 표현

**Since:**
- JDK1.0

## 생성자 상세

### Vector

```java
public Vector(int initialCapacity,
              int capacityIncrement)
```

- 지정된 초기 용량과 용량 증분을 사용하여 
 빈 벡터를 구성합니다.

**Parameters:**
- `capacityIncrement` - 벡터에 오버플로가 발생할 때 
 용량이 증가하는 양

**Throws:**
- `IllegalArgumentException` - 지정된 초기 용량이 
 음수인 경우

### Vector

```java
public Vector(int initialCapacity)
```

- 지정된 초기 용량을 사용하여 빈 벡터를 구성합니다.

**Parameters:**
- `initialCapacity` - 벡터의 초기 용량

**Since:**
- JDK1.0

### Vector

```java
public Vector()
```

- 빈 벡터를 구성합니다.

**Since:**
- JDK1.0

### copyInto

```java
public void copyInto(Object[] anArray)
```

**Parameters:**
- `anArray` - 구성 요소가 복사되는 배열

**Since:**
- JDK1.0

### trimToSize

```java
public void trimToSize()
```

**Since:**
- JDK1.0

### ensureCapacity

```java
public void ensureCapacity(int minCapacity)
```

**Parameters:**
- `minCapacity` - 최소 필요 용량

**Since:**
- JDK1.0

### setSize

```java
public void setSize(int newSize)
```

**Parameters:**
- `newSize` - 이 벡터의 새 크기

**Throws:**
- `ArrayIndexOutOfBoundsException` - 새 크기가 음수인 경우

**Since:**
- JDK1.0

### capacity

```java
public int capacity()
```

**Returns:**
- 이 벡터의 현재 용량

**Since:**
- JDK1.0

### size

```java
public int size()
```

**Returns:**
- 이 벡터의 구성 요소 수

**Since:**
- JDK1.0

### isEmpty

```java
public boolean isEmpty()
```

**Returns:**
- 이 벡터에 어떤 구성 요소도 없으면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### elements

```java
public Enumeration elements()
```

**Returns:**
- 이 벡터의 구성 요소 열거

**Since:**
- JDK1.0

**See Also:**
- ``Enumeration``

### contains

```java
public boolean contains(Object elem)
```

**Parameters:**
- `elem` - 객체

**Returns:**
- 지정된 객체가 이 벡터의 구성 요소이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### indexOf

```java
public int indexOf(Object elem)
```

**Parameters:**
- `elem` - 객체

**Returns:**
- 이 벡터에서 인자의 첫 항목 색인 또는 객체가 없는 경우 
 `-1`

**Since:**
- JDK1.0

**See Also:**
- ``Object.equals(java.lang.Object)``

### indexOf

```java
public int indexOf(Object elem,
                   int index)
```

**Parameters:**
- `index` - 검색이 시작되는 색인

**Returns:**
- 이 벡터의 `index` 이상의 위치에서 
 인자의 첫 항목 색인 또는 
 객체가 없는 경우 `-1`

**Since:**
- JDK1.0

**See Also:**
- ``Object.equals(java.lang.Object)``

### lastIndexOf

```java
public int lastIndexOf(Object elem)
```

**Parameters:**
- `elem` - 필요한 구성 요소

**Returns:**
- 이 벡터에서 지정된 객체의 마지막 항목 색인 또는 
 객체가 없는 경우 `-1`

**Since:**
- JDK1.0

### lastIndexOf

```java
public int lastIndexOf(Object elem,
                       int index)
```

**Parameters:**
- `index` - 검색이 시작되는 색인

**Returns:**
- 이 벡터의 `index`보다 작은 위치에서 
 지정된 객체의 마지막 항목 색인 또는 
 객체가 없는 경우 `-1`

**Throws:**
- `IndexOutOfBoundsException` - `index`가 
 이 벡터의 현재 크기보다 크거나 같은 경우

**Since:**
- JDK1.0

### elementAt

```java
public Object elementAt(int index)
```

**Parameters:**
- `index` - 이 벡터의 색인

**Returns:**
- 지정된 색인의 구성 요소

**Throws:**
- `ArrayIndexOutOfBoundsException` - 유효하지 않은 색인이 
 지정된 경우

**Since:**
- JDK1.0

### firstElement

```java
public Object firstElement()
```

**Returns:**
- 이 벡터의 첫 구성 요소

**Throws:**
- `NoSuchElementException` - 이 벡터에 어떤 구성 요소도 없는 경우

**Since:**
- JDK1.0

### lastElement

```java
public Object lastElement()
```

**Returns:**
- 벡터의 마지막 구성 요소(예: 색인 
 `size() - 1`의 구성 요소)

**Throws:**
- `NoSuchElementException` - 이 벡터가 비어 있는 경우

**Since:**
- JDK1.0

### setElementAt

```java
public void setElementAt(Object obj,
                         int index)
```

**Parameters:**
- `index` - 지정된 색인

**Throws:**
- `ArrayIndexOutOfBoundsException` - 색인이 유효하지 않은 경우

**Since:**
- JDK1.0

**See Also:**
- ``size()``

### removeElementAt

```java
public void removeElementAt(int index)
```

**Parameters:**
- `index` - 제거할 객체의 색인

**Throws:**
- `ArrayIndexOutOfBoundsException` - 색인이 유효하지 않은 경우

**Since:**
- JDK1.0

**See Also:**
- ``size()``

### insertElementAt

```java
public void insertElementAt(Object obj,
                            int index)
```

**Parameters:**
- `index` - 새 구성 요소를 삽입할 위치

**Throws:**
- `ArrayIndexOutOfBoundsException` - 색인이 유효하지 않은 경우

**Since:**
- JDK1.0

**See Also:**
- ``size()``

### addElement

```java
public void addElement(Object obj)
```

**Parameters:**
- `obj` - 추가되는 구성 요소

**Since:**
- JDK1.0

### removeElement

```java
public boolean removeElement(Object obj)
```

**Parameters:**
- `obj` - 제거되는 구성 요소

**Returns:**
- 인자가 이 벡터의 구성 요소이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### removeAllElements

```java
public void removeAllElements()
```

**Since:**
- JDK1.0

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 벡터의 문자열 표현

**Since:**
- JDK1.0

## 메서드 상세

### copyInto

```java
public void copyInto(Object[] anArray)
```

**Parameters:**
- `anArray` - 구성 요소가 복사되는 배열

**Since:**
- JDK1.0

### trimToSize

```java
public void trimToSize()
```

**Since:**
- JDK1.0

### ensureCapacity

```java
public void ensureCapacity(int minCapacity)
```

**Parameters:**
- `minCapacity` - 최소 필요 용량

**Since:**
- JDK1.0

### setSize

```java
public void setSize(int newSize)
```

**Parameters:**
- `newSize` - 이 벡터의 새 크기

**Throws:**
- `ArrayIndexOutOfBoundsException` - 새 크기가 음수인 경우

**Since:**
- JDK1.0

### capacity

```java
public int capacity()
```

**Returns:**
- 이 벡터의 현재 용량

**Since:**
- JDK1.0

### size

```java
public int size()
```

**Returns:**
- 이 벡터의 구성 요소 수

**Since:**
- JDK1.0

### isEmpty

```java
public boolean isEmpty()
```

**Returns:**
- 이 벡터에 어떤 구성 요소도 없으면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### elements

```java
public Enumeration elements()
```

**Returns:**
- 이 벡터의 구성 요소 열거

**Since:**
- JDK1.0

**See Also:**
- ``Enumeration``

### contains

```java
public boolean contains(Object elem)
```

**Parameters:**
- `elem` - 객체

**Returns:**
- 지정된 객체가 이 벡터의 구성 요소이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### indexOf

```java
public int indexOf(Object elem)
```

**Parameters:**
- `elem` - 객체

**Returns:**
- 이 벡터에서 인자의 첫 항목 색인 또는 객체가 없는 경우 
 `-1`

**Since:**
- JDK1.0

**See Also:**
- ``Object.equals(java.lang.Object)``

### indexOf

```java
public int indexOf(Object elem,
                   int index)
```

**Parameters:**
- `index` - 검색이 시작되는 색인

**Returns:**
- 이 벡터의 `index` 이상의 위치에서 
 인자의 첫 항목 색인 또는 
 객체가 없는 경우 `-1`

**Since:**
- JDK1.0

**See Also:**
- ``Object.equals(java.lang.Object)``

### lastIndexOf

```java
public int lastIndexOf(Object elem)
```

**Parameters:**
- `elem` - 필요한 구성 요소

**Returns:**
- 이 벡터에서 지정된 객체의 마지막 항목 색인 또는 
 객체가 없는 경우 `-1`

**Since:**
- JDK1.0

### lastIndexOf

```java
public int lastIndexOf(Object elem,
                       int index)
```

**Parameters:**
- `index` - 검색이 시작되는 색인

**Returns:**
- 이 벡터의 `index`보다 작은 위치에서 
 지정된 객체의 마지막 항목 색인 또는 
 객체가 없는 경우 `-1`

**Throws:**
- `IndexOutOfBoundsException` - `index`가 
 이 벡터의 현재 크기보다 크거나 같은 경우

**Since:**
- JDK1.0

### elementAt

```java
public Object elementAt(int index)
```

**Parameters:**
- `index` - 이 벡터의 색인

**Returns:**
- 지정된 색인의 구성 요소

**Throws:**
- `ArrayIndexOutOfBoundsException` - 유효하지 않은 색인이 
 지정된 경우

**Since:**
- JDK1.0

### firstElement

```java
public Object firstElement()
```

**Returns:**
- 이 벡터의 첫 구성 요소

**Throws:**
- `NoSuchElementException` - 이 벡터에 어떤 구성 요소도 없는 경우

**Since:**
- JDK1.0

### lastElement

```java
public Object lastElement()
```

**Returns:**
- 벡터의 마지막 구성 요소(예: 색인 
 `size() - 1`의 구성 요소)

**Throws:**
- `NoSuchElementException` - 이 벡터가 비어 있는 경우

**Since:**
- JDK1.0

### setElementAt

```java
public void setElementAt(Object obj,
                         int index)
```

**Parameters:**
- `index` - 지정된 색인

**Throws:**
- `ArrayIndexOutOfBoundsException` - 색인이 유효하지 않은 경우

**Since:**
- JDK1.0

**See Also:**
- ``size()``

### removeElementAt

```java
public void removeElementAt(int index)
```

**Parameters:**
- `index` - 제거할 객체의 색인

**Throws:**
- `ArrayIndexOutOfBoundsException` - 색인이 유효하지 않은 경우

**Since:**
- JDK1.0

**See Also:**
- ``size()``

### insertElementAt

```java
public void insertElementAt(Object obj,
                            int index)
```

**Parameters:**
- `index` - 새 구성 요소를 삽입할 위치

**Throws:**
- `ArrayIndexOutOfBoundsException` - 색인이 유효하지 않은 경우

**Since:**
- JDK1.0

**See Also:**
- ``size()``

### addElement

```java
public void addElement(Object obj)
```

**Parameters:**
- `obj` - 추가되는 구성 요소

**Since:**
- JDK1.0

### removeElement

```java
public boolean removeElement(Object obj)
```

**Parameters:**
- `obj` - 제거되는 구성 요소

**Returns:**
- 인자가 이 벡터의 구성 요소이면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

### removeAllElements

```java
public void removeAllElements()
```

**Since:**
- JDK1.0

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 벡터의 문자열 표현

**Since:**
- JDK1.0
