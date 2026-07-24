---
title: "2.10. 단말 리소스"
---

## 2.10.1. 개요

#### 용어정의

단말 리소스 이미지, 사운드, 주소록 등 특정 데이터 포맷을 가지면서 단말 영역에 저장된 데이 터들을 통칭. 단말 리소스 그룹 리소스들을 이동 통신사 자체적인 서비스 이름(그림친구, 벨소리, 사진, 음성녹음)에 따라 분류해 놓은 그룹. 단말 리소스 함수 단말 리소스 그룹 및 단말 리소스의 접근 및 이용이 가능한 함수. 리소스 그룹 이름 리소스 그룹을 나타내는 이름이다. 리소스 이름 리소스의 이름으로 리소스 그룹에서 리소스를 구별하는 유일한 식별자이다. OEM에 서 생성하며 동일 리소스 그룹에서 리소스 이름은 중복될 수 없다. 리소스 UI(User Interface) 이름 리소스가 UI 화면 상에 나타내는 이름이다. 응용 프로그램에서도 생성 가능하며, 동 일 리소스그룹에서 중복이 허용된다. 리소스 그룹 리스트 각각의 리소스 그룹의 이름을 ‘\0’문자로 구분한 리소스 그룹의 리스트. 마지막에는 ‘\0’문자가 2개 연속으로 온다. 단말 리소스 함수의 출력 값으로 사용되는 형식이다. 리소스 리스트 각각이 리소스 이름을 ‘\0’문자로 구분한 리소스 이름 리스트. 마지막에는 ‘\0’문 자가 2개 연속으로 온다. 단말 리소스 함수의 출력 값으로 사용되는 형식이다. 폰북개인 PHONEBOOK/PRIVATE 리소스 그룹의 리소스로서 단말기의 주소록이다. 폰북그룹 PHONEBOOK/GROUP 리소스 그룹의 리소스로서 단말기의 주소록 그룹이다. 단축번호 PHONEBOOK/SHORTKEY 리소스 그룹의 리소스로서 폰북개인의 특정 전화번호에 할당된, 전화번호보다 간단한 번호로서, 이를 이용하여 보다 간단하게 전화를 걸 수 있게 한다. 그룹 Lock 리소스 그룹이 Lock되어 있는 상태. 그룹 Lock된 리소스 그룹에 접근하는 API를 실 행하기 전에는 비밀번호를 확인하여야 한다. 그룹 Lock은 개별 Lock과는 무관하게 설정/해제한다. 그룹 Lock이 설정된 그룹의 리소스의 경우 리소스 갱신, 삭제, 읽기 의 접근이 불가능하다(리소스 생성은 가능) 개별 Lock 리소스가 Lock되어 있는 상태. 개별 Lock된 리소스에 접근하는 API를 실행하기 전 에는 비밀번호를 확인하여야 한다. 개별 Lock은 그룹 Lock과는 무관하게 설정/해제 한다. 개별 Lock이 설정된 리소스의 경우 리소스 갱신, 삭제, 읽기 접근이 불가능하 다. Lock 설정 리소스 그룹에 그룹 Lock 설정 또는 리소스에 개별 Lock 설정. Lock 설정시에는 비 밀번호를 확인하여야 한다. Lock 설정 여부 확인은 리소스 갱신, 삭제, 읽기의 시도 시에만 수행하며 기타 리소스 접근의 경우 Lock 설정 여부 확인하지 않는다. Lock 해제 리소스 그룹에 그룹 Lock 해제 또는 리소스에 개별 Lock 해제. Lock 해제시에는 비 밀번호를 확인하여야 한다. Lock 상태 그룹 Lock이 지원되는 리소스 그룹의 경우 그룹 Lock이 설정되었는지 그렇지 않은 지를 나타내는 상태. 또는 개별 Lock이 지원되는 리소스 그룹의 리소스의 경우 리소 스에 개별 Lock이 설정되었는지 그렇지 않은지를 나타내는 상태. Lock 상태와 리소스 접근 리소스의 데이터를 읽거나 쓰고 지우는 등 리소스에 접근할 때, 리소스가 포함된 리 소스 그룹이 그룹 Lock되어 있거나, 리소스가 개별 Lock되어 있으면 비밀번호를 확 인해야 한다. 비밀번호 단말기에 설정된 비밀번호. 이미지 리소스 화면에 보여지는 그림, 사진등의 리소스 (Animated Bitmap, 사운드가 없는 동영상 등 여러 이미지가 연속적으로 보여지는 리소스 포함) 사운드 리소스 벨, 음악등 소리가 재생되는 리소스 이미지와 사운드가 모두 포함된 리소스 화면에 보여지는 이미지가 있고 소리가 재생되는 리소스 단말 특정 상태 대기(IDLE), 전화 수신(INCOMING), 단말 구동(POWERON), 단말 종료(POWEROFF), 브라우저 구동(BROWSERON), 브라우저 종료(BROWSEROFF)의 6가지 단말 상태 Unique ID 망제공자나 Contents Provider에 의해 할당된 리소스의 유일한 ID 그룹 정보 단말 리소스 함수를 통해 얻을 수 있는 특정 리소스 그룹의 정보. 그룹 정보는 리소 스 그룹과 그룹 정보 타입에 따라 달라진다. 그룹 정보 타입 그룹 정보의 종류. 단말 리소스 함수를 통해 지정한 그룹 정보 타입에 따라, 지정한 리소스 그룹의 그룹 정보를 얻어 올 수 있다. 리소스 정보 단말 리소스 함수를 통해 얻을 수 있는 특정 리소스의 정보. 리소스 정보는 리소스 와 리소스 정보 타입에 따라 달라진다. 리소스 정보 타입 리소스 정보의 종류. 단말 리소스 함수를 통해 지정한 리소스 정보 타입에 따라, 지 정한 리소스의 리소스 정보를 얻어 올 수 있다. 검색어 단말 리소스 함수를 통해 리소스 검색시 사용하는 질의어(query). 리소스 검색시 단 말 리소스 함수는 검색어 타입에 따라 검색어 문자열을 가진 리소스의 리스트를 반 환한다. 검색어 타입 단말 리소스 함수를 통해 리소스 검색시 사용하는 검색어의 종류. 리소스 검색시 검 색어 타입에 따라 각기 다른 종류의 검색이 이루어지게 된다. 검색어 타입과 검색어 로 리소스를 검색한다. 검색 모드 검색 모드에 따라 주어진 문자열과 정확히 일치하는지를 검색하거나, 또는 주어진 문자열을 포함하는지를 검색한다. 쓰기 모드 단말 리소스 write시 새로운 리소스를 생성할 것인지, 기존 리소스를 덮어 쓸 것인지 를 결정 리소스 이름 확인 지정한 리소스 그룹에 지정한 리소스 이름의 리소스가 존재하는지 여부를 확인한다. wCard 표준 명함 데이터 포맷인 vCard 3.0을 기반으로 하여 단말의 주소록에서 필요한 정 보를 확장하여 정의한 WIPI 주소록 포맷을 말한다.

