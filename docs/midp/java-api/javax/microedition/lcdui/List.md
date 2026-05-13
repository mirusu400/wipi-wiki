# Class List

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Displayable
        |
        +--javax.microedition.lcdui.Screen
              |
              +--javax.microedition.lcdui.List
```

## 설명

**All Implemented Interfaces:**
- `Choice`

**implements Choice:**

선택 목록을 포함하는 `Screen`. 
대부분의 동작은 ``ChoiceGroup`` 클래스 및 
해당 공통 API와 유사합니다. 
특히 다른 `List` 유형은 ``Choice`` 
인터페이스에 정의되어 있습니다. 
디스플레이에 `List`가 있으면 사용자는 요소를 선택하고 
가능한 경우 여러 요소 간을 순회하고 스크롤하여 목록과 
상호 작용할 수 있습니다. 
순회 및 스크롤 작업은 응용 프로그램 가시적 이벤트를 발생하지 않습니다. 
시스템은 해당 ``CommandListener``에 알려 
``Command``가 호출될 때만 응용 프로그램에 알립니다. 
`List` 클래스는 
또한 장치의 기능에 따라 
특별히 호출될 수 있는 선택 명령도 지원합니다.

`List` 요소에 
대한 *선택* 작업의 
개념은 사용자와 `List`와의 상호 작용에 집중됩니다. 
지정된 하드웨어 "선택" 또는 "이동" 키가 있는 
장치에서는 해당 키를 사용하여 선택 작업을 구현합니다. 
지정된 키가 없는 장치에서는 
선택 작업을 수행할 수 있는 
다른 방법을 제공해야 합니다(예: 소프트 키 사용). 
유형이 다른 목록에서의 선택 작업 동작은 
다음 절에 설명되어 있습니다.

`List` 객체는 ``Choice.EXCLUSIVE``, 
``Choice.MULTIPLE`` 및 ``Choice.IMPLICIT``의 
`Choice` 유형으로 작성될 수 있습니다. 
``Choice.POPUP`` `Choice` 유형은 `List` 객체에서는 허용되지 않습니다.

### EXCLUSIVE 및 MULTIPLE 목록에서 선택

선택 작업은 `Command` 
객체와 연관되지 않으므로 
응용 프로그램에는 레이블을 설정하거나 작업 수행 시 알림을 
받을 방법이 없습니다. `EXCLUSIVE` 
유형의 `List`에서 선택 작업은 대상 요소를 
선택하고 이전에 선택한 요소를 선택 해제합니다. 
`MULTIPLE` 유형의 `List`에서 
선택 작업은 대상 요소의 선택된 상태를 전환하고 
다른 요소의 선택된 상태를 변경되지 않은 상태로 둡니다. 
소프트 키를 사용하여 선택 작업을 구현하는 장치는 
여기에 레이블을 제공해야 합니다. 
레이블은 `EXCLUSIVE` 유형 `List`의 
"선택" 및 `MULTIPLE`유형 
`List`의 "표시" 또는 
"표시 취소"와 유사한 부분이 있습니다.

### IMPLICIT 목록에서 선택

선택 작업은 *선택 명령*으로 불리는 
`Command` 객체와 연관되어 있습니다. 
사용자가 선택 작업을 수행할 때 시스템은 `List`의 
``CommandListener``에 알려 
선택 명령을 호출합니다. 
기본 선택 명령은 시스템이 제공한 
`SELECT_COMMAND` 명령입니다. 
응용 프로그램은 
``setSelectCommand`` 메소드를 
사용하여 선택 명령을 수정할 수 있습니다. 
소프트 키를 사용하여 선택 작업을 구현하는 장치는 선택 명령으로부터 
레이블을 사용합니다. 
선택 명령이 `SELECT_COMMAND`이면 
장치는 `SELECT_COMMAND` 레이블 속성을 사용하는 대신 
고유의 레이블을 제공하도록 선택할 수 있습니다. 
응용 프로그램은 일반적으로 `SELECT_COMMAND`를 교체할 
고유의 선택 명령을 제공해야 합니다. 이렇게 하면 응용 프로그램은 
`SELECT_COMMAND`에 시스템이 제공한 레이블에 의존하는 대신 
의미있는 레이블을 제공할 수 있습니다. 
구현 시 `List`에 요소가 없는 경우 `List`가 
비어 있으면 선택할 수 없기 때문에 선택 명령을 
호출해서는 *안 됩니다.* 
이런 경우 선택 명령이 
소프트 버튼이나 메뉴에 명시적으로 표시되면 구현 시 이를 제거하거나 
사용 불가능으로 해야 합니다. 
일반적으로 `List`가 비어 있을 때 
다른 명령은 호출할 수 있습니다.

### IMPLICIT 목록 사용

`IMPLICIT` `List`는 작업을 
`List` 요소로 제공하여 메뉴를 구성하는 데 
사용할 수 있습니다. 응용 프로그램은 `List` 요소를 
선택하는 데 사용되는 `Command`를 제공한 다음 
이 `Command`를 선택 명령으로 사용하도록 정의합니다. 
응용 프로그램은 또한 사용자가 
`Command`를 선택하거나 
활성화할 때 호출되는 `CommandListener`를 
등록해야 합니다.

String[] elements = { ... }; //Menu items as List elements
 List menuList = new List("Menu", List.IMPLICIT, elements, null);
 Command selectCommand = new Command("Open", Command.ITEM, 1);
 menuList.setSelectCommand(selectCommand);
 menuList.setCommandListener(...);

수신기는 `List`를 쿼리하여 
어떤 요소가 선택되었는지 확인한 다음 해당 작업을 수행합니다. 
명령을 선택 명령으로 설정하면 `List`가 
잘못 동작할 수도 있습니다.

선택 명령은 선택 키를 누를 때 수행되는 *기본 작업*으로 
간주되어야 합니다. 
예를 들어, 전자 메일 헤더를 표시하는 `List`에는 읽기, 
응답 및 삭제의 3가지 작업이 있을 수 있으며 읽기가 
기본 작업으로 간주됩니다.

List list = new List("Email", List.IMPLICIT, headers);
 readCommand = new Command("Read", Command.ITEM, 1);
 replyCommand = new Command("Reply", Command.ITEM, 2);
 deleteCommand = new Command("Delete", Command.ITEM, 3);
 list.setSelectCommand(readCommand);
 list.addCommand(replyCommand);
 list.addCommand(deleteCommand);
 list.setCommandListener(...);

지정된 선택 키가 있는 장치에서 이 키를 누르면 
`readCommand`가 호출됩니다. 
읽기 명령은 일반 `Command` 명령으로도 제공되기 때문에 
선택 키가 없는 장치에서도 사용자는 읽기 명령을 호출할 수 있습니다.

이러한 종류의 기본 작업은 주의해서 사용해야 하며 그 결과로 
만들어진 사용자 인터페이스의 유용성을 항상 염두에 두어야 합니다. 
기본 작업은 항상 특정 목록에서 
가장 직관적인 작업이어야 합니다.

**Since:**
- MIDP 1.0

## 필드 요약

- `static Command SELECT_COMMAND` — IMPLICIT List 의 기본 선택 명령.

## 생성자 요약

- List ( String title,
 int listType) 비어 있는 새 List 를 만들고 
목록의 제목과 
유형을 지정합니다.
- List ( String title,
 int listType, String [] stringElements, Image [] imageElements) 새 List 를 만들고 제목과 List 유형 
및 초기 내용으로 사용할 String 및 Image 의 배열을 지정합니다.

## 메서드 요약

- `int append ( String stringPart, Image imagePart)` — List 의 요소에 첨부합니다.
- `void delete (int elementNum)` — elementNum 에서 참조하는 요소를 삭제합니다.
- `void deleteAll ()` — 이 목록에서 모든 요소를 삭제합니다.
- `int getFitPolicy ()` — Choice 요소 내용을 사용 가능한 화면 크기에 맞추기 위한 응용 프로그램의 권장 정책을 가져옵니다.
- `Font getFont (int elementNum)` — 이 Choice 의 지정된 요소를 렌더링하기 위한 응용 프로그램의 기본 글꼴을 가져옵니다.
- `Image getImage (int elementNum)` — elementNum 에서 참조하는 요소의 Image 부분을 가져옵니다.
- `int getSelectedFlags (boolean[] selectedArray_return)` — List 의 상태를 쿼리하고 부울 배열 selectedArray_return 의 모든 요소 상태를 반환합니다.
- `int getSelectedIndex ()` — List 에서 선택된 요소의 색인 번호를 반환합니다.
- `String getString (int elementNum)` — elementNum 에서 참조하는 요소의 String 부분을 가져옵니다.
- `void insert (int elementNum, String stringPart, Image imagePart)` — 요소를 지정하기 전에 List 에 요소를 삽입합니다.
- `boolean isSelected (int elementNum)` — 이 요소의 선택 여부를 나타내는 부울 값을 가져옵니다.
- `void removeCommand ( Command cmd)` — 다음과 같은 의미가 추가되고 나머지는 `Displayable.removeCommand` 와 동일합니다.
- `void set (int elementNum, String stringPart, Image imagePart)` — 요소의 이전 내용을 바꿔 elementNum 에서 참조하는 요소의 String 및 Image 부분을 설정합니다.
- `void setFitPolicy (int fitPolicy)` — Choice 요소 내용을 사용 가능한 화면 크기에 맞추기 위한 응용 프로그램의 기본 정책을 설정합니다.
- `void setFont (int elementNum, Font font)` — 이 Choice 의 지정된 요소를 렌더링하기 위한 응용 프로그램의 기본 글꼴을 설정합니다.
- `void setSelectCommand ( Command command)` — IMPLICIT List 선택 작업에 사용할 Command 를 설정합니다.
- `void setSelectedFlags (boolean[] selectedArray)` — List 의 모든 요소의 선택된 상태를 설정합니다.
- `void setSelectedIndex (int elementNum, boolean selected)` — 요소의 선택된 상태를 설정합니다.
- `int size ()` — List 의 요소 수를 가져옵니다.

## 필드 상세

### SELECT_COMMAND

```java
public static final Command SELECT_COMMAND
```

- `IMPLICIT`
`List`의 기본 선택 명령. 
`IMPLICIT` `List`를 사용하는 
응용 프로그램은 ``setSelectCommand``를 
사용하여 고유의 선택 명령을 설정해야 합니다.

`SELECT_COMMAND`의 필드 값은 다음과 같습니다.
 
 - `label = ""` (an empty string)
 
 - `type = SCREEN`
 
 - `priority = 0`

(유형이 `ITEM`이면 더 적합하지만 
기록용으로 `SCREEN` 유형을 
그대로 사용합니다.)

응용 프로그램은 `SELECT_COMMAND`를 인식하기 위해 
이러한 값을 사용해서는 안 됩니다. 
대신 `Command` 및 
`Displayable`(`List`)의 객체 ID를 사용해야 합니다.

`SELECT_COMMAND`는 다른 `Displayable` 
유형과 함께 사용된 경우 일반 `Command`로 
처리됩니다.

### List

```java
public List(String title,
            int listType)
