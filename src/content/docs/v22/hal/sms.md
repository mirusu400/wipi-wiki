---
title: "2.18. SMS"
---

SMS를 이용하여 문자 메시지를 보내기 위한 규격이다.

## 2.18.1. 관련자료형

// SMS 이벤트

```c
typedef enum MH_SUB_SMS_EVENT {
MH_SMSEV_SEND_NOTIFY // 메시지가 전송 결과(성공 및 실패
// 여부)를 전달함.
} MH_SUB_SMS_EVENT;
```

// SMS 이벤트를 전달하는 구조체

```c
typedef struct MH_SMSEvent {
M_Int32 event; // MH_SUB_SMS_EVENT값
M_Int32 parm1; // event가 MH_SMSEV_SEND_NOTIFY일 때 성공했을 경우 1
//전송 실패시 -1
} MH_SMSEvent;
```

### MH_smsSend

**프로토타입**

```c
M_Int32 MH_smsSend (M_Char* telIDString, M_Char* telnum, M_Byte* buf,
M_Int32 len))
```

**설명**

일반 단문 메시지를 전송한다. 전송자와 전송하는데 걸리는 시간 등은 HAL 에서 처 리한다. 반환 값이 M_E_WOULDBLOCK일 경우에는 시스템 내부 요인으로 지금 당장 데이터 를 전송할 수 없다는 것을 의미한다. 이 경우 데이터를 처리한 후 전송 성공 여부에 대해 호출된 순서대로MH_SMSEV_SEND_NOTIFY 이벤트를 플랫폼으로 전달하여야 한다.

**매개 변수**

- `telIDString` - [in] 텔레서비스 문자열 (현재는 “SHORTMSG” 만 정의되 어 있음)
- `telnum` - [in] 상대방 전화 번호
- `buf` - [in] 사용자 데이터
- `len` - [in] 데이터의 길이

**반환 값**

성공

실패

- `M_E_ERROR` - 기타 이유에 의해 실패
- `M_E_WODULDBLOCK` - 시스템 내부 요인으로 지금 당장 데이터를 전송할 수 없는 경우
- `M_E_NOTSUP` - 해당 텔레서비스를 지원하지 않는 경우

**부작용**

없음

**참고 항목**

없음

### MH_smsGetMaxMsgLength

**프로토타입**

```c
M_Int32 MH_smsGetMaxMsgLength(M_Byte* telIDString)
```

**설명**

매개변수로 전달된 텔레서비스에 대한 전송 가능한 메시지의 최대 길이를 byte 단위 로 환산하여 반환한다.

**매개 변수**

- `telIDString` - [in] 서비스 문자열

**반환 값**

성공

byte단위의 전송가능한 최대 문자열 길이 값
실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_NOTSUP` - 해당 서비스를 지원하지 않는 경우

**부작용**

없음

**참고 항목**

없음
