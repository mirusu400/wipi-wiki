# Class Throwable

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Throwable
```

## 설명

**Direct Known Subclasses:**
- `Error`, `Exception`

**extends Object:**

Java에서 발생하는 Error나Exception의 최상위 클래스.

## 생성자 요약

- Throwable () Throwable 객체를 생성한다.
- Throwable ( String message) Throwable 객체를 생성한다.

## 메서드 요약

- `String getMessage ()` — Throwable이 발생한 원인에 대한 문자열을 구한다.
- `void printStackTrace ()` — 빈함수 임니다.
- `String toString ()` — 현 객체를 설명할 수 있는 문자열을 구한다.

## 생성자 상세

### Throwable

```java
public Throwable()
```

- Throwable 객체를 생성한다.

### Throwable

```java
public Throwable(String message)
```

**Parameters:**
- `message` - Throwable이 발생하게된 원인에 대한 세부 설명.

### getMessage

```java
public String getMessage()
```

**Returns:**
- Throwable이 발생한 원인에 대한 문자열.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체를 설명할 수 있는 문자열.

### printStackTrace

```java
public void printStackTrace()
```

- 빈함수 임니다.## 메서드 상세

### getMessage

```java
public String getMessage()
```

**Returns:**
- Throwable이 발생한 원인에 대한 문자열.

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 현 객체를 설명할 수 있는 문자열.

### printStackTrace

```java
public void printStackTrace()
```

- 빈함수 임니다.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
