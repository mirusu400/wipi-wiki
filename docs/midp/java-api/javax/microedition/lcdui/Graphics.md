# Class Graphics

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Graphics
```

## 설명

**extends Object:**

단순한 2D 기하 렌더링 기능을 제공합니다.

텍스트, 이미지, 선, 직사각형 및 호에 대해 그리기 프리미티브가 제공됩니다. 
또한 단색으로 직사각형과 호를 채울 수 있습니다. 
직사각형에 둥근 모서리를 지정할 수도 있습니다.

색의 빨간색, 녹색, 파란색 구성 요소 
각각에 대해 `8`비트씩 `24`비트 
색상 모델이 제공됩니다. 모든 장치가 전체 `24`비트 
색상을 지원하는 것은 아니므로 
응용 프로그램에서 요청하는 색을 
장치에서 사용 가능한 색으로 매핑합니다. 
사용 가능한 색은 무엇인지, 
사용 가능한 회색 수준은 몇 개나 되는지 등 
장치 특성을 알 수 있는 기능이 
``Display`` 클래스에 제공됩니다. 
응용 프로그램은 요청한 색에 대해 디스플레이할 실제 색을 얻기 위해 
``getDisplayColor()``를 
사용할 수 있습니다. 
이로 인해 응용 프로그램은 장치 독립성을 
침해하지 않으면서도 
장치에 동작을 순응시킬 수 있습니다.

모든 렌더링 작업의 경우 *소스 대 대상* 규칙 
[Porter-Duff]를 사용하여 소스 픽셀은 항상 대상 픽셀과 결합됩니다. 
소스 픽셀과 래스터 ops 같은 대상 픽셀을 결합하기 위한 다른 방법은 
제공되지 않습니다.

텍스트, 선, 직사각형, 호 그리기 및 채우기 프리미티브의 경우 
소스 픽셀은 렌더링에 사용되는 그래픽 객체의 현재 색을 
나타내는 픽셀입니다. 
이 픽셀은 항상 완전 불투명으로 간주됩니다. 
항상 완전 불투명인 소스 픽셀을 사용하면 소스 대 대상 규칙은 
픽셀을 바꾸는 효과를 가지므로 대상 픽셀은 단순히 그래픽 객체의 
소스 픽셀로 바뀝니다.

``drawImage()`` 및 ``drawRegion()`` 메소드는 
그래픽 객체의 현재 색 대신 작업을 렌더링하는 데 
필요한 소스로 이미지를 사용합니다. 
이 상황에서 소스 대 대상 규칙의 등록 정보는 다음과 같습니다. 
소스의 완전 불투명 픽셀은 대상 픽셀로 바꿔야 하고 소스의 투명 픽셀은 
대상 픽셀을 변경되지 않은 상태로 두어야 하며 
소스의 반투명 픽셀은 대상 픽셀과 알파 블렌딩되어야 합니다. 
반투명 픽셀을 알파 블렌딩해야 합니다. 
구현 시 알파 블렌딩을 지원하지 않는 경우 이미지를 만들 때 
이미지 소스 데이터에서 반투명도를 모두 제거해야 합니다. 
자세한 내용은 `알파 처리`를 참조하십시오.

모든 그래픽 렌더링의 대상은 전체가 
완전 불투명 픽셀로 구성되는 것으로 
간주됩니다. 소스 대 대상 규칙의 특성은 완전 불투명 대상 픽셀을 갖는 
픽셀을 합성하면 그 결과 완전 불투명 대상 픽셀이 반드시 생긴다는 것입니다. 
이는 전체 및 부분 투명성을 렌더링 작업의 소스로만 사용될 수 있는 
변경할 수 없는 이미지로 한정하는 효과가 있습니다.

그래픽은 디스플레이나 오프스크린 
이미지 버퍼로 직접 렌더링될 수 있습니다. 
렌더링된 그래픽의 대상은 그래픽 객체의 출처에 따라 달라집니다. 
디스플레이에 렌더링할 그래픽 객체는 `Canvas` 객체의 
``paint()`` 메소드에 전달됩니다. 
이는 대상이 디스플레이인 그래픽 객체를 얻을 수 있는 유일한 방법입니다. 
또한 응용 프로그램은 `paint()` 
메소드가 지속되는 동안만 
이 그래픽 객체를 사용하여 그릴 수 있습니다.

오프스크린 이미지 버퍼를 렌더링할 
그래픽 객체는 원하는 이미지에서 
``getGraphics()`` 메소드를 호출하여 
얻을 수 있습니다. 이렇게 얻은 그래픽 객체는 
응용 프로그램에 의해 무기한 보류되며 
이 그래픽 객체에 대해 언제든지 요청을 
실행할 수 있습니다.

기본 좌표계의 원점은 대상의 왼쪽 위 모서리에 있습니다. 
X축 방향은 오른쪽으로 양수이며 Y축 방향은 아래쪽으로 양수입니다. 
응용 프로그램은 좌표계의 수평 및 
수직 거리가 실제 장치 디스플레이에서 
같은 거리를 나타낸다고 가정합니다. 
즉, 픽셀은 정사각형입니다. 좌표계 원점을 변환하기 
위한 기능이 제공됩니다. 
모든 좌표는 정수로 지정됩니다.

좌표계는 픽셀 자체가 아닌 픽셀 사이의 위치를 나타냅니다. 
그러므로 디스플레이의 왼쪽 위 모서리에 있는 
첫 번째 픽셀은 좌표 `(0,0), (1,0), (0,1), (1,1)` 범위의 
정사각형에 놓입니다.

이러한 정의 하에 채우기 작업의 의미는 명확합니다. 
좌표 격자 선은 픽셀 사이에 놓이므로 채우기 작업은 
전체적으로 작업 좌표계에 의해 범위 설정된 영역 내에 놓인 
픽셀에 영향을 줍니다. 예를 들어, 다음 작업은

g.fillRect(0, 0, 3, 2)

정확히 6개의 픽셀을 그립니다. 
위의 예와 다음에 나오는 모든 예에서 변수 `g`가 
`Graphics` 객체에 대한 참조를 
포함한다고 가정합니다.

글꼴의 각 문자에는 문자의 모양을 형성하는 일련의 
픽셀 집합이 포함됩니다. 문자를 그릴 때 
문자의 모양을 형성하는 픽셀은 
`Graphics` 
객체의 현재 색으로 채워지며 
문자 모양의 일부가 아닌 픽셀은 변경되지 않습니다. 
텍스트 그리기 호출 ``drawChar()``, 
``drawChars()``, 
``drawString()`` 
및 ``drawSubstring()``은 텍스트를 
모두 이 방식으로 그립니다.

``setStrokeStyle()`` 메소드에서 
설정한 대로 선, 호, 직사각형 및 둥근 직사각형은 
`SOLID`나 `DOTTED` 입력 스타일 중 
하나로 그릴 수 있습니다. 입력 스타일은 채우기, 텍스트 및 이미지 작업에는 
영향을 미치지 않습니다.

`SOLID` 입력 스타일의 경우 그리기 작업은 
바로 아래의 픽셀을 지정한 좌표의 오른쪽까지 채우는 
픽셀 하나 너비의 펜으로 수행됩니다. 
그려진 선은 선의 양쪽 끝점에 있는 픽셀까지 사용합니다. 
따라서 다음 작업으로

g.drawLine(0, 0, 0, 0);

정확히 한 픽셀, 디스플레이의 왼쪽 위 모서리에 있는 
첫 번째 픽셀을 그립니다.

`DOTTED` 입력 스타일의 그리기 작업은 
`SOLID` 입력 스타일에서 
사용한 픽셀의 일부를 사용합니다. 
점의 빈도와 길이는 구현별로 다릅니다. 
선과 호의 끝점이 그려지지 않거나 직사각형의 모서리 점이 
그려지지 않을 수도 있습니다. 
현재 색을 사용하여 점을 칠하고 
점 사이의 공간은 그대로 둡니다.

좌표계의 아티팩트는 채우기 작업에 의해 영향을 받는 영역이 같은 좌표에서 그리기 
작업에 의해 영향을 받는 영역과 약간 다른 것입니다. 
예를 들어 다음 작업을 참조하십시오.

g.fillRect(x, y, w, h); // 1
 g.drawRect(x, y, w, h); // 2

명령문 (1)은 `w` 픽셀 너비와 
`h` 픽셀 높이인 직사각형을 채웁니다. 
명령문 (2)는 왼쪽과 위쪽 모서리가 명령문 (1)에서 
채운 영역 내에 있는 직사각형을 그립니다. 
하지만 아래쪽과 오른쪽 모서리는 채워진 영역 밖의 한 픽셀에 놓입니다. 
이는 반직관적이지만 위의 명령문 (2)와 동일한 효과를 갖는

g.drawLine(x, y, x+w, y);
 g.drawLine(x+w, y, x+w, y+h);
 g.drawLine(x+w, y+h, x, y+h);
 g.drawLine(x, y+h, x, y);

불변형을 보존합니다.

`drawLine()`과 `drawArc()`에 의해 
그려지는 정확한 픽셀은 지정되어 있지 않습니다. 
채우기 작업에서 사용하는 픽셀은 해당 그리기 작업에서 사용하는 
픽셀에 바로 인접해 있거나 정확하게 겹쳐야 합니다. 
채우기 작업 시에는 채우기 영역과 해당 그리기 작업으로 
다루는 픽셀 사이에 간격을 두지 말아야 하며 
해당 그리기 작업에 의해 
범위가 설정된 영역 밖에 있는 픽셀을 사용하면 안 됩니다.

### 자르기

클립은 그래픽 렌더링 작업으로 수정할 수 있는 
`Graphics` 객체의 대상 
픽셀 집합입니다.

`Graphics` 객체마다 한 개의 클립이 있습니다. 
그래픽 작업으로는 픽셀은 클립 내에 놓인 픽셀만 수정할 수 있습니다. 
해당 클립의 범위를 벗어난 픽셀은 그래픽 작업으로 수정되지 않습니다.

현재 클립을 지정된 직사각형과 교차시키고 명확하게 설정하기 위한 
작업이 제공됩니다. 응용 프로그램은 
현재 좌표계에 상대적인 좌표를 
사용하는 클립 직사각형을 제공하여 클립을 지정할 수 있습니다.

너비나 높이가 0이나 음수인 클립 직사각형을 지정하는 것은 유효합니다. 
이 경우 클립은 비어 있는 것으로 간주됩니다. 
즉, 클립에 포함된 픽셀이 없습니다. 
따라서 이러한 클립에서 그래픽 작업이 실행된 경우 
어떤 픽셀도 수정되지 않습니다.

대상의 범위를 벗어나 확장하거나 전체적으로 해당 범위 밖에 있는 
클립 직사각형을 지정하는 것은 유효합니다. 
대상의 범위 밖에 있는 픽셀은 없으며 대상의 범위 밖에 있는 
클립 직사각형의 영역은 무시됩니다. 
대상과 지정된 클립 직사각형 모두에 놓이는 
픽셀만 클립의 일부로 간주됩니다.

``translate()`` 
같은 좌표계 작업은 클립을 수정하지 않습니다. 
`Graphics` 객체 좌표계를 변경하지 않고 
`setClip`에 전달하는 경우 
``getClipX()``, 
``getClipY()``, 
``getClipWidth()`` 및 
``getClipHeight()`` 메소드는 
클립에서 동일한 픽셀 집합을 만드는 
직사각형을 반환해야 합니다. 
`getClip` 메소드 계열에서 
반환된 직사각형은 
``setClip()``에서 
요청된 클립 직사각형과 다를 수 있습니다. 
이러한 내용은 좌표계가 변경되었거나 구현 시 
클립 직사각형이 `Graphics` 객체의 
대상 경계와 교차하도록 선택한 경우 
발생할 수 있습니다.

그래픽 작업이 클립의 영향을 받은 경우 해당 작업으로 
다룬 픽셀은 클립이 작업에 
영향을 미치지 않은 것처럼 
다뤄지는 픽셀과 같아야 합니다. 예를 들어, 
직사각형 `(cx, cy, cw, ch)`에 의해 표현되는 클립과 
이 직사각형 밖에 있는 점 `(x1, y1)`, 그리고 
이 직사각형 내에 있는 점 `(x2, y2)`를 가정합니다. 
다음 코드 조각에서

g.setClip(0, 0, canvas.getWidth(),
 canvas.getHeight());
 g.drawLine(x1, y1, x2, y2); // 3
 g.setClip(cx, cy, cw, ch);
 g.drawLine(x1, y1, x2, y2); // 4

명령문 (4)의 터치를 받는 픽셀은 명령문 (3)의 터치를 받는 
`(cx, cy, cw, ch)` 내의 픽셀과 동일해야 합니다.

### 앵커 포인트

텍스트의 그리기는 "앵커 포인트"를 기반으로 합니다. 
앵커 포인트는 텍스트를 놓을 때 필요한 계산량을 최소화하기 위해 사용됩니다. 
예를 들어, 텍스트 일부를 가운데 맞추기 위해 
응용 프로그램은 `stringWidth()`나 
`charWidth()`를 호출하여 너비를 구한 다음 빼기와 
나누기의 조합을 수행하여 적절한 
위치를 계산해야 합니다. 
텍스트를 그리기 위한 메소드는 
다음과 같이 정의되어 있습니다.

이 메소드는 앵커 포인트가

에 있는 
현재 글꼴을 사용하여 텍스트를 
현재 색으로 그립니다. 
앵커 포인트의 정의는 비트

연산자를 사용하여 
수직 상수

중 
하나와 결합된 수평 상수

중 
하나가 되어야 합니다. 
0은 앵커 포인트의 값으로 사용될 수도 있습니다. 
앵커 포인트 값에 0을 사용하면

를 
사용하는 것과 같은 결과가 됩니다.

텍스트의 수직 가운데 맞춤은 지정하기 어렵고 구현하기 
번거로워 유용하지 않으므로 지정하지 않습니다. 
따라서 `VCENTER` 값은 
텍스트 그리기 호출의 앵커 
포인트 매개 변수에서 허용되지 않습니다.

`(x, y)` 위치에 비례하는 
텍스트 경계 상자의 실제 위치는 앵커 포인트에 의해 결정됩니다. 
이러한 앵커 포인트는 경계 상자의 외곽 모서리를 따라 
이름이 지정된 위치에서 발생합니다. 
따라서 `f`가 `g`의 현재 
글꼴(`g.getFont()`에서 반환)인 경우 
다음 호출은 모두 동일한 결과를 
반환합니다.

g.drawString(str, x, y, TOP|LEFT);
 g.drawString(str, x + f.stringWidth(str)/2, y, TOP|HCENTER);
 g.drawString(str, x + f.stringWidth(str), y, TOP|RIGHT);

 g.drawString(str, x,
 y + f.getBaselinePosition(), BASELINE|LEFT);
 g.drawString(str, x + f.stringWidth(str)/2,
 y + f.getBaselinePosition(), BASELINE|HCENTER);
 g.drawString(str, x + f.stringWidth(str),
 y + f.getBaselinePosition(), BASELINE|RIGHT);

 drawString(str, x,
 y + f.getHeight(), BOTTOM|LEFT);
 drawString(str, x + f.stringWidth(str)/2,
 y + f.getHeight(), BOTTOM|HCENTER);
 drawString(str, x + f.stringWidth(str),
 y + f.getHeight(), BOTTOM|RIGHT);

텍스트 그리기의 경우 글꼴 설계자가 지정한 문자간 간격 
및 줄간 간격(선행)은 ``Font`` 클래스의 
``stringWidth()``와 
``getHeight()`` 
호출에서 반환한 값의 일부로 
포함됩니다. 예를 들어, 다음 코드의 경우

// (5)
 g.drawString(string1+string2, x, y, TOP|LEFT);

 // (6)
 g.drawString(string1, x, y, TOP|LEFT);
 g.drawString(string2, x + f.stringWidth(string1), y, TOP|LEFT);

코드 조각 (5)와 (6)은 같지는 않더라도 유사한 방식으로 작동합니다. 
이러한 내용은 `f.stringWidth()`에 문자간 간격이 
포함되기 때문에 발생합니다. 시스템에서 글꼴 돌출을 지원하는 경우 
정확한 간격은 이러한 호출에 따라 다를 수 있습니다.

마찬가지로 다음 줄의 Y 위치에 글꼴 높이만 추가하면 
합리적으로 수직 간격이 정해질 수 있습니다. 
예를 들면 다음과 같습니다.

g.drawString(string1, x, y, TOP|LEFT);
 g.drawString(string2, x, y + f.fontHeight(), TOP|LEFT);

적절한 줄간 간격으로 별도의 줄에서 `string1`과 
`string2`를 그립니다.

그려지는 문자열의 `stringWidth()`와 
글꼴의 `fontHeight()`는 텍스트 일부의 
경계 상자 크기를 정의합니다. 
위에서 설명한 대로 이 상자에는 줄간 
간격 및 문자간 간격이 포함됩니다. 
구현 시 그려진 문자에 실제로 속하도록 픽셀의 아래와 오른쪽에 
이 공간을 두어야 합니다. 
그래픽을 텍스트 가까이 배치하려는 
응용 프로그램은 문자열의 아래쪽과 오른쪽에 공간이 있고 
문자열의 위쪽과 왼쪽에는 공간이 
*없다*고 가정합니다.

또한 이미지 배치를 위해 앵커 포인트가 사용됩니다. 
텍스트 그리기와 마찬가지로 이미지의 앵커 포인트는 
그래픽 요청에서 주어진 `(x,y)` 위치에 
배치될 대상의 경계 직사각형에서 점을 지정합니다. 
텍스트와 달리 이미지의 수직 가운데 맞춤은 잘 정의되어 있으므로 
`VCENTER` 값은 
이미지 그리기 요청의 앵커 포인트 
매개 변수 내에서 사용될 수 있습니다. 
이미지에는 기준선의 의미가 없으므로 `BASELINE` 값은 
이미지 그리기 요청의 앵커 포인트 매개 변수 내에서 
사용되지 않을 수 있습니다.

### 참조

**Porter-Duff:**
- Porter, T., T. Duff 공저. "Compositing Digital Images." 
*Computer Graphics V18 N3 (SIGGRAPH 1984)*, p. 253-259.

**Since:**
- MIDP 1.0

## 필드 요약

- `static int BASELINE` — 텍스트의 기준선에 앵커 포인트를 배치하기 위한 상수.
- `static int BOTTOM` — 텍스트나 이미지의 아래에 텍스트와 이미지의 앵커 포인트를 배치하기 위한 상수.
- `static int DOTTED` — DOTTED 입력 스타일의 상수.
- `static int HCENTER` — 앵커 포인트 주위로 텍스트와 이미지를 가로로 가운데 맞추기 위한 상수.
- `static int LEFT` — 텍스트나 이미지의 왼쪽에 텍스트와 이미지의 앵커 포인트를 배치하기 위한 상수.
- `static int RIGHT` — 텍스트나 이미지의 오른쪽에 텍스트와 이미지의 앵커 포인트를 배치하기 위한 상수.
- `static int SOLID` — SOLID 입력 스타일에 대한 상수.
- `static int TOP` — 텍스트나 이미지 위에 텍스트와 이미지의 앵커 포인트를 배치하기 위한 상수.
- `static int VCENTER` — 앵커 포인트 주위에 이미지를 세로로 가운데 맞추기 위한 상수.

## 메서드 요약

- `void clipRect (int x, int y, int width, int height)` — 현재 클립을 지정한 직사각형과 교차 시킵니다.
- `void copyArea (int x_src, int y_src, int width, int height, int x_dest, int y_dest, int anchor)` — 직사각형 영역 (x_src, y_src, width, height) 의 내용을 앵커에 의해 식별된 앵커 포인트가 (x_dest, y_dest) 에 있는 대상 영역으로 복사합니다.
- `void drawArc (int x, int y, int width, int height, int startAngle, int arcAngle)` — 지정한 직사각형을 덮는 원형 호나 타원형 호의 윤곽을 현재 색과 입력 스타일을 사용하여 그립니다.
- `void drawChar (char character, int x, int y, int anchor)` — 지정한 문자를 현재 글꼴과 색을 사용하여 그립니다.
- `void drawChars (char[] data, int offset, int length, int x, int y, int anchor)` — 지정한 문자를 현재 글꼴과 색을 사용하여 그립니다.
- `void drawImage ( Image img, int x, int y, int anchor)` — 지정한 이미지를 앵커 포인트를 사용하여 그립니다.
- `void drawLine (int x1, int y1, int x2, int y2)` — 현재 색과 입력 스타일을 사용하여 (x1,y1) 과 (x2,y2) 좌표 사이에서 선을 그립니다.
- `void drawRect (int x, int y, int width, int height)` — 지정한 직사각형의 윤곽을 현재 색과 입력 스타일을 사용하여 그립니다.
- `void drawRegion ( Image src, int x_src, int y_src, int width, int height, int transform, int x_dest, int y_dest, int anchor)` — 지정한 소스 이미지의 영역을, 선택한 변환 함수를 사용하여 이미지 데이터를 변환(회전 및 반사)하여 대상 내의 위치로 복사합니다.
- `void drawRGB (int[] rgbData, int offset, int scanlength, int x, int y, int width, int height, boolean processAlpha)` — 지정한 영역에서 일련의 장치 독립 RGB+투명도 값을 렌더링합니다.
- `void drawRoundRect (int x, int y, int width, int height, int arcWidth, int arcHeight)` — 지정한 둥근 모서리 직사각형의 윤곽을 현재 색과 입력 스타일을 사용하여 그립니다.
- `void drawString ( String str, int x, int y, int anchor)` — 지정한 String 을 현재 글꼴과 색을 사용하여 그립니다.
- `void drawSubstring ( String str, int offset, int len, int x, int y, int anchor)` — 지정한 String 을 현재 글꼴과 색을 사용하여 그립니다.
- `void fillArc (int x, int y, int width, int height, int startAngle, int arcAngle)` — 지정한 직사각형을 덮는 원형 호나 타원형 호를 채웁니다.
- `void fillRect (int x, int y, int width, int height)` — 지정한 직사각형을 현재 색으로 채웁니다.
- `void fillRoundRect (int x, int y, int width, int height, int arcWidth, int arcHeight)` — 현재 색으로 지정된 둥근 모서리의 직사각형을 채웁니다.
- `void fillTriangle (int x1, int y1, int x2, int y2, int x3, int y3)` — 현재 색으로 지정한 삼각형을 채웁니다 각 지점 쌍을 연결하는 선이 채워진 삼각형에 포함됩니다.
- `int getBlueComponent ()` — 현재 색의 파랑 구성 요소를 가져옵니다.
- `int getClipHeight ()` — 현재 클립 영역의 높이를 가져옵니다.
- `int getClipWidth ()` — 현재 클립 영역의 너비를 가져옵니다.
- `int getClipX ()` — 이 그래픽 컨텍스트의 좌표계 원점과 비례하여 현재 클립 영역의 X 오프셋을 가져옵니다.
- `int getClipY ()` — 이 그래픽 컨텍스트의 좌표계 원점과 비례하여 현재 클립 영역의 Y 오프셋을 가져옵니다.
- `int getColor ()` — 현재 색을 가져옵니다.
- `int getDisplayColor (int color)` — 지정한 색을 요청하면 표시될 색을 가져옵니다.
- `Font getFont ()` — 현재 글꼴을 가져옵니다.
- `int getGrayScale ()` — 렌더링 작업에 사용된 색의 현재 회색조 값을 가져옵니다.
- `int getGreenComponent ()` — 현재 색의 녹색 구성 요소를 가져옵니다.
- `int getRedComponent ()` — 현재 색의 빨강 구성 요소를 가져옵니다.
- `int getStrokeStyle ()` — 그리기 작업에 사용된 입력 스타일을 가져옵니다.
- `int getTranslateX ()` — 이 그래픽 컨텍스트의 변환된 원점의 X 좌표를 가져옵니다.
- `int getTranslateY ()` — 이 그래픽 컨텍스트의 변환된 원점의 Y 좌표를 가져옵니다.
- `void setClip (int x, int y, int width, int height)` — 현재 클립을 주어진 좌표에 의해 지정된 직사각형으로 설정합니다.
- `void setColor (int RGB)` — 현재 색을 지정한 RGB 값으로 설정합니다.
- `void setColor (int red, int green, int blue)` — 현재 색을 지정한 RGB 값으로 설정합니다.
- `void setFont ( Font font)` — 모든 후속 텍스트 렌더링 작업의 글꼴을 설정합니다.
- `void setGrayScale (int value)` — 모든 후속 렌더링 작업에서 사용되는 현재 회색조를 설정합니다.
- `void setStrokeStyle (int style)` — 선, 호, 직사각형 및 둥근 직사각형을 그리는 데 사용된 입력 스타일을 설정합니다.
- `void translate (int x, int y)` — 그래픽 컨텍스트의 원점을 현재 좌표계의 점 (x, y) 로 변환됩니다.

## 필드 상세

### HCENTER

```java
public static final int HCENTER
```

**See Also:**
- `Constant Field Values`

### VCENTER

```java
public static final int VCENTER
```

**See Also:**
- `Constant Field Values`

### LEFT

```java
public static final int LEFT
```

**See Also:**
- `Constant Field Values`

### RIGHT

```java
public static final int RIGHT
```

**See Also:**
- `Constant Field Values`

### TOP

```java
public static final int TOP
```

**See Also:**
- `Constant Field Values`

### BOTTOM

```java
public static final int BOTTOM
```

**See Also:**
- `Constant Field Values`

### BASELINE

```java
public static final int BASELINE
```

**See Also:**
- `Constant Field Values`

### SOLID

```java
public static final int SOLID
```

**See Also:**
- `Constant Field Values`

### DOTTED

```java
public static final int DOTTED
```

**See Also:**
- `Constant Field Values`

### translate

```java
public void translate(int x,
                      int y)
