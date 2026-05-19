---
title: "7.3. SMS 관련 API"
---

SMS 관련된 고급 기능은 선택적으로 제공할 수 있다. 이 기능을 제공하고자 하면, 다 음의 규격에따라 지원되어야 한다.

## 7.3.1. 용어 정의

### 가 Teleservice ID

SMS 어플리케이션 식별자이다. (Identification, TIA/EIA/IS-637 참조)

## 7.3.2. Java API

- org.kwis.msf.io.URL
SMS를 사용하기 위하여 URL.find() 메쏘드에 다음의 URL(RFC1738 참조) 문자열을 전달한다.

### 소켓 URL 문자열 예 비고

sms://SHORTME .모드 read: SSAGE:read 운영체제에서 복사해옴 sms://<텔레서비스문자열>: sms://SHORTME .모드 delread: SMS <모드> SSAGE:send 운영체제로 부터 sms://SHORTME 옮겨옴 SSAGE:delread .모드 send: 전송용

## 7.3.3. C API

SMS 송수신에 관한 API 를 모은 것이다. SMS API 는 텔레서비스에 따라서 단문 메 시지,벨소리 다운로드,이미지 다운로드 등 다양한 서비스가 가능하다. SMS 메시 지 수신관련 API 는 운영체제가 수신하여 저장하고 있는 메시지를 복사해 오거나 옮겨오는 두가지 방식이 존재한다. SMS 메시지를 읽어 오거나 복사해 올 때는 MC_phnSmsOpen() 함수를 통해 생성된 메시지 리스트 식별자를 사용한다. 이 리스 트가 생성된 후에 운영체제에 도착하는 메시지를 이 리스트에 반영할 지 여부는 플랫폼 구현의 선택사항이다.

**참고 항목**

없음

### MC_SmsData

**프로토타입**

```c
typedef MC_SmsData {
/// SMS Message의 번호
M_Byte index;
/// 새로운 메시지 또는 읽었던 메시지 인지 구분. 0 이면 읽지 않은 메
시지, 1 이면 읽은 메시지
M_Byte class;
/// ASCII 문자열로 된 발신자 전화번호.<br>bar 없이 붙여 사용된다.
예)016-123-4567 ->0161234567
M_Byte callback[12];
/// 발신자 전화번호의 길이 data의 size.
M_Byte cb_size;
/// 수신된 데이터
M_Byte data[256];
/// 수신된 데이터의 사이즈.
M_Byte data_size;
/**
year 2byte,etc 1byte.
<pre>
수신된 시간.
년 월 일 시 분 초
2 byte 1 byte 1 byte 1 byte 1 byte 1 byte
</pre>
*/
M_Byte timer[7];
} MC_SmsData;
```

**설명**

수신되는 SMS 데이터 를 가진 구조체

### MC_SmsCmd

**프로토타입**

```c
typedef enum MC_SmsCmd{
MC_SMSCMD_READONLY = 0, // 메시지 상태를 변경하지 않으면서 읽는 명령
MC_SMSCMD_CHANGEREAD, // 메시지를 읽지 않은 상태에서 읽은 상태로 변
환시키는 명령어
MC_SMSCMD_DELETE, // 메시지를 삭제시키는 명령어
} MC_SmsCmd;
```

**설명**

SMS 메시지의 상태를 변화시키는 명령어

### MC_phnSmsOpen

**설명**

