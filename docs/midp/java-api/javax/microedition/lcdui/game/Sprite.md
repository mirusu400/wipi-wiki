# Class Sprite

`package javax.microedition.lcdui.game`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.game.Layer
        |
        +--javax.microedition.lcdui.game.Sprite
```

## 설명

**extends Layer:**

Sprite는 Image에 저장되어 있는 여러 프레임 중 하나를 사용하여 
렌더링할 수 있는 기본 시각적 요소입니다. 
Sprite에 애니메이션 효과를 주기 위해 다양한 프레임을 표시할 수 있습니다. 
Sprite의 모양을 보다 다양화하기 위해 대칭 이동 및 회전 같은 
여러 변환을 적용할 수도 있습니다. 
모든 Layer 서브 클래스와 마찬가지로 Sprite의 위치를 변경할 수 있으며 표시하거나 표시하지 않을 수 있습니다.

### Sprite 프레임

Sprite를 렌더링하는 데 사용된 원시 프레임은 변경 가능하거나 
불가능한 단일 Image 객체에서 제공합니다. 
두 개 이상의 프레임이 사용되면 Image는 지정된 너비 및 
높이와 같은 크기를 가지는 일련의 프레임으로 나뉩니다. 
아래 그림에 표시된 대로 게임 개발자의 편의상 동일한 프레임 집합을 
여러 가지 다양한 배열로 저장할 수 있습니다.

각 프레임에는 고유 색인 번호가 할당됩니다. 
Image의 왼쪽 위 모서리에 있는 프레임에는 색인 0이 할당됩니다. 
그런 다음 나머지 프레임의 번호는 행 순서 위주로(첫 번째 행에 색인을 
할당한 다음 두 번째 행에 할당하는 식으로) 연속하여 매겨집니다. 
``getRawFrameCount()`` 메소드는 총 원시 프레임 수를 반환합니다.

### 프레임 시퀀스

Sprite의 프레임 시퀀스는 표시할 프레임의 정렬된 목록을 정의합니다. 
기본 프레임 시퀀스는 사용 가능한 프레임의 목록을 미러하므로 
시퀀스 색인과 해당 프레임 색인 사이에 직접 매핑됩니다. 
이는 또한 기본 프레임 시퀀스의 길이가 원시 프레임 수와 같다는 것을 
의미합니다. 예를 들어, Sprite에 4개의 프레임이 있는 경우 
기본 프레임 시퀀스는 {0, 1, 2, 3}입니다.

개발자는 프레임 시퀀스에서 현재 프레임을 수동으로 교환해야 합니다. 
이 작업은 ``setFrame(int)``, ``prevFrame()`` 또는 
``nextFrame()``을 호출하면 가능합니다. 
이러한 메소드는 항상 시퀀스 색인에서 작동해야 하며 
프레임 색인에서는 작동하지 않습니다. 
하지만 기본 프레임 시퀀스가 사용되는 경우 시퀀스 색인 및 프레임 색인은 상호 교환할 수 있습니다.

필요한 경우 Sprite에 대해 임의의 프레임 시퀀스가 
정의되어 있을 수 있습니다. 프레임 시퀀스는 한 개 이상의 요소를 포함해야 하며 
각 요소는 유효한 프레임 색인을 참조해야 합니다. 
개발자는 새 프레임 시퀀스를 정의하여 원하는 순서대로 편리하게 
Sprite 프레임을 표시할 수 있습니다. 즉, 프레임을 반복하거나 생략하거나 역순으로 표시할 수 있습니다.

예를 들어, 아래의 다이어그램은 모기에게 애니메이션 효과를 주기 위해 
특수 프레임 시퀀스를 사용하는 방법을 보여 줍니다. 
프레임 시퀀스는 모기가 날개를 세 번 퍼덕거린 다음 주기가 반복되기 전에 
일시 중지되도록 설계되어 있습니다.

디스플레이가 업데이트될 때마다

을 호출하면 
결과 애니메이션은 다음과 같습니다.

### 참조 픽셀

Sprite는 Layer의 서브 클래스로

,

,

등의 위치를 설정하고 검색할 수 있는 
다양한 메소드를 상속합니다. 이러한 메소드는 모두 Sprite 시각적 경계의 
왼쪽 위 모서리를 기준으로 위치를 정의합니다. 
하지만 경우에 따라, 특히 Sprite에 변환이 적용된 경우에는 프레임 내에서 
임의의 픽셀을 기준으로 Sprite의 위치를 정의하는 것이 보다 편리할 수 있습니다.

그러므로 Sprite에는 *참조 픽셀*의 개념이 포함됩니다. 
참조 픽셀은 ``defineReferencePixel(x,y)``을 
사용하여 Sprite의 변환되지 않은 
프레임에서 위치를 지정하여 정의됩니다. 
기본적으로 참조 픽셀은 프레임에서 (0,0)의 픽셀이 되도록 정의됩니다. 
필요한 경우 프레임 범위 밖에 있도록 
참조 픽셀을 정의할 수 있습니다.

이 예에서 참조 픽셀은 원숭이가 매달려 있는 
모습의 픽셀이 되도록 정의됩니다.

painter의 좌표계에서 참조 픽셀의 위치를 쿼리하기 위해
``getRefPixelX()``와 
``getRefPixelY()``를 사용할 수 있습니다. 
또한 개발자는 참조 픽셀이 painter 좌표계의 특정 위치에 나타나도록 
``setRefPixelPosition(x,y)``을 사용하여 
Sprite를 배치할 수 있습니다. 
이러한 메소드는 Sprite에 적용된 변환에도 자동으로 적용됩니다.

이 예에서 참조 픽셀의 위치는 나뭇가지 끝에 있는 점으로 설정됩니다. 
Sprite의 위치는 이 지점에 참조 픽셀이 표시되고 원숭이가 가지에 
매달려 있는 것처럼 보이도록 변경됩니다.

### Sprite 변환

Sprite에 다양한 변환이 적용될 수 있습니다. 
사용 가능한 변환에는 90도 배수로 회전 및 각 회전의 
미러된(수직 축 주위로) 버전이 포함됩니다. 
Sprite의 변환은

을 호출하여 설정됩니다.

변환이 적용되면 Sprite는 참조 픽셀이 painter의 좌표계에 고정되어 
표시되도록 자동으로 재배치됩니다. 
따라서 참조 픽셀은 효과적으로 변환 작업의 중심이 됩니다. 
참조 픽셀이 이동하지 않기 때문에

와

에서 반환하는 값은 그대로 있습니다. 
하지만

와

에서 
반환하는 값은 Sprite 왼쪽 위 모서리의 이동을 반영하도록 
변경될 수 있습니다.

원숭이 예를 다시 한 번 참조하면 90도 회전을 적용하는 경우 
참조 픽셀의 위치는 (48, 22)에 그대로 있습니다. 
따라서 원숭이가 가지에서 흔드는 것처럼 
보이도록 할 수 있습니다.

### Sprite 그리기

메소드를 사용하여 
언제든지 Sprite를 그릴 수 있습니다. 
Sprite에서 유지하는 현재 상태 정보(즉, 위치, 프레임, 표시 여부)에 따라 
Graphics 객체에 Sprite를 그립니다. 
Sprite를 지우는 것은 항상 Sprite 클래스 밖에 있는 코드를 통해 수행됩니다.

Sprite는 제조업체가 사용하고자 하는 기술을 사용하여 구현될 수 있습니다. 
예를 들어, 모든 Sprite에 대해 또는 특정 크기의 Sprite에 대해 
하드웨어 가속이 사용될 수도 있고 전혀 사용되지 않을 수도 있습니다.

일부 플랫폼에서 특정 Sprite 크기는 다른 크기보다 
더 효율적일 수 있습니다. 제조업체는 이와 같은 장치별 특성에 대한 
정보를 개발자에게 제공할지 여부를 선택할 수 있습니다.

**Since:**
- MIDP 2.0

## 필드 요약

- `static int TRANS_MIRROR` — Sprite가 수직 중심을 기준으로 대칭된 상태로 표시되게 합니다.
- `static int TRANS_MIRROR_ROT180` — Sprite가 수직 중심을 기준으로 대칭된 후 시계 방향으로 180도 회전하여 표시되게 합니다.
- `static int TRANS_MIRROR_ROT270` — Sprite가 수직 중심을 기준으로 대칭된 후 시계 방향으로 270도 회전하여 표시되게 합니다.
- `static int TRANS_MIRROR_ROT90` — Sprite가 수직 중심을 기준으로 대칭된 후 시계 방향으로 90도 회전하여 표시되게 합니다.
- `static int TRANS_NONE` — Sprite에 적용되는 변환은 없습니다.
- `static int TRANS_ROT180` — Sprite가 시계 방향으로 180도 회전하여 표시되게 합니다.
- `static int TRANS_ROT270` — Sprite가 시계 방향으로 270도 회전하여 표시되게 합니다.
- `static int TRANS_ROT90` — Sprite가 시계 방향으로 90도 회전하여 표시되게 합니다.

## 생성자 요약

- Sprite ( Image image) 제공된 Image를 사용하여 애니메이션 효과를 넣지 않은 
새로운 Sprite를 만듭니다.
- Sprite ( Image image,
 int frameWidth,
 int frameHeight) 제공된 Image에 포함된 프레임을 사용하여 애니메이션 효과를 넣을 
새 Sprite를 만듭니다.
- Sprite ( Sprite s) 다른 Sprite에서 새 Sprite를 만듭니다.

## 메서드 요약

- `boolean collidesWith ( Image image, int x, int y, boolean pixelLevel)` — 이 Sprite와 지정한 위치에 왼쪽 위 모서리가 있는 지정한 Image 사이의 충돌을 검사합니다.
- `boolean collidesWith ( Sprite s, boolean pixelLevel)` — 이 Sprite와 지정한 Sprite 사이의 충돌을 검사합니다.
- `boolean collidesWith ( TiledLayer t, boolean pixelLevel)` — 이 Sprite와 지정한 TiledLayer 사이의 충돌을 검사합니다.
- `void defineCollisionRectangle (int x, int y, int width, int height)` — 충돌 감지를 목적으로 사용되는 Sprite의 경계 직사각형을 정의합니다.
- `void defineReferencePixel (int x, int y)` — 이 Sprite의 참조 픽셀을 정의합니다.
- `int getFrame ()` — 프레임 시퀀스의 현재 색인을 가져옵니다.
- `int getFrameSequenceLength ()` — 프레임 시퀀스에서 요소의 수를 가져옵니다.
- `int getRawFrameCount ()` — 이 Sprite에 대한 원시 프레임의 수를 가져옵니다.
- `int getRefPixelX ()` — painter의 좌표계에서 Sprite 참조 픽셀의 수평 위치를 가져옵니다.
- `int getRefPixelY ()` — painter의 좌표계에서 Sprite 참조 픽셀의 수직 위치를 가져옵니다.
- `void nextFrame ()` — 프레임 시퀀스에서 다음 프레임을 선택합니다.
- `void paint ( Graphics g)` — Sprite를 그립니다.
- `void prevFrame ()` — 프레임 시퀀스에서 이전 프레임을 선택합니다.
- `void setFrame (int sequenceIndex)` — 프레임 시퀀스에서 현재 프레임을 선택합니다.
- `void setFrameSequence (int[] sequence)` — 이 Sprite의 프레임 시퀀스를 설정합니다.
- `void setImage ( Image img, int frameWidth, int frameHeight)` — Sprite의 프레임을 포함하는 Image를 변경합니다.
- `void setRefPixelPosition (int x, int y)` — Sprite의 참조 픽셀이 painter 좌표계의 (x,y)에 일치하도록 Sprite의 위치를 설정합니다.
- `void setTransform (int transform)` — 이 Sprite의 변환을 설정합니다.

## 필드 상세

### TRANS_NONE

```java
public static final int TRANS_NONE
```

**See Also:**
- `Constant Field Values`

### TRANS_ROT90

```java
public static final int TRANS_ROT90
```

**See Also:**
- `Constant Field Values`

### TRANS_ROT180

```java
public static final int TRANS_ROT180
```

**See Also:**
- `Constant Field Values`

### TRANS_ROT270

```java
public static final int TRANS_ROT270
```

**See Also:**
- `Constant Field Values`

### TRANS_MIRROR

```java
public static final int TRANS_MIRROR
```

**See Also:**
- `Constant Field Values`

### TRANS_MIRROR_ROT90

```java
public static final int TRANS_MIRROR_ROT90
```

**See Also:**
- `Constant Field Values`

### TRANS_MIRROR_ROT180

```java
public static final int TRANS_MIRROR_ROT180
```

**See Also:**
- `Constant Field Values`

### TRANS_MIRROR_ROT270

```java
public static final int TRANS_MIRROR_ROT270
```

**See Also:**
- `Constant Field Values`

### Sprite

```java
public Sprite(Image image)
```

- 제공된 Image를 사용하여 애니메이션 효과를 넣지 않은 
새로운 Sprite를 만듭니다. 
이 구성자는 `new Sprite(image, image.getWidth(), image.getHeight())`를 호출하는 것과 같은 기능을 합니다.

기본적으로 Sprite가 표시되며 왼쪽 위 모서리는 painter 좌표계의 (0,0)에 
위치합니다.

**Parameters:**
- `image` - Sprite의 단일 프레임으로 사용할 
`Image`

**Throws:**
- `NullPointerException` - `img`가 `null`인 경우

### Sprite

```java
public Sprite(Image image,
              int frameWidth,
              int frameHeight)
