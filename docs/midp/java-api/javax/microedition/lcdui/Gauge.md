# Class Gauge

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Item
        |
        +--javax.microedition.lcdui.Gauge
```

## 설명

**extends Item:**

정수 값의 그래픽 디스플레이(예: 막대 그래프)를 구현합니다. 
`Gauge`는 0에서 *최대값*까지의 범위(포함)에 있는 
*현재 값*을 포함합니다. 응용 프로그램은 
현재 값과 최대값을 제어할 수 있습니다. 
응용 프로그램에서 지정하는 값의 범위는 장치의 구분되는 시각적 상태 수보다 
클 수 있으므로 두 개 이상의 값이 동일한 
시각적 표현을 가져야 합니다.

예를 들어, 0에서 `99`까지의 값 범위를 
갖는 `Gauge` 객체가 1-10개의 막대 집합을 사용하여 
`Gauge`의 근사값을 표시하는 장치에서 실행 중인 
경우를 가정합니다. 장치에서 한 개의 막대는 0-9의 값을 표시하고 
두 개의 막대는 10-`19`의 값을, 
세 개의 막대는 `20`-`29`의 값을 
표시할 수 있습니다.

`Gauge`는 대화형이거나 비대화형일 수 있습니다. 
응용 프로그램은 상호 작용 모드에 관계없이 언제든지 
`Gauge`의 값을 설정하거나 검색할 수 있습니다. 
객체가 대화형 모드로 만들어지는지 여부에 따라 구현 시 
막대 그래프의 시각적 모양이 
변경될 수 있습니다.

대화형 모드에서는 사용자가 값을 수정할 수 있습니다. 
사용자는 언제든 해당 값을 위로나 아래로 1씩 변경할 방법이 있으며 보다 
큰 증분으로 값을 변경하는 방법도 있습니다. 
사용자는 설정된 범위를 벗어나는 값으로 이동할 수 없습니다. 
따라서 응용 프로그램에서 
초기 값을 설정한 다음 사용자가 
그 이후 값부터 수정하도록 허용하는 것이 좋습니다. 
사용자가 값과 상호 작용하고 있는 동안에도 응용 프로그램은 
해당 값을 수정할 수 있습니다.

많은 경우 사용자가 값을 수정하는 유일한 방법은 버튼을 눌러 
한 번에 한 단위씩 값을 늘리거나 줄이는 것입니다. 
따라서 응용 프로그램은 몇 십 개를 넘지 않는 범위 내에서 
지정해야 합니다.

비대화형 모드에서는 사용자가 값을 수정할 수 없습니다. 
비대화형 모드는 사용자에게 오래 실행되는 작업 상태에 관한 피드백을 
제공하기 위해 사용됩니다. 비대화형 모드는 주로 오래 실행되는 작업 중에 
사용자에게 피드백을 제공하는 "진행 표시기"나 
"작업 표시기"로 사용됩니다. 
응용 프로그램은 `setValue()` 메소드를 사용하여 
주기적으로 값을 업데이트할 수 있습니다.

비대화형 `Gauge`의 범위는 유한하거나 무한할 수 있습니다. 
`Gauge`의 범위가 유한하면 0과 응용 프로그램에서 
설정한 최대값 사이의 정수 값(포함)을 가집니다. 구현 시에는 위에서 
설명한 대로 이 값에 대한 그래픽 표현을 
제공합니다.

무한 범위를 가지는 비대화형 `Gauge`는 
계속 유휴 지속, 증분 유휴, 계속 실행, 증분 업데이트의 네 상태 중 
하나에 있습니다. 이러한 상태는 작업의 특정 수준이 발생 중임을 
사용자에게 알리는 것이 목적입니다. 
증분 업데이트를 사용하는 경우 작업에 대해 
알려진 종점이 없어도 진행 상태를 사용자에게 알릴 수 있습니다. 
계속 실행을 사용하는 경우에는 사용자에게 보고할 진행이 없으며 
알려진 종점이 없습니다. 
계속 실행은 단지 사용 중임을 알리는 표시기입니다. 
구현 시 이러한 내용을 적절하게 표시하는 
그래픽 디스플레이를 사용해야 합니다. 
구현 시 무한 지속 게이지와 무한 증분 게이지에 다양한 그래픽을 
사용할 수 있습니다. 이러한 이유로 각 모드에 대해 
별도의 유휴 상태가 존재합니다. 
예를 들어, 구현 시 계속 실행 상태의 모래 시계나 회전 시계를 
표시할 수 있지만 증분 업데이트 상태에서는 비치볼이나 
줄무늬 막대 사탕 같은 다양한 상태의 애니메이션을 표시할 수 있습니다.

계속 유휴 상태나 증분 유휴 상태에서 `Gauge`는 
아무 작업도 발생하지 않음을 나타냅니다. 
증분 업데이트 상태에서 `Gauge`는 작업을 나타내지만 
해당 그래픽 표현은 응용 프로그램에서 `setValue()`에 
대한 호출을 사용하여 업데이트를 요청하는 경우에만 
업데이트되어야 합니다. 계속 실행 상태에서 `Gauge`는 
응용 프로그램으로부터의 업데이트 요청 없이도 
계속 실행되는 애니메이션을 표시하여 
작업을 나타냅니다.

`Gauge`가 비대화형이고 무한 범위를 갖도록 
설정된 경우에만 `CONTINUOUS_IDLE`, 
`INCREMENTAL_IDLE`, 
`CONTINUOUS_RUNNING` 
및 `INCREMENTAL_UPDATING` 값이 특별한 의미를 갖습니다. 
`Gauge`가 대화형이거나 유한 범위를 갖도록 설정된 경우 
이러한 값은 일반 값으로 간주됩니다.

또한 `Gauge`를 진행 표시기로 사용하는 
응용 프로그램은 일반적으로 사용자가 진행 중인 작업을 중단시킬 수 있는 
`Gauge`를 포함하는 컨테이너에 
``STOP`` 명령을 연결해야 합니다.

### 응용 프로그램 개발자를 위한 참고 사항

위에서 언급한 대로 오래 실행되는 작업 도중 
사용자에게 피드백을 제공하기 위해 비대화형 `Gauge`가 
사용될 수 있습니다. 응용 프로그램에서 
이미 알려진 종점으로 진행할 때 
작업의 진행을 관찰할 수 있는 경우 응용 프로그램은 
유한 범위를 갖는 비대화형 `Gauge`를 사용해야 합니다. 
예를 들어, 응용 프로그램에서 크기가 `20`KB로 
알려진 파일을 다운로드한다고 가정합니다. 
응용 프로그램은 `Gauge`의 최대값을 `20`으로 
설정하고 게이지 값을 지금까지 다운로드한 KB로 설정합니다. 
지정된 시간에 완료된 작업의 비율을 보여주는 
`Gauge`가 사용자에게 제시됩니다.

반면 응용 프로그램에서 알 수 없는 크기의 파일을 
다운로드하고 있는 경우 응용 프로그램은 유한 범위를 갖는 비대화형 `Gauge`를 
사용해야 합니다. 응용 프로그램은 주기적으로(예를 들어 
입력 버퍼가 채워질 때마다) `setValue(INCREMENTAL_UPDATING)`를 
호출해야 합니다. 그러면 사용자에게 진행의 
발생 비율을 표시할 수 있습니다.

마지막으로 응용 프로그램이 작업을 수행하지만 
진행을 파악할 수 있는 방법이 없다면 비대화형 `Gauge`가 
무한 범위를 갖도록 설정하고 값을 `CONTINUOUS_RUNNING`이나 
`CONTINUOUS_IDLE` 중 
하나로 설정해야 합니다. 
예를 들어, 응용 프로그램에서 네트워크 서버에 요청을 발행하고 
서버가 응답 대기하는 것을 차단하려는 경우 `Gauge`의 상태를 
응답 대기 전에는 `CONTINUOUS_RUNNING`으로, 
응답을 받은 다음에는 `CONTINUOUS_IDLE`로 
설정해야 합니다.

**Since:**
- MIDP 1.0

## 필드 요약

- `static int CONTINUOUS_IDLE` — 무한 범위를 갖는 비대화형 Gauge 의 계속 유휴 상태를 나타내는 값.
- `static int CONTINUOUS_RUNNING` — 무한 범위를 갖는 비대화형 Gauge 의 계속 실행 상태를 나타내는 값.
- `static int INCREMENTAL_IDLE` — 무한 범위를 갖는 비대화형 Gauge 의 증분 유휴 상태를 나타내는 값.
- `static int INCREMENTAL_UPDATING` — 무한 범위를 갖는 비대화형 Gauge 의 증분 업데이트 상태를 나타내는 값.
- `static int INDEFINITE` — Gauge 가 무한 범위를 갖는다는 것을 나타내기 위해 최대값으로 특수 값이 사용되었습니다.

## 생성자 요약

- Gauge ( String label,
 boolean interactive,
 int maxValue,
 int initialValue) 대화형 모드나 비대화형 모드에서 지정된 최대값 및 
초기 값을 사용하여 지정된 레이블을 갖는 
새 Gauge 객체를 만듭니다.

## 메서드 요약

- `int getMaxValue ()` — 이 Gauge 객체의 최대값을 가져옵니다.
- `int getValue ()` — 이 Gauge 객체의 현재 값을 가져옵니다.
- `boolean isInteractive ()` — 사용자가 Gauge 의 값을 변경할 수 있는지 여부를 알려줍니다.
- `void setMaxValue (int maxValue)` — 이 Gauge 객체의 최대값을 설정합니다.
- `void setValue (int value)` — 이 Gauge 객체의 현재 값을 설정합니다.

## 필드 상세

### INDEFINITE

```java
public static final int INDEFINITE
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### CONTINUOUS_IDLE

