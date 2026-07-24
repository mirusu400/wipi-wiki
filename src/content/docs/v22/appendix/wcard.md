---
title: "5. wCard"
---

wCard는 vCard 3.0을 기반으로, vCard 3.0 규격에 없으나 단말 환경에 필요한 부분을 추가한 규격이다. 본 규격에서는 vCard 3.0 규격에 대한 개략적인 설명과 wCard 규격을 정의한다.

## 5.1. 관련규격

wCard 규격은 다음의 규격들을 근간으로 하며, 아래 문서의 내용 중 본 요구사항과 상충되는 부분은 본 요구사항을 준수함을 원칙으로 한다. 본 요구사항에서 언급되지 않은 사항들은 다음의 규격 및 관련된 규격을 준수함을 원칙으로 한다. RFC 2425, MIME Conternt-Type for Directory Information RFC 2426, vCard MIME Directory Profile

## 5.2. vCard 3.0 규격 개요

vCard 포맷은 문자열로 이루어져 있다. 하나의 필드는 하나의 줄(행)에 <Type>과 <Value>의 쌍으로 구성되며, 필드와 필드는 줄바꿈(CRLF)으로 구분된다. <Type>은 데이터 종류를 의미하며, N (이름), NICKNAME (애칭), TEL (전화번호)와 같은 방식으 로 사용된다. <Value>는 <Type>에 해당하는 데이터로서, “N:김철수” (이름이 김철수인 경우), “NICKNAME:위피” (애칭이 위피인 경우), “TEL:0200001111” (전화번호가 02- 0000-1111인 경우)와 같이 사용된다. <Type> <Type>은 <Type Name>과 <Type Parameter>로 구성되며, „;‟로 구분된다. 예1) “TEL;TYPE=home:0200001111” (집전화번호가 02-0000-1111인 경우) 예2) “TEL;TYPE=work:0233334444” (회사전화번호가 02-3333-4444인 경우) <Type Parameter> 하나의 <Type Name>에 대하여 <Type Parameter>는 없을 수도 있고, 다수개가 존재 할 수도 있다. 만약 <Type Parameter>가 다수개 존재한다면 각각의 <Type Parameter>는 „,‟로 구분한다. <Type Parameter>들의 맨 앞에는 “TYPE=”을 붙인다. 예) “TEL;TYPE=work,cell:01100001111” (회사 이동전화 번호가 011-0000-1111인 경우) <Value> <Value>는 각 <Type>에 대한 데이터를 의미하며, 하나의 <Type>에 다수개의 <Value>가 존재할 수 있다. 만약 <Value>가 다수개 존재한다면 각각의 <Value>는 „;‟로 구분한다. 예1) “ORG:코리아텔레콤;제주연구소” (코리아텔레콤의 제주연구소에 근무할 경우) 하나의 <Type>에 다수개의 <Value>가 있을 경우, <Value>는 삭제해도 구분자인 „;‟ 는 삭제하면 안된다. 단, 마지막 <Value>인 경우 „;‟를 삭제해도 무방하다. 예2) ORG:;제주연구소” (코리아텔레콤의 제주연구소에 근무하면서 제주연구소만 표 기할 경우 - “제주연구소” 앞에 „;‟이 남아있음) 예3) ORG:코리아텔레콤” (코리아텔레콤의 제주연구소에 근무하면서 코리아텔레콤만 표기할 경우 - “코리아텔레콤” 뒤에 „;‟이 없음)

## 5.3. vCard 3.0 규격 예

<Type Name> 다음은 RFC2426에 정의된 <Type Name> 중 일부이다. <Type Name> 설 명 N 이름 NICKNAME 애칭 TEL 전화번호 EMAIL e-mail URL 홈페이지 ADR 주소 NOTE 메모 ROLE 직업 ORG 직장 PHOTO 사진 REV 수정정보 <Type Parameter> 다음은 RFC2426에 정의된 <Type Parameter> 중 일부이다. <Type Name> <Type Parameter> N NICKNAME TEL work(직장), home(집), cell(휴대전화), fax(팩스), pager(호출 기) EMAIL URL work(직장) ADR home(집), work(직장) NOTE ROLE ORG PHOTO REV 모든 Type pref(대표) Name 예1) “TEL;TYPE=pager:01212345678” (호출기 번호가 012-1234-5678인 경우) 예2) “TEL;TYPE=fax:0298765432” (팩스 번호가 02-9876-5432인 경우)

