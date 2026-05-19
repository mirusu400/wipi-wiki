---
title: "Class TextBox"
---

`package javax.microedition.lcdui`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.Displayable
        |
        +--javax.microedition.lcdui.Screen
              |
              +--javax.microedition.lcdui.TextBox
```

## 설명

**extends Screen:**

`TextBox` 클래스는 
사용자가 텍스트를 입력하고 
편집할 수 있는 `Screen`입니다.

`TextBox`는 객체에 언제든지 저장할 수 있는 
문자의 최대 수(용량)를 나타내는 
최대 크기를 가집니다. 
이 제한은 `TextBox` 인스턴스가 구성될 때 
즉, 사용자가 `TextBox`에서 텍스트를 편집하고 
응용 프로그램이 내용을 수정하는 `TextBox`의 메소드를 
호출할 때 적용됩니다. 
최대 크기는 최대 저장 용량이며 
주어진 시간에 표시될 수 있는 문자 수와는 관계가 없습니다. 
문자 수가 표시되고 행과 열에 배열되는 방법은 
장치마다 다릅니다.

구현 시 최대 크기를 경계로 할 수 있으며 
실제로 지정되는 최대 크기는 응용 프로그램이 요청한 크기보다 
작을 수 있습니다. 
지정된 실제 값은 ``getMaxSize()``가 반환하는 값에 
반영됩니다. 방어적으로 작성된 응용 프로그램은 
이 값을 요청한 최대 크기와 비교하고 이 값이 서로 다를 경우를 처리할 수 있어야 합니다.

`TextBox`에 포함된 텍스트는 한 번에 표시하기에 
너무 많을 수도 있습니다. 이런 경우에는 구현 시 사용자 스크롤을 허용하여 
텍스트의 모든 부분을 보고 편집할 수 있도록 합니다. 
이 스크롤 작업은 응용 프로그램에 
투명하게 발생합니다.

제약 조건이 ``TextField.ANY``로 설정된 경우 텍스트는 
`줄 바꿈`을 포함할 수 있습니다. 
이에 따라 텍스트 표시가 줄 바꿈되고 사용자는 줄 바꿈 문자를 
입력할 수 있어야 합니다.

`TextBox`에는 
`TextField`와 동일한 
*입력 제약 조건* 개념이 있습니다. 
`TextBox` 클래스에서 메소드의 `constraints` 
매개 변수는 ``TextField`` 
클래스에 정의된 상수를 사용합니다. 
이러한 상수에 대한 정의는 `TextField` 클래스에서 
`입력 제약 조건`의 설명을 
참조하십시오. `TextBox`에는 *실제 내용*, 
*표시된 내용* 등 
`TextField`와 같은 개념이 
동일한 섹션에 설명되어 있습니다.

`TextBox`에는 또한 `TextField`와 
동일한 *입력 모드* 개념이 있습니다. 
자세한 내용은 `TextField` 클래스에 있는 
`입력 모드`의 
설명을 참조하십시오.

**Since:**
- MIDP 1.0

## 생성자 요약

- TextBox ( String title, String text,
 int maxSize,
 int constraints) 주어진 제목 문자열, 초기 내용, 최대 문자 수 및 제약 조건을 사용하여 
새 TextBox 객체를 만듭니다.

## 메서드 요약

- `void delete (int offset, int length)` — TextBox 에서 문자를 삭제합니다.
- `int getCaretPosition ()` — 현재 입력 위치를 가져옵니다.
- `int getChars (char[] data)` — TextBox 의 내용을 색인 0에서 시작하는 문자 배열로 복사합니다.
- `int getConstraints ()` — TextBox 의 현재 입력 제약 조건을 가져옵니다.
- `int getMaxSize ()` — TextBox 에 저장될 수 있는 최대 크기(문자 수)를 반환합니다.
- `String getString ()` — 문자열 값으로 TextBox 의 내용을 가져옵니다.
- `void insert (char[] data, int offset, int length, int position)` — 문자 배열의 하위 범위를 TextBox 의 내용에 삽입합니다.
- `void insert ( String src, int position)` — 문자열을 TextBox 의 내용에 삽입합니다.
- `void setChars (char[] data, int offset, int length)` — 문자 배열로부터 TextBox 의 내용을 설정하여 이전 내용을 교체합니다.
- `void setConstraints (int constraints)` — TextBox 의 입력 제약 조건을 설정합니다.
- `void setInitialInputMode ( String characterSubset)` — 사용자가 이 TextBox 의 편집을 시작할 때 사용되어야 할 입력 모드에 대한 힌트를 설정합니다.
- `int setMaxSize (int maxSize)` — TextBox 내에 포함될 수 있는 최대 크기(문자 수)를 설정합니다.
- `void setString ( String text)` — 문자열 값으로 TextBox 의 내용을 설정하여 이전 내용을 대체합니다.
- `int size ()` — 현재 TextBox 내에 저장된 문자 수를 가져옵니다.

## 생성자 상세

### TextBox

```java
public TextBox(String title,
               String text,
               int maxSize,
               int constraints)
