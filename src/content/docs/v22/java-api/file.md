---
title: "3.1.2. 파일"
---

---

## Class File

```text
java.lang.Object
  +--org.kwis.msp.io.File
```

*All Implemented Interfaces: Connection, InputConnection, OutputConnection, StreamConnection*

```java
public class File extends Object implements StreamConnection
```

파일에 대한 읽기/쓰기와 같은 기본적인 기능과 Stream 기능 지원을 위한 클래스이다. 파일이름은 모두 절대경로로 되어 있다. 실제로는 플랫폼에서 허용하는 디렉토리 안에서 모든 파일을 만들고 지울 수 있게 되어있다. 사용자입장에서는 플랫폼에서 어떤 식으로 지원하든 상관없이 절대경로로 사용하면 된다. 구분자(separator)의 경우 유닉스 시스템의 관행을 따랐다. 그러므로 "/"를 사용하면 된다. FileSystem 클래스와 마찬가지로 경로를 지정하는 메소드의 경우 접근 방법에 대한 제한이 있다. 접근방법은 아래와 같은 3가지가 있다. FileSystem.PRIVATE_ACCESS, FileSystem.SHARED_ACCESS, FileSystem.SYSTEM_ACCESS 아래와 같은 메소드를 호출하기 위해서는 반드시 접근 수준을 명시해야 한다. open(String, int, int) 어떤 모드로 open하느냐에 따라 열 수 있는 stream의 개수가 제한되어 있다. Read Only모드로 open할 경우 input stream을 하나만 열 수 있고 output stream은 열 수 없다. Write Only모드로 open할 경우 output stream은 하나만 열 수 있고, input stream은 열 수 없다. Read/Write모드로 open할 경우 output stream은 모두 하나씩 열 수 있다. File 메소드 중에서는 low level로 보다 빠른 접근을 가능하게 하는 API가 있다. read(byte[]) read(byte[], int, int) write(byte[]) write(byte[], int, int) write(int) seek(int) sizeOf() 등이 바로 그런 API이다. openInputStream(), openOutputStream(), openDataInputStream(), openDataOutputStream() 을 이용해서 파일에서 읽고 파일에 쓰는 것 보다 빠르게 접근할 수 있다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 필드 상세

### maxInputStream

```java
protected int maxInputStream
```

열 수 있는 최대 InputStream 개수

### maxOutputStream

```java
protected int maxOutputStream
```

열 수 있는 최대 OutputStream 개수

### READ_ONLY

```java
public static final int READ_ONLY
```

읽기만 할 때 쓰는 옵션

### WRITE

```java
public static final int WRITE
```

기존의 파일이 있으면 파일의 제일 끝부터 쓰기 시작하기 위한 옵션

### WRITE_TRUNC

```java
public static final int WRITE_TRUNC
```

기존의 파일이 있으면 크기를 0으로 만들고 열기 위한 옵션

### READ_WRITE

```java
public static final int READ_WRITE
```

읽기와 쓰기를 동시에 하기 위한 옵션

## 생성자 상세

### File

```java
public File(String filename, int mode) throws IOException
```

응용프로그램 자신만의 디렉토리에 지정된 파일을 생성한다. 파일이름은 구분자("/")로 시작하는 것과 없이 바로 파일이름으로 시작하는 것과 차이가 없다. 파일을 생성할 때는 다음과 같은 모드로 열 수 있다.이때 모드를 지정할 수 있으며 다음과 같은 방식으로 열게 된다. READ_ONLY read only로 읽다. 만약 쓰려고 하면 exception이 발생한다. WRITE 현재 파일을 유지하고 파일 포인터가 제일 뒤에 위치하게 된다. WRITE_TRUNC 파일이 truncation된다. 즉, 파일을 여는 순간 파일 길이는 0으로 된다. READ_WRITE read와 write를 동시에 할 수 있다. 위 모드 외에 다른 모드로 열고자 하면 IllegalArgumentException을 발생시킨다.

**매개 변수**

