# Class Image

`package javax.microedition.lcdui`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.Image
```

## 설명

**extends Object:**

`Image` 클래스는 그래픽 이미지 데이터를 보관하는 데 
사용됩니다. `Image` 객체는 디스플레이 장치와는 
별도로 존재합니다. 이러한 객체는 오프스크린 메모리에만 
존재하며 응용 프로그램에서 명시적인 
명령(예: `Canvas`의 `paint()` 메소드)을 
실행하거나 활성화된 `Form` 화면 또는 
`Alert` 화면에 `Image` 객체를 
배치한 경우가 아니라면 
디스플레이에 표시되지 않습니다.

이미지는 작성 방법에 따라 *변경 가능한* 경우도 있고 
*변경 불가능한* 경우도 있습니다. 
변경 불가능한 이미지는 일반적으로 자원 번들, 
파일 또는 네트워크에서 이미지 데이터를 로드할 때 작성됩니다. 
이러한 이미지는 한 번 작성되면 수정될 수 없습니다. 
변경 가능한 이미지는 흰색 픽셀만 들어 있는 공백 이미지로 작성됩니다. 
특히 이를 위해 응용 프로그램에서는 `Image`의 
``getGraphics()``를 호출하는 방식으로 변경 가능한 이미지를 렌더링하여 `Graphics` 객체를 얻을 수 있습니다.

`Images`는 `Alert`, 
`Choice`, `Form` 또는 
`ImageItem` 객체에 배치될 수 있습니다. 
응용 프로그램에 알리지 않고 언제든지 디스플레이를 업데이트하려면 
고급 사용자 인터페이스 구현이 필요할 수도 있습니다. 
동작을 예측 가능하도록 하기 위해 고급 사용자 인터페이스 
객체는 이미지의 스냅샷 의미를 제공합니다. 
즉, 변경 가능한 이미지가 `Alert`, 
`Choice`, `Form` 또는 
`ImageItem` 객체에 배치된 경우 현재 내용으로 
스냅샷을 생성한 것과 같은 기능을 합니다. 
그런 다음 이 스냅샷은 고급 사용자 인터페이스 구성 요소의 
모든 후속 그리기에 사용됩니다. 
응용 프로그램이 이미지의 내용을 수정한 경우 수정된 내용을 표시하려면 
해당 이미지가 들어 있는 구성 요소를 업데이트해야 합니다(예:
`ImageItem.setImage` 호출).

변경 불가능한 이미지는 ``createImage`` 
메소드를 사용하여 변경 가능한 이미지에서 작성될 수 있습니다. 
다음과 유사한 기술을 사용하여 변경 불가능한 이미지의 
변경 가능한 사본을 작성할 수 있습니다.

Image source; // the image to be copied
 source = Image.createImage(...);
 Image copy = Image
 .createImage(source.getWidth(), source.getHeight());
 Graphics g = copy.getGraphics();
 g.drawImage(source, 0, 0, TOP|LEFT);

### 알파 처리

변경 가능한 이미지에 있는 모든 픽셀은 항상 완전 불투명입니다. 
변경 불가능한 이미지에는 완전 불투명 
픽셀`(alpha = 2bitdepth - 1)`, 
완전 투명 픽셀 (`alpha = 0`) 및 
반투명 픽셀(`0 < alpha <  2bitdepth - 1`)의 
조합이 들어 있을 수 있습니다. 
여기서 *bitdepth*는 
소스 데이터의 샘플당 비트 수입니다.

구현 시 변경 불가능 이미지에서 완전 불투명 픽셀과 
완전 투명 픽셀의 저장소, 처리 및 렌더링을 지원해야 합니다. 
소스 데이터에서 이미지를 작성할 때(PNG 파일에서건 ARGB 데이터 
배열에서건 상관없이) 소스 데이터의 완전 불투명 픽셀은 
새 이미지에서 항상 완전 불투명 픽셀이 되어야 하고 
소스 데이터의 완전 투명 픽셀은 새 이미지에서 항상 완전 
투명 픽셀이 되어야 합니다.

반투명 픽셀 데이터에 필요한 처리는 
렌더링 시 알파 블렌딩을 지원하는지에 따라 다릅니다. 
구현 시 알파 블렌딩을 지원하면 소스 데이터의 반투명 픽셀은 
새 이미지에서도 반투명 픽셀이 되어야 합니다. 
결과 알파 값은 플랫폼이 지원하는 반투명도 수준 수에 맞춰 
수정될 수 있습니다. 
``Display.numAlphaLevels()`` 메소드를 
참조하십시오. 구현 시 알파 블렌딩을 지원하지 않으면 
소스 데이터의 반투명 픽셀은 모두 새 이미지의 
완전 투명 픽셀로 교체되어야 합니다.

### PNG 이미지 형식

구현 시 *PNG (Portable Network Graphics) 사양, 
버전 1.0*에서 지정된 대로 PNG 형식으로 저장된 이미지를 
지원해야 합니다. MIDP를 준수하는 모든 구현은 *PNG 사양*이 
제공하는 최소 요구 사항 집합도 준수합니다. 
MIDP 구현은 또한 PNG 이미지 처리와 관련하여 
여기에 제공된 추가 요구 사항도 준수해야 합니다. 
여기에 나열된 요구 사항은 *PNG 사양*에 제공된 
권장 사항과 충돌할 경우 이보다 우선합니다.

PNG가 지정한 모든 '위험' 청크가 지원되어야 합니다. 
아래 단락은 이러한 위험 청크를 설명합니다.

IHDR 청크. MIDP 장치는 IHDR 청크에서 
다음 값을 처리해야 합니다.

- 모든 양수 값의 너비와 높이가 지원되지만 
매우 큰 이미지는 메모리 제약 조건 때문에 읽지 못할 수도 있습니다. 
결과 `Image` 객체의 치수는 PNG 이미지의 
치수와 일치해야 합니다. 즉, ``getWidth()`` 
및 ``getHeight()``가 반환한 값과 
렌더링된 너비 및 높이는 IHDR 청크에 지정된 너비 및 
높이와 동일해야 합니다.
- 이미지의 모양은 장치 화면의 기능에 따라 달라지지만 
모든 색상 유형이 지원됩니다. 알파 채널 데이터를 포함하는 
색상 유형이 지원됩니다.
- 색상 유형 `4` & `6`(각각 
알파가 있는 회색조 및 알파가 있는 RGB)의 경우 
알파 채널은 디코딩되어야 합니다. 알파 값이 0인 픽셀은 
투명으로 처리되어야 합니다. 
알파 값이 `255`(샘플당 비트가 `8`인 
이미지의 경우) 또는 `65535`(샘플당 비트가 `16`인 
이미지의 경우)인 픽셀은 불투명으로 처리 되어야 합니다. 
알파 블렌딩을 사용한 렌더링이 지원되면 중간 알파 값이 있는 
모든 픽셀은 결과 이미지로 이동되어야 합니다. 
알파 블렌딩이 지원되지 않으면 중간 알파 값이 있는 
모든 픽셀은 완전 투명 픽셀로 
교체되어야 합니다.
- 주어진 색상 유형에 대한 모든 비트 깊이 값이 지원됩니다.
- 압축 메소드 `0`(수축)은 
지원되는 유일한 압축 메소드입니다. 
이 메소드는 "zlib" 압축 방법을 활용하는 데 
이 방법은 jar 파일에도 사용됩니다. 
따라서 jar 디코딩과 PNG 디코딩 구현 간에 
압축 해제(팽창) 코드가 공유될 수도 있습니다. 
PNG 사양에서 언급되었듯이 압축된 데이터 스트림은 
내부적으로 압축된 데이터와 압축 해제된(원시) 데이터 모두로 
구성될 수 있습니다.
- 필터 메소드는 압축을 최적화하는 데 사용할 수 있는 
일련의 인코딩 방법을 표현합니다. 
PNG 사양은 현재 5개의 기본 필터 유형이 있는 적응 필터링 방법인 
단일 필터 메소드(메소드 `0`)를 정의합니다. 
필터링은 이미지 내에서 공간의 유사성을 이용하기 위한 
수축 알고리즘을 사용할 수 있으므로 최적의 압축을 위해 매우 중요합니다. 
그러므로, MIDP 장치는 필터 메소드 `0`으로 정의된 
5개 필터 유형 모두를 지원해야 합니다.
- MIDP 장치는 교차 메소드 `0`(None) 또는 
교차 메소드 `1`(Adam7)로 인코딩되는 PNG 이미지를 
읽어야 합니다. MIDP에서의 이미지 로딩은 동기적이며 이미지 
렌더링과 겹쳐질 수 없습니다. 따라서 응용 프로그램은 
교차 메소드 `1`을 사용하는 장점이 없습니다. 
이미 교차된 이미지를 사용하는 
개발자들에게 편의를 제공하고 
PNG와의 호환을 위해 교차된 이미지 디코딩을 
지원해야 합니다.

PLTE 청크. 팔레트 기반 이미지가 지원되어야 합니다.

IDAT 청크. 이미지 데이터는 필터 메소드 
`0`(None, Sub, Up, Average, Paeth)에 의해 
정의된 `5` 필터 유형 중 하나를 사용하여 
인코딩될 수 있습니다.

IEND 청크. 이미지가 유효한 것으로 간주되려면
이 청크가 있어야 합니다.

PNG는 PNG 이미지에 있을 수 있지만 이미지 
디코딩에는 중요하지 않은 몇몇 '보조' 청크를 정의합니다.

tRNS 청크. 모든 구현은 tRNS 청크를 지원해야 합니다. 
이 청크는 각 픽셀에 알파 채널 데이터를 제공하지 않고 
투명도를 구현하는 데 사용됩니다. 
색상 유형 `0`과 `2`의 경우 
특정 회색이나 RGB 값이 투명 픽셀이 되도록 정의됩니다. 
이런 경우에는 구현 시 이 값이 있는 픽셀을 
완전 투명으로 처리해야 합니다. 
픽셀 값 비교는 원본 샘플 깊이를 사용하여 실제 픽셀 값을 
기준으로 해야 합니다. 즉, 픽셀 값이 장치의 디스플레이 
기능을 반영하여 재배열되기 전에 이 비교를 수행해야 합니다. 
색상 유형 `3`(색인 색상)의 경우, 
색상 팔레트의 각 항목에 잠재적으로 `8` 
비트 알파 값이 제공됩니다. 
이런 경우에는 구현 시 알파 값이 `0`인 픽셀을 
완전 투명으로 처리해야 하며 알파 값이 `255`인 픽셀을 
완전 불투명으로 처리해야 합니다. 
알파 블렌딩을 사용한 렌더링이 지원되면 중간 알파 값이 
있는 모든 픽셀은 결과 이미지로 이동되어야 합니다. 
알파 블렌딩이 지원되지 않으면 중간 알파 값이 있는 모든 픽셀은 
완전 투명 픽셀로 교체되어야 합니다.

구현 시 다른 보조 청크를 지원하지 
*않을 수도*(반드시 지원해야 하는 것은 아님) 있습니다. 
지원되지 않는 보조 청크가 발생하면 모두 자동으로 
*무시해야 합니다.* 현재 정의된 선택적 보조 청크는 다음과 같습니다.

### 참조

*PNG(Portable Network Graphics) Specification, Version 1.0.* 
W3C Recommendation, October 1, 1996.
http://www.w3.org/TR/REC-png.html(RFC 2083, http://www.ietf.org/rfc/rfc2083.txt로도 다운로드 가능).

**Since:**
- MIDP 1.0

## 메서드 요약

- `static Image createImage (byte[] imageData, int imageOffset, int imageLength)` — 지정된 오프셋과 길이에 지정된 바이트 배열로 저장된 데이터에서 디코딩된 변경 불가능한 이미지를 작성합니다.
- `static Image createImage ( Image source)` — 소스 이미지에서 변경 불가능한 이미지를 작성합니다.
- `static Image createImage ( Image image, int x, int y, int width, int height, int transform)` — 지정된 대로 변환된 소스 이미지의 지정된 영역에서 픽셀 데이터를 사용하여 변경 불가능한 이미지를 작성합니다.
- `static Image createImage ( InputStream stream)` — InputStream 에서 얻은 디코딩된 이미지 데이터에서 변경 불가능한 이미지를 작성합니다.
- `static Image createImage (int width, int height)` — 오프스크린 그리기에 대한 새로운 변경 가능한 이미지를 작성합니다.
- `static Image createImage ( String name)` — 이름 지정된 자원에서 얻은 디코딩된 이미지 데이터에서 변경 불가능한 이미지를 작성합니다.
- `static Image createRGBImage (int[] rgb, int width, int height, boolean processAlpha)` — 0xAARRGGBB 로 지정된 ARGB 값 순서에서 변경 불가능한 이미지를 작성합니다.
- `Graphics getGraphics ()` — 이 이미지에 렌더링하는 새 Graphics 객체를 작성합니다.
- `int getHeight ()` — 이미지의 높이(단위: 픽셀)를 가져옵니다.
- `void getRGB (int[] rgbData, int offset, int scanlength, int x, int y, int width, int height)` — 이 이미지의 지정된 영역에서 ARGB 픽셀 데이터를 얻어 이를 제공된 정수 배열에 저장합니다.
- `int getWidth ()` — 이미지의 너비(단위: 픽셀)를 가져옵니다.
- `boolean isMutable ()` — 이미지가 변경 가능한지 확인합니다.

## 메서드 상세

### createImage

```java
public static Image createImage(int width,
                                int height)