```

- 주어진 제목 문자열, 초기 내용, 최대 문자 수 및 제약 조건을 사용하여 
새 `TextBox` 객체를 만듭니다. 
텍스트 매개 변수가 `null`이면 `TextBox`는 
공백으로 작성됩니다. `maxSize` 
매개 변수는 0보다 커야 합니다. 
초기 내용 문자열의 길이가 `maxSize`를 
초과하면 `IllegalArgumentException`이 발생합니다. 
하지만 구현 시 응용 프로그램이 요청한 것보다 
작은 최대 크기를 할당할 수 있습니다. 
이런 경우 내용의 길이가 
새로 할당된 최대 크기를 초과하면 
여기에 맞추기 위해 내용의 끝부분이 잘리고 
예외가 발생하지 않습니다.

**Parameters:**
- `constraints` - `입력 
제약 조건`을 참조하십시오.

**Throws:**
- `IllegalArgumentException` - 문자열의 길이가 요청된 
최대 용량을 초과할 경우

### getString

```java
public String getString()
```

**Returns:**
- 현재 내용

**See Also:**
- ``setString(java.lang.String)``

### setString

```java
public void setString(String text)
```

**Parameters:**
- `text` - `TextBox`의 새 값 또는 
`TextBox`가 비어 있는 경우 
`null`

**Throws:**
- `IllegalArgumentException` - 텍스트가 현재 
최대 용량을 초과하는 경우

**See Also:**
- ``getString()``

### getChars

```java
public int getChars(char[] data)
```

**Parameters:**
- `data` - 값을 받을 문자 배열

**Returns:**
- 복사된 문자 수

**Throws:**
- `NullPointerException` - `data`가 `null`인 경우

**See Also:**
- ``setChars(char[], int, int)``

### setChars

```java
public void setChars(char[] data,
                     int offset,
                     int length)
```

**Parameters:**
- `length` - 복사할 문자 수

**Throws:**
- `IllegalArgumentException` - 텍스트가 현재 
최대 용량을 초과하는 경우

**See Also:**
- ``getChars(char[])``

### insert

```java
public void insert(String src,
                   int position)
```

**Parameters:**
- `position` - 삽입이 발생하는 위치

**Throws:**
- `NullPointerException` - `src`가 `null`인 경우

### insert

```java
public void insert(char[] data,
                   int offset,
                   int length,
                   int position)
```

**Parameters:**
- `position` - 삽입이 발생하는 위치

**Throws:**
- `NullPointerException` - `data`가 `null`인 경우

### delete

```java
public void delete(int offset,
                   int length)
