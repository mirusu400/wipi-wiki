# Class StringItem

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Item
        |
        +--javax.microedition.lcdui.StringItem
```

## 설명

**extends Item:**

문자열을 포함할 수 있는 항목. 
`StringItem`은 디스플레이 전용이므로 사용자는 내용을 
편집할 수 없습니다. `StringItem`의 레이블과 텍스트 
내용 모두 응용 프로그램을 사용하여 수정할 수 있습니다. 
레이블의 시각적 표현은 텍스트 내용의 
시각적 표현과 다를 수 있습니다.

## 필드 요약

## 생성자 요약

- StringItem ( String label, String text) 새 StringItem 객체를 만듭니다.
- StringItem ( String label, String text,
 int appearanceMode) 제공된 레이블, 텍스트 내용 및 모양 모드를 사용하여 새 StringItem 객체를 만듭니다.

## 메서드 요약

- `int getAppearanceMode ()` — StringItem 의 모양 모드를 반환합니다.
- `Font getFont ()` — 이 StringItem 을 렌더링하기 위한 응용 프로그램의 기본 글꼴을 가져옵니다.
- `String getText ()` — StringItem 의 텍스트 내용을 가져오거나 StringItem 이 비어 있는 경우에는 null 을 가져옵니다.
- `void setFont ( Font font)` — 이 StringItem 을 렌더링하기 위한 응용 프로그램의 기본 글꼴을 설정합니다.
- `void setText ( String text)` — StringItem 의 텍스트 내용을 설정합니다.

## 생성자 상세

### StringItem

```java
public StringItem(String label,
                  String text)
```

- 새 `StringItem` 객체를 만듭니다. 
이 구성자를 호출하는 것은 다음을 호출하는 것과 같습니다.
 
 

`
 StringItem(label, text, PLAIN); `

**Parameters:**
- `text` - 텍스트 내용

**See Also:**
- ``StringItem(String, String, int)``

### StringItem

```java
public StringItem(String label,
                  String text,
                  int appearanceMode)
```

- 제공된 레이블, 텍스트 내용 및 모양 모드를 사용하여 새 
`StringItem` 객체를 만듭니다. 
레이블이나 텍스트가 존재하거나 `null`일 수 있습니다.

`appearanceMode` 매개 
변수(`모양 모드` 참조)를 
보면 응용 프로그램이 이 `StringItem`에 사용할 
플랫폼이 무엇인지 알 수 있습니다. 
하이퍼링크나 버튼 같은 동작을 제공하려면 응용 프로그램은 
기본 `Command`를 이 `StringItem`과 
연관시키고 이 `StringItem`에 
`ItemCommandListener`를 
추가해야 합니다.

`StringItem`을 버튼으로 사용하는 예는 
다음과 같습니다.

```java
StringItem strItem = 
         new StringItem("Default: ", "Set",     
                        Item.BUTTON);    
     strItem.setDefaultCommand(
         new Command("Set", Command.ITEM, 1);    
     // icl is ItemCommandListener 
     strItem.setItemCommandListener(icl);
```

**Parameters:**
- `appearanceMode` - `StringItem`의 모양 모드, 
``Item.PLAIN``, ``Item.HYPERLINK`` 또는 ``Item.BUTTON`` 중 하나

**Throws:**
- `IllegalArgumentException` - `appearanceMode`가 유효하지 않은 경우

**Since:**
- MIDP 2.0

### getText

```java
public String getText()
```

**Returns:**
- 항목의 내용이 있는 문자열

**See Also:**
- ``setText(java.lang.String)``

### setText

```java
public void setText(String text)
```

**Parameters:**
- `text` - 새 내용

**See Also:**
- ``getText()``

### getAppearanceMode

```java
public int getAppearanceMode()
```

**Returns:**
- 모양 모드 값, ``Item.PLAIN``, ``Item.HYPERLINK`` 또는 
``Item.BUTTON`` 중 하나

**Since:**
- MIDP 2.0

### setFont

```java
public void setFont(Font font)
```

**Parameters:**
- `font` - `StringItem` 렌더링에 
사용할 기본 글꼴

**Since:**
- MIDP 2.0

**See Also:**
- ``getFont()``

### getFont

```java
public Font getFont()
```

**Returns:**
- `StringItem` 렌더링에 
사용할 기본 글꼴

**Since:**
- MIDP 2.0

**See Also:**
- ``setFont(javax.microedition.lcdui.Font)``

## 메서드 상세

### getText

```java
public String getText()
```

**Returns:**
- 항목의 내용이 있는 문자열

**See Also:**
- ``setText(java.lang.String)``

### setText

```java
public void setText(String text)
```

**Parameters:**
- `text` - 새 내용

**See Also:**
- ``getText()``

### getAppearanceMode

```java
public int getAppearanceMode()
```

**Returns:**
- 모양 모드 값, ``Item.PLAIN``, ``Item.HYPERLINK`` 또는 
``Item.BUTTON`` 중 하나

**Since:**
- MIDP 2.0

### setFont

```java
public void setFont(Font font)
```

**Parameters:**
- `font` - `StringItem` 렌더링에 
사용할 기본 글꼴

**Since:**
- MIDP 2.0

**See Also:**
- ``getFont()``

### getFont

```java
public Font getFont()
```

**Returns:**
- `StringItem` 렌더링에 
사용할 기본 글꼴

**Since:**
- MIDP 2.0

**See Also:**
- ``setFont(javax.microedition.lcdui.Font)``
