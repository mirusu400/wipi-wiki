# Class ImageItem

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Item
        |
        +--javax.microedition.lcdui.ImageItem
```

## 설명

**extends Item:**

이미지를 포함할 수 있는 항목입니다.

각 `ImageItem` 항목에는 ``Image`` 
객체에 대한 참조가 들어 있습니다. 
이 `Image`는 
변경 가능하거나 변경 불가능합니다. 
`Image`가 변경 가능한 경우 `ImageItem`이 
이 `Image`로 구성되고 `setImage`가 
`Image`와 함께 호출되는 시점의 이미지 내용으로 
스냅샷을 생성한 것과 같은 기능을 합니다. 
이 스냅샷은 `ImageItem`의 
내용이 표시될 때마다 사용됩니다. 
그 후에 응용 프로그램이 `Image`에 그림을 그리더라도 
`setImage`에 대한 
다음 호출 전까지는 
스냅샷이 수정되지 않습니다. 
이 스냅샷은 `ImageItem`의 컨테이너가 활성 상태가 
되거나 디스플레이에서 보이게 되면 
업데이트되지 *않습니다.* 
이는 응용 프로그램이 `Displayables`와 항목이 
디스플레이에 나타나고 사라질 정확한 시기를 
제어하지 못하기 때문입니다.

`ImageItem`의 이미지 내용에는 
`null` 값이 지정될 수 있습니다. 
이런 경우 및 레이블 또한 
`null`인 경우에는 
`ImageItem`이 화면에서 
공간을 차지하지 않습니다.

`ImageItem`에는 처음에 MIDP 1.0에 
정의된 레이아웃 지시어가 들어 있습니다. 
이러한 레이아웃 지시어는 ``Item`` 클래스로 이동되었고 
이제는 모든 항목에 적용됩니다. 
선언은 소스 호환성을 위해 `ImageItem`에 남아 있습니다.

`altText` 매개 변수는 이미지가 디스플레이 
용량을 초과한 경우 이미지의 
위치에 표시될 문자열을 지정합니다. 
`altText` 매개 변수는 
`null`일 수 있습니다.

**Since:**
- MIDP 1.0

## 필드 요약

- `static int LAYOUT_CENTER` — `Item.LAYOUT_CENTER` 를 참조하십시오.
- `static int LAYOUT_DEFAULT` — `Item.LAYOUT_DEFAULT` 를 참조하십시오.
- `static int LAYOUT_LEFT` — `Item.LAYOUT_LEFT` 를 참조하십시오.
- `static int LAYOUT_NEWLINE_AFTER` — `Item.LAYOUT_NEWLINE_AFTER` 를 참조하십시오.
- `static int LAYOUT_NEWLINE_BEFORE` — `Item.LAYOUT_NEWLINE_BEFORE` 를 참조하십시오.
- `static int LAYOUT_RIGHT` — `Item.LAYOUT_RIGHT` 를 참조하십시오.

## 생성자 요약

- ImageItem ( String label, Image img,
 int layout, String altText) 주어진 레이블, 이미지, 레이아웃 지시어 및 대체 텍스트 문자열로 
새 ImageItem 을 작성합니다.
- ImageItem ( String label, Image image,
 int layout, String altText,
 int appearanceMode) 주어진 레이블, 이미지, 레이아웃 지시어, 대체 
텍스트 문자열 및 모양 모드로 새 ImageItem 객체를 작성합니다.

## 메서드 요약

- `String getAltText ()` — 이미지가 장치의 표시 용량을 초과한 경우 사용할 텍스트 문자열을 가져옵니다.
- `int getAppearanceMode ()` — ImageItem 의 모양 모드를 반환합니다.
- `Image getImage ()` — ImageItem 에 포함된 이미지를 가져오거나 포함된 이미지가 없으면 null 을 가져옵니다.
- `int getLayout ()` — 이미지 배치에 사용할 레이아웃 지시어를 가져옵니다.
- `void setAltText ( String text)` — ImageItem 의 대체 텍스트를 설정하거나 대체 텍스트가 제공되지 않은 경우 null 을 설정합니다.
- `void setImage ( Image img)` — ImageItem 에 포함된 Image 객체를 설정합니다.
- `void setLayout (int layout)` — 레이아웃 지시어를 설정합니다.

## 필드 상세

### LAYOUT_DEFAULT

```java
public static final int LAYOUT_DEFAULT
```

**See Also:**
- `Constant Field Values`

### LAYOUT_LEFT

```java
public static final int LAYOUT_LEFT
```

**See Also:**
- `Constant Field Values`

### LAYOUT_RIGHT

```java
public static final int LAYOUT_RIGHT
```

**See Also:**
- `Constant Field Values`

### LAYOUT_CENTER

```java
public static final int LAYOUT_CENTER
```

**See Also:**
- `Constant Field Values`

### LAYOUT_NEWLINE_BEFORE

```java
public static final int LAYOUT_NEWLINE_BEFORE
```

**See Also:**
- `Constant Field Values`

### LAYOUT_NEWLINE_AFTER

```java
public static final int LAYOUT_NEWLINE_AFTER
```

**See Also:**
- `Constant Field Values`

### ImageItem

```java
public ImageItem(String label,
                 Image img,
                 int layout,
                 String altText)
