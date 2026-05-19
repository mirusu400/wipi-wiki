---
title: "Class Call"
---

`package org.kwis.msp.handset`

```text
java.lang.Object
  |
  +--org.kwis.msp.handset.Call
```

## 설명

**extends Object:**

전화 통화에 관련된 클래스이다.

## 메서드 요약

- `static void accept ()` — 걸려온 전화를 받다
- `protected static void accept0 ()`
- `static void end ()` — 전화 거는 중 혹은 현재 통화하고 있는 중에 통화를 종료 한다
- `protected static void end0 ()`
- `static void place ( String phonenumber)` — 전화를 건다.
- `protected static void place0 ( String phonenumber)`
- `static void reject ()` — 걸려온 전화를 거부한다
- `protected static void reject0 ()`
- `static void securePPPSession ()` — 전화통화에 필요한 PPP Session을 확보한다.
- `protected static void securePPPSession0 ()`

## 메서드 상세

### securePPPSession

```java
public static void securePPPSession()
```

**Throws:**
- `IOException` - 응용 프로그램 관리자이외의 프로그램에서 불릴 경우나 기타 에러 발생

### accept

```java
public static void accept()
```

**Throws:**
- `IOException` - 응용 프로그램 관리자이외의 프로그램에서 불릴 경우나 기타 에러 발생

### reject

```java
public static void reject()
```

**Throws:**
- `IOException` - 응용 프로그램 관리자이외의 프로그램에서 불릴 경우나 기타 에러 발생

### end

```java
public static void end()
```

**Throws:**
- `IOException` - 응용 프로그램 관리자이외의 프로그램에서 불릴 경우나 기타 에러 발생

### place

```java
public static void place(String phonenumber)
```

**Parameters:**
- `phonenumber` - 전화번호

**Throws:**
- `IOException` - 응용 프로그램 관리자이외의 프로그램에서 불릴 경우나 기타 에러 발생

### securePPPSession0

```java
protected static void securePPPSession0()
```

### accept0

```java
protected static void accept0()
```

### reject0

```java
protected static void reject0()
```

### end0

```java
protected static void end0()
```

### place0

```java
protected static void place0(String phonenumber)
```

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
