# Class Alert

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Displayable
        |
        +--javax.microedition.lcdui.Screen
              |
              +--javax.microedition.lcdui.Alert
```

## 설명

**extends Screen:**

경고는 다음 `Displayable`로 이동하기 전에 
사용자에게 데이터를 표시하고 
특정 시간 동안 대기하는 화면입니다. 
경고에는 텍스트 문자열과 이미지가 
포함될 수 있습니다. 
`Alert`의 용도는 사용자에게 오류 및 
기타 예외 조건에 대해 알리는 것입니다.

응용 프로그램에서는 ` setTimeout(Alert.FOREVER)`을 
사용하여 경고 시간을 무한대로 설정할 수 있습니다. 
이 경우 `Alert`는 *모달*로 간주되며 구현 시 
사용자가 경고를 "닫을 수" 있는 기능을 제공하므로 
경고를 닫으면 시간 초과가 즉시 만료되었을 때와 마찬가지로 다음 
`Displayable`이 
표시됩니다.

응용 프로그램에서 경고의 시간을 
다양하게 지정*하고* 
스크롤해야 할 정도로 많은 내용을 제공한 경우에는 
자동으로 모달 경고가 됩니다.

경고는 자신의 특성을 표시하기 위해 연관된 
`AlertType`을 가질 수도 있습니다. 
구현 시에는 이러한 유형을 사용하여 사용자에게 `Alert`를 
표시할 때 적절한 사운드를 재생할 수도 있습니다. 
``AlertType.playSound()``를 참조하십시오.

경고에는 선택적 `Image`가 포함될 수도 있습니다. 
`Image`는 변경 가능하거나 
변경 불가능할 수 있습니다. 
`Image`가 변경 가능한 경우에는 
`Alert`가 이 `Image`로 구성되고 
`setImage`가 `Image`와 함께 호출될 때 
이미지 내용의 스냅샷을 생성하는 것과 같은 기능을 합니다. 
`Alert`의 내용이 표시될 때마다 
이 스냅샷이 사용됩니다. 
그 후 응용 프로그램이 해당 
`Image`를 가져오더라도 
`setImage`에 대한 다음 호출이 있을 때까지 스냅샷은 
수정되지 않습니다. `Alert`가 
현재 디스플레이에 표시되어 있으면 
스냅샷을 업데이트할 수 *없습니다*. 
이는 응용 프로그램에서 `Displayables`가 표시된 다음 
디스플레이에서 사라져야 할 정확한 시점을 
제어할 수 없기 때문입니다.

### 작업 표시기

경고에는 작업 표시기나 진행 표시기로 사용되는 
선택적 ``Gauge`` 객체가 포함될 수도 있습니다. 
기본적으로 `Alert`에는 
작업 표시기가 없지만 
``setIndicator(javax.microedition.lcdui.Gauge)`` 메소드를 사용하여 작업 표시기를 설정할 수 있습니다. 
작업 표시기로 사용되는 `Gauge` 객체는 
다음 제한 사항을 모두 준수해야 합니다.

- 비대화형이어야 합니다.
- 다른 컨테이너(`Alert` 또는 `Form`)가 
소유하지 않아야 합니다.
- `Commands`가 없어야 합니다.
- `ItemCommandListener`가 없어야 합니다.
- 레이블이 없어야 합니다(즉, 
레이블이 `null`이어야 함).
- 기본 너비와 높이는 모두 잠금 해제되어 있어야 합니다.
- 레이아웃 값은 `LAYOUT_DEFAULT`이어야 합니다.

이러한 제한 사항 중 하나라도 위반하는 
`Gauge` 객체를 응용 프로그램에서 사용하려고 시도하면 
오류가 발생합니다. 
또한 `Gauge` 객체가 `Alert` 내에서 
표시기로 사용되고 있는 경우 
응용 프로그램은 이러한 `Gauge` 상태의 어느 조각도 
수정할 수 없습니다.

### 명령 및 수신기

다른 `Displayable` 클래스와 같이 
`Alert`도 응용 프로그램에 의해 설정된 
`CommandListener`로 전달될 수 있는 
`Commands`를 사용할 수 있습니다. 
`Alert` 클래스는 `Commands` 및 수신기에 대해 
몇 가지 특수 동작을 추가합니다.

`Alert`가 만들어지는 경우 
그 내부에는 암시적인 특수 `Command` ``DISMISS_COMMAND``가 
있습니다. 응용 프로그램이 다른 `Commands`를 
`Alert`에 추가하면 `DISMISS_COMMAND`는 
암시적으로 제거됩니다. 
응용 프로그램이 다른 `Commands`를 모두 제거하면 
`DISMISS_COMMAND`는 암시적으로 복원됩니다. 
`DISMISS_COMMAND`를 추가하거나 제거하려는 
시도는 명시적으로 무시됩니다. 
따라서 `Alert`에는 
항상 최소 한 개의 `Command`가 있습니다.

`Alert`에 두 개 이상의 
`Commands`가 있는 경우에는 
자동으로 모달 `Alert`로 변경되며 
시간 초과 값은 항상 ``FOREVER``입니다. 
`Command`가 호출될 때까지 `Alert`는 
디스플레이에 남아 있습니다. 경고에 한 개의 Command(DISMISS_COMMAND 또는 
응용 프로그램에서 제공한 명령)가 있는 경우 
위에 설명된 대로 `Alert`에는 시간이 지정된 
동작이 있을 수 있습니다. 시간 초과가 발생하면 그 결과는 
사용자가 `Command`를 
명시적으로 호출한 것과 동일합니다.

`Alert`는 만들어질 때 
해당 경고와 연관된 *기본 수신기*라는 
`CommandListener`를 암시적으로 가집니다. 
``setCommandListener(javax.microedition.lcdui.CommandListener)`` 메소드를 사용하여 
이 수신기를 응용 프로그램에서 제공한 수신기로 바꿀 수 있습니다. 
응용 프로그램이 `null`을 `setCommandListener` 
메소드에 전달하여 수신기를 제거한 경우 기본 수신기가 암시적으로 복원됩니다.

``Display.setCurrent(Alert, Displayable)`` 
메소드와 ``Display.setCurrent(Displayable)`` 
메소드가 `Alert`와 
함께 호출되는 경우에는 
`Alert`가 닫힌 후에 
다른 `Displayable`로 
자동으로 이동하는 특수 동작을 정의합니다. 
`Alert`가 닫힐 때나 명령이 호출될 때 
기본 수신기가 있는 경우에만 
이러한 특수 동작이 발생합니다. 
사용자가 `Command`를 호출하고 
기본 수신기가 있는 경우 
기본 수신기는 `Command`를 무시하고 
자동 진행 동작을 구현합니다.

응용 프로그램에 자체 `CommandListener`가 
설정되어 있는 경우 자동 진행 동작을 사용할 수 없습니다. 
listener 코드에서 다른 
`Displayable`로 이동해야 합니다. 
응용 프로그램에서 수신기를 제공하면 
일반적으로 수신기의 `commandAction` 메소드에 
명령을 전달하여 `Commands`가 호출됩니다. 
전달된 `Command`는 
`Alert`에 있는 
`Commands`인 `DISMISS_COMMAND` 또는 
응용 프로그램 제공 `Commands` 중 하나가 됩니다.

응용 프로그램은 `null`을 `setCommandListener` 
메소드에 전달하여 기본 수신기를 복원할 수 있습니다.

**주:** 응용 프로그램은 
`Alert`에서 
``Displayable.setTicker``를 
사용하여 ``Ticker``를 설정할 수 있지만 구현 제한으로 인해 표시되지 않을 수 있습니다.

**Since:**
- MIDP 1.0

**See Also:**
- ``AlertType``

## 필드 요약

- `static Command DISMISS_COMMAND` — Alert 가 닫혔음을 나타내기 위해 Command 가 수신기에 전달됩니다.
- `static int FOREVER` — FOREVER 는 사용자가 닫을 때까지 Alert 가 계속 표시된다는 것을 나타냅니다.

## 생성자 요약

- Alert ( String title) 주어진 제목으로 비어 있는 
새 Alert 객체를 구성합니다.
- Alert ( String title, String alertText, Image alertImage, AlertType alertType) 지정된 제목, 내용 문자열 및 이미지, 경고 유형과 함께 
새 Alert 객체를 구성합니다.

## 메서드 요약

- `void addCommand ( Command cmd)` — `Displayable.addCommand(javax.microedition.lcdui.Command)` 와 유사하지만 응용 프로그램이 먼저 Alert 에 명령을 추가하면 `DISMISS_COMMAND` 가 암시적으로 제거됩니다.
- `int getDefaultTimeout ()` — Alert 를 표시하기 위한 기본 시간을 가져옵니다.
- `Image getImage ()` — Alert 에 사용된 Image 를 가져옵니다.
- `Gauge getIndicator ()` — 이 Alert 에 대한 작업 표시기를 가져옵니다.
- `String getString ()` — Alert 에 사용된 텍스트 문자열을 가져옵니다.
- `int getTimeout ()` — Alert 가 표시될 시간을 가져옵니다.
- `AlertType getType ()` — Alert 의 유형을 가져옵니다.
- `void removeCommand ( Command cmd)` — `Displayable.removeCommand(javax.microedition.lcdui.Command)` 와 유사하지만 응용 프로그램이 Alert 에서 마지막 명령을 제거하면 `DISMISS_COMMAND` 가 암시적으로 추가됩니다.
- `void setCommandListener ( CommandListener l)` — `Displayable.setCommandListener(javax.microedition.lcdui.CommandListener)` 와 같지만 다음과 같은 의미가 추가됩니다.
- `void setImage ( Image img)` — Alert 에 사용된 Image 를 설정합니다.
- `void setIndicator ( Gauge indicator)` — 이 Alert 에 작업 표시기를 설정합니다.
- `void setString ( String str)` — Alert 에 사용된 텍스트 문자열을 설정합니다.
- `void setTimeout (int time)` — Alert 를 표시해야 할 시간을 설정합니다.
- `void setType ( AlertType type)` — Alert 의 유형을 설정합니다.

## 필드 상세

### FOREVER

```java
public static final int FOREVER
```

**See Also:**
- `Constant Field Values`

### DISMISS_COMMAND

```java
public static final Command DISMISS_COMMAND
```

**Since:**
- MIDP 2.0

### Alert

```java
public Alert(String title)
```

- 주어진 제목으로 비어 있는 
새 `Alert` 객체를 구성합니다. 
`null`이 전달되면 `Alert`에는 제목이 없습니다. 
이 구성체를 호출하는 것은 
다음을 호출하는 것과 같습니다.

 `Alert(title, null, null, null)`

**Parameters:**
- `title` - 제목 문자열 또는 `null`

**See Also:**
- ``Alert(String, String, Image, AlertType)``

### Alert

```java
public Alert(String title,
             String alertText,
             Image alertImage,
             AlertType alertType)