```

- 제공된 Image에 포함된 프레임을 사용하여 애니메이션 효과를 넣을 
새 Sprite를 만듭니다. 프레임은 `frameWidth`와 
`frameHeight`에 의해 지정된 치수를 갖는 동일한 크기여야 하며 
이미지에서 수평이나 수직으로 또는 격자 형태로 배치될 수 있습니다. 
소스 이미지의 너비는 프레임 
너비 정수의 배수가 되어야 하며 
소스 이미지의 높이는 프레임 
높이 정수의 배수가 되어야 합니다. 
``Layer.getWidth()``와 ``Layer.getHeight()``가 반환하는 값은 
Sprite의 현재 변환에 따라 프레임 너비와 프레임 높이를 반영합니다.

Sprite는 프레임 0에서 시작하여 원시 프레임에 해당하는 
기본 프레임 시퀀스를 가집니다. 
프레임 시퀀스는 ``setFrameSequence(int[])``로 수정할 수 있습니다.

기본적으로 Sprite가 표시되며 왼쪽 위 모서리는 painter의 좌표계 (0,0)에 
위치합니다.

**Parameters:**
- `frameHeight` - 개별 원시 프레임의 
`height`(픽셀 단위)

**Throws:**
- `IllegalArgumentException` - `image` 높이가 
`frameHeight`의 정수 배수가 아닌 경우

### Sprite

```java
public Sprite(Sprite s)
```

- 다른 Sprite에서 새 Sprite를 만듭니다.

소스 Sprite의 모든 인스턴스 속성(원시 프레임, 위치, 프레임 시퀀스, 
현재 프레임, 참조 점, 충돌 직사각형, 변환 및 표시 여부)은 
새 Sprite에 복제됩니다.

**Parameters:**
- `s` - 복사본을 만들 `Sprite`

**Throws:**
- `NullPointerException` - `s`가 `null`인 경우

### defineReferencePixel

```java
public void defineReferencePixel(int x,
                                 int y)
