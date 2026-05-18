# Class TiledLayer

`package javax.microedition.lcdui.game`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.game.Layer
        |
        +--javax.microedition.lcdui.game.TiledLayer
```

## 설명

**extends Layer:**

TiledLayer는 타일 이미지 집합으로 
채울 수 있는 
셀의 격자로 구성된 시각적 요소입니다. 
이 클래스를 사용하면 아주 큰 이미지가 없어도 
큰 가상 계층을 만들 수 있습니다. 
이 기술은 주로 2D 게임 플랫폼에서 
아주 큰 스크롤 배경을 만드는데 사용됩니다.

### 타일

TiledLayer 셀을 채우기 위해 
사용된 타일은 변경 가능하거나 
불가능한 단일 Image 객체로 제공됩니다. 
Image는 같은 크기를 갖는 
일련의 타일로 쪼개집니다. 
타일 크기는 Image에 따라 지정됩니다. 
아래의 그림에 표시된 대로 게임 
개발자의 편의상 같은 타일 집합을 
여러 가지 다양한 배열로 저장할 수 있습니다.

각 타일에는 고유 색인 번호가 할당됩니다. 
Image의 왼쪽 위 모서리에 있는 
타일에는 색인 1이 할당됩니다. 
그런 다음 나머지 타일의 번호는 행 순서 
위주로(첫 번째 행에 색인을 할당한 다음 
두 번째 행에 할당하는 식으로) 
연속하여 매겨집니다. 타일 및 타일과 연관된 이미지 데이터 사이에는 
고정된 연결이 있으므로 이러한 타일은

로 간주됩니다.

TiledLayer를 인스턴스화할 때 정적 
타일 집합이 만들어지며 이는 ``setStaticTileSet(javax.microedition.lcdui.Image, int, int)`` 메소드를 
사용하여 언제든지 업데이트할 수 있습니다.

정적 타일 집합 외에도 개발자는 
여러 *애니메이션 타일*을 
정의할 수 있습니다. 애니메이션 타일은 정적 타일과 
동적으로 연결되는 가상 타일입니다. 
애니메이션 타일의 모양은 
현재 연결된 정적 타일의 모양이 됩니다.

애니메이션 타일을 사용하면 개발자는 
셀 그룹의 모양을 매우 쉽게 변경할 수 있습니다. 
애니메이션 타일로 모두 채워진 
셀 그룹을 사용하는 경우 
애니메이션 타일과 연결된 정적 타일만 변경하면 
전체 그룹의 모양을 변경할 수 있습니다. 
이 기술은 여러 셀의 내용을 
명시적으로 변경하지 않고도 반복되는 
큰 영역에 애니메이션 효과를 줄 때 매우 유용합니다.

애니메이션 타일은 새 애니메이션 타일에 
사용될 색인을 반환하는 ``createAnimatedTile(int)`` 메소드를 
사용하여 만들어집니다. 
애니메이션 타일 색인은 -1에서 시작하며 항상 음수이고 연속적입니다. 
애니메이션 타일이 일단 만들어지면 
애니메이션 타일과 연결된 정적 타일은 
``setAnimatedTile(int, int)`` 메소드를 
사용하여 변경할 수 있습니다.

### 셀

TiledLayer 격자는 같은 
크기의 셀로 구성됩니다. 
격자에 있는 열과 행의 수는 
구성자에서 지정되며 
셀의 물리적 크기는 타일의 크기에 의해 정의됩니다.

각 셀의 내용은 타일 색인을 사용하여 지정됩니다. 
양수 타일 색인은 정적 타일을 참조하며 
음수 타일 색인은 애니메이션 타일을 참조합니다. 
타일 색인 0은 셀이 비어 있음을 나타냅니다. 
빈 셀은 완전히 투명하며 
해당 영역에는 TiledLayer로 그려진 
내용이 없습니다. 기본적으로 모든 셀은 타일 
색인 0을 포함합니다.

``setCell(int, int, int)``과 ``fillCells(int, int, int, int, int)``를 사용하면 
셀의 내용을 변경할 수 있습니다. 
여러 셀에 같은 타일이 포함될 수 있지만 
단일 셀에 두 개 이상의 타일이 포함될 수는 없습니다. 
다음 예에서는 TiledLayer를 사용하여 단순한 배경을 만들 수 있는 방법을 
설명합니다.

이 예에서 물의 영역은 색인 -1인 애니메이션 타일로 채워지는데 
처음에 이 타일은 정적 타일 5와 연결됩니다.

을 사용하여 
연결된 정적 타일만 변경하면 
전체 물의 영역에 애니메이션 
효과를 줄 수 있습니다.

### TiledLayer 렌더링

TiledLayer는 해당 paint 메소드를 수동으로 
호출하여 렌더링할 수 있으며 LayerManager 객체를 
사용하여 자동으로 렌더링할 수도 있습니다.

paint 메소드는 Graphics 
객체의 클립 영역에 따라 
전체 TiledLayer를 
렌더링하려고 시도합니다. 
TiledLayer의 왼쪽 위 모서리는 Graphics 객체의 원점에 대해 
현재 (x,y) 위치에서 렌더링됩니다. 
이에 따라 Graphics 객체의 클립 영역을 설정하여 
렌더링된 영역을 제어할 수 있습니다.

**Since:**
- MIDP 2.0

## 생성자 요약

- TiledLayer (int columns,
 int rows, Image image,
 int tileWidth,
 int tileHeight) 새 TiledLayer를 만듭니다.

## 메서드 요약

- `int createAnimatedTile (int staticTileIndex)` — 새 애니메이션 타일을 만들고 새 애니메이션 타일을 참조하는 색인을 반환합니다.
- `void fillCells (int col, int row, int numCols, int numRows, int tileIndex)` — 특정 타일을 사용하여 영역 셀을 채웁니다.
- `int getAnimatedTile (int animatedTileIndex)` — 애니메이션 타일이 참조하는 타일을 가져옵니다.
- `int getCell (int col, int row)` — 셀의 내용을 가져옵니다.
- `int getCellHeight ()` — 단일 셀의 높이(픽셀 단위)를 가져옵니다.
- `int getCellWidth ()` — 단일 셀의 너비(픽셀 단위)를 가져옵니다.
- `int getColumns ()` — TiledLayer 격자 열의 수를 가져옵니다.
- `int getRows ()` — TiledLayer 격자의 행 수를 가져옵니다.
- `void paint ( Graphics g)` — TiledLayer를 그립니다.
- `void setAnimatedTile (int animatedTileIndex, int staticTileIndex)` — 애니메이션 타일을 지정한 정적 타일과 연결합니다.
- `void setCell (int col, int row, int tileIndex)` — 셀의 내용을 설정합니다.
- `void setStaticTileSet ( Image image, int tileWidth, int tileHeight)` — 정적 타일 집합을 변경합니다.

## 생성자 상세

### TiledLayer

```java
public TiledLayer(int columns,
                  int rows,
                  Image image,
                  int tileWidth,
                  int tileHeight)