```

**Parameters:**
- `height` - 새 이미지의 높이(단위: 픽셀)

**Returns:**
- 만든 이미지

**Throws:**
- `IllegalArgumentException` - `width` 
또는 `height`가 0 이하인 경우

### createImage

```java
public static Image createImage(Image source)
```

**Parameters:**
- `source` - 복사할 소스 이미지

**Returns:**
- 변경 불가능한 새 이미지

**Throws:**
- `NullPointerException` - `source`가 `null`인 경우

### createImage

```java
public static Image createImage(String name)
                         throws IOException
```

**Parameters:**
- `name` - 지원되는 이미지 형식 중 하나로 된 
이미지 데이터가 들어 있는 자원 이름

**Returns:**
- 만든 이미지

**Throws:**
- `IOException` - 자원이 존재하지 않거나, 
데이터를 로드할 수 없거나, 
이미지 데이터를 디코딩할 수 없는 경우

### createImage

```java
public static Image createImage(byte[] imageData,
                                int imageOffset,
                                int imageLength)
```

**Parameters:**
- `imageLength` - 배열에 있는 데이터 길이

**Returns:**
- 만든 이미지

**Throws:**
- `IllegalArgumentException` - `imageData`의 
형식이 잘못되었거나 디코딩할 수 없는 경우

### createImage

```java
public static Image createImage(Image image,
                                int x,
                                int y,
                                int width,
                                int height,
                                int transform)
