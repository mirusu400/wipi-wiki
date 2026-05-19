---
title: "Interface PlayListener"
---

`package org.kwis.msp.media`

```text
public static final int ERROR
```

## 설명

- 에러가 발생

값은 -1 입니다.

### END_OF_DATA

- 재생데이타의 마지막에 도달함

값은 1 입니다.

### START

- 재생을 시작

값은 2 입니다.

### STOP

- 재생/녹음이 멈춤

값은 3입니다.

### PAUSE

- 재생/녹음이 일시 정지

값은 4입니다.

### RESUME

- 일시 정지된 데이타의 재생 재개

값은 5 입니다.

### RECORD

- 녹음 시작

값은 6 입니다.

### FULL_OF_DATA

- 녹음 버퍼가 완전히 채워져서 더이상 녹음할 수 없음

값은 7 입니다.

Method Detail

### playUpdate

**Parameters:**
- `parm` - 각 event에 추가 전달값이 있을 경우 사용## 필드 요약

- `static int END_OF_DATA` — 재생데이타의 마지막에 도달함 값은 1 입니다.
- `static int ERROR` — 에러가 발생 값은 -1 입니다.
- `static int FULL_OF_DATA` — 녹음 버퍼가 완전히 채워져서 더이상 녹음할 수 없음 값은 7 입니다.
- `static int PAUSE` — 재생/녹음이 일시 정지 값은 4입니다.
- `static int RECORD` — 녹음 시작 값은 6 입니다.
- `static int RESUME` — 일시 정지된 데이타의 재생 재개 값은 5 입니다.
- `static int START` — 재생을 시작 값은 2 입니다.
- `static int STOP` — 재생/녹음이 멈춤 값은 3입니다.

## 메서드 요약

- `void playUpdate ( Clip clip, int event, int parm)` — 클립재생시 상태가 변할 때 불리는 메쏘드이다.

## 필드 상세

### ERROR

```java
public static final int ERROR
```

- 에러가 발생

값은 -1 입니다.

### END_OF_DATA

```java
public static final int END_OF_DATA
```

- 재생데이타의 마지막에 도달함

값은 1 입니다.

### START

```java
public static final int START
```

- 재생을 시작

값은 2 입니다.

### STOP

```java
public static final int STOP
```

- 재생/녹음이 멈춤

값은 3입니다.

### PAUSE

```java
public static final int PAUSE
```

- 재생/녹음이 일시 정지

값은 4입니다.

### RESUME

```java
public static final int RESUME
```

- 일시 정지된 데이타의 재생 재개

값은 5 입니다.

### RECORD

```java
public static final int RECORD
```

- 녹음 시작

값은 6 입니다.

### FULL_OF_DATA

```java
public static final int FULL_OF_DATA
```

- 녹음 버퍼가 완전히 채워져서 더이상 녹음할 수 없음

값은 7 입니다.

### playUpdate

```java
public void playUpdate(Clip clip,
                       int event,
                       int parm)
```

**Parameters:**
- `parm` - 각 event에 추가 전달값이 있을 경우 사용## 메서드 상세

### playUpdate

```java
public void playUpdate(Clip clip,
                       int event,
                       int parm)
```

**Parameters:**
- `parm` - 각 event에 추가 전달값이 있을 경우 사용

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
