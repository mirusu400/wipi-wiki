# Class Kernel

`package org.kwis.msf.core`

```
java.lang.Object
  |
  +--org.kwis.msf.core.Kernel
```

## 설명

**extends Object:**

## 필드 요약

- `static int DIR_SHARED_READ_REQ_MASK` — shared directory read가능
- `static int DIR_SHARED_WRITE_REQ_MASK` — shared directory write가능
- `static int DIR_SYS_READ_REQ_MASK` — system directory read가능
- `static int DIR_SYS_WRITE_REQ_MASK` — system directory write가능
- `static int NETWORK_ACCESS_REQ_MASK` — network API사용 가능
- `static int PRGTYPE_CAPP`
- `static int PRGTYPE_CDLL`
- `static int PRGTYPE_JAVAAPP`
- `static int PRGTYPE_JAVADLL`
- `static int PRGTYPE_JAVASYSDLL`
- `static int SERIAL_ACCESS_REQ_MASK` — serial API사용 가능
- `static int SYSTEM1_ACCESS_REQ_MASK` — system group1에 속한 API사용가능(system group1에 속할 API들은 각 이통사가 정의)
- `static int SYSTEM2_ACCESS_REQ_MASK` — system group2에 속한 API사용가능(system group2에 속할 API들은 각 이통사가 정의)

## 생성자 요약

- Kernel ()

## 메서드 요약

- `static int execute ( String execName, String [] args)` — 플랫폼에 설치된 프로그램을 실행시킨다.
- `static int getAccessLevel ()` — 프로그램의 접근 수준을 구합니다.
- `static int getAMID ()` — 응용프로그램 관리자의 프로그램의 ID를 구한다.
- `static String [] getExecNames ( String prgName, String version, String vendor)` — 플랫폼에 설치된 애플리케이션중 prgName(프로그램이름), version, vendor와 일치하는 애플리케이션 식별이름을 반환한다.
- `static int getParentPrgID ()` — 부모 프로그램의 ID를 구한다
- `static int getPrgID ()` — 현재 프로그램의 ID를 구한다.
- `static int[] getPrgInfo ()` — 현재 동작중인 프로그램에 대한 정보를 얻는다. int array의 length는 현재 동작중인 프로그램의 수를 나타내고, 각 index에 속한 값은 해당 index에 해당하는 프로그램의 type를 나타낸다.
- `static String getPrgName ()` — 자기 자신의 프로그램 이름을 구한다.
- `static int letThrowExceptionWhenProgramExit ()` — 프로그램이 종료하면 이 함수를 부른 thread에 ProgramExitException exception이 발생하게 만든다.
- `static int load ( String execName, String [] args)` — 플랫폼에 설치된 동적로딩라이브러리를 로딩합니다.
- `static int mExecute ( String symName, String [] args)` — 프로그램에 설치된 프로그램을 실행시킵니다.
- `static int mLoad ( String symName, String [] args)` — 프로그램에 설치된 동적로딩라이브러리를 로딩합니다.
- `static void stop (int prgID)` — 프로그램을 강제로 종료시킨다.

## 필드 상세

### PRGTYPE_JAVAAPP

```java
public static final int PRGTYPE_JAVAAPP
```

### PRGTYPE_CAPP

```java
public static final int PRGTYPE_CAPP
```

### PRGTYPE_CDLL

```java
public static final int PRGTYPE_CDLL
```

### PRGTYPE_JAVADLL

```java
public static final int PRGTYPE_JAVADLL
```

### PRGTYPE_JAVASYSDLL

```java
public static final int PRGTYPE_JAVASYSDLL
```

### DIR_SYS_READ_REQ_MASK

```java
public static final int DIR_SYS_READ_REQ_MASK
```

- system directory read가능

### DIR_SYS_WRITE_REQ_MASK

```java
public static final int DIR_SYS_WRITE_REQ_MASK
```

- system directory write가능

### DIR_SHARED_READ_REQ_MASK

```java
public static final int DIR_SHARED_READ_REQ_MASK
```

- shared directory read가능

### DIR_SHARED_WRITE_REQ_MASK

```java
public static final int DIR_SHARED_WRITE_REQ_MASK
```

- shared directory write가능

### NETWORK_ACCESS_REQ_MASK

```java
public static final int NETWORK_ACCESS_REQ_MASK
```

- network API사용 가능

### SERIAL_ACCESS_REQ_MASK

```java
public static final int SERIAL_ACCESS_REQ_MASK
```

- serial API사용 가능

### SYSTEM1_ACCESS_REQ_MASK

```java
public static final int SYSTEM1_ACCESS_REQ_MASK
```

- system group1에 속한 API사용가능(system group1에 속할 API들은 각 이통사가 정의)

### SYSTEM2_ACCESS_REQ_MASK

```java
public static final int SYSTEM2_ACCESS_REQ_MASK
```

- system group2에 속한 API사용가능(system group2에 속할 API들은 각 이통사가 정의)

### Kernel

```java
public Kernel()
```

### execute

