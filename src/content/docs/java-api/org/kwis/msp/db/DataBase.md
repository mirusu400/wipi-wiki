---
title: "Class DataBase"
---

`package org.kwis.msp.db`

```text
java.lang.Object
  |
  +--org.kwis.msp.db.DataBase
```

## 설명

**extends Object:**

영속적인 데이터를 저장하고, 찾으며, 관리하기 위한 메카니즘을 제공합니다.

Jlet에서 간단한 데이터베이스를 구현하기 위한 클래스입니다.
 데이터베이스에는 여러개의 레코드(데이터)들이 저장되고 또 읽혀질 수 있습니다.

실제 레코드는 플랫폼의 영속적인 영역에 저장되어 Jlet이 수행이 종료
 되거나, 플랫폼이 다운되더라도 이미 저장된 레코드의 
 최소한의(예를 들어 레코드를 저장하는 중에 플랫폼이 다운 되었다면 
 해당 레코드의 무결성은 보장할 수 없습니다) 무결성은 보장됩니다

레코드는 바이트 어레이의 형태로 저장됩니다. 저장되는 데이터의 의미는 
 무시됩니다. 저장된 데이터의 논리적인 의미를 파악하는 것은 사용자의 
 몫입니다. 레코드의 크기는 처음 해당 데이터베이스를 생성할 때 지정한 
 크기를 초과할 수는 없습니다.

각각의 레코드는 데이터베이스 상에서 레코드 ID라는 Integer 값으로
 표현됩니다. 레코드 ID는 0부터 시작하며 레코드의 삭제가 없는 한 
 레코드 ID는 레코드를 하나 저장할 때 마다 1씩 증가합니다. 
 레코드가 중간에 삭제되면 다음 레코드를 저장할 때는
 삭제된 레코드 ID를 재사용합니다.

레코드의 빈번한 추가/삭제로 데이터베이스에 저장된 레코드의 개수와 
 데이터베이스가 실제 플랫폼의 파일시스템에 차지하는 용량이 차이가 
 날 수 있습니다. QTP는 이런 빈 공간을 없애는 메카니즘(compaction)은 
 제공하지 않습니다.

하나의 Jlet은 여러개의 데이터베이스를 생성할 수 있으며 한 Jlet은
 자신의 Jlet이 생성한 데이터베이스 모두에 접근이 가능합니다. 
 하지만 대부분의 경우 다른 Jlet이 생성한 데이터베이스에 접근할 
 수는 없습니다.

데이터베이스는 공유 디렉토리에 생성시키는 방법으로 여러 Jlet이 
 공유할 수도 있으며, 시스템 어플리케이션이 사용하는 데이터베이스에 
 접근할 수도 있습니다. 이는 데이터베이스를 오픈할 때 플래그를 줌으로써
 이루어집니다.

Jlet이 플랫폼 상에서 지워지면 데이터베이스도 삭제되며, 
 해당 데이터베이스가 플랫폼의 물리적인 영역에 생성한 
 자원들(주로 파일)도 동시에 삭제됩니다.

데이터베이스를 정렬하기 위해서 `DataFilter` 
 인터페이스와 `DataComparator` 인터페이스를 구현해야 합니다.
 전자는 정렬에 필요한 레코드를 골라내는 역할을 하며, 후자는 정렬을
 위해 레코드 두개를 비교하는 역할을 합니다.

## 메서드 요약

- `void closeDataBase ()` — 데이터베이스를 닫습니다.
- `static void deleteDataBase ( String dataBaseName)` — 데이터베이스를 삭제합니다.
- `static void deleteDataBase ( String dataBaseName, int flag)` — 데이터베이스를 삭제합니다.
- `void deleteRecord (int recordId)` — 레코드를 데이터베이스에서 삭제합니다.
- `static int getAccessMode ( String dbName)` — 데이터베이스의 접근 권한을 돌려줍니다.
- `String getDataBaseName ()` — 데이터베이스의 이름을 돌려줍니다.
- `int getDataBaseSize ()` — 데이터베이스의 크기를 돌려줍니다.
- `long getLastModified ()` — 데이터베이스가 가장 최근에 갱신된 시간을 돌려줍니다.
- `int getNumberOfRecords ()` — 데이터베이스에 저장된 레코드의 개수를 돌려줍니다.
- `int getRecordSize ()` — 데이터베이스의 하나의 레코드 크기를 돌려 줍니다.
- `int getSizeAvailable ()` — 앞으로 저장할 수 있는 남은 용량의 크기를 돌려줍니다.
- `int insertRecord (byte[] data)` — 새로운 레코드를 데이터베이스에 추가합니다.
- `int insertRecord (byte[] data, int offset, int numBytes)` — 새로운 레코드를 데이터베이스에 추가합니다.
- `static String [] listDataBases ()` — 데이터베이스의 이름의 어레이를 돌려줍니다.
- `static DataBase openDataBase ( String dataBaseName, int recordSize, boolean create)` — 데이터베이스를 엽니다.
- `static DataBase openDataBase ( String dataBaseName, int recordSize, boolean create, int flag)` — 데이터베이스를 엽니다.
- `byte[] selectRecord (int recordId)` — 특정 레코드 ID에 저장된 데이터를 돌려줍니다.
- `void selectRecord (int recordId, byte[] buffer, int offset)` — 특정 레코드 ID에 저장된 데이터를 돌려줍니다.
- `int[] sortRecord ( DataFilter filter, DataComparator comparator)` — 레코드를 정의한 비교 방법과 제한 조건으로 정렬합니다.
- `void updateRecord (int recordId, byte[] newData)` — 특정 레코드의 데이터의 내용을 바꿉니다.
- `void updateRecord (int recordId, byte[] newData, int offset, int numBytes)` — 특정 레코드의 데이터의 내용을 바꿉니다.