#### 개요

이미지, 사운드, 주소록 등 특정 데이터 포맷을 가지면서 단말 영역에 저장된 데이 터들을 통칭하여 단말 리소스(이하 리소스)라한다. 리소스들을 이동 통신사 자체적인 서비스 이름(그림친구, 벨소리, 사진, 음성녹음)에 따라 분류해 놓은 그룹을 단말 리소스 그룹 (이하 리소스 그룹)이라 한다. 모든 리소 스는 각각의 리소스 그룹에 속하게 된다. 단말 리소스 함수들은 WIPI 어플리케이션이 리소스 그룹과 리소스에 접근하는 통로 를 제공한다.

#### 함수 기능 및 목록

기 능 목 록 `MC_termResGetFormat` `MC_termResGetSize` `MC_termResGetUIName` `MC_termResExists` `MC_termResRead` 단말 리소스 관리 `MC_termResWrite` `MC_termResDelete` `MC_termResRegister` `MC_termResGetRegisteredInfo` `MC_termResGetInfo` `MC_termResSearch` `MC_termResGetSupportedGroups` `MC_termResGetCount` 단말 리소스 그룹 관리 `MC_termResGetList` `MC_termResGetGroupInfo` `MC_termResGetGroupLockState` 단말 리소스 보안 `MC_termResGetLockState` `MC_termResSetGroupLockState` `MC_termResSetLockState` `MC_termResCheckPassword` `MC_termResGetFreeSpace` 단말 리소스 기타 `MC_termResExecuteCmd`

#### 단말 리소스 그룹

각 리소스 그룹은 다수의 리소스들로 이루어져 있으며, 각 리소스들은 특정 데이터 포맷을 가질 수 있다. 미리 정의된 리소스 그룹은 다음과 같다. “PICTUREMATE” – 그림친구 “MUSICBELL” – 벨소리 “PHOTO” – 사진 “VOICE” – 음성녹음 “PHONEBOOK/PRIVATE” – 주소록(개인) “PHONEBOOK/GROUP” – 주소록(그룹) “PHONEBOOK/SHORTKEY” – 단축번호 “BLACKLIST” – 블랙리스트. 전화번호에 소리/진동/램프 상태를 설정 “SMSDATA/SENT” – SMS 발신 데이터 “SMSDATA/RECV” – SMS 수신 데이터

#### 리스트 형식

단말 리소스 함수가 하나의 매개 변수에 다수의 데이터를 입력 또는 출력 값으로 사 용할 때, 각각의 데이터 구분은 „\0‟(`NULL`)문자로 하며 마지막에는 „\0‟문자가 2개 연속으로 온다. “PHOTO\0MUSICBELL\0\0” “mypicture01\0mypicture02\0...mypictuer100\0\0” “MUSICBELL;mymusicbell\0PICTUREMATE;mypicture\0\0” “0114441234\001199995555\0Friend\0Family\0\0” “1\0100\0\0”

#### 단말 리소스 이름 형식

단말 리소스에 대한 모든 접근은 리소스 이름을 통해 이루어지므로 OEM은 어플리 케이션이 리소스 그룹 내에서 리소스 이름을 유일한 식별자로 사용할 수 있도록 중 복되지 않게 리소스 이름을 제공한다. 어플리케이션은 리소스를 새로 생성할 때 리 소스 이름을 지정할 수 없으며, OEM이 제공하는 리소스 이름을 받아 사용한다.

#### 리소스 이름 형식

리소스 이름은 리소스 그룹내에서 유일해야 한다는 조건 이외에 다른 제한은 없으며 단말이 제공한다.

#### 고정된 리소스 이름

아래의 리소스 이름은 고정된 것으로 해당 그룹의 해당 리소스 데이터를 접근하기 위해서는 주어진 리소스 이름을 사용하여야 한다. 리소스 그룹 리소스 이름 비고 PHONEBOOK/SHORTKEY 지정된 단축 번호 문자열. 예) “5”, “49”

#### 리소스 UI(User Interface) 이름

리소스가 UI 화면 상에 나타내는 이름이다. 리소스 그룹에 따라, 리소스에 UI이름이 없는 리소스 그룹이 있을 수 있다. (단, PHONEBOOK/GROUP과 PHONEBOOK/SHORTKEY 그룹은 리소스 이름과 UI 이름이 같아야 한다.)

#### 리소스 이름과 UI 이름

리소스에는 리소스 이름과 UI이름이 있다. 다음은 리소스 이름과 UI이름의 설명이다. 리소스 이름은 리소스 그룹내에서 리소스를 구분하는 유일한 식별자이다. PHONEBOOK/SHORTKEY 그룹은 리소스 이름이 규격에 정해져 있고, 이를 제외한 나머지 그룹의 리소스 이름은 단말에서 관리하게 된다. 어플리케이션은 단말이 제공 하는 리소스 이름의 리스트을 받아서 사용하며, 리소스를 새로 생성할 때에도 단말 이 넘겨주는 리소스 이름을 받아서 사용한다. 리소스 이름은 인덱스가 될 수도 있고 어떠한 형태의 문자열이 와도 상관 없으며, 단말은 오직 어플리케이션에게 리소스를 접근할 수 있도록 중복되지 않는 유일한 이름을 제공해준다. 반면에 UI이름은 UI를 통해서 사용자에게 보여지는 이름이다. 예를 들어 PHOTO그룹의 경우 카메라 촬영 후 얻은 이미지에 사용자가 직접 입력 하여 설정한 이름이 UI이름이다. 어플리케이션이 사용자에게 단말에 저정된 PHOTO 그룹의 이미지 리스트를 보여줄 경우 UI이름이 단말 화면에 나타나게 된다. 또는 사 용자가 이름을 설정하지 않고 단말이 사진의 이름을 알아서 생성해 주는 경우라 해 도, 어플리케이션이 사진 리스트를 보여 주어야 하는 경우라면, 각 사진의 이름 리 스트를 보여주어야 한다. 이럴 경우 UI이름이 필요하게 된다. 또 다른 예로 MUSICBELL그룹의 벨소리라면 각각의 리소스마다 "내 마음의 별", "소양강 처녀", " 돌아와요 부산항에" 등의 사용자에게 보여지는 이름이 있을 것이다. 이렇게 사용자 에게 보여지는 이름이 UI이름이다. 그러나 리소스에 따라서 UI이름이 없는 리소스도 있을 수 있다. 예를 들어 SMS DATA 등의 경우가 이에 해당한다. SMS DATA는 보통 메시지 리스트에서, 메시지의 처음 일부분을 사용자에게 보여주므로 UI이름이 필요하지 않게 된다. 즉 리소스 이름은 리소스를 이용하기 위한 식별자이고, UI이름은 UI를 통해서 사용 자에게 보여지는 이름이다. 하나의 리소스 그룹내에서 리소스 이름은 중복이 불가능 하며, UI이름은 중복이 가능하다. 리소스 이름은 모든 리소스에 부여되며, UI이름은 UI이름이 필요한 리소스그룹의 리소스에게만 부여된다. 리소스 이름은 어플리케이션 이 설정 및 변경할 수 없으며, UI이름은 어플리케이션이 설정 및 변경이 가능하다.

