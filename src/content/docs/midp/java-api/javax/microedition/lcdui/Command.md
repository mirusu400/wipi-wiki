---
title: "Class Command"
---

`package javax.microedition.lcdui`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.Command
```

## 설명

**extends Object:**

`Command` 클래스는 
작업의 의미 정보를 캡슐화하는 구조입니다. 
명령을 활성화하는 동작은 
이 객체에서 캡슐화되지 않습니다. 
이는 명령에는 명령이 활성화될 때 발생하는 
실제 작업이 아닌 "명령"에 대한 
정보만 포함된다는 의미입니다. 
이 작업은 `Displayable`과 연관된 
``CommandListener``에 정의됩니다. 
`Command` 객체는 
사용자 인터페이스에 *표시되며* 
이들이 표시되는 방식은 
명령 안에 포함된 의미 
정보에 따라 달라질 수 있습니다.

`Command`는 단일 작업을 활성화하는 
의미를 갖는 사용자 인터페이스 구조에 구현될 수 있습니다. 
이는 소프트 버튼, 메뉴의 항목 또는 몇 가지 다른 직접 사용자 인터페이스 
구조일 수 있습니다. 
예를 들어, 음성 인터페이스는 
이러한 명령을 음성 태그로 제시할 것입니다.

구체적인 사용자 인터페이스 구조에 대한 매핑은 
전체 명령 수에 따라서도 달라질 수 있습니다. 
예를 들어, 장치에서 사용 가능한 
물리적 버튼에 매핑하는 것보다 
더 추상적인 명령을 응용 프로그램에서 요구하는 경우 장치는 
메뉴 같은 대체 사용자 인터페이스를 사용할 수 있습니다. 
그 예로 물리적 버튼에 매핑할 수 없는 
추상 명령은 메뉴에 놓이며 레이블 "메뉴"는 프로그래밍 
가능한 버튼 중 하나에 매핑됩니다.

하나의 명령에는 *짧은 레이블*, 
선택적 *긴 레이블*, *유형*, 
*우선 순위*의 네 가지 정보가 포함됩니다. 
레이블 중 하나는 명령을 
시각적으로 표현하는 데 사용되며 
유형과 우선 순위는 명령의 의미를 나타냅니다.

### 레이블

각 명령에는 한두 개의 레이블 문자열이 포함됩니다. 
레이블 문자열은 이 명령을 표현하기 위해 응용 프로그램이 사용자에게 
표시하도록 요청하는 내용입니다. 
예를 들어, 이러한 문자열 중 하나는 장치의 소프트 버튼 옆이나 
메뉴의 한 요소로 표시됩니다. `SCREEN` 이외의 명령 유형의 경우 
제공된 레이블은 이 장치의 이 명령에 더 적합한 시스템별 레이블에 의해 
무시될 수 있습니다. 그렇지 않은 경우 레이블 문자열의 내용은 
구현 시 해석되지 않습니다.

모든 명령에는 짧은 레이블이 있습니다. 긴 레이블은 선택 사항입니다. 
긴 레이블이 명령에 없는 경우 항상 짧은 레이블이 사용됩니다.

짧은 레이블 문자열은 화면 면적을 최소로 차지하도록 
가능한 한 짧아야 합니다. 긴 레이블은 
더 길고 설명이 보다 자세하지만 
몇 단어를 초과하면 안 됩니다. 
예를 들어, 명령의 짧은 레이블은 "Play"이고 
긴 레이블은 "Play Sound Clip"일 수 있습니다.

구현 시 컨텍스트와 사용 가능한 공간을 기반으로 
사용자 인터페이스에 제시할 레이블 중 하나를 선택합니다. 
예를 들어, 명령이 소프트 버튼에 표시되면 구현 시 짧은 레이블을 사용하며, 
명령이 메뉴에 표시되고 해당 메뉴에 긴 레이블을 표시할 공간이 있는 경우에만 
긴 레이블을 사용합니다. 
구현 시 일부 명령의 짧은 레이블과 다른 명령의 긴 레이블을 
사용할 수 있으며 짧은 레이블과 긴 레이블의 사용을 마음대로 
전환할 수 있습니다. 응용 프로그램은 특정 시간에 
사용될 레이블을 결정할 수 없습니다.

### 유형

응용 프로그램은 해당 명령 유형을 사용하여 
이 명령의 의도를 지정합니다. 
예를 들어, 응용 프로그램에서 명령의 유형을 
`BACK`으로 지정하고 특정 소프트 버튼에 
"뒤로" 작업을 둘 수 있는 표준이 장치에 있으면 
구현 시 의미 정보를 가이드로 사용하여 
장치의 스타일을 따를 수 있습니다. 
정의된 유형은 
``BACK``, 
``CANCEL``, 
``EXIT``, 
``HELP``, 
``ITEM``, 
``OK``, 
``SCREEN`` 
및 
``STOP``입니다.

### 우선 순위

응용 프로그램은 우선 순위 값을 사용하여 
같은 화면의 다른 명령과 관련하여 이 명령의 중요성을 설명합니다. 
우선 순위 값은 정수이며 낮은 숫자는 더 큰 중요성을 나타냅니다. 
실제 값은 응용 프로그램에서 선택합니다. 
우선 순위 값 1은 가장 중요한 명령을 나타내며 
우선 순위 값 2, 3, 4 등은 
덜 중요한 명령을 나타냅니다.

일반적으로 구현 시 먼저 명령 유형에 따라 명령 위치를 선택한 다음 
우선 순위에 따라 유사한 명령을 놓습니다. 
이는 가장 높은 우선 순위를 갖는 명령은 
사용자가 직접 트리거할 수 있도록 
놓이며 낮은 순위를 갖는 명령은 메뉴에 놓인다는 것을 의미합니다. 
같은 화면에 같은 우선 순위와 유형을 가진 
명령이 있는 것은 오류가 아닙니다. 
이 경우 구현 시 명령의 표시 순서를 선택합니다.

예를 들어, 응용 프로그램에 다음 명령이 있는 경우

new Command("Buy", Command.ITEM, 1);
 new Command("Info", Command.ITEM, 1);
 new Command("Back", Command.BACK, 1);

두 개의 소프트 버튼이 있는 구현은 
`BACK` 명령을 
오른쪽 소프트 버튼에 매핑한 다음 
다른 명령을 포함할 수 있도록 
왼쪽 소프트 버튼에 "옵션" 
메뉴를 만듭니다. 

 

사용자가 왼쪽 소프트 버튼을 누르면 
나머지 두 개의 `Command`가 있는 메뉴가 다음과 같이 표시됩니다. 

 

응용 프로그램에 세 개의 소프트 버튼이 있는 경우 
다음과 같이 모든 명령을 소프트 버튼에 매핑할 수 있습니다.

응용 프로그램은 항상 사용자에게 다양한 화면을 통해 
진행할 수 있는 수단을 제공해야 합니다. 
응용 프로그램에서 아무런 명령이 없는 화면을 설정할 수도 있습니다. 
이는 API에서 가능하지만 일반적으로 유용하지는 않습니다. 
이러한 경우 사용자는 다른 화면으로 이동할 방법이 없습니다. 
이러한 프로그램은 단순히 오류로 간주될 것입니다. 일반적인 장치는 사용자가 응용 
프로그램 관리자에게 오류가 있는 응용 프로그램을 종료할 것을 지시할 수 있는 수단을 제공해야 합니다.

**Since:**
- MIDP 1.0

## 필드 요약

- `static int BACK` — 논리적으로 이전 화면으로 사용자를 되돌리는 이동 명령.
- `static int CANCEL` — 현재 화면에서 구현하는 대화 상자에 대한 표준 부정 대답인 명령.
- `static int EXIT` — 응용 프로그램을 종료하기 위해 사용되는 명령.
- `static int HELP` — 이 명령은 온라인 도움말에 대한 요청을 지정합니다.
- `static int ITEM` — 응용 프로그램은 이 명령 유형을 사용하여 해당 명령이 Screen 의 항목이나 Choice 의 요소에 고유하다는 것을 구현에 알려줄 수 있습니다.
- `static int OK` — 현재 화면에 의해 구현되는 대화 상자에 대한 표준 긍정 대답인 명령.
- `static int SCREEN` — 현재 화면과 관련된 응용 프로그램 정의 명령을 지정합니다.
- `static int STOP` — 현재 실행 중인 일부 프로세스, 작업 등을 중지하는 명령입니다.

## 생성자 요약

- Command ( String label,
 int commandType,
 int priority) 지정된 짧은 레이블 , 유형 및 우선 순위 를 사용하여 새 명령 객체를 만듭니다.
- Command ( String shortLabel, String longLabel,
 int commandType,
 int priority) 지정된 레이블 , 유형 및 우선 순위 를 사용하여 새 명령 객체를 만듭니다.

## 메서드 요약

- `int getCommandType ()` — 명령의 유형을 가져옵니다.
- `String getLabel ()` — 명령의 짧은 레이블을 가져옵니다.
- `String getLongLabel ()` — 명령의 긴 레이블을 가져옵니다.
- `int getPriority ()` — 명령의 우선 순위를 가져옵니다.

## 필드 상세

### SCREEN

```java
public static final int SCREEN
```

**See Also:**
- `Constant Field Values`

### BACK

```java
public static final int BACK
```

**See Also:**
- ``CANCEL``, 
``STOP``, 
`Constant Field Values`

### CANCEL

```java
public static final int CANCEL
```

**See Also:**
- ``BACK``, 
``STOP``, 
`Constant Field Values`

### OK

```java
public static final int OK
```

**See Also:**
- ``CANCEL``, 
`Constant Field Values`

### HELP

```java
public static final int HELP
```

**See Also:**
- `Constant Field Values`

### STOP

```java
public static final int STOP
```

**See Also:**
- ``BACK``, 
``CANCEL``, 
`Constant Field Values`

### EXIT

```java
public static final int EXIT
```

**See Also:**
- `Constant Field Values`

### ITEM

```java
public static final int ITEM
```

**See Also:**
- `Constant Field Values`

### Command

```java
public Command(String label,
               int commandType,
               int priority)
