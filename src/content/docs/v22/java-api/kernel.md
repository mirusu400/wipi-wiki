---
title: "2.2.1. 커널"
---

---

## Class Kernel

```text
java.lang.Object
  +--org.kwis.msf.core.Kernel
```

```java
public class Kernel extends java.lang.Object
```

System Kernel의 기능을 제공하는 클래스 이다. 프로그램의 정보를 얻어오기, 프로그램을 실행, 종료, shared library의 load와 같은 기능을 제공한다.

*Methods inherited from class java.lang.Object: clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 필드 상세

### PRGTYPE_ CAPP

```java
public static final int PRGTYPE_CAPP
```

C 애플리케이션

### PRGTYPE_ CDLL

```java
public static final int PRGTYPE_CDLL
```

C 동적 로딩 라이브러리

### PRGTYPE_ JAVAAPP

```java
public static final int PRGTYPE_JAVAAPP
```

Java 애플리케이션

### PRGTYPE_ JAVADLL

```java
public static final int PRGTYPE_JAVADLL
```

Java 동적 로딩 라이브러리

### PRGTYPE_ JAVASYSDLL

```java
public static final int PRGTYPE_JAVASYSDLL
```

Java 시스템라이브러리

### DIR_SYS_READ_REQ_MASK

```java
public static final int DIR_SYS_READ_REQ_MASK
```

system directory read가능

### DIR_SYS_WRITE_REQ_MASK

```java
public static final int DIR_SYS_WRITE_REQ_MASK
```

system directory write가능

### DIR_SHARED_READ_REQ_MASK

```java
public static final int DIR_SHARED_READ_REQ_MASK
```

shared directory read가능

### DIR_SHARED_WRITE_REQ_MASK

```java
public static final int DIR_SHARED_WRITE_REQ_MASK
```

shared directory write가능

### NETWORK_ACCESS_REQ_MASK

```java
public static final int NETWORK_ACCESS_REQ_MASK
```

network API사용 가능

### SERIAL_ACCESS_REQ_MASK

```java
public static final int SERIAL_ACCESS_REQ_MASK
```

serial API사용 가능

### SYSTEM1_ACCESS_REQ_MASK

```java
public static final int SYSTEM1_ACCESS_REQ_MASK
```

system group1에 속한 API사용가능(system group1에 속할 API들은 각 이통사가 정의)

### SYSTEM2_ACCESS_REQ_MASK

```java
public static final int SYSTEM2_ACCESS_REQ_MASK
```

system group2에 속한 API사용가능(system group2에 속할 API들은 각 이통사가 정의)

### ACCESS_ERROR

```java
public static final int ACCESS_ERROR
```

실행시킬 프로그램의 만료일이 지났거나, 접근이 허락되지 않는 경우에 발생하는 에러값은 -24 이다.

### MEMORY_ERROR

```java
public static final int MEMORY_ERROR
```

메모리가 부족하여 프로그램을 실행시키지 못할 경우 발생하는 에러 값은 -17 이다.

### ARGU_ERROR

```java
public static final int ARGU_ERROR
```

전달한 매개변수가 적합하지 않아서 프로그램을 실행시키지 못하는 경우에 발생하는 에러 값은 -9 이다.

## 생성자 상세

없음

## 메서드 상세

### execute

```java
public static int execute(String execName, String[] args)
```

플랫폼에 설치된 프로그램을 실행시킨다. 만료일이 지났거나 기타, 접근이 허락되지 않으면 에러값을 반환한다. 이 함수는 넌블라킹(non-blocking)함수이다. 프로그램이 죽게 되면, MV_CHILDSTOP_EVENT를 응용프로그램 관리자와 죽는 프로그램의 parent에 보내게 된다. 실행된 프로그램은 다른 프로그램과 서로 다른 메모리 공간에 존재하게 되고, 이벤트와 공유버퍼를 통하여만 데이타를 주고 받을 수 있다.

**매개 변수**

- `execName` - 실행시킬 프로그램의 이름, getExecNames()함수에 의해 구해진다
- `args` - Main method()로 전달될 매개변수

**반환 값**

성공

실행된 프로그램의 프로그램 ID
실패

ACCESS_ERROR 만기일이 지났거나, 접근 권한이 없는 경우 MEMORY_ERROR 메모리가 부족한 경우 ARGU_ERROR 전달한 매개변수가 잘못된 경우

**참고 항목**

getExecNames(String prgName, String version, String vendor)

### load

```java
public static int load(java.lang.String dllLibName, java.lang.String[] args)
```