#### MIME 타입 및 리소스 데이터 포맷

각 단말 리소스는 다음과 같이 MIME 타입과 데이터 포맷을 가지고 있다. 이미지 포맷 MIME 타입 데이터 포맷 image/bmp Bitmap 이미지 포맷 image/gif GIF 이미지 포맷 image/jpeg JPEG 이미지 포맷 image/png PNG 이미지 포맷 image/sis SIS 이미지 포맷 Animation 포맷 MIME 타입 데이터 포맷 anim/sis SIS 이미지 포맷 anim/gif GIF 이미지 포맷 동영상 포맷 MIME 타입 데이터 포맷 video/MPEG4 Mpeg4 video/H.263 H.263 video/H.264 H.264 사운드 포맷 MIME 타입 데이터 포맷 Qualcomm_CMX Qualcomm CMX Yamaha_MA1 Yamaha MA1 Yamaha_MA2 Yamaha MA2 Yamaha_MA3 Yamaha MA3 Single Channel Format Yamaha_MA5 Yamaha MA3 Yamaha_SMAF Yamaha Single Channel Format Yamaha_SMAF-Phrase Yamaha Multi Channel Format Yamaha_SMAF-Audio Yamaha SMAF-Audio Format audio/ONEPOLY One Poly Media Format audio/GVMONEPOLY GVM One Poly Media Format audio/MIDI MIDI audio/MP3 MP3 audio/TONE Tone audio/FREQTONE Frequency Tone IS96 QCELP-8K IS96A QCELP-8K IS733 QCELP-13K IS127 EVRC-8K G.723.1 G.723.1 audio/AAC AAC audio/AAC+ AAC+ AMR-WB WCDMA용 음성 코덱 AMR-NB 폰북개인, 폰북그룹 및 SHORTKEY 포맷 MIME 타입 데이터 포맷 phonebook/private wCard 문자열 phonebook/group 실제 그룹 이름 문자열 : UI를 통해서 보여지는 이름 phonebook/shortkey <폰북개인의 리소스 이름> + „/‟ + <wCard TEL Type의 Type 및 Value> 예) 리소스 이름이 “김철수”인 폰북개인 리소스의 집전화번호 가 02-1234-5678인 경우 “김철수/TEL;TYPE=home:0212345678” BLACKLIST 포맷 MIME 타입 데이터 포맷 blacklist blacklist 데이터 = NUMBER + „;‟ + STATE NUMBER : 착신번호 („-„가 없는 문자열 형태) STATE : blacklist 설정 상태 “SND” : 사운드 상태로 설정된 경우 “VIB” : 진동 상태로 설정된 경우 “LMP” : Lamp 상태로 설정된 경우 예) 011-1234-5678번을 Lamp 상태로 설정한 경우 “01112345678;LMP” SMS 착발신 데이터 포맷 MIME 타입 데이터 포맷 smsdata SMS 데이터 = TID + „\0‟ + STATE + „\0‟ + NUMBER + „\0‟ + DATA + „\0‟ + TIME + „\0‟ + „\0‟ TID : 텔레서비스 아이디 번호 문자열 STATE : 메시지의 상태 „0‟ : 새로운 메시지 „1‟ : 이미 읽은 메시지 NUMBER : 발신자 또는 수신자 전화 번호 문자열 („-„ 없음) DATA : ASCII 형식의 SMS 메시지 문자열 TIME : 착발신 시간 문자열 (년월일시분(yyyymmddhhmm) 형태) 예) 2003년 05월 04일 12시 55분에 011-1234-5678번으로부터 “Hello”라는 메시지가 새로 도착한 경우 “10\00\001112345678\0Hello\0200305041255\0\0”

#### 단말 리소스 관리 기능

특정 리소스에 대하여 리소스의 데이터 포맷 및 리소스의 데이터 크기를 알아올 수 있는 기능과, 리소스에 데이터를 써넣거나 읽어오는 기능, 그리고 리소스를 지우는 기능이 제공된다. 특정 단말 상태(“POWERON”, “POWEROFF”, “IDLE”, “INCOMING”, “BROWSERON”, “BROWSEROFF”)에 특정 리소스를 설정할 수 있고, 설정된 정보를 얻어올 수 있다. 특정 리소스의 정보를 얻어 오며, 리소스 검색하고, 특정 이름의 리 소스가 있는지 확인할 수 있다.

#### 단말 리소스 그룹 관리 기능

단말이 지원하는 리소스 그룹을 얻어오고, 특정 리소스 그룹의 리소스 개수와 리소 스 이름 리스트와, 리소스 그룹의 정보를 알 수 있다.

#### 단말 리소스 보안 기능

특정 리소스 그룹 및 리소스에 대해 Lock 상태을 얻어올 수 있으며 설정/해제할 수 있다. 사용자로부터 암호를 입력 받아 단말에 설정된 암호와 비교하여 암호가 적합 한지 그렇지 않은지를 평가할 수 있다. 어플리케이션은 그룹 Lock된 리소스 그룹의 리소스 데이터를 읽고 쓰고 지우거나, 개별 Lock된 리소스의 데이터를 읽고 쓰고 지우는 등의 리소스 접근시에는, 사용자 로부터 입력받은 비밀번호가 단말기에 설정된 비밀번호와 일치하는지 확인한 후 하 여야 한다. 또 Lock 설정/해제시에도 어플리케이션은 비밀번호를 확인한 후 하여야 한다.

#### 단말 리소스 기타 기능

단말 리소스 저장공간의 남은 여유공간 크기를 얻어오며, 지정한 명령에 따라 특정 서비스를 수행할 수 있다.

#### 리소스 그룹별 사용 가능 API 목록