## 메서드 상세

### openDataBase

```java
public static DataBase openDataBase(String dataBaseName,
                                    int recordSize,
                                    boolean create)
                             throws DataBaseException,
                                    IllegalArgumentException
```

**Parameters:**
- `create` - 만약 데이터베이스가 존재하지 않으면 새로 만들 것인지 여부

**Returns:**
- 연 데이터베이스

**Throws:**
- `IllegalArgumentException` - `create`가 
 `true`인데, `recordSize`가 0이거나 음수인 경우

### openDataBase

```java
public static DataBase openDataBase(String dataBaseName,
                                    int recordSize,
                                    boolean create,
                                    int flag)
                             throws DataBaseException,
                                    IllegalArgumentException
```

**Parameters:**
- `flag` - 데이터베이스의 공유 방법을 지정, 
 `FileSystem.PRIVATE_ACCESS`, 
 `FileSystem.SHARED_ACCESS`, 
 `FileSystem.SYSTEM_ACCESS` 가능

**Returns:**
- 연 데이터베이스

**Throws:**
- `IllegalArgumentException` - `create`가 
 `true`인데, `recordSize`가 0이거나 음수인 경우

### closeDataBase

```java
public void closeDataBase()
                   throws DataBaseException
```

**Throws:**
- `DataBaseException` - 데이터베이스 관리 정보를 저장할 수 없거나 
 파일을 닫을 수 없는 경우

### deleteDataBase

```java
public static void deleteDataBase(String dataBaseName)
                           throws DataBaseException
```

**Parameters:**
- `dataBaseName` - 삭제할 데이터베이스 이름

**Throws:**
- `DataBaseException` - 삭제할 데이터베이스가 없거나 
 지우지 못한 경우

### deleteDataBase

```java
public static void deleteDataBase(String dataBaseName,
                                  int flag)
                           throws DataBaseException
```

**Parameters:**
- `flag` - 어떤 접근권한에 있는 데이터베이스를 지울 것인지를 나타냄,
 `FileSystem.PRIVATE_ACCESS`, 
 `FileSystem.SHARED_ACCESS`, 
 `FileSystem.SYSTEM_ACCESS` 가능.

**Throws:**
- `DataBaseException` - 삭제할 데이터베이스가 없거나 
 지우지 못한 경우

### insertRecord

```java
public int insertRecord(byte[] data,
                        int offset,
                        int numBytes)
                 throws DataBaseRecordException,
                        DataBaseException,
                        IllegalArgumentException
```

**Parameters:**
- `numBytes` - 저장할 바이트 수

**Returns:**
- 저장된 레코드의 레코드 ID

**Throws:**
- `IllegalArgumentException` - data의 길이에서 offset을 뺀 값이 numBytes 보다 작은 경우

### insertRecord

```java
public int insertRecord(byte[] data)
                 throws DataBaseRecordException,
                        DataBaseException
```

**Parameters:**
- `data` - 저장할 데이터가 들어있는 버퍼

**Returns:**
- 저장된 레코드의 레코드 ID

**Throws:**
- `DataBaseException` - 레코드를 저장할 수 없는 경우

### deleteRecord

```java
public void deleteRecord(int recordId)
                  throws DataBaseException,
                         DataBaseRecordException
```

**Parameters:**
- `recordId` - 지울 레코드의 ID

**Throws:**
- `DataBaseRecordException` - 레코드 ID가 없는 경우

### selectRecord

```java
public byte[] selectRecord(int recordId)
                    throws DataBaseException,
                           DataBaseRecordException
```

**Parameters:**
- `recordId` - 레코드 ID

**Returns:**
- 해당 레코드 ID에 저장된 데이터

**Throws:**
- `DataBaseRecordException` - 레코드 ID가 존재하지 않는 경우

### selectRecord

```java
public void selectRecord(int recordId,
                         byte[] buffer,
                         int offset)
                  throws DataBaseException,
                         DataBaseRecordException,
                         IllegalArgumentException
```

**Parameters:**
- `offset` - 버퍼에서 복사를 시작할 첫번째 바이트 오프셋

**Throws:**
- `DataBaseRecordException` - 레코드 ID가 존재하지 않는 경우

### updateRecord

```java
public void updateRecord(int recordId,
                         byte[] newData,
                         int offset,
                         int numBytes)
                  throws DataBaseRecordException,
                         DataBaseException,
                         IllegalArgumentException
```

**Parameters:**
- `numBytes` - 저장할 바이트 수

**Throws:**
