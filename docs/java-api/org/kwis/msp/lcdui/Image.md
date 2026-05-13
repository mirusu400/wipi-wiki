# Class Image

`package org.kwis.msp.lcdui`

```
java.lang.Object
  |
  +--org.kwis.msp.lcdui.Image
```

## 설명

**extends Object:**

이미지를 나타내는 클래스입니다.
 
 이미지 클래스는 gif나 png등의 여러가지 이미지 포멧의 데이타로 부터
 생성할 수 있으며, 이전에 있는 이미지로부터 복사하여 생성할 수도 있습니다.
 이때 복사된 이미지에 한하여 `getGraphics`로 
 이미지의 내용의 변경이 가능합니다.

이미지는 변경이 가능한 이미지 변경이 가능하지 않은 이미지로 분류됩니다.
 변경이 가능한 이미지는 주로 프로그램에서 임의적으로 만드는 이미지 
 이며, 이미지 파일로 부터 생성하는 이미지는 변경이 가능하지 않은 이미지 
 입니다.

변경하기 위해서는 이미지를 복사하여 사용해야 합니다.
 코드는 다음과 같습니다.

```java
Image src; 
 
 src = Image.createImage("/test.gif"); 
 Image copy = Image.createImage(src); 
 Graphics g = copy.getGraphics(); 
 g.drawLine(0, 0, 10, 10);
```

복사할때에 애니메이션 이미지인 경우에는 이미지 복사가 되지 않으며, 
 mask된 이미지인 경우에 mask부분이 힌색으로 변환되어 복사되며,
 복사된 이미지는 더이상 mask를 가지고 있지 않습니다.

현재 이미지는 gif(animated), png, bmp(RLE압축포함) 포맷을 지원합니다.

## 생성자 요약

- Image ()

## 메서드 요약

- `static Image createImage (byte[] imagedata, int imageoffset, int imagelength)` — 지정된 이미지 데이타 어레이로 부터 이미지를 생성합니다.
- `static Image createImage ( Image image)` — 지정된 이미지를 복사해서 다른 편집이 가능한 이미지를 생성합니다.
- `static Image createImage (int width, int height)` — 지정된 높이와 폭의 편집 가능한 이미지를 생성합니다.
- `static Image createImage ( String name)` — 지정된 리소스의 이미지를 생성합니다.
- `Graphics getGraphics ()` — 이미지에 그릴수 있는 그래픽을 돌려줍니다.
- `int getHeight ()` — 이미지의 높이를 돌려줍니다.
- `int getWidth ()` — 이미지의 폭를 돌려줍니다.
- `boolean isAnimated ()` — Image가 Animation이 가능한지 여부를 돌려줍니다.
- `boolean isMutable ()` — 이미지의 편집 가능 여부를 돌려줍니다.
- `static Image loadImage ( String str, ImageObserver io)` — 문자열이 지정하는 자료로 부터 이미지를 읽어들입니다.
- `void play ( ImageObserver ob)` — 이미지의 움직임을 시작합니다.
- `void stop ()` — 애니메이션을 중지시킵니다.
- `static void stopImage ( ImageObserver io)` — ImageObserver 에 대응하는 이미지를 읽기를 중단 시킵니다.

## 생성자 상세

### Image

```java
public Image()
```

### createImage

```java
public static Image createImage(byte[] imagedata,
                                int imageoffset,
                                int imagelength)
```

**Parameters:**
- `imagelength` - 이미지 자료의 길이

**Returns:**
- 생성된 이미지

**Throws:**
- `ArrayIndexOutOfBoundsException` - `imageoffset`와
 `imagelength`가 지정하는 영역이 어레이의 유효한 영역을
 벗어 날때

### loadImage

```java
public static Image loadImage(String str,
                              ImageObserver io)
```

**Parameters:**
- `io` - 이미지 생성을 알려줄 `ImageObserver`

**Returns:**
- 새로 생성된 이미지; 초기에는 아무런 내용이 없음

**Throws:**
- `NullPointerException` - `str`이
 `null`인 경우.

**See Also:**
- ``ImageObserver.notify(org.kwis.msp.lcdui.Image, int)``

### createImage

```java
public static Image createImage(Image image)
```

**Parameters:**
- `image` - 복사할 이미지

**Returns:**
- 새로 만들어진 이미지

**Throws:**
- `NullPointerException` - `image`가
 `null`인 경우.

### createImage

```java
public static Image createImage(int width,
                                int height)
```

**Parameters:**
- `height` - 이미지의 높이.

**Throws:**
- `IllegalArgumentException` - `width`와 
 `height`가 0이하인 경우

### createImage

```java
public static Image createImage(String name)
                         throws IOException
```

**Parameters:**
- `name` - 자원 경로명

**Returns:**
- 이미지