```

**Parameters:**
- `y` - 변환되지 않은 프레임의 왼쪽 모서리에 상대적인 참조 
픽셀의 수직 위치

**See Also:**
- ``setRefPixelPosition(int, int)``, 
``getRefPixelX()``, 
``getRefPixelY()``

### setRefPixelPosition

```java
public void setRefPixelPosition(int x,
                                int y)
```

**Parameters:**
- `y` - 참조 픽셀을 둘 수직 위치

**See Also:**
- ``defineReferencePixel(int, int)``, 
``getRefPixelX()``, 
``getRefPixelY()``

### getRefPixelX

```java
public int getRefPixelX()
```

**Returns:**
- 참조 픽셀의 수평 위치

**See Also:**
- ``defineReferencePixel(int, int)``, 
``setRefPixelPosition(int, int)``, 
``getRefPixelY()``

### getRefPixelY

```java
public int getRefPixelY()
```

**Returns:**
- 참조 픽셀의 수직 위치

**See Also:**
- ``defineReferencePixel(int, int)``, 
``setRefPixelPosition(int, int)``, 
``getRefPixelX()``

### setFrame

```java
public void setFrame(int sequenceIndex)
```

**Parameters:**
- `sequenceIndex` - 프레임 시퀀스에 있는 
원하는 항목의 색인

**Throws:**
- `IndexOutOfBoundsException` - `frameIndex`가 
현재 프레임 시퀀스(또는 기본 시퀀스의 원시 프레임 수)의 
길이보다 큰 경우

**See Also:**
- ``setFrameSequence(int[])``, 
``getFrame()``

### getFrame

```java
public final int getFrame()
```

**Returns:**
- 프레임 시퀀스의 현재 색인

**See Also:**
- ``setFrameSequence(int[])``, 
``setFrame(int)``

### getRawFrameCount

```java
public int getRawFrameCount()
```

**Returns:**
- 이 Sprite 원시 프레임의 수

**See Also:**
- ``getFrameSequenceLength()``

### getFrameSequenceLength

```java
public int getFrameSequenceLength()
```

**Returns:**
- 이 Sprite 프레임 시퀀스의 요소 수

**See Also:**
- ``getRawFrameCount()``

### nextFrame

```java
public void nextFrame()
```

**See Also:**
- ``setFrameSequence(int[])``, 
``prevFrame()``

### prevFrame

```java
public void prevFrame()
```

**See Also:**
- ``setFrameSequence(int[])``, 
``nextFrame()``

### paint

```java
public final void paint(Graphics g)
```

**Specified by:**
- `paint` in class `Layer`

**Parameters:**
- `g` - `Sprite`를 그릴 그래픽 객체

**Throws:**
- `NullPointerException` - `g`가 `null`인 경우

### setFrameSequence

```java
public void setFrameSequence(int[] sequence)
```

**Parameters:**
- `sequence` - 색인 배열, 여기서 각 정수는 
프레임 색인을 나타냅니다.

**Throws:**
- `IllegalArgumentException` - 배열의 요소 수가 
`1`보다 적은 경우

**See Also:**
- ``nextFrame()``, 
``prevFrame()``, 
``setFrame(int)``, 
``getFrame()``

### setImage

```java
public void setImage(Image img,
                     int frameWidth,
                     int frameHeight)