```

**Parameters:**
- `y` - 새 변환 원점의 y 좌표

**See Also:**
- ``getTranslateX()``, 
``getTranslateY()``

### getTranslateX

```java
public int getTranslateX()
```

**Returns:**
- 현재 원점의 X

### getTranslateY

```java
public int getTranslateY()
```

**Returns:**
- 현재 원점의 Y

### getColor

```java
public int getColor()
```

**Returns:**
- `0x00RRGGBB` 형식의 정수

**See Also:**
- ``setColor(int, int, int)``

### getRedComponent

```java
public int getRedComponent()
```

**Returns:**
- `0-255` 범위의 정수 값

**See Also:**
- ``setColor(int, int, int)``

### getGreenComponent

```java
public int getGreenComponent()
```

**Returns:**
- `0-255` 범위의 정수 값

**See Also:**
- ``setColor(int, int, int)``

### getBlueComponent

```java
public int getBlueComponent()
```

**Returns:**
- `0-255` 범위의 정수 값

**See Also:**
- ``setColor(int, int, int)``

### getGrayScale

```java
public int getGrayScale()
```

**Returns:**
- `0-255` 범위의 정수 값

**See Also:**
- ``setGrayScale(int)``

### setColor

```java
public void setColor(int red,
                     int green,
                     int blue)
