# Interface Choice

`package javax.microedition.lcdui`

```text
    ch.set(k, ch.getString(k), ch.getImage(k));
```

## 필드 요약

- `static int EXCLUSIVE` — EXCLUSIVE 는 한 번에 정확히 한 요소만 선택하는 선택 방법입니다.
- `static int IMPLICIT` — IMPLICIT 는 `Command` 가 시작될 때 현재 포커스된 요소를 선택하는 선택 방법입니다.
- `static int MULTIPLE` — MULTIPLE 은 한 번에 여러 요소를 선택할 수 있는 선택 방법입니다.
- `static int POPUP` — POPUP 은 한 번에 정확히 한 요소만 선택하는 선택 방법입니다.
- `static int TEXT_WRAP_DEFAULT` — 응용 프로그램에 텍스트 요소 내용의 줄바꿈이나 자르기에 관한 기본 설정이 없으며 구현 시 기본 동작을 사용해야 함을 나타내는 상수입니다.
- `static int TEXT_WRAP_OFF` — 텍스트 요소 내용이 한 줄로 제한되어야 함을 알리는 상수입니다.
- `static int TEXT_WRAP_ON` — 사용 가능한 내용 공간에 맞추기 위해 필요한 경우 텍스트 요소 내용이 여러 줄에 줄바꿈되어야 함을 알리는 상수입니다.

## 메서드 요약

- `int append ( String stringPart, Image imagePart)` — 요소를 Choice 에 추가합니다.
- `void delete (int elementNum)` — elementNum 에서 참조하는 요소를 삭제합니다.
- `void deleteAll ()` — Choice 에서 요소를 남기지 않고 모든 요소를 삭제합니다.
- `int getFitPolicy ()` — Choice 요소 내용을 사용 가능한 화면 크기에 맞추기 위한 응용 프로그램의 권장 정책을 가져옵니다.
- `Font getFont (int elementNum)` — 이 Choice 의 지정된 요소를 렌더링하기 위한 응용 프로그램의 기본 글꼴을 가져옵니다.
- `Image getImage (int elementNum)` — elementNum 에서 참조하는 요소의 Image 부분을 가져옵니다.
- `int getSelectedFlags (boolean[] selectedArray_return)` — Choice 의 상태를 쿼리하여 부울 배열 selectedArray_return 에 있는 모든 요소의 상태를 반환합니다.
- `int getSelectedIndex ()` — 선택된 Choice 요소의 색인 번호를 반환합니다.
- `String getString (int elementNum)` — elementNum 에서 참조하는 요소의 String 부분을 가져옵니다.
- `void insert (int elementNum, String stringPart, Image imagePart)` — Choice 에서 지정한 요소 바로 앞에 요소를 삽입합니다.
- `boolean isSelected (int elementNum)` — 이 요소의 선택 여부를 나타내는 부울 값을 가져옵니다.
- `void set (int elementNum, String stringPart, Image imagePart)` — 요소의 이전 내용을 바꿔 elementNum 에서 참조하는 요소의 String 및 Image 부분을 설정합니다.
- `void setFitPolicy (int fitPolicy)` — Choice 요소 내용을 사용 가능한 화면 크기에 맞추기 위한 응용 프로그램의 기본 정책을 설정합니다.
- `void setFont (int elementNum, Font font)` — 이 Choice 의 지정된 요소를 렌더링하기 위한 응용 프로그램의 기본 글꼴을 설정합니다.
- `void setSelectedFlags (boolean[] selectedArray)` — Choice 의 모든 요소를 선택된 상태로 설정하려고 합니다.
- `void setSelectedIndex (int elementNum, boolean selected)` — MULTIPLE 의 경우 단순히 개별 요소의 선택된 상태를 설정합니다.
- `int size ()` — 현재 있는 요소의 수를 가져옵니다.

## 필드 상세

### EXCLUSIVE

```java
public static final int EXCLUSIVE
```

**See Also:**
- `Constant Field Values`

### MULTIPLE

```java
public static final int MULTIPLE
```

**See Also:**
- `Constant Field Values`

### IMPLICIT

```java
public static final int IMPLICIT
```

**See Also:**
- `Constant Field Values`

### POPUP

```java
public static final int POPUP
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### TEXT_WRAP_DEFAULT

```java
public static final int TEXT_WRAP_DEFAULT
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getFitPolicy()``, 
``setFitPolicy(int)``, 
`Constant Field Values`

### TEXT_WRAP_ON

```java
public static final int TEXT_WRAP_ON
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getFitPolicy()``, 
``setFitPolicy(int)``, 
`Constant Field Values`

### TEXT_WRAP_OFF

```java
public static final int TEXT_WRAP_OFF
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getFitPolicy()``, 
``setFitPolicy(int)``, 
`Constant Field Values`

### size

```java
public int size()
```

**Returns:**
- `Choice`에 있는 요소의 수

### getString

```java
public String getString(int elementNum)
```

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

**Parameters:**
- `elementNum` - 쿼리되는 요소 색인

**Returns:**
- 요소의 이미지 부분, 
또는 이미지가 없는 경우 `null`

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**See Also:**
- ``getString(int)``

