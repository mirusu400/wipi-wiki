---
title: "4. 사용 예제"
---

## 4.1. DLL 사용 예제

### 4.1.1. C API

WIPI에서는 표준으로 제정되어 단말기에 내장된 API외에 동적으로 라이브러리를 추 가하거나 갱신할 수 있는 기능을 제공해야 한다. 다음은 Clet에서 동적링킹라이브러 리(DLL)를 사용하고 개발하기 위한 예시와 필요한 API를 정의한다. 동적링킹라이브러리는 인터페이스라는 외부와 통신하는 통로를 가진다. 인터페이스 란 “함수와, 변수로 이루어진 group에 이름, 버전을 부여하여 관리하는 단위”를 말한 다. 인터페이스는 API를 추가/갱신하는데 있어서 기본 단위가 된다 예로서, 3D API를 제공하는 DLL개발자와 응용프로그램 개발자 측면에서 DLL을 구현 하고 사용하는 방법은 다음과 같다.

#### DLL Export 함수 header 정의

3D API DLL개발자는 응용프로그램 개발자에게 제공할 함수의 리스트 그룹의 head를 만든다. API3D.h <source1>

```c
typedef struct _API3D
{
M_Int32 (*draw3DLine)(M_Int32 x, M_Int32 y, M_Int32 x2, M_Int32 y2);
M_Int32 (*draw3DRect)(M_Int32 x, M_Int32 y, M_Int32 w, M_Int32 h);
…
}
```

API3D;

#### DLL Export 함수 구현

3D API DLL개발자는 “API3D.h”의 인터페이스를 제공하는 DLL을 만든다. 3D_DLL.c <source2> #Include “API3D.h” #include “Demo_Interface.h”

```c
M_Int32 dll_draw3DLine(M_Int32 x, M_Int32 y, M_Int32 x2, M_Int32 y2);
```

```c
M_Int32 dll_draw3DRect(M_Int32 x, M_Int32 y, M_Int32 w, M_Int32 h);
```

API3D api3d = { dll_draw3DLine, dll_draw3DRect }; DemoInf demoinf = { … }; `MC_EXPORT_DLL_INTERFACE_START`(module3D) `MC_DLL_INTERFACE`(api3d, “Fast3D”, 1, 0) `MC_DLL_INTERFACE`(demoinf, “TestDLL”, 1, 0) `MC_EXPORT_DLL_INTERFACE_END` `MC_EXPORT_DLL_START`(module3D) DLL_INIT(dll_init) DLL_EXIT(dll_exit) `MC_EXPORT_DLL_END`

```c
M_Int32 dll_init() {
return(0);
}
void dll_exit() {
}
M_Int32 dll_draw3DLine(M_Int32 x, M_Int32 y, M_Int32 x2, M_Int32 y2) {
MC_knlPrintk(“draw3d line\n”);
return(0);
}
M_Int32 dll_draw3DRect(M_Int32 x, M_Int32 y, M_Int32 w, M_Int32 h) {
MC_knlPrintk(“draw3d rect\n”);
return(0);
}
```

DLL을 개발하는 개발자는 DLL interface를 export해야 한다. export되는 DLL interface 는 `MC_knlGetDLLInterface`()에 의해 응용프로그램 개발자에게 노출되어 사용이 가능 하게 된다.

#### DLL 함수 사용

3D API 응용프로그램 개발자는 다음과 같이 사용한다. 3D_DLL.c는 dll option으로 컴파일되어 서버에 프로그램 이름 = “3d_library”, 버전 = “1.1”, 벤더 = “testsoft”로 등록되어 있다고 가정하면 다음과 같이 사용할 수 있다. 3D_USE.c <source3> #include “API3D.h” … API3D* inf3d;

```c
int startClet(int argc, char* argc[])
{
char buf[256];
…
rtn = MC_knlGetExecNames(“3d_library”, NULL, NULL, buf, sizeof(buf));
rtn = MC_knlLoad(buf, 0);
inf3d = MC_knlGetDLLInterface("“Fast3D", -1, -1, NULL, NULL);
inf3d->draw3DLine (0, 0, 10, 10);
rtn = int3d->draw3DRect (10, 10), 50, 60);
…
}
```

#### API 추가/갱신의 시나리오 예

내장된 API의 갱신(override)의 예로서 <source1>의 “API3D.h” 인터페이스가 내장되 어 있을 경우, <souce3>의 code는 변화가 없으나 “API3D.h” DLL/인터페이스를 다운 로드 받을 경우, “API3D.h” 인터페이스는 갱신(override)될 수 있다. 또한, 내장되지 않은 특정 DLL API를 사용하는 프로그램을 수행시킬 경우에는 해당 DLL을 다운로드한 후 프로그램을 수행시킬 수 있다.

### 4.1.2. Java API

Java는 언어적 특성에서 이미 모든 함수와 변수를 동적으로 로딩/링킹하는 기능을 가지고 있으므로 동적링킹라이브러리는 Java의 언어적 특성을 이용하여 구현된다. 예로서, 3D API를 제공하는 DLL개발자와 응용프로그램 개발자 측면에서 DLL을 구현 하고 사용하는 방법은 다음과 같다. 응용프로그램 개발자에게 제공할 3D_DLL.jar작성 3D API DLL개발자는 응용프로그램 개발자에게 제공할 3D DLL 을 만든다. Engine3D.java <source1> package api3d; public class Engine3D { public int draw3DLine(int x, int y, int x2, int y2) { … } public int draw3DRect(int x, int y, int x2, int y2) { … } } 자바는 3D_DLL.jar 라이브러리 자체가 응용프로그램 개발자에게는 C의 header역할 을 한다.