```

**Parameters:**
- `blue` - `0-255` 범위에 설정된 
색의 파랑 구성 요소

**Throws:**
- `IllegalArgumentException` - 색 구성 요소 중 하나가 
`0-255` 범위를 벗어난 경우

**See Also:**
- ``getColor()``

### setColor

```java
public void setColor(int RGB)
```

**Parameters:**
- `RGB` - 설정된 색

**See Also:**
- ``getColor()``

### setGrayScale

```java
public void setGrayScale(int value)
```

**Parameters:**
- `value` - 원하는 회색조 값

**Throws:**
- `IllegalArgumentException` - 회색이 범위를 벗어나는 경우

**See Also:**
- ``getGrayScale()``

### getFont

```java
public Font getFont()
```

**Returns:**
- 현재 글꼴

**See Also:**
- ``Font``, 
``setFont(javax.microedition.lcdui.Font)``

### setStrokeStyle

```java
public void setStrokeStyle(int style)
```

**Parameters:**
- `style` - `SOLID`나 `DOTTED`가 될 수 있습니다.

**Throws:**
- `IllegalArgumentException` - `style`이 유효하지 않은 경우

**See Also:**
- ``getStrokeStyle()``

### getStrokeStyle

```java
public int getStrokeStyle()
```

**Returns:**
- 입력 스타일, `SOLID` 또는 `DOTTED`

**See Also:**
- ``setStrokeStyle(int)``

### setFont

```java
public void setFont(Font font)
```

**Parameters:**
- `font` - 지정된 글꼴

**See Also:**
- ``Font``, 
``getFont()``, 
``drawString(java.lang.String, int, int, int)``, 
``drawChars(char[], int, int, int, int, int)``

### getClipX

```java
public int getClipX()
```

**Returns:**
- 현재 클립 영역의 X 오프셋

**See Also:**
- ``clipRect(int, int, int, int)``, 
``setClip(int, int, int, int)``

### getClipY

```java
public int getClipY()
```

**Returns:**
- 현재 클립 영역의 Y 오프셋

**See Also:**
- ``clipRect(int, int, int, int)``, 
``setClip(int, int, int, int)``

### getClipWidth

```java
public int getClipWidth()
```

**Returns:**
- 현재 클립 영역의 너비

**See Also:**
- ``clipRect(int, int, int, int)``, 
``setClip(int, int, int, int)``

### getClipHeight

```java
public int getClipHeight()
```

**Returns:**
- 현재 클립 영역의 높이

**See Also:**
- ``clipRect(int, int, int, int)``, 
``setClip(int, int, int, int)``

### clipRect

```java
public void clipRect(int x,
                     int y,
                     int width,
                     int height)
