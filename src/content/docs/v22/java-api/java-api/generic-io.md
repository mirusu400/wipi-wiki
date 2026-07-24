---
title: "3.1.5. Generic I/O"
---

Class IODevice java.lang.Object | +--org.kwis.msp.io.IODevice public class IODevice extends java.lang.Object 일반적인 I/O 디바이스를 제어하기 위한 클래스를 정의한다 Methods inherited from class java.lang.Object clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 생성자 상세 설명

#### IODevice

public IODevice(java.lang.String devname, int devnum, byte[] param) throws IOException 지원하는 장치의 이름 및 장치의 개수는 System.getProperty() 함수의 매개 변수로 "supported.iodevices"를 전달해서 얻어올 수 있다. 동일한 I/O 장치가 두 개 이상일 경우에는 매개 변수로 전달되는 devnum에 의해 구별한다. 예를 들어 IrDA 장치가 두 개일 경우 첫번째 장치는 "0"번, 두번째 장치는 "1"번이 된다. 장치의 이름 및 parma 데이터는 아래의 표와 같이 정의된다. 아래의 표에서 정의되지 않은 C API의 Generic I/O 및 `MC_ioDevOpen()` 함수의 규격을 따른다. devname Param 1st byte: 모드를 설정하며, 서버 모드일 경우 „S‟, 클라이언트 모드일 경우 „C‟로 설정함. “IrDA” 2nd~5th bytes: Timeout을 설정하며, big endian 형식의 byte 배열로 저장됨. Timeout값은 open시에만 적용됨. 타임아웃이 발생한 경우 IOException이 발생함. 바이트 배열 객체를 생성하여 파라미터로 줌. 함수 호출 “1ChipCard” 후 받는 값은 ATR (Answer To Reset) 값임. param의 크기가 ATR값의 길이보다 작을 경우 IllegalArgumentException이 발생함.

**매개 변수**

- `devname` - 장치의 이름
- `devnum` - 장치의 번호
- `param` - 장치 open시에 넘겨줄 파라미터 Throws
- `IOException` - 장치를 열 때 오류 발생 시
- `IllegalArgumentException` - 파마미터가 잘못 전달되었을 경우 메쏘드 상세 설명 close
- `public` - void close() throws IOException
- `open된` - IODevice를 닫는다. Throws
- `IOException` - 오류 발생시 read
- `public` - int read(byte[] buf, int offset,int length) throws IOException
- `IODevice로부터` - 데이터를 읽는다. (blocking) 함수임.

**매개 변수**

- `buf` - 읽을 데이터 저장 공간
- `offset` - 시작 offset
- `length` - 읽을 데이터 길이

**반환 값**

실제 읽은 바이트 수 Throws IOException 오류 발생시 write public int write(byte[] buf, int offset, int length) throws IOException IODevice에 데이터를 적는다. (blocking) 함수임.

**매개 변수**

- `buf` - 적을 데이터
- `offset` - 시작 offset
- `length` - 적을 데이터 길이

**반환 값**

실제 적은 바이트 수 Throws IOException 오류 발생시 control public void control(java.lang.String cmd, byte[] param1, byte[] param2) throws IOException IODevice를 제어한다. 장치에 주어진 명령에 따라 해당하는 오퍼레이션을 수행한다. cmd 및 param1, param2의 형식은 아래의 표와 같이 정의된다. 아래의 표에서 정의되지 않은 것은 C API의 General I/O의 규격을 따른다. device cmd param Param1: “SETOPCODE” [in] “SETMETHOD” “IrDA” (IrDA의 전송 Param2: 방식 설정) [in] “OBEXGET” or “OBEXPUT” “1ChipCard” “GETSTATUS” Param1: (IC Card의 삽입 [in] 길이 7의 바이트배열 여부 조사) [out] “exist” or “noexist” “GETCHANNEL” Param1: (현재 할당된 [in] 길이 4의 바이트배열 UICC의 [out] big-endian 형식의 Integer형 채널 논리적인 채널 번호 번호 얻기)

**매개 변수**

- `cmd` - 장치에 수행할 오퍼레이션의 종류를 나타내는 문자열 param1, param2 장치의 해당 오퍼레이션에 넘겨줄 매개 변수

**반환 값**

없음 Throws IOException 오류 발생시