- `filename` - 열고자 하는 파일의 절대 경로
- `mode` - READ_ONLY, WRITE,WRITE_TRUNC, READ_WRITE중 하나 Throws
- `IOException` - 파일을 열 수 없을 경우
- `IllegalArgumentException` - READ_ONLY, WRITE, WRITE_TRUNC, READ_WRITE 이외의 모드로 얻고자 할 경우

**참고 항목**

FileSystem

### File

```java
public File(String filename, int mode, int flag) throws IOException
```

파일을 생성한다. 파일이름은 구분자("/")로 시작하는 것과 없이 바로 파일이름으로 시작하는 것과 차이가 없다. 파일을 생성할 때는 다음과 같은 모드로 열 수 있다. READ_ONLY read only로 읽다. 만약 쓰려고 하면 exception이 발생한다. WRITE 현재 파일을 유지하고 파일 포인터가 제일 뒤에 위치하게 된다. WRITE_TRUNC 파일이 truncation된다. 즉, 파일을 여는 순간 파일 길이는 0으로 된다. READ_WRITE read와 write를 동시에 할 수 있다. 위 모드 외에 다른 모드로 열고자 하면 IllegalArgumentException을 발생시킨다.

**매개 변수**

- `filename` - 열고자 하는 파일의 절대 경로
- `mode` - READ_ONLY, WRITE,WRITE_TRUNC, READ_WRITE중 하나
- `flag` - FileSystem.PRIVATE_ACCESS, FileSystem.SHARED_ACCESS, FileSystem.SYSTEM_ACCESS중 하나 Throws
- `IOException` - 파일을 열 수 없을 경우
- `SecurityException` - 접근할 수 없는 디렉토리를 접근하려고 할 경우
- `IllegalArgumentException` - READ_ONLY, WRITE, WRITE_TRUNC, READ_WRITE 이외의 모드로 열고자 할 경우

**참고 항목**

FileSystem

## 메서드 상세

### openInputStream

```java
public InputStream openInputStream() throws IOException
```

InputStream을 가져온다. 열 수 있는 InputStream개수는 DataInputStream포함 최대 한 개이다. Specified by openInputStream in interface InputConnection

**반환 값**

파일에 대한 InputStream Throws IOException 파일이 아직 열리지 않았거나 이미 InputStream이 열려 있을 경우

**참고 항목**

InputStream

### openDataInputStream

```java
public DataInputStream openDataInputStream() throws IOException
```

DataInputStream을 가져온다. 열 수 있는 DataInputStream개수는 InputStream포함해서 최대 한 개이다. Specified by openDataInputStream in interface InputConnection

**반환 값**

파일에 대한 DataInputStream Throws IOException 파일이 아직 열리지 않았거나 이미 InputStream이 열려 있을 경우

**참고 항목**

DataInputStream

### openOutputStream

```java
public OutputStream openOutputStream() throws IOException
```

OutputStream을 가져온다. 열 수 있는 OutputStream개수는 DataOutputStream포함 최대 한 개이다. Specified by openOutputStream in interface OutputConnection

**반환 값**

파일에 대한 OutputStream Throws IOException 파일이 아직 열리지 않았거나 이미 OutputStream이 열려 있을 경우

**참고 항목**

OutputStream

### openDataOutputStream

```java
public DataOutputStream openDataOutputStream() throws IOException
```

DataOutputStream을 가져온다. 열 수 있는 DataOutputStream개수는 OutputStream포함해서 최대 한 개이다. Specified by openDataOutputStream in interface OutputConnection

**반환 값**

파일에 대한 DataOutputStream Throws IOException 파일이 아직 열리지 않았거나 이미 OutputStream이 열려 있을 경우

**참고 항목**

DataOutputStream

### close

```java
public void close() throws IOException
```

파일을 닫다. 이미 닫혀 있어도 Exception을 발생하지 않는다. Specified by close in interface Connection Throws IOException 파일을 제대로 닫을 수 없을 경우

### write

```java
public int write(int b) throws IOException
```

파일에 한 바이트만 쓸 때 사용한다.

**매개 변수**

- `b` - 쓸 한 바이트

**반환 값**

실제 데이터를 쓴 바이트 수 Throws IOException close함수로 닫혀진 File에서 write하는 경우이거나, 제대로 쓸 수 없을 경우

