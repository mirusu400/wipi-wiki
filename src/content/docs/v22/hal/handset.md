---
title: "2.12. 핸드셋 디바이스"
---

단말기에 장착된 장치를 제어하는 함수들이다.

#### 관련 자료형

백라이트 제어관련 상수이다.

```c
typedef enum MH_DevBackLight {
MH_LIGHT_ON = 0, // 백라이트를 켬
MH_LIGHT_OFF, // 백라이트를 끔
MH_LIGHT_ALWAYS_ON, // 백라이트를 항상 켬
MH_LIGHT_DEFAULT // 사용자 설정상태로 둠
} MH_DevBackLight;
```

### MH_devBacklight

**프로토타입**

```c
M_Int32 MH_devBacklight (M_Int32 id, MH_DevBackLight on_off, M_Int32 color, M_Int32 timeout)
```

**설명**

백라이트를 제어하는 함수 이다. 단말기에서 초기에 설정된 백라이트 설정이 존재 함 을 가정한다. 어플리케이션에서 사용 후 원 상태로 돌리고 싶다면 `MH_LIGHT_DEFAULT` 값으로 재 설정 후 종료 한다. 타임아웃 되면 자동으로 꺼진다. 이 함수를 호출 후 시스템은 이 상태를 유지 하므로, 반드시 사용자가 정의한 기본값 으로 이 함수를 통하여 복귀 해야 한다. 백라이트 번호는 0 이면 주 LCD 의 백라이 트이고 1 이면 보조 LCD 의 백라이트를 가리킨다. 만약 백라이트가 색상을 지정할 수 있을 경우 색상은 매개변수 color 로 지정하는데 color 값의 형식은 0xYYRRGGBB(네트워크 바이트 순서(network byte ordering)이다) 형태이다. 여기서 YY 는 무시되면 RR 은 빨간색, GG 는 녹색, BB 는 파란색 범위를 지정한다.

**매개 변수**

- `id` - [in] 백라이트 번호
- `on_off` - [in] 백라이트 조정 옵션
- `color` - [in] 백라이트 색상
- `timeout` - [in] 밀리 초 단위, 타임아웃은 `MH_DEV_LIGHT_ON` 경우만 유효 하다

**반환 값**

성공

실패

- `M_E_ERROR` - 지정하는 백라이트가 존재하지 않을 경우

**부작용**

없음

**참고 항목**

없음

### MH_devVibrator

**프로토타입**

```c
M_Int32 MH_devVibrator (M_Int32 level, M_Int32 timeout)
```

**설명**

Vibrator를 제어 한다. 지정한 시간 동안 on시킨 후 자동으로 꺼진다. 매개변수 level값이 0보다 큰 경우만 timeout 값이 유효하다. level값 0은 vibrator가 꺼 지는 것을 의미한다. 진동강도는 매개변수 level값으로 정해지고 0-100사이의 값이 올 수 있다. 100은 하드웨어가 지원하는 가장 강한 진동을 0은 가장 약한 진동을 의미한 다. 0-100사이 값을 어느 정도의 진동세기와 일치시키는가는 아래의 예처럼 하드웨어 가 지원하는 진동단계를 백분율로 일치시킨 것에 따른다. 하드웨어가 몇 단계의 진동 세기를 지원하는가는 `MH_sysGetInformation`()에서 반환한다. 예) 진동세기가 하나인 하드웨어 => 1-100 : 진동 진동세기가 강, 약 두 개인 하드웨어 => 1-50 : 약 진동, 51-100 : 강진 동 진동세기가 강,중,약 세 개인 하드웨어 => 1-33:약 진동, 34-66:중 진동, 67-100:강진 동

**매개 변수**

- `level` - [in] 0이면 off, 1-100이면 운영체제에서 일치시킨 진동세기로 진동
- `timeout` - [in] 진동시간, 밀리 초 단위

**반환 값**

성공

실패

- `M_E_INUSE` - 현재 요청한 vibrator 사용중인 경우
- `M_E_ERROR` - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음

### MH_devLedControl

**프로토타입**

```c
M_Int32 MH_devLedControl (M_Int32 leds, M_Int32 mask)
```

**설명**

LED를 제어 한다. 예) 외장 LED가 4개 존재한다면 LSB BIT 부터 4개를 사용한다. 31 bit ... 0 ... `MH_devLedControl`(0xF,0x6) 하위 led 4개를 대상으로 그 중 가운데 2개를 켠다. 단, 칼라가 지원되는 단말기인 경우 단말회사가 설정한 가장 밝은 값으로 설정된다.

**매개 변수**

- `leds` - [in] 제어할 LED
- `mask` - [in] 마스크할 비트

**반환 값**

성공

실패

- `M_E_INUSE` - 현재 요청한 LED가 사용중인 경우
- `M_E_ERROR` - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음

### MH_devGetLed

**프로토타입**

```c
M_Int32 MH_devGetLed(void)
```

**설명**

LED의 on/off 상태를 읽어온다.

**매개 변수**

없음

**반환 값**

각 led의 on/off 상태의 bit OR 값을 반환한다. 단, 칼라가 지원되는 단말기인 경우 단말회사가 각 칼라 값에 on/off 값을 가정한 다.

**부작용**

없음

**참고 항목**

없음

### MH_devGetLedCount

**프로토타입**

```c
M_Int32 MH_devGetLedCount (void)
```

**설명**

외장된 LED 개수를 얻어 온다

**매개 변수**

없음

**반환 값**

led개수

**부작용**

없음

**참고 항목**

없음

### MH_devGetLedSupportColor

**프로토타입**

```c
M_Int32 MH_devGetLedSupportColor (M_Int32 led, M_Int32 RGB[]
```

**설명**

단말기에서 해당 led가 제공하는 칼라 목록을 가지고 온다. 예) 8bit 8bit 8bit 8bit 8bit 8bit 8bit 8bit RGB[0] RGB[1] 미 미 사 R G B 사 R G B 용 용

**매개 변수**

- `led` - [in] 제어할 LED
- `RGB` - [out] 칼라 값 배열이 반환되는 버퍼

**반환 값**

제공하는칼라 수

**부작용**

없음

**참고 항목**

없음

### MH_devGetLedColor

**프로토타입**

```c
M_Int32 MH_devGetLedColor (M_Int32 led)
```

**설명**

현재 해당 led에 지정되어 있는 RGB 값을 가져온다.

**매개 변수**

- `led` - [in] 제어할 LED

**반환 값**

설정되어 있는 RGB 값

**부작용**

없음

**참고 항목**

없음

### MH_devSetLedColor

**프로토타입**

```c
M_Int32 MH_devSetLedColor (M_Int32 led, M_Int32 RGB)
```

**설명**

단말기에서 해당 led에 RGB 값을 지정한다. 단, 인자로 받은 RGB값이 없을 경우근 사값으로 설정된다.

**매개 변수**

- `led` - [in] 제어할 LED
- `RGB` - [in] 설정할 RGB 값

**반환 값**

성공

실패

- `M_E_INUSE` - 현재 요청한 LED가 사용중인 경우
- `M_E_ERROR` - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음
