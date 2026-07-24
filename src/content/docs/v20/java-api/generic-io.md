---
title: "3.1.5. Generic I/O"
---

---

## Class IODevice

```text
java.lang.Object
  +--org.kwis.msp.io.IODevice
```

```java
public class IODevice extends java.lang.Object
```

일반적인 I/O 디바이스를 제어하기 위한 클래스를 정의한다

*Methods inherited from class java.lang.Object: clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 생성자 상세

### IODevice

```java
public IODevice(java.lang.String devname, int devnum, byte[] param)
```

지원하는 장치의 이름 및 장치의 개수는 System.getProperty() 함수의 매개 변수로 "supported.iodevices"를 전달해서 얻어올 수 있다. 동일한 I/O 장치가 두 개 이상 일 경우에는 매개 변수로 전달되는 devnum에 의해 구별한다. 예를 들어 IrDA 장치가 두 개일 경우 첫번째 장치는 "0"번, 두번째 장치는 "1"번이 된다. 장치의 이름 및 parma 데이터는 C API의 Generic I/O 및 `MC_ioDevOpen()` 함수의 규격을 따른다.

**매개 변수**

- `devname` - 장치의 이름
- `devnum` - 장치의 번호
- `param` - 장치 open시에 넘겨줄 파라미터 Throws
- `IOException` - 장치 open 실패시 메쏘드 상세 설명 close

### close

```java
public void close() throws IOException
```

- `open된` - IODevice를 닫는다. Throws:
- `IOException` - – 오류 발생시 read

### read

```java
public int read(byte[] buf, int offset,int length) throws IOException
```

- `IODevice로부터` - 데이터를 읽는다. (blocking) 함수임.

**매개 변수**

- `buf` - 읽을 데이터 저장 공간
- `offset` - 시작 offset
- `length` - 읽을 데이터 길이 Throws:
- `IOException` - – 오류 발생시

**반환 값**

실제 읽은 바이트 수

### write

```java
public int write(byte[] buf, int offset, int length) throws IOException
```

IODevice에 데이터를 적는다. (blocking) 함수임.

**매개 변수**

- `buf` - 적을 데이터
- `offset` - 시작 offset
- `length` - 적을 데이터 길이 Throws:
- `IOException` - – 오류 발생시

**반환 값**

실제 적은 바이트 수

### control

```java
public void control(java.lang.String cmd, byte[] param1, byte[] param2)
```

IODevice를 제어한다. 장치에 주어진 command에 따라 해당하는 오퍼레이션을 수행한 다. cmd 및 param1, param2는 C API의 General I/O의 규격을 따른다.

**매개 변수**

- `cmd` - 장치에 수행할 오퍼레이션의 종류를 나타내는 문자열 param1, param2 장치의 해당 오퍼레이션에 넘겨줄 매개 변수

**반환 값**

없음