```

- 새 TiledLayer를 만듭니다.

TiledLayer의 격자는 `rows` 셀의 높이와 
`columns` 셀의 너비를 가집니다. 
격자의 모든 셀은 처음에는 비어 있습니다(즉, 타일 색인 0 포함). 
``setCell(int, int, int)``과 ``fillCells(int, int, int, int, int)``를 사용하여 격자의 내용을 수정할 수 있습니다.

TiledLayer의 정적 타일 집합은 
지정한 Image로부터 만들어지며 
각 타일의 치수는 tileWidth x tileHeight가 됩니다. 
소스 이미지의 너비는 타일 너비 정수의 배수가 되어야 하며 
소스 이미지의 높이는 타일 높이 정수의 배수가 되어야 합니다. 
그렇지 않은 경우 IllegalArgumentException이 발생합니다.

``setStaticTileSet(Image, int, int)``를 
사용하여 전체 정적 타일 집합을 변경할 수 있습니다. 
이러한 메소드는 메모리와 시간을 많이 소모하므로 
자주 사용하지 않습니다. 
가능하면 타일 모양에 애니메이션 효과를 주기 보다 
애니메이션 타일을 사용해야 합니다.

**Parameters:**
- `tileHeight` - 단일 타일의 높이(픽셀 단위)

**Throws:**
- `IllegalArgumentException` - `image` 높이가 
`tileHeight` 정수의 배수가 아닌 경우

### createAnimatedTile

```java
public int createAnimatedTile(int staticTileIndex)
```

**Parameters:**
- `staticTileIndex` - 연결된 타일의 색인(`0` 또는 
유효한 정적 타일 색인)

**Returns:**
- 새로 만든 애니메이션 타일의 색인

**Throws:**
- `IndexOutOfBoundsException` - `staticTileIndex`가 
유효하지 않은 경우

### setAnimatedTile

```java
public void setAnimatedTile(int animatedTileIndex,
                            int staticTileIndex)