## 5.4. wCard 규격

wCard 규격은 vCard3.0을 기반으로 vCard 3.0 규격에 정의되지 않은 다음의 내용을 추가하여 사용한다

### 5.4.1. <Type> 추가

<Type Name> 설 명 X-MDAY 기념일 (생일, 결혼, 만남, 기념일)을 기록한다. “<Type Name>;<Type Parameter>-1,<Type Parameter>- 2:<Value>”의 형식을 따르며, 문자 사이에 공백은 없다. <Type Parameter> 설 명 birthday 생일 wedding 결혼 meeting 만남 memorial 기념일 sun 양력 moon 음력 <Type Parameter>-1은 birthday, wedding, meeting, memorial 넷 중 하나이다. <Type Parameter>-2는 sun과 moon 둘 중 하나이다. 예를 들어 “memorial,sun”, “wedding,moon”와 같이 사용된다. <Value>는 기념일의 날짜이다. 기념일에 연도를 지원하는 단말의 경우 날짜는 연월일 8자리 (YYYYMMDD)이다. 예를 들어 “20030101”, “20031231”와 같이 사용된다. 기념일에 연도를 지원하지 않는 단말의 경우 날짜는 월일 4자 리 (MMDD)이다. 예를 들어 “1231”와 같이 사용된다. <Type parameter>가 moon일 경우 날짜끝에 'L'을 추가하면 해 당 달이 윤달임을 나타낸다. 예1) “X-MDAY;TYPE=wedding,sun:19960415” (결혼 기념일이 양 력으로 1996년 4월 15일인 경우 예2) “X-MDAY;TYPE=meeting,moon:20040213” (만남 기념일이 음력으로 2004년 02월 13일인 경우) 예3) “X-MDAY;TYPE=meeting,moon:20040213L” (만남 기념일이 음력으로 2004년 윤02월 13일인 경우) 예4) “X-MDAY;TYPE=meeting,moon:1102” (만남 기념일이 음력 으로 11월 02일인 경우, 기념일에 년도를 지원하지 않는 단말 일 경우) X-GROUP 폰북개인이 속해있는 폰북그룹의 리소스 이름을 기록한다. “<Type Name>:<Value>”의 형식을 따르며, 문자 사이에 공백은 없다. 하나의 X-GROUP Type에는 하나의 Value만 존재한다. 예) “X-GROUP:친구”, “X-GROUP:학교”, “X-GROUP:동창” X-GROUP이 없을 경우 단말의 디폴트 폰북그룹으로 설정한다. (예: "지정안됨"등과 같은 폰북그룹) 폰북그룹을 삭제할 경우 삭제할 폰북그룹에 속해있던 모든 폰 북개인들은 디폴트 폰북그룹(예: "지정안됨"등과 같은 폰북그룹) 으로 설정된다.

### 5.4.2. <Type Parameter> 추가

<Type Name> : PHOTO <Type Parameter> 설 명 termres 폰북개인에 단말리소스 사진을 설정한다. “<Type Name>;<Type Parameter>:<Value>-1;<Value>-2”의 형식을 따르며, 문자 사이에 공백은 없다. <Value>-1은 사진의 리소스 그룹 이름이며 , <Value>-2는 리소스 이름이다. 예1)“PHOTO;TYPE=termres:PICTUREMATE;mypicture” (PICTUREMATE 의 mypicture를 사진으로 설정한 경우) 예2)“PHOTO;TYPE=termres:PHOTO;myphoto” (PHOTO의 myphoto를 사진으로 설정한 경우) <Type Name> : TEL <Type Parameter> 설 명 etc 기타전화번호 예) 기타전화번호 02-1234-5678 “TEL;TYPE=etc:0212345678”

### 5.4.3. <Value> 사용 방식