```java
public static final int CONTINUOUS_IDLE
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### INCREMENTAL_IDLE

```java
public static final int INCREMENTAL_IDLE
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### CONTINUOUS_RUNNING

```java
public static final int CONTINUOUS_RUNNING
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### INCREMENTAL_UPDATING

```java
public static final int INCREMENTAL_UPDATING
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### Gauge

```java
public Gauge(String label,
             boolean interactive,
             int maxValue,
             int initialValue)
```

- 대화형 모드나 비대화형 모드에서 지정된 최대값 및 
초기 값을 사용하여 지정된 레이블을 갖는 
새 `Gauge` 객체를 만듭니다. 
대화형 모드(`interactive`가 
`true`)에서 최대값은 0보다 커야 하며 
그렇지 않으면 예외가 발생됩니다. 
비대화형 모드(`interactive`가 
`false`)에서 최대값은 0보다 크거나 
특수 값 `INDEFINITE`과 같아야 하며 그렇지 않으면 예외가 발생됩니다.

최대값이 0보다 큰 경우 게이지는 
유한 범위를 갖습니다. 
이 경우 초기 값은 0-`maxValue` 범위(포함)에 있어야 합니다. 
초기 값이 0보다 작은 경우 값은 0으로 설정됩니다. 
초기 값이 `maxValue` 보다 큰 경우 
`maxValue`로 설정됩니다.

