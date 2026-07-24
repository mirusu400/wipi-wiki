---
title: "2.13. SMS"
---

### MC_phnSmsSend

**프로토타입**

```c
M_Int32 MC_phnSmsSend(M_Byte *telIDString, M_Char *telnum, M_Byte *buf,
M_Int32 len)
```

**설명**

일반 단문 메시지를 전송한다. 매개변수 buf는 SMS 메시지 포맷의 사용자 데이터 버퍼에 실을 내용을 포함한다. 사용자 데이터는 `MC_phnSmsGetMaxMsgLength`()의 반환값에 해당하는 byte를 초과할 수 없다. M_E_WOULDBLOCK일 경우에는 시스템 내부 요인으로 지금 당장 데이터를 전송할 수 없다는 것을 의미하며 이후 SMS 메시 지 전송의 처리 결과는 handleCletEvent를 통해 호출한 순서대로 이벤트를 전달받을 수 있다. handleCletEvent의 param1에는 MC_SMSEV_SEND_NOTIFY가 param2에는 성공 했 을 경우 1 또는 실패했을 경우 –1이 전달된다. 여러 개 보낼 경우, 호출한 수만큼 순 서대로 이 이벤트를 전달한다.

**매개 변수**

- `telIDString` - [in] 텔레서비스 문자열 (현재는 “SHORTMSG”만 정의되어 있 음)
- `telnum` - [in] 상대방 전화번호
- `buf` - [in] 사용자 데이터 버퍼
- `len` - [in] 사용자 데이터버퍼의 크기

**반환 값**

성공

실패

- `M_E_INVALID` - 버퍼의 크기가 잘 못 될 경우
- `M_E_WODULDBLOCK` - 시스템 내부 요인으로 지금 당장 데이터를 전송할 수 없는 경우
- `M_E_ERROR` - 기타 에러
- `M_E_NOTSUP` - 해당 텔레서비스를 지원하지 않는 경우

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

### MC_phnSmsGetMaxMsgLength

**프로토타입**

```c
M_Int32 MC_phnSmsGetMaxMsgLength(M_Byte* tellIDString)
```

**설명**

전송가능한 메시지의 최대 길이를 byte로 환산하여 반환한다.

**매개 변수**

- `telIDString` - [in] 텔레서비스 문자열

**반환 값**

성공

Byte 단위의 SMS 메시지 최대 길이
실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_NOTSUP` - 해당 텔레서비스를 지원하지 않는 경우

**부작용**

없음

**참고 항목**

없음