<Type Name> <Value> N “성;이름” 예1) “N:김;철수” (이름이 김철수인 경우) 예2) “N:채;시라” (이름이 채시라인 경우) 예3) “N:김;혜수” (이름이 김혜수인 경우) “전체이름” (성+이름) 예1) “N:김철수” (이름이 김철수인 경우) 예2) “N:채시라” (이름이 채시라인 경우) 예3) “N:김혜수” (이름이 김혜수인 경우) ADR “;;주소;구/군/시;시/도;우편번호” 예1) 집주소가 서울 관악구 봉천동 WIPI 연구소 (우:123-456) 인 경우 “ADR;TYPE=home:;;봉천동 WIPI 연구소;관악구;서울;123-456” 예2) 직장 주소가 경기도 성남시 분당구 WIPI 연구소 (우:000- 111) 인 경우 “ADR;TYPE=work:;;분당구 WIPI 연구소;성남시;경기도;000-111” “ADR;TYPE=work:;;성남시 분당구 WIPI 연구소;;경기도;000- 111” “ADR;TYPE=work:;;경기도 성남시 분당구 WIPI 연구소;;;000- 111” “ADR;TYPE=work:;;경기도 성남시 분당구 WIPI 연구소” (우편 번호 미표기시) ORG “회사;부서” 예) 코리아텔레콤의 제주연구소에 근무할 경우 “ORG:코리아텔레콤;제주연구소” (회사 부서 모두 쓸 경우) “ORG:코리아텔레콤” (회사만 쓸 경우) “ORG:;제주연구소” (부서만 쓸 경우) PHOTO “리소스그룹이름;리소스이름” (<Type Parameter> : termres) 예) PHOTO 그룹에 myphoto 리소스를 지정할 경우 “PHOTO;TYPE=termres:PHOTO;myphoto”

### 5.4.4. 기타 설정

“pref” 사용 “pref” <Type parameter> 는 모든 <Type Name>에 사용이 가능하다. 같은 <Type Name>이 복수개 존재할 경우, 같은 <Type Name> 중 최소한 하나에는 “pref” <Type parameter>가 정의되어 있어야 한다. 같은 <Type Name>이 복수개 존재할 경우, 같은 <Type Name> 중 단지 하나에만 “pref” <Type parameter>가 정의되어 있어야 한다. “pref”는 <Type parameter>들의 맨 앞에 위치해야 한다. 예1) TEL;TYPE=pref,work:01188880000 TEL;TYPE=home:01199991111 TEL;TYPE=cell:01112345678 예2) X-MDAY;TYPE=pref,birthday,moon:19700505 X-MDAY;TYPE=wedding,sun:20000101 전화번호는 „-„를 빼고 기록한다. 예1) 01100001111 (O) 예2) 011-0000-1111 (X) URL <Type Name>에 <Type Parameter> “work”는 항상 기록한다. 예) URL;TYPE=work:http://www.nate.com <Value>내용에 „:‟, „;‟, „\‟을 사용할 경우 Back Slash („\‟) 를 선행시킨다. 그러나 구분자로 쓰이는 „:‟와 „;‟에는 Back Slash („\‟) 를 선행시키지 않는 다. 예1) 애칭이 “나의별;명”일 경우 NICKNAME:나의별\;명 예2) 회사가 “코리아텔레콤”이고 부서가 “제주연:구소”일 경우 ORG:코리아텔레콤;제주연\:구소 예3) 회사가 “코리아텔레콤”이고 부서가 “제주연\구소”일 경우 ORG:코리아텔레콤;제주연\\구소 X-MDAY의 기념일 종류를 나타내는 <Type parameter>가 사용자가 직접입 력하는 가변 형태일 때 <Type parameter>에 „:‟, „;‟, „,‟, „\‟을 사용할 경우 Back Slash („\‟) 를 선행시킨다. 그러나 구분자로 쓰이는 „:‟와 „;‟에는 Back Slash („\‟) 를 선행시키지 않는다. 예1) <Type parameter>가 “여친;만난날”이고 1월 1일 양력일 경우 (년도를 지원하지 않는 단말 : MMDD일 경우) X-MDAY;Type=여친\;만난날,sun:0101 예2) <Type parameter>가 “여친:100일”이고 2000년 12월 12일 음력일 경우 (년도를 지원하는 단말 : YYYYMMDD일 경우) X-MDAY;Type=여친\:100일,moon:20001212 예2) <Type parameter>가 “여친\헤어짐”이고 2001년 8월 15일 음력일 경우 (년도를 지원하는 단말 : YYYYMMDD일 경우) X-MDAY;Type=여친\\헤어짐,moon:20010815 예3) <Type parameter>가 “여친,재회”이고 2001년 8월 15일 음력일 경우 (년도를 지 원하는 단말 : YYYYMMDD일 경우) X-MDAY;Type=여친\,재회,moon:20010815

