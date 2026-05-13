# Class Network

`package org.kwis.msf.io`

```
java.lang.Object
  |
  +--org.kwis.msf.io.Network
```

## 설명

**extends Object:**

응용 프로그램이 TCP/IP 인터넷 통신을 하기 위한 인터넷 접근 API 를 모은 것이다.

## 생성자 요약

- Network ()

## 메서드 요약

- `static int connect ()` — TCP/IP 인터넷 접근을 시도한다.
- `static void disconnect ()` — TCP/IO 인터넷 접근을 종료한다.

## 생성자 상세

### Network

```java
public Network()
```

### connect

```java
public static int connect()
```

**Returns:**
- 현재 접근이 가능하다면 0을 돌려주고, 접근되어 있지 않은 상태에서 접근에 성공하면 1을 돌려준다. 만일 실패하면 -1을 돌려준다

### disconnect

```java
public static void disconnect()
```

- TCP/IO 인터넷 접근을 종료한다.## 메서드 상세

### connect

```java
public static int connect()
```

**Returns:**
- 현재 접근이 가능하다면 0을 돌려주고, 접근되어 있지 않은 상태에서 접근에 성공하면 1을 돌려준다. 만일 실패하면 -1을 돌려준다

### disconnect

```java
public static void disconnect()
```

- TCP/IO 인터넷 접근을 종료한다.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