```

- 지정된 제목, 내용 문자열 및 이미지, 경고 유형과 함께 
새 `Alert` 객체를 구성합니다. 
내용의 레이아웃은 구현에 따라 달라집니다. 
이러한 새 경고의 시간 초과 값은 
`getDefaultTimeout()`에서 
반환하는 것과 같은 값입니다. 
제공되는 `Image`는 변경 가능한 경우도 있고 
변경 불가능한 경우도 있습니다. 특정 `AlertTypes`의 처리 및 
동작은 ``AlertType``에 설명되어 있습니다. 
`null`을 `alertType` 매개 변수 값으로 
사용할 수 있으며 `Alert`가 특정 경고 
유형을 갖지 않음을 나타냅니다. 
`DISMISS_COMMAND`는 
새 `Alert`에 있는 
유일한 `Command`입니다. 
새 `Alert`와 연관된 `CommandListener`는 
*default listener*로 해당 동작은 
명령 및 수신기 절에 보다 
자세히 설명되어 있습니다.

**Parameters:**
- `alertType` - `Alert` 유형, 
또는 `Alert`에 특정 유형이 없는 경우 
`null`

### getDefaultTimeout

```java
public int getDefaultTimeout()
```

**Returns:**
- 기본 시간 초과(밀리초) 또는 `FOREVER`

### getTimeout

```java
public int getTimeout()
```

**Returns:**
- 기본 시간 초과(밀리초) 또는 `FOREVER`

**See Also:**
- ``setTimeout(int)``

### setTimeout

```java
public void setTimeout(int time)
```

**Parameters:**
- `time` - 기본 시간 초과(밀리초) 또는 `FOREVER`

**Throws:**
- `IllegalArgumentException` - 시간이 양수도 아니고 
`FOREVER`도 아닌 경우

**See Also:**
- ``getTimeout()``

### getType

```java
public AlertType getType()
```

**Returns:**
- `AlertType`의 
인스턴스에 대한 참조, 
또는 `Alert`에 
특정 유형이 없는 경우 `null`

**See Also:**
- ``setType(javax.microedition.lcdui.AlertType)``

### setType

```java
public void setType(AlertType type)
```

**Parameters:**
- `type` - `AlertType`, 또는 
`Alert`에 특정 유형이 없는 경우 
`null`

**See Also:**
- ``getType()``

### getString

```java
public String getString()
```

**Returns:**
- `Alert`의 텍스트 문자열, 
또는 텍스트가 없는 경우 `null`

**See Also:**
- ``setString(java.lang.String)``

### setString

```java
public void setString(String str)
```

**Parameters:**
- `str` - `Alert`의 텍스트 문자열, 
또는 텍스트가 없는 경우 `null`

**See Also:**
- ``getString()``

### getImage

```java
public Image getImage()
```

**Returns:**
- `Alert`의 이미지, 또는 
이미지가 없는 경우 `null`

**See Also:**
- ``setImage(javax.microedition.lcdui.Image)``

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - `Alert`의 이미지, 
또는 이미지가 없는 경우 `null`

**See Also:**
- ``getImage()``

### setIndicator

```java
public void setIndicator(Gauge indicator)
```

**Parameters:**
- `indicator` - 이 `Alert`에 대한 작업 표시기, 
또는 작업 표시기가 없는 경우 
`null`

**Throws:**
- `IllegalArgumentException` - `indicator`가 
`Alert`의 사용에 대한 제한을 충족시키지 못하는 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getIndicator()``

### getIndicator

```java
public Gauge getIndicator()
```

**Returns:**
- 이 `Alert`의 작업 표시기에 대한 참조, 
또는 참조가 없는 경우 
`null`

**Since:**
- MIDP 2.0

**See Also:**
- ``setIndicator(javax.microedition.lcdui.Gauge)``

### addCommand

```java
public void addCommand(Command cmd)
```

**Overrides:**
- `addCommand` in class `Displayable`

**Parameters:**
- `cmd` - 추가되는 명령

**Throws:**
- `NullPointerException` - cmd가 `null`인 경우

### removeCommand

```java
public void removeCommand(Command cmd)
```

**Overrides:**
- `removeCommand` in class `Displayable`

**Parameters:**
- `cmd` - 제거되는 명령

### setCommandListener

```java
public void setCommandListener(CommandListener l)
```

**Overrides:**
- `setCommandListener` in class `Displayable`

**Parameters:**
- `l` - 새 수신기 또는 `null`

## 생성자 상세

### Alert

```java
public Alert(String title)
```

- 주어진 제목으로 비어 있는 
새 `Alert` 객체를 구성합니다. 
`null`이 전달되면 `Alert`에는 제목이 없습니다. 
이 구성체를 호출하는 것은 
다음을 호출하는 것과 같습니다.

 `Alert(title, null, null, null)`

**Parameters:**
- `title` - 제목 문자열 또는 `null`

**See Also:**
- ``Alert(String, String, Image, AlertType)``

### Alert

```java
public Alert(String title,
             String alertText,
             Image alertImage,
             AlertType alertType)
