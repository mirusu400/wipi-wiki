# Class ChoiceGroup

`package javax.microedition.lcdui`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.Item
        |
        +--javax.microedition.lcdui.ChoiceGroup
```

## 설명

**All Implemented Interfaces:**
- `Choice`

**implements Choice:**

`ChoiceGroup`은 ``Form`` 내에 
놓을 선택 가능한 요소 그룹입니다. 
이 그룹은 단일 선택을 만들 필요가 있거나 
다중 선택이 가능한 모드에서 만들어질 수 있습니다. 
구현 시에는 이러한 모드의 그래픽 표현을 제공해야 하며 
여러 모드에 대한 여러 그래픽을 시각적으로 제공해야 합니다. 
예를 들어, 단일 선택 모드에 대해서는 "라디오 버튼"을, 
다중 선택 모드에 대해서는 "확인란"을 
사용할 수 있습니다.

**주:** 대부분의 필수 메소드는 
``Choice`` 인터페이스에 지정되어 있습니다.

**Since:**
- MIDP 1.0

## 필드 요약

## 생성자 요약

- ChoiceGroup ( String label,
 int choiceType) 새로운 빈 ChoiceGroup 을 만들고 제목과 유형을 지정합니다.
- ChoiceGroup ( String label,
 int choiceType, String [] stringElements, Image [] imageElements) 새 ChoiceGroup 을 만들어 제목, ChoiceGroup 의 유형 및 
초기 내용으로 사용될 Strings 와 Images 의 
배열을 지정합니다.

## 메서드 요약

- `int append ( String stringPart, Image imagePart)` — 요소를 ChoiceGroup 에 추가합니다.
- `void delete (int elementNum)` — elementNum 에서 참조하는 요소를 삭제합니다.
- `void deleteAll ()` — 이 ChoiceGroup 에서 요소를 모두 삭제합니다.
- `int getFitPolicy ()` — Choice 요소 내용을 사용 가능한 화면 크기에 맞추기 위한 응용 프로그램의 권장 정책을 가져옵니다.
- `Font getFont (int elementNum)` — 이 Choice 의 지정된 요소를 렌더링하기 위한 응용 프로그램의 기본 글꼴을 가져옵니다.
- `Image getImage (int elementNum)` — elementNum 에서 참조하는 요소의 Image 부분을 가져옵니다.
- `int getSelectedFlags (boolean[] selectedArray_return)` — ChoiceGroup 의 상태를 쿼리하여 부울 배열 selectedArray_return 에 있는 모든 요소의 상태를 반환합니다.
- `int getSelectedIndex ()` — 선택된 ChoiceGroup 에서 요소의 색인 번호를 반환합니다.
- `String getString (int elementNum)` — elementNum 에서 참조하는 요소의 String 부분을 가져옵니다.
- `void insert (int elementNum, String stringPart, Image imagePart)` — ChoiceGroup 에 지정된 요소 바로 앞에 요소를 삽입합니다.
- `boolean isSelected (int elementNum)` — 이 요소의 선택 여부를 나타내는 부울 값을 가져옵니다.
- `void set (int elementNum, String stringPart, Image imagePart)` — 요소의 이전 내용을 바꿔 elementNum 에서 참조하는 요소의 String 및 Image 부분을 설정합니다.
- `void setFitPolicy (int fitPolicy)` — Choice 요소 내용을 사용 가능한 화면 크기에 맞추기 위한 응용 프로그램의 기본 정책을 설정합니다.
- `void setFont (int elementNum, Font font)` — 이 Choice 의 지정된 요소를 렌더링하기 위한 응용 프로그램의 기본 글꼴을 설정합니다.
- `void setSelectedFlags (boolean[] selectedArray)` — ChoiceGroup 의 모든 요소를 선택된 상태로 설정하려고 합니다.
- `void setSelectedIndex (int elementNum, boolean selected)` — MULTIPLE 유형의 ChoiceGroup 객체의 경우 단순히 개별 요소의 선택된 상태를 설정합니다.
- `int size ()` — ChoiceGroup 에 있는 요소의 수를 반환합니다.

## 생성자 상세

### ChoiceGroup

```java
public ChoiceGroup(String label,
                   int choiceType)
