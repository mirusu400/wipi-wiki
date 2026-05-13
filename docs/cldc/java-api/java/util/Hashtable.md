# Class Hashtable

`package java.util`

```
java.lang.Object
  |
  +--java.util.Hashtable
```

## 설명

**extends Object:**

이 클래스는 키를 값에 매핑하는 해시 테이블을 구현합니다. 
`null`이 아닌 모든 객체를 키 또는 값으로 사용할 수 있습니다.

해시 테이블에서 객체를 저장하고 검색하려면 
키로 사용된 객체가 `hashCode` 
메소드와 `equals` 메소드를 구현해야 합니다.

`Hashtable`의 인스턴스에는 효율성에 영향을 주는 
두 매개 변수인 *용량*과 *로드 팩터*가 있습니다. 
hashtable 클래스의 CLDC 구현에서 
로드 팩터는 항상 75%입니다. 
해시 테이블의 항목 수가 로드 팩터와 
현재 용량을 곱한 값을 초과하면 
`rehash` 메소드를 호출하여 용량이 증가됩니다.

`Hashtable`에 많은 항목을 저장하려는 경우 
충분히 큰 용량을 할당하여 해시 테이블 만들면 필요에 따라 
자동으로 해싱을 다시 수행하여 테이블을 확장하도록 하는 것보다 
효율적으로 항목을 삽입할 수 있습니다.

이 예에서는 숫자 해시 테이블을 만들며 
숫자 이름을 키로 사용합니다.

숫자를 검색하려면 다음 코드를 사용합니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Object.equals(java.lang.Object)``, 
``Object.hashCode()``, 
``rehash()``

## 생성자 요약

- Hashtable () 기본 용량과 로드 팩터를 사용하여 
새로운 빈 해시 테이블을 구성합니다.
- Hashtable (int initialCapacity) 지정된 초기 용량을 사용하여 
새로운 빈 해시 테이블을 구성합니다.

## 메서드 요약

- `void clear ()` — 포함된 키가 없도록 이 해시 테이블을 지웁니다.
- `boolean contains ( Object value)` — 특정 키가 이 해시 테이블의 지정된 값에 매핑되는지 테스트합니다.
- `boolean containsKey ( Object key)` — 지정된 객체가 이 해시 테이블의 키인지 테스트합니다.
- `Enumeration elements ()` — 이 해시 테이블의 값 열거를 반환합니다.
- `Object get ( Object key)` — 이 해시 테이블에서 지정된 키가 매핑되는 값을 반환합니다.
- `boolean isEmpty ()` — 이 해시 테이블이 어떤 키도 값에 매핑하지 않는지 테스트합니다.
- `Enumeration keys ()` — 이 해시 테이블의 키 열거를 반환합니다.
- `Object put ( Object key, Object value)` — 이 해시 테이블에서 지정된 key 를 지정된 value 로 매핑합니다.
- `protected  void rehash ()` — 해시 테이블의 내용을 용량이 큰 해시 테이블로 다시 해시합니다.
- `Object remove ( Object key)` — 해시 테이블에서 키와 해당 값을 제거합니다.
- `int size ()` — 이 해시 테이블의 키 수를 반환합니다.
- `String toString ()` — 이 해시 테이블의 다소 긴 문자열 표현을 반환합니다.

## 생성자 상세

### Hashtable

```java
public Hashtable(int initialCapacity)
```

- 지정된 초기 용량을 사용하여 
새로운 빈 해시 테이블을 구성합니다.

**Parameters:**
- `initialCapacity` - 해시 테이블의 초기 용량

**Throws:**
- `IllegalArgumentException` - 초기 용량이 
 0보다 작은 경우

**Since:**
- JDK1.0

### Hashtable

```java
public Hashtable()
```

- 기본 용량과 로드 팩터를 사용하여 
새로운 빈 해시 테이블을 구성합니다.

**Since:**
- JDK1.0

### size

```java
public int size()
```

**Returns:**
- 이 해시 테이블의 키 수

**Since:**
- JDK1.0

### isEmpty

```java
public boolean isEmpty()
```

**Returns:**
- 이 해시 테이블이 어떤 키도 값에 매핑하지 않으면 
 `true`, 그렇지 않으면 `false`

**Since:**
- JDK1.0

### keys

```java
public Enumeration keys()
```

**Returns:**
- 이 해시 테이블의 키 열거

**Since:**
- JDK1.0

**See Also:**
- ``Enumeration``, 
``elements()``

### elements

```java
public Enumeration elements()
```

**Returns:**
- 이 해시 테이블의 값 열거

**Since:**
- JDK1.0

**See Also:**
- ``Enumeration``, 
``keys()``

### contains

```java
public boolean contains(Object value)
```

**Parameters:**
- `value` - 검색할 값