```

- 주어진 레이블, 이미지, 레이아웃 지시어 및 대체 텍스트 문자열로 
새 `ImageItem`을 작성합니다. 
이 구성자를 호출하는 것은 다음을 호출하는 것과 같습니다.

`
 ImageItem(label, image, layout, altText, PLAIN); `

**Parameters:**
- `altText` - 이미지 위치에 사용할 수 있는 텍스트

**Throws:**
- `IllegalArgumentException` - `layout` 값이 
지시어의 올바른 조합이 아닌 경우

**See Also:**
- ``ImageItem(String, Image, int, String, int)``

### ImageItem

```java
public ImageItem(String label,
                 Image image,
                 int layout,
                 String altText,
                 int appearanceMode)
```

- 주어진 레이블, 이미지, 레이아웃 지시어, 대체 
텍스트 문자열 및 모양 모드로 새 `ImageItem` 객체를 작성합니다.
레이블이나 대체 텍스트는 존재하거나 `null`일 수 있습니다.

`appearanceMode` 
매개 변수(`모양 모드` 참조)를 
보면 응용 프로그램이 이 `ImageItem`에 사용할 플랫폼이 
무엇인지 알 수 있습니다. 하이퍼링크나 버튼같은 동작을 
제공하려면 응용 프로그램은 기본 `Command`를 
이 `ImageItem`과 연관시키고 
이 `ImageItem`에 
`ItemCommandListener`를 
추가해야 합니다.

`ImageItem`을 버튼으로 
사용하는 예는 다음과 같습니다.

```java
ImageItem imgItem = 
         new ImageItem("Default: ", img,     
                       Item.LAYOUT_CENTER, null,    
                       Item.BUTTON);    
     imgItem.setDefaultCommand(
         new Command("Set", Command.ITEM, 1); 
     // icl is ItemCommandListener   
     imgItem.setItemCommandListener(icl);
```

**Parameters:**
- `appearanceMode` - `ImageItem`의 모양 모드. 
``Item.PLAIN``, ``Item.HYPERLINK`` 또는 ``Item.BUTTON`` 중 하나

**Throws:**
- `IllegalArgumentException` - `appearanceMode`가 유효하지 않은 경우

**Since:**
- MIDP 2.0

### getImage

```java
public Image getImage()
```

**Returns:**
- `ImageItem`이 사용하는 이미지

**See Also:**
- ``setImage(javax.microedition.lcdui.Image)``

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - `ImageItem`의 
`Image` 또는 없는 경우 `null`

**See Also:**
- ``getImage()``

### getAltText

```java
public String getAltText()
```

**Returns:**
- 대체 텍스트 값 또는 없는 경우 `null`

**See Also:**
- ``setAltText(java.lang.String)``

### setAltText

```java
public void setAltText(String text)
```

**Parameters:**
- `text` - 새 대체 텍스트

**See Also:**
- ``getAltText()``

### getLayout

```java
public int getLayout()
```

**Overrides:**
- `getLayout` in class `Item`

**Returns:**
- 레이아웃 지시어 값의 조합

**See Also:**
- ``setLayout(int)``

### setLayout

```java
public void setLayout(int layout)
```

**Overrides:**
- `setLayout` in class `Item`

**Parameters:**
- `layout` - 레이아웃 지시어 값의 조합

**Throws:**
- `IllegalArgumentException` - `layout`의 값이 
레이아웃 지시어의 
유효한 조합이 아닌 경우

**See Also:**
- ``getLayout()``

### getAppearanceMode

```java
public int getAppearanceMode()
```

**Returns:**
- 모양 모드 값. ``Item.PLAIN``, ``Item.HYPERLINK`` 또는 
``Item.BUTTON`` 중 하나

**Since:**
- MIDP 2.0

## 생성자 상세

### ImageItem

```java
public ImageItem(String label,
                 Image img,
                 int layout,
                 String altText)
```

- 주어진 레이블, 이미지, 레이아웃 지시어 및 대체 텍스트 문자열로 
새 `ImageItem`을 작성합니다. 
이 구성자를 호출하는 것은 다음을 호출하는 것과 같습니다.

`
 ImageItem(label, image, layout, altText, PLAIN); `

**Parameters:**
- `altText` - 이미지 위치에 사용할 수 있는 텍스트

**Throws:**
- `IllegalArgumentException` - `layout` 값이 
지시어의 올바른 조합이 아닌 경우

**See Also:**
- ``ImageItem(String, Image, int, String, int)``

### ImageItem

```java
public ImageItem(String label,
                 Image image,
                 int layout,
                 String altText,
                 int appearanceMode)
```

- 주어진 레이블, 이미지, 레이아웃 지시어, 대체 
텍스트 문자열 및 모양 모드로 새 `ImageItem` 객체를 작성합니다.
레이블이나 대체 텍스트는 존재하거나 `null`일 수 있습니다.

`appearanceMode` 
매개 변수(`모양 모드` 참조)를 
보면 응용 프로그램이 이 `ImageItem`에 사용할 플랫폼이 
무엇인지 알 수 있습니다. 하이퍼링크나 버튼같은 동작을 
제공하려면 응용 프로그램은 기본 `Command`를 
이 `ImageItem`과 연관시키고 
이 `ImageItem`에 
`ItemCommandListener`를 
추가해야 합니다.

`ImageItem`을 버튼으로 
사용하는 예는 다음과 같습니다.

```java
ImageItem imgItem = 
         new ImageItem("Default: ", img,     
                       Item.LAYOUT_CENTER, null,    
                       Item.BUTTON);    
     imgItem.setDefaultCommand(
         new Command("Set", Command.ITEM, 1); 
     // icl is ItemCommandListener   
     imgItem.setItemCommandListener(icl);
```

**Parameters:**
- `appearanceMode` - `ImageItem`의 모양 모드. 
``Item.PLAIN``, ``Item.HYPERLINK`` 또는 ``Item.BUTTON`` 중 하나

**Throws:**
- `IllegalArgumentException` - `appearanceMode`가 유효하지 않은 경우

**Since:**
- MIDP 2.0

### getImage

```java
public Image getImage()
```

**Returns:**
- `ImageItem`이 사용하는 이미지

**See Also:**
- ``setImage(javax.microedition.lcdui.Image)``

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - `ImageItem`의 
`Image` 또는 없는 경우 `null`

**See Also:**
- ``getImage()``

### getAltText

```java
public String getAltText()
```

**Returns:**
- 대체 텍스트 값 또는 없는 경우 `null`

**See Also:**
- ``setAltText(java.lang.String)``

### setAltText

```java
public void setAltText(String text)
```

**Parameters:**
- `text` - 새 대체 텍스트

**See Also:**
- ``getAltText()``

### getLayout

```java
public int getLayout()
```

**Overrides:**
- `getLayout` in class `Item`

**Returns:**
- 레이아웃 지시어 값의 조합

**See Also:**
- ``setLayout(int)``

### setLayout

```java
public void setLayout(int layout)
```

**Overrides:**
- `setLayout` in class `Item`

**Parameters:**
- `layout` - 레이아웃 지시어 값의 조합

**Throws:**
- `IllegalArgumentException` - `layout`의 값이 
레이아웃 지시어의 
유효한 조합이 아닌 경우

**See Also:**
- ``getLayout()``

### getAppearanceMode

```java
public int getAppearanceMode()
```

**Returns:**
- 모양 모드 값. ``Item.PLAIN``, ``Item.HYPERLINK`` 또는 
``Item.BUTTON`` 중 하나

**Since:**
- MIDP 2.0

## 메서드 상세

### getImage

```java
public Image getImage()
```

**Returns:**
- `ImageItem`이 사용하는 이미지

**See Also:**
- ``setImage(javax.microedition.lcdui.Image)``

### setImage

```java
public void setImage(Image img)
```

**Parameters:**
- `img` - `ImageItem`의 
`Image` 또는 없는 경우 `null`

**See Also:**
- ``getImage()``

### getAltText

```java
public String getAltText()
```

**Returns:**
- 대체 텍스트 값 또는 없는 경우 `null`

**See Also:**
- ``setAltText(java.lang.String)``

### setAltText

```java
public void setAltText(String text)
```

**Parameters:**
- `text` - 새 대체 텍스트

**See Also:**
- ``getAltText()``

### getLayout

```java
public int getLayout()
```

**Overrides:**
- `getLayout` in class `Item`

**Returns:**
- 레이아웃 지시어 값의 조합

**See Also:**
- ``setLayout(int)``

### setLayout

```java
public void setLayout(int layout)
```

**Overrides:**
- `setLayout` in class `Item`

**Parameters:**
- `layout` - 레이아웃 지시어 값의 조합

**Throws:**
- `IllegalArgumentException` - `layout`의 값이 
레이아웃 지시어의 
유효한 조합이 아닌 경우

**See Also:**
- ``getLayout()``

### getAppearanceMode

```java
public int getAppearanceMode()
```

**Returns:**
- 모양 모드 값. ``Item.PLAIN``, ``Item.HYPERLINK`` 또는 
``Item.BUTTON`` 중 하나

**Since:**
- MIDP 2.0