```

- 지정된 짧은 

레이블, 
유형 및 
우선 순위를 사용하여 새 명령 객체를 만듭니다. 

새로 만든 명령에는 긴 레이블이 없습니다. 이 구성자는 `Command(label, null, commandType, priority)`와 
동일합니다.

**Parameters:**
- `priority` - 명령의 우선 순위 값

**Throws:**
- `IllegalArgumentException` - `commandType`이 
유효하지 않은 유형인 경우

**See Also:**
- ``Command(String, String, int, int)``

### Command

```java
public Command(String shortLabel,
               String longLabel,
               int commandType,
               int priority)
```

- 지정된 
레이블, 
유형 및 
우선 순위를 사용하여 새 명령 객체를 만듭니다.

짧은 레이블은 필수이며 `null`이면 안 됩니다. 
긴 레이블은 선택 사항이며 
명령에 긴 레이블이 없는 경우 
`null`일 수 있습니다.

**Parameters:**
- `priority` - 명령의 우선 순위 값

**Throws:**
- `IllegalArgumentException` - `commandType`이 
유효하지 않은 유형인 경우

**Since:**
- MIDP 2.0

### getLabel

```java
public String getLabel()
```

**Returns:**
- `Command`의 짧은 레이블

### getLongLabel

```java
public String getLongLabel()
```

**Returns:**
- `Command`의 긴 레이블, 
또는 `Command`에 긴 레이블이 없는 경우 
`null`

**Since:**
- MIDP 2.0

### getCommandType

```java
public int getCommandType()
```

**Returns:**
- `Command`의 유형

### getPriority

```java
public int getPriority()
```

**Returns:**
- `Command`의 우선 순위

## 생성자 상세

### Command

```java
public Command(String label,
               int commandType,
               int priority)