다음은 단말 리소스 API 중 리소스 그룹을 지정하는 API들의 사용 가능한 리소스 그룹을 나타낸다. (리소스 그룹을 지정하지 않는 API는 다음 표와 무관하다.) 리소스 그룹 사용 가능한 API 모든 리소스 그룹 `MC_termResGetCount` `MC_termResGetList` `MC_termResGetFormat` `MC_termResGetSize` `MC_termResExists` `MC_termResRead` 단말에 따라 다름 `MC_termResGetGroupLockState` `MC_termResSetGroupLockState` `MC_termResGetLockState` `MC_termResSetLockState` `MC_termResGetUIName` Parameter에 따라 다름 `MC_termResGetGroupInfo` (infoType에 따라 다르다) `MC_termResGetInfo`(info Type에 따라 다르다) `MC_termResSearch` (queryType에 따라 다르다) `MC_termResExecuteCmd` (명령에 따라 다르다) PICTUREMATE `MC_termResWrite` MUSICBELL `MC_termResDelete` PHOTO `MC_termResRegister` VOICE PHONEBOOK/PRIVATE `MC_termResWrite` PHONEBOOK/SHORTKEY `MC_termResDelete` PHONEBOOK/GROUP BLACKLIST SMSDATA/SENT SMSDATA/RECV

#### Lock 상태

**프로토타입**

```c
#define MC_TERMRES_GROUP_LOCK 1
#define MC_TERMRES_GROUP_UNLOCK 2
#define MC_TERMRES_PRIVATE_LOCK 4
#define MC_TERMRES_PRIVATE_UNLOCK 8
```

**설명**

단말 리소스 그룹 및 단말 리소스의 Lock 상태를 나타낸다.

**참고 항목**

`MC_termResGetGroupLockState` `MC_termResGetLockState` `MC_termResSetGroupLockState` `MC_termResSetLockState`

#### 검색 모드

**프로토타입**

```c
#define MC_TERMRES_EXTSRCH 1
#define MC_TERMRES_INCSRCH 2
```

**설명**

단말 리소스 검색시 검색 모드를 결정한다.

**참고 항목**

`MC_termResSearch`

#### 쓰기 모드

**프로토타입**

```c
#define MC_TERMRES_CREATE 1
#define MC_TERMRES_UPDATE 2
```

**설명**

단말 리소스 Write시 쓰기 모드를 결정한다.

**참고 항목**

`MC_termResWrite`

#### 리소스 이름 확인

**프로토타입**

```c
#define MC_TERMRES_NAME_EXISTENT 1
#define MC_TERMRES_NAME_NONEXISTENT 2
```

**설명**

해당 리소스 그룹에 해당 리소스 이름의 리소스가 존재하는지 나타낸다.

**참고 항목**

`MC_termResExists`

### MC_termResGetSupportedGroups

**프로토타입**

```c
M_Int32 MC_termResGetSupportedGroups(M_Byte* resGroup, M_Int32 bufSize)
```

**설명**

단말이 지원하는 리소스 그룹 리스트를 반환한다.

**매개 변수**

- `resGroup` - [out] 리소스 그룹 리스트(단말 리소스 개요의 리스트 형식 을 따른다)
- `bufSize` - [in] resGroup 버퍼 크기

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_SHORTBUF` - 반환값이 담길 버퍼 크기가 작을 경우

**부작용**

없음

**참고 항목**

없음

### MC_termResGetCount

**프로토타입**

```c
M_Int32 MC_termResGetCount(M_Char* resGroupName)
```

**설명**

지정한 리소스 그룹에 속하는 리소스의 개수를 반환한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름

**반환 값**

성공

리소스 개수
실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹이 전달된 경우

**부작용**

없음

**참고 항목**

없음

### MC_termResGetList

**프로토타입**

```c
M_Int32 MC_termResGetList(M_Char* resGroupName, M_Byte* aszList,
M_Int32 bufSize)
```

**설명**

지정한 리소스 그룹에 속하는 리소스 리스트를 반환한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `aszList` - [out] 리소스 이름 리스트 (단말 리소스 개요의 리스트 형식 을 따른다)
- `bufSize` - [in] aszList 버퍼 크기

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_SHORTBUF` - 반환되는 문자열보다 전달한 버퍼크기가 작을때 발생
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹이 전달된 경우

**부작용**

없음

**참고 항목**

없음

### MC_termResGetFormat

**프로토타입**

```c
M_Int32 MC_termResGetFormat(M_Char* resGroupName, M_Char* resName,
M_Char* rtnFormat, M_Int32 rtnFormatSize)
```

**설명**

지정한 리소스의 MIME 타입 문자열을 반환한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `resName` - [in] 리소스 이름
- `rtnFormat` - [out] MIME 타입 문자열
- `rtnFormatSize` - [in] rtnFormat 버퍼 크기

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_SHORTBUF` - 반환되는 문자열보다 전달한 버퍼 크기가 작을때 발생
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹 혹은 존재하지 않는 리소스가 전달된 경우
- `M_E_NOTSUPPORTTYPE` - MIME 타입이 없는 리소스

**부작용**

없음

**참고 항목**

없음

### MC_termResGetSize

**프로토타입**

```c
M_Int32 MC_termResGetSize(M_Char* resGroupName, M_Char* resName)
```

**설명**

지정한 리소스의 데이터 크기를 반환한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `resName` - [in] 리소스 이름

**반환 값**

성공

리소스 크기
실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹 혹은 존재하지 않는 리소스가 전달된 경우

**부작용**

없음

**참고 항목**

MC_termResRead를 호출해서 리소스를 읽어올 때 필요한 버퍼를 할당하기 위해서 사용된다.

### MC_termResGetUIName

**프로토타입**

```c
M_Int32 MC_termResGetUIName(M_Char* resGroupName, M_Char* resName,
M_Char* uiName, M_Int32 uiNameSize)
```

**설명**

지정한 리소스의 UI 이름을 반환한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `resName` - [in] 리소스 이름
- `uiName` - [out] UI 상에 나타나는 이름
- `uiNameSize` - [in] uiName 버퍼 크기

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_SHORTBUF` - 반환되는 문자열보다 전달한 버퍼 크기가 작을때 발생
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹 혹은 존재하지 않는 리소스가 전달된 경우 (`M_E_NOTSUP` 보다 우선 처리됨)
- `M_E_NOTSUP` - UI 이름을 지원하지 않는 리소스 그룹일 경우

**부작용**

없음

**참고 항목**

없음

### MC_termResExists

**프로토타입**

```c
M_Int32 MC_termResExists(M_Char* resGroupName, M_Char* resName)
```

**설명**

지정한 리소스 이름의 리소스가 있는지 확인한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `resName` - [in] 리소스 이름

**반환 값**

성공

`MC_TERMRES_NAME_EXISTENT` 해당 리소스 그룹에 해당 리소스 이름의 리소 스가 있음. `MC_TERMRES_NAME_NONEXISTENT` 해당 리소스 그룹에 해당 리소스 이름의 리소 스가 없음.
실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹이 전달된 경우

**부작용**

없음

### MC_termResRead

**프로토타입**

```c
M_Int32 MC_termResRead (M_Char* resGroupName, M_Char* resName,
M_Byte* pData, M_Int32 bufSize)
```

**설명**