### write

```java
public int write(byte[] buf) throws IOException
```

파일에 buf에 들어 있는 데이타를 buf의 길이만큼 쓴다. buf가 null일 경우에 NullPointerException을 발생시킨다.

**매개 변수**

- `buf` - 실제 데이타가 들어있는 byte array

**반환 값**

실제 데이터를 쓴 바이트 수 Throws IOException close함수로 닫혀진 File에서 write하는 경우이거나, 제대로 쓸 수 없을 경우 NullPointerException buf가 null인 경우

### write

```java
public int write(byte[] buf, int off, int len) throws IOException
```

파일에 buf에 들어 있는 데이타를 off부터 시작해서 len만큼 쓴다. buf가 null일 경우에 NullPointerException을 발생시킨다.

**매개 변수**

- `buf` - 실제 데이타가 들어있는 byte array
- `off` - 쓸 데이타가 들어있는 위치
- `len` - 실제로 쓸 데이타 크기

**반환 값**

실제 데이터를 쓴 바이트 수 Throws IOException close함수로 닫혀진 File에서 write하는 경우이거나, 제대로 쓸 수 없을 경우 NullPointerException buf가 null인 경우

### read

```java
public int read() throws IOException
```

input stream으로 부터 1바이트를 읽어 들이다. 읽을 것이 없으면, 즉 EOF의 경우 - 1을 반환한다.

**반환 값**

읽은 바이트, 읽을 것이 없으면 -1 Throws IOException 읽는 도중 에러가 발생했을 경우

### read

```java
public int read(byte[] buf) throws IOException
```

input stream으로 부터 데이타를 읽어 들이다. buf의 size만큼 읽어 들이다. 만약 파일의 끝까지 모두 읽었을 경우 그 읽은 만큼만 buf에 저장하고, 저장된 개수를 돌려준다. 그리고, 다음 read시에 -1을 돌려준다.

**매개 변수**

- `buf` - 읽은 데이타를 담을 바이트 배열

**반환 값**

읽은 바이트 수 또는 한 바이트도 읽기 전에 EOF를 만나면 -1 Throws IOException close함수로 닫혀진 File에서 write하는 경우이거나, 제대로 읽을 수 없을 경우 NullPointerException buf가 null인 경우

### read

```java
public int read(byte[] buf, int off, int len) throws IOException
```

input stream으로 부터 데이타를 len 바이트 수만큼 읽어 들이다. len 만큼 읽지 못하고 EOF를 만나면 읽은 바이트 수만큼을 buf에 저장해서 돌려준다.

**매개 변수**

- `buf` - 읽은 데이타를 담을 바이트 배열
- `off` - buf의 어디서부터 읽은 데이타를 저장할 건지를 정하는 offset
- `len` - 얼마만큼 읽을 것인가를 나타낸다.

**반환 값**

읽은 바이트 수 또는 한 바이트도 읽기 전에 EOF를 만나면 -1 Throws IOException close함수로 닫혀진 File에서 write하는 경우이거나, 제대로 읽을 수 없을 경우 NullPointerException buf가 null인 경우 IndexOutOfBoundsException len이 0이하이거나. offset이 음수이거나 offset + len 값이 buf의 범위를 벗어난 경우

### seek

```java
public void seek(int pos) throws IOException
```

파일 포인터를 특정 위치로 옮긴다.

**매개 변수**

- `pos` - 옮길 파일 포인터 위치, 반드시 파일의 처음부터의 절대 값이어야 한다. Throws
- `IOException` - 파일 handle이 제대로 세팅되지 않았거나 파일 포인터를 옮기는 도중 에러가 발생했을 경우
- `IllegalArgumentException` - pos가 음수이거나 유효하지 않는 값일 경우 sizeOf

### sizeOf

```java
public int sizeOf() throws IOException
```

파일의 크기를 알려준다.

**반환 값**

파일의 크기 Throws IOException 파일 handle이 제대로 세팅되지 않았거나 크기를 읽어 오는 도중 에러가 발생했을 경우

### tell

