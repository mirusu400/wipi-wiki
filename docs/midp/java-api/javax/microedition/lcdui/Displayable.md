# Class Displayable

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Displayable
```

## 설명

**Direct Known Subclasses:**
- `Canvas`, `Screen`

**extends Object:**

디스플레이에 놓일 수 있는 기능을 보유한 객체입니다. 
`Displayable` 객체에는 제목, 티커, 
0개 이상의 명령 및 이와 연관된 수신기가 있습니다. 
표시되는 내용 및 사용자와의 상호 작용은 
서브 클래스에 의해 정의됩니다.

제목 문자열에는 `줄 바꿈`이 
포함될 수 있습니다. 제목 문자열을 표시할 때는 
적절하게 줄을 바꿔야 합니다. 
예를 들어, 제목줄로 한 줄만 사용할 수 있고 
줄 바꿈 문자열이 포함된 경우에는 줄 바꿈한 줄의 
문자만 표시됩니다.

서브 클래스에 의해 다르게 지정되지 않는 경우 
새로 만든 `Displayable` 객체의 기본 상태는 다음과 같습니다.

- `Display`에 표시되지 않습니다.
- 이 `Displayable`과 연관된 
`Ticker`가 없습니다.
- 제목이 `null`입니다.
- `Commands`가 없습니다.
- `CommandListener`가 없습니다.

**Since:**
- MIDP 1.0

## 메서드 요약

- `void addCommand ( Command cmd)` — 명령을 Displayable 에 추가합니다.
- `int getHeight ()` — 응용 프로그램에서 사용 가능한 표시 가능 영역의 높이(픽셀 단위)를 가져옵니다.
- `Ticker getTicker ()` — 이 Displayable 에 사용되는 티커를 가져옵니다.
- `String getTitle ()` — Displayable 의 제목을 가져옵니다.
- `int getWidth ()` — 응용 프로그램에서 사용 가능한 표시 가능 영역의 너비(픽셀 단위)를 가져옵니다.
- `boolean isShown ()` — Displayable 이 디스플레이에서 실제로 표시되는지 확인합니다.
- `void removeCommand ( Command cmd)` — Displayable 에서 명령을 제거합니다.
- `void setCommandListener ( CommandListener l)` — `Commands` 의 수신기를 Displayable 로 설정하여 이전 CommandListener 를 대체합니다.
- `void setTicker ( Ticker ticker)` — 이 Displayable 과 함께 사용할 티커를 설정하면 이전 티커를 대체합니다.
- `void setTitle ( String s)` — Displayable 의 제목을 설정합니다.
- `protected  void sizeChanged (int w, int h)` — Displayable 의 사용 가능 영역이 변경되면 구현 시 이 메소드를 호출합니다.

## 메서드 상세

### getTitle

```java
public String getTitle()
```

**Returns:**
- 인스턴스의 제목, 또는 제목이 없는 경우 `null`

**Since:**
- MIDP 2.0

**See Also:**
- ``setTitle(java.lang.String)``

### setTitle

```java
public void setTitle(String s)
```

**Parameters:**
- `s` - 새 제목, 또는 제목이 없는 경우 `null`

**Since:**
- MIDP 2.0

**See Also:**
- ``getTitle()``

### setTicker

```java
public void setTicker(Ticker ticker)
```

**Parameters:**
- `ticker` - 이 화면에 사용된 티커 객체

**Since:**
- MIDP 2.0

**See Also:**
- ``getTicker()``

### getTicker

```java
public Ticker getTicker()
```

**Returns:**
- 사용된 티커 객체, 또는 티커가 
없는 경우 `null`

**Since:**
- MIDP 2.0

**See Also:**
- ``setTicker(javax.microedition.lcdui.Ticker)``

### isShown

```java
public boolean isShown()
```

**Returns:**
- `Displayable`이 현재 표시되는 경우 
`true`

### addCommand

```java
public void addCommand(Command cmd)
```

**Parameters:**
- `cmd` - 추가되는 명령

**Throws:**
- `NullPointerException` - `cmd`가 
`null`인 경우

### removeCommand

```java
public void removeCommand(Command cmd)
```

**Parameters:**
- `cmd` - 제거되는 명령

### setCommandListener

```java
public void setCommandListener(CommandListener l)
```

**Parameters:**
- `l` - 새 수신기 또는 `null`.

### getWidth

```java
public int getWidth()
```

**Returns:**
- 응용 프로그램에서 사용 가능한 영역의 너비

**Since:**
- MIDP 2.0

### getHeight

```java
public int getHeight()
```

**Returns:**
- 응용 프로그램에서 사용 가능한 영역의 높이

**Since:**
- MIDP 2.0

### sizeChanged

```java
protected void sizeChanged(int w,
                           int h)
```

**Parameters:**
- `h` - 사용 가능한 영역의 새 높이(픽셀 단위)

**Since:**
- MIDP 2.0
