---
title: "Class Stack"
---

`package java.util`

```text
java.lang.Object
  |
  +--java.util.Vector
        |
        +--java.util.Stack
```

## 설명

**extends Vector:**

`Stack` 클래스는 LIFO (Last-In-First-Out) 
객체 스택을 나타냅니다. 
이 클래스는 벡터를 스택처럼 처리할 수 있도록 해주는 5가지 작업을 사용하여 
`Vector` 클래스를 확장합니다. 
일반적인 `push` 및 `pop` 작업은 
물론 스택 최상위 항목에서 `peek`하는 메소드, 
스택이 `empty`인지 테스트하는 메소드, 스택에서 항목을 `search`하고 최상위로부터의 거리를 확인하는 메소드 등도 제공됩니다.

처음 스택을 만들면 항목이 들어 있지 않습니다.

**Since:**
- JDK1.0, CLDC 1.0

## 필드 요약

## 생성자 요약

- Stack () 빈 스택을 만듭니다.

## 메서드 요약

- `boolean empty ()` — 이 스택이 비어 있는지 테스트합니다.
- `Object peek ()` — 이 스택의 최상위에 있는 객체를 스택에서 제거하지 않고 살펴봅니다.
- `Object pop ()` — 이 스택의 최상위에서 객체를 제거하여 함수 값으로 반환합니다.
- `Object push ( Object item)` — 항목을 이 스택의 최상위에 푸시합니다.
- `int search ( Object o)` — 1을 기반으로 하는 이 스택 상의 객체 위치를 반환합니다.

## 생성자 상세

### Stack

```java
public Stack()
```

- 빈 스택을 만듭니다.

### push

```java
public Object push(Object item)
```

**Parameters:**
- `item` - 이 스택에 푸시되는 항목

**Returns:**
- `item` 인자

**See Also:**
- ``Vector.addElement(java.lang.Object)``

### pop

```java
public Object pop()
```

**Returns:**
- 이 스택의 최상위에 있는 객체(`Vector` 객체의 
 마지막 항목)

**Throws:**
- `EmptyStackException` - 이 스택이 비어 있는 경우

### peek

```java
public Object peek()
```

**Returns:**
- 이 스택의 최상위에 있는 객체(`Vector` 객체의 
 마지막 항목)

**Throws:**
- `EmptyStackException` - 이 스택이 비어 있는 경우

### empty

```java
public boolean empty()
```

**Returns:**
- 이 스택에 포함된 항목이 없는 경우에만 
 `true`, 그렇지 않으면 `false`

### search

```java
public int search(Object o)
```

**Parameters:**
- `o` - 필요한 객체

**Returns:**
- 1을 기반으로 하는 스택 최상위로부터의 객체 위치. 
 반환 값이 `-1`이면 객체가 
 스택에 없음을 나타냅니다.

## 메서드 상세

### push

```java
public Object push(Object item)
```

**Parameters:**
- `item` - 이 스택에 푸시되는 항목

**Returns:**
- `item` 인자

**See Also:**
- ``Vector.addElement(java.lang.Object)``

### pop

```java
public Object pop()
```

**Returns:**
- 이 스택의 최상위에 있는 객체(`Vector` 객체의 
 마지막 항목)

**Throws:**
- `EmptyStackException` - 이 스택이 비어 있는 경우

### peek

```java
public Object peek()
```

**Returns:**
- 이 스택의 최상위에 있는 객체(`Vector` 객체의 
 마지막 항목)

**Throws:**
- `EmptyStackException` - 이 스택이 비어 있는 경우

### empty

```java
public boolean empty()
```

**Returns:**
- 이 스택에 포함된 항목이 없는 경우에만 
 `true`, 그렇지 않으면 `false`

### search

```java
public int search(Object o)
```

**Parameters:**
- `o` - 필요한 객체

**Returns:**
- 1을 기반으로 하는 스택 최상위로부터의 객체 위치. 
 반환 값이 `-1`이면 객체가 
 스택에 없음을 나타냅니다.
