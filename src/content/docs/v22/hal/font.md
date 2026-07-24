---
title: "2.6. 폰트"
---

다양한 폰트를 화면에 출력하거나 화면 출력 시에 다양한 정보들을 얻어오는 함수로 구성되어 있다. 폰트는 시스템에 마다 형태와 크기와 페이스(Face)가 일정하지 않으므로 각 폰트를 정 확히 지정하는 것이 아니라, 추상화된 내용으로 지정한다. 즉 크기(작음|보통|큼)과 스 타일(굵게|이탤릭|밑줄|보통)과 페이스를 가지고 실제적인 폰트를 얻어옴으로써 각 단말 기 마다 쉽게 적용될 수 있도록 하였다. Left Bear LLLeeegggRRRoooiiiggg hhhttt BBBeeeaaarrr AAAsssccceeennnttt HHHeeeiiiggghhhttt DDDeeesssccceeennnttt OOrriiggiinn ppooiinntt WWWiiidddttthhh [그림 2-6-1] 폰트정보 폰트의 각 부분은 폰트의 높이(Height)는 어센트(Ascent)와 디센트(Descent)를 합한 값 이 된다. 베어(Bear)는 폰트를 그릴 때 실제적으로 화면에 이미지를 어디서부터 어디까지 그릴 것인지를 결정한다. 대부분의 경우 왼쪽 베어(Left Bear)는 0이 되지만, 이탤릭 체와 같 은 경우에는 오른쪽 베어(Right Bear)가 폰트의 폭(Width)보다 큰 경우가 있다. 오른쪽 베어는 실제적으로 폰트의 이미지의 폭이 되고, 폭(Width)는 그 폰트를 그린 후에 얼마 만큼 이동한 후에 다음 문자를 그릴지를 결정하는 값이 된다. 폭이 오른쪽 베어(Right Bear)보다 작은 경우에는 위의 그림과 같이 겹쳐지는 부분이 있을 수 있다.

#### 관련 자료형

```c
typedef struct _MH_CharGlyphInfo {
int lbear; // 문자의 왼쪽 베어(bear)
int rbear; // 문자의 오른쪽 베어(bear)
int width; // 문자의 화면상의 폭
int height; // 문자의 화면상의 높이
} MH_CharGlyphInfo;
#define MH_FB_FT_SIZE_SMALL 8
#define MH_FB_FT_SIZE_MEDIUM 0
#define MH_FB_FT_SIZE_LARGE 16
#define MH_FB_FT_FACE_SYSTEM 0
#define MH_FB_FT_FACE_MONOSPACE 32
#define MH_FB_FT_FACE_PROPORTIONAL 64
#define MH_FB_FT_STYLE_PLAIN 0
#define MH_FB_FT_STYLE_BOLD 1
#define MH_FB_FT_STYLE_ITALIC 2
#define MH_FB_FT_STYLE_UNDERLINE 4
```

### MH_fnGetFont

**프로토타입**

```c
M_Int32 MH_fnGetFont (M_Int32 face, M_Int32 size, M_Int32 style)
```

**설명**

지정된 폰트 아이디를 얻어 온다. face는 `MH_FB_FT_FACE_SYSTEM`, `MH_FB_FT_FACE_MONOSPACE`(문자들의 폭이 일정한 폰트), `MH_FB_FT_FACE_PROPORTIONAL`(문자들의 폭이 일정하지 않은 폰 트) 중에 하나이며, size는 `MH_FB_FT_SIZE_SMALL`, `MH_FB_FT_SIZE_MEDIUM`, `MH_FB_FT_SIZE_` LARGE 중에 하나가 된다. style은 `MH_FB_FT_STYLE_ITALIC`, `MH_FB_FT_STYLE_BOLD`, MH_FB_FT_STYLE_UNDERLINED의 OR값이나 혹은 MH_FB_FT_STYLE_PLAIN을 사용할 수 있다. 지정된 폰트가 없으면 가장 근접한 폰 트를 돌려준다. 지정된 폰트 아이디로 “C” 로컬 문자 코드의 전체 문자를 출력할 수 있어야 한다.

**매개 변수**

- `face` - [in] 폰트 페이스(`MH_FB_FT_FACE_SYSTEM`, `MH_FB_FT_FACE_MONOSPACE`, `MH_FB_FT_FACE_PROPORTIONAL`)
- `size` - [in] 폰트 크기 (`MH_FB_FT_SIZE_SMALL`, `MH_FB_FT_SIZE_MEDIUM`, `MH_FB_FT_SIZE_LARGE`)
- `style` - [in] 폰트 스타일(`MH_FB_FT_STYLE_ITALIC`, `MH_FB_FT_STYLE_BOLD`, `MH_FB_FT_STYLE_UNDERLINED`)

