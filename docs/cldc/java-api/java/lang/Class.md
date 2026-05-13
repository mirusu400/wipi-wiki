# Class Class

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Class
```

## 설명

**extends Object:**

`Class` 클래스의 인스턴스는 실행 중인 Java 응용 프로그램의 
클래스와 인터페이스를 나타냅니다. 또한 모든 배열은 `Class` 
객체로 반영되는 클래스에 속합니다. 이 객체는 동일한 요소 유형과 차원 수를 
가진 모든 배열에 공유됩니다.

`Class`에는 공개 구성자가 없습니다. `Class` 
객체는 클래스를 로드할 때 Java 가상 머신이 자동으로 
구성합니다.

다음 예에서는 `Class` 객체를 사용하여 객체의 클래스 이름을 
인쇄합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 메서드 요약

- `static Class forName ( String className)` — 지정된 문자열 이름을 가진 클래스와 연결된 Class 객체를 반환합니다.
- `String getName ()` — 이 Class 객체가 나타내는 엔티티(클래스, 인터페이스, 배열 클래스, 프리미티브 유형 또는 void)의 정규화된 이름을 String 으로 반환합니다.
- `InputStream getResourceAsStream ( String name)` — 응용 프로그램의 JAR 파일에서 지정된 이름을 가진 자원을 찾습니다.
- `boolean isArray ()` — 이 Class 객체가 배열 클래스를 나타내는지 확인합니다.
- `boolean isAssignableFrom ( Class cls)` — Class 객체에서 나타내는 클래스 또는 인스턴스가 지정된 Class 매개 변수에서 나타내는 클래스 또는 인터페이스와 동일하거나 그 수퍼 클래스 또는 상위 인터페이스인지 확인합니다.
- `boolean isInstance ( Object obj)` — 지정된 Object 가 이 Class 에서 나타내는 객체와 할당이 호환되는지 확인합니다.
- `boolean isInterface ()` — 지정된 Class 객체가 인터페이스 유형을 나타내는지 확인합니다.
- `Object newInstance ()` — 클래스의 새 인스턴스를 만듭니다.
- `String toString ()` — 객체를 문자열로 변환합니다.

## 메서드 상세

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 클래스 객체의 문자열 표현

### forName

```java
public static Class forName(String className)
                     throws ClassNotFoundException
```

**Parameters:**
- `className` - 원하는 클래스의 정규화된 이름

**Returns:**
- 지정된 이름을 가진 클래스의 `Class` 
 객체

**Throws:**
- `Error` - 다른 어떤 이유로 인해 함수가 실패한 경우

**Since:**
- JDK1.0

### newInstance

```java
public Object newInstance()
                   throws InstantiationException,
                          IllegalAccessException
```

**Returns:**
- 이 객체가 나타내는 클래스의 새로 할당된 인스턴스. 
 빈 인자 목록을 가진 `new` 표현식과 
 같은 방식으로 수행됩니다.

**Throws:**
- `InstantiationException` - 응용 프로그램이 추상 클래스나 
 인터페이스를 인스턴스화하려고 시도하거나 다른 어떤 이유로 
 인해 인스턴스화가 실패한 경우

**Since:**
- JDK1.0

### isInstance

```java
public boolean isInstance(Object obj)
```

**Parameters:**
- `obj` - 확인할 객체

**Returns:**
- `obj`가 이 클래스의 인스턴스이면 true

**Since:**
- JDK1.1

### isAssignableFrom

```java
public boolean isAssignableFrom(Class cls)
```

**Parameters:**
- `cls` - 확인되는 `Class` 객체

**Returns:**
- `cls` 유형의 객체를 이 클래스의 객체에 
할당할 수 있는지 여부를 나타내는 `boolean` 값

**Throws:**
- `NullPointerException` - 지정된 Class 매개 변수가 
 null인 경우

**Since:**
- JDK1.1

### isInterface

```java
public boolean isInterface()
```

**Returns:**
- 이 객체가 인터페이스를 나타내면 `true`, 
그렇지 않으면 `false`

### isArray

```java
public boolean isArray()
```

**Returns:**
- 이 객체가 배열 클래스를 나타내면 `true`, 
그렇지 않으면 `false`

**Since:**
- JDK1.1

### getName

```java
public String getName()
```

**Returns:**
- 이 객체가 나타내는 클래스 또는 인터페이스의 
 정규화된 이름

### getResourceAsStream

```java
public InputStream getResourceAsStream(String name)
```

**Parameters:**
- `name` - 원하는 자원 이름

**Returns:**
- `java.io.InputStream` 객체