```

- 비어 있는 새 `List`를 만들고 
목록의 제목과 
유형을 지정합니다.

**Parameters:**
- `listType` - `IMPLICIT`, 
`EXCLUSIVE` 또는 `MULTIPLE` 중 하나

**Throws:**
- `IllegalArgumentException` - `listType`이 
`IMPLICIT`, `EXCLUSIVE` 또는 
`MULTIPLE` 중 하나가 아닌 경우

**See Also:**
- ``Choice``

### List

```java
public List(String title,
            int listType,
            String[] stringElements,
            Image[] imageElements)
```

- 새 `List`를 만들고 제목과 
`List`유형 
및 초기 내용으로 사용할 `String` 및 
`Image`의 배열을 지정합니다.

`stringElements` 배열은 null이 아니어야 하며 
모든 배열 요소도 null이 아니어야 합니다. 
`stringElements` 배열의 길이는 
`List`의 요소 수를 결정합니다. 
`imageElements` 배열은 
`List` 요소에 
이미지가 없음을 나타내기 위해 
`null`일 수 있습니다. 
`imageElements` 배열이 null이 아닌 경우 
`stringElements` 배열과 길이가 같아야 합니다. 
`imageElements` 배열의 개별 요소는 해당하는 
`List` 요소에 
이미지가 없음을 나타내기 위해 
`null`일 수 있습니다. 
`imageElements` 배열의 null이 아닌 요소는 
변경 가능하거나 변경 불가능한 이미지를 
나타낼 수 있습니다.

**Parameters:**
- `imageElements` - `List` 요소의 이미지 부분을 
지정하는 이미지 집합

**Throws:**
- `IllegalArgumentException` - `listType`이 
`IMPLICIT`, `EXCLUSIVE` 또는 
`MULTIPLE` 중 하나가 아닌 경우

**See Also:**
- ``Choice.EXCLUSIVE``, 
``Choice.MULTIPLE``, 
``Choice.IMPLICIT``

### size

```java
public int size()
```

**Specified by:**
- `size` in interface `Choice`

**Returns:**
- `List`의 요소 수

### getString

```java
public String getString(int elementNum)
```

**Specified by:**
- `getString` in interface `Choice`

**Parameters:**
- `elementNum` - 쿼리되는 요소 색인

**Returns:**
- 요소의 문자열 부분

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**See Also:**
- ``getImage(int)``

### getImage

```java
public Image getImage(int elementNum)
```

**Specified by:**
- `getImage` in interface `Choice`

**Parameters:**
- `elementNum` - 쿼리되는 요소 수

**Returns:**
- 요소의 이미지 부분 또는 이미지가 없는 경우 `null`

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 
유효하지 않은 경우

**See Also:**
- ``getString(int)``

### append

```java
public int append(String stringPart,
                  Image imagePart)
