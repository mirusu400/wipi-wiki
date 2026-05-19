---
title: "Class FileSystem"
---

`package org.kwis.msp.io`

```text
java.lang.Object
  |
  +--org.kwis.msp.io.FileSystem
```

## 설명

**extends Object:**

FileSystem 클래스는 파일에 관련된 생성/삭제/이름 바꾸기와 같은 일반적인 기능을 정의하고 있습니다.
 모든 파일 또는 디렉토리 경로는 모두 절대적인 경로입니다. 
 그렇다고 해서 사용자가 임의로 절대경로를 지정할 수는 없습니다.

아래에 설명하는 3가지 접근 방식으로만 지정할 수 있고, 그에 따라 시스템에서
 절대경로를 지정해 줍니다.

파일에 접근하는 방식은 모두 3가지가 있습니다.

- 응용프로그램 자신만이 쓰는 디렉토리로의 접근은 ``PRIVATE_ACCESS`` 플래그를 사용하고,
- 다른 프로그램과 공유할 디렉토리로 접근 하고자 할 때는 ``SHARED_ACCESS``를 사용합니다.
- 그리고 마지막으로 시스템 디렉토리로 접근하고자 할 때는 ``SYSTEM_ACCESS`` 방식으로 접근하면 됩니다.

경로를 지정하는 모든 메소드는 접근방식을 지정해야만 합니다. 아래는 접근 방식을 지정하는 메소드들입니다.

- `exists(java.lang.String, int)`
- `isDirectory(java.lang.String, int)`
- `isFile(java.lang.String, int)`
- `list(java.lang.String, int)`
- `mkdir(java.lang.String, int)`
- `rmdir(java.lang.String, int)`
- `remove(java.lang.String, int)`
- `rename(java.lang.String, int)`

만약 응용프로그램 자신만의 디렉토리에 있는 `test`라는 파일이 존재하는 지 여부를 알고 싶다면 다음과 같이 할 수 있습니다.

또는 아래와 같이 지정하지 않을 경우는 기본값으로 자신만의 디렉토리에서 
 찾게 됩니다.

위의 예에서 보듯이 test라는 파일의 존재유무를 확인하고자 할 때 test라는 파일
 이름은 시스템이 만들어주는 절대경로에서 찾게 됩니다.

## 필드 요약

- `static int MAX_FILENAME_LENGTH` — filename길이에 제한이 있습니다.
- `static int PRIVATE_ACCESS` — 응용프로그램 자신만이 접근할 수 있는 디렉토리를 접근하고자 할 때 쓰는 플래그. 1로 정의되어 있습니다.
- `static int SHARED_ACCESS` — 공유할 수 있는 디렉토리를 접근하고자 할 때 쓰는 플래그.
- `static int SYSTEM_ACCESS` — 시스템 응용프로그램이 사용하는 디렉토리를 접근하고자 할 때 쓰는 플래그.

## 생성자 요약

- FileSystem ()

## 메서드 요약