```

**Parameters:**
- `height` - 클립과 교차할 직사각형의 높이

**See Also:**
- ``setClip(int, int, int, int)``

### setClip

```java
public void setClip(int x,
                    int y,
                    int width,
                    int height)
```

**Parameters:**
- `height` - 새 클립 직사각형의 높이

**See Also:**
- ``clipRect(int, int, int, int)``

### drawLine

```java
public void drawLine(int x1,
                     int y1,
                     int x2,
                     int y2)
```

**Parameters:**
- `y2` - 선이 끝나는 부분의 y 좌표

### fillRect

```java
public void fillRect(int x,
                     int y,
                     int width,
                     int height)
```

**Parameters:**
- `height` - 채워질 직사각형의 높이

**See Also:**
- ``drawRect(int, int, int, int)``

### drawRect

```java
public void drawRect(int x,
                     int y,
                     int width,
                     int height)
```

**Parameters:**
- `height` - 그려지는 직사각형의 높이

**See Also:**
- ``fillRect(int, int, int, int)``

### drawRoundRect

```java
public void drawRoundRect(int x,
                          int y,
                          int width,
                          int height,
                          int arcWidth,
                          int arcHeight)
```

**Parameters:**
- `arcHeight` - 네 개의 모서리에 있는 호의 세로 지름

**See Also:**
- ``fillRoundRect(int, int, int, int, int, int)``

### fillRoundRect

```java
public void fillRoundRect(int x,
                          int y,
                          int width,
                          int height,
                          int arcWidth,
                          int arcHeight)
