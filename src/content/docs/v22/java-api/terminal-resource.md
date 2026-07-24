---
title: "3.1.6. 단말 리소스"
---

---

## Class ResourceGroup

```text
java.lang.Object
  +--org.kwis.msp.io.ResourceGroup
```

```java
public class ResourceGroup extends java.lang.Object
```

단말 리소스 그룹 관련 클래스를 정의한다.

*Methods inherited from class java.lang.Object: clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 생성자 상세

### ResourceGroup

```java
public ResourceGroup(java.lang.String grpName) throws IOException
```

그룹 이름 (grpName) 에 맞는 ResourceGroup 객체를 생성한다. 현재 단말에서 지원하는 리소스 그룹은 System.getProperty() 함수를 이용하여, supported.resourcegroups 값을 얻어오면 알 수 있다. (리스트내의 그룹은 '\0' 문자로 구분되어 지며, 리스트 마지막은 "\0\0" 문자열로 판단한다.)

**매개 변수**

- `grpName` - 생성할 ResourceGroup 이름 Throws
- `IOException` - 오류 발생시 필드 상세 설명 GROUP_LOCKED
- `public` - static final int GROUP_LOCKED GROUP_UNLOCKED
- `public` - static final int GROUP_UNLOCKED LOCKED
- `public` - static final int LOCKED UNLOCKED
- `public` - static final int UNLOCKED 메쏘드 상세 설명 checkPassword

### checkPassword

```java
public static boolean checkPassword( java.lang.String password) throws IOException
```

해당하는 리소스가 잠금되어 있으면 그 잠금을 해제하기 위해 필요한 비밀번호가 주어진 password와 맞는지 체크한다.

**매개 변수**

- `password` - Password

**반환 값**

성공하면 ture, 비밀번호가 일치하지 않으면 false Throws IllegalArgumentException 전달된 매개변수가 null인 경우(C API에서는
- `M_E_INVALID` - 에러 발생 시와 동일함) IOException 알 수 없는 이유로 실패(C API에서는 `M_E_ERROR` 에러 발생 시와 동일함) deleteData public void deleteData(String resName) throws IOException 해당 이름의 리소스를 삭제한다. 단, 리소스의 삭제를 허용하지 않는 그룹은 HandsetProperty.getSystemProperty함수의 "NOTDELGROUP"을 통해, 삭제가 불가능한 리소스에 대해서는 getGroupInfo함수의 infotype "IRREMOVABLE"을 통해 확인할 수 있다.

**매개 변수**

- `resName` - 리소스 이름 Throws
- `IllegalArgumentException` - 전달된 매개변수가 null이거나 존재하지 않는 리소스가 전달된 경우(C API에서는 `M_E_INVALID` 에러 발생 시와 동일함)
- `IOException` - 접근 권한이 없거나 (`M_E_ACCESSDENY`), 삭제 기능을 지원하지 않는 리소스 그룹 또는 리소스인 경우(`M_E_NOTSUP`), 삭제 기능을 지원하나 현재 리소스 그룹이나 리소스의 상태가 삭제 불가능한 상태일 경우(`M_E_NODELETE`), 알 수 없는 이유로 실패(`M_E_ERROR`) getCount

### getCount

```java
public int getCount()
```

이 ResourceGroup에 저장된 리소스의 개수를 반한한다.

**반환 값**

성공 리소스 개수 실패 에러코드(음수)
- `M_E_ERROR` - 알 수 없는 이유로 실패 getData public byte[] getData(java.lang.String resName) throws IOException 리소스 이름에 해당하는 리소스의 실제 데이터를 반환한다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

리소스 데이터 Throws IllegalArgumentException 전달된 매개변수가 null이거나 존재하지 않는 리소스가 전달된 경우(C API 에서는 `M_E_INVALID` 에러 발생 시와 동일함) IOException 사용자가 읽기권한이 없는 리소스일 경우(`M_E_ACCESSDENY`), 알 수 없는 이유로 실패(C API에서는 `M_E_ERROR` 에러 발생 시와 동일함) getFreeSpace public static int getFreeSpace()throws IOException 단말 리소스를 향후 최대 얼마나 저장할 수 있는지에 대해서 저장공간의 남은 크기를 byte 단위로 반환한다. 리소스 그룹 별로 나누어 반환하는 것이 아닌 그룹들이 사용 가능한 총 공간을 반환한다. 그룹별 저장 공간의 남은 크기를 알기 위해서는 getGroupInfo함수의 infoType "FREESPACE"를 사용, 전체 가용 공간의 크기를 알기 위해서는 "TOTALSPACE"를 사용한다.

**반환 값**

리소스 그룹 저장 공간의 여유 공간 Throws IOException 알 수 없는 이유로 실패(C API에서는 `M_E_ERROR` 에러 발생 시와 동일함)