지정한 리소스의 데이터를 반환한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `resName` - [in] 리소스 이름
- `pData` - [out] 리소스 데이터
- `bufSize` - [in] pData 버퍼 크기

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_SHORTBUF` - 반환되는 데이터보다 전달한 버퍼크기가 작을때 발생
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹 혹은 존재하지 않는 리소스가 전달된 경우
- `M_E_ACCESSDENY` - 사용자가 읽기 권한이 없는 리소스일 경우

**부작용**

없음

**참고 항목**

pData는 `MC_termResGetSize`()를 통해 얻어온 리소스의 크기만큼 Caller가 할 당한다.

### MC_termResWrite

**프로토타입**

```c
M_Int32 MC_termResWrite (M_Char* resGroupName, M_Char* resName,
M_Int32 nameSize, M_Char* uiName, M_Char* resFormat, M_Byte* pData,
M_Int32 bufSize, M_Int32 mode)
```

**설명**

지정한 리소스 그룹에 리소스를 기록/갱신한다. 기록의 경우 새로 생성된 리소스 이 름을 반환하며, UI 이름을 주지 않으면 OEM에서 임의로 부여할 수 있다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `resName` - [in/out] 새로 생성되거나 기존에 존재하는 리소스 이름
- `nameSize` - [in] resName 버퍼 크기
- `uiName` - [in] UI 상에 나타나는 이름
- `resFormat` - [in] 리소스의 MIME 타입
- `pData` - [in] 리소스 데이터
- `bufSize` - [in] pData 버퍼 크기
- `mode` - [in] 쓰기 모드 `MC_TERMRES_CREATE` 리소스를 새로 생성한다. 이 경우 resName은 새로 생성된 리소스 이름이 반환된다. resName은 Unique 한 값으로 MC_TERMRES_CREATE로 반환된 resName은 변할 수 없다. `MC_TERMRES_UPDATE` 기존 리소스에 덮어 쓴다. 이 경우 resName에 덮어 쓸 리소스 이름을 넣어준다.

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_INSUFSPACE` - 리소스 저장 공간 부족
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹 혹은 존재하지 않는 리소스(UPDATE 모드인 경우)가 전달된 경우
- `M_E_ACCESSDENY` - 사용자가 쓰기 권한이나 업데이트 권한이 없 는 리소스일 경우
- `M_E_NOTSUP` - 쓰기 기능이나 갱신 기능을 지원하지 않는 리 소스 그룹 또는 리소스인 경우
- `M_E_INVALIDDATA` - 데이터가 해당 데이터 포맷에 맞지 않음
- `M_E_SHORTBUF` - resName이 출력일 때 버퍼 크기가 작은 경우
- `M_E_MAXCOUNT` - 리소스 그룹에서 지원하는 최대 개수를 초과한 경우

**부작용**

`MC_TERMRES_CREATE` 모드시, OEM에서 UI이름에 대한 특별한 규칙이 있 거나 UI이름이 없는 리소스 그룹의 경우, 인자로 넘겨준 UI이름은 무시될 수 있다. `MC_TERMRES_UPDATE` 모드시, 리소스 그룹 이름, 리소스 이름, MIME 타입 이 존재하는 리소스의 정보와 모두 일치하는 경우에 함수가 동작하며 기존 데이터는 새로운 데이터로 업데이트된다. 단, PHONEBOOK/GROUP의 경우 UI 이름과 리소스 이름, 데이터명이 동일해 야 하므로 `MC_TERMRES_UPDATE` 모드를 지원하지 않는다. 또한, `MC_TERMRES_UPDATE` 모드 수행 시, 업데이트 하고자 하는 부분의 데이터만 넣을 경우, 다른 데이터들은 삭제된다. 예로 PHONEBOOK/PRIVATE의 경 우 특정 필드의 값을 업데이트 하고자 필드값만 넣고 수행 시, 데이터를 넣지 않은 다른 필드들은 모두 삭제된다. UI이름을 지원하는 리소스 그룹일 경우 UI이름을 지정해야 하며, 그렇지 않을 경우 에러(`M_E_INVALID`)가 반환된다.

**참고 항목**

PHONEBOOK/SHORTKEY와 PHONEBOOK/GROUP은 UI 이름과 리소스 이 름이 같아야 한다. PHONEBOOK/SHORTKEY그룹의 리소스는 UI이름을 단축번호로 사용한다. 따라서 PHONEBOOK/SHORTKEY그룹의 리소스는 UI이름과 리소스 이름이 일치하여야 하 며, UI이름을 이용하여 단축번호를 지정할 수 있다.

### MC_termResDelete

**프로토타입**

```c
M_Int32 MC_termResDelete (M_Char* resGroupName, M_Char* resName)
```

**설명**

지정한 리소스를 삭제한다. 단 리소스의 삭제를 허용하지 않는그룹은 MC_KnlGetSystemProperty함수의 “NOTDELGROUP”을 통해, 삭제가 불가능한 리 소스에 대해서는 MC_termResGetGroupInfo함수의 infotype “IRREMOVABLE”을 통 해 확일할 수 있다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `resName` - [in] 리소스 이름

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹 혹은 존재하지 않는 리소스가 전달된 경우
- `M_E_ACCESSDENY` - 사용자가 접근 권한이 없는 리소스일 경우
- `M_E_NOTSUP` - 삭제 기능을 지원하지 않는 리소스 그룹 또는 리소스인 경우
- `M_E_NODELETE` - 삭제 기능을 지원하나 현재 리소스 그룹이 리소스의 상태가 삭제 불가능한 상태일 경 우(예: 리소스가 현재 사용 중인 경우)

**부작용**

없음

**참고 항목**

없음

### MC_termResRegister

**프로토타입**

```c
M_Int32 MC_termResRegister (M_Char* resGroupName, M_Char* resName,
M_Char* szStatus)
```

**설명**

지정한 리소스를 단말 특정 상태에 설정한다. `MC_knlGetSystemProperty`(“)를 통하여 단말에서 허용하는 상태에 대해서 조회 할 수 있다. ("REGISTRABLESTATUS_IDLE", "REGISTRABLESTATUS_INCOMING", "REGISTRABLESTATUS_POWERON", "REGISTRABLESTATUS_POWEROFF", "REGISTRABLESTATUS_BROWSERON", "“REGISTRABLESTATUS_BROWSEROFF")

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `resName` - [in] 리소스 이름
- `szStatus` - [in] 단말 특정 상태 “IDLE” 대기 “INCOMING” 전화 수신 “POWERON” 단말 구동 “POWEROFF” 단말 종료 “BROWSERON” 브라우저 구동 “BROWSEROFF” 브라우저 종료

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹 혹은 존재하지 않는 리소스가 전달된 경우
- `M_E_ACCESSDENY` - 사용자가 설정 권한이 없는 경우
- `M_E_INVALIDSTATUS` - 리소스와 단말 특정 상태가 연관이 없는 경우
- `M_E_NOTSUP` - Register 기능을 지원하지 않는 리소스 그룹

**부작용**

