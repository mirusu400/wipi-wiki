# Interface CommandListener

`package org.kwis.msp.lwc`

```text
public static final int FOCUS_CHANGE
```

## 설명

### SELECT

Method Detail

### commandAction

**Parameters:**
- `type` - 커맨드 선택시 SELECT, 커맨드 포커스 변경시 FOCUS_CHANGE## 필드 요약

- `static int FOCUS_CHANGE`
- `static int SELECT`

## 메서드 요약

- `void commandAction ( Command c, int type, Object obj)` — 커맨드의 내용이 선택되었거나 커맨드의 포커스가 변경되었을 경우에 이 함수를 호출하여 줍니다.

## 필드 상세

### FOCUS_CHANGE

```java
public static final int FOCUS_CHANGE
```

### SELECT

```java
public static final int SELECT
```

### commandAction

```java
public void commandAction(Command c,
                          int type,
                          Object obj)
```

**Parameters:**
- `type` - 커맨드 선택시 SELECT, 커맨드 포커스 변경시 FOCUS_CHANGE## 메서드 상세

### commandAction

```java
public void commandAction(Command c,
                          int type,
                          Object obj)
```

**Parameters:**
- `type` - 커맨드 선택시 SELECT, 커맨드 포커스 변경시 FOCUS_CHANGE

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