SMS 메시지 리스트를 연다.테레서비스 문자열에 해당하는 SMS 메시지가 존재하면 SMS 리스트 식별자를 리턴한다. 매개변수 del 이 0 이 아니면 MC_phnSmsRead() 로 읽어 온 메시지는 다시 읽어 올 수 없다. 텔레서비스들은 서비스 사업자에 따라 서 그 기능과 구현이 다르므로 추가 되는 서비스에 대해서 서비스문자열을 추가해 나간다. 현재는 단문메세지를 위한 "SHORTMSG, 방송메세지를 위한 “BROADCAST”, 음성메일을 위한 “VOICEMAIL” 이 세개의 텔레서비스 문자열만 정의한다. 매개변수 cmd 에 따라 운영체제에서 관리하는 SMS 메시지의 상태가 MC_phnSmsRead() 함수가 불릴 때 마다 변한다. 메시지의 상태는 “읽지 않은 상태”, “읽은 상태”, “삭제된 상태” 세가지를 가지며 각 상태는 MC_SMSCMD_READONLY , MC_SMSCMD_CHANGEREAD, MC_SMSCMD_DELETE 로 각각 제어된다. “삭제된 상태” 메시지는 MC_phnSmsRead() 로 읽혀지지 않는다. 메시지 상태는 MC_phnSmsRead() 읽었을 때 SMS 메시지 구조체 MC_SmsData 의 class 필드에 “읽지 않은 상태” 는 0, “읽은 상태”는 1 로 표시된 다. 현재 호출된 MC_phnSmsOpen()과 MC_phnSmsRead()으로 제어되는 메시지리스트 의 메시지 상태는 MC_phnSmsClose() 가 불리고 다음번 MC_phnSmsOpen() 과 MC_phSmsRead() 불렸을 때 변화가되었는지 확인할 수 있다.

**프로토타입**

```c
M_Int32 MC_phnSmsOpen(M_Byte* telIDString, MC_SmsCmd cmd)
```

**매개 변수**

- `telIDString` — 서비스 문자열(현재는 “SHORTMSG” 만 정의되어 있음)
- `cmd` — MC_phnSmsRead() 한 메시지의 상태를 변경시키는 명령어.
**반환 값**

성공 SMS 리스트 식별자 실패 M_E_NOTSUP - 해당 서비스를 지원하지 않는 경우 M_E_NOENT – 리스트에 메시지가 없을 경우 M_E_ISCONN - 이미 OPEN되어 있는 경우

**부작용**

없음

**참고 항목**

MC_phnSmsRead

### MC_phnGetSMSAvailable

**설명**

해당 SMS 리스트의 데이터 갯수를 얻어온다. MC_phnSmsRead 로 메시지를 하나씩 읽을 때마다 이 함수가 리턴하는 값은 1 씩 줄어 든다. 만일 SMS 메시지를 운영체 제에서 복사해 오거나 옮겨 오는 도중에 운영체제에 도착하는 메시지를 메시지 리 스트에 반영하는 플랫폼 이라면 MC_phnSmsRead() 를 호출할 때 마다 이 함수가 리 턴하는 값이 반드시 1 씩 줄어 들지 않을 수도 있다.

**프로토타입**

```c
M_Int32 MC_phnGetSMSAvailable(M_Int32 fd)
```

**매개 변수**

- `fd` — SMS 리스트 식별자
**반환 값**

성공 매세지 개수 실패 MC_E_BADFD(입력된 식별자가 맞지 않는 경우)

**부작용**

없음

**참고 항목**

MC_phnSmsRead

### MC_phnSmsClose

**설명**

해당 SMS 리스트 탐색을 끝마친다. MC_telSmsRead() 함수를 통해 데이터을 읽은 후 더이상 데이터가 존재하지 않는 경우 이 함수를 호출한다.

**프로토타입**

```c
M_Int32 MC_phnSmsClose(M_Int32 fd)
```

**매개 변수**

- `fd` — SMS 리스트 식별자
**반환 값**

성공 실패 MC_E_BADFD(입력된 식별자가 맞지 않는 경우)

**부작용**

없음

**참고 항목**

없음

### MC_phnSmsRead

**설명**

SMS 메시지를 읽어 온다. 이 함수는 한번에 하나의 메시지를 전달해 준다.

**프로토타입**

```c
M_Int32 MC_phnSmsRead(M_Int32 fd, MC_SmsData* buf)
```

**매개 변수**

- `fd` — SMS 리스트 식별자
- `buf` — 메시지가 저장될 버퍼
**반환 값**

성공 0 혹은 1 실패 M_E_BADFD - 입력된 식별자가 맞지 않는 경우 M_E_NOENT - 더 이상 읽을 메시지가 존재하지 않는 경우 M_E_INVALID – 메시지가 저장될 버퍼가 NULL 일 경우

**부작용**

없음

**참고 항목**

MC_phnSmsOpen

### MC_phnSmsSend