- `static int available ()` — 응용 프로그램이 사용할 수 있는 공간이 얼마나 남았는지 알려줍니다.
- `static boolean exists ( String name)` — 응용프로그램 자신만의 디렉토리의 파일이나 디렉토리가 존재하는지를 확인합니다.
- `static boolean exists ( String name, int flag)` — 지정된 디렉토리아래 파일이나 디렉토리가 존재하는 지를 확인합니다.
- `static int getCreationTime ( String name)` — 응용프로그램 자신만의 디렉토리에 있는 파일의 생성시간을 알아옵니다.
- `static int getCreationTime ( String name, int flag)` — 파일의 생성시간을 알아옵니다.
- `static int getMaxFilenameLength ()` — 사용할 수 있는 파일이름의 최대길이를 확인합니다.
- `static boolean isDirectory ( String name)` — 응용프로그램 자신만의 디렉토리에 있는 디렉토리인지를 확인합니다.
- `static boolean isDirectory ( String name, int flag)` — 디렉토리인지를 확인합니다.
- `static boolean isFile ( String name)` — 응용프로그램 자신만의 디렉토리에 지정된 이름의 파일이 존재하는지 확인한다.
- `static boolean isFile ( String name, int flag)` — 지정된 이름의 파일이 존재하는지 확인한다.
- `static Vector list ( String dirname)` — 응용프로그램 자신만의 디렉토리안에 있는 파일과 디렉토리를 모두 보여줍니다.
- `static Vector list ( String dirname, int flag)` — 지정된 디렉토리안에 있는 파일과 디렉토리를 모두 보여줍니다.
- `static void mkdir ( String dirname)` — 응용프로그램 자신만의 디렉토리에 디렉토리를 만듭니다.
- `static void mkdir ( String dirname, int flag)` — 디렉토리를 만듭니다.
- `static void remove ( String filename)` — 응용프로그램 자신만의 디렉토리의 파일을 지웁니다.
- `static void remove ( String filename, int flag)` — 파일을 지웁니다.
- `static void rename ( String oldName, String newName)` — 응용프로그램 자신만의 디렉토리내에 있는 파일의 이름을 바꿉니다.
- `static void rename ( String oldName, String newName, int flag)` — 파일 이름을 바꿉니다.
- `static void rmdir ( String dirname)` — 응용프로그램 자신만의 디렉토리에 있는 디렉토리를 지웁니다.
- `static void rmdir ( String dirname, int flag)` — 디렉토리를 지웁니다.
- `static byte[] toCString ( String jStr)` — Java String을 C String으로 바꾸어 줍니다.
- `static int totalSpace ()`

## 필드 상세

### PRIVATE_ACCESS

```java
public static final int PRIVATE_ACCESS
```

- 응용프로그램 자신만이 접근할 수 있는 디렉토리를 접근하고자 할 때 쓰는 
 플래그. 

 1로 정의되어 있습니다.

### SHARED_ACCESS

```java
public static final int SHARED_ACCESS
```

- 공유할 수 있는 디렉토리를 접근하고자 할 때 쓰는 플래그.
 공유하고자 하는 디렉토리는 이미 프로그램이 설치될 때 
 ADF 파일에 명시된데로 지정되며,
 사용자가 임의로 공유 디렉토리를 변경할 수는 없습니다.
 2로 정의되어 있습니다.

### SYSTEM_ACCESS

```java
public static final int SYSTEM_ACCESS
```

- 시스템 응용프로그램이 사용하는 디렉토리를 접근하고자 할 때 쓰는 플래그.
 공유하고자 하는 디렉토리는 이미 프로그램이 설치될 때 
 ADF파일에 명시된데로 지정되며
 사용자가 임의로 공유 디렉토리를 변경할 수는 없습니다.
 3으로 정의되어 있습니다.

### MAX_FILENAME_LENGTH

```java
public static int MAX_FILENAME_LENGTH
```

- filename길이에 제한이 있습니다.
 

모든 파일 이름이 들어가는 API는 파일 이름이 MAX_FILENAME_LENGTH보다 길면 IOException을 발생시킨다.

### FileSystem

```java
public FileSystem()
```

### getMaxFilenameLength

```java
public static int getMaxFilenameLength()
```

**Returns:**
- 파일이름 최대 길이

### list

```java
public static Vector list(String dirname)
                   throws IOException
```

**Parameters:**
- `dirname` - 디렉토리 이름

**Returns:**
- `dirname`아래에 있는 모든 파일이름과 디렉토리 이름

**Throws:**
- `IOException` - 디렉토리가 존재하지 않을 경우

### list

```java
public static Vector list(String dirname,
                          int flag)
                   throws IOException,
                          SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Returns:**
- `dirname`아래에 있는 모든 파일 이름과 디렉토리 이름

**Throws:**
- `IOException` - `dirname`이 존재하지 않을 경우

### exists

```java
public static boolean exists(String name)
                      throws IOException
