---
title: "2.2. 그래픽"
---

#### 그래픽 함수

화면이나 오프 스크린 프레임 버퍼(Off Screen Frame Buffer)에 다양한 그리기를 할 수 있는 API들이다.

#### 프레임 버퍼

화면 프레임 버퍼나 오프 스크린 프레임 버퍼는 데이타의 포인터와 데이터의 한 줄 당 바이트 수(Byte Per Line)으로 기술된다. 이 기술되는 프레임 버퍼는 MC_GrpFrameBuffer로 정의되며, 내부에 데이터와 데이터의 한 줄당 바이트 수, 폭, 높이를 담고 있다.

#### 오프 스크린 프레임 버퍼 생성/소멸

프레임 버퍼는 `MC_grpCreateOffScreenFrameBuffer` 함수로 생성되거나 MC_grpGetScreenFrameBuffer함수로 존재하는 화면 프레임 버퍼를 가져 올 수 있다. 생성된 프레임 버퍼는 MC_grpDestoryScreenFrameBuffer함수로 삭제 해주어야 한다.

#### 그래픽 컨텍스트

프레임 버퍼에 그리는 함수에는 대부분 그래픽 컨텍스트가 매개 변수로 넘어간다. 그래픽 컨택스트는 그리기 시에 필요한 각종 매개 변수를 저장하는 구조체로써 안에 는 전경색상과 클리핑 영역, 투명정도, 픽셀 연산 함수, 폰트와 스타일, 상대 좌표의 원점Offset)등을 가지고 있다. 각 그래픽 컨텍스트의 값을 변경하기 위해서는 `MC_grpSetContext` 함수를 사용하여 그 값을 변경한다. 모든 그리기 API에 클리핑 영역이 지정되어 있는 상태에서 그려지며, API에 따라서 각기 필드값을 사용하거나 사용하지 않을 수 있다. 그리기 모드는 투명하게 그리기(alpha 모드), XOR로 그리기(xor 모드) 일반 모드(둘 다 아닌 모드) 가 있으며 각 모드 배타적인 모드이다. 즉, xor모드로 되어 있을 때 alpha모드로 지정하면 이전에 xor모드는 취소가 된다. 상대 좌표체계를 지정하면 모든 그리기 좌표는 상대 좌표 계에 따라서 변경된다.

#### 이미지 디코딩/인코딩

이미지는 프레임 버퍼와 애니메이션의 여부, 매스크 이미지로 이루어 진다. 이미지 포맷은 BMP, PNG를 지원한다. 먼저 이미지 원본 내용을 버퍼에 로드한 후 에 이미지 내용을 MC_grpCreateImage함수를 통하여 이미지 구조체를 생성하면 화 면에 출력할 수 있다. MC_grpDrawImage함수를 통하면 이미지를 화면에 출력한다. 만일 animated이미지라면 MC_grpDecodeNextImage함수를 사용하여 다음 이미지를 생성할 수 있다. 다 사용된 이미지는 MC_grpDestoryImage함수를 통하여 삭제한다. MC_grpEncodeImage함수를 통해서 원하는 프레임 버퍼 영역을 BMP로 인코딩 할 수 있다.

#### 더블 버퍼링

폰의 LCD는 대부분의 경우 호스트 메모리와 분리되어 있으며 화면의 내용을 갱신하 는데 상당히 많은 시간을 소요한다. 이로 인해서 더블 버퍼링 기법을 사용한다. 화면 프레임 버퍼에 임의의 그림을 그린다 해도 실제적으로 LCD 화면에 출력되지 않고, MC_grpFlushLcd함수를 호출해야만 LCD화면에 화면 프레임 버퍼의 내용이 출력된 다.

#### 듀얼 디스플레이

폰에 따라서 LCD가 두 개이며 다른 부가적인 LCD는 주 LCD와 색상수가 다를 수 있다. 색상이 다른 LCD라 할지라도 MC_grpFlushLcd함수에서 받아 들이는 프레임 버퍼의 색상은 주 LCD와 같은 형식을 사용한다.(색상수도 같다.) `MC_grpFlushLcd` 그 색상에 가장 근접한 색상을 출력한다.

#### 문자 입력 처리

사용자에 의해서 입력 키를 넘겨 받아서 키 값을 검사하고, 오토마타를 통해서 문자 조합하여 완성된 문자열버퍼와 조합 중인 문자열 버퍼를 통해 넘겨준다. 입력 가능 한 문자열은 오토마타에 의해 결정되며, 현재 오토마타에서 사용 가능한 문자열은 `MC_imGetSurpportModeCount`()를 통해서 얻을 수 있고, 이때 반환되는 타입은 스트 링 포인터로 그 데이터는 ISO 639 코드에 정의된 표준언어코드를 따른다. 추가적으 로 언어가 대소문자를 구분하는 경우 각 코드에 “/S”,”/L”를 추가하여 사용할 수 있다. 기타 숫자입력을 위한 언어코드는 “N123”이 사용된다.

### MC_GrpPixelOpProc

**프로토타입**

```c
typedef M_Int32 (*MC_GrpPixelOpProc)(M_Int32 srcpxl, M_Int32 orgpxl,
M_Int32 param1)
```

**설명**

픽셀 연산(Operation)함수이다. 모든 그리기 함수에서 이 함수를 통한 결과 값이 최종적으로 쓰여지는 값이 된다. srcpxl과 orgpxl을 param1의 매개 변수로 적절히 계산하여 그 결과 값을 돌려주면 그 값이 프레임 버퍼에 쓰여지는 최종적인 값이 된다. 예를 들면 투명 모드에서 사 용되는 함수는 다음과 같이 구성해야 한다.

**매개 변수**

- `srcpxl` - [in] 프레임 버퍼에 있는 픽셀 값
- `destpxl` - [in] 프레임 버퍼에 쓰려고 하는 픽셀 값
- `param1` - [in] 함수를 제어하는 매개 변수

**반환 값**

최종적으로 프레임 버퍼에 쓰여질 픽셀 값 int alphaOp(int srcpxl, int orgpxl, int param1){ return (srcpxl * (255 - param1) + orgpxl * param1) / 255; }

**부작용**

없음

**참고 항목**

없음

### MC_GrpContext

**프로토타입**

```c
typedef struct _MC_GrpContext MC_GrpContext
```

**설명**

그래픽 컨텍스트 그리기 시에 다양한 매개 변수들을 효율적으로 전달하기 위한 구조체이다. 대부분 그리기 함수는 이 구조체를 매개 변수로 받다. 이 구조체에는 그리는데 필요한 매개 변수 클리핑, 전경색, 폰트, 스타일, 상대 좌표 체계 등을 가진다.

### MC_GRP_DIRECT_COLOR_TYPE

**프로토타입**

```c
#define MC_GRP_DIRECT_COLOR_TYPE
```

**설명**

팔레트를 사용하지 않는 경우의 컬러 타입. 1로 정의한다.

### MC_GRP_GRAY_TYPE

**프로토타입**

```c
#define MC_GRP_GRAY_TYPE
```

**설명**

흑백 타입. 2로 정의한다.

### MC_GRP_COLOR_TYPE

**프로토타입**

```c
#define MC_GRP_COLOR_TYPE
```

**설명**

컬러 타입. 4로 정의한다.

### MC_GrpDisplayInfo

**프로토타입**

```c
struct _MC_GrpDisplayInfo int m_bpp // 픽셀당 비트 수 int m_depth // 실제적인 픽셀당 사용 비트 수 int m_width // 화면의 픽셀 단위 폭 int m_height // 화면의 픽셀 단위 높이 int m_bpl // 프레임 버퍼의 화면의 한 줄당 바이트 수 int m_colortype //컬러타입;MC_GRP_DIRECT_COLOR_TYPE,
MC_GRP_GRAY_TYPE, MC_GRP_COLOR_TYPE int m_redmask // 빨간 색상 매스크 int m_bluemask // 파랑 색상 매스크 int m_greenmask // 녹색 색상 매스크
```

