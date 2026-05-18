# Class Class

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Class
```

## 설명

**extends Object:**

Java에서 사용하는 class나 Interface를 대표하는 클래스.

## 메서드 요약

- `static Class forName ( String name)` — 특정 클래스를 찾는다.
- `String getName ()` — 현 클래스 명을 구한다.
- `InputStream getResourceAsStream ( String name)` — 특정 리소스를 구한다.
- `boolean isArray ()` — 현 클래스가 배열 클래스인지 여부를 구한다.
- `boolean isAssignableFrom ( Class c)` — 매개변수로 전달된 클래스에서 파생된 객체를 현 클래스에서 파생된 객체에 할당할 수 있는지 여부를 구한다.
- `boolean isInstance ( Object o)` — 특정 객체가 현 클래스에서 파생된 객체인지 여부를 구한다.
- `boolean isInterface ()` — 현 클래스가 인터페이스인지 여부를 구한다.
- `Object newInstance ()` — 현 클래스를 사용해서 새로운 객체를 생성시킨다.
- `String toString ()` — 현 클래스를 나타내는 문자열을 구한다.

## 메서드 상세

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`
- Following copied from class: `java.lang.Object`

**Returns:**
- 현 객체를 나타내는 문자열.

### getName

```java
public String getName()
```

**Returns:**
- 클래스명을 나타내는 문자열.

### isInterface

```java
public boolean isInterface()
```

**Returns:**
- 인터페이스이면 true 아니면 false.

### newInstance

```java
public Object newInstance()
                   throws InstantiationException,
                          IllegalAccessException
```

**Returns:**
- 생성된 자바 객체.

**Throws:**
- `InstantiationException` - ┚섶薨봇
