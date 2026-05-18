# Class Font

`package org.kwis.msp.lcdui`

```text
java.lang.Object
  |
  +--org.kwis.msp.lcdui.Font
```

## 설명

**extends Object:**

글꼴 클래스 입니다.

문자열을 찍는데 사용되는 문자를 나타내는 글꼴 클래스입니다.
 `getFont`를 사용해서 원하는 폰트를 가져옵니다. 
 기본적으로 `getFont`를 해서 가져온
 폰트는 내부적으로 공유하므로 자원을 프리해야할 필요는 없습니다.

`getFont`함수로 가져와서 
 ``Graphics.setFont(org.kwis.msp.lcdui.Font)``함수를 
 통해서 폰트를 지정하여 문자의 화면 출력 외형을 변경할 수 있습니다.

`getFont`를 통해서 시스템에 따라서,
 지정한 폰트가 아닌 그와 유사한 폰트를 돌려 받을 수 있습니다.

문자열의 화면 출력 길이를 알기 위해서는 `stringWidth`나 
 `substringWidth`함수를 사용합니다.

폰트의 스타일은 다음중 하나가 됩니다.
 `STYLE_PLAIN` 

`STYLE_UNDERLINED ` 

`STYLE_BOLD` 

`STYLE_BOLD | STYLE_UNDERLINED` 

`STYLE_ITALIC` 

`STYLE_ITALIC | STYLE_UNDERLINED` 

`STYLE_BOLD | STYLE_ITALIC` 

`STYLE_BOLD | STYLE_ITALIC | STYLE_UNDERLINED`

## 필드 요약

- `protected  int face`
- `static int FACE_MONOSPACE` — Monospace폰트 페이스.
- `static int FACE_PROPORTIONAL` — Proportional폰트 페이스.
- `static int FACE_SYSTEM` — System 폰트 페이스.
- `protected  int size`
- `static int SIZE_LARGE` — 큰 크기의 폰트 크기.
- `static int SIZE_MEDIUM` — 중간 크기의 폰트 크기.
- `static int SIZE_SMALL` — 작은 크기의 폰트 크기.
- `protected  int style`
- `static int STYLE_BOLD` — 진한 폰트 스타일.
- `static int STYLE_ITALIC` — 기운 폰트 스타일.
- `static int STYLE_PLAIN` — 보통 폰트 스타일.
- `static int STYLE_UNDERLINED` — 밑줄 그은 폰트 스타일.

## 메서드 요약

- `int charsWidth (char[] ch, int offset, int length)` — 문자열의 화면상의 폭을 넘겨줍니다.
- `int charWidth (char ch)` — 문자의 화면상의 폭을 넘겨 줍니다.
- `int getBaselinePosition ()` — 문자의 베이스 라인(base line) 높이를 돌려줍니다.
- `static Font getDefaultFont ()` — 시스템의 기본 폰트를 돌려줍니다.
- `int getFace ()` — 폰트의 페이스를 돌려줍니다.
- `static Font getFont (int face, int style, int size)` — 특정 폰트를 얻어 옵니다.
- `int getHeight ()` — 폰트의 높이를 얻어옵니다.
- `int getSize ()` — 폰트의 크기를 얻어 옵니다.
- `int getStyle ()` — 폰트의 스타일을 얻어 옵니다.
- `boolean isBold ()` — 폰트의 스타일을 STYLE_BOLD 인지 아닌지 여부를 돌려줍니다.
- `boolean isItalic ()` — 폰트의 스타일을 STYLE_ITALIC 인지 아닌지 여부를 돌려줍니다.
- `boolean isPlain ()` — 폰트의 스타일을 STYLE_PLAIN 인지 아닌지 여부를 돌려줍니다.
- `boolean isUnderlined ()` — 폰트의 스타일을 STYLE_UNDERLINED 인지 아닌지 여부를 돌려줍니다.
- `int stringWidth ( String str)` — 문자열의 폭을 얻어 옵니다.
- `int substringWidth ( String str, int offset, int len)` — 문자열의 일부의 폭을 얻어 옵니다.

