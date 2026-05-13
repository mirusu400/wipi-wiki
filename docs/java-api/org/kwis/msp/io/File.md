# Class File

`package org.kwis.msp.io`

```
java.lang.Object
  |
  +--org.kwis.msp.io.File
```

## 설명

**extends Object:**

파일에 대한 읽기/쓰기와 같은 기본적인 기능과 Stream 기능 지원을 위한 클래스입니다.

파일이름은 모두 절대경로로 되어 있습니다. 실제로는 플랫폼에서 허용하는
 디렉토리안에서 모든 파일을 만들고 지울 수 있게 되어있습니다.
 사용자입장에서는 플랫폼에서 어떤 식으로 지원하든 상관없이 절대경로로 
 사용하면 됩니다.

구분자(separator)의 경우 유닉스 시스템의 관행을 따랐습니다.
 그러므로 `"/"`를 사용하면 됩니다.

FileSystem 클래스와 마찬가지로 경로를 지정하는 메소드의 경우 접근 방법에 대한 제한이 있습니다. 
 접근방법은 아래와 같은 3가지가 있습니다.

``FileSystem.PRIVATE_ACCESS``, ``FileSystem.SHARED_ACCESS``, ``FileSystem.SYSTEM_ACCESS``

아래와 같은 메소드를 호출하기 위해서는 반드시 접근 수준을 명시해야 합니다.

- open(String, int, int)

어떤 모드로 open하느냐에 따라 열 수 있는 stream의 갯수가 제한되어 있습니다.

- Read Only모드로 open할 경우 input stream을 하나만 열 수 있고 output stream은 열 수 없습니다.
- Write Only모드로 open할 경우 output stream은 하나만 열 수 있고, input stream은 열 수 없습니다.
- Read/Write모드로 open할 경우 output stream은 모두 하나씩 열 수 있습니다.

File 메소드 중에서는 low level로 보다 빠른 접근을 가능하게 하는 API가 있습니다.

- ``read(byte[])``
- ``read(byte[], int, int)``
- ``write(byte[])``
- ``write(byte[], int, int)``
- ``write(int)``
- ``seek(int)``
- ``sizeOf()``

등이 바로 그런 API입니다.

`openInputStream()`,
 `openOutputStream()`,
 `openDataInputStream()`,
 `openDataOutputStream()`
 을 이용해서 파일에서 읽고 파일에 쓰는 것 보다 빠르게 접근할 수 있습니다.

## 필드 요약

- `protected  int maxInputStream` — 열 수 있는 최대 InputStream 갯수
- `protected  int maxOutputStream` — 열 수 있는 최대 OutputStream 갯수
- `static int READ_ONLY` — 읽기만 할 때 쓰는 옵션
- `static int READ_WRITE` — 읽기와 쓰기를 동시에 하기 위한 옵션
- `static int WRITE` — 기존의 파일이 있으면 파일의 제일 끝부터 쓰기 시작하기 위한 옵션
- `static int WRITE_TRUNC` — 기존의 파일이 있으면 크기를 0으로 만들고 열기위한 옵션

## 생성자 요약

- File ( String filename,
 int mode) 응용프로그램 자신만의 디렉토리에 지정된 파일을 생성합니다.
- File ( String filename,
 int mode,
 int flag) 파일을 생성합니다.

## 메서드 요약

- `void close ()` — 파일을 닫습니다.
- `DataInputStream openDataInputStream ()` — DataInputStream 을 가져옵니다.
- `DataOutputStream openDataOutputStream ()` — DataOutputStream 을 가져옵니다.
- `InputStream openInputStream ()` — InputStream 을 가져옵니다.
- `OutputStream openOutputStream ()` — OutputStream 을 가져옵니다.
- `int read (byte[] buf)` — input stream으로 부터 데이타를 읽어 들입니다.
- `int read (byte[] buf, int off, int len)` — input stream으로 부터 데이타를 len 바이트수만큼 읽어 들입니다.
- `void seek (int pos)` — 파일 포인터를 특정 위치로 옮깁니다.
- `int sizeOf ()` — 파일의 크기를 알려줍니다.
- `int write (byte[] buf)` — 파일에 buf 에 들어 있는 데이타를 buf 의 길이만큼 씁니다.
- `int write (byte[] buf, int off, int len)` — 파일에 buf 에 들어 있는 데이타를 off 부터 시작해서 len 만큼 씁니다.
- `int write (int b)` — 파일에 한 바이트만 쓸 때 사용합니다.

