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
public ResourceGroup(java.lang.String grpName)
```

그룹 이름 (grpName) 에 맞는 ResourceGroup 객체를 생성한다. 현재 단말에서 지원 하는 리소스 그룹은 System.getProperty() 함수를 이용하여, supports.resourcegroups 값을 얻어오면 알 수 있다.

**매개 변수**

- `grpName` - 생성할 ResourceGroup 이름 필드 상세 설명 GROUP_LOCKD
- `Static` - int GROUP_LOCKED 값은 2이다. GROUP_UNLOCKED
- `Static` - int GROUP_UNLOCKED 값은 3이다. LOCKED
- `Static` - int LOCKED 값은 0이다. UNLOCKED
- `Static` - int UNLOCKED 값은 1이다. 메쏘드 상세 설명 checkPassword

### checkPassword

```java
public int checkPassword( java.lang.String password)
```

해당하는 리소스가 잠금되어 있으면 그 잠금을 해제하기 위해 필요한 비밀번호가 주 어진 password와 맞는지 체크한다.

**매개 변수**

- `password` - Password

**반환 값**

성공하면 0, 아니면 에러코드 (음수 값)

### deleteData

```java
public int deleteData(String resName)
```

해당 이름의 리소스를 삭제한다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

성공하면 0, 아니면 에러코드(음수)

### getCount

```java
public int getCount()
```

이 ResourceGroup에 저장된 리소스의 개수를 반한한다.

**반환 값**

성공하면 리소스 개수, 아니면 에러코드(음수)

### getData

```java
public byte[] getData(java.lang.String resName)
```

리소스 이름에 해당하는 리소스의 실제 데이터를 반환한다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

리소스 데이터

### getFreeSpace

```java
public int getFreeSpace()
```

남은 리소스 그룹 저장 공간의 여유공간 크기를 바이트 단위로 구한다.

**반환 값**

리소스 그룹 저장 공간의 여유 공간

### getFormat

```java
public java.lang.String getFormat(java.lang.String resName)
```

이 ResourceGruop의 리소스 이름에 해당하는 리소스의 Format을 반환한다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

포맷을 스트링으로 리턴한다.

### getID

```java
public java.lang.String getID(java.lang.String resName)
```

주어진 이름에 해당하는 리소스에 대하여 특정한 Unique ID가 설정되어 있는 경우, 그 아이디를 반환한다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

ID가 있으면 Unique한 ID, 그렇지 않으면 에러코드(음수)

### getList

```java
public java.lang.String[] getList()
```

이 ResourceGroup의 리소스 이름 목록을 반환한다.

**반환 값**

리소스 이름 목록

### getGroupLockStatus

```java
public int getGroupLockStatus()
```

해당 그룹 리소스의 Lock 상태를 반환한다. Lock status에는 GROUP_LOCKED, GROUP_UNLOCKED가 있다. 매개변수: 없음 반환 값: Lock status를 리턴한다.

### getLockStatus

```java
public int getLockStatus(java.lang.String resName)
```

주어진 리소스 이름에 해당하는 리소스의 잠금 상태를 반환한다. 잠금 상태에는 LOCKED, UNLOCKED가 있다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

Lock status를 리턴한다.

### getRegisteredGroup

```java
public static java.lang.String[] getRegisteredGroup(java.lang.String state)
```

단말 특정 상태에 등록되어 있는 리소스 그룹의 리스트를 반환한다. 단말 상태에는 "POWERON", "POWEROFF", "IDLE", "INCOMMING", "BROWSERON", "BROWSEROFF" 이 있다.

**매개 변수**

- `state` - 단말 상태

**반환 값**

리소스 그룹 리스트

### getRegisteredInfo

```java
public java.lang.String[] getRegisteredInfo(java.lang.String state)
```

리소스 그룹에 속하는 리소스 중 단말 특정 상태에 등록되어 있는 리소스 이름의 리 스트를 반환한다.

**매개 변수**

- `state` - 단말기 상태

**반환 값**

이 리소스 그룹의 데이터 중 특정 state에 등록되어있는 리소스 이름 리스트

### getSize

```java
public int getSize(java.lang.String resName)
```

리소스 이름에 해당하는 리소스의 실제 데이터 크기를 반환한다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

리소스 실제 데이터 크기

### getSupportedGroups

```java
public static java.lang.String[] getSupportedGroups()
```

현재 단말이 지원하는 리소스 그룹 리스트를 반환하다. System.getProperty("supported.resourcegroups")와 동일한 기능을 한다. 단, return 값이 문자열 목록이다.

**반환 값**

제공되는 ResourceGroup의 이름 목록

### registerData

```java
public int registerData(java.lang.String resName, java.lang.String state)
```

리소스 이름에 해당하는 리소스를 단말 특정 상태에 설정한다.

**매개 변수**

- `resName` - 리소스 이름
- `state` - 단말 상태

**반환 값**

성공하면 0, 아니면 에러코드 (음수)

### setGroupLockStatus

```java
public int setGroupLockStatus(int status)
```

그룹에 해당하는 리소스의 잠금을 설정하거나 해제한다.

**매개 변수**

- `Status` - 잠금 상태 (GROUP_LOCKE, GROUP_UNLOCKED)

**반환 값**

성공하면 0, 아니면 에러코드(음수)

### setLockStatus

```java
public int setLockStatus(java.lang.String resName, int status)
```

주어진 이름에 해당하는 리소스의 잠금을 설정하거나 해제한다.

**매개 변수**

- `resName` - 리소스 이름
- `status` - 잠금 상태 (LOCKED, UNLOCKED)

**반환 값**

성공하면 0, 아니면 에러코드 (음수)

### writeData

```java
public java.lang.String writeData (java.lang.String title, java.lang.String format, byte[] data)
```

특정 포맷(format)을 가지는 리소스 데이터(data)를 Write한다.

**매개 변수**

- `title` - 새로 생성되거나 기존에 존재하는 리소스 이름
- `format` - 리소스의 MIME 타입
- `data` - 데이터

**반환 값**

title로 저장된 리소스 이름을 반환한다. 에러 처리 된 경우 null을 반환한다.

### exists

```java
public boolean exists(java.lang.String resName)
```

지정한 리소스 이름에 해당하는 리소스가 존재하는지 확인한다.

**매개 변수**

- `resName` - 리소스 이름

**반환 값**

리소스의 존재 여부. 존재하면 true, 존재하지 않으면 false

### getGroupInfo

```java
public java.lang.String getGroupInfo(java.lang.String type)
```

리소스 그룹에 대해 type 에 해당하는 그룹의 특성을 얻어 온다. 각 그룹마다 얻어 올 수 있는 그룹 특성 및 타입은 C API의 `MC_termResGetGroupInfo()` 함수의 정의를 따른다.

**매개 변수**

- `Type` - 그룹의 특성을 얻기 위한 타입 정보

**반환 값**

그룹의 타입에 해당하는 특성 정보를 리턴한다. 특성 정보가 존재하지 않을 경 우 null. getInfo
```java
public java.lang.String getGroupInfo(java.lang.String resName, java.lang.String type)
```

리소스에 대해 type 에 해당하는 리스소의 특성을 얻어 온다. 각 리소스마다 얻어 올 수 있는 리소스 특성 및 타입은 C API의 `MC_termResGetInfo()` 함수의 정의를 따 른다.

**매개 변수**

- `resName` - 리소스 이름
- `type` - 그룹의 특성을 얻기 위한 타입 정보 반환 값: 리소스의 타입에 해당하는 특성 정보를 리턴한다. 특성 정보가 존재하지 않을 경우 null. search
- `static` - public String[] search(java.lang.String grp, java.lang.String type, java.lang.String query, boolean exactMatch) 리소스 그룹과 검색어 타입에 따라 주어진 문자열 검색어와 일치하는 리소스를 검색 한다. 검색 결과로는 리소스 이름 리스트를 반환한다. 검색 타입(type) 지정 방밥은
- `C` - API의 `MC_termResSearch()` 함수의 정의를 따른다.

**매개 변수**

- `grp` - 리소스 그룹 이름
- `type` - 검색 타입
- `query` - 검색어
- `exactMatch` - 검색 방법(true 이면 검색어와 완전히 일치하는 리소스만 검색 한다.) 반환 값: 검색 결과를 리스트로 반환한다. 검색 결과가 존재하지 않