```

- 지정된 제목, 내용 문자열 및 이미지, 경고 유형과 함께 
새 `Alert` 객체를 구성합니다. 
내용의 레이아웃은 구현에 따라 달라집니다. 
이러한 새 경고의 시간 초과 값은 
`getDefaultTimeout()`에서 
반환하는 것과 같은 값입니다. 
제공되는 `Image`는 변경 가능한 경우도 있고 
변경 불가능한 경우도 있습니다. 특정 `AlertTypes`의 처리 및 
동작은 ``AlertType``에 설명되어 있습니다. 
`null`을 `alertType` 매개 변수 값으로 
사용할 수 있으며 `Alert`가 특정 경고 
유형을 갖지 않음을 나타냅니다. 
`DISMISS_COMMAND`는 
새 `Alert`에 있는 
유일한 `Command`입니다. 
새 `Alert`와 연관된 `CommandListener`는 
*default listener*로 해당 동작은 
명령 및 수신기 절에 보다 
자세히 설명되어 있습니다.

**Parameters:**
- `alertType` - `Alert` 유형, 
또는 `Alert`에 특정 유형이 없는 경우 
`null`

### getDefaultTimeout

```java
public int getDefaultTimeout()
```

**Returns:**
- 기본 시간 초과(밀리초) 또는 `FOREVER`

### getTimeout

```java
public int getTimeout()
```

**Returns:**
- 기본 시간 초과(밀리초) 또는 `FOREVER`

**See Also:**
- ``setTimeout(int)``

### setTimeout

```java
public void setTimeout(int time)
```

**Parameters:**
- `time` - 기본 시간 초과(밀리초) 또는 `FOREVER`

**Throws:**
- `IllegalArgumentException` - 시간이 양수도 아니고 
`FOREVER`도 아닌 경우

**See Also:**
- ``getTimeout()``

### getType

```java
public AlertType getType()
```

**Returns:**
- `AlertType`의 
인스턴스에 대한 참조, 
또는 `Alert`에 
특정 유형이 없는 경우 `null`

**See Also:**
- ``setType(javax.microedition.lcdui.AlertType)``

### setType

```java
public void setType(AlertType type)
```

**Parameters:**
- `type` - `AlertType`, 또는 
`Alert`에 특정 유형이 없는 경우 
`null`

**See Also:**
- ``getType()``

### getString

```java
public String getString()
```

**Returns:**
- `Alert`의 텍스트 문자열, 
또는 텍스트가 없는 경우 `null`

**See Also:**
- ``setString(java.lang.String)``

### setString

```java
public void setString(String str)
```

**Parameters:**
- `str` - `Alert`의 텍스트 문자열, 
또는 텍스트가 없는 경우 `null`

**See Also:**
- ``getString()``

### getImage

```java
public Image getImage()
```

**Returns:**
- `Alert`의 이미지, 또는 
이미지가 없는 경우 `null`

**See Also:**
- ``setImage(javax.microedition.lcdui.Image)``

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - `Alert`의 이미지, 
또는 이미지가 없는 경우 `null`

**See Also:**
- ``getImage()``

### setIndicator

```java
public void setIndicator(Gauge indicator)
```

**Parameters:**
- `indicator` - 이 `Alert`에 대한 작업 표시기, 
또는 작업 표시기가 없는 경우 
`null`

**Throws:**
- `IllegalArgumentException` - `indicator`가 
`Alert`의 사용에 대한 제한을 충족시키지 못하는 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getIndicator()``

### getIndicator

```java
public Gauge getIndicator()
```

**Returns:**
- 이 `Alert`의 작업 표시기에 대한 참조, 
또는 참조가 없는 경우 
`null`

**Since:**
- MIDP 2.0

**See Also:**
- ``setIndicator(javax.microedition.lcdui.Gauge)``

### addCommand

```java
public void addCommand(Command cmd)
```

**Overrides:**
- `addCommand` in class `Displayable`

**Parameters:**
- `cmd` - 추가되는 명령

**Throws:**
- `NullPointerException` - cmd가 `null`인 경우

### removeCommand

```java
public void removeCommand(Command cmd)
```

**Overrides:**
- `removeCommand` in class `Displayable`

**Parameters:**
- `cmd` - 제거되는 명령

### setCommandListener

```java
public void setCommandListener(CommandListener l)
```

**Overrides:**
- `setCommandListener` in class `Displayable`

**Parameters:**
- `l` - 새 수신기 또는 `null`

## 메서드 상세

### getDefaultTimeout

```java
public int getDefaultTimeout()
```

**Returns:**
- 기본 시간 초과(밀리초) 또는 `FOREVER`

### getTimeout

```java
public int getTimeout()
```

**Returns:**
- 기본 시간 초과(밀리초) 또는 `FOREVER`

**See Also:**
- ``setTimeout(int)``

### setTimeout

```java
public void setTimeout(int time)
```

**Parameters:**
- `time` - 기본 시간 초과(밀리초) 또는 `FOREVER`

**Throws:**
- `IllegalArgumentException` - 시간이 양수도 아니고 
`FOREVER`도 아닌 경우

**See Also:**
- ``getTimeout()``

### getType

```java
public AlertType getType()
```

**Returns:**
- `AlertType`의 
인스턴스에 대한 참조, 
또는 `Alert`에 
특정 유형이 없는 경우 `null`

**See Also:**
- ``setType(javax.microedition.lcdui.AlertType)``

### setType

```java
public void setType(AlertType type)
```

**Parameters:**
- `type` - `AlertType`, 또는 
`Alert`에 특정 유형이 없는 경우 
`null`

**See Also:**
- ``getType()``

### getString

```java
public String getString()
```

**Returns:**
- `Alert`의 텍스트 문자열, 
또는 텍스트가 없는 경우 `null`

**See Also:**
- ``setString(java.lang.String)``

### setString

```java
public void setString(String str)
```

**Parameters:**
- `str` - `Alert`의 텍스트 문자열, 
또는 텍스트가 없는 경우 `null`

**See Also:**
- ``getString()``

### getImage

```java
public Image getImage()
```

**Returns:**
- `Alert`의 이미지, 또는 
이미지가 없는 경우 `null`

**See Also:**
- ``setImage(javax.microedition.lcdui.Image)``

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - `Alert`의 이미지, 
또는 이미지가 없는 경우 `null`

**See Also:**
- ``getImage()``

### setIndicator

```java
public void setIndicator(Gauge indicator)
```

**Parameters:**
- `indicator` - 이 `Alert`에 대한 작업 표시기, 
또는 작업 표시기가 없는 경우 
`null`

**Throws:**
- `IllegalArgumentException` - `indicator`가 
`Alert`의 사용에 대한 제한을 충족시키지 못하는 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getIndicator()``

### getIndicator

```java
public Gauge getIndicator()
```

**Returns:**
- 이 `Alert`의 작업 표시기에 대한 참조, 
또는 참조가 없는 경우 
`null`

**Since:**
- MIDP 2.0

**See Also:**
- ``setIndicator(javax.microedition.lcdui.Gauge)``

### addCommand

```java
public void addCommand(Command cmd)
```

**Overrides:**
- `addCommand` in class `Displayable`

**Parameters:**
- `cmd` - 추가되는 명령

**Throws:**
- `NullPointerException` - cmd가 `null`인 경우

### removeCommand

```java
public void removeCommand(Command cmd)
```

**Overrides:**
- `removeCommand` in class `Displayable`

**Parameters:**
- `cmd` - 제거되는 명령

### setCommandListener

```java
public void setCommandListener(CommandListener l)
```

**Overrides:**
- `setCommandListener` in class `Displayable`

**Parameters:**
- `l` - 새 수신기 또는 `null`