## 필드 상세

### maxInputStream

```java
protected int maxInputStream
```

- 열 수 있는 최대 InputStream 갯수

### maxOutputStream

```java
protected int maxOutputStream
```

- 열 수 있는 최대 OutputStream 갯수

### READ_ONLY

```java
public static final int READ_ONLY
```

- 읽기만 할 때 쓰는 옵션

### WRITE

```java
public static final int WRITE
```

- 기존의 파일이 있으면 파일의 제일 끝부터 쓰기 시작하기 위한 옵션

### WRITE_TRUNC

```java
public static final int WRITE_TRUNC
```

- 기존의 파일이 있으면 크기를 0으로 만들고 열기위한 옵션

### READ_WRITE

```java
public static final int READ_WRITE
```

- 읽기와 쓰기를 동시에 하기 위한 옵션

### File

```java
public File(String filename,
            int mode)
     throws IOException
```

**Parameters:**
- `mode` - `READ_ONLY`, `WRITE`,`WRITE_TRUNC`, `READ_WRITE`중 하나

**Throws:**
- `IOException` - 파일을 열 수 없을 경우

**See Also:**
- ``FileSystem``

### File

```java
public File(String filename,
            int mode,
            int flag)
     throws IOException,
            SecurityException
```

**Parameters:**
- `flag` - ``FileSystem.PRIVATE_ACCESS``, ``FileSystem.SHARED_ACCESS``, ``FileSystem.SYSTEM_ACCESS``중 하나

**Throws:**
- `SecurityException` - 접근할 수 없는 디렉토리를 접근할려고 할려고할 경우

**See Also:**
- ``FileSystem``

### openInputStream

```java
public InputStream openInputStream()
                            throws IOException
```

**Returns:**
- 파일에 대한 `InputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `InputStream`이 열려 있을 경우

**See Also:**
- ``InputStream``

### openDataInputStream

```java
public DataInputStream openDataInputStream()
                                    throws IOException
```

**Returns:**
- 파일에 대한 `DataInputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `InputStream`이 열려 있을 경우

**See Also:**
- ``DataInputStream``

### openOutputStream

```java
public OutputStream openOutputStream()
                              throws IOException
```

**Returns:**
- 파일에 대한 `OutputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `OutputStream`이 열려 있을 경우

**See Also:**
- ``OutputStream``

### openDataOutputStream

```java
public DataOutputStream openDataOutputStream()
                                      throws IOException
```

**Returns:**
- 파일에 대한 `DataOutputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `OutputStream`이 열려 있을 경우

**See Also:**
- ``DataOutputStream``

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` - 파일을 제대로 닫을 수 없을 경우

### write

```java
public int write(int b)
          throws IOException
```

**Parameters:**
- `b` - 쓸 한 바이트

**Throws:**
- `IOException` - `close`함수로 닫혀진 `File`에서 write하는 경우이거나, 제대로 쓸 수 없을 경우

### write

```java
public int write(byte[] buf)
          throws IOException,
                 NullPointerException
```

**Parameters:**
- `buf` - 실제 데이타가 들어있는 byte array

**Throws:**
- `NullPointerException` - `buf`가 `null`인 경우

### write

```java
public int write(byte[] buf,
                 int off,
                 int len)
          throws IOException,
                 NullPointerException
```

**Parameters:**
- `len` - 실제로 쓸 데이타 크기

**Throws:**
- `IOException` - `buf`가 `null`인 경우

### read

```java
public int read(byte[] buf)
         throws IOException,
                NullPointerException
```

**Parameters:**
- `buf` - 읽은 데이타를 담을 바이트 배열

**Returns:**
- 읽은 바이트수 또는 한 바이트도 읽기전에 EOF를 만나면 -1

**Throws:**
- `NullPointerException` - `buf`가 `null`인 경우

### read

```java
public int read(byte[] buf,
                int off,
                int len)
         throws IOException,
                NullPointerException