```

**Specified by:**
- `append` in interface `Choice`

**Parameters:**
- `imagePart` - 추가되는 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 `null`

**Returns:**
- 요소의 할당된 색인

**Throws:**
- `NullPointerException` - `stringPart`가 
`null`인 경우

### insert

```java
public void insert(int elementNum,
                   String stringPart,
                   Image imagePart)
```

**Specified by:**
- `insert` in interface `Choice`

**Parameters:**
- `imagePart` - 삽입되는 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 `null`

**Throws:**
- `NullPointerException` - `stringPart`가 
`null`인 경우

### delete

```java
public void delete(int elementNum)
```

**Specified by:**
- `delete` in interface `Choice`

**Parameters:**
- `elementNum` - 삭제되는 요소 색인

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

### deleteAll

```java
public void deleteAll()
```

**Specified by:**
- `deleteAll` in interface `Choice`

### set

```java
public void set(int elementNum,
                String stringPart,
                Image imagePart)
```

**Specified by:**
- `set` in interface `Choice`

**Parameters:**
- `imagePart` - 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 `null`

**Throws:**
- `NullPointerException` - `stringPart`가 
`null`인 경우

### isSelected

```java
public boolean isSelected(int elementNum)
```

**Specified by:**
- `isSelected` in interface `Choice`

**Parameters:**
- `elementNum` - 쿼리되는 요소의 색인

**Returns:**
- 요소의 선택 상태

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

### getSelectedIndex

```java
public int getSelectedIndex()
```

**Specified by:**
- `getSelectedIndex` in interface `Choice`

**Returns:**
- 선택한 요소의 색인 또는 색인이 없는 경우 `-1`

**See Also:**
- ``setSelectedIndex(int, boolean)``

### getSelectedFlags

```java
public int getSelectedFlags(boolean[] selectedArray_return)
```

**Specified by:**
- `getSelectedFlags` in interface `Choice`

**Parameters:**
- `selectedArray_return` - 결과를 포함할 배열

**Returns:**
- `Choice`에서 선택된 요소 수

**Throws:**
- `NullPointerException` - `selectedArray_return`이 
`null`인 경우

**See Also:**
- ``setSelectedFlags(boolean[])``

### setSelectedIndex

```java
public void setSelectedIndex(int elementNum,
                             boolean selected)