```

**Parameters:**
- `staticTileIndex` - 연결된 타일의 색인(`0`이거나 
유효한 정적 타일 색인)

**Throws:**
- `IndexOutOfBoundsException` - 애니메이션 타일 색인이 
유효하지 않은 경우

**See Also:**
- ``getAnimatedTile(int)``

### getAnimatedTile

```java
public int getAnimatedTile(int animatedTileIndex)
```

**Parameters:**
- `animatedTileIndex` - 애니메이션 타일의 색인

**Returns:**
- 애니메이션 타일에서 참조하는 타일의 색인

**Throws:**
- `IndexOutOfBoundsException` - 애니메이션 타일 색인이 
유효하지 않은 경우

**See Also:**
- ``setAnimatedTile(int, int)``

### setCell

```java
public void setCell(int col,
                    int row,
                    int tileIndex)
```

**Parameters:**
- `tileIndex` - 셀에 놓을 타일의 색인

**Throws:**
- `IndexOutOfBoundsException` - `row`나 
`col`이 `TiledLayer` 격자의 
범위를 벗어나는 경우

**See Also:**
- ``getCell(int, int)``, 
``fillCells(int, int, int, int, int)``

### getCell

```java
public int getCell(int col,
                   int row)
```

**Parameters:**
- `row` - 검사할 셀의 행

**Returns:**
- 셀에 있는 타일의 색인

**Throws:**
- `IndexOutOfBoundsException` - `row`나 
`col`이 `TiledLayer` 
격자의 범위를 벗어나는 경우

**See Also:**
- ``setCell(int, int, int)``, 
``fillCells(int, int, int, int, int)``

### fillCells

```java
public void fillCells(int col,
                      int row,
                      int numCols,
                      int numRows,
                      int tileIndex)
```

**Parameters:**
- `tileIndex` - 지정한 영역의 모든 
셀에 놓을 타일의 색인

**Throws:**
- `IndexOutOfBoundsException` - `tileIndex` 
색인이 있는 타일이 없는 경우

**See Also:**
- ``setCell(int, int, int)``, 
``getCell(int, int)``

### getCellWidth

```java
public final int getCellWidth()
```

**Returns:**
- `TiledLayer` 격자에 있는 
단일 셀의 너비(픽셀 단위)

### getCellHeight

```java
public final int getCellHeight()
```

**Returns:**
- `TiledLayer` 격자에 있는 
단일 셀의 높이(픽셀 단위)

### getColumns

```java
public final int getColumns()
```

**Returns:**
- `TiledLayer` 
격자의 열 너비

### getRows

```java
public final int getRows()
```

**Returns:**
- `TiledLayer` 
격자의 행 높이

### setStaticTileSet

```java
public void setStaticTileSet(Image image,
                             int tileWidth,
                             int tileHeight)
