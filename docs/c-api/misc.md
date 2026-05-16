# 5.1.9. MISC

단말기에서 지원되는 부가장치들에 대해서 제어하는 함수 들이다. HAL 에서 수정된 부분 반영함.


### MC_BackLight

**프로토타입**

```c
typedef enum _MC_BackLight MC_BackLight {
    MC_LIGHT_ON = 0  // 백라이트 켬
    MC_LIGHT_OFF,  // 백라이트 끔
    MC_LIGHT_ALWAYS_ON,  // 백라이트 항상 켬
    MC_LIGHT_DEFAULT,  //사용자가 설정한 상태로 함
} MC_BackLight;
```

**설명**

백라이트 제어 옵션을 나타내는 열거형

### MC_miscBackLight

**설명**

백라이트를 제어하는 함수 이다. 단말기에서 초기에 설정된 백라이트 설정이 존재 한다. 이 설정된 값은 키가 눌려 질 때 몇 초 동안 그 상태를 유지 하게 되어 있 다. 이 함수는 그 설정된 값을 무효화 시켜야 하며 어플리케이션에서 사용 후 원 상태로 돌리고 싶다면 `MC_LIGHT_DEFAULT` 값으로 재 설정 후 종료 한다.타임아웃 되면 `Backlight` 는 자동으로 꺼진다. 백라이트 번호는 0 이면 주 LCD 의 백라이트 이고 1 이면 보조 LCD 의 백라이트를 가르킨다. 만약 백라이트가 색상을 지정할 수 있을 경우 색상은 매개변수 color 로 지정하는데 color 값의 형식은 0xYYRRGGBB(네트웍 바이트 순서(network byte ordering)이다) 형태이다. 여기서 YY 는 무시되면 RR 은 빨강(Red), GG 는 녹색(Green), BB 는 파랑(Blue) 범위를 지정한다.

**프로토타입**

```c
M_Int32 MC_miscBackLight(M_Int32 id, MC_BackLight on_off, M_Int32 color, M_Int32 timeout)
```

**매개 변수**

- `id` - 백라이트 번호
- `on_off` - 백라이트 조정옵션
- `color` – 백라이트 색상
- `timeout` - 밀리초단위의 타임머값. on_off 가 `MC_DEV_LIGHT_ON` 경우만 참조한다

**반환 값**

성공

- 0

실패

- `M_E_ERROR` - 지정한 백라이트가 없을 경우

**부작용**

없음

**참고 항목**

없음


### MC_miscSetLed

**설명**

LED on/off 를 설정한다. 각 bit 가 1 이면 on, 0 이면 off 를 나타낸다.

예) 외장 LED 가 4 개 존재한다면 LSB BIT 부터 4 개를 사용한다.


```
 *                          0 bit 
 *   +---------------------+ 
 *   |             |*|*|*|*| 
 *   +---------------------+ 
 * 
```

`MC_miscSetLed(0x3)` led2 개를 켜고, 두개를 끈다.

**프로토타입**

```c
void MC_miscSetLed(M_Int32 leds)
```

**매개 변수**

- `leds` - 비트가 1 이면 해당 LED 가 on 되고 0 이면 off 된다

**부작용**

없음

**참고 항목**

없음

### MC_miscGetLed

**설명**

LED 의 on/off 상태를 읽어온다.

**프로토타입**

```c
M_Int32 MC_miscGetLed()
```

**매개 변수**

없음

**반환 값**

- 각 led의 on/off상태의 bit OR값

**부작용**

없음

**참고 항목**

없음

### MC_miscGetLedCount

**설명**

외장된 LED 개수를 얻어 온다.

**프로토타입**

```c
M_Int32 MC_miscGetLedCount(void)
```

**반환 값**

led 개수

**부작용**

없음

**참고 항목**

없음

