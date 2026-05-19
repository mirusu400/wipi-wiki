---
title: "Class Graphics"
---

`package org.kwis.msp.lcdui`

```text
java.lang.Object
  |
  +--org.kwis.msp.lcdui.Graphics
```

## 설명

**extends Object:**

간단한 2차 기하학적인 도형을 그리는 기능을 제공합니다.

 텍스트나 이미지, 선, 사각형, 아크등을 그릴 수 있는 단순한 기능을 제공합니다.
 사각형과 아크는 특정 색상으로 칠해 질 수 있고, 사각형은 둥근 모서리를 
 가질수도 있습니다.

### 좌표 체계

화면의 좌측 상단이 (0, 0)이 되며, 아래로 y축이 증가하고, 오른쪽으로
 x축이 증가하는 좌표체계를 가집니다.
 그래픽객체에서 사용되는 모든 좌표는 `translate`함수에 
 의해서 변경 될 수 
 있는 원점을 가지는 좌표체계 하에 있게 됩니다.

### 앵커

앵커는 이미지나 폰트등을 출력시에 위치를 결정해주는 
 파라미터가 됩니다. 지정된 좌표에 객체의 어떤 부분을 위치시킬 
 것인지를 결정합니다.

폰트의 경우에는 
 앵커는 수평적으로는 `LEFT, HCENTER, RIGHT`중에 하나가 
 될 수 있으며,
 수직적으로는 `TOP, BASELINE, BOTTOM`이 될 수 있습니다.
 이 수평/수직적인 내용을 논리적 OR을 사용해서 앵커를 지정합니다.

 다음의 코드는 서로 같은 위치에 같은 내용을 출력하는 함수들의 
 예제 입니다.

```java
g.drawString(str, x, y, g.TOP|g.LEFT); 
 g.drawString(str, x + f.stringWidth(str)/2, y, g.TOP|g.HCENTER); 
 g.drawString(str, x + f.stringWidth(str), y, g.TOP|g.RIGHT); 
 g.drawString(str, x, 
       y + f.getBaselinePosition(), g.BASELINE|g.LEFT); 
 g.drawString(str, x + f.stringWidth(str)/2, 
       y + f.getBaselinePosition(), g.BASELINE|g.HCENTER); 
 g.drawString(str, x + f.stringWidth(str), 
       y + f.getBaselinePosition(), g.BASELINE|g.RIGHT); 
 g.drawString(str, x, 
       y + f.getHeight(), g.BOTTOM|g.LEFT); 
 g.drawString(str, x + f.stringWidth(str)/2, 
       y + f.getHeight(), g.BOTTOM|g.HCENTER); 
 g.drawString(str, x + f.stringWidth(str), 
       y + f.getHeight(), g.BOTTOM|g.RIGHT);
```

이미지의 경우에는 `BASELINE`대신에 `VCENTER`를 
 사용합니다.

 수평 앵커는 적어도 하나 지정이 되어야하며, 거기에 OR되는 수직 앵커는 
 지정되지 않아도 됩니다.

### 스트로크 스타일

스트로크 스타일은 `DOTTED`나 SOLID로 정의됩니다. 
 이 정의된 스타일은 `drawLine`, `drawArc`등에서만 
 적용이 되며`fillRect`같이 칠하기 함수에는 적용이되지 않습니다.

### 다른 그림 모드

스트로크 스타일 외에 Graphics에서 지원하는 
 그리기 모드가 있습니다. 하나는 XOR 모드로 그리기 이며,
 또하나는 투명정도를 지정합니다.
 ``setXORMode(boolean)``함수를 사용하면, 화면의 내용과 현재 출력하는 내용을
 XOR하여 출력할 수 있으며
 ``setAlpha(int)``함수를 사용하면, 화면의 내용과 현재 출력하는 내용을
 적절히 섞어서 출력할 수 있씁니다. ` g.setAlpha(255) `
 는 일반적으로 화면에 나타나며 ` g.setAlpha(0) `하면
 화면에 내용이 출력되지 않습니다. XOR모드나 Alpha모드로 출력시에
 속도가 저하 됩니다.

 
 모든 그래픽 오퍼레이션은 클리핑 영역에 영향을 받습니다.
 이 클리핑 영역 외에에는 오퍼레이션에 의해서 내용이 바뀌지 않습니다.
 클리핑 영역은 `Graphics`객체가 생성될때 사용된 
 화면이나 이미지의 크기보다는 클 수가 없습니다.

## 필드 요약

- `protected  int alpha`
- `static int BASELINE` — 앵커 위치를 문자열의 baseline으로 지정하는 상수.
- `static int BOTTOM` — 앵커의 위치를 문자나 이미지의 아래로 지정하는 상수.
- `protected  int clipX1`
- `protected  int clipX2`
- `protected  int clipY1`
- `protected  int clipY2`
- `static int DOTTED` — 도트 스트로크 스타일을 지정하는 상수.
- `protected Font ft`
- `protected  int gray`
- `static int HCENTER` — 앵커의 수평 위치를 문자나 이미지의 가운데로 지정하는 상수.
- `protected Image img`
- `static int LEFT` — 앵커의 수평 위치를 문자나 이미지의 왼쪽으로 지정하는 상수.
- `protected  int mode`
- `protected  int rgb`
- `static int RIGHT` — 앵커의 수평 위치를 문자나 이미지의 오른쪽으로 지정하는 상수.
- `static int SOLID` — 솔리드 스트로크 스타일을 지정하는 상수.
- `protected  int style`
- `static int TOP` — 앵커의 수직 위치를 문자나 이미지의 맨 위로 지정하는 상수.
- `protected  int transX`
- `protected  int transY`
- `static int VCENTER` — 앵커의 수직 위치를 이미지의 가운대로 지정하는 상수.