```

**Parameters:**
- `tileHeight` - 단일 타일의 높이(픽셀 단위)

**Throws:**
- `IllegalArgumentException` - `image` 높이가 
`tileHeight` 정수의 배수가 아닌 경우

### paint

```java
public final void paint(Graphics g)
```

**Specified by:**
- `paint` in class `Layer`

**Parameters:**
- `g` - `TiledLayer`를 그릴 graphics 객체

**Throws:**
- `NullPointerException` - `g`가 `null`인 경우

## 메서드 상세

### createAnimatedTile

```java
public int createAnimatedTile(int staticTileIndex)
```

**Parameters:**
- `staticTileIndex` - 연결된 타일의 색인(`0` 또는 
유효한 정적 타일 색인)

**Returns:**
- 새로 만든 애니메이션 타일의 색인

**Throws:**
- `IndexOutOfBoundsException` - `staticTileIndex`가 
유효하지 않은 경우

### setAnimatedTile

```java
public void setAnimatedTile(int animatedTileIndex,
                            int staticTileIndex)
```

**Parameters:**
- `staticTileIndex` - 연결된 타일의 색인(`0`이거나 
유효한 정적 타일 색인)

**Throws:**
- `IndexOutOfBoundsException` - 애니메이션 타일 색인이 
유효하지 않은 경우

**See Also:**
- ``getAnimatedTile(int)``

### getAnimatedTile

```java
public int getAnimatedTile(int animatedTileIndex)
```

**Parameters:**
- `animatedTileIndex` - 애니메이션 타일의 색인

**Returns:**
- 애니메이션 타일에서 참조하는 타일의 색인

**Throws:**
- `IndexOutOfBoundsException` - 애니메이션 타일 색인이 
유효하지 않은 경우

**See Also:**
- ``setAnimatedTile(int, int)``

### setCell

```java
public void setCell(int col,
                    int row,
                    int tileIndex)
```

**Parameters:**
- `tileIndex` - 셀에 놓을 타일의 색인

**Throws:**
- `IndexOutOfBoundsException` - `row`나 
`col`이 `TiledLayer` 격자의 
범위를 벗어나는 경우

**See Also:**
- ``getCell(int, int)``, 
``fillCells(int, int, int, int, int)``

### getCell

```java
public int getCell(int col,
                   int row)
```

**Parameters:**
- `row` - 검사할 셀의 행

**Returns:**
- 셀에 있는 타일의 색인

**Throws:**
- `IndexOutOfBoundsException` - `row`나 
`col`이 `TiledLayer` 
격자의 범위를 벗어나는 경우

**See Also:**
- ``setCell(int, int, int)``, 
``fillCells(int, int, int, int, int)``

### fillCells

```java
public void fillCells(int col,
                      int row,
                      int numCols,
                      int numRows,
                      int tileIndex)
```

**Parameters:**
- `tileIndex` - 지정한 영역의 모든 
셀에 놓을 타일의 색인

**Throws:**
- `IndexOutOfBoundsException` - `tileIndex` 
색인이 있는 타일이 없는 경우

**See Also:**
- ``setCell(int, int, int)``, 
``getCell(int, int)``

### getCellWidth

```java
public final int getCellWidth()
```

**Returns:**
- `TiledLayer` 격자에 있는 
단일 셀의 너비(픽셀 단위)

### getCellHeight

```java
public final int getCellHeight()
```

**Returns:**
- `TiledLayer` 격자에 있는 
단일 셀의 높이(픽셀 단위)

### getColumns

```java
public final int getColumns()
```

**Returns:**
- `TiledLayer` 
격자의 열 너비

### getRows

```java
public final int getRows()
```

**Returns:**
- `TiledLayer` 
격자의 행 높이

### setStaticTileSet

```java
public void setStaticTileSet(Image image,
                             int tileWidth,
                             int tileHeight)
```

**Parameters:**
- `tileHeight` - 단일 타일의 높이(픽셀 단위)

**Throws:**
- `IllegalArgumentException` - `image` 높이가 
`tileHeight` 정수의 배수가 아닌 경우

### paint

```java
public final void paint(Graphics g)
```

**Specified by:**
- `paint` in class `Layer`

**Parameters:**
- `g` - `TiledLayer`를 그릴 graphics 객체

**Throws:**
- `NullPointerException` - `g`가 `null`인 경우