**설명**

SMS 메시지를 전송한다. 매개변수 telIDString 은 MC_phnSmsOpen()참조. 매개변수 buf 는 SMS 메시지 포맷의 사용자 데이터 버퍼에 실을 내용을 포함한다. 사용자 데이터는 256 바이트를 초과할 수 없다.

**프로토타입**

```c
M_Int32 MC_phnSmsSend(M_Byte* telIDString, M_Char* telnum , M_Byte* buf,
M_Int32 len)
```

**매개 변수**

- `telIDString` — 텔레서비스 문자열
- `telnum` — 상대방 전화번호
- `buf` — 사용자 데이터 버퍼
- `len` — 사용자 데이터버퍼의 크기
**반환 값**

성공 실패 M_E_NOTSUP - 해당 텔레서비스를 지원하지 않는 경우 M_E_INVALID – 버퍼의 크기가 잘 못 될 경우 M_E_ERROR – 기타 에러

**부작용**

없음

**참고 항목**

없음.

## 7.3.4. HAL API

플랫폼에서 지원하는 SMS 관련 함수들이다. SMS 메시지 리스트는 한번에 하나만 접근이 가능하다. 따라서 다른 텔레서비스에 해당하는 리스트에 접근하려면 현재 사용되는 SMS 메시지 리스트를 닫고 다시 다른 텔레서비스에 해당하는 SMS 메시지 리스트를 열어야 한다. SMS 메시지 리스트가 열려 있는 상태에서 운영체제에 새로 도착하는 메시지를 이 메시지 리스트에 반영할 것인가는 선택사항이다. SMS 메시 지 리스트가 열려 있어도 메시지 전송은 언제든지 가능하다. 새로운 SMS 데이터가 도착하면 운영체제는 MH_SMSEV_NEW 이벤트를 플랫폼에 보내 새 SMS 메시지 도착을 알려야 한다. 운영체제 MH_pltEvent() 함수에 매개변수로 MH_SMS_EVENT 와 MH_SMSEvent 를 넘겨주어 플랫폼에 이벤트를 전달한다.

- 관련 자료형
```c
// SMS 메시지를 읽어 올 때 쓰이는 구조체. TIA/EIA/IS-637 표준 참조
typedef struct MH_SmsData{
M_Byte index; // SMS 메시지의 번호;
M_Byte class; /*새로운 메시지 또는 읽었던 메시지 인지 구분. 0 은 새
로운 메시지, 1은 읽은 상태로 변한 메시지 */
M_Byte callback[16]; /* ASCII 문자열로 된 발신자 전화번호. “-“ 없음
*/
M_Byte cb_size; // callback 에 저장된 발신자 전화번호 길이.
M_Byte data[512]; // 수신된 데이터,CBS 의 경우에는 user data + url
callback + image data = max 512
M_Byte data_size; // 수신된 데이터의 사이즈.
M_Byte timer[7]; // 년0-99사이
/** 각각의 바이트는 정수값임
수신된 시간
년 월 일 시 분 초
1 byte 1 byte 1 byte 1 byte 1 byte 1 byte
*/
} MH_SmsData;
//운영체제가 저장하고 있는 SMS 메시지의 상태를 변화시키는 명령어
typedef enum MH_SmsCmd{
MH_SMSCMD_READONLY = 0, // 메시지 상태를 변경하지 않으면서 읽는 명령
MH_SMSCMD_CHANGEREAD , // 메시지를 읽지 않은 상태에서 읽은 상태로 변
환시키는 명령어
MH_SMSCMD_DELETE, // 메시지를 삭제시키는 명령어
} MH_SmsCmd;
//SMS 이벤트
typedef enum MH_SUB_SMS_EVENT {
MH_SMSEV_NEW = 0, // 새로운 메시지가 도착함
```

MH_SMSEV_SEND_NOTIFY //메시지가 전송되었을 경우에 전달함.