**Throws:**
- `NullPointerException` - `name`이
 `null`인 경우.

**See Also:**
- ``Class.getResourceAsStream(java.lang.String)``

### getGraphics

```java
public Graphics getGraphics()
```

**Returns:**
- 이미지의 Graphics객체

### getHeight

```java
public int getHeight()
```

**Returns:**
- 이미지의 높이

### getWidth

```java
public int getWidth()
```

**Returns:**
- 이미지의 높이

### isMutable

```java
public boolean isMutable()
```

**Returns:**
- 편집 가능한지의 여부

### isAnimated

```java
public boolean isAnimated()
```

**Returns:**
- Animation이 가능한지의 여부

### play

```java
public void play(ImageObserver ob)
```

**Parameters:**
- `ob` - 이미지 Observer

**See Also:**
- ``ImageObserver``

### stop

```java
public void stop()
```

- 애니메이션을 중지시킵니다.

 애니메이션을 멈춥니다.
 이미지가 Animation Gif와 같은 이미지인 경우에 
 이 함수가 사용될 수 있습니다. Animation 이미지가 아닌 경우에 아무런
 작업도 하지 않습니다.

 이미지를 더이상 사용하지 않으면 
 이 함수를 불러서 이미지의 레퍼런스를 없애야 합니다.
 그렇지 않으면, 사용하지 않은 이미지 레퍼런스를 가지게 되므로, 
 메모리를 낭비할 수 있습니다.

### stopImage

```java
public static void stopImage(ImageObserver io)
```

**Parameters:**
- `io` - 삭제할 이미지에 대응하는 `ImageObserver`

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 메서드 상세

### createImage

```java
public static Image createImage(byte[] imagedata,
                                int imageoffset,
                                int imagelength)
```

**Parameters:**
- `imagelength` - 이미지 자료의 길이

**Returns:**
- 생성된 이미지

**Throws:**
- `ArrayIndexOutOfBoundsException` - `imageoffset`와
 `imagelength`가 지정하는 영역이 어레이의 유효한 영역을
 벗어 날때

### loadImage

```java
public static Image loadImage(String str,
                              ImageObserver io)
```

**Parameters:**
- `io` - 이미지 생성을 알려줄 `ImageObserver`

**Returns:**
- 새로 생성된 이미지; 초기에는 아무런 내용이 없음

**Throws:**
- `NullPointerException` - `str`이
 `null`인 경우.

**See Also:**
- ``ImageObserver.notify(org.kwis.msp.lcdui.Image, int)``

### createImage

```java
public static Image createImage(Image image)
```

**Parameters:**
- `image` - 복사할 이미지

**Returns:**
- 새로 만들어진 이미지

**Throws:**
- `NullPointerException` - `image`가
 `null`인 경우.

### createImage

```java
public static Image createImage(int width,
                                int height)
```

**Parameters:**
- `height` - 이미지의 높이.

**Throws:**
- `IllegalArgumentException` - `width`와 
 `height`가 0이하인 경우

### createImage

```java
public static Image createImage(String name)
                         throws IOException
```

**Parameters:**
- `name` - 자원 경로명

**Returns:**
- 이미지

**Throws:**
- `NullPointerException` - `name`이
 `null`인 경우.

**See Also:**
- ``Class.getResourceAsStream(java.lang.String)``

### getGraphics

```java
public Graphics getGraphics()
```

**Returns:**
- 이미지의 Graphics객체

### getHeight

```java
public int getHeight()
```

**Returns:**
- 이미지의 높이

### getWidth

```java
public int getWidth()
```

**Returns:**
- 이미지의 높이

### isMutable

```java
public boolean isMutable()
```

**Returns:**
- 편집 가능한지의 여부

### isAnimated

```java
public boolean isAnimated()
```

**Returns:**
- Animation이 가능한지의 여부

### play

```java
public void play(ImageObserver ob)
```

**Parameters:**
- `ob` - 이미지 Observer

**See Also:**
- ``ImageObserver``

### stop

```java
public void stop()
```

- 애니메이션을 중지시킵니다.

 애니메이션을 멈춥니다.
 이미지가 Animation Gif와 같은 이미지인 경우에 
 이 함수가 사용될 수 있습니다. Animation 이미지가 아닌 경우에 아무런
 작업도 하지 않습니다.

 이미지를 더이상 사용하지 않으면 
 이 함수를 불러서 이미지의 레퍼런스를 없애야 합니다.
 그렇지 않으면, 사용하지 않은 이미지 레퍼런스를 가지게 되므로, 
 메모리를 낭비할 수 있습니다.

### stopImage

```java
public static void stopImage(ImageObserver io)
```

**Parameters:**
- `io` - 삭제할 이미지에 대응하는 `ImageObserver`

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