```

**Parameters:**
- `len` - 얼마만큼 읽을 것인가를 나타냅니다.

**Returns:**
- 읽은 바이트수 또는 한 바이트도 읽기전에 EOF를 만나면 -1

**Throws:**
- `NullPointerException` - `buf`가 `null`인 경우

### seek

```java
public void seek(int pos)
          throws IOException
```

**Parameters:**
- `pos` - 옮길 파일 포인터 위치, 반드시 파일의 처음부터의 절대 값이여야합니다.

**Throws:**
- `IOException` - 파일 handle이 제대로 세팅되지 않았거나 파일 포인터를 옮기는 도중 에러가 발생했을 경우

### sizeOf

```java
public int sizeOf()
           throws IOException
```

**Returns:**
- 파일의 크기

**Throws:**
- `IOException` - 파일 handle이 제대로 세팅되지 않았거나 크기를 읽어 오는도중 에러가 발생했을 경우

## 생성자 상세

### File

```java
public File(String filename,
            int mode)
     throws IOException
```

**Parameters:**
- `mode` - `READ_ONLY`, `WRITE`,`WRITE_TRUNC`, `READ_WRITE`중 하나

**Throws:**
- `IOException` - 파일을 열 수 없을 경우

**See Also:**
- ``FileSystem``

### File

```java
public File(String filename,
            int mode,
            int flag)
     throws IOException,
            SecurityException
```

**Parameters:**
- `flag` - ``FileSystem.PRIVATE_ACCESS``, ``FileSystem.SHARED_ACCESS``, ``FileSystem.SYSTEM_ACCESS``중 하나

**Throws:**
- `SecurityException` - 접근할 수 없는 디렉토리를 접근할려고 할려고할 경우

**See Also:**
- ``FileSystem``

### openInputStream

```java
public InputStream openInputStream()
                            throws IOException
```

**Returns:**
- 파일에 대한 `InputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `InputStream`이 열려 있을 경우

**See Also:**
- ``InputStream``

### openDataInputStream

```java
public DataInputStream openDataInputStream()
                                    throws IOException
```

**Returns:**
- 파일에 대한 `DataInputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `InputStream`이 열려 있을 경우

**See Also:**
- ``DataInputStream``

### openOutputStream

```java
public OutputStream openOutputStream()
                              throws IOException
```

**Returns:**
- 파일에 대한 `OutputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `OutputStream`이 열려 있을 경우

**See Also:**
- ``OutputStream``

### openDataOutputStream

```java
public DataOutputStream openDataOutputStream()
                                      throws IOException
```

**Returns:**
- 파일에 대한 `DataOutputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `OutputStream`이 열려 있을 경우

**See Also:**
- ``DataOutputStream``

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` - 파일을 제대로 닫을 수 없을 경우

### write

```java
public int write(int b)
          throws IOException
```

**Parameters:**
- `b` - 쓸 한 바이트

**Throws:**
- `IOException` - `close`함수로 닫혀진 `File`에서 write하는 경우이거나, 제대로 쓸 수 없을 경우

### write

```java
public int write(byte[] buf)
          throws IOException,
                 NullPointerException
```

**Parameters:**
- `buf` - 실제 데이타가 들어있는 byte array

**Throws:**
- `NullPointerException` - `buf`가 `null`인 경우

### write

```java
public int write(byte[] buf,
                 int off,
                 int len)
          throws IOException,
                 NullPointerException
```

**Parameters:**
- `len` - 실제로 쓸 데이타 크기

**Throws:**
- `IOException` - `buf`가 `null`인 경우

### read

```java
public int read(byte[] buf)
         throws IOException,
                NullPointerException
```

**Parameters:**
- `buf` - 읽은 데이타를 담을 바이트 배열

**Returns:**
- 읽은 바이트수 또는 한 바이트도 읽기전에 EOF를 만나면 -1

**Throws:**
- `NullPointerException` - `buf`가 `null`인 경우

### read

```java
public int read(byte[] buf,
                int off,
                int len)
         throws IOException,
                NullPointerException
```

**Parameters:**
- `len` - 얼마만큼 읽을 것인가를 나타냅니다.