## 필드 상세

### FACE_MONOSPACE

```java
public static int FACE_MONOSPACE
```

- Monospace폰트 페이스.
 값 32로 지정되어 있으며, 폭이 일정한 폰트를 지정합니다.

### FACE_PROPORTIONAL

```java
public static int FACE_PROPORTIONAL
```

- Proportional폰트 페이스.
 값이 64로 지정되어 있으며, 폭이 일정하지 않은 폰트를 지정합니다.

### FACE_SYSTEM

```java
public static int FACE_SYSTEM
```

- System 폰트 페이스.
 값이 0으로 지정되어 있으며, 시스템 폰트에서 사용하는
 폰트입니다. MONOSPACE혹은 PROPORTIONAL둘중 하나 입니다.

### SIZE_LARGE

```java
public static int SIZE_LARGE
```

- 큰 크기의 폰트 크기.
 값이 16으로 지정되어 있으며, 시스템의 큰 폰트를 지정합니다.

### SIZE_MEDIUM

```java
public static int SIZE_MEDIUM
```

- 중간 크기의 폰트 크기.
 값이 0으로 지정되어 있으며, 시스템의 중간 폰트를 지정합니다.

### SIZE_SMALL

```java
public static int SIZE_SMALL
```

- 작은 크기의 폰트 크기.
 값이 8로 지정되어 있으며, 시스템의 작은 폰트를 지정합니다.

### STYLE_BOLD

```java
public static int STYLE_BOLD
```

- 진한 폰트 스타일.
 다른 폰트 스타일과 혼합되어 사용할 수 있다. 값은 1로 지정합니다.

### STYLE_ITALIC

```java
public static int STYLE_ITALIC
```

- 기운 폰트 스타일.
 다른 폰트 스타일과 혼합되어 사용할 수 있다. 값은 2로 지정합니다.

### STYLE_PLAIN

```java
public static int STYLE_PLAIN
```

- 보통 폰트 스타일.
 다른 폰트 스타일과 혼합되어 사용할 수 있다. 값은 0로 지정합니다.

### STYLE_UNDERLINED

```java
public static int STYLE_UNDERLINED
```

- 밑줄 그은 폰트 스타일.
 다른 폰트 스타일과 혼합되어 사용할 수 있다. 값은 4로 지정되어 있다.

### style

```java
protected int style
```

### size

```java
protected int size
```

### face

```java
protected int face
```

### getFont

```java
public static Font getFont(int face,
                           int style,
                           int size)
```

**Parameters:**
- `size` - 폰트 크기; `SIZE_LARGE`, 
 `SIZE_MEDIUM`, `SIZE_SMALL`중 하나가 
 올 수 있음

**Throws:**
- `IllegalArgumentException` - `face`, `style`,
 `size`중에 하나라도 유효한 값을 가지지 않는 경우.

### charsWidth

```java
public int charsWidth(char[] ch,
                      int offset,
                      int length)
```

**Parameters:**
- `length` - 문자 갯수

**Returns:**
- 문자열의 화면상의 픽셀 단위의 폭

**Throws:**
- `NullPointerException` - ch가 null인 경우

### charWidth

```java
public int charWidth(char ch)
```

**Parameters:**
- `ch` - 문자

**Returns:**
- 문자의 화면상의 픽셀 단위의 폭

### getBaselinePosition

```java
public int getBaselinePosition()
```

**Returns:**
- 문자의 baseline

### getDefaultFont

```java
public static Font getDefaultFont()
```

**Returns:**
- 시스템 기본 폰트

### getFace

```java
public int getFace()
```

**Returns:**
- 폰트의 페이스

### getHeight

```java
public int getHeight()
```

**Returns:**
- 폰트의 높이

### getSize

```java
public int getSize()
```

**Returns:**
- 폰트의 크기

### getStyle

```java
public int getStyle()
```

**Returns:**
- 폰트의 스타일

### isBold

```java
public boolean isBold()
```