**설명**

화면 정보 구조체

### MC_GrpFrameBuffer

**프로토타입**

```c
typedef M_Int32 MC_GrpFrameBuffer
```

**설명**

프레임 버퍼. 내부에 높이와 넓이와 프레임 버퍼 포인터를 가진다.

### MC_GRP_GET_FRAME_BUFFER_POINTER

**프로토타입**

```c
#define MC_GRP_GET_FRAME_BUFFER_POINTER(a)
```

**설명**

프레임 버퍼의 포인터를 돌려준다. NULL을 반환하는 경우 응용 프로그램의 포인터를 이용한 직접 접근을 허용하지 않는다.

**매개 변수**

- `a` - [in] `MC_GrpFrameBuffer`

**반환 값**

직접 접근 허용이 되는 경우는 프레임 버퍼의 내용이 있는 포인터를 접근 허 용이 되지 않는 경우는 NULL을 반환한다.

**부작용**

`MC_grpGetScreenFrameBuffer`()를 통해서 얻어진 스크린 프레임 버퍼의 포인 터는 NULL을 반환한다

### MC_GRP_GET_FRAME_BUFFER_WIDTH

**프로토타입**

```c
#define MC_GRP_GET_FRAME_BUFFER_WIDTH(a)
```

**설명**

프레임 버퍼의 폭을 돌려준다.

**매개 변수**

- `a` - [in] `MC_GrpFrameBuffer`

**반환 값**

프레임 버퍼 포인터

### MC_GRP_GET_FRAME_BUFFER_HEIGHT

**프로토타입**

```c
#define MC_GRP_GET_FRAME_BUFFER_HEIGHT(a)
```

**설명**

프레임 버퍼의 높이를 돌려준다.

**매개 변수**

- `a` - [in] `MC_GrpFrameBuffer`

**반환 값**

프레임 버퍼 높이

### MC_GRP_GET_FRAME_BUFFER_BPL

**프로토타입**

```c
#define MC_GRP_GET_FRAME_BUFFER_BPL(a)
```

**설명**

프레임 버퍼의 한 줄당 바이트 수를 돌려준다.

**매개 변수**

- `a` - [in] `MC_GrpFrameBuffer`

**반환 값**

프레임 버퍼 한 줄당 바이트 수

### MC_GRP_GET_FRAME_BUFFER_BPP

**프로토타입**

```c
#define MC_GRP_GET_FRAME_BUFFER_BPP(a)
```

**설명**

프레임의 한 픽셀당 비트 수를 돌려준다.

**매개 변수**

- `a` - [in] `MC_GrpFrameBuffer`

**반환 값**

한 픽셀당 비트 수

### MC_GRP_CONTEXT_CLIP_IDX

**프로토타입**

```c
#define MC_GRP_CONTEXT_CLIP_IDX
```

**설명**

클리핑 영역을 가리키는 사각형을 지정한다. 사각형은 왼쪽 상단의 점과 오른쪽 하단의 점으로 기술되며, 왼쪽 상단의 점은 사각 형에 포함되지만, 오른쪽 하단의 점은 사각형에 포함되지 않는다. 0으로 정의한다.

### MC_GRP_CONTEXT_FG_PIXEL_IDX

**프로토타입**

```c
#define MC_GRP_CONTEXT_FG_PIXEL_IDX
```

**설명**

전경색 픽셀 값을 지정한다. 1로 정의한다.

### MC_GRP_CONTEXT_BG_PIXEL_IDX

**프로토타입**

```c
#define MC_GRP_CONTEXT_BG_PIXEL_IDX
```

**설명**

후경색 픽셀 값을 지정한다. 2로 정의한다.

### MC_GRP_CONTEXT_ALPHA_IDX

**프로토타입**

```c
#define MC_GRP_CONTEXT_ALPHA_IDX
```

**설명**

그리기의 투명 정도를 지정한다. 0이면 화면에 나오지 않고, 255이면 화면에 투명하지 않게 출력된다. 4로 정의한다.

### MC_GRP_CONTEXT_PIXELOP_IDX

**프로토타입**

```c
#define MC_GRP_CONTEXT_PIXELOP_IDX
```

**설명**

픽셀 연산(Operation)함수를 지정한다. 5로 정의한다.

**참고 항목**

`MC_GrpPixelOpFunc`

### MC_GRP_CONTEXT_PIXEL_PARAM1_IDX

**프로토타입**

```c
#define MC_GRP_CONTEXT_PIXEL_PARAM1_IDX
```

**설명**

픽셀 연산 함수의 매개 변수를 지정한다. 픽셀 연산 함수가 불릴 때 넘어가는 세 번째 파라미터를 지정한다. 6으로 정의한다.

### MC_GRP_CONTEXT_FONT_IDX

**프로토타입**

```c
#define MC_GRP_CONTEXT_FONT_IDX
```

**설명**

폰트 식별자를 지정한다. MC_getFont함수를 통해서 얻어오는 폰트 식별자를 지정한다. 7로 정의한다.

### MC_GRP_CONTEXT_STYLE_IDX

**프로토타입**

```c
#define MC_GRP_CONTEXT_STYLE_IDX
```

**설명**

선 그리기 스타일을 지정한다. `MC_GRP_SOLID_STYLE` 혹은 MC_GRP_DOTTED_STYLE둘 중에 하나가 된다. 8로 정의한다.

### MC_GRP_CONTEXT_XOR_MODE_IDX

**프로토타입**

```c
#define MC_GRP_CONTEXT_XOR_MODE_IDX
```

**설명**

그리기 모드를 지정한다. 그리기 시 XOR로 그릴지 여부를 정의한다. 1이면 XOR로 그리고, 그렇지 않으면 일 반적인 모드로 그린다. 9로 정의한다.

### MC_GRP_CONTEXT_OFFSET_IDX

**프로토타입**

```c
#define MC_GRP_CONTEXT_OFFSET_IDX
```

**설명**

그리기 상대 좌표의 원점(Offset)을 지정한다. 상대 좌표의 점 좌표를 정수 어레이에 넣어서 지정한다. 10으로 정의한다.

### MC_GRP_SOLID_STYLE

**프로토타입**

```c
#define MC_GRP_SOLID_STYLE
```

**설명**

선 그리기 시에 동일한 색상으로 그린다. MG_FB_SOLID_STYLE로 정의한다.

### MC_GRP_DOTTED_STYLE

**프로토타입**

```c
#define MC_GRP_DOTTED_STYLE
```

**설명**

선 그리기 시에 한 점 그린 후 다음 점은 그리지 않는 식으로 반복해서 그린다. MG_FB_DOTTED_STYLE로 정의한다.

### MC_GRP_FT_SIZE_SMALL

**프로토타입**

```c
#define MC_GRP_FT_SIZE_SMALL
```

**설명**

작은 폰트 크기를 지정한다. 8로 정의한다.

### MC_GRP_FT_SIZE_MEDIUM

**프로토타입**

```c
#define MC_GRP_FT_SIZE_MEDIUM
```

**설명**

중간 폰트 크기를 지정한다. 0으로 정의한다.

### MC_GRP_FT_SIZE_LARGE

**프로토타입**

```c
#define MC_GRP_FT_SIZE_LARGE
```

**설명**

큰 폰트 크기를 지정한다. 16으로 정의한다.

### MC_GRP_FT_FACE_SYSTEM

**프로토타입**

```c
#define MC_GRP_FT_FACE_SYSTEM
```

**설명**

시스템에서 사용하는 폰트 페이스를 지정한다. 0으로 정의한다.

### MC_GRP_FT_FACE_MONOSPACE

**프로토타입**

```c
#define MC_GRP_FT_FACE_MONOSPACE
```

