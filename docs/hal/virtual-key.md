# 4.15. Virtual Key

응용프로그램에서 단말기의 키를 가상적인 기능 키로 사용할 때 필요한 함수들이 다. 예를 들어 단말기에서 방향 키가 존재하지 않는 경우 번호 키를 매핑 (mapping)해서 사용한다.게임이나 기타 응용 프로그램은 숫자키 외의 키를 받아서 수행된다. 그러나 숫자키 외의 키(조절키)의 존재 여부는 폰 모델에 따라 다르므 로 이런 조절키는 가상 기능키라 정의하고, 이런 가상 기능 키는 , `MH_keyGetVirtualCode` 나 `MH_keyGetKeyCode` 함수로 각각 가상 기능 키 값을 실제 키 값으로, 실제 키 값을 가상 기능 키 값으로 변경하여 일반 응용 프로그램에서 조절키 존재 여부에 상관없이 동작할 수 있도록 해준다. 예를 들어 `MH_VIRGAME_A` 키라는 가상 키가 있으며 이 가상 키는 “7”키나 “1”키 혹은 “SOFT_2”키에 대응될 수 있다.

```c
int a;
a = MH_keyGetVirtualCode(MH_KEY_7);  /* a == MH_VIRGAME_A */

/* 관련 자료형 */

#define MH_VIRUP          1   /* UP 기능 키        */
#define MH_VIRDOWN        6   /* DOWN 기능 키      */
#define MH_VIRLEFT        2   /* LEFT 기능 키      */
#define MH_VIRRIGHT       5   /* RIGHT 기능 키     */
#define MH_VIRFIRE        8   /* FIRE(SEL) 기능 키 */
#define MH_VIRGAME_A      9   /* GAME1 기능 키     */
#define MH_VIRGAME_B      10  /* GAME2 기능 키     */
#define MH_VIRGAME_C      11  /* GAME3 기능 키     */
#define MH_VIRGAME_D      12  /* GAME4 기능 키     */
#define MH_VIRSIDE_UP     96  /* SIDE UP 기능 키   */
#define MH_VIRSIDE_DOWN   97  /* SIDE DOWN 기능 키 */
#define MH_VIRSIDE_SEL    98  /* SIDE SEL 기능 키  */
#define MH_VIRSIDE_CLEAR  99  /* SIDE CLEAR 기능 키 */
```

### MH_keyGetVirtualCode

**설명**

주어진 실제 키의 값에 매핑(mapping)되는 가상 키 값을 가져 온다

**프로토타입**

```c
M_Int32 MH_keyGetVirtualCode(M_Int32 keyCode)
```

**매개 변수**

- `keyCode` - [in] 폰의 KeyCode 값. `MH_KeyCode` 참조

**반환 값**

- Virutal Keypad

**부작용**

없음

**참고 항목**

없음

### MH_keyGetKeyCode

**설명**

주어진 가상 키의 값에 매핑(mapping)되는 실제 키 값을 가져 온다

**프로토타입**

```c
M_Int32 MH_keyGetKeyCode(M_Int32 gameAction)
```

**매개 변수**

- `gameAction` - [in] Virtual KeyPad

**반환 값**

폰의 KeyCode 값. `MH_KeyCode` 참조.

**부작용**

없음

**참고 항목**

없음

