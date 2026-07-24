---
title: "2.3. 시스템"
---

표준 플랫폼 커널에서 단말기의 정보 또는 이벤트를 입력받아 다음 수행 동작을 결정 하는 함수들이다. 커널의 동작 수행 상태를 확인 하기 위해 디버깅 하는 콘솔을 지원 하는 함수와 크리티컬 섹션(Critical Section) 을 보호 하기 위해서 단말기 운영체제에서 지원하는 잠금 메커니즘을 구현한 함수와 커널이 사용할 메모리영역을 잡아주는 함수 등으로 구성되어 있다.

### MH_sysGetHeapBlock

**프로토타입**

```c
void MH_sysGetHeapBlock (M_Uint32* start, M_Uint32* size)
```

**설명**

이 함수는 플랫폼이 사용할 휘발성 메모리의 크기와 시작번지를 얻어오는 함수 이다. 이 메모리는 고정되어야 하며, 플랫폼을 제외한 타 소프트웨어 모듈 이 메모리를 사 용해서는 안된다.

**매개 변수**

- `start` - [out] Heap의 시작 번지 반환
- `size` - [out] Heap의 사이즈 반환

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_sysGetInformation

**프로토타입**

```c
M_Int32 MH_sysGetInformation (M_Char* command, M_Char* buf, M_Int32 bufSize)
```

**설명**

이 함수는 단말기의 시스템 정보를 얻어오는 함수이다. 반환할 값이 정수일 때는 10 진수 string으로 변환하여 버퍼를 통하여 반환한다. 제조사나 이통사가 플랫폼에서 정 의되지 않은 정보를 확장하고 싶은 경우, command값을 추가하여 확장한다. 예) `M_Char` buf[16]; `MH_sysGetInformation`(”ESN”, buf, sizeof(buf));

**매개 변수**

- `command` - [in] String 값
- `buf` - [out] 버퍼
- `bufSize` - [out] 버퍼 크기

> **<표 2-3-2> 시스템 명령**