```

**Parameters:**
- `arcHeight` - 네 개의 모서리에 있는 호의 세로 지름

**See Also:**
- ``drawRoundRect(int, int, int, int, int, int)``

### fillArc

```java
public void fillArc(int x,
                    int y,
                    int width,
                    int height,
                    int startAngle,
                    int arcAngle)
```

**Parameters:**
- `arcAngle` - 시작 각도에 
비례하는 호의 각도 범위

**See Also:**
- ``drawArc(int, int, int, int, int, int)``

### drawArc

```java
public void drawArc(int x,
                    int y,
                    int width,
                    int height,
                    int startAngle,
                    int arcAngle)
```

**Parameters:**
- `arcAngle` - 시작 각도에 
비례하는 호의 각 범위

**See Also:**
- ``fillArc(int, int, int, int, int, int)``

### drawString

```java
public void drawString(String str,
                       int x,
                       int y,
                       int anchor)
```

**Parameters:**
- `anchor` - 텍스트를 배치할 앵커 포인트

**Throws:**
- `IllegalArgumentException` - 앵커가 유효한 값이 아닌 경우

**See Also:**
- ``drawChars(char[], int, int, int, int, int)``

### drawSubstring

```java
public void drawSubstring(String str,
                          int offset,
                          int len,
                          int x,
                          int y,
                          int anchor)
