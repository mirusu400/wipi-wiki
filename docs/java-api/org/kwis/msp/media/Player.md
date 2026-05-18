# Class Player

`package org.kwis.msp.media`

```text
java.lang.Object
  |
  +--org.kwis.msp.media.Player
```

## 설명

**extends Object:**

이 클래스는 매디어를 재생하기 위한 static 메쏘드를 포함하는 클래스입니다.

## 메서드 요약

- `static boolean pause ( Clip clip)` — 매체 처리(재생/녹음)를 일시적으로 멈춘다.
- `static boolean play ( Clip clip, boolean repeat)` — 클립의 데이타를 재생한다.
- `static boolean record ( Clip clip)` — 녹음을 시작한다.
- `static boolean resume ( Clip clip)` — 일시 정지한 매체처리(재생/녹음)를 재개한다.
- `static boolean stop ( Clip clip)` — 매체처리(재생/녹음)를 종료한다.

## 메서드 상세

### pause

```java
public static boolean pause(Clip clip)
```

**Parameters:**
- `clip` - 일시 중지시킬 클립

**Returns:**
- ture : 성공
 
 false : 이미 멈추어 있거나, 정지되어 있음

### resume

```java
public static boolean resume(Clip clip)
```

**Parameters:**
- `clip` - 재개시킬 클립

**Returns:**
- ture : 성공
 
 false : 이미 매체처리중

### stop

```java
public static boolean stop(Clip clip)
```

**Parameters:**
- `clip` - 종료시킬 클립

**Returns:**
- ture : 성공
 
 false : 전달된 clip이 재생/녹화중이 아니거나, 비 정상적으로 정지 되었음

### play

```java
public static boolean play(Clip clip,
                           boolean repeat)
```

**Parameters:**
- `repeat` - false이면 1회재생, true는 반복 재생

**Returns:**
- ture : 성공
 
 false : 재생실패

### record

```java
public static boolean record(Clip clip)
```

**Parameters:**
- `clip` - 녹음데이타를 저장할 클립

**Returns:**
- ture : 성공
 
 false : 이미 녹음중

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