```

- 지정된 짧은 

레이블, 
유형 및 
우선 순위를 사용하여 새 명령 객체를 만듭니다. 

새로 만든 명령에는 긴 레이블이 없습니다. 이 구성자는 `Command(label, null, commandType, priority)`와 
동일합니다.

**Parameters:**
- `priority` - 명령의 우선 순위 값

**Throws:**
- `IllegalArgumentException` - `commandType`이 
유효하지 않은 유형인 경우

**See Also:**
- ``Command(String, String, int, int)``

### Command

```java
public Command(String shortLabel,
               String longLabel,
               int commandType,
               int priority)
```

- 지정된 
레이블, 
유형 및 
우선 순위를 사용하여 새 명령 객체를 만듭니다.

짧은 레이블은 필수이며 `null`이면 안 됩니다. 
긴 레이블은 선택 사항이며 
명령에 긴 레이블이 없는 경우 
`null`일 수 있습니다.

**Parameters:**
- `priority` - 명령의 우선 순위 값

**Throws:**
- `IllegalArgumentException` - `commandType`이 
유효하지 않은 유형인 경우

**Since:**
- MIDP 2.0

### getLabel

```java
public String getLabel()
```

**Returns:**
- `Command`의 짧은 레이블

### getLongLabel

```java
public String getLongLabel()
```

**Returns:**
- `Command`의 긴 레이블, 
또는 `Command`에 긴 레이블이 없는 경우 
`null`

**Since:**
- MIDP 2.0

### getCommandType

```java
public int getCommandType()
```

**Returns:**
- `Command`의 유형

### getPriority

```java
public int getPriority()
```

**Returns:**
- `Command`의 우선 순위

## 메서드 상세

### getLabel

```java
public String getLabel()
```

**Returns:**
- `Command`의 짧은 레이블

### getLongLabel

```java
public String getLongLabel()
```

**Returns:**
- `Command`의 긴 레이블, 
또는 `Command`에 긴 레이블이 없는 경우 
`null`

**Since:**
- MIDP 2.0

### getCommandType

```java
public int getCommandType()
```

**Returns:**
- `Command`의 유형

### getPriority

```java
public int getPriority()
```

**Returns:**
- `Command`의 우선 순위
