# Class Spacer

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Item
        |
        +--javax.microedition.lcdui.Spacer
```

## 설명

**extends Item:**

설정 가능한 최소 크기를 가진 비어 있는 비대화식 항목. 
최소 너비는 `Form`의 같은 행에서 `Item` 사이에 
유연성 있는 공간을 할당하는 데 유용합니다. 
최소 높이는 행의 특정 최소 높이를 적용하는 데 유용합니다. 
응용 프로그램은 음수가 아닌 값으로 
최소 너비나 높이를 설정할 수 있습니다. 
최소 너비와 높이에 구현 시 정의한 
최대값을 적용할 수 있습니다.

`Spacer`의 잠금 해제된 기본 너비는 
현재 최소 너비와 같습니다. 잠금 해제된 기본 높이는 
현재 최소 높이와 같습니다.

`Spacer`의 주요 용도는 
다른 항목을 배치하는 것이므로 
비대화식으로만 사용할 수 있으며 
응용 프로그램은 `Spacer`에 `Command`를 
추가할 수 없습니다. `Item`에 레이블이 있으면 
장치마다 다른 방법으로 레이아웃에 영향을 미칠 수 있으므로 
`Spacer`의 레이블은 항상 `null`로 
제한되어 있으며 응용 프로그램은 
이를 변경할 수 없습니다.

**Since:**
- MIDP 2.0

## 필드 요약

## 생성자 요약

- Spacer (int minWidth,
 int minHeight) 제공된 최소 크기로 새 Spacer 를 만듭니다.

## 메서드 요약

- `void addCommand ( Command cmd)` — Spacer 는 Command 를 가질 수 없으므로 이 메소드는 호출될 때마다 항상 IllegalStateException 을 발생합니다.
- `void setDefaultCommand ( Command cmd)` — 스페이서는 Command를 가질 수 없으므로 이 메소드는 호출될 때마다 항상 IllegalStateException 을 발생합니다.
- `void setLabel ( String label)` — Spacer 는 null 레이블만 가질 수 있으므로 이 메소드는 호출될 때마다 항상 IllegalStateException 을 발생합니다.
- `void setMinimumSize (int minWidth, int minHeight)` — 이 스페이서의 최소 크기를 설정합니다.

## 생성자 상세

### Spacer

```java
public Spacer(int minWidth,
              int minHeight)
```

- 제공된 최소 크기로 새 
`Spacer`를 만듭니다. 
`Spacer`의 
레이블은 `null`입니다. 
최소 크기는 0 이상이어야 합니다. 
`minWidth`가 구현 시 
정의한 최대 너비보다 크면 
최대 너비가 사용됩니다. 
`minHeight`가 구현 시 
정의한 최대 높이보다 크면 최대 높이가 사용됩니다.

**Parameters:**
- `minHeight` - 최소 높이(단위: 픽셀)

**Throws:**
- `IllegalArgumentException` - `minWidth` 또는 
`minHeight`가 0 미만인 경우

### setMinimumSize

```java
public void setMinimumSize(int minWidth,
                           int minHeight)
```

**Parameters:**
- `minHeight` - 최소 높이(단위: 픽셀)

**Throws:**
- `IllegalArgumentException` - `minWidth` 
또는 `minHeight`가 0 미만인 경우

### addCommand

```java
public void addCommand(Command cmd)
```

**Overrides:**
- `addCommand` in class `Item`

**Parameters:**
- `cmd` - `Command`

**Throws:**
- `IllegalStateException` - 항상

### setDefaultCommand

```java
public void setDefaultCommand(Command cmd)
```

**Overrides:**
- `setDefaultCommand` in class `Item`

**Parameters:**
- `cmd` - `Command`

**Throws:**
- `IllegalStateException` - 항상

### setLabel

```java
public void setLabel(String label)
```

**Overrides:**
- `setLabel` in class `Item`

**Parameters:**
- `label` - 레이블 문자열

**Throws:**
- `IllegalStateException` - 항상

**See Also:**
- ``Item.getLabel()``

## 메서드 상세

### setMinimumSize

```java
public void setMinimumSize(int minWidth,
                           int minHeight)
```

**Parameters:**
- `minHeight` - 최소 높이(단위: 픽셀)

**Throws:**
- `IllegalArgumentException` - `minWidth` 
또는 `minHeight`가 0 미만인 경우

### addCommand

```java
public void addCommand(Command cmd)
```

**Overrides:**
- `addCommand` in class `Item`

**Parameters:**
- `cmd` - `Command`

**Throws:**
- `IllegalStateException` - 항상

### setDefaultCommand

```java
public void setDefaultCommand(Command cmd)
```

**Overrides:**
- `setDefaultCommand` in class `Item`

**Parameters:**
- `cmd` - `Command`

**Throws:**
- `IllegalStateException` - 항상

### setLabel

```java
public void setLabel(String label)
```

**Overrides:**
- `setLabel` in class `Item`

**Parameters:**
- `label` - 레이블 문자열

**Throws:**
- `IllegalStateException` - 항상

**See Also:**
- ``Item.getLabel()``