```c
} MH_SUB_SMS_EVENT;
//SMS 이벤트를 전달하는 구조체
typedef struct MH_SMSEvent{
M_Int32 event; // MH_SUB_SMS_EVENT값
M_Int32 parm1; //event가 MH_SMSEV_SEND_NOTIFY 일 때 실
제로 전송된 메시지 수, 전송 실패시 -1
//event가 MH_SMSEV_NEW일 때 메시지 저장
함 내의 인덱스
M_Int32 parm2;//event가 MH_SMSEV_NEW일 때 수신한 메시지의 tele -
Service ID
} MH_SMSEvent;
```

### MH_smsOpen

**설명**

텔레서비스 문자열에 해당하는 SMS 메시지 리스트를 연다. 매개변수 telIDString 을 분석한 후 그에 해당되는 텔레서비스(Teleservice)가 존재한다면 해당 리스트 의 식별자를 리턴한다. 이 문서에서 텔레서비스 아래의 세가지만 정의하며 다른 텔레서비스에 대한 문자열의 정의는 이 문서가 규정할 수 있는 범위 밖의 것이다.

입력 String 설명 “SHORTMSG” 단문 메시지 “BROADCAST” 방송메시지 “VOICEMAIL" 음성메일 메시지 매개변수 cmd 에 따라 운영체제에서 관리하는 SMS 메시지의 상태가 MH_smsGetNext() 함수가 불릴 때 마다 변한다. 메시지의 상태는 “읽지 않은 상태”, “읽은 상태”, “삭제된 상태” 세가지를 가지며 각 상태는 MH_SMSCMD_READONLY , MH_SMSCMD_CHANGEREAD, MH_SMSCMD_DELETE 로 각각 제어된다. “삭제된 상태” 메시 지는 MH_smsGetNext() 로 읽혀지지 않는다. 메시지 상태는 MH_smsGetNext() 읽었 을 때 SMS 메시지 구조체 MH_SmsData 의 class 필드에 “읽지 않은 상태” 는 0, “읽은 상태”는 1 로 표시된다. 현재 호출된 MH_smsOpen()과 MH_smsGetNext()으로 제어되는 메시지리스트의 메시지 상태는 MH_smsClose() 가 불리고 다음번 MH_smsOpen() 과 MH_smsGetNext() 불렸을 때 변화가되었는지 확인할 수 있다.

**프로토타입**

```c
M_Int32 MH_smsOpen (M_Char * tID, MH_SmsCmd cmd)
```

**매개 변수**

[in] telIDString teleservice ID String [in] cmd 메시지 상태를 변경하는 명령어

**반환 값**

성공 SMS 메시지 리스트 식별자 실패 M_E_NOTSUP – 해당 서비스를 지원하지 않는 경우 M_E_ERROR - 기타 이유로 실패할 경우 M_E_ISCONN – 해당 텔레서비스에 대한 리스트가 이미 열려 있는 경우

**부작용**

없음

**참고 항목**

없음

### MH_smsGetAvailable

**설명**

SMS 메시지 리스트의 갯수를 얻어 온다. 리턴되는 값은 MC_smsGetNext() 를 호출 할 때 마다 1 씩 감소하는 것이 일반적이지만 만약 운영체제가 리스트가 열려 있 는 상태에서 운영체제게 새롭게 도착하는 메시지를 열려 있는 리스트에 반영한다 면 MC_smsGetNext() 함수 호출 후에 이 함수가 리턴하는 값이 반드시 1 씩 감소하 지 않을 수도 있다.

**프로토타입**

```c
M_Int32 MH_smsGetAvailable (M_Int32 tID)
```

**매개 변수**

[in] tID 텔레서비스식별자

**반환 값**

성공:메시지 개수 실패: M_E_ERROR – 기타 이유로 인한 실패

**부작용**

없음

**참고 항목**

MH_smsGetNext

### MH_smsClose

**설명**

해당 SMS 메시지 리스트사용을 종료한다.

**프로토타입**

```c
void MH_smsClose (M_Int32 tID)
```

**매개 변수**

[in] tID SMS 메시지 리스트 식별자

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_smsGetNext

**설명**

SMS 메시지 리스트의 메세지를 하나씩 얻어 온다. 반환될 데이터가 더 이상 존재 하지 않는다면 M_E_NOENT 가 반환된다.

**프로토타입**

```c
M_Int32 MH_smsGetNext (
M_Int32 tID,
MH_SmsData *buf,
)
```

