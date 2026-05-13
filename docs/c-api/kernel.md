# 5.1.1. 커널

커널 인터페이스 API
동적 메모리 할당/해제, 프로그램의 생성/종료, 타이머, 시스템 정보, 공유 메모
리에 관한 API 를 제공한다.
메모리 관리
메모리의 효율적인 관리를 위하여 메모리의 고정(static)할당과, 동적(dynamic)할
당을 지원한다. 또한 동적으로 할당된 메모리는 컴팩션(compaction)을 지원한다.
고정할당되는 메모리는 프로그램 로딩시 메모리에 할당되며, 프로그램 수행중에는
해제될수 없고, 프로그램 종료시에 자동으로 해제된다. 동적할당되는 메모리는 프
로그램 수행중에 MC_knlCalloc() API 에 의해 할당되며, 수행중에 MC_knlFree()
API 를 통해 해제할 수 있다. 프로그램 종료시 해제되지 않은 메모리는 플랫폼이
자동으로 해제한다. 컴팩션(compaction)은 동적 메모리 할당시 할당할 미사용 메
모리가 없으면 자동으로 일어난다. 동적으로 할당되는 메모리는 메모리식별자(ID)
이며 사용자는 컴팩션(compaction)이 일어날 수 있는 곳에서는 메모리식별자에서
포인터를 다시 구해와서 사용해야 한다. 컴팩션(compaction)은 동적메모리 할당시
할당할 미사용 메모리가 없는 경우와, MC_knlGetFreeMemory() API 를 부를 때만
일어난다. 이외의 API 에서 컴팩션(compaction)이 일어나는 경우는 해당 API 내부
에서 메모리를 동적으로 할당하는 경우이다. 내부적으로 메모리를 동적으로 할당
하는 API는 각 API 의 부작용 항목을 참조한다. 플랫폼 API 중에는 입력으로 간접
(indirect)버퍼를 요구하는 API들이 있다. 이런 API들은 주로 내부적으로 동적할
당을 사용하여 컴팩션이 일어날 수 있는 API들이다.
간접버퍼(메모리식별자와 같음)는 동적할당된 버퍼와, DECLARE_INDIRECTBUF()로
선언된 고정할당된 버퍼를 말한다.DECLARE_INDIRECTBUF()로 선언된 버퍼는 동적할
당된 버퍼와 같은 구조를 가지지만 실제로는 고정할당된다.
typedef struct _IndirectBuf {
INDIRECT_BUF_HEAD;
char buf[1024]
} IndirectBuf;
char staticBuf[256]; // 고정(static)할당 buffer
char imageBuf[1024];
DECLARE_INDIRECTBUF(IndirectBuf, idBuf);
void startClet() {
M_Byte* dynamicBuf;
M_Uint32 mBufID;
M_Int32 freeMemorySize;
strcpy(staticBuf, "this is testing...\n");
MC_knlPrintk("%s", staticBuf);
mBufID = MC_knlCalloc(256); // mBufID는 메모리식별자
dynamicBuf = MC_GETDPTR(mBufID); // 메모리식별자에서 포인터를 구해옴
strcpy(dynamicBuf, "this is testing...\n");
MC_knlPrintk("%s", dynamicBuf);
freeMemorySize = MC_knlGetFreeMemory(); //
컴팩션(compaction)이 일어남
dynamicBuf = MC_GETDPTR(mBufID); // 컴팩션(compaction)이 일어 날 수
있으므로
// 메모리식별자에서 다시 포인터를
구해옴
MC_knlPrintk("%s", dynamicBuf);
MC_knlFree(mBufID);
...
if ( (rID = MC_knlGetResourceID("test.gif", &rSize)) < 0 ) {
MC_knlPrintk(resource not found\n");
...
}
mBufID = MC_knlCalloc(rSize); // 동적할당을 이용한 리소스 얻기
MC_knlGetResource(rID, mBufID, rSize);
dynamicBuf = MC_GETDPTR(mBufID);
memcpy(imageBuf, dynamicBuf, rSize);
...
MC_knlGetResource(rID, &idBuf, rSize); //
DECLARE_INDIRECTBUF()로 할당된 간접버퍼를 통한 리소스 얻기
memcpy(imageBuf, idBuf.buf, rSize);
...
}
프로그램 관리
다중 프로그램 수행을 지원한다. 각 프로그램은 독립적인 메모리/실행 공간을 가
진다.플랫폼은 여러개의 프로그램을 동시에 실행할 수 있고 가능한한 자신이외의
프로그램 자원을 접근(access)할 수 없게 해야 한다. 프로그램간의 통신은 event
와 공유메모리를 사용한다. 프로그램은 자기자신을 생성시킨 프로그램과 부모/자
식간의 관계를 가진다. 응용 프로그램 관리자는 최상위 부모가 되고, 여기서부터
자식 프로그램이 수행된다. 자식 프로그램은 부모 프로그램을 강제로 종료시킬 수
없고, 부모는 자식을 강제로 종료시킬 수 있다. 또한 부모 프로그램이 종료되면
자식프로그램들은 자동으로 종료된다.
플랫폼은 오버레이(overlay)기능을 제공할 수 있다.. 프로그램 개발자는 플랫폼에
서 제공하는 heap 보다 큰 프로그램을 실행시킬 수 있다. 오버레이 기능을 이용하
기 위하여 플랫폼 개발환경에서는 프로그램 개발자가 큰 프로그램을 여러개의 작
은 프로그램으로 나누어 컴파일하고, 이것을 묶어서 플랫폼에 하나의 프로그램으
로 설치할 수 있는 환경을 제공해야 한다. 또한 프로그램 개발자가 큰 프로그램을
여러 작은 프로그램으로 나눌때, 작은 프로그램마다 심볼릭(symbolic)이름을 정의
할 수 있어야 한다. 플랫폼은 오버레이방식으로 작은 프로그램을 로딩할때, 프로
그램 식별자로 이 심볼릭(symbolic)이름을 사용한다.
동적 로딩 라이브러리를 지원한다. 플랫폼은 플랫폼에 추가할 API 를 라이브러리
로 만들고, 여러 프로그램이 공유하여 사용할 수 있는 기능을 제공한다.
공유메모리
프로그램간에 자료공유는 공유메모리를 이용한다. 공유메모리는 플랫폼에 1 개가
존재하고, 필요한 프로그램이 수행중에 생성할 수 있다. 공유메모리는 사용하는
프로그램이 종료되면 자동으로 해제된다.
기타
여러개의 타이머를 지원한다. 타이머를 설정한 프로그램이 타이머가 해제되기 전
에 종료되면 해제되지 않은 타이머도 자동으로 해제된다. 단말기 번호, ESN 등 각
종 시스템정보를 읽어오는 API를 제공한다.
버퍼할당
? 언급이 없을 경우, 플랫폼의 모든 API는 버퍼가 필요할 때 호출자(caller)
가 버퍼를 할당하여 매개변수로 전달한다.. 호출받는 API안에서 메모리버퍼
가 할당되어 반환할 경우에는 각API에 명확히 언급된다.
MC_PRGTYPE_JAVAAPP
프로토타입
#define MC_PRGTYPE_JAVAAPP
설명
자바 애플리케이션. 1로 정의 되어있다.
? MC_PRGTYPE_CAPP
프로토타입
#define MC_PRGTYPE_CAPP
설명
C 애플리케이션. 2로 정의 되어있다.
? MC_PRGTYPE_CDLL
프로토타입
#define MC_PRGTYPE_CDLL
설명
C 동적로딩 라이브러리, 3로 정의 되어있다.
? MC_PRGTYPE_JAVADLL
프로토타입
#define MC_PRGTYPE_JAVADLL
설명
자바 동적로딩 라이브러리, 4로 정의 되어있다.
? MC_PRGTYPE_JAVASYSDLL
프로토타입
#define MC_PRGTYPE_JAVASYSDLL
설명
자바 시스템 라이브러리, 5로 정의 되어있다.
? MC_DIR_SYS_READ_REQ_MASK
프로토타입
#define MC_DIR_SYS_READ_REQ_MASK
설명
system directory read가능. 0x01로 정의 되어있다.
? MC_DIR_SYS_WRITE_REQ_MASK
프로토타입
#define MC_DIR_SYS_WRITE_REQ_MASK
설명
system directory write가능. 0x02로 정의 되어있다.
? MC_DIR_SHARED_READ_REQ_MASK
프로토타입
#define MC_DIR_SHARED_READ_REQ_MASK
설명
shared directory read가능. 0x04로 정의 되어있다.
? MC_DIR_SHARED_WRITE_REQ_MASK
프로토타입
#define MC_DIR_SHARED_WRITE_REQ_MASK
설명
shared directory write가능. 0x08로 정의 되어있다.
? MC_NETWORK_ACCESS_REQ_MASK
프로토타입
#define MC_NETWORK_ACCESS_REQ_MASK
설명
network API사용 가능. 0x10으로 정의 되어있다.
? MC_SERIAL_ACCESS_REQ_MASK
프로토타입
#define MC_SERIAL_ACCESS_REQ_MASK
설명
serial API사용 가능. 0x20으로 정의 되어있다.
? MC_SYSTEM1_ACCESS_REQ_MASK
프로토타입
#define MC_SYSTEM1_ACCESS_REQ_MASK
설명
system group1 에 속한 API 사용가능(system group1 에 속할 API 들은 각 이통사가
정의) . 0x40으로 정의 되어있다.
? MC_SYSTEM2_ACCESS_REQ_MASK
프로토타입
#define MC_SYSTEM2_ACCESS_REQ_MASK
설명
system group2 에 속한 API 사용가능(system group2 에 속할 API 들은 각 이통사가
정의) . 0x80으로 정의 되어있다.
? MC_GETDPTR
프로토타입
#define MC_GETDPTR(mID)
설명
메모리식별자에서 포인터를 구한다.
MC_knlCalloc()에서 할당한 메모리식별자에서 실제로 사용할 포인터를 구한다.
매개 변수
mID – 메모리식별자
반환 값
포인터
? DECLARE_INDIRECTBUF
프로토타입
#define DECLARE_INDIRECTBUF(typeName, var)
설명
고정할당으로 간접버퍼(메모리식별자)를 할당한다.
버퍼를 할당하기 위하여는 먼저, 할당할 버퍼의 타입을 아래와 같은 형태로 정의
한다.
typedef struct type_name {
INDIRECT_BUF_HEAD; // 간접버퍼할당을 위해 플랫폼에서 제공하는
매크로
char buf[1024]; // 사용자가 원하는 크기의 버퍼 설정
};
매개 변수
typeName – 사용자가 선언한 타입선어의 이름
var – 간접버퍼로 선언할 변수명
반환 값
포인터
참고항목
사용법은 kernel overview의 예제 참조
? MCTimer
프로토타입
typedef struct _MTimer MCTimer
설명
타이머 설정에 사용되는 구조체형 선언
참고항목
MC_knlDefTimer, MC_knlSetTimer, MC_knlUnsetTimer
? TIMERCB
프로토타입
typedef void (*TIMERCB)(MCTimer *tm, void* parm)
설명
MC_knlDefTimer()에 등록하는 콜백함수이다. 설정한 타이머가 만료되면 불린다.
매개 변수
tm – 타이머 설정시 타이머 구조체 포인터
parm - 타이머 설정시 전달한 매개변수
참고항목
MC_knlDefTimer
? MC_knlPrintk
프로토타입
int MC_knlPrintk(M_Char* format, ...)
설명
format string 을 stdout 으로 출력한다. “ISO/IEC 9899:1999(E) -- Programming
Languages – C” 의 printf 규격을 따른다.
부작용
없음
참고 항목
없음
? MC_knlSprintk
프로토타입
int MC_knlSprintk(M_Char* buf, M_Char* format, ...)
설명
format string을 buf로 출력한다.
“ISO/IEC 9899:1999(E) -- Programming Languages – C” 의 sprintf 규격을 따른다.
부작용
없음
참고 항목
없음
? MC_knlGetExecNames
프로토타입
M_Int32 MC_knlGetExecNames(M_Char* prgName, M_Char* version, M_Char* vendor,
M_Char* buf, M_Int32 bufSize)
설명
플랫폼에 설치된 어플리케이션중 prgName(프로그램이름), version, vendor 와 일
치하는 어플리케이션 식별이름을 반환한다. 매개변수가 NULL 인 경우에는 아무것
이나 일치한다는 뜻 이다. 예를 들어 prgName, version, vendor가 모두 NULL인경
우, 플랫폼에 설치된 모든 프로그램의 이름을 반환한다. 반환되는 이름은 null 로
끝나는 문자열의 리스트이다.
예로서 두개의 일치하는 프로그램이 있을 경우
예)"/1/1.jar,3\0/2/2.jar,2\0" 와같이 buf에 저장되어 반환될 수 있다.
매개 변수
prgName - [in] 프로그램 이름
version - [in] 버전
vendor - [in] 제작사
buf - [out] null로 끝나는 문자열의 list
bufSize - [in] buf의 크기
반환 값
성공
해당되는 프로그램의 count
실패
M_E_SHORTBUF - buf가 작아 해당되는 이름을 모두 반환하지 못하는 경우
부작용
없음
참고 항목
없음
? MC_knlExecute
프로토타입
M_Int32 MC_knlExecute(M_Char* execName, M_Int32 parmCnt, ...)
설명
플랫폼에 설치된 java/C/C++프로그램을 실행시킨다
만기일이 지났거나 기타, 접근이 허락되지 않으면 에러값을 반환한다. 이 함수는
넌블라킹(non-blocking)함수이다. 프로그램이 죽게되면,
MV_CHILD_APP_DESTROY_EVENT 를 응용프로그램 관리자와 죽는 프로그램의 부모 프
로그램에게 보내게 된다. 실행된 프로그램은 다른 프로그램과 서로 다른 메모리
공간에 존재하게 되고, event 와 공유메모리를 통하여만 데이타를 주고 받을 수
있다.
매개변수 전달 : 프로그램은 자신이 실행시킨 자식프로그램에게 필요한 정보를 전
달할 수 있다. 전달할 매개변수는 문자열이어야만 한다.
C 부모 프로그램
...
MC_knlExecute("execName", 4, "this parm1", "20", "this parm3", "40");
...
실행된 프로그램이 C/C++ 자식 프로그램인 경우
void startClet(int argc, char* args[]) {
args[0]; // 프로그램 이름(플랫폼이 전달함)
args[1]; // "this parm1" 이 들어가 있음
args[2]; // "20" 이 들어가 있음
args[3]; // "this parm3" 이 들어가 있음
args[4]; // "40" 이 들어가 있음
}
실행된 프로그램이 Java 자식 프로그램인 경우
public static void main(String[] args) {
int argsLen = args.length; // 5임
args[0]; // " 프로그램 이름(플랫폼이 전달함)
args[1]; // "this parm1" 이 들어가 있음
args[2]; // "20" 이 들어가 있음
args[3]; // "this parm3" 이 들어가 있음
args[4]; // "40" 이 들어가 있음
}
매개 변수
execName - [in] 실행시킬 프로그램의 이름, MC_knlGetExecNames()에 의해 구해진
다.
parmCnt - [in] 이 매개변수뒤에 연속해서 전달할 매개변수 수
반환 값
성공
생성된 프로그램 ID
실패
M_E_ACCESS - 만기일이 지났거나, 접근 권한이 없는 경우
M_E_NOMEMORY – 메모리가 부족한 경우
M_E_INVALID - 전달한 매개변수가 잘못된 경우
부작용
없음
참고 항목
없음
? MC_knlExit
프로토타입
void MC_knlExit(M_Int32 exitCode)
설명
프로그램을 종료한다. 실제 종료시점은 이 함수가 불리는 시점이 아니라, 이 함수
에서 return 되고, 이벤트 핸들러를 빠져나간 시점에서 종료가 일어난다. 그러므
로 MC_knlExit()를 호출한 이후에는 바로 return 해야 한다. MC_knlExit()를 통하
여 프로그램이 종료되게 되면 부모 프로그램과, 응용 프로그램 관리자에게
MV_CHILD_APP_DESTROY_EVENT(exitCode 는 이벤트 매개변수로 전달)를 보내게 된다.
프로그램 종료시 해제되지 않은 자원들은 플랫폼에서 자동으로 해제한다.
아래의 예는 프로그램 A 가 프로그램 B 를 실행시키고 프로그램 B 가 exitCode 27
로 종료하는 예제이다.
program A
void handleCletEvent(int type, int parm1, int parm2)
switch(type) {
case MV_CHILD_APP_DESTROY_EVENT :
knlPrintk("exit code %d\n", param1); // 27을 출력함
break;
case XXX :
...
execute("B", ...);
...
break;
}
...
}
program B
void handleCletEvent(int type, int parm1, int parm2) {
...
if ( xxx ) {
MC_knlExit(27);
return
}
}
매개 변수
exitCode - [in] 종료값
부작용
없음
참고 항목
없음
? MC_knlProgramStop
프로토타입
M_Int32 MC_knlProgramStop(M_Int32 prgID)
설명
수행중인 다른 응용 프로그램을 강제로 종료시킨다. 동적로딩라이브러리는 강제로
해제될 수 없고, 동적로딩라이브러리를 사용하는 모든 응용프로그램이 종료되면
자동으로 종료된다. 부모프로그램은 종료시킬 수 없고, 자식프로그램만 종료시킬
수 있다.
매개 변수
prgID - [in] 종료시킬 프로그램 식별자
반환 값
성공
실패
M_E_ACCESS - 부모 프로그램 종료를 시도한 경우
부작용
없음
참고 항목
없음
? MC_knlGetCurProgramID
프로토타입
M_Int32 MC_knlGetCurProgramID()
설명
현재 수행되고 있는 자기 자신의 프로그램 식별자를 얻어 온다.
반환 값
프로그램 식별자
부작용
없음
참고 항목
없음
? MC_knlGetParentProgramID
프로토타입
M_Int32 MC_knlGetParentProgramID()
설명
현재 수행되고 있는 프로그램의 부모 프로그램 식별자를 얻어 온다.
반환 값
프로그램 식별자
부작용
없음
참고 항목
없음
? MC_knlGeAppManagerID
프로토타입
M_Int32 MC_knlGetAppManagerID()
설명
응용프로그램 관리자의 프로그램 ID를 구한다.
반환 값
프로그램 식별자
부작용
없음
참고 항목
없음
? MC_knlGetProgramInfo
프로토타입
M_Int32 MC_knlGetProgramInfo(M_Int32* buf, M_Int32 bufSize)
설명
현재 동작중인 프로그램에 대한 정보를 얻는다. 반환값은 현재 동작중인 프로그램
의 수를 나타내고, 각 index 에 속한 값은 해당 index 에 해당하는 프로그램의
type를 나타낸다. 예로소 buf[2]가 MC_PRGTYPE_JAVADLL인경우 prgID가 2인 프로
그램은 java application DLL이다.
매개 변수
buf - [out] 구해진 프로그램 타입이 반환될 버퍼
bufSize - [in] 전달되는 버퍼 크기
반환 값
성공
동작중인 프로그램 수
실패
M_E_SHORTBUF - 버퍼가 작아 모두 반환하지 못하는 경우
부작용
없음
참고 항목
없음
? MC_knlGetAccessLevel
프로토타입
M_Int32 MC_knlGetAccessLevel()
설명
프로그램의 접근 수준을 구한다. 반환값의 각 비트(bit)는 현재 프로그램이 접근
할 수 있는 API들의 종류를 나타낸다. 각 비트(bit)의 의미는
MC_DIR_SYS_READ_REQ_MASK, MC_DIR_SYS_WRITE_REQ_MASK,
MC_DIR_SHARED_READ_REQ_MASK, MC_DIR_SHARED_WRITE_REQ_MASK,
MC_NETWORK_ACCESS_REQ_MASK, MC_SERIAL_ACCESS_REQ_MASK,
MC_SYSTEM1_ACCESS_REQ_MASK, MC_SYSTEM2_ACCESS_REQ_MASK 마스크값에 따른다.
반환 값
접근수준(각 마스크값의 OR값)
부작용
없음
참고 항목
없음
? MC_knlGetProgramName
프로토타입
M_Int32 MC_knlGetProgramName(M_Char* nameBuf, M_Int32 bufSize)
설명
현재 수행되고 있는 자기 자신의 프로그램 이름을 구한다. 구해지는 이름은 ADF
파일에 기술된 이름이다.
매개 변수
nameBuf - [out] 구해진 이름이 반환될 버퍼
bufSize - [in] namebuf size
반환 값
성공
실패
M_E_SHORTBUF - 버퍼가 작아 이름을 모두 반환하지 못하는 경우
부작용
없음
참고 항목
없음
? MC_knlCreateSharedBuf
프로토타입
void* MC_knlCreateSharedBuf(const M_Char* name, M_Int32 size)
설명
공유 버퍼를 생성한다. 공유 버퍼는 프로그램간에 자료를 공유할 수 있도록 한다.
생성된 버퍼는 이 버퍼를 사용하는 모든 프로그램이 종료되면 자동으로 삭제된다.
매개 변수
name – [in] 공유버퍼의 이름. Null 문자로 끝난다.
size - [in] 생성시킬 버퍼의 크기
반환 값
성공
생성된 간접버퍼(메모리식별자)
실패
0 - 경우 같은 이름의 공유버퍼가 존재하거나 메모리가 부족한 경우
부작용
공유버퍼 생성시 메모리가 부족하면 컴팩션이 일어날 수 있다.
참고 항목
없음
? MC_knlDestroyShareBuf
프로토타입
M_Int32 MC_knlDestroySharedBuf(void* buf)
설명
생성된 공유버퍼를 파괴한다.
매개 변수
buf – [in] 공유 간접버퍼(메모리식별자)
반환 값
성공
실패
M_E_INVALID – 공유버퍼의 메모리식별자가 존재하지 않을 경우
M_E_ERROR – 기타 이유로 공유버퍼를 파괴할 수 없을 경우
부작용
없음
참고 항목
없음
? MC_knlGetSharedBuf
프로토타입
void* MC_knlGetSharedBuf(const M_char* name)
설명
name 문자열로 생성된 공유 버퍼를 얻어 온다.
매개 변수
name – [in] 공유버퍼의 이름. Null 문자로 끝난다.
반환 값
성공
공유 간접버퍼(메모리식별자)
실패
0 - 설정된 공유버퍼가 없는 경우
부작용
없음
참고 항목
없음
? MC_knlGetSharedBufSize
프로토타입
M_Int32 MC_knlGetSharedBufSize(void* buf)
설명
공유 버퍼 크기를 얻어 온다.
매개 변수
buf – [in] 공유 간접버퍼(메모리식별자). MC_knlCreateSharedBuf() 나
MC_knlGetSharedBuf() 함수의 리턴값이다.
반환 값
성공
공유버퍼 크기
실패
-1 - 설정된 공유버퍼가 없는 경우
부작용
없음
참고 항목
없음
? MC_knlResizeSharedBuf
프로토타입
void* MC_knlResizeSharedBuf(void* buf, M_Int32 size)
설명
공유버퍼의 크기를 변경한다.
매개 변수
buf – [in] 공유 간접버퍼(메모리식별자)
size - [in] 생성할 공유버퍼 크기
반환 값
성공
크기가 변경된 공유 간접버퍼(메모리식별자)
실패
부작용
공유버퍼 크기변경시 메모리가 부족하면 컴팩션이 일어날 수 있다
참고 항목
없음
? MC_knlAlloc
프로토타입
M_Uint32 MC_knlAlloc(M_Int32 size)
설명
힙에서 요청하는 크기만큼의 메모리를 할당한다. 할당된 메모리는 MC_knlFree()에
서 해제해 주어야 재사용된다. 할당된 메모리를 프로그램 종료시까지 해제하지 않
으면 프로그램 종료시 플랫폼에서 자동으로 해제한다. 할당된 메모리는 메모리 식
별자로 사용시 MC_GETDPTR()를 이용하여 포인터를 구해와 사용해야 한다.
매개 변수
size - [in] 할당을 요청하는 크기(byte단위)
반환 값
성공
할당된 메모리 식별자
실패
부작용
메모리가 부족하면 컴팩션이 일어날 수 있다
참고 항목
없음
? MC_knlCalloc
프로토타입
M_Uint32 MC_knlCalloc(M_Int32 size)
설명
힙에서 요청하는 크기만큼의 메모리를 할당한다. 할당되는 영역은 0 으로 초기화
된다. 할당된 메모리는 MC_knlFree()에서 해제해 주어야 재사용된다. 할당된 메모
리를 프로그램 종료시까지 해제하지 않으면 프로그램 종료시 플랫폼에서 자동으로
해제한다. 할당된 메모리는 메모리 식별자로 사용시 MC_GETDPTR()를 이용하여 포
인터를 구해와 사용해야 한다.
매개 변수
size - [in] 할당을 요청하는 크기(byte단위)
반환 값
성공
할당된 메모리 식별자
실패
부작용
메모리가 부족하면 컴팩션이 일어날 수 있다
참고 항목
없음
? MC_knlFree
프로토타입
void MC_knlFree(M_Uint32 mID)
설명
MC_knlCalloc()으로 할당한 메모리를 해제한다. 할당되지 않은 메모리를 해제할려
고 하면 안된다.
매개 변수
mID - [in] 해제할 메모리 식별자
부작용
없음
참고 항목
없음
? MC_knlGetTotalMemory
프로토타입
M_Int32 MC_knlGetTotalMemory()
설명
total메모리를 구한다.
반환 값
total메모리(byte단위)
부작용
없음
참고 항목
없음
? MC_knlGetFreeMemory
프로토타입
M_Int32 MC_knlGetFreeMemory()
설명
free메모리를 구한다. 컴팩션을 수행하고 free메모리를 구해 반환한다. 명시적으
로 메모리 컴팩션이 필요한 경우, 이 함수를 이용한다
반환 값
free메모리(byte단위)
부작용
없음
참고 항목
없음
? MC_knlDefTimer
프로토타입
void MC_knlDefTimer(MCTimer* tm, TIMERCB cb)
설명
타이머를 초기화하고 콜백함수를 등록한다.
타이머가 만료되면 등록된 콜백함수가 불립니다.
콜백함수가 불릴때 MC_knlSetTimer()호출시 설정한 타이머구조체 포인터와 매개변
수가 전될됩니다.
MCTimer tm;
void TimerCb(MCTimer* ptm, void* parm) {
MC_knlPrintk("timer occur %d\n", parm);
MC_knlSetTimer(ptm, 1000L, (int)param+1);
}
void startClet(int argc, char* argv[]) {
MC_knlPrintk("start Clet!!!\n");
MC_knlDefTimer(&tm, TimerCb);
MC_knlSetTimer(&tm, 1000L, 0x1234);
}
매개 변수
tm - [in] 초기화할 타이머 구조체 포인터
cb – [in] 타이머 콜백함수
부작용
없음
참고 항목
없음
? MC_knlSetTimer
프로토타입
M_Int32 MC_knlSetTimer(MCTimer* tm, M_Int64 timeout, void* parm)
설명
타이머를 설정한다.
타이머가 만료되면 MC_knlDefTimer()에서 설정한 콜백함수가 불린다.
만료되지않은 타이머가 남은 상태에서 프로그램이 종료하면, 남은 타이머들은 자
동으로 해제된다.
만료되지 않은 타이머를 이 함수를 통해서 재 정의하면 오류가 발생한다.
만일 만료되지 않은 타이머를 재 정의하기 위해서는 MC_knlUnsetTimer()를 호출한
후에 이 함수를 다시 호출한다.
타이머는 플랫폼하단의 운영체제에서 지원하는 타이머 resolution 과 타이머 만료
시 다른 태스크가 수행될 경우
어느정도의 오차는 발생할 수 있다.
매개 변수
tm - [in] 타이머 구조체 포인터
timeout - [in] milliseconde단위
parm - [in] 타이머가 만료되었을때 콜백함수에 전달될 매개변수
반환 값
성공
실패
M_E_EXIST – 기존에 설정된 타이머가 만료되지 않고 존재하는 경우
부작용
없음
참고 항목
없음
? MC_knlUnsetTimer
프로토타입
void MC_knlUnsetTimer(MCTimer* tm)
설명
설정된 타이머를 취소한다. 타이머가 설정되지 않았을때는 무시된다.
매개 변수
tm - [in] 타이머 구조체 포인터
부작용
없음
참고 항목
없음
? MC_knlCurrentTime
프로토타입
M_Int64 MC_knlCurrentTime()
설명
현재의 시간을 구한다. 단위는 millisecond이다.
반환 값
1970년1월1일0시0분0초를 기준으로 현재시간까지의 millisecond
부작용
없음
참고 항목
없음
? MC_knlGetSystemProperty
프로토타입
M_Int32 MC_knlGetSystemProperty(M_Char* id, M_Char* rtnBuf, M_Int32 bufSize)
설명
단말기에 특화된 값을 읽어 온다. 패러미터로 올 수 있는 id 문자열은
HAL 문서 API중 MH_sysGetInformation()에서 사용하는 문자열에
준하고, 또한 각 이통사나 벤더에 따라 추가 확장될 수 있다.
"ESN", "NID", "SID", "BASELAT", "BASELONG", "CURRENTCH",
"PHONENUMBER", "RSSILEVEL", "BATTERYLEVEL",
"DATASERVICEMODE", "MAXSOCKETNUM", "MAXRSSILEVEL",
"MAXSERIALNUM", "MAXBATTLEVEL", "MEDIADEVICES", "DNS",
“VIBRATORLEVEL” 등의 id 문자열이 온다. 이것은 탑재되는
단말기에 따라 달라 질 수 있다.
매개 변수
id - [in] 읽어 오고자 하는 문자열
rtnBuf - [out] 반환 문자열이 반환되는 버퍼
bufSize - [in] 반환값이 저장될 버퍼 크기
반환 값
성공
실패
M_E_SHORTBUF : 반환되는 문자열보다 전달한 버퍼크기가 작을때 발생
M_E_INVALID : 전달한 매개변수가 잘못되었음
부작용
없음
참고 항목
없음
? MC_knlSetSystemProperty
프로토타입
M_Int32 MC_knlSetSystemProperty(M_Char* id, M_Char* buf)
설명
단말기에 특화된 값을 설정 한다. 패러미터로 올 수 있는 id,
buf문자열은 HAL 문서 API 중 MH_sysSetInformation()에서
사용하는 문자열에 준하고, 또한 각 이통사나 벤더에 따라 추가
확장될 수 있다.
매개 변수
id - [in] 설정 하고자 하는 ID 문자열
buf - [in] 설정할 문자열 버퍼
반환 값
성공
실패
M_E_INVALID : 전달한 매개변수가 잘못되었거나, 설정할 수 없는 정보
부작용
없음
참고 항목
없음
? MC_knlGetResourceID
프로토타입
M_Int32 MC_knlGetResourceID(M_Char* resourceName, M_Int32* size)
설명
프로그램과 연관된 리소스의 ID를 얻어온다
매개 변수
resourceName - [in] 리소스 이름
size - [?] 리소스 크기
반환 값
성공
리소스 ID
실패
M_E_NOENT : 리소스가 존재하지 않는 경우
부작용
없음
참고 항목
없음
? MC_knlGetResource
프로토타입
M_Int32 MC_knlGetResource(M_Int32 resourceID, void* buf, M_Int32 bufSize)
설명
리소스 ID에 해당하는 리소스를 읽어온다.
매개 변수
resourceID - [in] 리소스 ID
buf - [in] 리소스를 복사할 간접버퍼(메모리식별자)
bufSize – [in] 버퍼크기
반환 값
성공
실패
M_E_SHORTBUF : 버퍼크기가 작은 경우
부작용
컴팩션이 일어날 수 있음
참고 항목
없음