#### REV

1. 폰북개인을 OEM에서 생성 및 수정할 경우, OEM에서 시간정보를 기록(수정)해야 한다. 2. WIPI 주소록 어플이 `MC_termResRead`, MH_termResRead로 폰북개인 데이터 요 구시, OEM은 wCard 포맷에 REV 타입으로 시간정보를 제공해야 한다. 3. 폰북개인을 WIPI 주소록 어플에서 생성 및 수정할 경우, OEM은 wCard REV 값으 로 시간정보를 기록(수정)하여야 한다. 4. WIPI 주소록 어플에서 폰북개인을 생성 및 수정할 경우 wCard에 REV 값이 없으 면 OEM은 `MC_termResWrite`, MH_termResWrite호출 시점을 기준으로 시간정보를 기록(수정)한다.

## 5.5. wCard 필수 항목

각 제조사마다 단말에서 지원하는 wCard의 Type Name이 상이하여, 어떤 단말에서 는 저장 성공하는 wCard 포맷이, 다른 단말에서는 저장 실패하는 경우가 발생할 수 있다. 이러한 문제를 방지하기 위해, wCard에 필수 항목을 지정하고, 이 필수 항목 에 대해서는 모든 단말에서 지원하도록 한다. 필수 항목 이외의 Type Name, Parameter에 대해서는 해당 단말에서 지원하지 않을 시, 무시하도록 한다.

#### 필수 항목

다음은 wCard에서 사용되는 Type Name, Parameter 중 필수 항목이다. <Type Name> <Parameter> 설 명 N 없음 이름 TEL work 네 개의 Parameter 중 하나는 반드시 있어야 home 함 cell Etc

## 5.6. wCard 규격 예

<Type Name> 다음은 wCard에서 사용될 수 있는 <Type Name> 예이다. <Type Name> 설 명 N 이름 NICKNAME 애칭 TEL 전화번호 EMAIL e-mail URL 홈페이지 ADR 주소 NOTE 메모 ROLE 직업 ORG 직장 X-MDAY 기념일 (vCard 3.0 에 없는 Type name으로, wCard에서 추가 됨) X-GROUP 폰북그룹(vCard 3.0 에 없는 Type name으로, wCard에서 추가 됨) PHOTO 사진 REV 수정정보 <Type Parameter> 다음은 wCard에서 사용될 수 있는 <Type Parameter> 예이다. <Type Name> <Type Parameter> N NICKNAME TEL work(직장), home(집), cell(휴대전화), fax(팩스), pager(호출 기), etc(기타) EMAIL URL work(직장) ADR home(집), work(직장) NOTE ROLE ORG X-MDAY birthday(생일), wedding(결혼), meeting(만남), memorial(기념 일), sun(양력), moon(음력) X-GROUP PHOTO termres(단말리소스) REV 모든 Type pref(대표) Name

## 5.7. wCard 예제

#### 예제 1

