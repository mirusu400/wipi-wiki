# Class System

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.System
```

## 설명

**extends Object:**

`System` 클래스에는 여러 개의 유용한 클래스 필드와 메소드가 
 포함되어 있습니다. 이 클래스는 인스턴스화할 수 없습니다.

**Since:**
- JDK1.0, CLDC 1.0

## 필드 요약

- `static PrintStream err` — "표준" 오류 출력 스트림.
- `static PrintStream out` — "표준" 출력 스트림.

## 메서드 요약

- `static void arraycopy ( Object src, int srcOffset, Object dst, int dstOffset, int length)` — 지정된 위치부터 시작하여 지정된 소스 배열의 배열을 대상 배열의 지정된 위치에 복사합니다.
- `static long currentTimeMillis ()` — 현재 시간(밀리초)을 반환합니다.
- `static void exit (int status)` — 현재 실행 중인 Java 응용 프로그램을 종료합니다.
- `static void gc ()` — 가비지 컬렉터를 실행합니다.
- `static String getProperty ( String key)` — 지정된 키가 나타내는 시스템 등록 정보를 가져옵니다.
- `static int identityHashCode ( Object x)` — 지정된 객체의 클래스가 hashCode()를 무시하는지 여부에 관계 없이 지정된 객체에 대해 기본 메소드 hashCode()에서 반환되는 것과 동일한 해시 코드를 반환합니다.

## 필드 상세

### out

```java
public static final PrintStream out
```

**See Also:**
- ``PrintStream.println()``, 
``PrintStream.println(boolean)``, 
``PrintStream.println(char)``, 
``PrintStream.println(char[])``, 
``PrintStream.println(int)``, 
``PrintStream.println(long)``, 
``PrintStream.println(java.lang.Object)``, 
``PrintStream.println(java.lang.String)``

### err

```java
public static final PrintStream err
```

- "표준" 오류 출력 스트림. 이 스트림은 이미 열려 있으며 
 출력 데이터를 받아들일 준비가 되어 있습니다.

일반적으로 이 스트림은 디스플레이 출력이나 호스트 환경 
 또는 사용자가 지정한 다른 출력 대상에 해당합니다. 
 관례적으로 이 출력 스트림은 중요한 출력 스트림인 변수 
 `out` 값이 일반적으로 계속 모니터되지 않는 
 파일이나 다른 대상으로 리디렉션되었지만 
 사용자의 즉각적인 주의가 필요한 정보나 
 오류 메시지를 표시하는 데 사용됩니다.

### currentTimeMillis

```java
public static long currentTimeMillis()
```

**Returns:**
- 현재 시간과 1970년 1월 1일 자정(세계 표준시) 사이의 
 차이(밀리초)

### arraycopy

```java
public static void arraycopy(Object src,
                             int srcOffset,
                             Object dst,
                             int dstOffset,
                             int length)
```

**Parameters:**
- `length` - 복사되는 배열 요소 수

**Throws:**
- `NullPointerException` - `src` 또는 
 `dst`가 `null`인 경우

### identityHashCode

```java
public static int identityHashCode(Object x)
```

**Parameters:**
- `x` - hashCode가 계산되는 객체

**Returns:**
- hashCode

**Since:**
- JDK1.1

### getProperty

```java
public static String getProperty(String key)
```

**Parameters:**
- `key` - 시스템 등록 정보의 이름

**Returns:**
- 시스템 등록 정보의 문자열 값 또는 
 해당 키를 가진 등록 정보가 없는 경우 `null`

**Throws:**
- `IllegalArgumentException` - `key`가 비어 있는 경우

### exit

```java
public static void exit(int status)
```

**Parameters:**
- `status` - 종료 상태

**See Also:**
- ``Runtime.exit(int)``

### gc

```java
public static void gc()
```

**See Also:**
- ``Runtime.gc()``

## 메서드 상세

### currentTimeMillis

```java
public static long currentTimeMillis()
```

**Returns:**
- 현재 시간과 1970년 1월 1일 자정(세계 표준시) 사이의 
 차이(밀리초)

### arraycopy

```java
public static void arraycopy(Object src,
                             int srcOffset,
                             Object dst,
                             int dstOffset,
                             int length)
```

**Parameters:**
- `length` - 복사되는 배열 요소 수

**Throws:**
- `NullPointerException` - `src` 또는 
 `dst`가 `null`인 경우

### identityHashCode

```java
public static int identityHashCode(Object x)
```

**Parameters:**
- `x` - hashCode가 계산되는 객체

**Returns:**
- hashCode

**Since:**
- JDK1.1

### getProperty

```java
public static String getProperty(String key)
```

**Parameters:**
- `key` - 시스템 등록 정보의 이름

**Returns:**
- 시스템 등록 정보의 문자열 값 또는 
 해당 키를 가진 등록 정보가 없는 경우 `null`

**Throws:**
- `IllegalArgumentException` - `key`가 비어 있는 경우

### exit

```java
public static void exit(int status)
```

**Parameters:**
- `status` - 종료 상태

**See Also:**
- ``Runtime.exit(int)``

### gc

```java
public static void gc()
```

**See Also:**
- ``Runtime.gc()``