`interactive`가 `false`이고 
최대값이 `INDEFINITE`인 경우 무한 범위를 갖는 
비대화형 게이지가 만들어집니다. 
초기 값은 `CONTINUOUS_IDLE`, 
`INCREMENTAL_IDLE`, `CONTINUOUS_RUNNING`, 
`INCREMENTAL_UPDATING` 중 하나여야 합니다.

**Parameters:**
- `initialValue` - `[0..maxValue]` 범위의 초기 값, 
또는 `maxValue`가 `INDEFINITE`인 경우 
`CONTINUOUS_IDLE`, `INCREMENTAL_IDLE`, 
`CONTINUOUS_RUNNING`, 
`INCREMENTAL_UPDATING` 중 하나

**Throws:**
- `IllegalArgumentException` - 무한 범위를 갖는 비대화형 게이지에 대해 
initialValue가 `CONTINUOUS_IDLE`, 
`INCREMENTAL_IDLE`, `CONTINUOUS_RUNNING`, `INCREMENTAL_UPDATING` 
중 하나가 아닌 경우

**See Also:**
- ``INDEFINITE``, 
``CONTINUOUS_IDLE``, 
``INCREMENTAL_IDLE``, 
``CONTINUOUS_RUNNING``, 
``INCREMENTAL_UPDATING``