```

**Parameters:**
- `frameHeight` - 개별 원시 프레임의 높이(픽셀 단위)

**Throws:**
- `IllegalArgumentException` - 이미지 높이가 
`frameHeight`의 정수 배수가 아닌 경우

### defineCollisionRectangle

```java
public void defineCollisionRectangle(int x,
                                     int y,
                                     int width,
                                     int height)
```

**Parameters:**
- `height` - 충돌 직사각형의 높이

**Throws:**
- `IllegalArgumentException` - 지정한 
`width`나 `height`가 
`0`보다 작은 경우

### setTransform

```java
public void setTransform(int transform)
```

**Parameters:**
- `transform` - 이 `Sprite`에 필요한 변환

**Throws:**
- `IllegalArgumentException` - 요청한 
`transform`이 유효하지 않은 경우

**See Also:**
- ``TRANS_NONE``, 
``TRANS_ROT90``, 
``TRANS_ROT180``, 
``TRANS_ROT270``, 
``TRANS_MIRROR``, 
``TRANS_MIRROR_ROT90``, 
``TRANS_MIRROR_ROT180``, 
``TRANS_MIRROR_ROT270``

### collidesWith

```java
public final boolean collidesWith(Sprite s,
                                  boolean pixelLevel)
```

**Parameters:**
- `pixelLevel` - 픽셀 단위로 충돌을 테스트하려면 
`true`, 간단한 경계 검사를 
테스트하려면 `false`

**Returns:**
- 두 Sprite가 충돌한 경우 `true`, 
그렇지 않은 경우 `false`

**Throws:**
- `NullPointerException` - Sprite `s`가 `null`인 경우

### collidesWith

```java
public final boolean collidesWith(TiledLayer t,
                                  boolean pixelLevel)
