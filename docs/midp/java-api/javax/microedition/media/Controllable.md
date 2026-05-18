# Interface Controllable

`package javax.microedition.media`

```text
public Control[] getControls()
```

## 설명

**Returns:**
- `Control` 객체 모음

**Throws:**
- `IllegalStateException` - `getControls`가 
잘못된 상태에서 호출된 경우 발생합니다. 
자세한 내용은 ``Player``를 
참조하십시오.

### getControl

**Parameters:**
- `controlType` - `Control`의 클래스 이름. 
클래스 이름은 클래스의 전체 이름으로 제공되어야 하며 
클래스의 패키지가 제공되지 않는 경우 
`javax.microedition.media.control` 
패키지로 간주합니다.

**Returns:**
- 컨트롤을 구현하는 객체 또는 
`null`

**Throws:**
- `IllegalStateException` - `getControl`이 
잘못된 상태에서 호출된 경우 발생합니다. 
자세한 내용은 ``Player``를 
참조하십시오.

## 메서드 요약

- `Control getControl ( String controlType)` — 지정된 Control 인터페이스를 구현하는 객체를 가져옵니다.
- `Control [] getControls ()` — 이 인터페이스를 구현하는 객체에서 Control 모음을 가져옵니다.

## 메서드 상세

### getControls

```java
public Control[] getControls()
```

**Returns:**
- `Control` 객체 모음

**Throws:**
- `IllegalStateException` - `getControls`가 
잘못된 상태에서 호출된 경우 발생합니다. 
자세한 내용은 ``Player``를 
참조하십시오.

### getControl

```java
public Control getControl(String controlType)
```

**Parameters:**
- `controlType` - `Control`의 클래스 이름. 
클래스 이름은 클래스의 전체 이름으로 제공되어야 하며 
클래스의 패키지가 제공되지 않는 경우 
`javax.microedition.media.control` 
패키지로 간주합니다.

**Returns:**
- 컨트롤을 구현하는 객체 또는 
`null`

**Throws:**
- `IllegalStateException` - `getControl`이 
잘못된 상태에서 호출된 경우 발생합니다. 
자세한 내용은 ``Player``를 
참조하십시오.