```

**Specified by:**
- `setSelectedIndex` in interface `Choice`

**Parameters:**
- `selected` - 요소 상태, 여기서 `true`는 선택된 상태를, 
`false`는 선택되지 않은 상태를 의미합니다.

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**See Also:**
- ``getSelectedIndex()``

### setSelectedFlags

```java
public void setSelectedFlags(boolean[] selectedArray)
```

**Specified by:**
- `setSelectedFlags` in interface `Choice`

**Parameters:**
- `selectedArray` - 메소드가 선택 상태를 
수집하는 배열

**Throws:**
- `NullPointerException` - `selectedArray`가 
`null`인 경우

**See Also:**
- ``getSelectedFlags(boolean[])``

### removeCommand

```java
public void removeCommand(Command cmd)
```

**Overrides:**
- `removeCommand` in class `Displayable`

**Parameters:**
- `cmd` - 제거되는 명령

**Since:**
- MIDP 2.0

### setSelectCommand

```java
public void setSelectCommand(Command command)
```

**Parameters:**
- `command` - `IMPLICIT` 목록 선택 작업에 
사용할 명령, 없는 경우에는 `null`

**Since:**
- MIDP 2.0

### setFitPolicy

```java
public void setFitPolicy(int fitPolicy)
```

**Specified by:**
- `setFitPolicy` in interface `Choice`

**Parameters:**
- `fitPolicy` - 선택 사항 요소의 기본 내용 맞춤 정책

**Throws:**
- `IllegalArgumentException` - `fitPolicy`가 유효하지 않은 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getFitPolicy()``

### getFitPolicy

```java
public int getFitPolicy()
```

**Specified by:**
- `getFitPolicy` in interface `Choice`

**Returns:**
- ``Choice.TEXT_WRAP_DEFAULT``, ``Choice.TEXT_WRAP_ON`` 또는 
``Choice.TEXT_WRAP_OFF`` 중의 하나

**Since:**
- MIDP 2.0

**See Also:**
- ``setFitPolicy(int)``

### setFont

```java
public void setFont(int elementNum,
                    Font font)
