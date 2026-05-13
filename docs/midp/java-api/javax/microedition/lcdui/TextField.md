# Class TextField

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Item
        |
        +--javax.microedition.lcdui.TextField
```

## 설명

**extends Item:**

`TextField`는 ``Form``에 
들어갈 수 있는 편집할 수 있는 
텍스트 구성 요소입니다. 
초기 값으로 사용되는 텍스트가 제공될 수 있습니다.

`TextField`는 객체에 언제든지 
저장할 수 있는 문자의 최대 수(용량)를 
나타내는 최대 크기를 가집니다. 
이 제한은 `TextField` 인스턴스가 구성될 때 
즉, 사용자가 `TextField`에서 텍스트를 편집하고 
응용 프로그램이 내용을 수정하는 
`TextField`의 메소드를 
호출할 때 적용됩니다. 최대 크기는 
최대 저장 용량이며 주어진 시간에 표시될 수 있는 
문자 수와는 관계가 없습니다. 문자 수가 표시되고 
행과 열에 배열되는 방법은 장치마다 다릅니다.

구현 시 최대 크기를 경계로 할 수 있으며 
실제로 지정되는 최대 크기는 응용 프로그램이 
요청한 크기보다 작을 수 있습니다. 
지정된 실제 값은 ``getMaxSize()``가 
반환하는 값에 반영됩니다. 방어적으로 작성된 응용 프로그램은 
이 값을 요청한 최대 크기와 비교하고 이 값이 서로 다를 경우를 처리할 수 있어야 합니다.

### 입력 제약 조건

`TextField`는 ``TextBox`` 클래스와 
*입력 제약 조건* 개념을 공유합니다. 
제약 조건이 서로 다르면 응용 프로그램은 사용자 입력을 
여러 방법으로 제한하도록 요청할 수 있습니다. 
구현 시에는 응용 프로그램이 요청한 대로 사용자 입력을 제한해야 합니다. 
예를 들어, 응용 프로그램이 `TextField`에 
`NUMERIC` 제약 조건을 요청하면 숫자만 입력할 수 있도록 
구현해야 합니다.

텍스트 객체의 *실제 내용*은 
`TextBox` 및 `TextField` API를 
사용하여 설정 및 수정되고 
응용 프로그램에 보고됩니다. 
구현 시 텍스트 객체의 제약 조건 설정에 적합한 특수 포맷을 
제공하는 경우에는 *표시된 내용*이 
실제 내용과 다를 수 있습니다. 
예를 들어, `PHONENUMBER` 필드는 숫자 
구분자 및 구두점을 사용해서 숫자를 국가 코드, 지역 코드, 
접미어 등으로 묶어 사용 중인 전화 번호 규칙에 적합하게 표시할 수 있습니다. 
제공되는 모든 공백이나 구두점은 텍스트 객체의 실제 내용으로 
간주되지 않습니다. 
예를 들어, `PHONENUMBER` 제약 조건을 
가진 텍스트 객체는 다음과 같이 표시될 수 있습니다.

(408) 555-1212

하지만 API를 통해 응용 프로그램에 제공되는 객체의 
실제 내용은 "`4085551212`" 문자열입니다. 
`size` 메소드는 표시되는 문자 수가 아닌 
실제 내용의 문자 수를 나타내기 때문에, 
이 예에서 `size` 메소드는 
`10`을 반환합니다.

`DECIMAL`과 같은 일부 제약 조건을 사용하면 
구현 시 텍스트 객체 내용의 구문을 검증해야 합니다. 
구문 검사는 텍스트 객체의 실제 내용에 대해 수행되며 
이 실제 내용은 위에서 설명한 대로 표시된 내용과 다를 수 있습니다. 
구문 검사는 구성자에 전달된 초기 내용에 대해 수행되며 
텍스트 객체의 내용에 영향을 주는 
모든 메소드 호출에도 강제 수행됩니다. 
메소드 및 구성자가 필요한 구문을 충족시키지 못하는 텍스트 객체 내용을 
만들면 `IllegalArgumentException`이 발생합니다.

``setConstraints()`` 메소드에 전달된 값은 
위에서 설명한 제한적 제약 조건과 
텍스트 입력 및 표시를 수정하는 
여러 플래그 비트로 구성되어 있습니다. 
제한적 제약 조건 설정 값은 값의 하위 `16`비트 부분이며 
비트 연산자 `AND`(`&`)로 제약 조건 
값과 `CONSTRAINT_MASK` 
상수를 결합하여 추출할 수 있습니다. 
제한적 제약 조건 설정은 다음과 같습니다.

수정자 플래그는 제약 조건 값의 
상위 `16`비트 부분 
즉, `CONSTRAINT_MASK` 상수의 보수 부분에 있습니다. 
수정자 플래그는 비트 `AND` (`&`) 
연산자로 제약 조건 값을 수정자 
플래그에 결합시켜 개별적으로 
테스트될 수 있습니다. 
수정자 플래그는 다음과 같습니다.

### 입력 모드

`TextField`는 ``TextBox`` 
클래스와 *입력 모드* 개념을 공유합니다. 
응용 프로그램은 사용자가 `TextField` 또는 
`TextBox`의 편집을 시작할 때 
특정 입력 모드를 사용하도록 구현될 수 있습니다. 
입력 모드는 특정 장치의 텍스트 입력용 
사용자 인터페이스에 존재하는 개념입니다. 
텍스트 입력용 사용자 인터페이스는 표준화되어 있지 않고 장치마다 
다르기 때문에 응용 프로그램이 입력 모드를 직접 요청할 수는 없습니다. 
대신 응용 프로그램은 특정 문자를 쉽게 입력할 수 있도록 요청할 수 있습니다. 
``setInitialInputMode()`` 메소드에 
유니코드 문자 하위 집합 이름을 전달하는 방법으로 
이러한 작업을 요청할 수 있습니다. 
이 메소드를 호출하면 구현 시 텍스트 입력 사용자 인터페이스 
모드를 이 하위 집합에 포함되는 문자 입력을 쉽게 할 수 있도록 
설정할 수 있습니다. 응용 프로그램은 수정자 플래그를 제약 조건 값으로 설정하여 
입력 모드가 특정한 동작 특성을 가지도록 요청할 수도 있습니다.

요청된 입력 모드는 사용자가 `TextBox` 
또는 `TextField` 객체의 편집을 시작할 때마다 
사용되어야 합니다. 사용자가 이전 편집 세션에서 입력 모드를 
변경한 경우 응용 프로그램이 요청한 입력 모드의 
우선 순위가 사용자가 설정했던 이전 입력 모드의 우선 순위보다 높습니다. 
하지만 입력 모드는 제한적이지 않으므로 사용자가 편집 중 
언제든지 입력 모드를 변경할 수 있습니다. 
편집이 이미 진행 중이면 `setInitialInputMode` 메소드에 
대한 호출이 현재 입력 모드에는 영향을 주지 않고 대신 
사용자가 다음 번에 이 텍스트 객체의 편집을 시작할 때 영향을 줍니다.

초기 입력 모드를 보면 구현에 대해 알 수 있습니다. 
구현 시 응용 프로그램의 요청을 충족하는 입력 모드를 제공할 수 없는 
경우에는 기본 입력 모드를 사용해야 합니다.

응용 프로그램이 요청하여 적용한 입력 모드는 
사용자가 입력할 수 있는 문자 집합으로 제한되지 않습니다. 
사용자는 입력 모드를 전환하여 현재 제약 조건 설정 내에서 
허용되는 모든 문자를 입력할 수 있어야 합니다. 
제약 조건 설정은 입력 모드 요청보다 우선 순위가 높으며 구현 시 
현재 제약 조건 설정과 맞지 않을 경우 특정 입력 모드를 
제공하지 않을 수 있습니다.

예를 들어, 현재 제약 조건이 `ANY`이면

setInitialInputMode("MIDP_UPPERCASE_LATIN");

호출은 초기 입력 모드가 라틴어 대문자 입력을 
허용하도록 설정해야 합니다. 
이로 인해 입력이 이러한 문자로 제한되는 것은 아니며 
숫자 및 라틴어 소문자 입력을 허용하는 입력 모드로 전환하여 
다른 문자를 입력할 수 있습니다. 
하지만 현재 제약 조건이 `NUMERIC`이면 
라틴어 대문자가 제약 조건이 `NUMERIC`인 
`TextField`에 허용되지 않기 때문에 
구현 시 초기 입력 모드가 `MIDP_UPPERCASE_LATIN` 
문자를 허용하도록 설정하는 요청은 무시될 수 있습니다. 
이 경우 숫자 입력을 허용하는 입력 모드가 `NUMERIC` 
제약 조건 하에서의 데이터 입력에 가장 적합하기 때문에 구현 시 
이 입력 모드를 대신 사용할 수 있습니다.

``setInitialInputMode()`` 메소드에 
매개 변수로 전달된 유니코드 문자 
하위 집합 이름에는 문자열이 사용됩니다. 
문자열 비교는 대소문자를 구분합니다.

유니코드 문자 블록의 이름은 J2SE 클래스 
`java.lang.Character.UnicodeBlock`에 정의된 대로, 
유니코드 문자 블록을 나타내는 필드의 문자열 이름에 
"`UCB`_"라는 접두어를 추가하여 만듭니다. 
유니코드 문자 블록의 이름은 모두 이런 형태로 지정합니다. 
편의를 위해 가장 일반적인 유니코드 문자 블록을 아래에 나열합니다.

"입력 하위 집합"은 J2SE 클래스 
`java.awt.im.InputSubset`에 정의된 대로 
이 클래스에 정의된 입력 하위 집합을 나타내는 필드의 
문자열 이름에 "`IS_`"라는 
접두어를 추가하여 만들 수 있습니다. 
정의된 입력 하위 집합은 모두 사용할 수 있습니다. 편의를 위해 현재 정의된 입력 하위 집합의 이름을 다음에 나열합니다.

MIDP에서는 다음과 같은 문자 하위 집합도 정의합니다.

마지막으로 구현별 문자 하위 집합의 이름은 
"`X_`"라는 접두어를 붙인 
문자열로 지정할 수 있습니다. 이름 공간의 충돌을 피하기 위해 
구현별 이름에는 "`X_`" 접두어 다음에 
회사나 조직을 정의하는 이름을 
포함시키는 것이 좋습니다.

예를 들어, 일본어 응용 프로그램에는 일본어가 아닌 
언어에서 "차용한" 단어를 입력할 때 주로 사용할 
특별한 `TextField`가 있을 수 있습니다. 
응용 프로그램은 다음 메소드를 
호출하여 히라가나를 사용하는 
입력 모드를 요청할 수 있습니다.

textfield.setInitialInputMode("UCB_HIRAGANA");

### 구현 노트

구현 시 위에 나열된 모든 문자열을 컴파일할 필요는 없습니다. 
대신 지원하는 유니코드 문자 하위 집합의 이름을 지정하는 문자열만 
컴파일하면 됩니다. 응용 프로그램이 전달한 하위 집합 이름이 
알려진 하위 집합 이름과 일치하지 않으면 요청은 오류 없이 
그냥 무시되고 기본 입력 모드가 사용되어야 합니다. 
이렇게 하면 구현 시 이 기능을 간단하게 지원할 수 있습니다. 
하지만 응용 프로그램에서는 요청이 수락되었는지 여부 및 
요청한 유니코드 문자 하위 집합이 실제로 유효한 하위 집합인지 
여부를 알 수 없습니다.

**Since:**
- MIDP 1.0

## 필드 요약

- `static int ANY` — 모든 텍스트를 입력할 수 있습니다.
- `static int CONSTRAINT_MASK` — 제약 조건 모드를 결정하는 마스크 값.
- `static int DECIMAL` — "-123", "0.123" 또는 ".5"와 같이 선택적 소수가 있는 숫자 값을 입력할 수 있습니다.
- `static int EMAILADDR` — 전자 메일 주소를 입력할 수 있습니다.
- `static int INITIAL_CAPS_SENTENCE` — 이 플래그를 보면 텍스트 편집 중 각 문장의 첫 번째 문자가 대문자여야 한다는 것을 알 수 있습니다.
- `static int INITIAL_CAPS_WORD` — 이 플래그를 보면 텍스트 편집 중 각 단어의 첫 번째 문자가 대문자여야 한다는 것을 알 수 있습니다.
- `static int NON_PREDICTIVE` — 입력된 텍스트가 일반적으로 예측 입력 계획에 사용되는, 사전에 없는 단어로 구성되어 있음을 표시합니다.
- `static int NUMERIC` — 정수 값만 입력할 수 있습니다.
- `static int PASSWORD` — 입력된 텍스트가 가능한 한 알아보기 힘들게 해야 하는 기밀 데이터임을 표시합니다.
- `static int PHONENUMBER` — 전화 번호를 입력할 수 있습니다.
- `static int SENSITIVE` — 입력된 텍스트가 구현 시 예측 가능하거나 자동 완성 또는 기타 빠른 입력 체계를 위해 내용을 사전이나 테이블에 저장하지 않아야 하는 중요한 데이터라는 것을 표시합니다.
- `static int UNEDITABLE` — 현재 편집이 허용되지 않음을 표시합니다.
- `static int URL` — URL을 입력할 수 있습니다.

## 생성자 요약

- TextField ( String label, String text,
 int maxSize,
 int constraints) 주어진 레이블, 초기 내용, 최대 문자 수 및 
제약 조건을 사용하여 새 TextField 객체를 만듭니다.

## 메서드 요약

- `void delete (int offset, int length)` — TextField 에서 문자를 삭제합니다.
- `int getCaretPosition ()` — 현재 입력 위치를 가져옵니다.
- `int getChars (char[] data)` — TextField 의 내용을 색인 0에서 시작하는 문자 배열로 복사합니다.
- `int getConstraints ()` — TextField 의 현재 입력 제약 조건을 가져옵니다.
- `int getMaxSize ()` — TextField 에 저장될 수 있는 최대 크기(문자 수)를 반환합니다.
- `String getString ()` — 문자열 값으로 TextField 의 내용을 가져옵니다.
- `void insert (char[] data, int offset, int length, int position)` — 문자 배열의 하위 범위를 TextField 의 내용에 삽입합니다.
- `void insert ( String src, int position)` — 문자열을 TextField 의 내용에 삽입합니다.
- `void setChars (char[] data, int offset, int length)` — 문자 배열로부터 TextField 의 내용을 설정하여 이전 내용을 교체합니다.
- `void setConstraints (int constraints)` — TextField 의 입력 제약 조건을 설정합니다.
- `void setInitialInputMode ( String characterSubset)` — 사용자가 이 TextField 의 편집을 시작할 때 사용되어야 할 입력 모드에 대한 힌트를 설정합니다.
- `int setMaxSize (int maxSize)` — TextField 내에 포함될 수 있는 최대 크기(문자 수)를 설정합니다.
- `void setString ( String text)` — 문자열 값으로 TextField 의 내용을 설정하여 이전 내용을 대체합니다.
- `int size ()` — 현재 TextField 내에 저장된 문자 수를 가져옵니다.

## 필드 상세

### ANY

```java
public static final int ANY
```

**See Also:**
- `Constant Field Values`

### EMAILADDR

```java
public static final int EMAILADDR
```

**See Also:**
- `Constant Field Values`

### NUMERIC

```java
public static final int NUMERIC
```

**See Also:**
- `Constant Field Values`

### PHONENUMBER

```java
public static final int PHONENUMBER
```

**See Also:**
- `Constant Field Values`

### URL

```java
public static final int URL
```

**See Also:**
- `Constant Field Values`

### DECIMAL

```java
public static final int DECIMAL
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### PASSWORD

