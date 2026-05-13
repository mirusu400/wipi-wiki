# 4.5. HandSet Device

단말기에 장착된 장치를 제어하는 함수들이다.

관련 자료형

//백라이트 제어관련 상수이다. typedef enum MH_DevBackLight {

MH_LIGHT_ON = 0,	// 백라이트를 켬 MH_LIGHT_OFF,	// 백라이트를 끔 MH_LIGHT_ALWAYS_ON,	// 백라이트를 항상 켬 MH_LIGHT_DEFAULT	// 사용자 설정상태로 둠

} MH_DevBackLight;

```c
MH_devBacklight
```

**설명**

백라이트를 제어하는 함수 이다. 단말기에서 초기에 설정된 백라이트 설정이 존재 함을 가정한다. 어플리케이션에서 사용 후 원 상태로 돌리고 싶다면 MH_LIGHT_DEFAULT 값으로 재 설정 후 종료 한다. 타임아웃되면 자동으로 꺼진다. 이 함수를 호출 후 system 은 이 상태를 유지 하므로, 반드시 사용자가 정의한 기 본값으로 이 함수를 통화여 복귀 해야 한다. 백라이트 번호는 0 이면 주 LCD 의 백라이트이고 1 이면 보조 LCD 의 백라이트를 가르킨다. 만약 백라이트가 색상을 지정할 수 있을 경우 색상은 매개변수 color 로 지정하는데 color 값의 형식은 0xYYRRGGBB(네트웍 바이트 순서(network byte ordering)이다) 형태이다. 여기서 YY 는 무시되면 RR 은 빨강(Red), GG 는 녹색(Green), BB 는 파랑(Blue) 범위를 지정한다.

**프로토타입**

```c
M_Int32 MH_devBacklight (M_Int32 id, MH_DevBackLight on_off, M_Int32 color, M_Int32 timeout)
```

**매개 변수**

[in]  id	백라이트 번호

[in]  on_off     백라이트 조정 옵션

```c
[in]   color	백라이트 색상
```

[in]  timeout    밀리초 단위, 타임아웃은 MH_DEV_LIGHT_ON 경우만 유효 하다

**반환 값**

성공 실패

M_E_ERROR – 지정하는 백라이트가 존재하지 않을 경우

**부작용**

없음

**참고 항목**

없음

```c
MH_devVibrator 설명
```

Vibrator 를 제어 한다. 지정한 시간 동안 on 시킨 후 자동으로 꺼진다.

매개변수 level 값이 0 보다 큰 경우만 timeout 값이 유효하다. level 값 0 은 virbrator 가 꺼지는 것을 의미한다. 진동강도는 매개변수 level 값으로 정해지고 0-100 사이의 값이 올수 있다. 100 은 하드웨어가 지원하는 가장 강한 진동을 0 은 가장 약한 진동을 의미한다. 0-100 사이값을 어느정도의 진동세기와 일치시키는가 는 아래의 예처럼 하드웨어가 지원하는 진동단계를 백분율로 일치시킨것에 따른다. 하드웨어가 몇단계의 진동세기를 지원하는가는 MH_sysGetInformation()에서 반환 한다.

예) 진동세기가 하나인 하드웨어 => 1-100 : 진동

진동세기가 강, 약 두개인 하드웨어 => 1-50 : 약진동, 51-100 : 강진동 진동세기가 강,중,약 세개인 하드웨어 => 1-33:약진동, 34 -66:중진동,

67-100:강진동

**프로토타입**

```c
void MH_devVibrator (M_Int32 level,  M_Int32 timeout)
```

**매개 변수**

[in]	level	0 이면 off, 1-100 이면 운영체제에서 일치시킨 진동세기로 진동 [in]	timeout 진동시간, 밀리초 단위

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

```c
MH_devLedControl 설명
```

LED 를 제어 한다. 예)

외장 LED 가 4 개 존재한다면 LSB BIT 부터 4 개를 사용한다.

31 bit ...	0

...

MH_devLedControl(0xF,0x6) 하위 led 4 개를 대상으로 그 중 가운데 2 개를 켠다.

**프로토타입**

```c
void MH_devLedControl (M_Int32 leds, M_Int32 mask)
```

**매개 변수**

[in]

[in]

leds

mask

제어할 LED

마스크할 비트

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

```c
MH_devGetLedCount 설명
```

외장된 LED 개수를 얻어 온다

**프로토타입**

```c
M_Int32 MH_devGetLedCount (void)
```

**매개 변수**

없음

**반환 값**

led 개수

**부작용**

없음

**참고 항목**

없음