### getFormat

```java
public java.lang.String getFormat(java.lang.String resName) throws IOException
```

이 ResourceGruop의 리소스 이름에 해당하는 리소스의 포맷(MIME type)을 반환한다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

MIME 타입을 스트링으로 반환한다. Throws IllegalArgumentException 전달된 매개변수가 null이거나 존재하지않는 리소스가 전달된 경우(C API 에서는 `M_E_INVALID` 에러 발생 시와 동일함) IOException MIME 타입이 없는 리소스(C API에서는
- `M_E_NOTSUPPORTTYPE` - 에러 발생 시와 동일함) getList public java.lang.String[] getList()throws IOException 이 ResourceGroup의 리소스 이름 목록을 반환한다.

**반환 값**

성공 리소스 이름 목록 혹은 리소스 목록이 존재하지 않을 경우 null 반환 Throws IOException 알 수 없는 이유로 실패(`M_E_ERROR`)

### getGroupLockStatus

```java
public int getGroupLockStatus() throws IOException
```

해당 그룹 리소스의 Lock 상태를 반환한다. Lock status에는 GROUP_LOCKED, GROUP_UNLOCKED가 있다.

**매개 변수**

없음

**반환 값**

Lock status를 반환한다. Throws IOException 해당 리소스 그룹(또는 리소스)이 LOCK 기능을 제공하지 않을 경우(`M_E_NOTSUPPORTLOCK`,
`M_E_NOTSUPPORTGLOCK`), 알 수 없는 이유로 실패(`M_E_ERROR`)

### getLockStatus

```java
public int getLockStatus(java.lang.String resName) throws IOException
```

주어진 리소스 이름에 해당하는 리소스의 잠금 상태를 반환한다. 잠금 상태에는 LOCKED, UNLOCKED가 있다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

Lock status를 반환한다. Throws IOException 해당 리소스 그룹(또는 리소스)이 LOCK 기능을 제공하지 않을 경우(`M_E_NOTSUPPORTLOCK`,
`M_E_NOTSUPPORTPLOCK`), 알 수 없는 이유로 실패(`M_E_ERROR`) IllegalArgumentException 전달한 매개변수가 null이거나 존재하지 않는 리소스가 전달된 경우(`M_E_INVALID`)

### getRegisteredInfo

```java
public static java.lang.String[] getRegisteredInfo(java.lang.String state) throws IOException
```

리소스 그룹에 속하는 리소스 중 단말 특정 상태에 등록되어 있는 리소스 이름의 리스트를 반환한다.

**매개 변수**

- `state` - 단말기 상태 “IDLE” 대기 화면 “INCOMING” 전화 수신 화면 “POWERON” 단말 구동 화면 “POWEROFF” 단말 종료 화면 “BROWSERON” 브라우저 구동 시 “BROWSEROFF” 브라우저 종료시

**반환 값**

성공

리소스 그룹과 리소스 이름의 목록 리소스 그룹 이름, “;”, 리소스 이름 순으로 구성된다.
실패

null(`M_E_NORES` 의 경우) Throws IllegalArgumentException 전달된 매개 변수가 null인 경우. (C API에서
- `M_E_INVALID` - 에러 발생 시와 동일함) IOException 다른 에러 발생 시 getSize public int getSize(java.lang.String resName) throws IOException 리소스 이름에 해당하는 리소스의 실제 데이터 크기를 반환한다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

리소스 실제 데이터 크기 Throws IllegalArgumentException 전달된 매개 변수가 null이거나 존재하지 않는 리소스가 전달된 경우. (C API에서 `M_E_INVALID` 에러 발생 시와 동일함) IOException 알 수 없는 이유로 실패할 경우(`M_E_ERROR`) getSupportedGroups public static java.lang.String[] getSupportedGroups()throws IOException 현재 단말이 지원하는 리소스 그룹 리스트를 반환하다. System.getProperty("supported.resourcegroups")와 동일한 기능을 한다. 단, return 값이 문자열 목록이다.

**반환 값**

제공되는 ResourceGroup의 이름 목록 Throws IOException 알 수 없는 이유로 실패할 경우(`M_E_ERROR`)

### registerData

```java
public void registerData(java.lang.String resName, java.lang.String state) throws IOException
```

리소스 이름에 해당하는 리소스를 단말 특정 상태에 설정한다. HandsetProperty.getSystemProperty("REGISTRABLESTATUS_IDLE"), HandsetProperty.getSystemProperty("REGISTRABLESTATUS_INCOMING"), HandsetProperty.getSystemProperty("REGISTRABLESTATUS_POWERON"), HandsetProperty.getSystemProperty("REGISTRABLESTATUS_POWEROFF"), HandsetProperty.getSystemProperty("REGISTRABLESTATUS_BROWSERON"), HandsetProperty.getSystemProperty("REGISTRABLESTATUS_BROWSEROFF")을 통하여 단말에서 허용하는 상태에 대해서 조회할 수 있다