```java
public static final int PASSWORD
```

**See Also:**
- `Constant Field Values`

### UNEDITABLE

```java
public static final int UNEDITABLE
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### SENSITIVE

```java
public static final int SENSITIVE
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### NON_PREDICTIVE

```java
public static final int NON_PREDICTIVE
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### INITIAL_CAPS_WORD

```java
public static final int INITIAL_CAPS_WORD
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### INITIAL_CAPS_SENTENCE

```java
public static final int INITIAL_CAPS_SENTENCE
```

**Since:**
- MIDP 2.0

**See Also:**
- `Constant Field Values`

### CONSTRAINT_MASK

```java
public static final int CONSTRAINT_MASK
```

**See Also:**
- `Constant Field Values`

### TextField

```java
public TextField(String label,
                 String text,
                 int maxSize,
                 int constraints)
```

- 주어진 레이블, 초기 내용, 최대 문자 수 및 
제약 조건을 사용하여 새 `TextField` 객체를 만듭니다. 
텍스트 매개 변수가 `null`이면 빈 `TextField`가 
작성됩니다. `maxSize` 매개 변수는 0보다 커야 합니다. 
초기 내용 문자열의 길이가 `maxSize`를 초과하면 
`IllegalArgumentException`이 발생합니다. 
하지만 구현 시 응용 프로그램이 요청한 것보다 
작은 최대 크기를 할당할 수 있습니다. 
이런 경우 내용의 길이가 
새로 할당된 최대 크기를 초과하면 
여기에 맞추기 위해 내용의 끝부분이 잘리고 
예외가 발생하지 않습니다.

