---
title: "Class AlertType"
---

`package javax.microedition.lcdui`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.AlertType
```

## 설명

**extends Object:**

`AlertType`은 경고의 특징을 표시합니다. 
`Alert`는 사용자에게 다양한 정보를 제공하기 위해 
응용 프로그램에서 사용합니다. 
`AlertType`은 
현재 `Displayable`을 
변경하지 않고 사용자에게 직접 신호를 보내는 데 사용할 수 있습니다. 
`playSound` 메소드는 
사용자에게 경고하기 위해 
자연스러운 사운드를 생성하는 데 사용할 수 있습니다. 
예를 들어, `Canvas`를 사용하는 게임은 
`playSound`를 사용하여 
성공이나 진행을 표시할 수 있습니다. 

미리 정의된 유형은 `INFO`, `WARNING`, 
`ERROR`, `ALARM` 및 `CONFIRMATION`입니다.

**Since:**
- MIDP 1.0

**See Also:**
- ``Alert``

## 필드 요약

- `static AlertType ALARM` — ALARM AlertType 은 사용자가 이전에 알려달라고 요청한 이벤트에 대해 사용자에게 경고하기 위한 힌트입니다.
- `static AlertType CONFIRMATION` — CONFIRMATION AlertType 은 사용자 작업을 확인하기 위한 힌트입니다.
- `static AlertType ERROR` — ERROR AlertType 은 사용자에게 오류 가능성 있는 작업을 경고하기 위한 힌트입니다.
- `static AlertType INFO` — INFO AlertType 은 일반적으로 사용자에게 위협적이지 않은 정보를 제공합니다.
- `static AlertType WARNING` — WARNING AlertType 은 잠재적으로 위험한 작업을 수행하는 사용자에게 경고하기 위한 힌트입니다.

## 생성자 요약

- `protected AlertType ()` — 서브 클래스의 구성자를 보호합니다.

## 메서드 요약

- `boolean playSound ( Display display)` — 이 AlertType 의 사운드를 재생하여 사용자에게 경고합니다.

## 필드 상세

### INFO

```java
public static final AlertType INFO
```

- `INFO` `AlertType`은 
일반적으로 사용자에게 위협적이지 않은 정보를 제공합니다. 
예를 들어, 단순한 시작 화면은 
`INFO` `AlertType`일 수 있습니다.

### WARNING

```java
public static final AlertType WARNING
```

- `WARNING` `AlertType`은 
잠재적으로 위험한 작업을 수행하는 사용자에게 경고하기 위한 힌트입니다. 
예를 들어, 경고 메시지에는 
"경고: 이 작업으로 데이터가 지워질 수 있습니다."라는 
메시지가 포함될 수 있습니다.

### ERROR

```java
public static final AlertType ERROR
```

- `ERROR` `AlertType`은 
사용자에게 오류 가능성 있는 작업을 경고하기 위한 힌트입니다. 
예를 들어, 오류 경고는 "응용 프로그램을 설치할 공간이 
충분하지 않습니다."라는 메시지를 표시합니다.

### ALARM

```java
public static final AlertType ALARM
```

- `ALARM` `AlertType`은 
사용자가 이전에 알려달라고 요청한 이벤트에 대해 
사용자에게 경고하기 위한 힌트입니다. 
예를 들어, "임원 회의가 5분 후에 열립니다."라는 
메시지가 있습니다.

### CONFIRMATION

```java
public static final AlertType CONFIRMATION
```

- `CONFIRMATION` `AlertType`은 
사용자 작업을 확인하기 위한 힌트입니다. 
예를 들어, 저장 작업이 완료되었음을 알리기 위해 "저장되었습니다."라는 
메시지가 표시될 수 있습니다.

### AlertType

```java
protected AlertType()
```

- 서브 클래스의 구성자를 보호합니다.

### playSound

```java
public boolean playSound(Display display)
```

**Parameters:**
- `display` - `AlertType` 
사운드 재생할 대상

**Returns:**
- 사용자에게 경고한 경우 `true`, 
경고하지 않은 경우 `false`

**Throws:**
- `NullPointerException` - `display`가 `null`인 경우

## 생성자 상세

### AlertType

```java
protected AlertType()
```

- 서브 클래스의 구성자를 보호합니다.

### playSound

```java
public boolean playSound(Display display)
```

**Parameters:**
- `display` - `AlertType` 
사운드 재생할 대상

**Returns:**
- 사용자에게 경고한 경우 `true`, 
경고하지 않은 경우 `false`

**Throws:**
- `NullPointerException` - `display`가 `null`인 경우

## 메서드 상세

### playSound

```java
public boolean playSound(Display display)
```

**Parameters:**
- `display` - `AlertType` 
사운드 재생할 대상

**Returns:**
- 사용자에게 경고한 경우 `true`, 
경고하지 않은 경우 `false`

**Throws:**
- `NullPointerException` - `display`가 `null`인 경우
