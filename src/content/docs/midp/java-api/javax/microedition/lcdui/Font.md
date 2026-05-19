---
title: "Class Font"
---

`package javax.microedition.lcdui`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.Font
```

## 설명

**extends Object:**

`Font` 클래스는 
글꼴 및 글꼴 메트릭을 나타냅니다. 
`Font`는 응용 프로그램에서 만들 수 없습니다. 
대신 응용 프로그램은 글꼴 속성을 
기반으로 글꼴을 쿼리하며 
시스템은 가능하면 요청한 속성과 일치하는 
글꼴을 제공하려고 시도합니다.

`Font`의 속성은 스타일, 크기 및 서체입니다. 
속성 값은 심볼릭 상수를 기준으로 지정해야 합니다. 
스타일 속성 값은 비트 방식 `OR` 연산자를 
사용하여 결합될 수 있지만 
다른 속성의 값은 결합되지 않을 수 있습니다. 
예를 들어, 다음 값

`
 STYLE_BOLD | STYLE_ITALIC 
`은

굵은 기울임체 글꼴을 지정하는 데 사용할 수 있지만 다음 값

`
 SIZE_LARGE | SIZE_SMALL
 `은

유효하지 않습니다.

이러한 상수 값은 각 속성에 대해 0이 유효하도록 정렬되며 
시스템에 적합한 기본 글꼴을 지정하는 데 사용할 수 있습니다. 
정확한 프로그래밍을 위해 다음 심볼릭 상수가 제공되며 
값은 0으로 정의됩니다.

- ` STYLE_PLAIN `
- ` SIZE_MEDIUM `
- ` FACE_SYSTEM `

다른 속성 값의 경우 실수로 이 속성을 잘못 
사용하면(예: 스타일이 필요한 곳에 
`FACE_PROPORTIONAL` 사용) 
오류를 발생시키기 위해 분리된 
비트 패턴을 가지도록 정렬됩니다. 
하지만 다양한 속성 값은 서로 결합되지는 않습니다.

**Since:**
- MIDP 1.0

## 필드 요약

- `static int FACE_MONOSPACE` — "고정 폭" 글꼴.
- `static int FACE_PROPORTIONAL` — "비례" 글꼴.
- `static int FACE_SYSTEM` — "시스템" 글꼴.
- `static int FONT_INPUT_TEXT` — 사용자가 텍스트 입력을 그리기 위해 구현 시 사용하는 글꼴 지정자.
- `static int FONT_STATIC_TEXT` — 항목 및 화면 내용을 그리기 위해 사용된 기본 글꼴 지정자.
- `static int SIZE_LARGE` — "큰" 시스템 종속 글꼴 크기.
- `static int SIZE_MEDIUM` — "중간" 시스템 종속 글꼴 크기.
- `static int SIZE_SMALL` — "작은" 시스템 종속 글꼴 크기.
- `static int STYLE_BOLD` — 굵은체 스타일 상수.
- `static int STYLE_ITALIC` — 기울임꼴 스타일 상수.
- `static int STYLE_PLAIN` — 일반 스타일 상수.
- `static int STYLE_UNDERLINED` — 밑줄 스타일 상수.

## 메서드 요약

- `int charsWidth (char[] ch, int offset, int length)` — 지정한 오프셋에서 시작하여 지정한 문자 수(길이)로 ch 의 문자 진행 폭을 반환합니다.
- `int charWidth (char ch)` — 이 글꼴로 지정된 문자의 진행 폭을 가져옵니다.
- `int getBaselinePosition ()` — 텍스트의 맨 위에서 텍스트 기준선까지의 거리(픽셀 단위)를 가져옵니다.
- `static Font getDefaultFont ()` — 시스템의 기본 글꼴을 가져옵니다.
- `int getFace ()` — 글꼴의 서체를 가져옵니다.
- `static Font getFont (int fontSpecifier)` — 전달된 fontSpecifier 에 높은 수준의 사용자 인터페이스에서 사용하는 Font 를 가져옵니다.
- `static Font getFont (int face, int style, int size)` — 지정한 서체, 스타일 및 크기를 갖는 글꼴을 나타내는 객체를 가져옵니다.
- `int getHeight ()` — 이 글꼴인 텍스트 행의 표준 높이를 가져옵니다.
- `int getSize ()` — 글꼴의 크기를 가져옵니다.
- `int getStyle ()` — 글꼴의 스타일을 가져옵니다.
- `boolean isBold ()` — 굵은체 글꼴인 경우 true 를 반환합니다.
- `boolean isItalic ()` — 기울임꼴 글꼴인 경우 true 를 반환합니다.
- `boolean isPlain ()` — 일반 글꼴인 경우 true 를 반환합니다.
- `boolean isUnderlined ()` — 밑줄 그어진 글꼴인 경우 true 를 반환합니다.
- `int stringWidth ( String str)` — 이 Font 로 지정한 String 을 표시하기 위해 전체 진행 폭을 가져옵니다.
- `int substringWidth ( String str, int offset, int len)` — 이 Font 로 지정한 하위 문자열을 표시하기 위해 전체 진행 폭을 가져옵니다.

## 필드 상세

### STYLE_PLAIN

```java
public static final int STYLE_PLAIN
```

**See Also:**
- `Constant Field Values`

### STYLE_BOLD

```java
public static final int STYLE_BOLD
```

**See Also:**
- `Constant Field Values`

### STYLE_ITALIC

```java
public static final int STYLE_ITALIC
```

**See Also:**
- `Constant Field Values`

### STYLE_UNDERLINED

```java
public static final int STYLE_UNDERLINED
```

**See Also:**
- `Constant Field Values`

### SIZE_SMALL

```java
public static final int SIZE_SMALL
```

**See Also:**
- `Constant Field Values`

### SIZE_MEDIUM

```java
public static final int SIZE_MEDIUM
```

**See Also:**
- `Constant Field Values`

### SIZE_LARGE

```java
public static final int SIZE_LARGE
```

**See Also:**
- `Constant Field Values`

### FACE_SYSTEM

```java
public static final int FACE_SYSTEM
```

**See Also:**
- `Constant Field Values`

### FACE_MONOSPACE

```java
public static final int FACE_MONOSPACE
```

**See Also:**
- `Constant Field Values`

### FACE_PROPORTIONAL

```java
public static final int FACE_PROPORTIONAL
```

**See Also:**
- `Constant Field Values`

### FONT_STATIC_TEXT

```java
public static final int FONT_STATIC_TEXT
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getFont(int fontSpecifier)``, 
`Constant Field Values`