`MC_termResGetGroupInfo` 또는 MH_termResGetGroupInfo의 결과가 다음과 같을 때. `MC_termResGetGroupInfo` `MH_termResGetGroupInfo` infoType infoData “TYPELIST” “N\0NICKNAME\0TEL\0EMAIL\0URL\0ADR\0NOTE \0ROLE\0ORG\0X-MDAY\0X- GROUP\0PHOTO\0REV\0\0” “TYPEINFO/N” “10/1” “TYPEINFO/NI “10/1” CKNAME” “TYPEINFO/T “16/7/work:7/home:7/cell:7/fax:7/pager:7/etc:7” EL” “TYPEINFO/E “30/2” MAIL” “TYPEINFO/U “50/1” RL” “TYPEINFO/A “50/2/home:2/work:2” DR” “TYPEINFO/N “40/1” OTE” “TYPEINFO/R “20/1” OLE” “TYPEINFO/O “30/1” RG” “TYPEINFO/X- “4/4/birthday:4/wedding:4/meeting:4/memorial:4/sun:4/moon:4 MDAY” ” “TYPEINFO/X- “10/3” GROUP” “TYPEINFO/P “20/1/termres:1” HOTO” “TYPEINFO/R “16/1” EV” “X- “MMDD/FIXED” MDAYINFO” BEGIN:VCARD N:김;철수 NICKNAME:위피 TEL;TYPE=pref,work:0200001111 TEL;TYPE=work:0211110000 TEL;TYPE=home:0222223333 TEL;TYPE=cell:01112345678 TEL;TYPE=fax:0267896789 TEL;TYPE=pager:01203690369 TEL;TYPE=etc:0212345678 EMAIL;TYPE=pref:wipi@nate.com EMAIL:wipi-apps@nate.com URL;TYPE=work:http://www.nate.com ADR;TYPE=pref,home:;;봉천동 WIPI 연구소;관악구;서울;123-456 ADR;TYPE=work:;;분당구 WIPI 연구소;성남시;경기도;000-111 NOTE:wCard 예제입니다. ROLE:프로그래머 ORG:코리아텔레콤;제주연구소 X-MDAY;TYPE=pref,birthday,moon:0505 X-MDAY;TYPE=wedding,sun:0101 X-MDAY;TYPE=meeting,sun:1231 X-MDAY;TYPE=memorial,moon:0630 X-GROUP;TYPE=pref:친구 X-GROUP:학교 X-GROUP:동창 PHOTO;TYPE=termres:PHOTO;myphoto REV:20031009T180135Z END:VCARD 다음은 위의 wCard 예제에 대한 설명이다. 이름 : 김철수 (성:김, 이름:철수) 애칭 : 위피 전화번호(직장, 대표) : 02-0000-1111 전화번호(직장) : 02-1111-0000 전화번호(집) : 02-2222-3333 전화번호(휴대전화) : 011-1234-5678 전화번호(팩스) : 02-6789-6789 전화번호(호출기) : 012-0369-0369 전화번호(기타) : 02-1234-5678 이메일(대표) : wipi@nate.com 이메일 : wipi-apps@nate.com 홈페이지 : http://www.nate.com 주소(집, 대표) : 서울 관악구 봉천동 WIPI 연구소 (우:123-456) 주소(직장) : 경기도 성남시 분당구 WIPI 연구소 (우:000-111) 메모 : wCard 예제입니다. 직업 : 프로그래머 직장 : 코리아텔레콤(회사), 제주연구소(부서) 기념일(생일, 대표) : 05-05 (음) 기념일(결혼) : 01-01 (양) 기념일(만남) : 12-31 (양) 기념일(기념일) : 06-30 (음) 폰북그룹(대표) : 친구 폰북그룹 : 학교 폰북그룹 : 동창 수정일 : 2003년 10월 9일 18시 1분 35초 (GMT), 2003년 10월 10일 03시 1분 35초 (GMT + 09:00) 사진 : 단말 리소스 PHOTO 그룹의 myphoto

#### 예제 2

`MC_termResGetGroupInfo` 또는 MH_termResGetGroupInfo의 결과가 다음과 같을 때. `MC_termResGetGroupInfo` `MH_termResGetGroupInfo` infoType infoData “TYPELIST” “N\0TEL\0EMAIL\0NOTE\0X-MDAY\0X- GROUP\0REV\0\0” “TYPEINFO/N” “10/1” “TYPEINFO/T “16/4/work:1/home:1/fax:1/cell:1” EL” “TYPEINFO/E “30/1” MAIL” “TYPEINFO/N “40/1” OTE” “TYPEINFO/X- “8/2/sun:2/moon:2” MDAY” “TYPEINFO/X- “10/1” GROUP” “TYPEINFO/R “16/1” EV” “X- “YYYYMMDD/VARIABLE/10” MDAYINFO” BEGIN:VCARD N:김철수 TEL;TYPE=pref,work:0200001111 TEL;TYPE=home:0211110000 TEL;TYPE=fax:0222223333 TEL;TYPE=cell:01112345678 EMAIL:wipi@nate.com NOTE:wCard 예제입니다. X-MDAY;TYPE=pref,생일,moon:19700505 X-MDAY;TYPE=처음만난날,sun:20000101 X-GROUP:친구 REV:20031009T180135Z END:VCARD 다음은 위의 wCard 예제에 대한 설명이다. 이름 : 김철수 전화번호(직장, 대표) : 02-0000-1111 전화번호(집) : 02-1111-0000 전화번호(팩스) : 02-2222-3333 전화번호(휴대전화) : 011-1234-5678 이메일 : wipi@nate.com 메모 : wCard 예제입니다. 기념일(생일, 대표) : 1970-05-05 (음) 기념일(처음만난날) : 2000-01-01 (양) 폰북그룹 : 친구 수정일 : 2003년 10월 9일 18시 1분 35초 (GMT), 2003년 10월 10일 03시 1분 35초 (GMT + 09:00)