### setValue

```java
public void setValue(int value)
```

**Parameters:**
- `value` - 새 값

**Throws:**
- `IllegalArgumentException` - 무한 범위를 갖는 
비대화형 게이지에 대한 값이 `CONTINUOUS_IDLE`, 
`INCREMENTAL_IDLE`, `CONTINUOUS_RUNNING`, 
`INCREMENTAL_UPDATING` 중 하나가 아닌 경우

**See Also:**
- ``CONTINUOUS_IDLE``, 
``INCREMENTAL_IDLE``, 
``CONTINUOUS_RUNNING``, 
``INCREMENTAL_UPDATING``, 
``getValue()``

### getValue

```java
public int getValue()
```

**Returns:**
- `Gauge`의 현재 값

**See Also:**
- ``CONTINUOUS_IDLE``, 
``INCREMENTAL_IDLE``, 
``CONTINUOUS_RUNNING``, 
``INCREMENTAL_UPDATING``, 
``setValue(int)``

### setMaxValue

```java
public void setMaxValue(int maxValue)
```

**Parameters:**
- `maxValue` - 새 최대값

**Throws:**
- `IllegalArgumentException` - `masValue`가 유효하지 않은 경우

**See Also:**
- ``INDEFINITE``, 
``getMaxValue()``

### getMaxValue

```java
public int getMaxValue()
```

**Returns:**
- `Gauge`의 최대값, 또는 
`INDEFINITE`

**See Also:**
- ``INDEFINITE``, 
``setMaxValue(int)``

### isInteractive

```java
public boolean isInteractive()
```

**Returns:**
- `Gauge`가 대화형인지 
여부를 나타내는 부울

## 생성자 상세

### Gauge

```java
public Gauge(String label,
             boolean interactive,
             int maxValue,
             int initialValue)
```

- 대화형 모드나 비대화형 모드에서 지정된 최대값 및 
초기 값을 사용하여 지정된 레이블을 갖는 
새 `Gauge` 객체를 만듭니다. 
대화형 모드(`interactive`가 
`true`)에서 최대값은 0보다 커야 하며 
그렇지 않으면 예외가 발생됩니다. 
비대화형 모드(`interactive`가 
`false`)에서 최대값은 0보다 크거나 
특수 값 `INDEFINITE`과 같아야 하며 그렇지 않으면 예외가 발생됩니다.

최대값이 0보다 큰 경우 게이지는 
유한 범위를 갖습니다. 
이 경우 초기 값은 0-`maxValue` 범위(포함)에 있어야 합니다. 
초기 값이 0보다 작은 경우 값은 0으로 설정됩니다. 
초기 값이 `maxValue` 보다 큰 경우 
`maxValue`로 설정됩니다.

`interactive`가 `false`이고 
최대값이 `INDEFINITE`인 경우 무한 범위를 갖는 
비대화형 게이지가 만들어집니다. 
초기 값은 `CONTINUOUS_IDLE`, 
`INCREMENTAL_IDLE`, `CONTINUOUS_RUNNING`, 
`INCREMENTAL_UPDATING` 중 하나여야 합니다.

**Parameters:**
- `initialValue` - `[0..maxValue]` 범위의 초기 값, 
또는 `maxValue`가 `INDEFINITE`인 경우 
`CONTINUOUS_IDLE`, `INCREMENTAL_IDLE`, 
`CONTINUOUS_RUNNING`, 
`INCREMENTAL_UPDATING` 중 하나