**Parameters:**
- `constraints` - 입력 제약 조건을 참조하십시오.

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
- `text` - `TextField`의 새 값 또는 
TextField가 비어 있는 경우에는 `null`

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
- `IllegalArgumentException` - 텍스트가 현재 최대 용량을 
초과하는 경우

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
`length`가 `TextField` 내용 내의 
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
- `IllegalArgumentException` - 잘려진 후 내용이 
현재의 `입력 제약 조건`에 
유효하지 않은 경우

**See Also:**
- ``getMaxSize()``

### size

```java
public int size()
```

**Returns:**
- `TextField`의 문자 수

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
- `constraints` - 입력 제약 조건을 참조하십시오.

**Throws:**
- `IllegalArgumentException` - 제약 조건이 `입력 제약 조건`에 
지정된 제약 조건 중 하나가 아닌 경우

**See Also:**
- ``getConstraints()``

### getConstraints

```java
public int getConstraints()
```

**Returns:**
- 현재 제약 조건 값(입력 제약 조건 
참조)

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

## 생성자 상세

### TextField

```java
public TextField(String label,
                 String text,
                 int maxSize,
                 int constraints)
```

- 주어진 레이블, 초기 내용, 최대 문자 수 및 
제약 조건을 사용하여 새 `TextField` 객체를 만듭니다. 
텍스트 매개 변수가 `null`이면 빈 `TextField`가 
작성됩니다. `maxSize` 매개 변수는 0보다 커야 합니다. 
초기 내용 문자열의 길이가 `maxSize`를 초과하면 
`IllegalArgumentException`이 발생합니다. 
하지만 구현 시 응용 프로그램이 요청한 것보다 
작은 최대 크기를 할당할 수 있습니다. 
이런 경우 내용의 길이가 
새로 할당된 최대 크기를 초과하면 
여기에 맞추기 위해 내용의 끝부분이 잘리고 
예외가 발생하지 않습니다.