**설명**

각 폰트의 폭이 균일한 폰트 페이스를 지정한다. 32로 정의한다.

### MC_GRP_FT_FACE_PROPORTIONAL

**프로토타입**

```c
#define MC_GRP_FT_FACE_PROPORTIONAL
```

**설명**

각 폰트의 폭이 균일하지 않은 폰트 페이스를 지정한다. 64로 정의한다.

### MC_GRP_FT_STYLE_PLAIN

**프로토타입**

```c
#define MC_GRP_FT_STYLE_PLAIN
```

**설명**

일반적은 스타일의 폰트를 지정한다. 0으로 정의한다.

### MC_GRP_FT_STYLE_BOLD

**프로토타입**

```c
#define MC_GRP_FT_STYLE_BOLD
```

**설명**

굵은 스타일의 폰트를 지정한다. 1로 정의한다.

### MC_GRP_FT_STYLE_ITALIC

**프로토타입**

```c
#define MC_GRP_FT_STYLE_ITALIC
```

**설명**

기울여진 스타일의 폰트를 지정한다. 2로 정의한다.

### MC_GRP_FT_STYLE_UNDERLINE

**프로토타입**

```c
#define MC_GRP_FT_STYLE_UNDERLINE
```

**설명**

밑줄이 쳐진 스타일의 폰트를 지정한다. 4로 정의한다.

### MC_GRP_IMAGE_DONE

**프로토타입**

```c
#define MC_GRP_IMAGE_DONE
```

**설명**

전체 이미지 소스 디코딩이 끝났음을 알린다. 1로 정의한다.

### MC_GRP_FRAME_DONE

**프로토타입**

```c
#define MC_GRP_FRAME_DONE
```

**설명**

이미지 소스에서부터 한 프레임이 이미지가 완성되었음을 알린다. 0으로 정의한다.

### MC_GrpImage

**프로토타입**

```c
typedef void * MC_GrpImage
```

**설명**

이미지이다. 이미지는 내부에 프레임 버퍼와 기타 속성(애니메이션 여부 등)가지고 있다.

### MC_GRP_IS_ANIMATED

**프로토타입**

```c
#define MC_GRP_IS_ANIMATED
```

**설명**

애니메이션 여부의 이미지의 속성. 1로 정의한다.

### MC_GRP_ANIMATE_DELAY

**프로토타입**

```c
#define MC_GRP_ANIMATE_DELAY
```

**설명**

애니메이션 지연 단위 이미지의 속성. 2로 정의한다.

### MC_GRP_LOOP_COUNT

**프로토타입**

```c
#define MC_GRP_LOOP_COUNT
```

**설명**

애니메이션 루프 카운트 이미지의 속성. 3로 정의한다.

### MC_grpGetImageProperty

**프로토타입**

```c
int MC_grpGetImageProperty(MC_GrpImage img, M_Int32 index)
```

**설명**

이미지의 속성을 돌려준다. 애니메이션 여부 : 1이면 애니메이션, 0이면 애니메이션이 `MC_GRP_IS_ANIMATED` 아님 `MC_GRP_ANIMATE_DELAY` 애니메이션 지연 단위 : 밀리 세컨드 단위 `MC_GRP_LOOP_COUNT` 애니메이션 전체 루프 카운트 `MC_GRP_IMAGE_WIDTH` 이미지의 넓이 `MC_GRP_IMAGE_HEIGHT` 이미지의 높이 `MC_GRP_IMAGE_BPP` 픽셀당 비트 수(Bit per Pixel) `MC_GRP_CURRENT_FRAME` 애니메이션의 현재 Frame Index. 첫번째 프레임은 0

**매개 변수**

- `img` - 이미지
- `index` - 이미지 속성

**반환 값**

속성 값

**부작용**

없음

**참고 항목**

없음

### MC_grpGetImageFrameBuffer

**프로토타입**

```c
MC_GrpFrameBuffer MC_grpGetImageFrameBuffer(MC_GrpImage img)
```

**설명**

이미지의 프레임 버퍼를 돌려준다.

**매개 변수**

- `img` - 이미지

**반환 값**

이미지의 프레임 버퍼

**부작용**

없음

**참고 항목**

없음

### MC_grpGetScreenFrameBuffer

**프로토타입**

```c
MC_GrpFrameBuffer MC_grpGetScreenFrameBuffer(M_Int32 i)
```

**설명**

현재 화면 프레임 버퍼를 얻어 온다. 각 i에 해당하는 화면 프레임 버퍼를 얻어 온다.

**매개 변수**

- `I` - [in] 화면 프레임 버퍼 0인 경우에 주 LCD화면 프레임 버퍼이고, 1인 경우에는 외부 보조 LCD화면 프레임 버퍼.

**반환 값**

화면에 대응되는 프레임 버퍼; i에 대응하는 화면 프레임 버퍼가 없는 경우 NULL을 돌려준다.

**부작용**

없음

**참고 항목**

없음

### MC_grpDestroyOffScreenFrameBuffer

**프로토타입**

```c
void MC_grpDestroyOffScreenFrameBuffer(MC_GrpFrameBuffer fb)
```

**설명**

생성된 오프 스크린 프레임 버퍼를 파괴한다. 만일 매개 변수로 화면 프레임 버퍼를 넣으면 아무런 동작도 하지 않는다.

**매개 변수**

- `fb` - [in] 파괴할 오프 스크린 프레임 버퍼.

**부작용**

없음

**참고 항목**

없음

### MC_grpCreateOffScreenFrameBuffer

**프로토타입**

```c
MC_GrpFrameBuffer MC_grpCreateOffScreenFrameBuffer(M_Int32 w, M_Int32 h)
```

**설명**

오프 스크린 프레임 버퍼를 생성한다. 지정된 폭과 높이의 오프 스크린 프레임 버퍼를 메모리에 생성한다. 이때 생성되는 오프 스크린 프레임 버퍼는 주 화면 LCD와 같은 색상수를 가질 수 있다. w와 h는 0보다는 큰 수이어야 한다.

**매개 변수**

- `w` - [in] 프레임 버퍼의 폭
- `h` - [in] 프레임 버퍼의 높이

**반환 값**

새로 생성된 프레임 버퍼; w, h가 0보다 작은 경우나 생성시 메모리가 부족하 면 NULL을 돌려준다.

**부작용**

없음

**참고 항목**

없음

### MC_grpInitContext

**프로토타입**

```c
void MC_grpInitContext(MC_GrpContext* pgc)
```

**설명**

그래픽 컨텍스트를 초기화 한다. 그래픽 컨텍스트의 모든 필드들을 초기화 한다. 폰트, 상대 좌표의 원점, 색상, 스트 로크 스타일, Alpha값, XORMode, 클리핑 영역 등을 기본값으로 초기화 한다. 폰트는 기본 시스템 폰트가 되고, 색상은 검정색, 그리기 모드는 일반 모드, 클리핑 영역은 해제되고, 상대 좌표의 원점은 (0, 0)이 된다.

**매개 변수**

- `pgc` - [in] 초기화 할 MC_GrpContext의 포인터

**부작용**

없음

**참고 항목**

없음

### MC_grpSetContext

**프로토타입**

```c
void MC_grpSetContext(MC_GrpContext* pgc, M_Int32 index, void* pv)
```

**설명**

