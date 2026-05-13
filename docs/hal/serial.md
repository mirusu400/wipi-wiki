# 4.7. Serial

단말기에서 지원하는 시리얼을 제어하는 함수 들이다.
지원하는 시리얼 포트 수는 MH_sysGetSystemInformation()함수에서 구할 수 있다.
시리얼 포트 번호는 “첫 번째 시리얼포트가 0, 두 번째 시리얼포트가 1, … … (최
대 지원포트 수-1)” 와 같은 방식으로 번호를 부여한다. 시리얼포트에 상태변화가
일어나면 운영체제는 이벤트를 플랫폼에 전달하여 상태변화를 알린다. 운영체제가
플랫폼에 이벤트를 전달할 때 호출하는 함수는 MH_pltEvent() 이며 이때 매개변수
로 MH_SERIAL_EVENT와 MH_SerialEvent 를 넘겨주어야 한다.
? 관련 자료형
//시리얼 이벤트
typedef enum MH_SUB_SERIAL_EVENT{
MH_SERIALEV_READ = 0, // 수신할 수 있게 될 경우 전달되는 이벤트
MH_SERIALEV_WRITE, // 전송할 수 있게될 경우 전달되는 이벤트
MH_SERIALEV_ERROR, // 시리얼 H/W 에러
} MH_SUB_SERIAL_EVENT;
//시리얼 이벤트를 전달하는 구조체
typedef struct MH_SerialEvent{
M_Int32 fd; // 포트식별자
M_Int32 event; // 발생되는 Event, MH_SUB_SERIAL_EVENT값
} MH_SerialEvent;
? MH_serialOpen
설명
시리얼을 포트를 연다. 지정되는 포트는 매개변수 param 으로 전달되는 제어문자
열에 의해 제어된다. 제어문자열은 다음과 같은 문법으로 만들어 져야 한다.
제어문자열 ::= [제어쌍]
제어쌍 ::= 제어키 “=” 제어값 *(,제어키 “=” 제어값)
제어키 ::= 알파벳혹은 숫자문자로 만들어진 문자열
제어값 ::= 알파벳혹은 숫자문자로 만들어진 문자열
이 문서에서 정의하는 제어키와 제어값은 아래 표와 같다.
제어키 제어값 의미 디폴트
baudrate 9600, 19200, 38400, 속도 115200
57600, 115200
parity even, odd, no 패리티 no
size 숫자 바이트 크기 8
flow hardware, software, 흐름제어 no
no
이외의 제어키와 제어값에 대한 정의는 추가될 수 있다. 예를 들어 8 비트, 패리티없
음, 115200 속도로 하드웨어 흐름제어를 하기 위해 포트를 열 경우 제어문자열은 다
음과 같다.
”baudrate=115200,parity=no,size=8,flow=hardware”
제어문자열에 앞에서 정의한 제어키가 없을 경우 디폴트 값으로 설정된다.
프로토타입
M_Int32 MH_serialOpen (M_Int32 port,M_byte *param)
매개 변수
[in] port 포트 번호
[in] param 제어문자열
반환 값
성공
식별자를 반환한다.
실패
M_E_NOTSUP - 해당 포트번호 또는 제어문자열에 대한 제어을 제공하지
않을 경우
M_E_INVALID – 제어문자열이 잘 못된 포멧일 경우
M_E_ISCONN – 해당 포트가 이미 열린 경우
M_E_ERROR - 기타 이유로 실패할 경우
부작용
없음
참고 항목
없음
? MH_serialWrite
설명
시리얼로 데이터를 전송한다.
반환 값이 M_E_WOULDBLOCK 일 경우에는 시스템 내부 요인으로 지금 당장 전송할
수 없다는 것을 의미하며, 전송할 수 있는 상태가 되면, MH_SERIALEV_WRITE 이벤
트를 플랫폼에 전달해야 한다. 플랫폼은 MH_SERIALEV_WRITE 이벤트를 받으면 다시
MH_serialWrite()를 호출하여 시리얼 데이터 쓰기를 재시도 하면 된다. 만약 이
함수를 호출했을 때 DTR 핀에 상대방이 감지되지 않으면 M_E_NOTCONN 을 리턴한다.
프로토타입
M_Int32 MH_serialWrite (M_Int32 fd, M_Uint8* buf, M_Int32 len)
매개 변수
[in] fd 시리얼 식별자
[in] buf 데이터 버퍼
[in] len 전송할 크기
반환 값
성공
전송한 크기
실패
M_E_ERROR - 기타 이유로 실패할 경우
M_E_WODULDBLOCK –전송할 수 있을 때 까지 기다려야 경우
M_E_NOTCONN – 이 함수를 호출 했을 때 DTR 핀에 상대방이 감지되지 않을
경우
부작용
없음
참고 항목
없음
? MH_serialRead
설명
시리얼로 데이터를 수신한다. 반환 값이 M_E_WOULDBLOCK 일 경우에는 읽어 들일
데이터가 없다는 것을 의미하며, 읽어 들일 데이터가 도착하면, MH_SERIALEV_READ
이벤트가 플랫폼에 전달되어야 한다. 플랫폼은 MH_SERIALEV_READ 이벤트를 받으면
다시 MH_serialRead()를 호출하여 시리얼 데이터 읽기를 재시도 하면 된다. 만약
이 함수를 호출했을 때 DTR 핀에 상대방이 감지되지 않으면 M_E_NOTCONN 을 리턴
한다.
프로토타입
M_Int32 MH_serialRead (M_Int32 fd, M_Uint8 *buffer, M_Int32 len)
매개 변수
[in] port 시리얼 식별자
[out] buf 데이터 버퍼
[in] len 버퍼의 길이
반환 값
성공
읽은 데이터 길이
실패
M_E_ERROR - 기타 이유로 실패할 경우 M_E_WOULDBLOCK –읽을 데이터가
도착할 때까지 기다려야 하는 경우
M_E_NOTCONN - 이 함수를 호출 했을 때 DTR 핀에 상대방이 감지되지 않
을 경우
부작용
없음
참고 항목
없음
? MH_serialClose
설명
시리얼포트를 닫는다.
프로토타입
void MH_serialClose (M_Int32 fd)
매개 변수
[in] fd 시리얼 식별자
반환 값
없음
부작용
없음
참고 항목
없음