없음

**참고 항목**

없음

### MC_termResGetRegisteredInfo

**프로토타입**

```c
M_Int32 MC_termResGetRegisteredInfo (M_Byte* resList, M_Int32 bufSize,
M_Char* szStatus)
```

**설명**

단말 특정 상태에 설정된 리소스 그룹 이름과 리소스 이름을 반환한다.

**매개 변수**

- `resList` - [out] 리소스 그룹과 리소스 이름의 리스트 리소스 그룹 이름, “;”, 리소스 이름 순으로 구성된다. 리소스가 두개일 경우 다음의 리소스 그룹이름과 리소스 이름의 구별은 단말 리소스 개요의 리스트 형식을 따른다) 예) “MUSICBELL;mymusicbell\0\0” “MUSICBELL;mymusicbell\0PICTUREMATE;mypicture\0\0”
- `bufSize` - [in] resList 버퍼 크기
- `szStatus` - [in] 단말 특정 상태 “IDLE” 대기화면 “INCOMING” 전화 수신 화면 “POWERON” 단말 구동 화면 “POWEROFF” 단말 종료 화면 “BROWSERON” 브라우져 구동시 “BROWSEROFF” 브라우져 종료시

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_INVALID` - 전달한 매개변수가 NULL인 경우
- `M_E_ACCESSDENY` - 사용자가 설정 권한이 없는 경우
- `M_E_NORES` - 특정 상태에 설정된 리소스가 없을 경우
- `M_E_SHORTBUF` - resList 버퍼 크기가 작을 경우

**부작용**

없음

**참고 항목**

단말 특정 상태에 설정된 리소스는 최대 2개이다.

### MC_termResGetGroupLockState

**프로토타입**

```c
M_Int32 MC_termResGetGroupLockState (M_Char* resGroupName)
```

**설명**

지정한 리소스 그룹의 Lock 상태를 반환한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름

**반환 값**

성공

`MC_TERMRES_GROUP_LOCK` 해당 리소스 그룹이 그룹 Lock 설정 되어 있 음. `MC_TERMRES_GROUP_UNLOCK` 해당 리소스 그룹이 그룹 Lock 설정 안되어 있음.
실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_NOTSUPPORTLOCK` - 해당 리소스 그룹/리소스가 Lock 설정을 지원하지 않 음
- `M_E_NOTSUPPORTGLOCK` - 해당 리소스 그룹이 그룹 Lock은 지원하지 않음 (개 별 Lock은 지원함)
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹이 전달된 경우

**부작용**

없음

**참고 항목**

없음

### MC_termResGetLockState

**프로토타입**

```c
M_Int32 MC_termResGetLockState (M_Char* resGroupName, M_Char* resName)
```

**설명**

지정한 리소스의 Lock상태를 반환한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `resName` - [in] 리소스 이름

**반환 값**

성공

`MC_TERMRES_PRIVATE_LOCK` 해당 리소스가 개별 Lock 설정 되어 있음. `MC_TERMRES_PRIVATE_UNLOCK` 해당 리소스가 개별 Lock 설정 안되어 있음.
실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_NOTSUPPORTLOCK` - 해당 리소스 그룹/리소스가 Lock 설정을 지원하지 않 음
- `M_E_NOTSUPPORTPLOCK` - 해당 리소스 그룹이 개별 Lock은 지 원 하지 않음 (그룹 Lock은 지원함)
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹 혹은 존재하지 않는 리소스가 전달된 경우

**부작용**

없음

**참고 항목**

없음

### MC_termResSetGroupLockState

**프로토타입**

```c
M_Int32 MC_termResSetGroupLockState(M_Char* resGroupName, M_Int32 state)
```

**설명**

지정한 리소스 그룹의 Lock 상태를 설정한다. `MC_knlGetSystemProperty`(“SUPPORTGLOCK”) 를 통하여 그룹 Lock을 지원하는 단 말 리소스 그룹에 대해 조회 할 수 있다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `state` - [in] 그룹 Lock 설정/해제 `MC_TERMRES_GROUP_LOCK` 그룹 Lock 설정 `MC_TERMRES_GROUP_UNLOCK` 그룹 Lock 해제

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_NOTSUPPORTLOCK` - 해당 리소스 그룹/리소스가 Lock 설정을 지원하지 않 음
- `M_E_NOTSUPPORTGLOCK` - 해당 리소스 그룹이 그룹 Lock은 지원하지 않음 (개 별 Lock은 지원함)
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹이 전달된 경우

**부작용**

없음

**참고 항목**

MC_termResCheckPassword를 이용해 비밀번호를 확인한 후 사용한다.

### MC_termResSetLockState

**프로토타입**

```c
M_Int32 MC_termResSetLockState(M_Char* resGroupName, M_Char* resName, M_Int32 state)
```

**설명**

지정한 리소스의 Lock 상태를 설정한다. `MC_knlGetSystemProperty`(“SUPPORTPLOCK”) 를 통하여 개별 리소스 Lock을 지원 하는 단말 리소스 그룹에 대해 조회 할 수 있다

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `resName` - [in] 리소스 이름
- `state` - [in] 개별 Lock 설정/해제 `MC_TERMRES_PRIVATE_LOCK` 개별 Lock 설정 `MC_TERMRES_PRIVATE_UNLOCK` 개별 Lock 해제

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_NOTSUPPORTLOCK` - 해당 리소스 그룹/리소스가 Lock 설정을 지원하지 않 음
- `M_E_NOTSUPPORTPLOCK` - 해당 리소스 그룹이 개별 Lock은 지원하지 않음 (그 룹 Lock은 지원함)
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹 혹은 존재하지 않는 리소스가 전달된 경우

**부작용**

없음

**참고 항목**

MC_termResCheckPassword를 이용해 비밀번호를 확인한 후 사용한다.

### MC_termResCheckPassword

**프로토타입**

```c
M_Int32 MC_termResCheckPassword(M_Char* szPassword)
```

**설명**

지정한 비밀번호가 단말에 설정된 비밀번호와 일치하는지 확인한다.

**매개 변수**

- `szPassword` - [in] 비밀번호

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_INCORRECTPASSWORD` - 비밀번호 불일치일 경우
- `M_E_INVALID` - 전달한 매개변수가 NULL인 경우

**부작용**

없음

**참고 항목**

없음

### MC_termResGetFreeSpace

**프로토타입**

```c
M_Int32 MC_termResGetFreeSpace(void)
```

**설명**

단말 리소스를 향후 최대 얼마나 저장할 수 잇는지에 대해서 저장 공간의 남은 크기 를 byte 단위로 반환한다. 리소스 그룹 별로 나누어 반환하는 것이 아닌 그룹들이 사 용 가능한 총 공간을 반환한다. 그룹별 저장 공간의 남은 크기를 알기 위해서는 `MC_terResGetGroupInfo` 함수의 infoType “FREESPACE”를 전체 가용 공간의 크기를 알기 위해서는 “TOTALSPACE”를 사용한다.