```java
public static int execute(String execName,
                          String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 매개변수

**Returns:**
- 성공이면 살행된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

**See Also:**
- ``getExecNames(String prgName, String version, String vendor)``

### mExecute

```java
public static int mExecute(String symName,
                           String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 매개변수

**Returns:**
- 성공이면 살행된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

### load

```java
public static int load(String execName,
                       String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 parameter

**Returns:**
- 성공이면 load된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

**See Also:**
- ``getExecNames(String prgName, String version, String vendor)``

### mLoad

```java
public static int mLoad(String symName,
                        String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 parameter

**Returns:**
- 성공이면 load된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

### getExecNames

```java
public static String[] getExecNames(String prgName,
                                    String version,
                                    String vendor)
```

**Parameters:**
- `vendor` - 프로그램 공급자

**Returns:**
- 프로그램 이름 string array

### getPrgID

```java
public static int getPrgID()
```

**Returns:**
- 프로그램 ID

### getAMID

```java
public static int getAMID()
```

**Returns:**
- 프로그램 ID

### getParentPrgID

```java
public static int getParentPrgID()
```

**Returns:**
- 프로그램 ID

### getPrgInfo

```java
public static int[] getPrgInfo()
```

**Returns:**
- 동작중인 프로그램의 type을 포함하는 integer array

### stop

```java
public static void stop(int prgID)
```

**Parameters:**
- `prgID` - 강제 종료시킬 프로그램이 ID

### letThrowExceptionWhenProgramExit

```java
public static int letThrowExceptionWhenProgramExit()
```

**Returns:**
- 0보다 크면 가장 최근에 종료된 프로그램의 ID

### getAccessLevel

```java
public static int getAccessLevel()
```

**Returns:**
- 접근수준(각 마스크값의 OR값)

### getPrgName

```java
public static String getPrgName()
```

**Returns:**
- 프로그램 이름## 생성자 상세

### Kernel

```java
public Kernel()
```

### execute

```java
public static int execute(String execName,
                          String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 매개변수

**Returns:**
- 성공이면 살행된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

**See Also:**
- ``getExecNames(String prgName, String version, String vendor)``

### mExecute

```java
public static int mExecute(String symName,
                           String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 매개변수

**Returns:**
- 성공이면 살행된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

### load

```java
public static int load(String execName,
                       String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 parameter

**Returns:**
- 성공이면 load된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

**See Also:**
- ``getExecNames(String prgName, String version, String vendor)``

### mLoad

```java
public static int mLoad(String symName,
                        String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 parameter

**Returns:**
- 성공이면 load된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

### getExecNames

```java
public static String[] getExecNames(String prgName,
                                    String version,
                                    String vendor)
```

**Parameters:**
- `vendor` - 프로그램 공급자

**Returns:**
- 프로그램 이름 string array

### getPrgID

```java
public static int getPrgID()
```

**Returns:**
- 프로그램 ID

### getAMID

```java
public static int getAMID()
```

**Returns:**
- 프로그램 ID

### getParentPrgID

```java
public static int getParentPrgID()
```

**Returns:**
- 프로그램 ID

### getPrgInfo

```java
public static int[] getPrgInfo()
```

**Returns:**
- 동작중인 프로그램의 type을 포함하는 integer array

### stop

```java
public static void stop(int prgID)
```

**Parameters:**
- `prgID` - 강제 종료시킬 프로그램이 ID

### letThrowExceptionWhenProgramExit

```java
public static int letThrowExceptionWhenProgramExit()
```

**Returns:**
- 0보다 크면 가장 최근에 종료된 프로그램의 ID

### getAccessLevel

```java
public static int getAccessLevel()
```

**Returns:**
- 접근수준(각 마스크값의 OR값)

### getPrgName

```java
public static String getPrgName()
```

**Returns:**
- 프로그램 이름## 메서드 상세

### execute

```java
public static int execute(String execName,
                          String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 매개변수

**Returns:**
- 성공이면 살행된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

**See Also:**
- ``getExecNames(String prgName, String version, String vendor)``

### mExecute

```java
public static int mExecute(String symName,
                           String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 매개변수

**Returns:**
- 성공이면 살행된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

### load

```java
public static int load(String execName,
                       String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 parameter

**Returns:**
- 성공이면 load된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

**See Also:**
- ``getExecNames(String prgName, String version, String vendor)``

### mLoad

```java
public static int mLoad(String symName,
                        String[] args)
```

**Parameters:**
- `args` - Main method()로 전달될 parameter

**Returns:**
- 성공이면 load된 프로그램의 프로그램ID 반환, 실패하면 음수 반환

### getExecNames

```java
public static String[] getExecNames(String prgName,
                                    String version,
                                    String vendor)
```

**Parameters:**
- `vendor` - 프로그램 공급자

**Returns:**
- 프로그램 이름 string array

### getPrgID

```java
public static int getPrgID()
```

**Returns:**
- 프로그램 ID

### getAMID

```java
public static int getAMID()
```

**Returns:**
- 프로그램 ID

### getParentPrgID

```java
public static int getParentPrgID()
```

**Returns:**
- 프로그램 ID

### getPrgInfo

```java
public static int[] getPrgInfo()
```

**Returns:**
- 동작중인 프로그램의 type을 포함하는 integer array

### stop

```java
public static void stop(int prgID)
```

**Parameters:**
- `prgID` - 강제 종료시킬 프로그램이 ID

### letThrowExceptionWhenProgramExit

```java
public static int letThrowExceptionWhenProgramExit()
```

**Returns:**
- 0보다 크면 가장 최근에 종료된 프로그램의 ID

### getAccessLevel

```java
public static int getAccessLevel()
```

**Returns:**
- 접근수준(각 마스크값의 OR값)

### getPrgName

```java
public static String getPrgName()
```

**Returns:**
- 프로그램 이름

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