Command 비고
“ESN” ESN번호
“NID” 네트워크 식별(Network Identification )
“SID” 시스템 식별(System Identification)
“BASEID” 기본 스테이션 식별(Base station Identification)
“BASELAT” 기본 스테이션 위도(Base station Latitude)
“BASELONG” 기본 스테이션 경도(Base station longitude)
“CURRENTCH” 현재 채널 번호(Current Channel number)
“PHONENUMBER” 전화 번호
“RSSILEVEL” 현재 RSSI 레벨
“BATTERYLEVEL” 현재 배터리레벨
“MAXRSSILEVEL” 최대 RSSI 레벨
“MAXBATTLEVEL” 최대 배터리 레벨
“MAXSERIALNUM” 최대 지원되는 시리얼포트 개수
“MAXSOCKETNUM” 최대 지원되는 소켓 개수
“MEDIADEVICES” 지원하는 미디어 device의 문자열, 여러 개일 경우 “,”
로 구분함. 지원되는 device가 없으면 M_E_NOTSUP를
반환.
미리 정의된 문자열
문자열 Device
“Qualcomm_CMX” Qualcomm CMX
“Yamaha_MA1” Yamaha MA1
“Yamaha_MA2” Yamaha MA2
“Yamaha_MA3” Yamaha MA3
“Yamaha_MA5” Yamaha MA5
“audio/MIDI” MIDI 포맷을 play할 수 있는
디바이스일 경우,
“audio/MP3” MP3 포맷을 play할 수 있는
디바이스일 경우,
“IS96” QCELP-8K
“IS96A” QCELP-8K
“IS733” QCELP-13K
“IS127” EVRC-8K
디바이스가 미리 정의된 문자열을 지원할 시에는 정의
된 문자열을 반환하고, 그렇지 않을 경우에는 벤더나 이
통사에서 정의하여 확장한다. 지원되는 포맷이 하드웨어
종속적이 아닌 경우에는 “audio/xxx”와 MIME타입에 따
라 확장한다.
예) 운영체제가 CMX, MA1 EVRC-8K을 지원할 경우, 반
환되는 문자열
“Qualcomm_CMX, Yamaha_MA1”
“DNS” 도메인 네임 서버를 지정한다. IP 주소 문자열. 예)
“127.0.0.1”
“TIMEZONE” “GMT+시:분 “, “GMT-시:분“와 같은 형태로 현재의
time zone을 반환한다. 시, 분은 각각 두 자리 문자열을
사용한다.
예) “GMT+09:30”, “GMT-12:00”
“PHONEMODEL” 단말기의 모델 ID string
폰 모델
“KEYREPEAT” “반복시작시간:반복주기시간”, 단위는 ms이다.
지원하지 않으면 M_E_NOTSUP반환할 수 있다.
예) “600:250” 버튼이 눌려지고 600ms후에
MH_KEYREPEAT_EVENT가 처음 발생한 후, 250ms마다
주기적으로 버튼이 떼어질 때까지 발생한다.
“VIBRATORLEVEL” 하드웨어가 지원하는 진동세기의 단계를 반환한다.
(최소 0, 최대 100)
예) “3” 3단계의 진동세기 지원
“1” 1단계의 진동세기 지원
“VOLUMELEVEL” 하드웨어가 지원하는 볼륨세기의 단계를 반환한다.
(최소 0, 최대 100)
예) “10” 10단계의 볼륨세기 지원
“4” 4단계의 볼륨세기 지원
“IODEVICES” 지원하는 I/O device의 문자열, 여러 개일 경우 “,”로 구
분함 지원되는 device가 없으면 M_E_NOTSUP를 반환
문자열 device
“IrDA” IrDA 장치
“Camera” 카메라 장치
“1ChipCard” 1Chip용 IC 카드 장치
“Bluetooth” 블루투스 장치
디바이스가 미리 정의된 문자열을 지원할 시에는 정의
된 문자열을 반환하고, 그렇지 않을 경우에는 벤더나 이
통사에서 정의하여 확장한다.
“DEFAULTVOLUME” 단말기가 제공하는 시스템 볼륨 문자열
단말기가 제공하는 시스템 볼륨 카테고리 문자열, 여러
개일 경우 “,” 로 구분함.
지원되는 시스템 볼륨 카테고리가 존재하지 않으면
`M_E_NOTSUP` 에러값을 반환함
문자열 설명
“GENERAL” 일반적인 application에서 사
용되는 특성을 갖는다.
“VOICE” 음성의 재생/녹음 특성을 갖
는다.
“RING” 착신 벨 특성을 갖는다. 예를
들어 현재 착신 벨이 진동으
로 되어 있다면, play 시 소리
가 나지 않고 진동이 발생한
다. 별도의 멜로디용 speaker
가 따로 있다면 이를 통해 소
리가 발생한다. 즉, 단말기에
전화가 왔을 때의 특성 그대
로 행동 한다.
“KEY” 키 톤의 특성을 갖는다.
“MESSAGE” SMS message 도착 경고음
특성을 갖는다.
“ALARM” 알람 경고음 특성을 갖는다.
“ALERT” No service, low battery 각종
경고음 특성을 갖는다.
“MMEDIA” TCM2, AOD, VOD 재생시 사
용되는 특성을 갖는다.
“GAME” 게임 시 재생되는 특성을 갖
는다.
“OEM” 위에서 정의되지 않은 음량에
대한 설정 시 사용한다.
“REGISTRABLESTATUS_I `MH_termResRegister()` 함수를 통하여 단말의 IDLE 상
DLE” 태에 설정이 허용된 단말 리소스 그룹 목록을 반환함
여러 개일 경우 “,”로 구분함
“REGISTRABLESTATUS_I `MH_termResRegister()` 함수를 통하여 단말의
NCOMING” INCOMING 상태에 설정이 허용된 단말 리소스 그룹 목
록을 반환함 여러 개일 경우 “,”로 구분함
“REGISTRABLESTATUS_P `MH_termResRegister()` 함수를 통하여 단말의
OWERON” POWERON 상태에 설정이 허용된 단말 리소스 그룹 목
록을 반환함 여러 개일 경우 “,”로 구분함
“REGISTRABLESTATUS_P `MH_termResRegister()` 함수를 통하여 단말의
OWEROFF” POWEROFF 상태에 설정이 허용된 단말 리소스 그룹
목록을 반환함 여러 개일 경우 “,”로 구분함
“REGISTRABLESTATUS_B `MH_termResRegister()` 함수를 통하여 단말의
ROWSERON” BROWSERON 상태에 설정이 허용된 단말 리소스 그룹
목록을 반환함 여러 개일 경우 “,”로 구분함
“REGISTRABLESTATUS_B `MH_termResRegister()` 함수를 통하여 단말의
ROWSEROFF” BROWSEROFF 상태에 설정이 허용된 단말 리소스 그룹
목록을 반환함 여러 개일 경우 “,”로 구분함
“SUPPORTGLOCK” 단말 리소스 그룹 중 그룹 Lock을 지원하는 리소스 그
룹의 목록을 반환함. 여러 개일 경우 “,”로 구분함
“SUPPORTPLOCK” 단말 리소스 그룹 중 개별 리소스 Lock을 지원하는 리
소스 그룹의 목록을 반환함. 여러 개일 경우 “,”로 구
분함
"NOTDELGROUP" 리소스의 삭제를 허용하지 않는 리소스 그룹 목록을 반
환함. 여러 개 일 경우 ","로 구분함.