#### 예제 3

`MC_termResGetGroupInfo` 또는 MH_termResGetGroupInfo의 결과가 다음과 같을 때. `MC_termResGetGroupInfo` `MH_termResGetGroupInfo` infoType infoData “TYPELIST” “N\0TEL\0EMAIL\0NOTE\0X-MDAY\0X- GROUP\0REV\0\0” “TYPEINFO/N” “10/1” “TYPEINFO/T “16/4/work:1/home:1/fax:1/cell:1” EL” “TYPEINFO/E “30/1” MAIL” “TYPEINFO/N “40/1” OTE” “TYPEINFO/X- “8/2/birthday:2/wedding:2/meeting:2/memorial:2/sun:2/moon:2 MDAY” ” “TYPEINFO/X- “10/1” GROUP” “TYPEINFO/R “16/1” EV” “X- “YYYYMMDD/FIXED” MDAYINFO” BEGIN:VCARD N:김철수 TEL;TYPE=pref,work:0200001111 TEL;TYPE=home:0211110000 TEL;TYPE=fax:0222223333 TEL;TYPE=cell:01112345678 EMAIL:wipi@nate.com NOTE:wCard 예제입니다. X-MDAY;TYPE=pref,birthday,moon:19700505 X-MDAY;TYPE=wedding,sun:20000101 X-GROUP:친구 REV:20031009T180135Z END:VCARD 다음은 위의 wCard 예제에 대한 설명이다. 이름 : 김철수 전화번호(직장, 대표) : 02-0000-1111 전화번호(집) : 02-1111-0000 전화번호(팩스) : 02-2222-3333 전화번호(휴대전화) : 011-1234-5678 이메일 : wipi@nate.com 메모 : wCard 예제입니다. 기념일(생일, 대표) : 1970-05-05 (음) 기념일(결혼) : 2000-01-01 (양) 폰북그룹 : 친구 수정일 : 2003년 10월 9일 18시 1분 35초 (GMT), 2003년 10월 10일 03시 1분 35초 (GMT + 09:00) 표준작성 공헌자 표준 번호: TTAK.KO-06.0036/R6 이 표준의 제정 및 발간을 위해 아래와 같이 여러분들이 공헌하였습니다. 구분 성명 위원회 및 직위 연락처 소속사 ETRI, 과제 제안 이형석 010-3082-3455 ETRI 표준 초안 위원 제출 한국무선인터넷표준화포럼 김선자 042-860-6638 ETRI 위원 모바일 플랫폼 및 서비스 허태범 bombbie@ktf.com KTF㈜ 표준 초안 프로젝트그룹 의장 검토 외 모바일 플랫폼 및 서비스 프로젝트그룹 위원 이동통신기술위원회 042-860-1600 위규진 ETRI 표준안 의장 jschae@etri.re.kr 심의 외 이동통신기술위원회 위원 등 031-724-0090 김대중 - TTA 사무국 kdj@tta.or.kr 담당 070-7780-0096 김수학 - TTA soohagi@tta.or.kr (Specification for Mobile Standard Platform Version 2.2.0) 발행인 : 한국정보통신기술협회 회장 발행처 : 한국정보통신기술협회 463-824, 경기도 성남시 분당구 서현동 267-2 Tel : 031-724-0114, Fax : 031-724-0019 발행일 : 2008.12.