#### 3D DLL 함수 사용

3D API 응용프로그램 개발자는 다음과 같이 사용한다. DLL이 서버에 프로그램 이름 = “java_3d_library”, 버전 = “1.1”, 벤더 = “testsoft”로 등 록되어 있다고 가정하면, 다음과 같이 사용된다. USE_3D.java <source2> import api3d.Engine3D; public class USE_3D { … public int dLine(int x, int y, int x2, int y2) { String[] exeName = Kernel.getExecNames(“java_3d_llibrary”, “1.1”, “testsoft”); Kernel.load(exeName[0], null); try { Class c = Class.forName("api3d.Engine3D”); Engine3D obj3d = (Engine3D) c.newInstance();

#### 주의1

obj3d.draw3DLine(x, y, x2, y2); … } catch(Error r) { System.out.println(“3D libraray가 로드되지 않았음”); } } … } <source2>주의1에서 3D library API를 사용하기 전에 해당 라이브러를 Kernel.load() 로 로딩하지 않으면 “java/lang/Error”가 발생되게 된다.

## 4.2. 단말 성능 측정 관련 예제

다양한 단말기 디바이스가 나오면서 하드웨어마다 처리 속도가 틀리기 때문에 하나 의 어플리케이션을 여러 단말기상에서 개발해야 하는 개발자들에게는 화면 크기 및 단말기의 성능에 따라 여러 버전의 패키지로 서비스를 해야 하는 경우가 발생한다. 개발자들의 수고를 조금이나마 덜기 위하여 성능에 관해 튜닝 가이드를 제시하도록 한다. 먼저 해당 단말기 성능에 맞도록 튜닝을 하기 전에 단말기의 성능을 측정해야 한다. 개발자가 측정 항목과 측정에 필요한 소스를 작성해도 무방하나 여러 사람이 많이 사용하고 있는 툴을 이용함으로써 측정 데이터를 함께 공유할 수 있다. 개발자들이 쉽게 활용할 수 있는 성능 벤치마크 툴 중에서 TaylorBench (http://www.poqit.com/midp/bench/)라는 벤치마크 툴은 자바 MIDlet으로 만들어졌으며 라이센스가 전혀 없기 때문에 누구든지 사용 및 수정할 수 있으며 („About‟에 해당 개발자 이름만 명시되어 있다면) 어떤 목적으로도 이용 가능하다. TaylorBench 프로그램은 MIDP 기반 디바이스의 Low-Level Graphics와 VM/CPU 등 의 성능을 측정하는 간단한 항목들로 이루어져 있다. 만약 연산이 많은 어플리케이 션이면 산술연산 항목에 더 많은 가중치를 두어 계산을 하고, 화면 움직임이 많은 어플리케이션이면 UI 테스트 항목들에 대한 결과값을 가지고 이용할 수 있다. 각 항목들에 대하여 간단히 서술하면 아래와 같다 Low-level Graphics lines : 임의의 두 점 사이에 선을 그린다. rectangles (outline and filled) - 외각 선과 채워진 사각형을 임의의 위치에 임의의 크기로 그린다. ellipses (outline and filled) - 외각 선과 채워진 타원형을 임의의 위치에 임의의 크기 로 그린다. arcs (outline and filled) – 외각 선과 채워진 호를 임의의 위치에 임의의 크기로 그린 다. image (small, medium, large) – 세가지 크기의 이미지를 임의의 위치에 그린다. fonts (small, medium, large) – 세가지 크기의 Font로 임의의 위치에 String을 그린다.

#### RMS

record creation – 레코드를 생성한다. record reading, using a enumeration – 순차적으로 레코드를 읽어온다. record reading, randomly accessing records – 임의의 위치의 레코드를 읽어온다. record deletion, randomly deleting – 레코드를 지운다.

#### CPU / VM

system array copies - 자바의 구현과 상관 없는 Native 메소드로 CPU/VM의 성능을 테스트 한다. VM test (multiply, divide, add) - 산술 연산 처리속도를 나타낸다. random ints. – random number generator에 의해 나온 숫자가 영역 내에 고루 분포되 었는지 그래프를 통해 보여준다.

#### COMM

read file (or a dynamically generated number bytes) from an HTTP server. write file, or specific number of bytes to HTTP server. read local file - TaylorBench MIDlet jar 파일 안에 있는 파일을 읽어온다. ※ Control 항목은 정해진 반복횟수 만큼 Loop에 의하여 걸린 시간만을 나타낸다. 우선 성능 측정값 없이 고정적인 화면 Frame 전환 속도를 구현하는 간단한 예제 소 스를 보도록 하겠다. 각 항목들에 대하여 간단히 서술하면 아래와 같다 Game.java <source1> while (running) {

```c
long time = System.currentTimeMillis();
```

moveSprites(); checkCollision(); repaint(); serviceRepaints(); time = System.currentTimeMillis(); try { if (time < DELAY) Thread.sleep(DELAY – (int) time); } catch (Exception ex) { } } ※ Reference : “UI Guidelines & Efficient MIDP Java Programming” by Chiam Poh Guan (Forum Nokia)