**반환 값**

성공

실패

- `M_E_INVALID` - 전달한 매개변수가 잘못되었음
- `M_E_NOTSUP` - 지원하지 않는 command 임
- `M_E_SHORTBUF` - 반환되는 문자열보다 전달한 버퍼 크기가 작 을 때 발생
- `M_E_ACCESS` - 읽어 올 수 없는 단말기의 정보임

**부작용**

없음

**참고 항목**

없음

### MH_sysSetInformation

**프로토타입**

```c
M_Int32 MH_sysSetInformation(M_Char* cmd, M_Char* value)
```

**설명**

시스템 정보 값을 변경할 때 사용하는 함수이다. HAL 구현 시 단말기 기본 소프트웨 어에 따라 변경이 불가능한 정보가 있을 수 있다.

**매개 변수**

- `cmd` - [in] 변경하고자 하는 정보명.
- `value` - [in] cmd에 해당하는 정보값을 나타내는 문자열

**반환 값**

성공

실패

- `M_E_ACCESS` - 변경할 수 없는 정보임
- `M_E_INVALID` - cmd값이나 value값이 잘못됨

**부작용**

없음

**참고 항목**

없음

### MH_sysLock

**프로토타입**

```c
void MH_sysLock (void)
```

**설명**

크리티컬 섹션을 보호하기 위한 함수 이다. 플랫폼 외부 문맥의 진입을 금지하는 영역의 시작을 지정한다. `MH_sysUnlock` 함수의 해 재진입을 허용한다. `MH_pltEvent()` 같은 함수는 운영체제가 플랫폼에 이벤트를 전달하기 위하여 부른다. 운영체제가 `MH_pltEvent`()를 호출 할 때는 운영체제의 인터럽트 서비스 루틴(Interrupt Service Routine)에서 호출할 수도 있고, 플랫폼 태스크가 아닌 다른 태스크에서 호출 할 수도 있다. 이때 호출된 `MH_pltEvent()` 함수와 플랫폼의 context에서 사용하는 영 역간에 크리티컬 섹션이 발생한다. 포팅자는 `MH_sysLock`()이 불려진 경우에는 `MH_sysUnlock`()이 호출될 때까지 운영체제가 `MH_pltEvent`()를 부르지 않도록 HAL을 구현해야 한다. `MH_sysLock()`, MH_sysUnlock은 중복되게 호출될 수 있다. 이때 맨 처음 `MH_sysLock`()이 호출될 때 lock이 되고, 맨 마지막 MH_sysUnlock이 호출될 때 lock 이 해제 되어야 한다.

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MH_sysUnlock`

### MH_sysUnlock

**프로토타입**

```c
void MH_sysUnlock (void)
```

**설명**

MH_sysLock에서 진입 금지한 상태를 해제 한다..

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MH_sysLock`

### MH_sysHalInit

**프로토타입**

```c
void MH_sysHalInit (void)
```

**설명**

Hal 초기화 루틴 이다. 이 함수는 어떤 HAL API도 사용되기 이전에 최초 호출 되어야 한다. HAL에서 지원하 는 API중 초기화가 필요한 API는 여기서 초기화 과정을 수행하도록 한다.

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_sysHalExit

**프로토타입**

```c
void MH_sysHalExit()
```

**설명**

플랫폼 종료 시 호출되는 함수이다. HAL 계층에서 사용된 자원 해제 등 각 단말기 HAL에 맞도록 플랫폼 종료 시 취해야 할 작업을 정의한다.

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_sysWait

**프로토타입**

```c
void MH_sysWait (void)
```

**설명**

Binary semaphore wait 기능이다. 플랫폼은 내부적으로 더 이상 처리할 일이 없을 때 이 함수를 부른다. HAL은 이 함수 가 불리면 태스크를 blocking시켜 CPU power를 소비하지 않도록 구현해야 한다.

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_sysSignal

**프로토타입**

```c
void MH_sysSignal (void)
```

**설명**

Binary semaphore signal 기능이다. 이 함수가 불리면 `MH_sysWait`()에서 blocking된 태스크를 깨워주어야 한다. 이 함수는 주로 `MH_pltEvent`()내에서 주로 사용한다. `MH_sysSignal`()은 인터럽트 서비 스 루틴 안에서 불려도 동작하게 포팅 해야 한다.

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_debugPutChar

**프로토타입**

```c
void MH_debugPutChar(M_Char ch);
```

**설명**

플랫폼의 디버깅정보를 출력한다. 플랫폼의 표준출력은 모두 이 API로 오게 된다. HAL구현자는 이 API를 시리얼, 네트워크, 콘솔(console)등 적절한 곳으로 연결하여 메시지를 볼 수 있다.

**매개 변수**

- `ch` - [in] 출력한 문자

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음
