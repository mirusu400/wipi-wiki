# 4.4. CALL

```c
전화를 걸거나 받는 함수들이다. 플랫폼 수행 중에 전화가 걸려 올 때 수신 여부를 결 정할 수 있고, 플랫폼에서 전화를 걸 수 있다. 운영체제는 MH_pltEvent() 함수에 매개 변수로 MH_CALL_EVENT 와 MH_ CallEvent 를 넘겨주어 플랫폼에 이벤트를 전달한다
```

관련 자료형

```c
//전화관련 이벤트
typedef enum MH_SUB_CALL_EVENT {
```

MH_CALLEV_INCOMING = 0,		// 전화가 왔음을 알림 MH_CALLEV_NOTIFY	// MH_callPlace()를 수행후 전화종료/상태를

알림

} MH_SUB_CALL_EVENT;

```c
//전화관련 이벤트를 전달할 때 사용하는 구조체
typedef struct MH_CallEvent{
M_Int32 event;	// 발생되는 Event, enum _MH_SUB_CALL_EVENT
```

값

M_Int32 rtnCode;	//**0 : 성공적으로 MH_callPlace()가 수행되고

정상적으로 종료되었음, -1 : MH_callPlace()가 성공적으로 수행되지 못함 */

} MH_CallEvent;

```c
MH_callPlace
```

**설명**

전화를 건다. 함수가 성공으로 반환 후에는 전화 거는 상태이어야 한다. 통화가 종료된 후에는 플랫폼에 종료 이벤트(MH_CALLEV_NOTIFY)가 전달 되어야 한다.

**프로토타입**

```c
M_Int32 MH_callPlace (char * phonenum)
```

**매개 변수**

[in]	phonenum	전화번호

**반환 값**

성공 실패

**부작용**

```c
없음
```

**참고 항목**

없음

M_E_ERROR – 전화를 걸수 없음

MH_callEnd 설명

전화 거는 중 혹은 현재 통화하고 있는 중에 통화를 종료 한다. 종료 후 MH_CALLEV_NOTIFY 이벤트를 플랫폼에 전달 한다.

**프로토타입**

```c
void MH_callEnd (void)
```

**매개 변수**

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

```c
MH_callAccept 설명
```

통화 요청 된 전화를 받는다. 응용프로그램 수행 중에 표준 플랫폼 내부에서 MH_CALLEV_INCOMING 이벤트가 발생한다면, 이 함수를 통해서 전화를 수신할 수 있 다.

**프로토타입**

```c
void MH_callAccept(void)
```

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

```c
MH_SUB_CALL_EVENT
MH_callReject 설명
```

통화 요청 된 전화를 거부한다. MH_CALLEV_INCOMING 이벤트가 발생하면 이 함수를 통해서 전화를 거부할 수 있다.

```c
.
```

**프로토타입**

```c
void MH_callReject(void)
```

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음
