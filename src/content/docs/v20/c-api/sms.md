---
title: "2.13. SMS"
---

### MC_smsSend

**프로토타입**

```c
M_Int32 MC_smsSend(M_Char* telnum, M_Byte* smsMsg, M_Int32 len)
```

**설명**

일반 단문 메시지를 전송한다. 매개변수 smsMsg는 SMS 메시지 포맷의 사용자 데이 터 버퍼에 실을 내용을 포함한다. 사용자 데이터는 `MC_smsGetMaxMsgLength`()의 반환값에 해당하는 byte를 초과할 수 없다. M_E_WOULDBLOCK일 경우에는 시스템 내부 요인으로 지금 당장 데이터를 전송할 수 없다는 것을 의미하며 이후 SMS 메시 지 전송의 처리 결과는 handleCletEvent를 통해 호출한 순서대로 이벤트를 전달받을 수 있다. handleCletEvent의 param1에는 MC_SMSEV_SEND_NOTIFY가 param2에는 1(전송된 메시지 수) 또는 실패했을 경우 –1이 전달된다. 여러 개 보낼 경우, 호출한 수만큼 순서대로 이 이벤트를 전달한다. MC_smsSend가 호출되면 사용자가 SMS 메시지 전송에 대한 확인창이 뜨고 "확인" 을 선택했을 때에만 메세지가 전송되게 된다

**매개 변수**

- `telnum` - [in] 상대방 전화 번호
- `smsMsg` - [in] 전송할 문자열
- `len` - [in] 문자열의 길이

**반환 값**

성공

실패

- `M_E_INVALID` - 버퍼의 크기가 잘 못 될 경우
- `M_E_WODULDBLOCK` - 시스템 내부 요인으로 지금 당장 데이터를 전송할 수 없는 경우
- `M_E_ERROR` - 기타 에러

**부작용**

없음

**참고 항목**

없음

### MC_smsGetMaxMsgLength

**프로토타입**

```c
M_Int32 MC_smsGetMaxMsgLength(void)
```

**설명**

전송가능한 메시지의 최대 길이를 byte로 환산하여 반환한다.

**매개 변수**

없음

**반환 값**

성공

Byte 단위의 SMS 메시지 최대 길이
실패

- `M_E_ERROR` - 알 수 없는 이유로 실패

**부작용**

없음

**참고 항목**

없음