```

**Parameters:**
- `length` - 삭제되는 문자 수

**Throws:**
- `StringIndexOutOfBoundsException` - `offset`과 
`length`가 `TextBox` 내용 내의 
유효한 범위를 지정하지 않는 경우

### getMaxSize

```java
public int getMaxSize()
```

**Returns:**
- 최대 문자 크기

**See Also:**
- ``setMaxSize(int)``

### setMaxSize

```java
public int setMaxSize(int maxSize)
```

**Parameters:**
- `maxSize` - 새 최대 크기

**Returns:**
- 할당된 최대 용량(요청된 것보다 작을 수 있음)

**Throws:**
- `IllegalArgumentException` - 잘려진 후 
내용이 현재의 `입력 제약 조건`에 
유효하지 않은 경우

**See Also:**
- ``getMaxSize()``

### size

```java
public int size()
```

**Returns:**
- 문자 수

### getCaretPosition

```java
public int getCaretPosition()
```

**Returns:**
- 현재 캐럿 위치. 시작 부분이면 `0`

### setConstraints

```java
public void setConstraints(int constraints)
```

**Parameters:**
- `constraints` - `입력 제약 조건`을 
참조하십시오.

**Throws:**
- `IllegalArgumentException` - 제약 조건 매개 변수의 값이 
유효하지 않을 경우

**See Also:**
- ``getConstraints()``

### getConstraints

```java
public int getConstraints()
```

**Returns:**
- 현재 제약 조건 값(`입력 
제약 조건` 참조)

**See Also:**
- ``setConstraints(int)``

### setInitialInputMode

```java
public void setInitialInputMode(String characterSubset)
```

**Parameters:**
- `characterSubset` - 유니코드 문자 하위 집합의 이름인 
문자열 또는 `null`

**Since:**
- MIDP 2.0

## 메서드 상세

### getString

```java
public String getString()
```

**Returns:**
- 현재 내용

**See Also:**
- ``setString(java.lang.String)``

### setString

```java
public void setString(String text)
```

**Parameters:**
- `text` - `TextBox`의 새 값 또는 
`TextBox`가 비어 있는 경우 
`null`

**Throws:**
- `IllegalArgumentException` - 텍스트가 현재 
최대 용량을 초과하는 경우

**See Also:**
- ``getString()``

### getChars

```java
public int getChars(char[] data)
```

**Parameters:**
- `data` - 값을 받을 문자 배열

**Returns:**
- 복사된 문자 수

**Throws:**
- `NullPointerException` - `data`가 `null`인 경우

**See Also:**
- ``setChars(char[], int, int)``

### setChars

```java
public void setChars(char[] data,
                     int offset,
                     int length)
```

**Parameters:**
- `length` - 복사할 문자 수

**Throws:**
- `IllegalArgumentException` - 텍스트가 현재 
최대 용량을 초과하는 경우

**See Also:**
- ``getChars(char[])``

### insert

```java
public void insert(String src,
                   int position)
```

**Parameters:**
- `position` - 삽입이 발생하는 위치

**Throws:**
- `NullPointerException` - `src`가 `null`인 경우

### insert

```java
public void insert(char[] data,
                   int offset,
                   int length,
                   int position)
```

**Parameters:**
- `position` - 삽입이 발생하는 위치

**Throws:**
- `NullPointerException` - `data`가 `null`인 경우

### delete

```java
public void delete(int offset,
                   int length)
```

**Parameters:**
- `length` - 삭제되는 문자 수

**Throws:**
- `StringIndexOutOfBoundsException` - `offset`과 
`length`가 `TextBox` 내용 내의 
유효한 범위를 지정하지 않는 경우

### getMaxSize

```java
public int getMaxSize()
```

**Returns:**
- 최대 문자 크기

**See Also:**
- ``setMaxSize(int)``

### setMaxSize

```java
public int setMaxSize(int maxSize)
```

**Parameters:**
- `maxSize` - 새 최대 크기

**Returns:**
- 할당된 최대 용량(요청된 것보다 작을 수 있음)

**Throws:**
- `IllegalArgumentException` - 잘려진 후 
내용이 현재의 `입력 제약 조건`에 
유효하지 않은 경우

**See Also:**
- ``getMaxSize()``

### size

```java
public int size()
```

**Returns:**
- 문자 수

### getCaretPosition

```java
public int getCaretPosition()
```

**Returns:**
- 현재 캐럿 위치. 시작 부분이면 `0`

### setConstraints

```java
public void setConstraints(int constraints)
```

**Parameters:**
- `constraints` - `입력 제약 조건`을 
참조하십시오.

**Throws:**
- `IllegalArgumentException` - 제약 조건 매개 변수의 값이 
유효하지 않을 경우

**See Also:**
- ``getConstraints()``

### getConstraints

```java
public int getConstraints()
```

**Returns:**
- 현재 제약 조건 값(`입력 
제약 조건` 참조)

**See Also:**
- ``setConstraints(int)``

### setInitialInputMode

```java
public void setInitialInputMode(String characterSubset)
```

**Parameters:**
- `characterSubset` - 유니코드 문자 하위 집합의 이름인 
문자열 또는 `null`

**Since:**
- MIDP 2.0