```

**Parameters:**
- `pixelLevel` - 픽셀 단위로 충돌을 테스트하려면 
`true`, 비어있지 않은 셀에 대해 
간단한 경계 검사를 테스트하려면 `false`

**Returns:**
- 이 `Sprite`가 `TiledLayer`와 
충돌한 경우 `true` 그렇지 않은 경우 
`false`

**Throws:**
- `NullPointerException` - `t`가 `null`인 경우

### collidesWith

```java
public final boolean collidesWith(Image image,
                                  int x,
                                  int y,
                                  boolean pixelLevel)
```

**Parameters:**
- `pixelLevel` - 픽셀 단위로 충돌을 테스트하려면 
`true`, 단순한 경계 검사를 사용하여 
테스트하려면 `false`

**Returns:**
- `Sprite`가 `Image`와 
충돌한 경우 `true`, 그렇지 않은 경우 
`false`

**Throws:**
- `NullPointerException` - `image`가 
`null`인 경우

## 생성자 상세

### Sprite

```java
public Sprite(Image image)
```

- 제공된 Image를 사용하여 애니메이션 효과를 넣지 않은 
새로운 Sprite를 만듭니다. 
이 구성자는 `new Sprite(image, image.getWidth(), image.getHeight())`를 호출하는 것과 같은 기능을 합니다.

기본적으로 Sprite가 표시되며 왼쪽 위 모서리는 painter 좌표계의 (0,0)에 
위치합니다.

**Parameters:**
- `image` - Sprite의 단일 프레임으로 사용할 
`Image`

**Throws:**
- `NullPointerException` - `img`가 `null`인 경우

### Sprite

```java
public Sprite(Image image,
              int frameWidth,
              int frameHeight)