```

- 새로운 빈 `ChoiceGroup`을 만들고 제목과 유형을 지정합니다. 
유형은 `EXCLUSIVE`, `MULTIPLE`, 
`POPUP` 중 하나여야 합니다. 
`IMPLICIT` 선택 유형은 
`ChoiceGroup` 내에서는 
허용되지 않습니다.

**Parameters:**
- `choiceType` - `EXCLUSIVE`, `MULTIPLE` 
또는 `POPUP`

**Throws:**
- `IllegalArgumentException` - `choiceType`이 
`EXCLUSIVE`, `MULTIPLE`, `POPUP` 중 하나가 아닌 경우

**See Also:**
- ``Choice.EXCLUSIVE``, 
``Choice.MULTIPLE``, 
``Choice.IMPLICIT``, 
``Choice.POPUP``

### ChoiceGroup

```java
public ChoiceGroup(String label,
                   int choiceType,
                   String[] stringElements,
                   Image[] imageElements)
```

- 새 `ChoiceGroup`을 만들어 제목, 
`ChoiceGroup`의 유형 및 
초기 내용으로 사용될 
`Strings`와 `Images`의 
배열을 지정합니다.

유형은 `EXCLUSIVE`, `MULTIPLE`, 
`POPUP` 중 하나여야 합니다. 
`IMPLICIT` 유형은 `ChoiceGroup`에는 
허용되지 않습니다.

`stringElements` 배열은 
null이 아니어야 하며 모든 배열 요소도 null이 아니어야 합니다. 
`stringElements` 배열의 
길이는 `ChoiceGroup`에 
있는 요소 수를 결정합니다. 
`imageElements` 배열은 
`ChoiceGroup` 
요소에 이미지가 없음을 나타내기 위해 
`null`일 수 있습니다. 
`imageElements` 배열이 null이 아닌 경우 
`stringElements` 배열과 
길이가 같아야 합니다. 
`imageElements` 배열의 개별 요소는 
해당 `ChoiceGroup` 요소의 
이미지가 없음을 나타내기 위해 
`null`일 수 있습니다. `imageElements` 
배열의 null이 아닌 요소는 변경 가능하거나 
변경 불가능한 이미지를 
참조할 수 있습니다.

**Parameters:**
- `imageElements` - `ChoiceGroup` 요소의 이미지 부분을 
지정하는 이미지 집합

**Throws:**
- `IllegalArgumentException` - `choiceType`이 
`EXCLUSIVE`, `MULTIPLE`, `POPUP` 중 하나가 아닌 경우

**See Also:**
- ``Choice.EXCLUSIVE``, 
``Choice.MULTIPLE``, 
``Choice.IMPLICIT``, 
``Choice.POPUP``

### size

```java
public int size()
```

**Specified by:**
- `size` in interface `Choice`

**Returns:**
- `ChoiceGroup`에 있는 요소의 수

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
- `elementNum` - 쿼리되는 요소의 수

**Returns:**
- 요소의 이미지 부분, 또는 이미지가 없는 경우 null

**Throws:**
- `IndexOutOfBoundsException` - elementNum이 유효하지 않은 경우

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
- `elementNum` - 쿼리되는 요소 색인

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
- `ChoiceGroup`에 선택된 요소의 수

**Throws:**
- `NullPointerException` - `selectedArray_return`이 
null인 경우

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
- `selected` - 요소의 새 상태, `true=selected`, 
`false=not` selected

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
- ``Choice.TEXT_WRAP_DEFAULT``, ``Choice.TEXT_WRAP_ON`` 
또는 ``Choice.TEXT_WRAP_OFF`` 중의 하나

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
- `ChoiceGroup`에 있는 요소의 수

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
- `elementNum` - 쿼리되는 요소의 수

**Returns:**
- 요소의 이미지 부분, 또는 이미지가 없는 경우 null

**Throws:**
- `IndexOutOfBoundsException` - elementNum이 유효하지 않은 경우

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
- `elementNum` - 쿼리되는 요소 색인

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
- `ChoiceGroup`에 선택된 요소의 수

**Throws:**
- `NullPointerException` - `selectedArray_return`이 
null인 경우

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
- `selected` - 요소의 새 상태, `true=selected`, 
`false=not` selected

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
- ``Choice.TEXT_WRAP_DEFAULT``, ``Choice.TEXT_WRAP_ON`` 
또는 ``Choice.TEXT_WRAP_OFF`` 중의 하나

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