```

**Specified by:**
- `setFont` in interface `Choice`

**Parameters:**
- `font` - 요소 렌더링에 사용할 기본 글꼴

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getFont(int)``

### getFont

```java
public Font getFont(int elementNum)
```

**Specified by:**
- `getFont` in interface `Choice`

**Parameters:**
- `elementNum` - 0부터 시작하는 요소의 색인

**Returns:**
- 요소 렌더링에 사용할 기본 글꼴

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``setFont(int elementNum, Font font)``

## 생성자 상세

### List

```java
public List(String title,
            int listType)
```

- 비어 있는 새 `List`를 만들고 
목록의 제목과 
유형을 지정합니다.

**Parameters:**
- `listType` - `IMPLICIT`, 
`EXCLUSIVE` 또는 `MULTIPLE` 중 하나

**Throws:**
- `IllegalArgumentException` - `listType`이 
`IMPLICIT`, `EXCLUSIVE` 또는 
`MULTIPLE` 중 하나가 아닌 경우

**See Also:**
- ``Choice``

### List

```java
public List(String title,
            int listType,
            String[] stringElements,
            Image[] imageElements)
```

- 새 `List`를 만들고 제목과 
`List`유형 
및 초기 내용으로 사용할 `String` 및 
`Image`의 배열을 지정합니다.

`stringElements` 배열은 null이 아니어야 하며 
모든 배열 요소도 null이 아니어야 합니다. 
`stringElements` 배열의 길이는 
`List`의 요소 수를 결정합니다. 
`imageElements` 배열은 
`List` 요소에 
이미지가 없음을 나타내기 위해 
`null`일 수 있습니다. 
`imageElements` 배열이 null이 아닌 경우 
`stringElements` 배열과 길이가 같아야 합니다. 
`imageElements` 배열의 개별 요소는 해당하는 
`List` 요소에 
이미지가 없음을 나타내기 위해 
`null`일 수 있습니다. 
`imageElements` 배열의 null이 아닌 요소는 
변경 가능하거나 변경 불가능한 이미지를 
나타낼 수 있습니다.

**Parameters:**
- `imageElements` - `List` 요소의 이미지 부분을 
지정하는 이미지 집합

**Throws:**
- `IllegalArgumentException` - `listType`이 
`IMPLICIT`, `EXCLUSIVE` 또는 
`MULTIPLE` 중 하나가 아닌 경우

**See Also:**
- ``Choice.EXCLUSIVE``, 
``Choice.MULTIPLE``, 
``Choice.IMPLICIT``

### size

```java
public int size()
```

**Specified by:**
- `size` in interface `Choice`

**Returns:**
- `List`의 요소 수

### getString

```java
public String getString(int elementNum)
```

**Specified by:**
- `getString` in interface `Choice`

**Parameters:**
- `elementNum` - 쿼리되는 요소 색인

**Returns:**
- 요소의 문자열 부분

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**See Also:**
- ``getImage(int)``

### getImage

```java
public Image getImage(int elementNum)
```

**Specified by:**
- `getImage` in interface `Choice`

**Parameters:**
- `elementNum` - 쿼리되는 요소 수

**Returns:**
- 요소의 이미지 부분 또는 이미지가 없는 경우 `null`

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 
유효하지 않은 경우

**See Also:**
- ``getString(int)``

### append

```java
public int append(String stringPart,
                  Image imagePart)
