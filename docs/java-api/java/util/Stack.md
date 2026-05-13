# Class Stack

`package java.util`

```
java.lang.Object
  |
  +--java.util.Vector
        |
        +--java.util.Stack
```

## 설명

**extends Vector:**

스택 구조체을 위한 클래스.

======== INNER CLASS SUMMARY ======== 
 =========== FIELD SUMMARY ===========

Fields inherited from class java.util. Vector capacityIncrement , elementCount , elementData

======== CONSTRUCTOR SUMMARY ========

Constructor Summary Stack () 새로운 스택 객체를 만든다.

========== METHOD SUMMARY ===========

Method Summary boolean empty () 스택이 비었는지 여부를 구한다. Object peek () 스택 맨위 객체를 스택에서 제거하지 않고 구한다. Object pop () 스택에 객체를 pop한다. Object push ( Object item) 스택에 객체를 push한다. int search ( Object o) 특정 객체가 스택 맨위에서 부터 몇번째에 위치하는지 구한다.

Methods inherited from class java.util. Vector addElement , capacity , contains , copyInto , elementAt , elements , ensureCapacity , firstElement , indexOf , indexOf , insertElementAt , isEmpty , lastElement , lastIndexOf , lastIndexOf , removeAllElements , removeElement , removeElementAt , setElementAt , setSize , size , toString , trimToSize

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , wait , wait , wait

============ FIELD DETAIL =========== 
 ========= CONSTRUCTOR DETAIL ========

Constructor Detail

### Stack

- 새로운 스택 객체를 만든다.

============ METHOD DETAIL ==========

Method Detail

### push

**Parameters:**
- `item` - push할 대상.

**Returns:**
- push할 대상.

### pop

**Returns:**
- pop한 객체.

**Throws:**
- `EmptyStackException` - 스택이 비었을 때.

### peek

**Returns:**
- 스택 맨위 객체.

**Throws:**
- `EmptyStackException` - 스택이 비었을 때.

### empty

**Returns:**
- 비었으면 true 아니면 false.

### search

**Returns:**
- 스택 맨위로 부터 객체의 위치까지 offset 없으면 -1.

========= END OF CLASS DATA =========

========== START OF NAVBAR ==========

=========== END OF NAVBAR ===========

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 생성자 요약

- Stack () 새로운 스택 객체를 만든다.

## 메서드 요약

- `boolean empty ()` — 스택이 비었는지 여부를 구한다.
- `Object peek ()` — 스택 맨위 객체를 스택에서 제거하지 않고 구한다.
- `Object pop ()` — 스택에 객체를 pop한다.
- `Object push ( Object item)` — 스택에 객체를 push한다.
- `int search ( Object o)` — 특정 객체가 스택 맨위에서 부터 몇번째에 위치하는지 구한다.

## 생성자 상세

### Stack

```java
public Stack()
```

- 새로운 스택 객체를 만든다.

### push

```java
public Object push(Object item)
```

**Parameters:**
- `item` - push할 대상.

**Returns:**
- push할 대상.

### pop

```java
public Object pop()
```

**Returns:**
- pop한 객체.

**Throws:**
- `EmptyStackException` - 스택이 비었을 때.

### peek

```java
public Object peek()
```

**Returns:**
- 스택 맨위 객체.

**Throws:**
- `EmptyStackException` - 스택이 비었을 때.

### empty

```java
public boolean empty()
```

**Returns:**
- 비었으면 true 아니면 false.

### search

```java
public int search(Object o)
```

**Returns:**
- 스택 맨위로 부터 객체의 위치까지 offset 없으면 -1.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 메서드 상세

### push

```java
public Object push(Object item)
```

**Parameters:**
- `item` - push할 대상.

**Returns:**
- push할 대상.

### pop

```java
public Object pop()
```

**Returns:**
- pop한 객체.

**Throws:**
- `EmptyStackException` - 스택이 비었을 때.

### peek

```java
public Object peek()
```

**Returns:**
- 스택 맨위 객체.

**Throws:**
- `EmptyStackException` - 스택이 비었을 때.

### empty

```java
public boolean empty()
```

**Returns:**
- 비었으면 true 아니면 false.

### search

```java
public int search(Object o)
```

**Returns:**
- 스택 맨위로 부터 객체의 위치까지 offset 없으면 -1.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