**Returns:**
- 폰트의 스타일이 `STYLE_BOLD`이면 
 `true` 그렇지 않으면 
 `false`

### isItalic

```java
public boolean isItalic()
```

**Returns:**
- 폰트의 스타일이 `STYLE_ITALIC`이면 
 `true` 그렇지 않으면 `false`

### isPlain

```java
public boolean isPlain()
```

**Returns:**
- 폰트의 스타일이 `STYLE_PLAIN`이면 `true`
 그렇지 않으면 `false`

### isUnderlined

```java
public boolean isUnderlined()
```

**Returns:**
- 폰트의 스타일이 `STYLE_UNDERLINED`이면 
 `true` 그렇지 않으면 `false`

### stringWidth

```java
public int stringWidth(String str)
```

**Parameters:**
- `str` - 폭을 계산할 문자열

**Returns:**
- 문자열의 폭

**Throws:**
- `NullPointerException` - str이 `null`인 경우.

### substringWidth

```java
public int substringWidth(String str,
                          int offset,
                          int len)
```

**Parameters:**
- `len` - 문자열의 문자 갯수

**Returns:**
- 문자열의 폭

**Throws:**
- `NullPointerException` - str이 `null`인 경우.## 메서드 상세

### getFont

```java
public static Font getFont(int face,
                           int style,
                           int size)
```

**Parameters:**
- `size` - 폰트 크기; `SIZE_LARGE`, 
 `SIZE_MEDIUM`, `SIZE_SMALL`중 하나가 
 올 수 있음

**Throws:**
- `IllegalArgumentException` - `face`, `style`,
 `size`중에 하나라도 유효한 값을 가지지 않는 경우.

### charsWidth

```java
public int charsWidth(char[] ch,
                      int offset,
                      int length)
```

**Parameters:**
- `length` - 문자 갯수

**Returns:**
- 문자열의 화면상의 픽셀 단위의 폭

**Throws:**
- `NullPointerException` - ch가 null인 경우

### charWidth

```java
public int charWidth(char ch)
```

**Parameters:**
- `ch` - 문자

**Returns:**
- 문자의 화면상의 픽셀 단위의 폭

### getBaselinePosition

```java
public int getBaselinePosition()
```

**Returns:**
- 문자의 baseline

### getDefaultFont

```java
public static Font getDefaultFont()
```

**Returns:**
- 시스템 기본 폰트

### getFace

```java
public int getFace()
```

**Returns:**
- 폰트의 페이스

### getHeight

```java
public int getHeight()
```

**Returns:**
- 폰트의 높이

### getSize

```java
public int getSize()
```

**Returns:**
- 폰트의 크기

### getStyle

```java
public int getStyle()
```

**Returns:**
- 폰트의 스타일

### isBold

```java
public boolean isBold()
```

**Returns:**
- 폰트의 스타일이 `STYLE_BOLD`이면 
 `true` 그렇지 않으면 
 `false`

### isItalic

```java
public boolean isItalic()
```

**Returns:**
- 폰트의 스타일이 `STYLE_ITALIC`이면 
 `true` 그렇지 않으면 `false`

### isPlain

```java
public boolean isPlain()
```

**Returns:**
- 폰트의 스타일이 `STYLE_PLAIN`이면 `true`
 그렇지 않으면 `false`

### isUnderlined

```java
public boolean isUnderlined()
```

**Returns:**
- 폰트의 스타일이 `STYLE_UNDERLINED`이면 
 `true` 그렇지 않으면 `false`

### stringWidth

```java
public int stringWidth(String str)
```

**Parameters:**
- `str` - 폭을 계산할 문자열

**Returns:**
- 문자열의 폭

**Throws:**
- `NullPointerException` - str이 `null`인 경우.

### substringWidth

```java
public int substringWidth(String str,
                          int offset,
                          int len)
```

**Parameters:**
- `len` - 문자열의 문자 갯수

**Returns:**
- 문자열의 폭

**Throws:**
- `NullPointerException` - str이 `null`인 경우.

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