```

**Specified by:**
- `append` in interface `Choice`

**Parameters:**
- `imagePart` - 추가되는 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 `null`

**Returns:**
- 요소의 할당된 색인

**Throws:**
- `NullPointerException` - `stringPart`가 
`null`인 경우

### insert

```java
public void insert(int elementNum,
                   String stringPart,
                   Image imagePart)
```

**Specified by:**
- `insert` in interface `Choice`

**Parameters:**
- `imagePart` - 삽입되는 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 `null`

**Throws:**
- `NullPointerException` - `stringPart`가 
`null`인 경우

### delete

```java
public void delete(int elementNum)
```

**Specified by:**
- `delete` in interface `Choice`

**Parameters:**
- `elementNum` - 삭제되는 요소 색인

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

### deleteAll

```java
public void deleteAll()
```

**Specified by:**
- `deleteAll` in interface `Choice`

### set

```java
public void set(int elementNum,
                String stringPart,
                Image imagePart)
```

**Specified by:**
- `set` in interface `Choice`

**Parameters:**
- `imagePart` - 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 `null`

**Throws:**
- `NullPointerException` - `stringPart`가 
`null`인 경우

### isSelected

```java
public boolean isSelected(int elementNum)
```

**Specified by:**
- `isSelected` in interface `Choice`

**Parameters:**
- `elementNum` - 쿼리되는 요소의 색인

**Returns:**
- 요소의 선택 상태

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

### getSelectedIndex

```java
public int getSelectedIndex()
```

**Specified by:**
- `getSelectedIndex` in interface `Choice`

**Returns:**
- 선택한 요소의 색인 또는 색인이 없는 경우 `-1`

**See Also:**
- ``setSelectedIndex(int, boolean)``

### getSelectedFlags

```java
public int getSelectedFlags(boolean[] selectedArray_return)
```

**Specified by:**
- `getSelectedFlags` in interface `Choice`

**Parameters:**
- `selectedArray_return` - 결과를 포함할 배열

**Returns:**
- `Choice`에서 선택된 요소 수

**Throws:**
- `NullPointerException` - `selectedArray_return`이 
`null`인 경우

**See Also:**
- ``setSelectedFlags(boolean[])``

### setSelectedIndex

```java
public void setSelectedIndex(int elementNum,
                             boolean selected)
