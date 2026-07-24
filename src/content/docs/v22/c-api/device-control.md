---
title: "2.15. 부가 장치 제어"
---

단말기에서 지원되는 부가장치들에 대해서 제어하는 함수 들이다.

### MC_BackLight

**프로토타입**

```c
typedef enum _MC_BackLight MC_BackLight {
MC_LIGHT_ON = 0 // 백라이트 켬 MC_LIGHT_OFF, // 백라이트 끔 MC_LIGHT_ALWAYS_ON, // 백라이트 항상 켬 MC_LIGHT_DEFAULT, //사용자가 설정한 상태로 함 } MC_BackLight;
```

**설명**

백라이트 제어 옵션을 나타내는 열거형

### MC_miscBackLight

**프로토타입**

```c
M_Int32 MC_miscBackLight(M_Int32 id, MC_BackLight on_off, M_Int32 color,
M_Int32 timeout)
```

**설명**

백라이트를 제어하는 함수 이다. 단말기에서 초기에 설정된 백라이트 설정이 존재 한다. 이 설정된 값은 키가 눌려 질 때 몇 초 동안 그 상태를 유지 하게 되어 있다. 이 함수는 그 설정된 값을 무효화 시켜야 하며 어플리케이션에서 사용 후 원 상태로 돌리고 싶다면 `MC_LIGHT_DEFAULT` 값으로 재 설정 후 종료 한다.타임아웃 되면 Backlight는 자동으로 꺼진다. 백라이트 번호는 0 이면 주 LCD 의 백라이트이고 1 이면 보조 LCD 의 백라이트를 가리킨다. 만약 백라이트가 색상을 지정할 수 있을 경우 색상은 매개변수 color 로 지정하는데 color 값의 형식은 0xYYRRGGBB(네트웍 바이트 순서(network byte ordering)이다) 형태이다. 여기서 YY 는 무시되면 RR 은 빨 강(Red), GG 는 녹색(Green), BB 는 파랑(Blue) 범위를 지정한다.

**매개 변수**

- `id` - 백라이트 번호
- `on_off` - 백라이트 조정옵션
- `color` - 백라이트 색상
- `timeout` - 밀리 초 단위의 타임머값. on_off 가 MC_DEV_LIGHT_ON경우만 참조한다

**반환 값**

성공

실패

- `M_E_ERROR` - – 지정한 백라이트가 없을 경우

**부작용**

없음

**참고 항목**

없음

### MC_miscSetLed

**프로토타입**

```c
M_Int32 MC_miscSetLed (M_Int32 leds)
```

**설명**

LED on/off를 설정한다. 각bit가 1이면 on, 0이면 off를 나타낸다. 예) 외장 LED가 4개 존재한다면 LSB BIT 부터 4개를 사용한다. 31bit ... 0 ... `MC_miscSetLed`(0x3) led2개를 켜고, 두개를 끈다. 단, 칼라가 지원되는 단말기인 경우 단말회사가 설정한 가장 밝은 값으로 설정된다.

**매개 변수**

- `leds` - [in] 비트가 1 이면 해당 LED 가 on 되고 0 이면 off 된다

**반환 값**

성공

각 led의 설정된 on/off상태의 bit OR값 (>= 0)
실패

- `M_E_INUSE` - 현재 요청한 LED가 사용중인 경우
- `M_E_ERROR` - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음

### MC_miscLedControl

**프로토타입**

```c
M_Int32 MC_miscLedControl (M_Int32 leds, M_Int32 mask)
```

**설명**

LED를 제어한다. 예) 외장 LED가 4개 존재한다면 LSB BIT 부터 4개를 사용한다. 31bit ... 0 ... `MC_miscLedControl`(0xF, 0x6) 하위 led 4개를 대상으로 그 중 가운데 2개를 켠다.

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

### MC_miscGetLed

**프로토타입**

```c
M_Int32 MC_miscGetLed (void)
```

**설명**

LED의 on/off상태를 읽어온다.

**매개 변수**

없음

**반환 값**

각 led의 on/off상태의 bit OR값

**부작용**

없음

**참고 항목**

없음

### MC_miscGetLedCount

**프로토타입**

```c
M_Int32 MC_miscGetLedCount (void)
```

**설명**

외장된 LED 개수를 얻어 온다.

**반환 값**

led 개수

**부작용**

없음

**참고 항목**

없음

### MC_miscGetLedSupportColor

**프로토타입**

```c
M_Int32 MC_miscGetLedSupportColor (M_Int32 led, M_Int32 RGB[])
```

**설명**

단말기에서 해당 led가 제공하는 칼라 목록을 가지고 온다.

**매개 변수**

- `led` - [in] 제어할 LED
- `RGB` - [out] 칼라 목록

**반환 값**

제공하는 칼라 수

**부작용**

없음

**참고 항목**

없음

### MC_miscGetLedColor

**프로토타입**

```c
M_Int32 MC_miscGetLedCount (M_Int32 led)
```

**설명**

현재 해당 led에 지정되어 있는RGB 값을 가져온다.

**매개 변수**

- `led` - [in] 제어할 LED

**반환 값**

RGB값

**부작용**

없음

**참고 항목**

없음

### MC_miscSetLedColor

**프로토타입**

```c
M_Int32 MC_miscSetLedColor (M_Int32 led, M_Int32 RGB)
```

**설명**

단말기에서 해당 led에 RGB 값을 지정한다. 단, 인자로 받은 RGB값이 없을 경우 지원되는 근사값으로 설정된다.

**매개 변수**

- `led` - [in] 제어할 LED
- `RGB` - [in] RGB값

**반환 값**

성공

설정된 RGB 값
실패

- `M_E_INUSE` - 현재 요청한 LED가 사용중인 경우
- `M_E_ERROR` - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음