```java
public int tell() throws IOException
```

파일 포인터의 현재 위치를 얻는다.

**반환 값**

파일의 처음 위치로부터 현재 위치까지 오프셋 값 Throws IOException 파일 handle이 제대로 세팅되지 않았거나 파일 포인터를 읽는 도중 에러가 발생했을 경우

---

## Class FileSystem

```text
java.lang.Object
  +--org.kwis.msp.io.FileSystem
```

```java
public final class FileSystem extends Object
```

FileSystem 클래스는 파일에 관련된 생성/삭제/이름 바꾸기와 같은 일반적인 기능을 정의하고 있다. 모든 파일 또는 디렉토리 경로는 모두 절대적인 경로이다. 그렇다고 해서 사용자가 임의로 절대경로를 지정할 수는 없다. 아래에 설명하는 3가지 접근 방식으로만 지정할 수 있고, 그에 따라 시스템에서 절대경로를 지정해 준다. 파일에 접근하는 방식은 모두 3가지가 있다. 응용프로그램 자신만이 쓰는 디렉토리로의 접근은 PRIVATE_ACCESS 플래그를 사용하고, 다른 프로그램과 공유할 디렉토리로 접근 하고자 할 때는 SHARED_ACCESS를 사용한다. 그리고 마지막으로 시스템 디렉토리로 접근하고자 할 때는 SYSTEM_ACCESS 방식으로 접근하면 된다. 경로를 지정하는 모든 메소드는 접근방식을 지정해야만 한다. 아래는 접근 방식을 지정하는 메소드들이다. exists(java.lang.String, int) isDirectory(java.lang.String, int) isFile(java.lang.String, int) list(java.lang.String, int) mkdir(java.lang.String, int) rmdir(java.lang.String, int) remove(java.lang.String, int) rename(java.lang.String, int) 만약 응용프로그램 자신만의 디렉토리에 있는 test라는 파일이 존재하는 지 여부를 알고 싶다면 다음과 같이 할 수 있다. if (exists("test", PRIVATE_ACCESS)){ System.err.println("test exists"); }; 또는 아래와 같이 지정하지 않을 경우는 기본값으로 자신만의 디렉토리에서 찾게 된다. if (exists("test")){ System.err.println("test exists"); }; 위의 예에서 보듯이 test라는 파일의 존재유무를 확인하고자 할 때 test라는 파일 이름은 시스템이 만들어주는 절대경로에서 찾게 된다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 필드 상세

PRIVATE_ACCESS public static final int PRIVATE_ACCESS 응용프로그램 자신만이 접근할 수 있는 디렉토리를 접근하고자 할 때 쓰는 플래그. 1로 정의되어 있다. SHARED_ACCESS public static final int SHARED_ACCESS 공유할 수 있는 디렉토리를 접근하고자 할 때 쓰는 플래그. 공유하고자 하는 디렉토리는 이미 프로그램이 설치될 때 응용 프로그램 명세 파일(Jlet Descriptor)파일에 명시된 데로 지정되며, 사용자가 임의로 공유 디렉토리를 변경할 수는 없다. 2로 정의되어 있다. SYSTEM_ACCESS public static final int SYSTEM_ACCESS 시스템 응용프로그램이 사용하는 디렉토리를 접근하고자 할 때 쓰는 플래그. 공유하고자 하는 디렉토리는 이미 프로그램이 설치될 때 응용 프로그램 명세 파일(Jlet Descriptor)파일에 명시된 데로 지정되며 사용자가 임의로 공유 디렉토리를 변경할 수는 없다. 3으로 정의되어 있다. MAX_FILENAME_LENGTH public static final int MAX_FILENAME_LENGTH filename길이에 제한이 있다. 모든 파일이름이 들어가는 API는 파일 이름이 MAX_FILENAME_LENGTH보다 길면 IOException을 발생시킨다.

## 생성자 상세

FileSystem public FileSystem()

## 메서드 상세

### getMaxFilenameLength

```java
public static int getMaxFilenameLength()
```

사용할 수 있는 파일이름의 최대길이를 확인한다.

**반환 값**

파일이름 최대 길이