플랫폼에 설치된 동적링킹라이브러리(DLL)를 로딩한다. 만기일이 지났거나 기타, 접근이 허락되지 않으면 에러값을 반환한다. 이 함수는 넌블라킹(non- blocking)함수이다. 프로그램이 라이브러리를 로딩하면 같은 메모리공간에 존재하고 바로 라이브러리 함수를 불러 사용할 수 있다. 서로 다른 프로그램이 같은 라이브러리를 로딩하면, 라이브러리 등록시 설정한 값(예를 들어 ADF)에 따라 라이브러리가 공유 될 수도 있고, 별도로 로딩 될 수도 있다. 해당 라이브러리는 라이브러리를 로딩한 모든 프로그램이 명시적으로 `MC_knlUnload`()를 수행하거나, 사용하는 모든 프로그램이 종료되면 자동으로 종료된다.

**매개 변수**

- `dllLibName` - 실행시킬 프로그램의 이름, getExecNames()함수에 의해 구해진다.
- `args` - Main method()로 전달될 parameter

**반환 값**

성공

load된 프로그램의 프로그램ID 반환
실패

음수 반환

**참고 항목**

getExecNames(String prgName, String version, String vendor)

### load

```java
public static int load(java.lang.String dllLibName)
```

플랫폼에 설치된 동적링킹라이브러리(DLL)를 로딩한다. 만기일이 지났거나 기타, 접근이 허락되지 않으면 에러값을 반환한다. 이 함수는 넌블라킹(non- blocking)함수이다. 프로그램이 라이브러리를 로딩하면 같은 메모리공간에 존재하고 바로 라이브러리 함수를 불러 사용할 수 있다. 서로 다른 프로그램이 같은 라이브러리를 로딩하면, 라이브러리 등록시 설정한 값(예를 들어 ADF)에 따라 라이브러리가 공유 될 수도 있고, 별도로 로딩 될 수도 있다. 해당 라이브러리는 라이브러리를 로딩한 모든 프로그램이 명시적으로 `MC_knlUnload`()를 수행하거나, 사용하는 모든 프로그램이 종료되면 자동으로 종료된다.

**매개 변수**

- `dllLibName` - 실행시킬 프로그램의 이름, getExecNames()함수에 의해 구해진다.

**반환 값**

성공

load된 프로그램의 프로그램ID 반환
실패

음수 반환

**참고 항목**

getExecNames(String prgName, String version, String vendor)

### getPrgID

```java
public static int getPrgID()
```

현재 프로그램의 ID를 구한다.

**반환 값**

프로그램 ID

### getAMID

```java
public static int getAMID()
```

응용프로그램 관리자의 프로그램의 ID를 구한다.

**반환 값**

프로그램 ID

### getParentPrgID

```java
public static int getParentPrgID()
```

parent 프로그램의 ID를 구한다.

**반환 값**

프로그램 ID

### getExecNames

```java
public static String[] getExecNames(String prgName, String version, String vendor)
```

플랫폼에 설치된 애플리케이션 중 prgName(프로그램이름), version, vendor와 일치하는 애플리케이션 식별이름을 반환한다. 매개변수가 NULL인 경우에는 아무것이나 일치한다는 뜻 이다. 예를 들어 prgName, version, vendor가 모두 NULL인 경우, 플랫폼에 설치된 모든 프로그램의 이름을 반환한다. 반환되는 이름은 null로 끝나는 문자열의 리스트이다.

**매개 변수**

- `prgName` - 프로그램 이름
- `version` - 프로그램 버전
- `vendor` - 프로그램 공급자

**반환 값**

프로그램 이름 string array

### getPrgInfo

```java
public static int[] getPrgInfo()
```

현재 동작중인 프로그램에 대한 정보를 얻는다. 반환되는 buf 배열에는 프로그램 ID, 프로그램 type이 쌍으로 온다. 예를 들어 buf[0] 이 1 이고 buf[1]가 PRGTYPE_ JAVADLL일 경우, 프로그램 ID가 1인 프로그램의 타입이 java application DLL이라는 것을 나타낸다. 따라서 배열의 크기는 프로그램 수의 2배가 된다.

**반환 값**

동작중인 프로그램의 prgID와 type을 포함하는 integer array

### stop

```java
public static void stop(int prgID)
```

프로그램을 강제로 종료시킨다. DLL은 강제로 종료될 수 없고, DLL을 사용하는 모든 APP가 종료되면 자동으로 종료된다.

**매개 변수**

- `prgID` - 강제 종료시킬 프로그램이 ID getAccessLevel