```

**Specified by:**
- `setSelectedIndex` in interface `Choice`

**Parameters:**
- `selected` - 요소 상태, 여기서 `true`는 선택된 상태를, 
`false`는 선택되지 않은 상태를 의미합니다.

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**See Also:**
- ``getSelectedIndex()``

### setSelectedFlags

```java
public void setSelectedFlags(boolean[] selectedArray)
```

**Specified by:**
- `setSelectedFlags` in interface `Choice`

**Parameters:**
- `selectedArray` - 메소드가 선택 상태를 
수집하는 배열

**Throws:**
- `NullPointerException` - `selectedArray`가 
`null`인 경우

**See Also:**
- ``getSelectedFlags(boolean[])``

### removeCommand

```java
public void removeCommand(Command cmd)
```

**Overrides:**
- `removeCommand` in class `Displayable`

**Parameters:**
- `cmd` - 제거되는 명령

**Since:**
- MIDP 2.0

### setSelectCommand

```java
public void setSelectCommand(Command command)
```

**Parameters:**
- `command` - `IMPLICIT` 목록 선택 작업에 
사용할 명령, 없는 경우에는 `null`

**Since:**
- MIDP 2.0

### setFitPolicy

```java
public void setFitPolicy(int fitPolicy)
```

**Specified by:**
- `setFitPolicy` in interface `Choice`

**Parameters:**
- `fitPolicy` - 선택 사항 요소의 기본 내용 맞춤 정책

**Throws:**
- `IllegalArgumentException` - `fitPolicy`가 유효하지 않은 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getFitPolicy()``

### getFitPolicy

```java
public int getFitPolicy()
```

**Specified by:**
- `getFitPolicy` in interface `Choice`

**Returns:**
- ``Choice.TEXT_WRAP_DEFAULT``, ``Choice.TEXT_WRAP_ON`` 또는 
``Choice.TEXT_WRAP_OFF`` 중의 하나

**Since:**
- MIDP 2.0

**See Also:**
- ``setFitPolicy(int)``

### setFont

```java
public void setFont(int elementNum,
                    Font font)
```

**Specified by:**
- `setFont` in interface `Choice`

**Parameters:**
- `font` - 요소 렌더링에 사용할 기본 글꼴

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getFont(int)``

### getFont

```java
public Font getFont(int elementNum)
```

**Specified by:**
- `getFont` in interface `Choice`

**Parameters:**
- `elementNum` - 0부터 시작하는 요소의 색인

**Returns:**
- 요소 렌더링에 사용할 기본 글꼴

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``setFont(int elementNum, Font font)``

## 메서드 상세

### size

```java
public int size()
```

**Specified by:**
- `size` in interface `Choice`

**Returns:**
- `List`의 요소 수

### getString

```java
public String getString(int elementNum)
```

**Specified by:**
- `getString` in interface `Choice`

**Parameters:**
- `elementNum` - 쿼리되는 요소 색인

**Returns:**
- 요소의 문자열 부분

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**See Also:**
- ``getImage(int)``

### getImage

```java
public Image getImage(int elementNum)
```

**Specified by:**
- `getImage` in interface `Choice`

**Parameters:**
- `elementNum` - 쿼리되는 요소 수

**Returns:**
- 요소의 이미지 부분 또는 이미지가 없는 경우 `null`

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 
유효하지 않은 경우

**See Also:**
- ``getString(int)``

### append

```java
public int append(String stringPart,
                  Image imagePart)
```

**Specified by:**
- `append` in interface `Choice`

**Parameters:**
- `imagePart` - 추가되는 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 `null`

**Returns:**
- 요소의 할당된 색인

**Throws:**
- `NullPointerException` - `stringPart`가 
`null`인 경우

### insert

```java
public void insert(int elementNum,
                   String stringPart,
                   Image imagePart)
```

**Specified by:**
- `insert` in interface `Choice`

**Parameters:**
- `imagePart` - 삽입되는 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 `null`

**Throws:**
- `NullPointerException` - `stringPart`가 
`null`인 경우

### delete

```java
public void delete(int elementNum)
```

**Specified by:**
- `delete` in interface `Choice`

**Parameters:**
- `elementNum` - 삭제되는 요소 색인

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

### deleteAll

```java
public void deleteAll()
```

**Specified by:**
- `deleteAll` in interface `Choice`

### set

```java
public void set(int elementNum,
                String stringPart,
                Image imagePart)