```

- 제공된 Image에 포함된 프레임을 사용하여 애니메이션 효과를 넣을 
새 Sprite를 만듭니다. 프레임은 `frameWidth`와 
`frameHeight`에 의해 지정된 치수를 갖는 동일한 크기여야 하며 
이미지에서 수평이나 수직으로 또는 격자 형태로 배치될 수 있습니다. 
소스 이미지의 너비는 프레임 
너비 정수의 배수가 되어야 하며 
소스 이미지의 높이는 프레임 
높이 정수의 배수가 되어야 합니다. 
``Layer.getWidth()``와 ``Layer.getHeight()``가 반환하는 값은 
Sprite의 현재 변환에 따라 프레임 너비와 프레임 높이를 반영합니다.

Sprite는 프레임 0에서 시작하여 원시 프레임에 해당하는 
기본 프레임 시퀀스를 가집니다. 
프레임 시퀀스는 ``setFrameSequence(int[])``로 수정할 수 있습니다.

기본적으로 Sprite가 표시되며 왼쪽 위 모서리는 painter의 좌표계 (0,0)에 
위치합니다.

**Parameters:**
- `frameHeight` - 개별 원시 프레임의 
`height`(픽셀 단위)

**Throws:**
- `IllegalArgumentException` - `image` 높이가 
`frameHeight`의 정수 배수가 아닌 경우

### Sprite

```java
public Sprite(Sprite s)
```

- 다른 Sprite에서 새 Sprite를 만듭니다.

소스 Sprite의 모든 인스턴스 속성(원시 프레임, 위치, 프레임 시퀀스, 
현재 프레임, 참조 점, 충돌 직사각형, 변환 및 표시 여부)은 
새 Sprite에 복제됩니다.

**Parameters:**
- `s` - 복사본을 만들 `Sprite`

**Throws:**
- `NullPointerException` - `s`가 `null`인 경우

### defineReferencePixel

```java
public void defineReferencePixel(int x,
                                 int y)
```

**Parameters:**
- `y` - 변환되지 않은 프레임의 왼쪽 모서리에 상대적인 참조 
픽셀의 수직 위치

**See Also:**
- ``setRefPixelPosition(int, int)``, 
``getRefPixelX()``, 
``getRefPixelY()``

### setRefPixelPosition

```java
public void setRefPixelPosition(int x,
                                int y)
```

**Parameters:**
- `y` - 참조 픽셀을 둘 수직 위치

**See Also:**
- ``defineReferencePixel(int, int)``, 
``getRefPixelX()``, 
``getRefPixelY()``

### getRefPixelX

```java
public int getRefPixelX()
```

**Returns:**
- 참조 픽셀의 수평 위치

**See Also:**
- ``defineReferencePixel(int, int)``, 
``setRefPixelPosition(int, int)``, 
``getRefPixelY()``

### getRefPixelY

```java
public int getRefPixelY()
```

**Returns:**
- 참조 픽셀의 수직 위치

**See Also:**
- ``defineReferencePixel(int, int)``, 
``setRefPixelPosition(int, int)``, 
``getRefPixelX()``

### setFrame

```java
public void setFrame(int sequenceIndex)
```

**Parameters:**
- `sequenceIndex` - 프레임 시퀀스에 있는 
원하는 항목의 색인

**Throws:**
- `IndexOutOfBoundsException` - `frameIndex`가 
현재 프레임 시퀀스(또는 기본 시퀀스의 원시 프레임 수)의 
길이보다 큰 경우

**See Also:**
- ``setFrameSequence(int[])``, 
``getFrame()``

### getFrame

```java
public final int getFrame()
```

**Returns:**
- 프레임 시퀀스의 현재 색인

**See Also:**
- ``setFrameSequence(int[])``, 
``setFrame(int)``

### getRawFrameCount

```java
public int getRawFrameCount()
```

**Returns:**
- 이 Sprite 원시 프레임의 수

**See Also:**
- ``getFrameSequenceLength()``

### getFrameSequenceLength

```java
public int getFrameSequenceLength()
```

**Returns:**
- 이 Sprite 프레임 시퀀스의 요소 수

**See Also:**
- ``getRawFrameCount()``

### nextFrame

```java
public void nextFrame()
```

**See Also:**
- ``setFrameSequence(int[])``, 
``prevFrame()``

### prevFrame

```java
public void prevFrame()
```

**See Also:**
- ``setFrameSequence(int[])``, 
``nextFrame()``

### paint

```java
public final void paint(Graphics g)
```

**Specified by:**
- `paint` in class `Layer`

**Parameters:**
- `g` - `Sprite`를 그릴 그래픽 객체

**Throws:**
- `NullPointerException` - `g`가 `null`인 경우

### setFrameSequence

```java
public void setFrameSequence(int[] sequence)
```

**Parameters:**
- `sequence` - 색인 배열, 여기서 각 정수는 
프레임 색인을 나타냅니다.

**Throws:**
- `IllegalArgumentException` - 배열의 요소 수가 
`1`보다 적은 경우

**See Also:**
- ``nextFrame()``, 
``prevFrame()``, 
``setFrame(int)``, 
``getFrame()``

### setImage

```java
public void setImage(Image img,
                     int frameWidth,
                     int frameHeight)