그래픽 컨텍스트 값을 변경한다. 그래픽 컨텍스트의 특정 부분을 변경한다. index값에 의해서 pv에 들어 가는 내용이 달라진다. idx 값 pv 값 클리핑 영역으로써 pv에는 정수의 어레이가 들어간다. 이때 이 정수의 어레이는 복사된다. 정수의 어레이 첫 번째, 두 번째에는 클리핑 사각형의 왼쪽 상단의 x, y `MC_GRP_CONTEXT_CLIP_IDX` 축 좌표가 들어 가며, 세 번째 네 번째에는 사각형 오 른쪽 하단점의 x, y축 좌표가 들어 간다. 이때 왼쪽 상단의 점은 클리핑 영역에 포함되지만, 오른쪽 하단 의 점은 클리핑 영역에 포함되지 않는다. `MC_GRP_CONTEXT_FG_PIXEL_IDX` 전경 픽셀 값을 지정한다. `MC_GRP_CONTEXT_BG_PIXEL_IDX` 배경 픽셀 값을 지정한다. 투명한 정도를 지정한다. 투명정도는 0에서부터 255 의 값으로 0인 경우는 나타나지 않으며 255인 경우에 `MC_GRP_CONTEXT_ALPHA_IDX` 는 화면에 불투명하게 나타난다. 투명정도를 지정하면 내부에서 MC_GRP_CONTEXT_PIXELOP_IDX와 MC_GRP_CONTEXT_PIXEL_PARAM1_IDX가 지정된다. `MC_GRP_CONTEXT_FONT_IDX` 폰트 식별자를 지정한다. 스트로크 스타일를 지정한다. 값은 `MC_GRP_CONTEXT_STYLE_IDX` `MC_GRP_SOLID_STYLE`, MC_GRP_DOTTED_STYLE중 에 하나 이다. 픽셀 연산 함수를 지정한다. 함수의 포인터를 지정한 `MC_GRP_CONTEXT_PIXELOP_IDX` 다. 상대 좌표의 원점을 지정한다. pv에는 정수의 어레이 `MC_GRP_CONTEXT_OFFSET_IDX` 가 들어간다. 첫 번째는 원점의 x축 좌표, 두 번째에 는 원점의 y축 좌표가 지정된다.

**매개 변수**

- `index` - [in] 인덱스; `MC_GRP_CONTEXT_CLIP_IDX`, `MC_GRP_CONTEXT_FG_PIXEL_IDX`, `MC_GRP_CONTEXT_BG_PIXEL_IDX`, `MC_GRP_CONTEXT_ALPHA_IDX`, `MC_GRP_CONTEXT_FONT_IDX`, `MC_GRP_CONTEXT_STYLE_IDX`, `MC_GRP_CONTEXT_PIXELOP_IDX`, `MC_GRP_CONTEXT_OFFSET_IDX`
- `pv` - [in] 인덱스에 해당하는 값

**부작용**

없음

**참고 항목**

`MC_GrpContext`, `MC_GrpGetContext`

### MC_grpGetContext

**프로토타입**

```c
void MC_grpGetContext(MC_GrpContext* pgc, M_Int32 index, void* pv)
```

**설명**

그래픽 컨텍스트의 값을 구한다. 그래픽 컨텍스트의 특정 부분의 값을 읽어온다. index값에 의해서 pv에 들어 가는 내 용이 달라진다. 자세한 내용은 MC_grpSetContext참조.

**매개 변수**

- `index` - [in] 인덱스; `MC_GRP_CONTEXT_CLIP_IDX`, `MC_GRP_CONTEXT_FG_PIXEL_IDX`, `MC_GRP_CONTEXT_BG_PIXEL_IDX`, `MC_GRP_CONTEXT_ALPHA_IDX`, `MC_GRP_CONTEXT_FONT_IDX`, `MC_GRP_CONTEXT_STYLE_IDX`, `MC_GRP_CONTEXT_PIXELOP_IDX`, `MC_GRP_CONTEXT_OFFSET_IDX`
- `pv` - [out] 인덱스에 해당하는 값

**부작용**

없음

**참고 항목**

`MC_GrpContext`, `MC_grpSetContext`

### MC_grpPutPixel

**프로토타입**

```c
void MC_grpPutPixel(MC_GrpFrameBuffer dst, M_Int32 x, M_Int32 y,
MC_GrpContext* pgc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)에 점을 찍다. pgc가 지정하는 그래픽 컨텍스트가 지정하는 색상과 투명 정도로 x, y가 지정하는 위 치에 점을 찍는다. 점 찍는 부분이 화면을 넘어가는 경우에 프레임 버퍼 내에는 아 무것도 그려지지 않는다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `x` - [in] 점의 x축 좌표
- `y` - [in] 점의 y축 좌표
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpDrawLine

**프로토타입**

```c
void MC_grpDrawLine(MC_GrpFrameBuffer dst, M_Int32 x1, M_Int32 y1,
M_Int32 x2, M_Int32 y2, MC_GrpContext* pgc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)에 선을 그린다. pgc가 지정하는 그래픽 컨텍스트가 지정하는 색상, 스타일과 투명 정도/그리기 모드 로 (x1, y2), (x2, y2)를 연결하는 선을 그린다. 선 그리는 영역이 화면을 넘어가는 경 우에 프레임 버퍼 내에는 아무것도 그려지지 않는다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `x1` - [in] 시작점의 x축 좌표
- `y1` - [in] 시작점의 y축 좌표
- `x2` - [in] 끝점의 x축 좌표
- `y2` - [in] 끝점의 y축 좌표
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpDrawRect

**프로토타입**

```c
void MC_grpDrawRect(MC_GrpFrameBuffer dst, M_Int32 x, M_Int32 y,
M_Int32 w, M_Int32 h, MC_GrpContext* pgc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)에 사각형을 그린다. pgc가 지정하는 그래픽 컨텍스트가 지정하는 색상, 스타일과 투명정도/그리기 모드로 (x,y) 부터 시작해서 폭 w, 높이 h인 사각형을 그린다. 이때 (x+w-1,y+h-1)까지 포함 된다. w나 h가 음수 값이면 화면에 아무것도 그리지 않는다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `x` - [in] 시작점의 x축 좌표
- `y` - [in] 시작점의 y축 좌표
- `w` - [in] 사각형의 폭
- `h` - [in] 사각형의 높이
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpFillRect

**프로토타입**

```c
void MC_grpFillRect(MC_GrpFrameBuffer dst, M_Int32 x, M_Int32 y, M_Int32 w, M_Int32 h, MC_GrpContext* pgc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)에 사각형을 칠한다. pgc가 지정하는 그래픽 컨텍스트가 지정하는 색상과 투명정도/그리기 모드로 (x,y) 부터 시작해서 폭 w, 높이 h인 사각형을 그린다. 이때 (x+w,y+h)까지 포함되지 않고, (x+w-1, y+h-1)까지 포함된다. w나 h가 0이하이면 화면에 아무것도 그리지 않는다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `x` - [in] 시작점의 x축 좌표
- `y` - [in] 시작점의 y축 좌표
- `w` - [in] 사각형의 폭
- `h` - [in] 사각형의 높이
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpCopyFrameBuffer

**프로토타입**