### FONT_INPUT_TEXT

```java
public static final int FONT_INPUT_TEXT
```

**Since:**
- MIDP 2.0

**See Also:**
- ``getFont(int fontSpecifier)``, 
`Constant Field Values`

### getFont

```java
public static Font getFont(int fontSpecifier)
```

**Parameters:**
- `fontSpecifier` - `FONT_INPUT_TEXT`나 
`FONT_STATIC_TEXT` 중 하나

**Returns:**
- 글꼴 지정자에 전달된 글꼴

**Throws:**
- `IllegalArgumentException` - `fontSpecifier`가 
유효한 fontSpecifier가 아닌 경우

**Since:**
- MIDP 2.0

### getDefaultFont

```java
public static Font getDefaultFont()
```

**Returns:**
- 기본 글꼴

### getFont

```java
public static Font getFont(int face,
                           int style,
                           int size)
```

**Parameters:**
- `size` - `SIZE_SMALL`이나 `SIZE_MEDIUM`, 
`SIZE_LARGE` 중 하나

**Returns:**
- 검색된 가장 근접한 글꼴 인스턴스

**Throws:**
- `IllegalArgumentException` - `face`, 
`style` 또는 `size`가 
유효한 값이 아닌 경우

### getStyle

```java
public int getStyle()
```

**Returns:**
- 현재 글꼴 스타일

**See Also:**
- ``isPlain()``, 
``isBold()``, 
``isItalic()``

### getSize

```java
public int getSize()
```

**Returns:**
- `SIZE_SMALL`이나 `SIZE_MEDIUM`, 
`SIZE_LARGE` 중 하나

### getFace

```java
public int getFace()
```

**Returns:**
- `FACE_SYSTEM`이나 
`FACE_PROPORTIONAL`, `FACE_MONOSPACE` 중 하나

### isPlain

```java
public boolean isPlain()
```

**Returns:**
- 일반 글꼴인 경우 `true`

**See Also:**
- ``getStyle()``

### isBold

```java
public boolean isBold()
```

**Returns:**
- 굵은체 글꼴인 경우 `true`

**See Also:**
- ``getStyle()``

### isItalic

```java
public boolean isItalic()
```

**Returns:**
- 기울임꼴 글꼴인 경우 `true`

**See Also:**
- ``getStyle()``

### isUnderlined

```java
public boolean isUnderlined()
```

**Returns:**
- 밑줄 그어진 글꼴인 경우 `true`

**See Also:**
- ``getStyle()``

### getHeight

```java
public int getHeight()
```

**Returns:**
- 이 글꼴인 텍스트 행의 
표준 높이(음수가 아닌 값)

### getBaselinePosition

```java
public int getBaselinePosition()
```