```

**Parameters:**
- `name` - 파일이나 디렉토리 이름

**Returns:**
- 존재하면 true, 존재하지 않으면 false

### exists

```java
public static boolean exists(String name,
                             int flag)
                      throws IOException,
                             SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Returns:**
- 존재하면 true, 존재하지 않으면 false

**Throws:**
- `SecurityException` - 접근할 수 없는 디렉토리를 접근하려고 할 경우

### remove

```java
public static void remove(String filename)
                   throws IOException
```

**Parameters:**
- `filename` - 파일 이름

**Throws:**
- `IOException` - 파일을 지울 때 제대로 지우지 못할 경우, 파일이 존재하지 않을 경우

### remove

```java
public static void remove(String filename,
                          int flag)
                   throws IOException,
                          SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Throws:**
- `IOException` - 파일을 지울 때 제대로 지우지 못할 경우, 파일이 존재하지 않을 경우

### mkdir

```java
public static void mkdir(String dirname)
                  throws IOException
```

**Parameters:**
- `dirname` - 디렉토리 이름

**Throws:**
- `IOException` - 디렉토리를 만들 수 없을 경우나 디렉토리가 이미 존재할 경우, 또는 파일 이름 길이가 최대값을 넘어 갈 경우

### mkdir

```java
public static void mkdir(String dirname,
                         int flag)
                  throws IOException,
                         SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Throws:**
- `IOException` - 디렉토리를 만들 수 없을 경우나 디렉토리가 이미 존재할 경우, 또는 파일 이름 길이가 최대값을 넘어 갈 경우

### rmdir

```java
public static void rmdir(String dirname)
                  throws IOException
```

**Parameters:**
- `dirname` - 디렉토리 이름

**Throws:**
- `IOException` - 디렉토리가 비어있지 않거나 디렉토리를 지울 수 없을 경우, 또는 디렉토리가 존재하지 않을 경우

### rmdir

```java
public static void rmdir(String dirname,
                         ang/String.html">String dirname,
                         int flag)
                  throws IOException,
                         SecurityException
```

## 생성자 상세

### FileSystem

```java
public FileSystem()
```

### getMaxFilenameLength

```java
public static int getMaxFilenameLength()
```

**Returns:**
- 파일이름 최대 길이

### list

```java
public static Vector list(String dirname)
                   throws IOException
```

**Parameters:**
- `dirname` - 디렉토리 이름

**Returns:**
- `dirname`아래에 있는 모든 파일이름과 디렉토리 이름

**Throws:**
- `IOException` - 디렉토리가 존재하지 않을 경우

### list

```java
public static Vector list(String dirname,
                          int flag)
                   throws IOException,
                          SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Returns:**
- `dirname`아래에 있는 모든 파일 이름과 디렉토리 이름

**Throws:**
- `IOException` - `dirname`이 존재하지 않을 경우

### exists

```java
public static boolean exists(String name)
                      throws IOException
```

**Parameters:**
- `name` - 파일이나 디렉토리 이름

**Returns:**
- 존재하면 true, 존재하지 않으면 false

### exists

```java
public static boolean exists(String name,
                             int flag)
                      throws IOException,
                             SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Returns:**
- 존재하면 true, 존재하지 않으면 false

**Throws:**
- `SecurityException` - 접근할 수 없는 디렉토리를 접근하려고 할 경우

### remove

```java
public static void remove(String filename)
                   throws IOException
```

**Parameters:**
- `filename` - 파일 이름

**Throws:**
- `IOException` - 파일을 지울 때 제대로 지우지 못할 경우, 파일이 존재하지 않을 경우

### remove

```java
public static void remove(String filename,
                          int flag)
                   throws IOException,
                          SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Throws:**
- `IOException` - 파일을 지울 때 제대로 지우지 못할 경우, 파일이 존재하지 않을 경우

### mkdir

```java
public static void mkdir(String dirname)
                  throws IOException