```c
void MC_grpCopyFrameBuffer( MC_GrpFrameBuffer dst, M_Int32 dx, M_Int32 dy, M_Int32 w, M_Int32 h, MC_GrpFrameBuffer src, M_Int32 sx, M_Int32 sy,
MC_GrpContext* pgc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)에 이미지를 그린다. pgc가 지정하는 그래픽 컨텍스트가 지정하는 투명정도와 투명색으로 (dx, dy)부터 시 작해서 폭 w, 높이 h인 영역에 img가 가리키는 프레임 버퍼에서 (sx, sy)의 위치의 내용을 복사한다. 이때 dst와 src는 같은 버퍼를 가리키면 안 된다. 이 경우에는 MC_grpCopyArea함수 를 사용해야 한다. w나 h가 0이하이거나 복사할 영역이 src의 영역을 벗어나는 경우에 화면에 아무것도 그리지 않는다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `dx` - [in] 영역의 x축 좌표
- `dy` - [in] 영역의 y축 좌표
- `w` - [in] 영역의 폭
- `h` - [in] 영역의 높이
- `src` - [in] 소스 프레임 버퍼의 영역
- `sx` - [in] 소스 영역의 x축 좌표
- `sy` - [in] 소스 영역의 y축 좌표
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

`MC_grpCopyArea`

### MC_grpDrawImage

**프로토타입**

```c
void MC_grpDrawImage( MC_GrpFrameBuffer dst, M_Int32 dx, M_Int32 dy,
M_Int32 w, M_Int32 h, MC_GrpImage src, M_Int32 sx, M_Int32 sy,
MC_GrpContext* pgc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)에 이미지를 그린다. pgc가 지정하는 그래픽 컨텍스트가 지정하는 투명정도와 투명색으로 (dx, dy)부터 시 작해서 폭 w, 높이 h인 영역에 img가 가리키는 프레임 버퍼에서 (sx, sy)의 위치의 내용을 복사한다. 이때 이미지 내부에 매스크 이미지가 있다면 이 매스크 이미지에 의해서 출력되는 내용이 변경된다. w나 h가 0이하이거나 복사할 영역이 src의 영역을 벗어나거나 mask plane의 영역을 벗어나거나 mask가 1bit plane이 아니거나 src가 화면과 같은 DEPTH가 아닌 경우에 화면에 아무것도 그리지 않는다.

**매개 변수**

- `ds` - [in] 프레임 버퍼
- `dx` - [in] 영역의 x축 좌표
- `dy` - [in] 영역의 y축 좌표
- `w` - [in] 영역의 폭
- `h` - [in] 영역의 높이
- `src` - [in] 소스 프레임 버퍼의 영역
- `sx` - [in] 소스 영역의 x축 좌표
- `sy` - [in] 소스 영역의 y축 좌표
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpDrawImageRegion

**프로토타입**

```c
void MC_grpDrawImageRegion(MC_GrpFrameBuffer destbuf, M_Int32 destX,
M_Int32 destY, M_Int32 width, M_Int32 height, MC_GrpImage srcbuf, M_Int32 srcX, M_Int32 srcY, M_Int32 transform, MC_GrpContext *gc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)에 지정한 변환을 수행 후 이미지를 그린다. gc가 지정하는 그래픽 컨텍스트가 지정하는 투명정도와 투명색으로 (destX, destY)부 터 시작해서 폭 weight, 높이 height인 영역에 img가 가리키는 프레임 버퍼에서 (srcX, srcY)의 위치의 내용을 복사한다. 이때 이미지 내부에 매스크 이미지가 있다면 이 매스크 이미지에 의해서 출력되는 내용이 변경된다. 지정된 변환 후 destbuf에 최종적으로 복사된다. 가능한 변환은 다음과 같이 transform의 값에 의하여 결정된다. `MC_GRP_TRAN_ROT90` 오른쪽으로 90도 회전 `MC_GRP_TRAN_ROT180` 오른쪽으로 180도 회전 `MC_GRP_TRAN_ROT270` 오른쪽으로 270도 회전 `MC_GRP_TRAN_MIR` 좌우 미러링 `MC_GRP_TRAN_MIR_ROT90` 좌우 미러링 후 오른쪽으로 90도 회전 `MC_GRP_TRAN_MIR_ROT180` 좌우 미러링 후 오른쪽으로 180도 회전 `MC_GRP_TRAN_MIR_ROT180` 좌우 미러링 후 오른쪽으로 270도 회전 width나 height가 0이하이거나 복사할 영역이 src의 영역을 벗어나거나 mask plane의 영역을 벗어나거나 mask가 1bit plane이 아니거나 src가 화면과 같은 DEPTH가 아닌 경우에 화면에 아무것도 그리지 않는다.

**매개 변수**

- `destbuf` - [in] 프레임 버퍼
- `destX` - [in] 영역의 x축 좌표
- `destY` - [in] 영역의 y축 좌표
- `width` - [in] 영역의 폭
- `height` - [in] 영역의 높이
- `srcbuf` - [in] 소스 프레임 버퍼의 영역
- `srcX` - [in] 소스 영역의 x축 좌표
- `srcY` - [in] 소스 영역의 y축 좌표
- `transform` - [in] 회전, mirror효과등을 지정
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpCopyArea

**프로토타입**

```c
void MC_grpCopyArea(MC_GrpFrameBuffer dst, M_Int32 dx, M_Int32 dy,
M_Int32 w, M_Int32 h, M_Int32 x, M_Int32 y, MC_GrpContext* pgc)
```

**설명**

지정된 프레임의 내용을 자기 자신으로 복사한다. dst가 가리키는 프레임 버퍼의 (dx, dy)에 dst의 (x, y)부터 폭 w, 높이 h의 내용을 복 사한다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `dx` - [in] 새로 복사되는 이미지의 x축 좌표
- `dy` - [in] 새로 복사되는 이미지의 y축 좌표
- `w` - [in] 새로 복사되는 이미지의 폭
- `h` - [in] 새로 복사되는 이미지의 높이
- `x` - [in] 복사할 영역의 x축 좌표
- `y` - [in] 복사할 영역의 y축 좌표
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpDrawArc

**프로토타입**

```c
void MC_grpDrawArc(MC_GrpFrameBuffer dst, M_Int32 x, M_Int32 y, M_Int32 w, M_Int32 h, M_Int32 s, M_Int32 e, MC_GrpContext* pgc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)에 아크를 그린다. pgc가 지정하는 그래픽 컨텍스트가 지정하는 스타일, 투명정도와 색상/그리기 모드로 아크를 그린다. 이때 아크는 s에서 시작해서 e만큼 그리며, 각도는 0도가 3시 방향이 된다. 양수 값 은 시계 반대 방향이고, 음수 값은 시계 방향이다 (x,y)가 시작점이고 높이 height, 넓이 width인 사각형의 중심이 아크의 중심이 된다. 된다. 아크는 drawRect할 때와 마찬가지로 (x + width, y + height)높이를 가지는 영역을 차 지 한다. 만일 폭이나 높이가 0보다 작은 경우에 아무것도 그려지지 않는다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `x` - [in] 영역의 x축 좌표
- `y` - [in] 영역의 y축 좌표
- `w` - [in] 아크의 폭
- `h` - [in] 아크의 높이
- `s` - [in] 시작 각도 (0-360단위:도)
- `e` - [in] 아크의 각도 (0-360단위:도)
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpFillArc

**프로토타입**

```c
void MC_grpFillArc(MC_GrpFrameBuffer dst, M_Int32 x, M_Int32 y, M_Int32 w,
M_Int32 h, M_Int32 s, M_Int32 e, MC_GrpContext* pgc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)에 아크를 칠한다. pgc가 지정하는 그래픽 컨텍스트가 지정하는 투명정도와 색상/그리기 모드로 아크를 칠한다. 이때 아크는 s에서 시작해서 e만큼 그리며, 각도는 0도가 3시 방향이 된다. 양수 값 은 시계 반대 방향이고, 음수 값은 시계 방향이다 아크의 중심은 (x,y)가 시작점이고 높이 height, 넓이 width인 사각형의 중심이 된다. 아크는 fillRect할 때와 마찬가지로 (x + width - 1, y + height - 1)높이를 가지는 영역을 차지 한다. 만일 폭이나 높이가 0이하인 경우에 아무것도 그려지지 않는다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `x` - [in] 영역의 x축 좌표
- `y` - [in] 영역의 y축 좌표
- `w` - [in] 아크의 폭
- `h` - [in] 아크의 높이
- `s` - [in] 시작 각도 (0-360단위:도)
- `e` - [in] 아크의 각도 (0-360단위:도)
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpDrawString

**프로토타입**

```c
void MC_grpDrawString(MC_GrpFrameBuffer dst, M_Int32 x, M_Int32 y, const M_Char* str, M_Int32 len, MC_GrpContext* pgc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)에 문자열을 그려준다. pgc가 지정하는 그래픽 컨텍스트가 지정하는 투명정도와 색상/그리기 모드와 지정된 폰트로 문자열을 그린다. str은 일반적인 "C" 문자열이 되며 Unicode를 출력하기 위해서는 drawUnicodeString 함수를 사용하십시오. len이 -1이면 문자가 NULL일때 까지 문자열을 처리하며, len이 0이거나 -1이 아닌 음 수이면 화면에 아무것도 출력되지 않는다.