### list

```java
public static Vector list(String dirname) throws IOException
```

응용프로그램 자신만의 디렉토리 안에 있는 파일과 디렉토리를 모두 보여준다. dirname이 null일 경우 NullPointerException을 발생시킨다. dirname이 MAX_FILENAME_LENGTH보다 길 경우 IOException을 발생시킨다.

**매개 변수**

- `dirname` - 디렉토리 이름

**반환 값**

dirname아래에 있는 모든 파일이름과 디렉토리 이름 Throws IOException 디렉토리가 존재하지 않을 경우 NullPointerException dirname이 null일 경우

### list

```java
public static Vector list(String dirname, int flag) throws IOException
```

지정된 디렉토리 안에 있는 파일과 디렉토리를 모두 보여준다. dirname이 null일 경우 NullPointerException을 발생시킨다. dirname이 MAX_FILENAME_LENGTH보다 길 경우 IOException을 발생시킨다.

**매개 변수**

- `dirname` - 디렉토리 이름
- `flag` - 접근하고자 하는 디렉토리

**반환 값**

dirname아래에 있는 모든 파일 이름과 디렉토리 이름 Throws SecurityException 허가되지 않은 디렉토리를 접근하려고 할 경우. IOException dirname이 존재하지 않을 경우 NullPointerException dirname이 null일 경우

### exists

```java
public static boolean exists(String name) throws IOException
```

응용프로그램 자신만의 디렉토리의 파일이나 디렉토리가 존재하는지를 확인한다. name이 null일 경우 NullPointerException을 발생시킨다. name이 MAX_FILENAME_LENGTH보다 길 경우 IOException을 발생시킨다.

**매개 변수**

- `name` - 파일이나 디렉토리 이름

**반환 값**

존재하면 true, 존재하지 않으면 false Throws NullPointerException name이 null일 경우

### exists

```java
public static boolean exists(String name, int flag) throws IOException
```

지정된 디렉토리아래 파일이나 디렉토리가 존재하는 지를 확인한다. name이 null일 경우 NullPointerException을 발생시킨다. name이 MAX_FILENAME_LENGTH보다 길 경우 IOException을 발생시킨다.

**매개 변수**

- `name` - 파일이나 디렉토리 이름
- `flag` - 접근하고자 하는 디렉토리

**반환 값**

존재하면 true, 존재하지 않으면 false Throws SecurityException 접근할 수 없는 디렉토리를 접근하려고 할 경우 NullPointerException name이 null일 경우

### remove

```java
public static void remove(String filename) throws IOException
```

응용프로그램 자신만의 디렉토리의 파일을 지운다. filename이 null일 경우 NullPointerException을 발생시킨다. filename이 MAX_FILENAME_LENGTH보다 길 경우 IOException을 발생시킨다.

**매개 변수**

- `filename` - 파일 이름 Throws
- `IOException` - 파일을 지울 때 제대로 지우지 못할 경우, 파일이 존재하지 않을 경우
- `NullPointerException` - filename이 null일 경우 remove

### remove

```java
public static void remove(String filename, int flag) throws IOException
```

파일을 지운다. filename이 null일 경우 NullPointerException을 발생시킨다. filename이
- `MAX_FILENAME_LENGTH보다` - 길 경우 IOException을 발생시킨다.

**매개 변수**

- `filename` - 파일 이름
- `flag` - 접근하고자 하는 디렉토리 Throws
- `SecurityException` - 접근할 수 없는 디렉토리를 접근하려고 할 경우
- `IOException` - 파일을 지울 때 제대로 지우지 못할 경우, 파일이 존재하지 않을 경우
- `NullPointerException` - filename이 null일 경우 mkdir

### mkdir

```java
public static void mkdir(String dirname) throws IOException
```

응용프로그램 자신만의 디렉토리에 디렉토리를 만든다. dirname이 null일 경우
- `NullPointerException을` - 발생시킨다. dirname이 MAX_FILENAME_LENGTH보다 길 경우 IOException을 발생시킨다.

**매개 변수**