**매개 변수**

[in] tID SMS 메시지 리스트 식별자 [out] buf 메시지가 저장될 버퍼

**반환 값**

성공 실패 M_E_NOENT– 더 이상 읽을 메시지가 존재하지 않는 경우 M_E_ERROR – 기타 이유로 인한 실패

**부작용**

없음

**참고 항목**

없음

### MH_smsSend

**설명**

SMS 메시지를 전송한다. 송신자와 보낸 시간 등은 HAL 에서 처리한다. 전송하는 사용자 데이터는 256 바이트를 초과할 수 없다. 텔레서비스 문자열은 MH_smsOpen() 참조한다. 반환 값이 M_E_WOULDBLOCK 일 경우에는 시스템 내부요인 으로 지금 당장 데이터를 전송할 수 없다는 것을 의미한다. 이 경우 데이터를 처 리한후 전송여부에 대한 결과를 MH_SMSEV_SEND_NOTIFY 이벤트로 플랫폼에 전달되 어야 한다.

**프로토타입**

```c
M_Int32 MH_smsSend (M_Char* telIDString, M_Char* telnum, M_Byte* buf,
M_Int32 len)
```

**매개 변수**

[in] telIDString 텔레서비스 문자열 [in] telnum 상대방 전화번호 [in] buf 사용자 데이터 버퍼길이는 256 바이트를 넘길 수 없다.

[in] len 데이터의 길이

**반환 값**

성공: 0실패: M_E_ERROR - 기타 이유에 의해 실패 M_E_NOTSUP - 해당 텔레서비스를 지원하지 않는 경우 M_E_WODULDBLOCK – 시스템 내부 요인으로 지금 당장 데이터를 전송할 수 없는 경우

**부작용**

없음

**참고 항목**

MH_smsOpen

### MH_smsGetMaximumLength

**설명**

텔레서비스 문자열에 해당하는 SMS 메시지의 사용자 데이터 영역의 최대 지원길이 를 리턴한다.

**프로토타입**

```c
M_Int32 MH_smsGetMaximumLength (M_Char* telIDString)
```

**매개 변수**

[in] telIDString 텔레서비스 문자열

**반환 값**

성공: 메시지 사용자 데이터 영역의 최대 지원길이 실패: M_E_NOTSUP - 해당 텔레서비스를 지원하지 않는 경우

**부작용**

없음

**참고 항목**

없음.

### MH_smsGetDirect

**설명**

메시지 저장함으로부터 지정한 인덱스를 가진 메시지를 조회한다. 메시지 저장함 내에 지정한 인덱스를 가진 메시지가 없으면M_E_NOENT 가 반환된다..

**프로토타입**

```c
M_Int32 MH_smsGetDirect (M_Char * telIDString,M_Int32 idx,MH_SmsData *buf)
```

**매개 변수**

[in] telIDString tele-Service ID String(메시지 저장함을 구분함.) [in] idx 조회할 메시지의 인덱스 [out] buf 메시지가 저장될 버퍼

**반환 값**

성공: 실패: M_E_NOTSUP – 해당 tele-Service ID String이 존재하지 않을 때 M_E_NOENT - 지정한 인덱스를 가진 메시지가 존재하지 않는 경우

**부작용**

없음

**참고 항목**

없음

### MH_smsSetStateDirect

**설명**

메시지 저장함 내의 특정 메시지의 상태를 변경한다.

**프로토타입**

```c
M_Int32 MH_smsSetStateDirect(M_Char * telIDString,M_Int32 idx,MH_SmsCmd cmd)
```

**매개 변수**

[in] telIDString tele-Service ID String(메시지 저장함을 구분함.) [in] idx 조회할 메시지의 인덱스 [in] cmd 메시지 상태를 변경하는 명령어

**반환 값**

성공: 실패: M_E_NOTSUP - 해당 서비스를 지원하지 않는 경우 M_E_ERROR - 기타 이유로 실패할 경우,MH_smsOpen으로 개방된 메 시지 리스트에 대해 이 API를 호출할 경우에도 이 에러 값을 리턴한다.

**부작용**

없음

**참고 항목**

없음