**매개 변수**

- `pd` - [in] 프레임 버퍼
- `bpl` - [in] 프레임 버퍼의 한 줄당 차지하는 바이트 개수
- `x` - [in] 문자열의 x축 좌표
- `y` - [in] 문자열의 baseline의 y축 좌표
- `str` - [in] "C" 문자열
- `len` - [in] 문자열의 길이
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpDrawUnicodeString

**프로토타입**

```c
void MC_grpDrawUnicodeString(MC_GrpFrameBuffer dst, M_Int32 x, M_Int32 y, const M_UCode* str, M_Int32 len, MC_GrpContext* pgc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)에 문자열을 그려준다. pgc가 지정하는 그래픽 컨텍스트가 지정하는 투명정도와 색상/그리기 모드로 지정된 폰트로 문자열을 그린다. str은 유니 코드 문자열이 되며 일반 "C" 문자열을 출력하기 위해서 drawString함수 를 사용하십시오. 일반 응용 프로그램에서 이 함수를 제공할 필요는 없지만, 자바 프 로그램 작성시에 "C"언어와 혼용하여 작성하는 경우에 보다 빠른 그리기를 위해서 제공한다. len이 -1이면 문자가 NULL일때 까지 문자열을 처리하며, len이 0이거나 -1 이 아닌 음수이면 화면에 아무것도 출력되지 않는다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `x` - [in] 문자열의 x축 좌표
- `y` - [in] 문자열의 baseline의 y축 좌표
- `str` - [in] 유니코드 문자열
- `len` - [in] 문자열의 길이
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpGetRGBPixels

**프로토타입**

```c
void MC_grpGetRGBPixels(MC_GrpFrameBuffer dst, M_Int32 x, M_Int32 y,
M_Int32 w, M_Int32 h, M_Uint32* pd, M_Int32 ipl)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)의 여러 픽셀 색상을 동시에 가져온다. 임의 프레임 버퍼의 영역의 색상 값들을 정수 어레이에 복사한다. 이때 색상 값은 0x00RRGGBB 형태이다. 만일 가져오는 영역이 프레임 버퍼의 영역을 넘어 가거나 폭이 ipl보다 큰 경우에는 복사되는 값은 프로그램 수행마다 임의적으로 결정된다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `x` - [in] 가져올 영역의 x축 좌표
- `y` - [in] 가져올 영역의 y축 좌표
- `w` - [in] 가져올 영역의 폭
- `h` - [in] 가져올 영역의 높이
- `pd` - [out] 정수 어레이
- `ipl` - [in] 이미지 한 줄당 정수의 개수

**부작용**

없음

**참고 항목**

없음

### MC_grpSetRGBPixels

**프로토타입**

