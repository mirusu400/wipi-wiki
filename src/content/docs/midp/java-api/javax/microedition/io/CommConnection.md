---
title: "Interface CommConnection"
---

`package javax.microedition.io`

```text
 CommConnection cc = (CommConnection)
            Connector.open("comm:com0;baudrate=19200");
 int baudrate = cc.getBaudRate();
 InputStream is  = cc.openInputStream();
 OutputStream os = cc.openOutputStream();
 int ch = 0;
 while(ch != 'Z') {
     os.write(ch);
     ch = is.read();
     ch++;
 }
 is.close();
 os.close();
 cc.close();
```

## 설명

아래 예에서는 `CommConnection`을 사용하여
이용 가능한 통신 포트를 검색하는 방법을 보여 줍니다.

논리적 포트 이름은 영숫자 문자의 조합을 사용하여 
플랫폼 이름 지정 규약과 일치하도록 정의할 수 있습니다. 
하지만 제안된 규약에 따라 이 클래스의 
각 구현에서 일관성 있게 포트 이름을 지정하는 것이 좋습니다. 
가상 머신 구현 시 다음 규약을 따라야 합니다.
 
 포트 이름에는 포트 기능을 나타내는 텍스트 약어가 포함되며 
그 뒤에는 포트의 일련 번호가 옵니다. 
다음과 같은 장치 이름 유형을 사용해야 합니다.

- COM#, 여기서 COM은 RS-232 포트에 사용되고 
#은 포트에 할당된 번호입니다.
- IR#, 여기서 IR은 IrDA IRCOMM 포트에 사용되고 
#은 포트에 할당된 번호입니다.

이 이름 지정 체계에서는 API 사용자가 원하는 
포트 유형을 결정할 수 있습니다. 
예를 들어, 응용 프로그램이 데이터 조각을 "빔"하려는 경우에는 
연결을 열 "IR#" 포트를 찾을 수 있습니다. 
또는 사용 가능한 모든 포트를 시도해 볼 수도 있습니다.

**Since:**
- MIDP 2.0

## 메서드 요약

- `int getBaudRate ()` — 직렬 포트 연결의 보 속도를 가져옵니다.
- `int setBaudRate (int baudrate)` — 직렬 포트 연결의 보 속도를 설정합니다.

## 메서드 상세

### getBaudRate

```java
public int getBaudRate()
```

**Returns:**
- 연결의 보 속도

**See Also:**
- ``setBaudRate(int)``

### setBaudRate

```java
public int setBaudRate(int baudrate)
```

**Parameters:**
- `baudrate` - 연결의 보 속도

**Returns:**
- 연결의 이전 보 속도

**See Also:**
- ``getBaudRate()``