- `dirname` - 디렉토리 이름 Throws
- `IOException` - 디렉토리를 만들 수 없을 경우나 디렉토리가 이미 존재할 경우, 또는 파일 이름 길이가 최대값을 넘어 갈 경우
- `NullPointerException` - dirname이 null일 경우 mkdir

### mkdir

```java
public static void mkdir(String dirname, int flag) throws IOException
```

디렉토리를 만든다. dirname이 null일 경우 NullPointerException을 발생시킨다.
- `dirname이` - MAX_FILENAME_LENGTH보다 길 경우 IOException을 발생시킨다.

**매개 변수**

- `dirname` - 디렉토리 이름
- `flag` - 접근하고자 하는 디렉토리 Throws
- `SecurityException` - 접근할 수 없는 디렉토리를 접근하려고 할 경우
- `IOException` - 디렉토리를 만들 수 없을 경우나 디렉토리가 이미 존재할 경우, 또는 파일 이름 길이가 최대값을 넘어 갈 경우
- `NullPointerException` - dirname이 null일 경우 rmdir

### rmdir

```java
public static void rmdir(String dirname) throws IOException
```

응용프로그램 자신만의 디렉토리에 있는 디렉토리를 지운다. dirname이 null일 경우
- `NullPointerException을` - 발생시킨다. dirname이 MAX_FILENAME_LENGTH보다 길 경우 IOException을 발생시킨다.

**매개 변수**

- `dirname` - 디렉토리 이름 Throws
- `IOException` - 디렉토리가 비어있지 않거나 디렉토리를 지울 수 없을 경우, 또는 디렉토리가 존재하지 않을 경우
- `NullPointerException` - dirname이 null일 경우 rmdir

### rmdir

```java
public static void rmdir(String dirname, int flag) throws IOException
```

디렉토리를 지운다. dirname이 null일 경우 NullPointerException을 발생시킨다.
- `dirname이` - MAX_FILENAME_LENGTH보다 길 경우 IOException을 발생시킨다.

**매개 변수**

- `dirname` - 디렉토리 이름
- `flag` - 접근하고자 하는 디렉토리 Throws
- `SecurityException` - 접근할 수 없는 디렉토리를 접근하려고 할 경우
- `IOException` - 디렉토리가 비어있지 않거나 디렉토리를 지울 수 없을 경우, 또는 디렉토리가 존재하지 않을 경우
- `NullPointerException` - dirname이 null일 경우 toCString

### toCString

```java
public static byte[] toCString(String jStr)
```

- `Java` - String을 C String으로 바꾸어 준다. Encoding방식은 ISO8859(영어)와 KSC5601(한글)이다.

**매개 변수**

- `jStr` - java String

**반환 값**

jStr을 C 문자열로 변환한 바이트 배열 Throws NullPointExcetption jStr이 null 인 경우

### available

```java
public static int available()
```

응용 프로그램이 사용할 수 있는 공간이 얼마나 남았는지 알려준다.

**반환 값**

파일 시스템 중에 사용할 수 있는 공간

### isFile

```java
public static boolean isFile(String name) throws java.io.IOException
```

응용프로그램 자신만의 디렉토리에 지정된 이름의 파일이 존재하는지 확인한다. 같은 디렉토리 아래에 같은 이름의 파일과 디렉토리는 존재할 수 없다.

**매개 변수**

- `name` - 확인하고자 하는 파일 이름

**반환 값**

name과 같은 파일이 존재하면 true, 디렉토리 이름이거나 존재하지 않으면 false Throws java.io.IOException name이 MAX_FILENAME_LENGTH보다 길 경우 NullPointerException name이 null 일 경우

### isFile

```java
public static boolean isFile(String name, int flag) throws java.io.IOException
```

지정된 이름의 파일이 존재하는지 확인한다. 같은 디렉토리 아래에 같은 이름의 파일과 디렉토리는 존재할 수 없다.

**매개 변수**

- `name` - 확인하고자 하는 파일 이름
- `flag` - 접근하고자 하는 디렉토리

**반환 값**