```c
void MC_grpSetRGBPixels(MC_GrpFrameBuffer dst, M_Int32 x, M_Int32 y,
M_Int32 w, M_Int32 h, const M_Uint32* psrc, M_Int32 ibpl, MC_GrpContext* pgc)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)의 여러 픽셀의 색상을 동시에 지정한다. 정수 어레이에 저장되어 있는 색상들을 임의 프레임 버퍼 영역에 복사한다. LCD의 컬러 수에 따라서 색상은 가장 근접한 색상 값으로 변경되어 지정된다. 이때 색상 값은 0x00RRGGBB 형태이다. 가져올 영역이 프레임 버퍼를 벗어 나거나 만일 ibpl이 w보다 작은 값이거나 제대로 된 이미지를 복사하지 않는다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `x` - [in] 수정될 영역의 x축 좌표
- `y` - [in] 수정될 영역의 y축 좌표
- `w` - [in] 수정될 영역의 폭
- `h` - [in] 수정될 영역의 높이
- `pd` - [in] 정수 어레이
- `ibpl` - [in] 이미지 한 줄당 바이트 수
- `pgc` - [in] 그래픽 컨텍스트

**부작용**

없음

**참고 항목**

없음

### MC_grpFlushLcd

**프로토타입**

```c
void MC_grpFlushLcd(M_Int32 i, MC_GrpFrameBuffer frm, M_Int32 x, M_Int32 y, M_Int32 w, M_Int32 h)
```

**설명**

지정된 프레임 버퍼(Frame Buffer)를 LCD 화면에 출력한다. 임의 프레임 버퍼의 내용의 일부분을 LCD화면에 출력한다. 이때 프레임 버퍼의 한 줄당 차지하는 바이트 수와 LCD의 한 줄당 차지하는 바이트 수는 동일해야 한다. 사용자는 여러 개의 화면 프레임 버퍼를 사용할 수도 있고, 하나의 화면 프레임 버 퍼만을 사용할 수 있다.

**매개 변수**

- `i` - [in] 화면 인덱스(0; 주화면 1; 보조LCD화면)
- `frm` - [in] 프레임 버퍼
- `x` - [in] 출력할 영역의 x축 좌표
- `y` - [in] 출력할 영역의 y축 좌표
- `w` - [in] 출력할 영역의 폭
- `h` - [in] 출력할 영역의 높이

**부작용**

없음

**참고 항목**

없음

### MC_grpGetPixelFromRGB

**프로토타입**

```c
M_Int32 MC_grpGetPixelFromRGB(M_Int32 r, M_Int32 g, M_Int32 b)
```

**설명**

지정된 색상의 픽셀 값을 얻어 온다. 만일 r, g, b가 255를 넘어가면 제대로 된 픽셀 값을 얻어 오지 않는다. 해당 함수로 반환된 pixel값으로 `MC_grpGetRGBFromPixel` 함수를 호출하여 RGB값을 얻을 경우, 처음 r, g, b 값과 동일하지 않을 수 있다.

**매개 변수**

- `r` - [in] red값(0-255)
- `g` - [in] green값(0-255)
- `b` - [in] blue값(0-255)

**반환 값**

픽셀 값

**부작용**

없음

**참고 항목**

없음

### MC_grpGetRGBFromPixel

**프로토타입**

```c
M_Int32 MC_grpGetRGBFromPixel(M_Int32 pixel, M_Int32 *r, M_Int32 *g,
M_Int32 *b)
```

**설명**

지정된 픽셀 값의 색상 값들을 얻어 온다.

**매개 변수**

- `pixel` - [in] pixel값
- `r` - [out] red값(0-255)
- `g` - [out] green값(0-255)
- `b` - [out] blue값(0-255)

**반환 값**

픽셀 값 pixel과 같음

**부작용**

없음

**참고 항목**

없음

### MC_grpGetDisplayInfo

**프로토타입**

```c
M_Int32 MC_grpGetDisplayInfo(M_Int32 i, MC_GrpDisplayInfo* pi)
```

**설명**

화면 정보 구조체를 얻어 온다.

**매개 변수**

- `I` - [in] 예약된 파라미터; 0을 넣다.
- `pi` - [out] 화면 정보 구조체

**반환 값**

해당되는 정보 구조체가 있으면 1, 그렇지 않으면 0을 돌려준다.

**부작용**

없음

**참고 항목**

없음

### MC_grpRepaint

**프로토타입**

```c
void MC_grpRepaint(M_Int32 lcd, M_Int32 x, M_Int32 y, M_Int32 w, M_Int32 h)
```

**설명**

특정 영역에 대해서 paintClet함수가 불리도록 한다. 이 함수를 부르면, 함수 내에서 paintClet을 직접 부르지 않고, paintClet이 불릴 수 있도록 응용 프로그램 이벤트 큐 에 관련 이벤트를 넣어 준다.

**매개 변수**

- `I` - [in] 화면 프레임 버퍼 0인 경우에 주 LCD화면 프레임 버퍼이고, 1인 경우에는 외부 보조 LCD화면 프레임 버퍼
- `x` - [in] 영역의 x축 좌표
- `y` - [in] 영역의 y축 좌표
- `w` - [in] 영역의 폭
- `h` - [in] 영역의 높이

**부작용**

없음

**참고 항목**

없음

### MC_grpGetFont

**프로토타입**

```c
M_Int32 MC_grpGetFont(M_Int32 face, M_Int32 size, M_Int32 style)
```

**설명**

지정된 폰트와 가장 근접한 시스템 폰트를 돌려준다. face나 size, style에 제대로 된 값이 넘어 오지 않으면 기본 폰트를 돌려준다.

**매개 변수**

- `face` - [in] 폰트 페이스; `MC_GRP_FT_FACE_SYSTEM`, `MC_GRP_FT_FACE_MONOSPACE`, MC_GRP_FT_FACE_PROPORTIONAL중 하나
- `size` - [in] 폰트 크기; MC_GRP_FT_SIZE_LARGE이나 `MC_GRP_FT_SIZE_MEDIUM`, MC_GRP_FT_SIZE_SMALL중 하나.
- `style` - [in] 폰트 스타일; MC_GRP_FT_STYLE_PLAIN이나 `MC_GRP_FT_STYLE_ITALIC`, `MC_GRP_FT_STYLE_BOLD`, MC_GRP_FT_STYLE_UNDERLINED을 OR한 값.

**반환 값**

지정된 폰트 식별자

**부작용**

없음

**참고 항목**

없음

### MC_grpGetFontHeight

**프로토타입**

```c
M_Int32 MC_grpGetFontHeight(M_Int32 font)
```

**설명**

폰트 높이를 돌려준다. 만일 지정된 폰트가 유효하지 않은 값인 경우에 0을 돌려준다.

**매개 변수**

- `font` - [in] 폰트 식별자

**반환 값**

폰트 높이

**부작용**

없음

**참고 항목**

없음

### MC_grpGetFontAscent

**프로토타입**

```c
M_Int32 MC_grpGetFontAscent(M_Int32 font)
```

**설명**

폰트의 어센트(Ascent)를 돌려준다. 만일 지정된 포트가 유효하지 않은 값인 경우에는 0을 돌려준다.

**매개 변수**

- `font` - [in] 폰트 식별자

**반환 값**

폰트의 어센트

**부작용**

없음

**참고 항목**

없음

### MC_grpGetFontDescent

**프로토타입**

```c
M_Int32 MC_grpGetFontDescent(M_Int32 font)
```

**설명**

폰트의 디센트(Descent)를 돌려준다. 만일 지정된 폰트가 유효하지 않은 값인 경우에는 0을 돌려준다.

**매개 변수**

- `font` - [in] 폰트 식별자

**반환 값**

폰트의 디센트

**부작용**

없음

**참고 항목**

없음

### MC_grpGetStringWidth

**프로토타입**

```c
M_Int32 MC_grpGetStringWidth(M_Int32 font, const M_Uint8* str, M_Int32 len)
```

**설명**

문자열의 화면상의 폭을 얻어 온다. 지정된 폰트로 문자를 화면상에 출력하였을때 화면에서 차지하는 폭을 돌려준다. 만일 len값이 -1이면 문자열 끝(`NULL` 문자가 나타나는 곳까지)까지 의 폭을 돌려준 다.

**매개 변수**

- `font` - [in] 폰트 식별자
- `str` - [in] 문자열
- `len` - [in] 문자열의 길이

**반환 값**

성공

문자열의 폭
실패

- `M_E_INVALID` - 잘못된 매개 변수

**부작용**

없음

**참고 항목**

없음

### MC_grpGetUnicodeStringWidth

**프로토타입**

```c
M_Int32 MC_grpGetUnicodeStringWidth(M_Int32 font, const M_UCode* str,
M_Int32 len)
```

**설명**

유니코드 문자열의 화면상의 폭을 얻어 온다. 지정된 폰트로 유니코드 문자를 화면상에 출력하였을때 화면에서 차지하는 폭을 돌 려준다. 만일 len값이 -1이면 문자열 끝(`NULL` 문자가 나타나는 곳까지)까지 의 폭을 돌려준 다. (`NULL` 문자는 문자열의 폭에 포함되지 않는다.)

**매개 변수**

- `font` - [in] 폰트
- `str` - [in] 문자열
- `len` - [in] 문자열의 길이

**반환 값**

성공

문자열의 폭
실패

- `M_E_INVALID` - 잘못된 매개 변수

**부작용**

없음

**참고 항목**

없음

### MC_grpCreateImage

**프로토타입**

```c
M_Int32 MC_grpCreateImage(MC_GrpImage *newImg, M_Uint32 bufID, M_Int32 off, M_Int32 len)
```

**설명**

이미지를 생성한다. 이미지 데이타(PNG, BMP포맷)를 가지고 있는 버퍼를 넘겨서 이미지 구조체를 초기 화 한다. 이 함수를 부르면 맨 처음 이미지가 생성된다. 만일 이미지가 제대로 생성되지 않았 다면 NULL을 돌려준다. 매개 변수로 넘기는 buf는 이미지 함수 내에서 자동으로 해제 시켜준다. 그러므로 MC_knlCalloc으로 생성된 버퍼의 ID이어야 한다. 해제 시키는 시점은 애니메이션 이 미지가 아닌 경우에 초기 한 장 프레임을 완성 시킨 후 해제되며, 애니메이션 이미 지인 경우에는 MC_grpDestroyImage함수가 호출되면 그때 해제 된다.

**매개 변수**

- `newImg` - [out] 새로 생성된 이미지 ; 오류 시 NULL로 세팅된다.
- `bufID` - [in] 이미지 데이타를 가지고 있는 버퍼로써 MC_knlCalloc으로 할당된 버퍼ID이어야 함
- `off` - [in] 이미지 데이타의 시작 부분
- `len` - [in] 이미지 데이타의 길이

**반환 값**

`MC_GRP_IMAGE_DONE` 오류 없이 이미지가 디코딩 되었을 때
- `M_E_NOMEMORY` - 이미지를 생성하는데 메모리가 부족할 때
- `M_E_BADFORMAT` - 이미지 포맷이 잘못되었을 때

**부작용**

없음

**참고 항목**

없음

### MC_grpCreateSubImage

**프로토타입**

```c
MC_GrpImage MC_grpCreateSubImage(MC_GrpImage srcImage, M_Int32 startx, M_Int32 starty , M_Int32 widt, M_Int32 height)
```

**설명**

서브이미지를 생성한다. 만일 이미지가 제대로 생성되지 않았다면 NULL을 돌려준다. 소스이미지의 (startx, starty)에서 넓이w, 높이h의 서브이미지를 만들어내는데 소스이 미지에 Mask가 있었다면 서브이미지에 해당하는 Mask도 생성된다.

**매개 변수**

- `srcImage` - [in] 서브 이미지를 만들어낼 원본 이미지 구조체이다.
- `startx` - [in] ,starty 원본 이미지 상의 기준좌표. 서브이미지의 (0,0)좌표가 된다.
- `width` - [in] ,height 생성할 서브이미지의 넓이와 높이

**반환 값**

서브이미지 구조체

**부작용**

없음

**참고 항목**

없음

### MC_grpDestroyImage

**프로토타입**

```c
void MC_grpDestroyImage(MC_GrpImage img)
```

**설명**

이미지를 삭제한다.

**매개 변수**

- `img` - 삭제할 이미지

**부작용**

없음

**참고 항목**

없음

### MC_grpDecodeNextImage

**프로토타입**

```c
M_Int32 MC_grpDecodeNextImage(MC_GrpImage dst)
```

**설명**

이미지의 다음 프레임을 만든다. 특정 버퍼에서 데이타를 읽어 들여서 이미지를 생성한다. 만들어진 이미지는 이미지 타겟 구조체에 들어간다. 만일 움직이는 이미지인 경우에는 한번 더 부르면, 다음 이미지를 디코딩하여 dst에 저장한다. 이때 유의해야 할 점은 처음 이미지를 저장한 dst를 넘겨주어야 한다. 움 직이는 이미지 특성상 이전 이미지 위에 변경된 이미지만을 그려서 다음 이미지를 만드는 경우가 있기 때문이다.

**매개 변수**

- `dst` - [out] 이미지 타겟 구조체

**반환 값**

다음 중의 한 값이 된다. `MC_GRP_FRAME_DONE` 오류 없이 이미지가 디코딩 되었을 때 `MC_GRP_IMAGE_DONE` 오류 없이 이미지가 디코딩 되었으며, 더 이상의 디코딩할 이미지가 남아 있지 않을 때
- `M_E_NOMEMORY` - 이미지를 생성하는데 메모리가 부족할 때
- `M_E_BADFORMAT` - 이미지 포맷이 잘못되었을 때

**부작용**

없음

**참고 항목**

없음

### MC_grpEncodeImage

**프로토타입**

```c
M_Int16 MC_grpEncodeImage(MC_GrpFrameBuffer src, M_Int32 x, M_Int32 y,
M_Int32 w, M_Int32 h, M_Int32* len)
```

**설명**

지정된 프레임버퍼의 일정 영역을 그래픽 파일 포맷으로 인코딩한다. 지정한 프레임버퍼의 일정 영역을 BMP 파일 포맷으로 인코딩해서 반환한다. 반환된 이미지 버퍼의 크기는 len 파라미터로 얻어온다. 반환된 값은 MC_knlCalloc에 의해 서 생성된 버퍼ID이다.

**매개 변수**

- `src` - [in] 이미지 소스 구조체
- `x` - [in] 영역의 시작 x축 좌표
- `y` - [in] 영역의 시작 y축 좌표
- `w` - [in] 영역의 폭
- `h` - [in] 영역의 높이
- `len` - [out] 인코딩된 이미지 버퍼의 크기

**반환 값**

인코딩된 이미지 버퍼 ID, 실패하면 `NULL`

**부작용**

없음

**참고 항목**

없음

### MC_grpPostEvent

**프로토타입**

```c
M_Int32 MC_grpPostEvent(M_Int32 id, M_Int32 type, M_Int32 param1,
M_Int32 param2)
```

**설명**

지정한 응용 프로그램의 이벤트 큐에 이벤트를 넣다. 지정한 응용 프로그램이 이벤트를 받을 수 있도록 이벤트 큐에 이벤트를 넣다. 지정 한 응용 프로그램에는 해당 이벤트가 발생하여 handleCletEvent함수가 호출되고. 각 parameter는 type, param1, param2가 된다.

**매개 변수**

- `id` - [in] 응용 프로그램 식별자
- `type` - [in] 이벤트 타입
- `param1` - [in] 매개 변수1
- `param2` - [in] 매개 변수2

**반환 값**

성공

실패


**부작용**

없음

**참고 항목**

없음

### MC_grpDrawPolygon

**프로토타입**

```c
void MC_grpDrawPolygon( MC_GrpFrameBuffer dst, M_INT32* xPoints,
M_INT32* yPoints, M_Int32 nPoints, MC_GrpContext* pgc)
```

**설명**

임의의 꼭지점을 갖는 다각형을 그린다.

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `xPoints` - [in] x좌표 배열
- `yPoints` - [in] y좌표 배열
- `nPoints` - [in] 꼭지점의 개수
- `pgc` - [in] 그래픽 컨텍스트

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MC_grpDrawFillPolygon`