**반환 값**

폰트 아이디

**부작용**

없음

**참고 항목**

없음

### MH_fnGetFontHeight

**프로토타입**

```c
M_Int32 MH_fnGetFontHeight (M_Int32 font)
```

**설명**

지정된 폰트의 높이를 돌려준다. 만일 지정된 폰트가 유효하지 않은 값인 경우에 0을 돌려준다.

**매개 변수**

- `font` - [in] 폰트 아이디

**반환 값**

폰트의 높이

**부작용**

없음

**참고 항목**

없음

### MH_fnGetFontAscent

**프로토타입**

```c
M_Int32 MH_fnGetFontAscent (M_Int32 font)
```

**설명**

지정된 폰트의 어센트(Ascent)를 돌려준다. 만일 지정된 폰트가 유효하지 않은 값인 경우에 0을 돌려준다.

**매개 변수**

- `font` - [in] 폰트 아이디

**반환 값**

폰트의 어센트(Ascent)

**부작용**

없음

**참고 항목**

없음

### MH_fnGetFontDescent

**프로토타입**

```c
M_Int32 MH_fnGetFontDescent (M_Int32 font)
```

**설명**

지정된 폰트의 디센트(Descent)를 돌려준다. 만일 지정된 폰트가 유효하지 않은 값인 경우에 0을 돌려준다.

**매개 변수**

- `font` - [in] 폰트 아이디

**반환 값**

폰트의 디센트(Descent)

**부작용**

없음

**참고 항목**

없음

### MH_fnGetCharGlyph

**프로토타입**

```c
const M_Uint8 *MH_fnGetCharGlyph(const M_Int32 fontid,const M_Uint16 ch,const M_Uint32 fgPxl,const M_Uint32 bgPxl,M_Int32 *pbpl)
```

**설명**

지정된 문자를 화면에 바로 찍을 수 있는 이미지 형태로 만들어 돌려준다. 돌려주는 버퍼는 주 화면 LCD와 같은 색상수를 가지며 주화면 LCD에 바로 복사할 수 있는 형태의 이미지이다. 이미지 내용은 반환하는 값이 가리키는 버퍼에 (0, 0)에서 부터 (1, 0), (2, 0), ... (0, 1), (1, 1) ... 의 순서대로 저장된다. PPiixxeell 단단위위 [그림 2-6-2] 폰트 예 LCD가 16bit 컬러를 지원할 때.

```c
M_Uint8 *pbuf = MH_fnGetCharGlyph(fontid, „H‟, blackPixel, whitePixel, &bpl);
```

```c
M_Uint16 *ppxls = (M_Uint16 *)pbuf;
```

와 같은 코드가 수행되었다면, , ppxls[0]은 whitePixel이 되고 ppxls[bpl*1] 은 whitePixel, ppxls[bpl * 1 + 1]은 blackPixel이 된다.

**매개 변수**

- `fontid` - [in] 폰트아이디
- `ch` - [in] 문자 (문자는 로컬 코드 이다. 즉 유니 코드가 아니다)
- `fgPxl` - [in] 문자의 전경색
- `bgPxl` - [in] 문자의 배경색
- `bpl` - [out] 프레임 버퍼의 한 줄 당 차지하는 바이트 수

**반환 값**

복사 할 수 있는 형태의 이미지 내부 버퍼에 대한 포인터. 이 버퍼 는 밖에서 해제되면 안되며 내용이 바뀌어서도 안 된다. 만일 ch에 대응하는 문자가 없는 경우에는 NULL을 돌려준다.

**부작용**

없음

**참고 항목**

없음

### MH_fnGetCharInfo

**프로토타입**

```c
M_Int32 MH_fnGetCharInfo(M_Int32 font, M_Uint16 ch, MH_CharGlyphInfo *pcg)
```

**설명**

지정된 문자의 폭과 왼쪽 베어(Left Bear)와 오른쪽(Right Bear)와 높이를 얻어 온다.

**매개 변수**

- `font` - [in] 폰트
- `char` - [in] 문자(문자는 로컬 코드 이다. 즉 유니 코드가 아니다)
- `pcg` - [out] 문자의 정보 반환

**반환 값**

성공

실패

- `M_E_ERROR` - 대응하는 문자 인덱스에 폰트가 없는 경우

**부작용**

없음

**참고 항목**

없음