```

**Specified by:**
- `set` in interface `Choice`

**Parameters:**
- `imagePart` - 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 `null`

**Throws:**
- `NullPointerException` - `stringPart`가 
`null`인 경우

### isSelected

```java
public boolean isSelected(int elementNum)
```

**Specified by:**
- `isSelected` in interface `Choice`

**Parameters:**
- `elementNum` - 쿼리되는 요소의 색인

**Returns:**
- 요소의 선택 상태

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

### getSelectedIndex

```java
public int getSelectedIndex()
```

**Specified by:**
- `getSelectedIndex` in interface `Choice`

**Returns:**
- 선택한 요소의 색인 또는 색인이 없는 경우 `-1`

**See Also:**
- ``setSelectedIndex(int, boolean)``

### getSelectedFlags

```java
public int getSelectedFlags(boolean[] selectedArray_return)
```

**Specified by:**
- `getSelectedFlags` in interface `Choice`

**Parameters:**
- `selectedArray_return` - 결과를 포함할 배열

**Returns:**
- `Choice`에서 선택된 요소 수

**Throws:**
- `NullPointerException` - `selectedArray_return`이 
`null`인 경우

**See Also:**
- ``setSelectedFlags(boolean[])``

### setSelectedIndex

```java
public void setSelectedIndex(int elementNum,
                             boolean selected)
```

**Specified by:**
- `setSelectedIndex` in interface `Choice`

**Parameters:**
- `selected` - 요소 상태, 여기서 `true`는 선택된 상태를, 
`false`는 선택되지 않은 상태를 의미합니다.

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**See Also:**
- ``getSelectedIndex()``

### setSelectedFlags

```java
public void setSelectedFlags(boolean[] selectedArray)
```

**Specified by:**
- `setSelectedFlags` in interface `Choice`

**Parameters:**
- `selectedArray` - 메소드가 선택 상태를 
수집하는 배열

**Throws:**
- `NullPointerException` - `selectedArray`가 
`null`인 경우

**See Also:**
- ``getSelectedFlags(boolean[])``

### removeCommand

```java
public void removeCommand(Command cmd)
```

**Overrides:**
- `removeCommand` in class `Displayable`

**Parameters:**
- `cmd` - 제거되는 명령

**Since:**
- MIDP 2.0

### setSelectCommand

```java
public void setSelectCommand(Command command)
```

**Parameters:**
- `command` - `IMPLICIT` 목록 선택 작업에 
사용할 명령, 없는 경우에는 `null`

**Since:**
- MIDP 2.0

### setFitPolicy

```java
public void setFitPolicy(int fitPolicy)
```

**Specified by:**
- `setFitPolicy` in interface `Choice`

**Parameters:**
- `fitPolicy` - 선택 사항 요소의 기본 내용 맞춤 정책

**Throws:**
- `IllegalArgumentException` - `fitPolicy`가 유효하지 않은 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getFitPolicy()``

### getFitPolicy

```java
public int getFitPolicy()
```

**Specified by:**
- `getFitPolicy` in interface `Choice`

**Returns:**
- ``Choice.TEXT_WRAP_DEFAULT``, ``Choice.TEXT_WRAP_ON`` 또는 
``Choice.TEXT_WRAP_OFF`` 중의 하나

**Since:**
- MIDP 2.0

**See Also:**
- ``setFitPolicy(int)``

### setFont

```java
public void setFont(int elementNum,
                    Font font)
```

**Specified by:**
- `setFont` in interface `Choice`

**Parameters:**
- `font` - 요소 렌더링에 사용할 기본 글꼴

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``getFont(int)``

### getFont

```java
public Font getFont(int elementNum)
```

**Specified by:**
- `getFont` in interface `Choice`

**Parameters:**
- `elementNum` - 0부터 시작하는 요소의 색인

**Returns:**
- 요소 렌더링에 사용할 기본 글꼴

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``setFont(int elementNum, Font font)``