```

**Parameters:**
- `anchor` - 텍스트를 배치하기 위한 앵커 포인트

**Throws:**
- `NullPointerException` - `str`이 `null`인 경우

**See Also:**
- ``drawString(String, int, int, int).``

### drawChar

```java
public void drawChar(char character,
                     int x,
                     int y,
                     int anchor)
```

**Parameters:**
- `anchor` - 텍스트를 배치할 앵커 포인트. 
앵커 포인트 참조

**Throws:**
- `IllegalArgumentException` - `anchor`가 
유효한 값이 아닌 경우

**See Also:**
- ``drawString(java.lang.String, int, int, int)``, 
``drawChars(char[], int, int, int, int, int)``

### drawChars

```java
public void drawChars(char[] data,
                      int offset,
                      int length,
                      int x,
                      int y,
                      int anchor)
```

**Parameters:**
- `anchor` - 텍스트를 배치할 앵커 포인트. 
앵커 포인트 참조

**Throws:**
- `NullPointerException` - `data`가 `null`인 경우

**See Also:**
- ``drawString(java.lang.String, int, int, int)``

### drawImage

```java
public void drawImage(Image img,
                      int x,
                      int y,
                      int anchor)
```

**Parameters:**
- `anchor` - 이미지 배치를 위한 앵커 포인트

**Throws:**
- `NullPointerException` - `img`가 `null`인 경우

**See Also:**
- ``Image``

### drawRegion

```java
public void drawRegion(Image src,
                       int x_src,
                       int y_src,
                       int width,
                       int height,
                       int transform,
                       int x_dest,
                       int y_dest,
                       int anchor)
```

**Parameters:**
- `anchor` - 대상 이미지 내에서 
영역을 배치할 앵커 포인트

**Throws:**
- `IllegalArgumentException` - 복사되는 영역이 소스 이미지의 
범위를 넘는 경우

**Since:**
- MIDP 2.0

### copyArea

```java
public void copyArea(int x_src,
                     int y_src,
                     int width,
                     int height,
                     int x_dest,
                     int y_dest,
                     int anchor)