**Returns:**
- 읽은 바이트수 또는 한 바이트도 읽기전에 EOF를 만나면 -1

**Throws:**
- `NullPointerException` - `buf`가 `null`인 경우

### seek

```java
public void seek(int pos)
          throws IOException
```

**Parameters:**
- `pos` - 옮길 파일 포인터 위치, 반드시 파일의 처음부터의 절대 값이여야합니다.

**Throws:**
- `IOException` - 파일 handle이 제대로 세팅되지 않았거나 파일 포인터를 옮기는 도중 에러가 발생했을 경우

### sizeOf

```java
public int sizeOf()
           throws IOException
```

**Returns:**
- 파일의 크기

**Throws:**
- `IOException` - 파일 handle이 제대로 세팅되지 않았거나 크기를 읽어 오는도중 에러가 발생했을 경우

## 메서드 상세

### openInputStream

```java
public InputStream openInputStream()
                            throws IOException
```

**Returns:**
- 파일에 대한 `InputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `InputStream`이 열려 있을 경우

**See Also:**
- ``InputStream``

### openDataInputStream

```java
public DataInputStream openDataInputStream()
                                    throws IOException
```

**Returns:**
- 파일에 대한 `DataInputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `InputStream`이 열려 있을 경우

**See Also:**
- ``DataInputStream``

### openOutputStream

```java
public OutputStream openOutputStream()
                              throws IOException
```

**Returns:**
- 파일에 대한 `OutputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `OutputStream`이 열려 있을 경우

**See Also:**
- ``OutputStream``

### openDataOutputStream

```java
public DataOutputStream openDataOutputStream()
                                      throws IOException
```

**Returns:**
- 파일에 대한 `DataOutputStream`

**Throws:**
- `IOException` - 파일이 아직 열리지 않았거나 이미 `OutputStream`이 열려 있을 경우

**See Also:**
- ``DataOutputStream``

### close

```java
public void close()
           throws IOException
```

**Throws:**
- `IOException` - 파일을 제대로 닫을 수 없을 경우

### write

```java
public int write(int b)
          throws IOException
```

**Parameters:**
- `b` - 쓸 한 바이트

**Throws:**
- `IOException` - `close`함수로 닫혀진 `File`에서 write하는 경우이거나, 제대로 쓸 수 없을 경우

### write

```java
public int write(byte[] buf)
          throws IOException,
                 NullPointerException
```

**Parameters:**
- `buf` - 실제 데이타가 들어있는 byte array

**Throws:**
- `NullPointerException` - `buf`가 `null`인 경우

### write

```java
public int write(byte[] buf,
                 int off,
                 int len)
          throws IOException,
                 NullPointerException
```

**Parameters:**
- `len` - 실제로 쓸 데이타 크기

**Throws:**
- `IOException` - `buf`가 `null`인 경우

### read

```java
public int read(byte[] buf)
         throws IOException,
                NullPointerException
```

**Parameters:**
- `buf` - 읽은 데이타를 담을 바이트 배열

**Returns:**
- 읽은 바이트수 또는 한 바이트도 읽기전에 EOF를 만나면 -1

**Throws:**
- `NullPointerException` - `buf`가 `null`인 경우

### read

```java
public int read(byte[] buf,
                int off,
                int len)
         throws IOException,
                NullPointerException
```

**Parameters:**
- `len` - 얼마만큼 읽을 것인가를 나타냅니다.

**Returns:**
- 읽은 바이트수 또는 한 바이트도 읽기전에 EOF를 만나면 -1

**Throws:**
- `NullPointerException` - `buf`가 `null`인 경우

### seek

```java
public void seek(int pos)
          throws IOException
```

**Parameters:**
- `pos` - 옮길 파일 포인터 위치, 반드시 파일의 처음부터의 절대 값이여야합니다.

**Throws:**
- `IOException` - 파일 handle이 제대로 세팅되지 않았거나 파일 포인터를 옮기는 도중 에러가 발생했을 경우

### sizeOf

```java
public int sizeOf()
           throws IOException
```

**Returns:**
- 파일의 크기

**Throws:**
- `IOException` - 파일 handle이 제대로 세팅되지 않았거나 크기를 읽어 오는도중 에러가 발생했을 경우
