---
title: "Class BackLight"
---

`package org.kwis.msp.handset`

```text
java.lang.Object
  |
  +--org.kwis.msp.handset.BackLight
```

## 설명

**extends Object:**

LCD 의 백라이트를 조절하는 클래스이다.

## 메서드 요약

- `static void alwaysOn ()` — 백라이트를 계속해서 킨다
- `static void before ()` — 백라이트를 프로그램 실행 이전 상태로 유지한다
- `static void off ()` — 백라이트를 끈다
- `static void on (int id, int color, int duration)` — 백라이트를 제어하는 함수 이다.

## 메서드 상세

### on

```java
public static void on(int id,
                      int color,
                      int duration)
```

**Parameters:**
- `duration` - 백라이트가 켜져있는 시간을(msec 단위로)

### off

```java
public static void off()
```

- 백라이트를 끈다

### before

```java
public static void before()
```

- 백라이트를 프로그램 실행 이전 상태로 유지한다

### alwaysOn

```java
public static void alwaysOn()
```

- 백라이트를 계속해서 킨다

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