```

**Parameters:**
- `anchor` - 대상 이미지 내에서 영역을 
배치할 앵커 포인트

**Throws:**
- `IllegalArgumentException` - 복사되는 영역이 소스 이미지의 
범위를 넘는 경우

**Since:**
- MIDP 2.0

### fillTriangle

```java
public void fillTriangle(int x1,
                         int y1,
                         int x2,
                         int y2,
                         int x3,
                         int y3)
```

**Parameters:**
- `y3` - 삼각형의 세 번째 정점의 y 좌표

**Since:**
- MIDP 2.0

### drawRGB

```java
public void drawRGB(int[] rgbData,
                    int offset,
                    int scanlength,
                    int x,
                    int y,
                    int width,
                    int height,
                    boolean processAlpha)
```

**Parameters:**
- `processAlpha` - `rgbData`에 
알파 채널이 있는 경우 `true`, 
모든 픽셀이 전체적으로 불투명한 경우 false

**Throws:**
- `NullPointerException` - `rgbData`가 `null`인 경우

**Since:**
- MIDP 2.0

### getDisplayColor

```java
public int getDisplayColor(int color)
```

**Parameters:**
- `color` - 원하는
색(`0x00RRGGBB` 형식이며 
상위 바이트는 무시됨)

**Returns:**
- 장치 화면에 표시될 해당 
색(`0x00RRGGBB` 형식으로)

**Since:**
- MIDP 2.0

## 메서드 상세

### translate

```java
public void translate(int x,
                      int y)
```

**Parameters:**
- `y` - 새 변환 원점의 y 좌표

**See Also:**
- ``getTranslateX()``, 
``getTranslateY()``

### getTranslateX

```java
public int getTranslateX()
```

**Returns:**
- 현재 원점의 X

### getTranslateY

```java
public int getTranslateY()
```

**Returns:**
- 현재 원점의 Y

### getColor

```java
public int getColor()
```

**Returns:**
- `0x00RRGGBB` 형식의 정수

**See Also:**
- ``setColor(int, int, int)``

### getRedComponent

```java
public int getRedComponent()
```

**Returns:**
- `0-255` 범위의 정수 값

**See Also:**
- ``setColor(int, int, int)``

### getGreenComponent

```java
public int getGreenComponent()
```

**Returns:**
- `0-255` 범위의 정수 값

**See Also:**
- ``setColor(int, int, int)``

### getBlueComponent

```java
public int getBlueComponent()
```

**Returns:**
- `0-255` 범위의 정수 값

**See Also:**
- ``setColor(int, int, int)``

### getGrayScale

```java
public int getGrayScale()
```

**Returns:**
- `0-255` 범위의 정수 값

**See Also:**
- ``setGrayScale(int)``

### setColor

```java
public void setColor(int red,
                     int green,
                     int blue)
```

**Parameters:**
- `blue` - `0-255` 범위에 설정된 
색의 파랑 구성 요소

**Throws:**
- `IllegalArgumentException` - 색 구성 요소 중 하나가 
`0-255` 범위를 벗어난 경우

**See Also:**
- ``getColor()``

### setColor

```java
public void setColor(int RGB)
```

**Parameters:**
- `RGB` - 설정된 색

**See Also:**
- ``getColor()``

### setGrayScale

```java
public void setGrayScale(int value)
```

**Parameters:**
- `value` - 원하는 회색조 값

**Throws:**
- `IllegalArgumentException` - 회색이 범위를 벗어나는 경우

**See Also:**
- ``getGrayScale()``

### getFont

```java
public Font getFont()
```

**Returns:**
- 현재 글꼴

**See Also:**
- ``Font``, 
``setFont(javax.microedition.lcdui.Font)``

### setStrokeStyle

```java
public void setStrokeStyle(int style)
```

**Parameters:**
- `style` - `SOLID`나 `DOTTED`가 될 수 있습니다.

**Throws:**
- `IllegalArgumentException` - `style`이 유효하지 않은 경우

**See Also:**
- ``getStrokeStyle()``

### getStrokeStyle

```java
public int getStrokeStyle()
```

**Returns:**
- 입력 스타일, `SOLID` 또는 `DOTTED`

**See Also:**
- ``setStrokeStyle(int)``

### setFont

```java
public void setFont(Font font)
```

**Parameters:**
- `font` - 지정된 글꼴

**See Also:**
- ``Font``, 
``getFont()``, 
``drawString(java.lang.String, int, int, int)``, 
``drawChars(char[], int, int, int, int, int)``

### getClipX

```java
public int getClipX()
```

**Returns:**
- 현재 클립 영역의 X 오프셋

**See Also:**
- ``clipRect(int, int, int, int)``, 
``setClip(int, int, int, int)``

### getClipY

```java
public int getClipY()
```

**Returns:**
- 현재 클립 영역의 Y 오프셋

**See Also:**
- ``clipRect(int, int, int, int)``, 
``setClip(int, int, int, int)``

### getClipWidth

```java
public int getClipWidth()
```

**Returns:**
- 현재 클립 영역의 너비

**See Also:**
- ``clipRect(int, int, int, int)``, 
``setClip(int, int, int, int)``

### getClipHeight

```java
public int getClipHeight()
```

**Returns:**
- 현재 클립 영역의 높이

**See Also:**
- ``clipRect(int, int, int, int)``, 
``setClip(int, int, int, int)``

### clipRect

```java
public void clipRect(int x,
                     int y,
                     int width,
                     int height)
```

**Parameters:**
- `height` - 클립과 교차할 직사각형의 높이

**See Also:**
- ``setClip(int, int, int, int)``

### setClip

```java
public void setClip(int x,
                    int y,
                    int width,
                    int height)
```

**Parameters:**
- `height` - 새 클립 직사각형의 높이

**See Also:**
- ``clipRect(int, int, int, int)``

### drawLine

```java
public void drawLine(int x1,
                     int y1,
                     int x2,
                     int y2)
