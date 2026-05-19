---
title: "Interface PlayerListener"
---

`package javax.microedition.media`

```text
public static final String STARTED
```

## 설명

**See Also:**
- `Constant Field Values`

### STOPPED

**See Also:**
- `Constant Field Values`

### END_OF_MEDIA

**See Also:**
- `Constant Field Values`

### DURATION_UPDATED

**See Also:**
- `Constant Field Values`

### DEVICE_UNAVAILABLE

**See Also:**
- `Constant Field Values`

### DEVICE_AVAILABLE

**See Also:**
- `Constant Field Values`

### VOLUME_CHANGED

**See Also:**
- `Constant Field Values`

### ERROR

**See Also:**
- `Constant Field Values`

### CLOSED

**See Also:**
- `Constant Field Values`

Method Detail

### playerUpdate

**Parameters:**
- `eventData` - 연관된 이벤트 데이터

## 필드 요약

- `static String CLOSED` — Player 가 종료되면 게시됩니다.
- `static String DEVICE_AVAILABLE` — 시스템이나 우선 순위가 더 높은 다른 응용 프로그램이 현재 Player 가 사용할 수 있는 독점 장치를 해제할 때 게시됩니다.
- `static String DEVICE_UNAVAILABLE` — 시스템이나 우선 순위가 더 높은 다른 응용 프로그램이 Player 가 이전에 사용했던 독점 장치를 일시적으로 제어할 때 게시됩니다.
- `static String DURATION_UPDATED` — Player 의 재생 시간이 업데이트될 때 게시됩니다.
- `static String END_OF_MEDIA` — Player 가 미디어 끝에 도달할 때 게시됩니다.
- `static String ERROR` — 오류가 발생한 경우 게시됩니다.
- `static String STARTED` — Player 가 시작되면 게시됩니다.
- `static String STOPPED` — stop 메소드 호출에 응답하여 Player 가 정지할 때 게시됩니다.
- `static String VOLUME_CHANGED` — 오디오 장치 볼륨이 변경될 때 게시됩니다.

## 메서드 요약

- `void playerUpdate ( Player player, String event, Object eventData)` — 이 메소드는 Player 이벤트가 관찰될 때 등록된 수신기에 이벤트를 전달하기 위해 호출됩니다.

## 필드 상세

### STARTED

```java
public static final String STARTED
```

**See Also:**
- `Constant Field Values`

### STOPPED

```java
public static final String STOPPED
```

**See Also:**
- `Constant Field Values`

### END_OF_MEDIA

```java
public static final String END_OF_MEDIA
```

**See Also:**
- `Constant Field Values`

### DURATION_UPDATED

```java
public static final String DURATION_UPDATED
```

**See Also:**
- `Constant Field Values`

### DEVICE_UNAVAILABLE

```java
public static final String DEVICE_UNAVAILABLE
```

**See Also:**
- `Constant Field Values`

### DEVICE_AVAILABLE

```java
public static final String DEVICE_AVAILABLE
```

**See Also:**
- `Constant Field Values`

### VOLUME_CHANGED

```java
public static final String VOLUME_CHANGED
```

**See Also:**
- `Constant Field Values`

### ERROR

```java
public static final String ERROR
```

**See Also:**
- `Constant Field Values`

### CLOSED

```java
public static final String CLOSED
```

**See Also:**
- `Constant Field Values`

### playerUpdate

```java
public void playerUpdate(Player player,
                         String event,
                         Object eventData)
```

**Parameters:**
- `eventData` - 연관된 이벤트 데이터

## 메서드 상세

### playerUpdate

```java
public void playerUpdate(Player player,
                         String event,
                         Object eventData)
```

**Parameters:**
- `eventData` - 연관된 이벤트 데이터