```

**Parameters:**
- `dirname` - 디렉토리 이름

**Throws:**
- `IOException` - 디렉토리를 만들 수 없을 경우나 디렉토리가 이미 존재할 경우, 또는 파일 이름 길이가 최대값을 넘어 갈 경우

### mkdir

```java
public static void mkdir(String dirname,
                         int flag)
                  throws IOException,
                         SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Throws:**
- `IOException` - 디렉토리를 만들 수 없을 경우나 디렉토리가 이미 존재할 경우, 또는 파일 이름 길이가 최대값을 넘어 갈 경우

### rmdir

```java
public static void rmdir(String dirname)
                  throws IOException
```

**Parameters:**
- `dirname` - 디렉토리 이름

**Throws:**
- `IOException` - 디렉토리가 비어있지 않거나 디렉토리를 지울 수 없을 경우, 또는 디렉토리가 존재하지 않을 경우

### rmdir

```java
public static void rmdir(String dirname,
                         ang/String.html">String dirname,
                         int flag)
                  throws IOException,
                         SecurityException
```

## 메서드 상세

### getMaxFilenameLength

```java
public static int getMaxFilenameLength()
```

**Returns:**
- 파일이름 최대 길이

### list

```java
public static Vector list(String dirname)
                   throws IOException
```

**Parameters:**
- `dirname` - 디렉토리 이름

**Returns:**
- `dirname`아래에 있는 모든 파일이름과 디렉토리 이름

**Throws:**
- `IOException` - 디렉토리가 존재하지 않을 경우

### list

```java
public static Vector list(String dirname,
                          int flag)
                   throws IOException,
                          SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Returns:**
- `dirname`아래에 있는 모든 파일 이름과 디렉토리 이름

**Throws:**
- `IOException` - `dirname`이 존재하지 않을 경우

### exists

```java
public static boolean exists(String name)
                      throws IOException
```

**Parameters:**
- `name` - 파일이나 디렉토리 이름

**Returns:**
- 존재하면 true, 존재하지 않으면 false

### exists

```java
public static boolean exists(String name,
                             int flag)
                      throws IOException,
                             SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Returns:**
- 존재하면 true, 존재하지 않으면 false

**Throws:**
- `SecurityException` - 접근할 수 없는 디렉토리를 접근하려고 할 경우

### remove

```java
public static void remove(String filename)
                   throws IOException
```

**Parameters:**
- `filename` - 파일 이름

**Throws:**
- `IOException` - 파일을 지울 때 제대로 지우지 못할 경우, 파일이 존재하지 않을 경우

### remove

```java
public static void remove(String filename,
                          int flag)
                   throws IOException,
                          SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Throws:**
- `IOException` - 파일을 지울 때 제대로 지우지 못할 경우, 파일이 존재하지 않을 경우

### mkdir

```java
public static void mkdir(String dirname)
                  throws IOException
```

**Parameters:**
- `dirname` - 디렉토리 이름

**Throws:**
- `IOException` - 디렉토리를 만들 수 없을 경우나 디렉토리가 이미 존재할 경우, 또는 파일 이름 길이가 최대값을 넘어 갈 경우

### mkdir

```java
public static void mkdir(String dirname,
                         int flag)
                  throws IOException,
                         SecurityException
```

**Parameters:**
- `flag` - 접근하고자 하는 디렉토리

**Throws:**
- `IOException` - 디렉토리를 만들 수 없을 경우나 디렉토리가 이미 존재할 경우, 또는 파일 이름 길이가 최대값을 넘어 갈 경우

### rmdir

```java
public static void rmdir(String dirname)
                  throws IOException
```

**Parameters:**
- `dirname` - 디렉토리 이름

**Throws:**
- `IOException` - 디렉토리가 비어있지 않거나 디렉토리를 지울 수 없을 경우, 또는 디렉토리가 존재하지 않을 경우

### rmdir

```java
public static void rmdir(String dirname,
                         ang/String.html">String dirname,
                         int flag)
                  throws IOException,
                         SecurityException
```