**매개 변수**

없음

**반환 값**

성공

단말 리소스 저장 공간의 남은 크기
실패

- `M_E_ERROR` - 알 수 없는 이유로 실패

### MC_termResGetGroupInfo

**프로토타입**

```c
M_Int32 MC_termResGetGroupInfo(M_Char* resGroupName, M_Char* infoType, M_Byte* infoData, M_Int32 bufSize)
```

**설명**

지정한 리소스 그룹에 대하여 지정한 그룹 정보 타입의 그룹 정보를 반환한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름
- `infoType` - [in] 그룹 정보 타입. (아래 참고 항목에 정의)
- `infoData` - [out] 그룹 정보
- `bufSize` - [in] infoData 버퍼 크기

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹이 전달된 경우
- `M_E_SHORTBUF` - 그룹 정보 버퍼 크기가 작을 경우
- `M_E_NOTSUPPORTTYPE` - 해당 그룹은 지정한 그룹 정보 타입의 그룹 정보를 지원하지 않음
- `M_E_NOENT` - 지정한 그룹 정보 타입의 그룹 정보가 없음

**부작용**

다음의 참고 항목에 정의된 infoType에 해당하는 리소스 그룹만 resGroupName으로 지정 가능하다.

**참고 항목**

„+‟ : 앞뒤 문자열/문자를 strcat 하는 연산을 의미한다. 리소스 그룹 infoType 비고 모든 그룹 “MAXUINAMESI 지정한 리소스그룹에서 UI이름의 최대 저장 가능한 ZE” 길이를 문자열로 반환한다. "FREESPACE" 지정한 리소스 그룹에서 사용 가능한 남은 공간의 크기를 byte단위로 반환한다. 단, EFS를 사용하지 않는 그룹 중에서 본 infoType을 반환받고자 할 경 우 M_E_NOTSUP을 반환한다. "TOTALSPACE" 지정한 리소스 그룹이 사용할 수 있는 전체 가용 공 간의 크기를 바이트 단위의 문자열로 반환한다. “IRREMOVABLE 삭제가 불가능한 리소스 리스트를 반환한다. 반환 ” 형식은 Terminal Resource 모듈 포팅의 ‘리스트 형 식’을 따른다. 삭제 불가능한 리소스가 없을 경우 에러(`M_E_NOENT`)가 반환된다. PHONEBOOK/PRIV “MAXCOUNT” 지정한 리소스 그룹의 최대 저장 가능한 리소스 수 ATE 를 문자열로 반환한다. PHONEBOOK/GRO UP SMSDATA/SENT SMSDATA/RECV BLACKLIST PHONEBOOK/SHO “RANGE” 단말기가 지원하는 단축번호의 시작 번호와 마지막 RTKEY 번호를 문자열로 반환한다. 반환 형식은 3.9.1을 따 르며, 시작 번호와 마지막 번호 순으로 반환한다. 예1)“1\0100\0\0” (1번부터 100번까지의 번호를 단축번호로 사용할 수 있는 단말기) 예2)”0\0200\0\0” (0번부터 200번까지의 번호를 단축번호로 사용할 수 있는 단말기) „PHONEBOOK/PRI “MAXTELCOUN 단말에 저장 가능한 최대 전화번호 수를 문자열로 VATE T” 반환한다. “TYPELIST” 단말이 지원하는 wCard Type의 리스트를 반환한다. 반환 형식은 Terminal Resource 모듈 포팅의 „리스 트 형식‟을 따른다. “TYPECOUNT” 단말이 지원하는 wCard Type 수를 반환한다. “TYPEINFO” + wCard의 Type name에 해당하는 wCard Type의 정 „/‟ + <Type 보를 반환한다. name> 반환 형식은 다음과 같은 문자열 형태이다.. <저장 가능한 Value의 길이> + „/‟ + <하나의 폰북개인에 저장 가능한 해당 Type의 개수 ex) > “TYPEINFO/N” [+ „/‟ + <Type parameter> + „:‟ < 하나의 폰북개인 “TYPEINFO/TEL 에 저장 가능한 해당 Type parameter의 개수> ] ” 사용예는 다음에 있다. PHONEBOOK/PRIV “X-MDAYINFO” 단말의 기념일 관련 정보를 얻어온다. ATE 반환 형식은 다음과 같은 문자열 형태이다.. <기념일> + ‘/’ + <기념일 종류의 고정 여부> (+ ‘/’ + <가변일 경우 최대 길이>) (+ “/NOLEAF”) <기념일> : YYYYMMDD 또는 MMDD <기념일 종류의 고정 여부> : FIXED 또는 VARIABLE <가변일 경우 최대 길이> : 기념일 종류를 나타내는 Type parameter의 ASCII CHAR 기준 입력 가능한 최대 길이 “/NOLEAF” : 음력에서 윤달 입력이 안되는 단말일 경우 wCard 참조. 예1) 단말이 기념일에 연도를 지원하며, 기념일 종 류가 정해져 있는 경우. 음력이 지원될 경우 윤달 지원함. “YYYYMMDD/FIXED” 예2) 단말이 기념일에 연도를 지원하며, 기념일 종 류가 정해져 있는 경우. 음력 지원하나 윤달 지원 안함. “YYYYMMDD/FIXED/NOLEAF” 예3) 단말이 기념일에 연도를 지원하지 않으며, 기 념일 종류를 사용자가 직접 입력하는 경우 최대 입 력 길이가 6인 경우. “MMDD/VARIABLE/6” X-MDAY를 지원하지 않는 단말은 에러 (`M_E_NOENT`)를 반환한다. “TYPEINFO” 예 예1) “TYPEINFO/N”을 infoType으로 하여 “10/1”반환 „N‟ Type에 저장가능한 Value의 길이는 ASCII CHAR 기준 10자 „N‟ Type은 하나의 폰북개인에 1개 저장 가능 „N‟ Type에는 Type parameter가 없다. 예2) “TYPEINFO/TEL”을 infoType으로 하여 “15/4/cell:4/work:4/home:4” 반환 „TEL‟ Type에 저장가능한 Value의 길이는 ASCII CHAR 기준 15자 „TEL‟ Type은 하나의 폰북개인에 4개 저장 가능 „TEL‟ Type에는 cell, work, home 3개의 Type parameter가 있다. Type parameter cell, work, home은 하나의 폰북개인에 각각 4개씩 저장 가능. 설명 : 하나의 폰북개인에 집전화, 회사전화, 휴대전화 번호를 통틀어 4개 저 장할 수 있다. 4개 모두를 집전화번호로 설정할 수도 있으며, 4개 모두를 회사전화번 호 또는 휴대전화번호로도 설정할 수 있다. 예3) “TYPEINFO/X-MDAY”를 infoType으로 하여 “10/4/birthday:1/wedding:1/meeting:1/memorial:1/sun:4/moon:4” 반환 „X-MDAY‟ Type에 저장가능한 Value의 길이는 ASCII CHAR 기준 10자 „X-MDAY‟ Type은 하나의 폰북개인에 4개 저장 가능 „X-MDAY‟ Type에는 birthday, wedding, meeting, memorial, sun, moon 6개의 Type parameter가 있다. Type parameter birthday, wedding, meeting, memorial은 하나의 폰북개인에 각 각 1개씩 저장 가능. Type parameter sun, moon은 하나의 폰북개인에 각각 4개씩 저장 가능. 설명 : 하나의 폰북개인에 기념일은 모두 4개 저장할 수 있으며, 생일, 결혼기 념일, 만남, 기념은 각각 하나씩 저장할 수 있다. 따라서 생일, 결혼기념일, 만남, 기 념을 각각 하나씩 저장하여 4개의 기념일을 저장하게 된다. 4개의 기념일 모두 양력 으로 저장하거나 음력으로 저장할 수 있다.