**매개 변수**

- `resName` - 리소스 이름
- `state` - 단말 상태 “IDLE” 대기 화면 “INCOMING” 전화 수신 화면 “POWERON” 단말 구동 화면 “POWEROFF” 단말 종료 화면 “BROWSERON” 브라우저 구동 시 “BROWSEROFF” 브라우저 종료시 Throws
- `IllegalArgumentException` - 전달된 매개 변수가 null이거나 존재하지 않는 리소스가 전달된 경우. (C API에서 `M_E_INVALID` 에러 발생 시와 동일함)
- `IOException` - 다른 에러 발생 시(접근 권한이 없거나 (`M_E_ACCESSDENY`), register 기능을 지원하지 않을시(`M_E_NOTSUP`, 리소스와 단말 특정 상태가 연관이 없는 경우(`M_E_INVALIDSTATUS`), 그 밖의 알 수 없는 이유(`M_E_ERROR`)) setGroupLockStatus

### setGroupLockStatus

```java
public void setGroupLockStatus(int status) throws IOException
```

그룹에 해당하는 리소스의 잠금을 설정하거나 해제한다. HandsetProperty.getSystemProperty("SUPPORTGLOCK")을 통하여 단말에서 구룹
- `Lock을` - 지원하는 리소스구룹의 목록을 조회할 수 있다.

**매개 변수**

- `Status` - 잠금 상태 (GROUP_LOCKED, GROUP_UNLOCKED) Throws
- `IllegalArgumentException` - 잘못된 status값인 경우 (GROUP_LOCKED,
- `GROUP_UNLOCKED` - 이 아닌 값인 경우)
- `IOException` - IllegalArgumentException 제외한 그 밖의 에러일 경우(해당 리소스 그룹/리소스가 Lock 설정을 지원하지 않음(`M_E_NOTSUPPORTLOCK`), 해당 리소스 그룹이 그룹
- `Lock은` - 지원하지 않음 (개별 Lock은 지원함) (`M_E_NOTSUPPORTGLOCK`), 알 수 없는 이유로 실패(`M_E_ERROR`)) setLockStatus

### setLockStatus

```java
public void setLockStatus(java.lang.String resName, int status) throws IOException
```

주어진 이름에 해당하는 리소스의 잠금을 설정하거나 해제한다. HandsetProperty.getSystemProperty("SUPPORTPLOCK")을 통하여 단말에서 개별 리소스 Lock을 지원하는 리소스구룹의 목록을 조회할 수 있다.

**매개 변수**

- `resName` - 리소스 이름
- `status` - 잠금 상태 (LOCKED, UNLOCKED) Throws
- `IllegalArgumentException` - 전달된 매개 변수가 null이거나 존재하지 않는 리소스가 전달된 경우. (C API 에서 `M_E_INVALID` 에러 발생 시와 동일함), 잘못된 status 값인 경우 (LOCKED,
- `UNLOCKED` - 이 아닌 값인 경우)
- `IOException` - 해당 리소스 그룹(또는 리소스)이 LOCK 기능을 제공하지 않을 경우 (`M_E_NOTSUPPORTLOCK`, `M_E_NOTSUPPORTPLOCK`), 알 수 없는 이유로 실패 (`M_E_ERROR`) writeData

### writeData

```java
public java.lang.String writeData (java.lang.String title, java.lang.String uiName, java.lang.String format, byte[] data, boolean update)
```

- `throws` - IOException 특정 포맷을 가지는 리소스 데이터를 쓰기한다.

**매개 변수**

- `title` - 새로 생성되거나 기존에 존재하는 리소스 이름
- `uiName` - UI 상에 나타나는 이름
- `format` - 리소스의 MIME 타입
- `data` - 데이터
- `update` - 리소스 이름을 가지는 리소스가 있으면 갱신한다.

**반환 값**

title로 저장된 리소스 이름을 반환한다. 에러 처리 된 경우 null을 반환한다. 단, title은 Unique한 값으로 리소스 생성시 반환된 title은 변할수 없다. 또한, UPDATE 모드 수행 시, 업데이트 하고자 하는 필드의 데이터만 넣을 경우, 다른 필드의 데이터들은 삭제된다. 예로 PHONEBOOK/PRIVATE의 경우 특정 필드의 값을 업데이트 하고자 필드값만 넣고 수행 시, 데이터를 넣지 않은 다른 필드들은 모두 삭제된다. Throws IllegalArgumentException 전달된 매개 변수가 null이거나 존재하지 않는 리소스가(UPDATE 모드인 경우) 전달된 경우. (C API에서 `M_E_INVALID` 에러 발생 시와 동일함) IOException 쓰기 권한이 없거나 (`M_E_ACCESSDENY`), 쓰기 기능이나 갱신 기능이 지원되지 않을 경우(`M_E_NOTSUP`), 리소스 저장 공간 부족(`M_E_INSUFSPACE`), 데이터가 해당 데이터 포맷에 맞지 않을 경우(`M_E_INVALIDDATA`), 리소스 그룹에서 지원하는 최대 개수를 초과한 경우 (`M_E_MAXCOUNT`), 알 수 없는 이유로 실패(`M_E_ERROR`)

### exists

```java
public boolean exists(java.lang.String resName) throws IOException
```

지정한 리소스 이름에 해당하는 리소스가 존재하는지 확인한다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

리소스의 존재 여부. 존재하면 true, 존재하지 않으면 false Throws IllegalArgumentException 전달된 매개 변수가 null인 경우. (C API 에서
- `M_E_INVALID` - 에러 발생 시와 동일함) IOException 알 수 없는 이유로 실패 getGroupInfo public byte[] getGroupInfo(java.lang.String type) throws IOException 리소스 그룹에 대해 type 에 해당하는 그룹의 특성을 얻어 온다. 각 그룹마다 얻어 올 수 있는 그룹 특성 및 타입은 C API의 `MC_termResGetGroupInfo()` 함수의 정의를 따른다.

**매개 변수**

- `type` - 그룹의 특성을 얻기 위한 타입 정보

**반환 값**

그룹의 타입에 해당하는 특성 정보를 반환한다. 특성 정보가 존재하지 않을 경우 null. Throws IllegalArgumentException 전달된 매개 변수가 null인 경우. (C API 에서 `M_E_INVALID` 에러 발생 시와 동일함) IOException 해당 그룹은 지정한 그룹 정보 타입의 그룹 정보를지원하지 않음(`M_E_NOTSUPPORTTYPE`), 알 수 없는 이유로 실패(`M_E_ERROR`)

### getInfo

```java
public byte[] getInfo(java.lang.String resName, java.lang.String type) throws IOException
```

리소스에 대해 type 에 해당하는 리스소의 특성을 얻어 온다. 각 리소스마다 얻어 올 수 있는 리소스 특성 및 타입은 C API의 `MC_termResGetInfo()` 함수의 정의를 따른다.

**매개 변수**

- `resName` - 리소스 이름
- `type` - 그룹의 특성을 얻기 위한 타입 정보

**반환 값**

리소스의 타입에 해당하는 특성 정보를 반환한다. 특성 정보가 존재하지 않을 경우 null. Throws IllegalArgumentException 전달된 매개 변수가 null이거나 존재하지 않는 리소스가 전달된 경우. (C API에서 `M_E_INVALID` 에러 발생 시와 동일함) IOException 알 수 없는 이유로 실패

### search

```java
public static String[] search(java.lang.String grp, java.lang.String type, java.lang.String query, boolean exactMatch) throws IOException
```

리소스 그룹과 검색어 타입에 따라 주어진 문자열 검색어와 일치하는 리소스를 검색한다. 검색 결과로는 리소스 이름 리스트를 반환한다. 검색 타입(type) 지정 방밥은 C API의 `MC_termResSearch()` 함수의 정의를 따른다.

**매개 변수**

- `grp` - 리소스 그룹 이름
- `type` - 검색 타입
- `query` - 검색어
- `exactMatch` - 검색 방법(true 이면 검색어와 완전히 일치하는 리소스만 검색 한다.) 반환 값: 검색 결과를 리스트로 반환한다. 검색 결과가 존재하지 않을 경우 null을 반환한다. Throws
- `IllegalArgumentException` - 전달된 매개 변수가 null이거나 단말에서 지원하지 않는 리소스 그룹이 전달된 경우. (C API에서 `M_E_INVALID` 에러 발생 시와 동일함)
- `IOException` - 해당 리소스 그룹은 지정한 queryType을 지원하지 않음(`M_E_NOTSUPPORTTYPE`), 알 수 없는 이유로 실패(`M_E_ERROR`) getUIName

### getUIName

```java
public java.lang.String getUIName(java.lang.String resName) throws IOException
```

지정한 리소스의 UI 이름을 반환한다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

UI 이름. Throws IllegalArgumentException 전달된 매개 변수가 null이거나 존재하지 않는 리소스가 존달된 경우. (C API에서 `M_E_INVALID` 에러 발생 시와 동일함) IOException llegalArgumentException 제외한 그 밖의 에러일 경우