```

**Parameters:**
- `frameHeight` - 개별 원시 프레임의 높이(픽셀 단위)

**Throws:**
- `IllegalArgumentException` - 이미지 높이가 
`frameHeight`의 정수 배수가 아닌 경우

### defineCollisionRectangle

```java
public void defineCollisionRectangle(int x,
                                     int y,
                                     int width,
                                     int height)
```

**Parameters:**
- `height` - 충돌 직사각형의 높이

**Throws:**
- `IllegalArgumentException` - 지정한 
`width`나 `height`가 
`0`보다 작은 경우

### setTransform

```java
public void setTransform(int transform)
```

**Parameters:**
- `transform` - 이 `Sprite`에 필요한 변환

**Throws:**
- `IllegalArgumentException` - 요청한 
`transform`이 유효하지 않은 경우

**See Also:**
- ``TRANS_NONE``, 
``TRANS_ROT90``, 
``TRANS_ROT180``, 
``TRANS_ROT270``, 
``TRANS_MIRROR``, 
``TRANS_MIRROR_ROT90``, 
``TRANS_MIRROR_ROT180``, 
``TRANS_MIRROR_ROT270``

### collidesWith

```java
public final boolean collidesWith(Sprite s,
                                  boolean pixelLevel)
```

**Parameters:**
- `pixelLevel` - 픽셀 단위로 충돌을 테스트하려면 
`true`, 간단한 경계 검사를 
테스트하려면 `false`

**Returns:**
- 두 Sprite가 충돌한 경우 `true`, 
그렇지 않은 경우 `false`

**Throws:**
- `NullPointerException` - Sprite `s`가 `null`인 경우

### collidesWith

```java
public final boolean collidesWith(TiledLayer t,
                                  boolean pixelLevel)
```

**Parameters:**
- `pixelLevel` - 픽셀 단위로 충돌을 테스트하려면 
`true`, 비어있지 않은 셀에 대해 
간단한 경계 검사를 테스트하려면 `false`

**Returns:**
- 이 `Sprite`가 `TiledLayer`와 
충돌한 경우 `true` 그렇지 않은 경우 
`false`

**Throws:**
- `NullPointerException` - `t`가 `null`인 경우

### collidesWith

```java
public final boolean collidesWith(Image image,
                                  int x,
                                  int y,
                                  boolean pixelLevel)
```

**Parameters:**
- `pixelLevel` - 픽셀 단위로 충돌을 테스트하려면 
`true`, 단순한 경계 검사를 사용하여 
테스트하려면 `false`

**Returns:**
- `Sprite`가 `Image`와 
충돌한 경우 `true`, 그렇지 않은 경우 
`false`

**Throws:**
- `NullPointerException` - `image`가 
`null`인 경우

## 메서드 상세

### defineReferencePixel

```java
public void defineReferencePixel(int x,
                                 int y)
```

**Parameters:**
- `y` - 변환되지 않은 프레임의 왼쪽 모서리에 상대적인 참조 
픽셀의 수직 위치

**See Also:**
- ``setRefPixelPosition(int, int)``, 
``getRefPixelX()``, 
``getRefPixelY()``

### setRefPixelPosition

```java
public void setRefPixelPosition(int x,
                                int y)