**Throws:**
- `IllegalArgumentException` - 무한 범위를 갖는 비대화형 게이지에 대해 
initialValue가 `CONTINUOUS_IDLE`, 
`INCREMENTAL_IDLE`, `CONTINUOUS_RUNNING`, `INCREMENTAL_UPDATING` 
중 하나가 아닌 경우

**See Also:**
- ``INDEFINITE``, 
``CONTINUOUS_IDLE``, 
``INCREMENTAL_IDLE``, 
``CONTINUOUS_RUNNING``, 
``INCREMENTAL_UPDATING``

### setValue

```java
public void setValue(int value)
```

**Parameters:**
- `value` - 새 값

**Throws:**
- `IllegalArgumentException` - 무한 범위를 갖는 
비대화형 게이지에 대한 값이 `CONTINUOUS_IDLE`, 
`INCREMENTAL_IDLE`, `CONTINUOUS_RUNNING`, 
`INCREMENTAL_UPDATING` 중 하나가 아닌 경우

**See Also:**
- ``CONTINUOUS_IDLE``, 
``INCREMENTAL_IDLE``, 
``CONTINUOUS_RUNNING``, 
``INCREMENTAL_UPDATING``, 
``getValue()``

### getValue

```java
public int getValue()
```

**Returns:**
- `Gauge`의 현재 값

**See Also:**
- ``CONTINUOUS_IDLE``, 
``INCREMENTAL_IDLE``, 
``CONTINUOUS_RUNNING``, 
``INCREMENTAL_UPDATING``, 
``setValue(int)``

### setMaxValue

```java
public void setMaxValue(int maxValue)
```

**Parameters:**
- `maxValue` - 새 최대값

**Throws:**
- `IllegalArgumentException` - `masValue`가 유효하지 않은 경우

**See Also:**
- ``INDEFINITE``, 
``getMaxValue()``

### getMaxValue

```java
public int getMaxValue()
```

**Returns:**
- `Gauge`의 최대값, 또는 
`INDEFINITE`

**See Also:**
- ``INDEFINITE``, 
``setMaxValue(int)``

### isInteractive

```java
public boolean isInteractive()
```

**Returns:**
- `Gauge`가 대화형인지 
여부를 나타내는 부울

## 메서드 상세

### setValue

```java
public void setValue(int value)
```

**Parameters:**
- `value` - 새 값

**Throws:**
- `IllegalArgumentException` - 무한 범위를 갖는 
비대화형 게이지에 대한 값이 `CONTINUOUS_IDLE`, 
`INCREMENTAL_IDLE`, `CONTINUOUS_RUNNING`, 
`INCREMENTAL_UPDATING` 중 하나가 아닌 경우

**See Also:**
- ``CONTINUOUS_IDLE``, 
``INCREMENTAL_IDLE``, 
``CONTINUOUS_RUNNING``, 
``INCREMENTAL_UPDATING``, 
``getValue()``

### getValue

```java
public int getValue()
```

**Returns:**
- `Gauge`의 현재 값

**See Also:**
- ``CONTINUOUS_IDLE``, 
``INCREMENTAL_IDLE``, 
``CONTINUOUS_RUNNING``, 
``INCREMENTAL_UPDATING``, 
``setValue(int)``

### setMaxValue

```java
public void setMaxValue(int maxValue)
```

**Parameters:**
- `maxValue` - 새 최대값

**Throws:**
- `IllegalArgumentException` - `masValue`가 유효하지 않은 경우

**See Also:**
- ``INDEFINITE``, 
``getMaxValue()``

### getMaxValue

```java
public int getMaxValue()
```

**Returns:**
- `Gauge`의 최대값, 또는 
`INDEFINITE`

**See Also:**
- ``INDEFINITE``, 
``setMaxValue(int)``

### isInteractive

```java
public boolean isInteractive()
```

**Returns:**
- `Gauge`가 대화형인지 
여부를 나타내는 부울