name과 같은 파일이 존재하면 true, 디렉토리 이름이거나 존재하지 않으면 false Throws NullPointerExcepiton name이 null일 경우 IOException name이 MAX_FILENAME_LENGTH보다 길 경우 SecurityException 접근할 수 없는 디렉토리를 접근하려고 할 경우

### isDirectory

```java
public static boolean isDirectory(String name) throws IOException
```

응용프로그램 자신만의 디렉토리에 있는 디렉토리인지를 확인한다. 같은 디렉토리 아래에 같은 이름의 파일과 디렉토리는 존재할 수 없다.

**매개 변수**

- `name` - 확인하고자 하는 디렉토리 이름

**반환 값**

name과 같은 디렉토리 이름이 존재하면 true, 파일이름이거나 존재하지 않으면 false Throws NullPointerExcepiton name이 null일 경우 IOException name이 MAX_FILENAME_LENGTH보다 길 경우

### isDirectory

```java
public static boolean isDirectory(String name, int flag) throws IOException
```

디렉토리인지를 확인한다. 같은 디렉토리 아래에 같은 이름의 파일과 디렉토리는 존재할 수 없다.

**매개 변수**

- `name` - 확인하고자 하는 디렉토리 이름
- `flag` - 접근하고자 하는 디렉토리

**반환 값**

name과 같은 디렉토리 이름이 존재하면 true, 파일이름이거나 존재하지 않으면 false Throws NullPointerExcepiton name이 null일 경우 IOException name이 MAX_FILENAME_LENGTH보다 길 경우 SecurityException 접근할 수 없는 디렉토리를 접근하려고 할 경우

### getCreationTime

```java
public static int getCreationTime(String name) throws IOException
```

응용프로그램 자신만의 디렉토리에 있는 파일의 생성시간을 알아온다. name이 만약 디렉토리일 경우는 -1을 return한다.

**매개 변수**

- `name` - 확인하고자 하는 파일이름

**반환 값**

만약 디렉토리이면 -1을, file일 경우는 생성시간 초로 표현 Throws NullPointerExcepiton name이 null일 경우 IOException name이 MAX_FILENAME_LENGTH보다 길 경우

### getCreationTime

```java
public static int getCreationTime(String name, int flag) throws IOException
```

파일의 생성시간을 알아온다.name이 만약 디렉토리일 경우는 -1을 return한다.

**매개 변수**

- `name` - 확인하고자 하는 파일이름

**반환 값**

만약 디렉토리이면 -1을, file일 경우는 생성시간 초로 표현 Throws NullPointerExcepiton name이 null일 경우 IOException name이 MAX_FILENAME_LENGTH보다 길 경우

### rename

```java
public static void rename(String oldName, String newName) throws IOException
```

응용프로그램이 개인 디렉토리 및 하부 디렉토리 내에 있는 파일의 이름을 바꾼다. 하부 디렉토리의 경우에는 상대 디렉토리 Path가 파일이름에 포함되어야 한다. oldName과 newName 화일의 디렉토리는 동일하여야 한다. oldName이나 newName이 null일 경우 NullPointerException을 발생시킨다. oldName이나 newName이 MAX_FILENAME_LENGTH보다 길 경우 IOException을 발생시킨다.

**매개 변수**

- `oldName` - 현재 이름
- `newName` - 바뀐 후 이름 Throws
- `IOException` - 바꾸는 과정에 에러가 발생할 경우
- `NullPointerException` - oldName이나 newName이 null일 경우 rename

### rename

```java
public static void rename(String oldName, String newName, int flag) throws IOException
```

파일 이름을 바꾼다. 바꾸고자 하는 파일의 현재 이름과 바뀐 후 이름은 디렉토리를 포함하는 경로가 될 수 없다. 즉 디렉토리 구분자가 포함되어서는 안 된다.

**매개 변수**

- `oldName` - 현재 이름
- `newName` - 바뀐 후 이름
- `flag` - 접근하고자 하는 디렉토리 Throws
- `NullPointerExcepiton` - oldName이나 newName이 null일 경우
- `SecurityException` - 접근할 수 없는 디렉토리를 접근하려고 할 경우.
- `IOException` - oldName, newName이 MAX_FILENAME_LENGTH 보다 길 경우