```

**Parameters:**
- `y` - 참조 픽셀을 둘 수직 위치

**See Also:**
- ``defineReferencePixel(int, int)``, 
``getRefPixelX()``, 
``getRefPixelY()``

### getRefPixelX

```java
public int getRefPixelX()
```

**Returns:**
- 참조 픽셀의 수평 위치

**See Also:**
- ``defineReferencePixel(int, int)``, 
``setRefPixelPosition(int, int)``, 
``getRefPixelY()``

### getRefPixelY

```java
public int getRefPixelY()
```

**Returns:**
- 참조 픽셀의 수직 위치

**See Also:**
- ``defineReferencePixel(int, int)``, 
``setRefPixelPosition(int, int)``, 
``getRefPixelX()``

### setFrame

```java
public void setFrame(int sequenceIndex)
```

**Parameters:**
- `sequenceIndex` - 프레임 시퀀스에 있는 
원하는 항목의 색인

**Throws:**
- `IndexOutOfBoundsException` - `frameIndex`가 
현재 프레임 시퀀스(또는 기본 시퀀스의 원시 프레임 수)의 
길이보다 큰 경우

**See Also:**
- ``setFrameSequence(int[])``, 
``getFrame()``

### getFrame

```java
public final int getFrame()
```

**Returns:**
- 프레임 시퀀스의 현재 색인

**See Also:**
- ``setFrameSequence(int[])``, 
``setFrame(int)``

### getRawFrameCount

```java
public int getRawFrameCount()
```

**Returns:**
- 이 Sprite 원시 프레임의 수

**See Also:**
- ``getFrameSequenceLength()``

### getFrameSequenceLength

```java
public int getFrameSequenceLength()
```

**Returns:**
- 이 Sprite 프레임 시퀀스의 요소 수

**See Also:**
- ``getRawFrameCount()``

### nextFrame

```java
public void nextFrame()
```

**See Also:**
- ``setFrameSequence(int[])``, 
``prevFrame()``

### prevFrame

```java
public void prevFrame()
```

**See Also:**
- ``setFrameSequence(int[])``, 
``nextFrame()``

### paint

```java
public final void paint(Graphics g)
```

**Specified by:**
- `paint` in class `Layer`

**Parameters:**
- `g` - `Sprite`를 그릴 그래픽 객체

**Throws:**
- `NullPointerException` - `g`가 `null`인 경우

### setFrameSequence

```java
public void setFrameSequence(int[] sequence)
```

**Parameters:**
- `sequence` - 색인 배열, 여기서 각 정수는 
프레임 색인을 나타냅니다.

**Throws:**
- `IllegalArgumentException` - 배열의 요소 수가 
`1`보다 적은 경우

**See Also:**
- ``nextFrame()``, 
``prevFrame()``, 
``setFrame(int)``, 
``getFrame()``

### setImage

```java
public void setImage(Image img,
                     int frameWidth,
                     int frameHeight)
```

**Parameters:**
- `frameHeight` - 개별 원시 프레임의 높이(픽셀 단위)

**Throws:**
- `IllegalArgumentException` - 이미지 높이가 
`frameHeight`의 정수 배수가 아닌 경우

### defineCollisionRectangle

```java
public void defineCollisionRectangle(int x,
                                     int y,
                                     int width,
                                     int height)
```

**Parameters:**
- `height` - 충돌 직사각형의 높이

**Throws:**
- `IllegalArgumentException` - 지정한 
`width`나 `height`가 
`0`보다 작은 경우

### setTransform

```java
public void setTransform(int transform)
```

**Parameters:**
- `transform` - 이 `Sprite`에 필요한 변환

**Throws:**
- `IllegalArgumentException` - 요청한 
`transform`이 유효하지 않은 경우

**See Also:**
- ``TRANS_NONE``, 
``TRANS_ROT90``, 
``TRANS_ROT180``, 
``TRANS_ROT270``, 
``TRANS_MIRROR``, 
``TRANS_MIRROR_ROT90``, 
``TRANS_MIRROR_ROT180``, 
``TRANS_MIRROR_ROT270``

### collidesWith

```java
public final boolean collidesWith(Sprite s,
                                  boolean pixelLevel)
```

**Parameters:**
- `pixelLevel` - 픽셀 단위로 충돌을 테스트하려면 
`true`, 간단한 경계 검사를 
테스트하려면 `false`

**Returns:**
- 두 Sprite가 충돌한 경우 `true`, 
그렇지 않은 경우 `false`

**Throws:**
- `NullPointerException` - Sprite `s`가 `null`인 경우

### collidesWith

```java
public final boolean collidesWith(TiledLayer t,
                                  boolean pixelLevel)
```

**Parameters:**
- `pixelLevel` - 픽셀 단위로 충돌을 테스트하려면 
`true`, 비어있지 않은 셀에 대해 
간단한 경계 검사를 테스트하려면 `false`

**Returns:**
- 이 `Sprite`가 `TiledLayer`와 
충돌한 경우 `true` 그렇지 않은 경우 
`false`

**Throws:**
- `NullPointerException` - `t`가 `null`인 경우

### collidesWith

```java
public final boolean collidesWith(Image image,
                                  int x,
                                  int y,
                                  boolean pixelLevel)
```

**Parameters:**
- `pixelLevel` - 픽셀 단위로 충돌을 테스트하려면 
`true`, 단순한 경계 검사를 사용하여 
테스트하려면 `false`

**Returns:**
- `Sprite`가 `Image`와 
충돌한 경우 `true`, 그렇지 않은 경우 
`false`

**Throws:**
- `NullPointerException` - `image`가 
`null`인 경우