## 메서드 요약

- `void clipRect (int x, int y, int width, int height)` — 클리핑 영역을 지정된 사각형과 인터섹트(intersect)합니다.
- `void copyArea (int dx, int dy, int sx, int sy, int w, int h)` — 화면이나 이미지를 내부에서 내부로 복사합니다.
- `void drawArc (int x, int y, int width, int height, int startAngle, int arcAngle)` — 현재 그래픽이 지정하는 색상과 스트로크 스타일로 아크를 그립니다.
- `void drawChar (char character, int x, int y, int anchor)` — 그래픽 좌표계에서 현재 그래픽 개체가 가지고 있는 폰트와 색상으로 character가 지정하는 문자를 지정된 위치에 그려 줍니다.
- `void drawChars (char[] data, int offset, int length, int x, int y, int anchor)` — data가 가르키는 문자열의 일부를 현재 그래픽 개체가 가지고 있는 폰트와 색상으로 지정된 위치에 그려줍니다.
- `void drawImage ( Image img, int x, int y, int anchor)` — img가 가르키는 이미지를 지정된 위치에 그려줍니다.
- `void drawLine (int x1, int y1, int x2, int y2)` — 현재 그래픽이 가지고 있는 좌표체계의 두 점에을 연결하는 선을 그래픽 개체가 정의하는 색상과 스트로크 스타일로 그려줍니다.
- `void drawPolygon (int[] x, int[] y)` — 다각형을 그립니다.
- `void drawRect (int x, int y, int width, int height)` — 현재 그래픽이 지정하는 색상과 스트로크 스타일로 사각형을 그립니다.
- `void drawRoundRect (int x, int y, int width, int height, int arcWidth, int arcHeight)` — 현재 그래픽이 지정하는 색상과 스트로크 스타일로 모서리가 둥근 사각형을 그립니다.
- `void drawString ( String str, int x, int y, int anchor)` — 현재 그래픽이 지정하는 색상과 폰트로 문자열을 그립니다.
- `void drawSubstring ( String str, int offset, int len, int x, int y, int anchor)` — 현재 그래픽이 지정하는 색상과 폰트로 문자열의 일부를 그립니다.
- `byte[] encodeImage (int x, int y, int w, int h)` — 화면의 특정 영역을 BMP 포맷으로 인코딩합니다.
- `void fillArc (int x, int y, int width, int height, int startAngle, int arcAngle)` — 현재 그래픽이 지정하는 색상으로 아크를 칠합니다.
- `void fillRect (int x, int y, int width, int height)` — 현재 그래픽이 지정하는 색상으로 사각형을 칠합니다.
- `void fillRoundRect (int x, int y, int width, int height, int arcWidth, int arcHeight)` — 현재 그래픽이 지정하는 색상으로 모서리가 둥근 사각형을 칠합니다.
- `int getAlpha ()` — alpha 값을 가져옵니다.
- `int getBlueComponent ()` — 현재 지정된 색상의 파랑색값을 돌려줍니다.
- `int getClipHeight ()` — 클리핑 사각형의 높이를 돌려줍니다.
- `int getClipWidth ()` — 클리핑 사각형의 폭을 돌려줍니다.
- `int getClipX ()` — 클리핑 사각형의 그래픽 좌표계에서의 x축 좌표를 돌려줍니다.
- `int getClipY ()` — 클리핑 사각형의 그래픽 좌표계에서의 y축 좌표를 돌려줍니다.
- `int getColor ()` — 현재 지정된 색상을 돌려줍니다.
- `Font getFont ()` — 현재 지정된 폰트를 돌려줍니다.
- `int getGrayScale ()` — 현재 지정된 색상의 회색조 값을 얻어 옵니다.
- `int getGreenComponent ()` — 현재 지정된 색상의 녹색값을 돌려줍니다.
- `int getPixel (int x, int y)` — 특정 위치의 픽셀을 RGB 형태로 가지고 옵니다.
- `void getPixels (int x, int y, int w, int h, byte[] pixels, int offset, int bpl)` — 화면이나 이미지에서 특정 부분의 픽셀 값들을 가지고 옵니다.
- `int getRedComponent ()` — 현재 지정된 색상의 빨강색값을 돌려줍니다.
- `void getRGBPixels (int x, int y, int w, int h, int[] pixels, int offset, int bpl)` — 화면이나 이미지에서 특정 부분의 픽셀 값들을 가지고 옵니다.
- `int getStrokeStyle ()` — 선, 아크, 사각형 그리기에 사용되는 현재 지정된 스트로크 스타일을 돌려줍니다.
- `int getTranslateX ()` — 그래픽 좌표체계의 원점의 x축 좌표을 돌려줍니다.
- `int getTranslateY ()` — 그래픽 좌표체계의 원점의 y축 좌표을 돌려줍니다.
- `boolean isXORMode ()` — 설정된XOR모드를 리턴합니다
- `int getStrokeStyle ()`