```

**Parameters:**
- `y2` - 선이 끝나는 부분의 y 좌표

### fillRect

```java
public void fillRect(int x,
                     int y,
                     int width,
                     int height)
```

**Parameters:**
- `height` - 채워질 직사각형의 높이

**See Also:**
- ``drawRect(int, int, int, int)``

### drawRect

```java
public void drawRect(int x,
                     int y,
                     int width,
                     int height)
```

**Parameters:**
- `height` - 그려지는 직사각형의 높이

**See Also:**
- ``fillRect(int, int, int, int)``

### drawRoundRect

```java
public void drawRoundRect(int x,
                          int y,
                          int width,
                          int height,
                          int arcWidth,
                          int arcHeight)
```

**Parameters:**
- `arcHeight` - 네 개의 모서리에 있는 호의 세로 지름

**See Also:**
- ``fillRoundRect(int, int, int, int, int, int)``

### fillRoundRect

```java
public void fillRoundRect(int x,
                          int y,
                          int width,
                          int height,
                          int arcWidth,
                          int arcHeight)
```

**Parameters:**
- `arcHeight` - 네 개의 모서리에 있는 호의 세로 지름

**See Also:**
- ``drawRoundRect(int, int, int, int, int, int)``

### fillArc

```java
public void fillArc(int x,
                    int y,
                    int width,
                    int height,
                    int startAngle,
                    int arcAngle)
```

**Parameters:**
- `arcAngle` - 시작 각도에 
비례하는 호의 각도 범위

**See Also:**
- ``drawArc(int, int, int, int, int, int)``

### drawArc

```java
public void drawArc(int x,
                    int y,
                    int width,
                    int height,
                    int startAngle,
                    int arcAngle)
```

**Parameters:**
- `arcAngle` - 시작 각도에 
비례하는 호의 각 범위

**See Also:**
- ``fillArc(int, int, int, int, int, int)``

### drawString

```java
public void drawString(String str,
                       int x,
                       int y,
                       int anchor)
```

**Parameters:**
- `anchor` - 텍스트를 배치할 앵커 포인트

**Throws:**
- `IllegalArgumentException` - 앵커가 유효한 값이 아닌 경우

**See Also:**
- ``drawChars(char[], int, int, int, int, int)``

### drawSubstring

```java
public void drawSubstring(String str,
                          int offset,
                          int len,
                          int x,
                          int y,
                          int anchor)
```

**Parameters:**
- `anchor` - 텍스트를 배치하기 위한 앵커 포인트

**Throws:**
- `NullPointerException` - `str`이 `null`인 경우

**See Also:**
- ``drawString(String, int, int, int).``

### drawChar

```java
public void drawChar(char character,
                     int x,
                     int y,
                     int anchor)
```

**Parameters:**
- `anchor` - 텍스트를 배치할 앵커 포인트. 
앵커 포인트 참조

**Throws:**
- `IllegalArgumentException` - `anchor`가 
유효한 값이 아닌 경우

**See Also:**
- ``drawString(java.lang.String, int, int, int)``, 
``drawChars(char[], int, int, int, int, int)``

### drawChars

```java
public void drawChars(char[] data,
                      int offset,
                      int length,
                      int x,
                      int y,
                      int anchor)
```

**Parameters:**
- `anchor` - 텍스트를 배치할 앵커 포인트. 
앵커 포인트 참조

**Throws:**
- `NullPointerException` - `data`가 `null`인 경우

**See Also:**
- ``drawString(java.lang.String, int, int, int)``

### drawImage

```java
public void drawImage(Image img,
                      int x,
                      int y,
                      int anchor)
```

**Parameters:**
- `anchor` - 이미지 배치를 위한 앵커 포인트

**Throws:**
- `NullPointerException` - `img`가 `null`인 경우

**See Also:**
- ``Image``

### drawRegion

```java
public void drawRegion(Image src,
                       int x_src,
                       int y_src,
                       int width,
                       int height,
                       int transform,
                       int x_dest,
                       int y_dest,
                       int anchor)
```

**Parameters:**
- `anchor` - 대상 이미지 내에서 
영역을 배치할 앵커 포인트

**Throws:**
- `IllegalArgumentException` - 복사되는 영역이 소스 이미지의 
범위를 넘는 경우

**Since:**
- MIDP 2.0

### copyArea

```java
public void copyArea(int x_src,
                     int y_src,
                     int width,
                     int height,
                     int x_dest,
                     int y_dest,
                     int anchor)
```

**Parameters:**
- `anchor` - 대상 이미지 내에서 영역을 
배치할 앵커 포인트

**Throws:**
- `IllegalArgumentException` - 복사되는 영역이 소스 이미지의 
범위를 넘는 경우

**Since:**
- MIDP 2.0

### fillTriangle

```java
public void fillTriangle(int x1,
                         int y1,
                         int x2,
                         int y2,
                         int x3,
                         int y3)
```

**Parameters:**
- `y3` - 삼각형의 세 번째 정점의 y 좌표

**Since:**
- MIDP 2.0

### drawRGB

```java
public void drawRGB(int[] rgbData,
                    int offset,
                    int scanlength,
                    int x,
                    int y,
                    int width,
                    int height,
                    boolean processAlpha)
```

**Parameters:**
- `processAlpha` - `rgbData`에 
알파 채널이 있는 경우 `true`, 
모든 픽셀이 전체적으로 불투명한 경우 false

**Throws:**
- `NullPointerException` - `rgbData`가 `null`인 경우

**Since:**
- MIDP 2.0

### getDisplayColor

```java
public int getDisplayColor(int color)
```

**Parameters:**
- `color` - 원하는
색(`0x00RRGGBB` 형식이며 
상위 바이트는 무시됨)

**Returns:**
- 장치 화면에 표시될 해당 
색(`0x00RRGGBB` 형식으로)

**Since:**
- MIDP 2.0
