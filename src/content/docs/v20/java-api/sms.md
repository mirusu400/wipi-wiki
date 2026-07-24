---
title: "3.1.9. SMS"
---

---

## Class SMSMessage

```text
java.lang.Object
  +--org.kwis.msp.io.SMSMessage
```

```java
public class SMSMessage extends java.lang.Object
```

단말기의 단문 문자서비스를 제공한다

*Methods inherited from class java.lang.Object: clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 생성자 상세

### SMSMessage

```java
public SMSMessage(Byte[] data)
```

SHORT_MESSAGE 타입의 SMS 메시지를 생성한다. 생성된 SMS 메시지는 SMS.send() 메 소드를 사용하여 보낼 수 있다.

**매개 변수**

data[] 메세지 데이터
- `필드` - 상세 설명 SHORT_MESSAGE
- `static` - int SHORT_MESSAGE 단말기의 단문 문자 메시지를 정의한다. UNKNOWN
- `static` - int UNKNOWN 단말기에 정의되지 않은 문자메세지 타입에 대한 상수정보를 나타낸다.
- `Class` - SMS java.lang.Object | +--org.kwis.msp.io.SMS
- `public` - class SMS extends java.lang.Object
- `SMSMessage와` - 함께 단말기의 단말 문자 서비스 기능을(Short Message Service) 제공한 다.
- `Methods` - inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 생성자 상세 설명 없음 필드 상세 설명 `M_E_NOTSUP`
- `const` - int `M_E_NOTSUP` 해당 텔레서비스를 지원하지 않는 경우 발생하는 에러. `M_E_INVALID`
- `const` - int `M_E_INVALID` 버퍼의 크기가 잘못되었을 경우 발생하는 에러. `M_E_WOULDBLOCK`
- `const` - int `M_E_WOULDBLOCK` 시스템 내부 요인으로 지금 당장 데이터를 전송할 수 없는 경우에 발생하는 에러 `M_E_ERROR`
- `const` - int `M_E_ERROR` 기타 에러 메쏘드 상세 설명 send
- `public` - const int send(String telnum, SMSMessage smsMsg)
- `SMSMessage를` - 보낸다. send() 메소드가 호출되면 사용자가 SMS 메시지 전송에 대한 확인창이 뜨고 "확인"을 선택했을 때에만 SMSMessage가 전송되게 된다.

**매개 변수**

- `telNum` - 상대방 전화번호
- `smsMsg` - SMSMessage object

**반환 값**

메시지 전송이 성공하면 0, 실패시에는 다음과 같은 Error값을 반환한다;
- `M_E_NOTSUP` - 해당 텔레서비스를 지원하지 않는 경우
- `M_E_INVALID` - 버퍼의 크기가 잘 못 될 경우
- `M_E_WODULDBLOCK` - 시스템 내부 요인으로 지금 당장 데이터를 전송할 수 없는 경우
- `M_E_ERROR` - 기타 에러 Throws NullPointerException telNum 이나 smsMsg가 null일때 발생 getMaxMsgLength public const int getMaxMsgLength(void) 전송 가능한 메시지의 길이를 byte로 환산하여 반환한다.

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