### getAccessLevel

```java
public static int getAccessLevel()
```

프로그램의 access level을 구한다. return value의 각 bit는 현재 프로그램이 access할 수 있는 API들의 종류를 나타낸다. 각 bit의 의미는 위에 정의된 XXX_REQ
- `define문에` - 따른다.

**반환 값**

access level

### getPrgName

```java
public static java.lang.String getPrgName()
```

프로그램의 이름을 구한다. 구해지는 이름은 ADF file에 기술된 이름이다.

**반환 값**

프로그램 이름

---

## Class ProgramExitException

```text
java.lang.Object
  +--java.lang.Throwable
    +--java.lang.Exception
      +--java.lang.RuntimeException
        +--org.kwis.msf.core.ProgramExitException
```

*All Implemented Interfaces: java.io.Serializable*

```java
public class ProgramExitException extends java.lang.RuntimeException
```

등록된 thread에게 특정 프로그램이 종료되었음을 알리는 exception

생성자 상세 설명 ProgramExitException public ProgramExitException() ProgramExitException object를 생성 ProgramExitException public ProgramExitException(java.lang.String s) message를 가지고 ProgramExitException object를 생성

---

## Class Shared

```text
java.lang.Object
  +--org.kwis.msf.core.Shared
```

```java
public class Shared extends java.lang.Object
```

프로그램간에 memory shared를 제공하는 클래스 이다.. shared buffer의 size는 create시 정해 줄 수 있고, shared buffer를 사용하는 모든 프로그램이 종료되면 자동으로 free된다.

*Methods inherited from class java.lang.Throwable: fillInStackTrace, getLocalizedMessage, getMessage, printStackTrace, printStackTrace, printStackTrace, toString*

*Methods inherited from class java.lang.Object: clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait*

*Methods inherited from class java.lang.Object: clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 생성자 상세

생성자 없음

## 메서드 상세

### createBuf

```java
public static byte[] createBuf(String name, int size)
```

네임(name) 공유 버퍼를 create한다. 공유 버퍼는 byte array이며 여러 개 create될 수 있다. 생성될 수 있는 공유버퍼의 수는 플랫폼 종속적이다. create된 buf는 이 buf를 사용하는 모든 프로그램이 죽으면 자동적으로 삭제된다. 공유버퍼에 저장될 정보의 타입은 MIME type을 버퍼선두에 저장함으로써 구분한다

**매개 변수**

- `name` - 생성시킬 공유버퍼의 이름
- `size` - 생성시킬 byte array 버퍼의 크기

**반환 값**

성공이면 생성된 buf를 돌려주고, 이미 생성된 버퍼가 존재 하거나, 더 이상 공유버퍼를 생성할 수 없으면 null을 돌려준다.

### getBuf

```java
public static byte[] getBuf(String name)
```

shared 버퍼를 얻는다.

**매개 변수**

- `name` - 얻어올 공유버퍼의 이름

**반환 값**

성공이면 공유버퍼, 이미 생성된 shared buffer가 없으면 null을 돌려줌

### resizeBuf

```java
public static byte[] resizeBuf(byte[] sharedBuf,int size)
```

공유버퍼의 크기를 변경한다. 기존의 공유버퍼보다 크기가 커지면 기존의 공유버퍼 내용이 크기가 변경된 공유버퍼로 복사되고 나머지는 0으로 채워진다. 기존의 공유버퍼보다 크기가 작아지면 기존의 공유버퍼 내용 중 변경된 공유버퍼 크기만큼만 복사된다. 크기가 변경되어 반환되는 공유버퍼는 새로운 object가 할당되어 반환되는 것이므로, 기존의 공유버퍼 object를 가지고 있는 프로그램들은 공유버퍼를 새로 얻어가야 한다

**매개 변수**

- `sharedBuf` - 크기를 변경시킬 공유버퍼 참조자(reference)
- `size` - 변경할 공유버퍼 크기

**반환 값**

크기가 변경된 공유버퍼

### destroyBuf

```java
public static void destroyBuf(byte[] sharedBuf)
```

생성된 공유 버퍼를 파괴한다. 실제로 공유 버퍼가 파괴되는 시점은 공유 버퍼를 공유하는 모든 프로그램이 destroyBuf()를 부르는 경우, 맨 마지막에 destroyBuf()가 불릴 때이다. 혹은 공유 버퍼를 사용하는 모든 프로그램이 죽으면 자동적으로 삭제된다.

**매개 변수**

- `sharedBuf` - 파괴시킬 공유 버퍼 참조자(reference)