**Returns:**
- 이 해시 테이블에서 특정 키가 
 `value` 인자에 매핑되면 
 `true`, 그렇지 않으면 `false`

**Throws:**
- `NullPointerException` - 값이 `null`인 경우

**Since:**
- JDK1.0

**See Also:**
- ``containsKey(java.lang.Object)``

### containsKey

```java
public boolean containsKey(Object key)
```

**Parameters:**
- `key` - 가능한 키

**Returns:**
- 지정된 객체가 이 해시 테이블의 키면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

**See Also:**
- ``contains(java.lang.Object)``

### get

```java
public Object get(Object key)
```

**Parameters:**
- `key` - 해시 테이블의 키

**Returns:**
- 이 해시 테이블에서 키가 매핑되는 값 또는 
 이 해시 테이블에서 키가 어떤 값에도 매핑되지 않으면 
 `null`

**Since:**
- JDK1.0

**See Also:**
- ``put(java.lang.Object, java.lang.Object)``

### rehash

```java
protected void rehash()
```

**Since:**
- JDK1.0

### put

```java
public Object put(Object key,
                  Object value)
```

**Parameters:**
- `value` - 값

**Returns:**
- 이 해시 테이블에서 지정된 키의 이전 값 또는 
 이전 값이 없으면 `null`

**Throws:**
- `NullPointerException` - 키 또는 값이 
 `null`인 경우

**Since:**
- JDK1.0

**See Also:**
- ``Object.equals(java.lang.Object)``, 
``get(java.lang.Object)``

### remove

```java
public Object remove(Object key)
```

**Parameters:**
- `key` - 제거해야 하는 키

**Returns:**
- 이 해시 테이블에서 키가 매핑된 값 또는 
 키가 매핑되지 않았으면 `null`

**Since:**
- JDK1.0

### clear

```java
public void clear()
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
- 이 해시 테이블의 문자열 표현

**Since:**
- JDK1.0

## 메서드 상세

### size

```java
public int size()
```

**Returns:**
- 이 해시 테이블의 키 수

**Since:**
- JDK1.0

### isEmpty

```java
public boolean isEmpty()
```

**Returns:**
- 이 해시 테이블이 어떤 키도 값에 매핑하지 않으면 
 `true`, 그렇지 않으면 `false`

**Since:**
- JDK1.0

### keys

```java
public Enumeration keys()
```

**Returns:**
- 이 해시 테이블의 키 열거

**Since:**
- JDK1.0

**See Also:**
- ``Enumeration``, 
``elements()``

### elements

```java
public Enumeration elements()
```

**Returns:**
- 이 해시 테이블의 값 열거

**Since:**
- JDK1.0

**See Also:**
- ``Enumeration``, 
``keys()``

### contains

```java
public boolean contains(Object value)
```

**Parameters:**
- `value` - 검색할 값

**Returns:**
- 이 해시 테이블에서 특정 키가 
 `value` 인자에 매핑되면 
 `true`, 그렇지 않으면 `false`

**Throws:**
- `NullPointerException` - 값이 `null`인 경우

**Since:**
- JDK1.0

**See Also:**
- ``containsKey(java.lang.Object)``

### containsKey

```java
public boolean containsKey(Object key)
```

**Parameters:**
- `key` - 가능한 키

**Returns:**
- 지정된 객체가 이 해시 테이블의 키면 `true`, 
 그렇지 않으면 `false`

**Since:**
- JDK1.0

**See Also:**
- ``contains(java.lang.Object)``

### get

```java
public Object get(Object key)
```

**Parameters:**
- `key` - 해시 테이블의 키

**Returns:**
- 이 해시 테이블에서 키가 매핑되는 값 또는 
 이 해시 테이블에서 키가 어떤 값에도 매핑되지 않으면 
 `null`

**Since:**
- JDK1.0

**See Also:**
- ``put(java.lang.Object, java.lang.Object)``

### rehash

```java
protected void rehash()
```

**Since:**
- JDK1.0

### put

```java
public Object put(Object key,
                  Object value)
```

**Parameters:**
- `value` - 값

**Returns:**
- 이 해시 테이블에서 지정된 키의 이전 값 또는 
 이전 값이 없으면 `null`

**Throws:**
- `NullPointerException` - 키 또는 값이 
 `null`인 경우

**Since:**
- JDK1.0

**See Also:**
- ``Object.equals(java.lang.Object)``, 
``get(java.lang.Object)``

### remove

```java
public Object remove(Object key)
```

**Parameters:**
- `key` - 제거해야 하는 키

**Returns:**
- 이 해시 테이블에서 키가 매핑된 값 또는 
 키가 매핑되지 않았으면 `null`

**Since:**
- JDK1.0

### clear

```java
public void clear()
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
- 이 해시 테이블의 문자열 표현

**Since:**
- JDK1.0