**Parameters:**
- `constraints` - 입력 제약 조건을 참조하십시오.

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
- `text` - `TextField`의 새 값 또는 
TextField가 비어 있는 경우에는 `null`

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
- `IllegalArgumentException` - 텍스트가 현재 최대 용량을 
초과하는 경우

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
`length`가 `TextField` 내용 내의 
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
- `IllegalArgumentException` - 잘려진 후 내용이 
현재의 `입력 제약 조건`에 
유효하지 않은 경우

**See Also:**
- ``getMaxSize()``

### size

```java
public int size()
```

**Returns:**
- `TextField`의 문자 수

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
- `constraints` - 입력 제약 조건을 참조하십시오.

**Throws:**
- `IllegalArgumentException` - 제약 조건이 `입력 제약 조건`에 
지정된 제약 조건 중 하나가 아닌 경우

**See Also:**
- ``getConstraints()``

### getConstraints

```java
public int getConstraints()
```

**Returns:**
- 현재 제약 조건 값(입력 제약 조건 
참조)

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
- `text` - `TextField`의 새 값 또는 
TextField가 비어 있는 경우에는 `null`

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
- `IllegalArgumentException` - 텍스트가 현재 최대 용량을 
초과하는 경우

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
`length`가 `TextField` 내용 내의 
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
- `IllegalArgumentException` - 잘려진 후 내용이 
현재의 `입력 제약 조건`에 
유효하지 않은 경우

**See Also:**
- ``getMaxSize()``

### size

```java
public int size()
```

**Returns:**
- `TextField`의 문자 수

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
- `constraints` - 입력 제약 조건을 참조하십시오.

**Throws:**
- `IllegalArgumentException` - 제약 조건이 `입력 제약 조건`에 
지정된 제약 조건 중 하나가 아닌 경우

**See Also:**
- ``getConstraints()``

### getConstraints

```java
public int getConstraints()
```

**Returns:**
- 현재 제약 조건 값(입력 제약 조건 
참조)

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