**Returns:**
- 텍스트의 맨 위에서 텍스트의 
기준선까지의 거리(픽셀 단위)

### charWidth

```java
public int charWidth(char ch)
```

**Parameters:**
- `ch` - 측정되는 문자

**Returns:**
- 전체 진행 폭(음수가 아닌 값)

### charsWidth

```java
public int charsWidth(char[] ch,
                      int offset,
                      int length)
```

**Parameters:**
- `length` - 측정할 문자 수

**Returns:**
- 문자 범위의 너비

**Throws:**
- `NullPointerException` - `ch`가 `null`인 경우

### stringWidth

```java
public int stringWidth(String str)
```

**Parameters:**
- `str` - 측정되는 `String`

**Returns:**
- 전체 진행 폭

**Throws:**
- `NullPointerException` - `str`이 `null`인 경우

### substringWidth

```java
public int substringWidth(String str,
                          int offset,
                          int len)
```

**Parameters:**
- `len` - 하위 문자열 길이

**Returns:**
- 전체 진행 폭

**Throws:**
- `NullPointerException` - `str`이 `null`인 경우

## 메서드 상세

### getFont

```java
public static Font getFont(int fontSpecifier)
```

**Parameters:**
- `fontSpecifier` - `FONT_INPUT_TEXT`나 
`FONT_STATIC_TEXT` 중 하나

**Returns:**
- 글꼴 지정자에 전달된 글꼴

**Throws:**
- `IllegalArgumentException` - `fontSpecifier`가 
유효한 fontSpecifier가 아닌 경우

**Since:**
- MIDP 2.0

### getDefaultFont

```java
public static Font getDefaultFont()
```

**Returns:**
- 기본 글꼴

### getFont

```java
public static Font getFont(int face,
                           int style,
                           int size)
```

**Parameters:**
- `size` - `SIZE_SMALL`이나 `SIZE_MEDIUM`, 
`SIZE_LARGE` 중 하나

**Returns:**
- 검색된 가장 근접한 글꼴 인스턴스

**Throws:**
- `IllegalArgumentException` - `face`, 
`style` 또는 `size`가 
유효한 값이 아닌 경우

### getStyle

```java
public int getStyle()
```

**Returns:**
- 현재 글꼴 스타일

**See Also:**
- ``isPlain()``, 
``isBold()``, 
``isItalic()``

### getSize

```java
public int getSize()
```

**Returns:**
- `SIZE_SMALL`이나 `SIZE_MEDIUM`, 
`SIZE_LARGE` 중 하나

### getFace

```java
public int getFace()
```

**Returns:**
- `FACE_SYSTEM`이나 
`FACE_PROPORTIONAL`, `FACE_MONOSPACE` 중 하나

### isPlain

```java
public boolean isPlain()
```

**Returns:**
- 일반 글꼴인 경우 `true`

**See Also:**
- ``getStyle()``

### isBold

```java
public boolean isBold()
```

**Returns:**
- 굵은체 글꼴인 경우 `true`

**See Also:**
- ``getStyle()``

### isItalic

```java
public boolean isItalic()
```

**Returns:**
- 기울임꼴 글꼴인 경우 `true`

**See Also:**
- ``getStyle()``

### isUnderlined

```java
public boolean isUnderlined()
```

**Returns:**
- 밑줄 그어진 글꼴인 경우 `true`

**See Also:**
- ``getStyle()``

### getHeight

```java
public int getHeight()
```

**Returns:**
- 이 글꼴인 텍스트 행의 
표준 높이(음수가 아닌 값)

### getBaselinePosition

```java
public int getBaselinePosition()
```

**Returns:**
- 텍스트의 맨 위에서 텍스트의 
기준선까지의 거리(픽셀 단위)

### charWidth

```java
public int charWidth(char ch)
```

**Parameters:**
- `ch` - 측정되는 문자

**Returns:**
- 전체 진행 폭(음수가 아닌 값)

### charsWidth

```java
public int charsWidth(char[] ch,
                      int offset,
                      int length)
```

**Parameters:**
- `length` - 측정할 문자 수

**Returns:**
- 문자 범위의 너비

**Throws:**
- `NullPointerException` - `ch`가 `null`인 경우

### stringWidth

```java
public int stringWidth(String str)
```

**Parameters:**
- `str` - 측정되는 `String`

**Returns:**
- 전체 진행 폭

**Throws:**
- `NullPointerException` - `str`이 `null`인 경우

### substringWidth

```java
public int substringWidth(String str,
                          int offset,
                          int len)
```

**Parameters:**
- `len` - 하위 문자열 길이

**Returns:**
- 전체 진행 폭

**Throws:**
- `NullPointerException` - `str`이 `null`인 경우