### MC_termResGetInfo

**프로토타입**

```c
M_Int32 MC_termResGetInfo(M_Char* resGroupName, M_Char* resName,
M_Char* infoType, M_Byte* infoData, M_Int32 bufSize)
```

**설명**

지정한 리소스에 대하여 지정한 리소스 정보 타입의 리소스 정보를 반환한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름.
- `resName` - [in] 리소스 이름.
- `infoType` - [in] 리소스 정보 타입. (아래 참고 항목에 정의)
- `infoData` - [out] 리소스 정보.
- `bufSize` - [in] infoData 버퍼 크기

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹 혹은 존재하지 않는 리소스가 전달된 경우
- `M_E_SHORTBUF` - 리소스 정보 버퍼 크기가 작을 경우
- `M_E_NOTSUPPORTTYPE` - 해당 리소스는 지정한 리소스 정보 타입의 리소스정보 를 지원하지 않음
- `M_E_NOENT` - 해당 리소스에, 지정한 리소스 정보 타입의 리소스 정보 가 없음.

**부작용**

다음의 참고 항목에 정의된 리소스 포맷에 해당하는 리소스만 지정 가능하다.

**참고 항목**

„+‟ : 앞뒤 문자열/문자를 strcat 하는 연산을 의미한다. 리소스 포맷은 단말 리소스 개요의 „ MIME 타입 및 리소스 데이터 포맷‟을 따 른다. 리소스 포맷 infoType 비고 이미지 포맷 “WIDTH” 지정한 리소스에 width 정보가 있는 경우 이 Animation 포맷 를 문자열로 반환한다. 단위는 pixel이다. 동영상 포맷 “HEIGHT” 지정한 리소스에 height 정보가 있는 경우 이를 문자열로 반환한다. 단위는 pixel이다. 동영상 포맷 “RUNTIME” 지정한 리소스에 running time 정보가 있는 사운드 포맷 경우 이를 문자열로 반환한다. 단위는 ms이 다. “BITRATE” 지정한 리소스에 bit rate 정보가 있는 경우 이를 문자열로 반환한다. 단위는 bps(bit per sec)이다. 동영상 포맷 “FRAMERATE” 지정한 리소스에 frame rate 정보가 있는 경 우 이를 문자열로 반환한다. 단위는 fps(frame per sec)이다. phonebook/group 포 “PRIVATECOU 지정한 폰북그룹에 포함된 폰북개인 수를 문 맷 NT” 자열로 반환한다. 폰북개인이 없는 폰북그룹 은 숫자 0이 반환된다. “PRIVATELIST” 지정한 폰북그룹에 포함된 폰북개인의 리소 스 이름 리스트를 반환한다. 반환 형식은 단 말 리소스 개요의 리스트 형식을 따른다. 폰 북개인이 없는 폰북그룹은 에러 (`M_E_NOENT`)가 반환된다.

### MC_termResSearch

**프로토타입**

```c
M_Int32 MC_termResSearch (M_Char* resGroupName, M_Char* queryType,
M_Char* queryName, M_Byte* resNames, M_Int32 bufSize, M_Int32 mode)
```

**설명**

리소스 그룹과 검색어 타입에 따라, 주어진 문자열 검색어와 일치하는 리소스를 검 색한다. 검색 결과로 리소스 이름 리스트를 반환한다.

**매개 변수**

- `resGroupName` - [in] 리소스 그룹 이름.
- `queryType` - [in] 검색어 타입. (아래 참고 항목에 정의)
- `queryName` - [in] 문자열 검색어.
- `resNames` - [out] 리소스 이름 리스트. (개요 문서의 “리스트 형식”을 따른다.)
- `bufSize` - [in] resNames 버퍼 크기
- `mode` - [in] 검색 모드. `MC_TERMRES_EXTSRCH` queryName 문자열과 정확히 일치하는지를 검색 `MC_TERMRES_INCSRCH` queryName 문자열을 포함하는지를 검색

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_SHORTBUF` - 반환되는 문자열보다 전달한 버퍼 크기가 작을때 발생
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹이 전달된 경우
- `M_E_NOTSUPPORTTYPE` - 해당 리소스 그룹은 지정한 queryType을 지원 하지않음.
- `M_E_NOTFOUND` - 검색 결과 리소스가 없음

**부작용**

다음의 참고 항목에 정의된 queryType에 해당하는 리소스 그룹만 resGroupName으로 지정 가능하다.

**참고 항목**

리소스 그룹 queryType 비고 모든 리소스 그룹 “UINAME” 지정한 리소스 그룹에서 queryName 문자 열을 가진 UI 이름의 리소스 검색 (UI이름 을 지원하지 않는 리소스 그룹이 있을 수 있음) PHONEBOOK/PRIVATE “NUMBER” 전화번호 검색 : 전화번호에 queryName 문자열을 가진 폰북개인 검색

### MC_termResExecuteCmd

**프로토타입**

```c
M_Int32 MC_termResExecuteCmd(M_Char* resGroupName, M_Char* cmd,
void* param1, void* param2)
```

**설명**

지정한 명령에 따라 서비스를 요청한다.

**매개 변수**

- `resGroupName` - [in] 명령을 실행시킬 리소스 그룹 이름
- `cmd` - [in] 서비스 받고자하는 명령
- `param1` - [in/out] 서비스에 대한 인자/반환값
- `param2` - [in/out] 서비스에 대한 인자/반환값

**반환 값**

성공

실패

- `M_E_ERROR` - 알 수 없는 이유로 실패
- `M_E_INVALID` - 전달한 매개변수가 NULL이거나 단말에서 지 원하지 않는 리소스 그룹이 전달된 경우
- `M_E_NOTSUP` - 지원되지 않는 명령 기타 각각의 명령에 따라 정의