```

**Parameters:**
- `transform` - 영역에 적용할 변환

**Returns:**
- 변경 불가능한 새 이미지

**Throws:**
- `IllegalArgumentException` - `transform`이 
유효하지 않은 경우

**Since:**
- MIDP 2.0

### createImage

```java
public static Image createImage(InputStream stream)
                         throws IOException
```

**Parameters:**
- `stream` - 지원되는 이미지 형식 중 하나로 된 이미지 
데이터가 들어 있는 자원 이름

**Returns:**
- 만든 이미지

**Throws:**
- `IOException` - 입출력 오류가 발생한 경우, 
이미지 데이터를 로드할 수 없는 경우 또는 이미지 데이터를 디코딩할 수 없는 경우

**Since:**
- MIDP 2.0

### getGraphics

```java
public Graphics getGraphics()
```

**Returns:**
- 이 이미지가 대상인 `Graphics` 객체

**Throws:**
- `IllegalStateException` - 이미지가 변경 불가능한 경우

### getWidth

```java
public int getWidth()
```

**Returns:**
- 이미지 너비

### getHeight

```java
public int getHeight()
```

**Returns:**
- 이미지 높이

### isMutable

```java
public boolean isMutable()
```

**Returns:**
- 이미지가 변경 가능한 경우 `true`, 
그렇지 않은 경우 `false`

### createRGBImage

```java
public static Image createRGBImage(int[] rgb,
                                   int width,
                                   int height,
                                   boolean processAlpha)
```

**Parameters:**
- `processAlpha` - `rgb`에 알파 채널이 있으면 
`true`, 모든 픽셀이 완전 불투명이면 
`false`

**Returns:**
- 만든 이미지

**Throws:**
- `ArrayIndexOutOfBoundsException` - `rgb`의 
길이가 ` width * height`보다 
작은 경우

**Since:**
- MIDP 2.0

### getRGB

```java
public void getRGB(int[] rgbData,
                   int offset,
                   int scanlength,
                   int x,
                   int y,
                   int width,
                   int height)
```

**Parameters:**
- `height` - 영역의 높이

**Throws:**
- `NullPointerException` - `rgbData`가 `null`인 경우

**Since:**
- MIDP 2.0