### MC_grpFillPolygon

**프로토타입**

```c
void MC_grpDrawFillPolygon( MC_GrpFrameBuffer dst, M_INT32* xPoints,
M_INT32* yPoints, M_INT32 nPoints, MC_GrpContext* pgc)
```

**설명**

임의의 꼭지점을 갖는 채워진 다각형을 그린다

**매개 변수**

- `dst` - [in] 프레임 버퍼
- `xPoints` - [in] x좌표 배열
- `yPoints` - [in] y좌표 배열
- `nPoints` - [in] 꼭지점의 개수
- `pgc` - [in] 그래픽 컨텍스트

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MC_grpDrawPolygon`

### MC_imGetSurpportModeCount

**프로토타입**

```c
M_Int32 MC_imGetSurpportModeCount()
```

**설명**

오토마타에서 지원되는 입력모드의 수를 얻어온다

**매개 변수**

없음

**반환 값**

입력모드의 수

**부작용**

없음

**참고 항목**

없음

### MC_imGetSupportedModes

**프로토타입**

```c
M_Char** MC_imGetSupportedModes()
```

**설명**

오토마타에서 지원하는 입력모드의 언어코드를 얻어온다. 언어코드는 ISO 639 코드 를 따른다. 단, 해당 언어가 대소문자를 구분하는 경우 각 언어코드에 "/S","/L"를 추 가하여 지정할 수 있다. 예를 들어 영문 소문자의 경우 "EN/S"의 언어코드를 넘겨주 게 된다. 한글의 경우에는 "KO"의 언어코드를 넘겨주게 된다.

**매개 변수**

없음

**반환 값**

언어코드 (스트링 어레이 포인터)

**부작용**

없음

**참고 항목**

없음

### MC_imSetCurrentMode

**프로토타입**

```c
M_Int32 MC_imSetCurrentMode (M_Int32 mode)
```

**설명**

오토마타에서 사용할 모드를 지정한다. 이 값은 `MH_IMAgetSupportedModes`()로 얻 은 언어코드의 인덱스값이다.

**매개 변수**

- `mode` - [in] 입력모드

**반환 값**

지정한 입력모드가 바르게 적용된 경우 "1". 그렇지 않은 경우 "0".

**부작용**

없음

**참고 항목**

없음

#### MC_imGetCurrentMode()

**프로토타입**

```c
M_Int32 MC_imGetCurrentMode()
```

**설명**

오토마타의 현재 입력모드를 얻어온다. 이 값은 `MH_IMAgetSupportedModes`()로 얻 은 언어코드의 인덱스값이다..

**매개 변수**

없음

**반환 값**

오토마타의 현재 입력모드

**참고 항목**

없음

### MC_imHandleInput

**프로토타입**

```c
M_Int32 MC_imHandleInput (M_Char key, M_Int32 type,char *buf1,M_Int32 *size1,char *buf2,M_Int32 *size2)
```

**설명**

사용자 컴포넌트로부터 받은 키 입력을 현재 입력모드에 따라 처리하며 문자를 생성 하고, 생성된 문자를 넘긴다. 전달된 키가 오토마타의 조합에 사용할 수 없는 키인 경우, 현재 조합중인 문자를 완성 버퍼에 설정하고 0을 반환한다.

**매개 변수**

- `key` - [in] 입력된 키 값 (MH_KeyCode에 정의된 것, `MH_IMA_FLUSH`)
- `type` - [in] 입력된 키 타입 (MH_Event에 정의된 것.)
- `buf1` - [out] 완성된 문자열버퍼
- `size1` - [in] 완성된 문자열 버퍼의 크기
- `buf2` - [out] 조합중인 문자열버퍼
- `size2` - [in] 조합중인 문자열 버퍼의 크기

**반환 값**

성공

- 1 오토마타가 처리했을 경우
실패

- 0 오토마타가 처리하지 못했을 경우

**참고 항목**

없음