### append

```java
public int append(String stringPart,
                  Image imagePart)
```

**Parameters:**
- `imagePart` - 추가되는 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 
`null`

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

**Parameters:**
- `elementNum` - 삭제되는 요소 색인

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

### deleteAll

```java
public void deleteAll()
```

**Since:**
- MIDP 2.0

### set

```java
public void set(int elementNum,
                String stringPart,
                Image imagePart)
```

**Parameters:**
- `imagePart` - 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 
`null`

**Throws:**
- `NullPointerException` - `stringPart`가 
`null`인 경우

### isSelected

```java
public boolean isSelected(int elementNum)
```

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

**Returns:**
- 선택한 요소의 색인 또는 색인이 없는 경우 `-1`

**See Also:**
- ``setSelectedIndex(int, boolean)``

### getSelectedFlags

```java
public int getSelectedFlags(boolean[] selectedArray_return)
```

**Parameters:**
- `selectedArray_return` - 결과를 포함할 배열

**Returns:**
- `Choice`에 선택된 요소의 수

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

**Parameters:**
- `selected` - 요소의 상태이며 `true`는 선택했음을, 
`false`는 선택하지 않았음을 의미합니다.

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**See Also:**
- ``getSelectedIndex()``

### setSelectedFlags

```java
public void setSelectedFlags(boolean[] selectedArray)
```

**Parameters:**
- `selectedArray` - 메소드가 
선택 상태를 수집하는 배열

**Throws:**
- `NullPointerException` - `selectedArray`가 
`null`인 경우

**See Also:**
- ``getSelectedFlags(boolean[])``

### setFitPolicy

```java
public void setFitPolicy(int fitPolicy)
```

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

**Returns:**
- ``TEXT_WRAP_DEFAULT``, 
``TEXT_WRAP_ON`` 또는 ``TEXT_WRAP_OFF`` 중의 하나

**Since:**
- MIDP 2.0

**See Also:**
- ``setFitPolicy(int)``

### setFont

```java
public void setFont(int elementNum,
                    Font font)
```

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

**Parameters:**
- `elementNum` - 0부터 시작하는 요소의 색인

**Returns:**
- 요소 렌더링에 사용할 기본 글꼴

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``setFont(int, javax.microedition.lcdui.Font)``

## 메서드 상세

### size

```java
public int size()
```

**Returns:**
- `Choice`에 있는 요소의 수

### getString

```java
public String getString(int elementNum)
```

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

**Parameters:**
- `elementNum` - 쿼리되는 요소 색인

**Returns:**
- 요소의 이미지 부분, 
또는 이미지가 없는 경우 `null`

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**See Also:**
- ``getString(int)``

### append

```java
public int append(String stringPart,
                  Image imagePart)
```

**Parameters:**
- `imagePart` - 추가되는 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 
`null`

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

**Parameters:**
- `elementNum` - 삭제되는 요소 색인

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

### deleteAll

```java
public void deleteAll()
```

**Since:**
- MIDP 2.0

### set

```java
public void set(int elementNum,
                String stringPart,
                Image imagePart)
```

**Parameters:**
- `imagePart` - 요소의 이미지 부분 또는 
이미지 부분이 없는 경우 
`null`

**Throws:**
- `NullPointerException` - `stringPart`가 
`null`인 경우

### isSelected

```java
public boolean isSelected(int elementNum)
```

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

**Returns:**
- 선택한 요소의 색인 또는 색인이 없는 경우 `-1`

**See Also:**
- ``setSelectedIndex(int, boolean)``

### getSelectedFlags

```java
public int getSelectedFlags(boolean[] selectedArray_return)
```

**Parameters:**
- `selectedArray_return` - 결과를 포함할 배열

**Returns:**
- `Choice`에 선택된 요소의 수

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

**Parameters:**
- `selected` - 요소의 상태이며 `true`는 선택했음을, 
`false`는 선택하지 않았음을 의미합니다.

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**See Also:**
- ``getSelectedIndex()``

### setSelectedFlags

```java
public void setSelectedFlags(boolean[] selectedArray)
```

**Parameters:**
- `selectedArray` - 메소드가 
선택 상태를 수집하는 배열

**Throws:**
- `NullPointerException` - `selectedArray`가 
`null`인 경우

**See Also:**
- ``getSelectedFlags(boolean[])``

### setFitPolicy

```java
public void setFitPolicy(int fitPolicy)
```

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

**Returns:**
- ``TEXT_WRAP_DEFAULT``, 
``TEXT_WRAP_ON`` 또는 ``TEXT_WRAP_OFF`` 중의 하나

**Since:**
- MIDP 2.0

**See Also:**
- ``setFitPolicy(int)``

### setFont

```java
public void setFont(int elementNum,
                    Font font)
```

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

**Parameters:**
- `elementNum` - 0부터 시작하는 요소의 색인

**Returns:**
- 요소 렌더링에 사용할 기본 글꼴

**Throws:**
- `IndexOutOfBoundsException` - `elementNum`이 유효하지 않은 경우

**Since:**
- MIDP 2.0

**See Also:**
- ``setFont(int, javax.microedition.lcdui.Font)``
