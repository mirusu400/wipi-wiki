# Class System

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.System
```

## 설명

**extends Object:**

VM에 관련된 기능과 유용한 메소드 등을 모아놓은 클래스.

## 필드 요약

- `static PrintStream err` — VM에서 공통적으로 사용하는 에러 스트림.
- `static PrintStream out` — VM내에서 공통적으로 사용하는 출력 스트림.

## 메서드 요약

- `static void arraycopy ( Object src, int srcStart, Object dest, int destStart, int len)` — 자바 객체로 이루어진 배열끼리 복사한다.
- `static long currentTimeMillis ()` — 현재 시각을 1970년 1월1일 정오(UTC)기준으로 millisecond단위로 얻어온다.
- `static void exit (int status)` — 현재 수행 중인 자바 프로그램을 종료한다.
- `static void gc ()` — garbage collection을 기동 시킨다.
- `static String getProperty ( String key)` — VM 프로퍼티 값을 구한다.
- `static int identityHashCode ( Object o)` — 객체에 대한 해쉬 코드 값을 구한다.

## 필드 상세

### out

```java
public static PrintStream out
```

- VM내에서 공통적으로 사용하는 출력 스트림. 에뮬레이터에서는 콘솔에 화면 출력
 폰에서는 시리얼 출력이 될 수 있다.

### err

```java
public static PrintStream err
```

- VM에서 공통적으로 사용하는 에러 스트림. 에뮬레이터에서는 콘솔에 화면 출력
 폰에서는 시리얼 출력이 될 수 있다.

### arraycopy

```java
public static void arraycopy(Object src,
                             int srcStart,
                             Object dest,
                             int destStart,
                             int len)
```

**Parameters:**
- `len` - 복사될 객체 수.

### currentTimeMillis

```java
public static long currentTimeMillis()
```

**Returns:**
- 현재 시각을 나타내는 long값.

### exit

```java
public static void exit(int status)
```

**Parameters:**
- `status` - 종료원인을 나타낸는 정수값.

### gc

```java
public static void gc()
```

- garbage collection을 기동 시킨다.

### getProperty

```java
public static String getProperty(String key)
```

**Parameters:**
- `key` - 구하고자 하는 프로퍼티.

**Returns:**
- key에 해당하는 프로퍼티 값.

### identityHashCode

```java
public static int identityHashCode(Object o)
```

**Parameters:**
- `o` - 해쉬코드를 구하고자 하는 객체.

**Returns:**
- o에 해당하는 해쉬코드 정수 값.## 메서드 상세

### arraycopy

```java
public static void arraycopy(Object src,
                             int srcStart,
                             Object dest,
                             int destStart,
                             int len)
```

**Parameters:**
- `len` - 복사될 객체 수.

### currentTimeMillis

```java
public static long currentTimeMillis()
```

**Returns:**
- 현재 시각을 나타내는 long값.

### exit

```java
public static void exit(int status)
```

**Parameters:**
- `status` - 종료원인을 나타낸는 정수값.

### gc

```java
public static void gc()
```

- garbage collection을 기동 시킨다.

### getProperty

```java
public static String getProperty(String key)
```

**Parameters:**
- `key` - 구하고자 하는 프로퍼티.

**Returns:**
- key에 해당하는 프로퍼티 값.

### identityHashCode

```java
public static int identityHashCode(Object o)
```

**Parameters:**
- `o` - 해쉬코드를 구하고자 하는 객체.

**Returns:**
- o에 해당하는 해쉬코드 정수 값.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
