---
title: "3.1.3. 데이터베이스"
---

Interface DataComparator All Known Implementing Classes: DataComparatorInteger, DataComparatorString public interface DataComparator 두 개의 레코드를 비교하는 인터페이스이다. 데이터베이스를 정렬할 때 필요하며 그 때 sortRecord 메쏘드는 이 인터페이스에 있는 compare 메쏘드를 이용하여 데이터베이스의 각 레코드들끼리의 순서를 결정한다. 레코드를 정렬하려면 애플리케이션은 이 인터페이 스를 구현해 주어야 한다. 정수, 문자열 등 기본적인 비교를 위해서는 기 구현된 클래스 가 제공된다.

## 필드 상세

### EQUIVALENT

```java
public static final int EQUIVALENT
```

레코드 정렬이나 검색 시 파라미터로 받은 두 개의 레코드가 순서상 같다는 의미이 다.

### FOLLOWS

```java
public static final int FOLLOWS
```

레코드 정렬이나 검색 시 파라미터로 받은 첫 번째 레코드가 두 번째 레코드 다음에 온다는 의미이다.

### PRECEDES

```java
public static final int PRECEDES
```

레코드 정렬이나 검색 시 파라미터로 받은 두 번째 레코드가 첫 번째 레코드 다음에 온다는 의미이다.

## 메서드 상세

### compare

```java
public int compare(byte[] data1, byte[] data2)
```

레코드를 비교하는 메쏘드(비교자, comparator)이다. 파라미터로 넘어오는 바이트 어레이들은 데이터베이스에 저장된 레코드 데이터의 포맷을 따른다는 것을 염두하고 구현해야 한다.

**매개 변수**

- `data1` - 비교할 레코드의 데이터
- `data2` - 비교할 레코드의 데이터

**반환 값**

두 레코드가 순서상 같으면 DataComparator.EQUIVALENT, data2다음에 data1 이 오는 순서이면 (즉 data1이 data2를 따르는 순서이면) DataComparator.FOLLOWS, data1 다음에 data2가 오는 순서이면 DataComparator.PRECEDES Interface DataFilter All Known Implementing Classes: DataFilterInteger public interface DataFilter 정렬에 사용할 레코드를 제한한다. sortRecord 메쏘드로 데이터베이스의 레코드를 정렬할 때 해당 레코드를 정렬에 포함시킬 것인가를 결정한다. 정수, 문자열 등 기본적인 데이 터 형에 대한 DataFilter 를 위해서 기 구현된 클래스가 제공된다.

## 메서드 상세

### filter

```java
public boolean filter(byte[] data)
```

정렬에 사용할 레코드를 제한하는 메쏘드이다. 해당 레코드를 정렬에 사용할 것인지 를 결정한다. 구현할 때 파라미터로 넘어오는 바이트 어레이들은 데이터베이스에 저 장된 레코드 데이터의 포맷을 따른다는 것을 염두 해 두어야 한다.

**매개 변수**

- `data` - 레코드에 저장된 데이터를 나타내는 바이트 어레이

**반환 값**

해당 레코드가 정렬에 포함된다면 true, 아니면 false

---

## Class DataBase

```text
java.lang.Object
  +--org.kwis.msp.db.DataBase
```

```java
public class DataBase extends Object
```

영속적인 데이터를 저장하고, 찾으며, 관리하기 위한 메커니즘을 제공한다. Jlet에서 간단한 데이터베이스를 구현하기 위한 클래스이다. 데이터베이스에는 여러 개의 레코드(데이터)들이 저장되고 또 읽혀질 수 있다. 실제 레코드는 플랫폼의 영속적인 영역에 저장되어 Jlet이 수행이 종료 되거나, 플랫폼이 다운되더라도 이미 저장된 레코드의 최소한의(예를 들어 레코드를 저장하는 중에 플랫폼 이 다운 되었다면 해당 레코드의 무결성은 보장할 수 없다) 무결성은 보장된다 레코드는 바이트 어레이의 형태로 저장된다. 저장되는 데이터의 의미는 무시된다. 저장 된 데이터의 논리적인 의미를 파악하는 것은 사용자의 몫이다. 레코드의 크기는 처음 해 당 데이터베이스를 생성할 때 지정한 크기를 초과할 수는 없다. 각각의 레코드는 데이터베이스 상에서 레코드 ID라는 Integer 값으로 표현된다. 레코드 ID는 0부터 시작하며 레코드의 삭제가 없는 한 레코드 ID는 레코드를 하나 저장할 때 마다 1씩 증가한다. 레코드가 중간에 삭제되면 다음 레코드를 저장할 때는 삭제된 레코 드 ID를 재사용한다. 레코드의 빈번한 추가/삭제로 데이터베이스에 저장된 레코드의 개수와 데이터베이스가 실제 플랫폼의 파일시스템에 차지하는 용량이 차이가 날 수 있다. MSP는 이런 빈 공간 을 없애는 메커니즘(compaction)은 제공하지 않는다. 하나의 Jlet은 여러 개의 데이터베이스를 생성할 수 있으며 한 Jlet은 자신의 Jlet이 생성 한 데이터베이스 모두에 접근이 가능하다. 하지만 대부분의 경우 다른 Jlet이 생성한 데 이터베이스에 접근할 수는 없다. 데이터베이스는 공유 디렉토리에 생성시키는 방법으로 여러 Jlet이 공유할 수도 있으며, 시스템 어플리케이션이 사용하는 데이터베이스에 접근할 수도 있다. 이는 데이터베이스 를 오픈할 때 플래그를 줌으로써 이루어진다. Jlet이 플랫폼 상에서 지워지면 데이터베이스도 삭제되며, 해당 데이터베이스가 플랫폼의 물리적인 영역에 생성한 자원들(주로 파일)도 동시에 삭제된다. 데이터베이스를 정렬하기 위해서 DataFilter 인터페이스와 DataComparator 인터페이스를 구현해야 한다. 전자는 정렬에 필요한 레코드를 골라내는 역할을 하며, 후자는 정렬을 위해 레코드 두 개를 비교하는 역할을 한다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 메서드 상세

### openDataBase

```java
public static DataBase openDataBase(String dataBaseName, int recordSize, boolean create) throws DataBaseException,
```

IllegalArgumentException 데이터베이스를 연다. 이 데이터베이스는 현재의 Jlet만 접근할 수 있다. 데이터베 이스는 FileSystem.PRIVATE_ACCESS 모드로 열린다.

**매개 변수**

- `dataBaseName` - 데이터베이스 이름
- `recordSize` - 생성할 데이터베이스의 레코드 하나의 크기(byte단위). 데이터베이스가 이미 존재하는 경우 지정된 recordSize는 무시되고 기존의 레코드 크기가 적용됨
- `create` - 만약 데이터베이스가 존재하지 않으면 새로 만들 것인지 여부

**반환 값**

연 데이터베이스 Throws DataBaseException create가 false인데 데이터베이스가 없거나 데이터 베이스에 사용되는 파일을 열수 없거나 데이터베이스 가 깨어진 경우 IllegalArgumentException create가 true인데, recordSize가 0이거나 음수 인 경우

### openDataBase

```java
public static DataBase openDataBase(String dataBaseName, int recordSize, boolean create, int flag) throws DataBaseException,
```

IllegalArgumentException 데이터베이스를 연다. 현재의 Jlet만 접근할 수 있게 할 것인지, 다른 Jlet과 공유 되는 데이터베이스를 열 것인지, 시스템이 제공하는 데이터베이스를 사용할 것인지 flag를 통해 지정할 수 있다.

**매개 변수**

- `dataBaseName` - 데이터베이스 이름
- `recordSize` - 생성할 데이터베이스의 레코드 하나의 크기(byte단위). 데이터베이스가 이미 존재하는 경우 지정된 recordSize는 무시되고 기존의 레코드 크기가 적용됨
- `create` - 만약 데이터베이스가 존재하지 않으면 새로 만들 것인지 여부
- `flag` - 데이터베이스의 공유 방법을 지정, FileSystem.PRIVATE_ACCESS, FileSystem.SHARED_ACCESS, FileSystem.SYSTEM_ACCESS 가능

**반환 값**

연 데이터베이스 Throws DataBaseException create가 false인데 데이터베이스가 없거나 데이터 베이스에 사용되는 파일을 열수 없거나 데이터베이스 가 깨어진 경우 IllegalArgumentException create가 true인데, recordSize가 0이거나 음수 인 경우

### closeDataBase

```java
public void closeDataBase() throws DataBaseException
```

데이터베이스를 닫다. Throws DataBaseException 데이터베이스 관리 정보를 저장할 수 없거나 파일을 닫을 수 없는 경우

### deleteDataBase

```java
public static void deleteDataBase(String dataBaseName) throws DataBaseException
```

데이터베이스를 삭제한다. 해당 Jlet이 FileSystem.PRIVATE_ACCESS로 생성한 데이터 베이스만 삭제할 수 있다.

**매개 변수**

- `dataBaseName` - 삭제할 데이터베이스 이름 Throws
- `DataBaseException` - 삭제할 데이터베이스가 없거나 지우지 못한 경우 deleteDataBase

### deleteDataBase

```java
public static void deleteDataBase(String dataBaseName, int flag)
```

- `throws` - DataBaseException 데이터베이스를 삭제한다. 해당 Jlet이 flag로 접근 가능한 데이터베이스만 삭제 가 능하다.

**매개 변수**

- `dataBaseName` - 삭제할 데이터베이스 이름
- `flag` - 어떤 접근권한에 있는 데이터베이스를 지울 것인지를 나타냄, FileSystem.PRIVATE_ACCESS, FileSystem.SHARED_ACCESS, FileSystem.SYSTEM_ACCESS 가능. Throws
- `DataBaseException` - 삭제할 데이터베이스가 없거나 지우지 못한 경우 insertRecord

### insertRecord

```java
public int insertRecord(byte[] data, int offset, int numBytes) throws DataBaseRecordException,
```

DataBaseException, IllegalArgumentException 새로운 레코드를 데이터베이스에 추가한다. 바이트 어레이에 저장된 데이터를 하나 의 레코드로 데이터베이스에 저장한다. 데이터는 리턴되기 전에 플랫폼의 물리적 영 역에 쓰여진다. 저장할 바이트 어레이의 길이가 데이터베이스를 생성할 때 지정한 레코드 크기보다 작으면, 남는 영역에 쓰레기값(garbage)이 저장되어 있을 수 있다.
- `selectRecord는` - 레코드 크기 단위로 읽어오기 때문에, 저장한 후에 다시 읽어 들인 바이트 어레이에서 실제 데이터와 쓰레기값(garbage)를 구별하는 것은 사용자 몫이 다.

**매개 변수**

- `data` - 저장할 데이터가 들어있는 버퍼
- `offset` - 버퍼에서 저장할 데이터가 시작되는 첫 번째 바이트 오프셋
- `numBytes` - 저장할 바이트 수

**반환 값**

저장된 레코드의 레코드 ID Throws DataBaseRecordException 데이터가 데이터베이스 생성시에 지정한 레코 드 크기보다 큰 경우 DataBaseException 레코드를 저장할 수 없는 경우 IllegalArgumentException data의 길이에서 offset을 뺀 값이 numBytes 보다 작은 경우

### insertRecord

```java
public int insertRecord(byte[] data) throws DataBaseRecordException,
```

DataBaseException 새로운 레코드를 데이터베이스에 추가한다. 바이트 어레이에 저장된 데이터를 하나 의 레코드로 데이터베이스에 저장한다. 데이터는 리턴되기 전에 플랫폼의 물리적 영 역에 쓰여진다. 저장할 바이트 어레이의 길이가 데이터베이스를 생성할 때 지정한 레코드 크기보다 작으면, 남는 영역에 쓰레기값(garbage)이 저장되어 있을 수 있다. selectRecord는 레코드 크기 단위로 읽어오기 때문에, 저장한 후에 다시 읽어 들인 바이트 어레이에서 실제 데이터와 쓰레기값(garbage)를 구별하는 것은 사용자 몫이 다.

**매개 변수**

- `data` - 저장할 데이터가 들어있는 버퍼

**반환 값**

저장된 레코드의 레코드 ID Throws DataBaseRecordException 데이터가 데이터베이스 생성시에 지정한 레코 드 크기보다 큰 경우 DataBaseException 레코드를 저장할 수 없는 경우

### deleteRecord

```java
public void deleteRecord(int recordId) throws DataBaseException,
```

DataBaseRecordException 레코드를 데이터베이스에서 삭제한다. 파라미터로 받은 레코드 ID에 해당하는 레코 드를 지운다.

**매개 변수**

- `recordId` - 지울 레코드의 ID Throws
- `DataBaseException` - 레코드를 지울 수 없는 경우
- `DataBaseRecordException` - 레코드 ID가 없는 경우 selectRecord

### selectRecord

```java
public byte[] selectRecord(int recordId) throws DataBaseException,
```

DataBaseRecordException 특정 레코드 ID에 저장된 데이터를 돌려준다.

**매개 변수**

- `recordId` - 레코드 ID

**반환 값**

해당 레코드 ID에 저장된 데이터 Throws DataBaseException 레코드를 읽을 수 없는 경우 DataBaseRecordException 레코드 ID가 존재하지 않는 경우

### selectRecord

```java
public void selectRecord(int recordId, byte[] buffer, int offset) throws DataBaseException,
```

DataBaseRecordException, IllegalArgumentException 특정 레코드 ID에 저장된 데이터를 돌려준다. 읽어 들인 데이터는 버퍼에 복사되어 돌려진다. 뒤에 버퍼의 내용을 바꾸더라도 데이터베이스에 저장된 레코드는 변하지 않는다. 버퍼는 하나의 레코드가 들어갈 수 있을 만큼 충분히 커야 한다. 데이터베 이스의 하나의 레코드의 크기는 getRecordSize 메쏘드를 통해 알아올 수 있다.

**매개 변수**

- `recordId` - 레코드 ID
- `buffer` - 읽어 들인 데이터를 복사하여 저장할 버퍼
- `offset` - 버퍼에서 복사를 시작할 첫 번째 바이트 오프셋 Throws
- `IllegalArgumentException` - 버퍼가 레코드 크기보다 작은 경우
- `DataBaseException` - 레코드를 읽을 수 없는 경우
- `DataBaseRecordException` - 레코드 ID가 존재하지 않는 경우 updateRecord
- `public` - void updateRecord(int recordId, byte[] newData, int offset,
- `int` - numBytes) throws DataBaseRecordException, DataBaseException, IllegalArgumentException 특정 레코드의 데이터의 내용을 바꾼다. 해당 레코드 ID에 저장되어 있던 내용을 새 로운 내용으로 바꾼다.

**매개 변수**

- `recordId` - 데이터 내용을 변경시킬 레코드 ID
- `newData` - 새로이 저장할 데이터가 들어있는 버퍼
- `offset` - 버퍼에서 저장할 데이터가 시작되는 첫 번째 바이트 오프셋
- `numBytes` - 저장할 바이트 수 Throws
- `DataBaseException` - 데이터를 저장 할 수 없는 경우
- `DataBaseRecordException` - 데이터가 데이터베이스 생성시에 지정한 레코 드 크기보다 크거나 레코드 ID가 존재하지 않 는 경우
- `IllegalArgumentException` - 버퍼의 길이에서 오프셋을 뺀 값이 저장할 바이트 수 보다 작은 경우 updateRecord

### updateRecord

```java
public void updateRecord(int recordId, byte[] newData)
```

- `throws` - DataBaseException, DataBaseRecordException 특정 레코드의 데이터의 내용을 바꾼다. 해당 레코드 ID에 저장되어 있던 내용을 새 로운 내용으로 바꾼다.

**매개 변수**

- `recordId` - 데이터 내용을 변경시킬 레코드 ID
- `newData` - 새로이 저장할 데이터가 들어있는 버퍼 Throws
- `DataBaseException` - 데이터를 저장 할 수 없는 경우
- `DataBaseRecordException` - 데이터가 데이터베이스 생성시에 지정한 레코 드 크기보다 크거나 레코드 ID가 존재하지 않 는 경우 sortRecord

### sortRecord

```java
public int[] sortRecord(DataFilter filter, DataComparator comparator)
```

- `throws` - DataBaseException 레코드를 정의한 비교 방법과 제한 조건으로 정렬한다. 레코드 비교 방법은 DataComparator 인터페이스를 구현하여 정의할 수 있다.
- `DataComparator는` - 두 개의 레코드를 비교하는 클래스이다. 만약 comparator가 null 이면 정렬되지 않은 레코드 ID를 돌려 준다. 레코드 제한 조건은 DataFilter 인터페이스를 구현하여 정의할 수 있으며 조건을 만 족하는 레코드만 정렬에 사용한다. 만약 filter가 null이면 제한 조건이 없는 것으 로 간주하여 데이터베이스의 모든 레코드를 정렬에 사용한다. 요약하면 filter만 null인 경우 모든 레코드를 지정한 comparator로 정렬해서 그 레 코드 ID 리스트를 돌려주며 comparator만 null 인 경우 filter 가 지정한 조건을 만 족하는 레코드의 레코드 ID 리스트를 돌려준다. filter와 comparator 모두 null인 경우 데이터베이스에 저장된 모든 레코드 ID를 정렬하지 않고 돌려 준다. 정수의 범위 조건과 문자열의 조건은 미리 구현되어 있는 클래스를 사용할 수 있다 (DataFilterInteger, DataComparatorInteger.) 이 메쏘드는 레코드의 ID를 가지고 있는 정수 어레이를 돌려준다. 각각의 레코드를 얻어오기 위해서는 알아낸 레코드 ID를 이용하여 selectRecord 메쏘드를 사용할 수 있다.

**매개 변수**

- `filter` - 레코드 제한 조건. null이 될 수 있음
- `comparator` - 레코드 비교 방법. null이 될 수 있음

**반환 값**

정렬된 레코드 ID의 어레이. 레코드가 없으면 null Throws DataBaseException 레코드를 정렬할 수 없는 경우

### listDataBases

```java
public static String[] listDataBases()
```

데이터베이스의 이름의 어레이를 돌려준다. 해당 Jlet이 FileSystem.PRIVATE_ACCESS 로 생성된 모든 데이터베이스의 이름과 FileSystem.SHARED_ACCESS, FileSystem.SYSTEM_ACCESS로 생성된 데이터베이스 중 접근 가능한 데이터베이스의 이름을 돌려준다.

**반환 값**

데이터베이스의 이름들, 존재하지 않으면 null

### getAccessMode

```java
public static int getAccessMode(String dbName) throws DataBaseException
```

데이터베이스의 접근 권한을 돌려준다.

**매개 변수**

- `dbName` - 접근 권한을 알아볼 데이터베이스 이름

**반환 값**

FileSystem.PRIVATE_ACCESS, FileSystem.SHARED_ACCESS, FileSystem.SYSTEM_ACCESS 중 한 가지 Throws DataBaseException 데이터베이스가 존재하지 않거나 dbName이 null인 경 우

### getDataBaseName

```java
public String getDataBaseName()
```

데이터베이스의 이름을 돌려준다. 오픈된 인스턴스의 데이터베이스 이름을 돌려준다.

**반환 값**

데이터베이스의 이름

### getDataBaseSize

```java
public int getDataBaseSize()
```

데이터베이스의 크기를 돌려준다. 돌려주는 값은 데이터베이스에 저장된 레코드의 크기와 저장과, 관리에 필요한 크기까지 포함된 크기이다. 따라서 돌려지는 값은, 데이터베이스에 저장된 실제 레코드 개수와 레코드 하나의 크기를 곱한 값과 다를 수 있다(보통 더 큰 값이 리턴된다.)

**반환 값**

데이터베이스의 물리적인 크기

### getNumberOfRecords

```java
public int getNumberOfRecords()
```

데이터베이스에 저장된 레코드의 개수를 돌려준다.

**반환 값**

레코드 개수

### getRecordSize

```java
public int getRecordSize()
```

데이터베이스의 하나의 레코드 크기를 돌려 준다. 레코드의 저장에 필요한 오버헤드 (overhead)는 포함되지 않는다.

**반환 값**

하나의 레코드의 크기(byte)

### getSizeAvailable

```java
public int getSizeAvailable()
```

앞으로 저장할 수 있는 남은 용량의 크기를 돌려준다. 저장되는 레코드는 레코드 관 리, 저장에 필요한 오버헤드(overhead)가 있으므로 실제 데이터의 크기가 남은 용량 보다 작더라도 저장하지 못할 수 있다. 하드웨어의 크기에 따라 달라질 수 있다.

**반환 값**

남은 용량(byte 단위)

### getLastModified

```java
public long getLastModified()
```

데이터베이스가 가장 최근에 갱신된 시간을 돌려준다. System.currentTimeMillis() 가 리턴하는 포맷이다.

**반환 값**

최근 갱신된 시간

---

## Class DataComparatorInteger

```text
java.lang.Object
  +--org.kwis.msp.db.DataComparatorInteger
```

*All Implemented Interfaces: DataComparator*

```java
public class DataComparatorInteger extends Object implements DataComparator
```

두 개의 레코드를 정수로 비교하는 클래스이다. 데이터베이스의 sortRecord메쏘드를 호 출할 때 필요하다. Fields inherited from interface org.kwis.msp.db.DataComparator EQUIVALENT, FOLLOWS, PRECEDES

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 생성자 상세

### DataComparatorInteger

```java
public DataComparatorInteger(int offset)
```

두 개의 레코드를 정수로 비교하는 클래스이다. 데이터베이스에서 sortRecord 메쏘드를 호출 할 때 DataComparator 인터페이스를 구 현한 클래스로 이 클래스, 즉 DataComparatorInteger를 넘길 수 있다. 그럼 sortRecord는 이 클래스 생성시 넘겨지는 오프셋을 시작으로 레코드의 4 바이트를 정수로 생각하고 레코드를 정렬한다. 바이트 순서는 빅엔디안(big-endian)이다. sortRecord 호출 시에 필요로 한다.

**매개 변수**

- `offset` - 레코드에서 비교할 정수가 시작되는 바이트 오프셋 메쏘드 상세 설명 compare

### compare

```java
public int compare(byte[] data1, byte[] data2)
```

레코드를 비교하는 메쏘드(비교자, comparator)이다. 파라미터로 넘어오는 바이트 어레이들은 데이터베이스에 저장된 레코드 데이터의 포맷을 따른다는 것을 염두하고 구현해야 한다.

**매개 변수**

- `data1` - 비교할 레코드의 데이터
- `data2` - 비교할 레코드의 데이터

**반환 값**

두 레코드가 순서상 같으면 DataComparator.EQUIVALENT, data2다음에 data1 이 오는 순서이면 (즉 data1이 data2를 따르는 순서이면) DataComparator.FOLLOWS, data1 다음에 data2가 오는 순서이면 DataComparator.PRECEDES

---

## Class DataComparatorString

```text
java.lang.Object
  +--org.kwis.msp.db.DataComparatorString
```

*All Implemented Interfaces: DataComparator*

```java
public class DataComparatorString extends Object implements DataComparator
```

두 개의 레코드를 문자열로 비교하는 클래스이다. 데이터베이스의 sortRecord메쏘드를 호출할 때 필요하다. Fields inherited from interface org.kwis.msp.db.DataComparator EQUIVALENT, FOLLOWS, PRECEDES

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 생성자 상세

### DataComparatorString

```java
public DataComparatorString(int offset)
```

두 개의 레코드를 문자열로 비교하는 클래스이다. 데이터베이스에서 sortRecord 메쏘드를 호출 할 때 DataComparator 인터페이스를 구 현한 클래스로 이 클래스, 즉 DataComparatorString을 넘길 수 있다. 그럼 sortRecord는 이 클래스 생성시 넘겨지는 오프셋을 시작점으로 바이트 어레이를 String으로 변환하여 비교를 수행한다. sortRecord 호출 시에 필요로 한다.

**매개 변수**

- `offset` - 레코드에서 비교할 문자열이 시작되는 바이트 오프셋 메쏘드 상세 설명 compare

### compare

```java
public int compare(byte[] data1, byte[] data2)
```

레코드를 비교하는 메쏘드(비교자, comparator)이다. 파라미터로 넘어오는 바이트 어레이들은 데이터베이스에 저장된 레코드 데이터의 포맷을 따른다는 것을 염두하고 구현해야 한다.

**매개 변수**

- `data1` - 비교할 레코드의 데이터
- `data2` - 비교할 레코드의 데이터

**반환 값**

두 레코드가 순서상 같으면 DataComparator.EQUIVALENT, data2다음에 data1 이 오는 순서이면 (즉 data1이 data2를 따르는 순서이면) DataComparator.FOLLOWS, data1 다음에 data2가 오는 순서이면 DataComparator.PRECEDES

---

## Class DataFilterInteger

```text
java.lang.Object
  +--org.kwis.msp.db.DataFilterInteger
```

*All Implemented Interfaces: DataFilter*

```java
public class DataFilterInteger extends Object implements DataFilter
```

정렬에 사용할 레코드를 한정한다. 정수로 정렬할 때 사용한다. 레코드의 데이터인 바이트 어레이에서, 특정 오프셋에 저장 된 데이터가 정수(int)라 가정하고, 이 값이 일정 범위(min, max로 지정된)에 속한 레코드 만 정렬에 포함한다. sortRecord 메쏘드를 호출할 때 사용한다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 필드 상세

offset protected int offset 비교할 오프셋 min protected int min 최소값 max protected int max 최대값

## 생성자 상세

### DataFilterInteger

```java
public DataFilterInteger(int offset, int min, int max) throws IllegalArgumentException
```

정렬에 사용할 레코드를 한정한다. 정수로 정렬할 때 사용한다. 레코드의 데이터에서 특정 위치(offset)를 정수 값으로 보고, 이 레코드가 최대값(max), 최소값(min)으로 표현되는 범위에 있는가를 나타낸 다. 모든 바이트 순서는 빅엔디안(big-endian)을 따른다, sortRecord시에 특정 값의 범위에 속하는 레코드만 정렬하기 원할 때 이 세팅된 값을 사용된다.

**매개 변수**

- `offset` - 비교할 오프셋
- `min` - 최소값. Integer.MIN_VALUE이면 max 이하를 의미
- `max` - 최대값. Integer.MAX_VALUE 이면 min 이상을 의미 Throws
- `IllegalArgumentException` - offset이 음수이거나 min, max가 제대로 주어지지 않은 경우 메쏘드 상세 설명 filter

### filter

```java
public boolean filter(byte[] data)
```

정렬에 사용할 레코드를 제한하는 메쏘드이다. 해당 레코드를 정렬에 사용할 것인지 를 결정한다. 구현할 때 파라미터로 넘어오는 바이트 어레이들은 데이터베이스에 저 장된 레코드 데이터의 포맷을 따른다는 것을 염두 해 두어야 한다.

**매개 변수**

- `data` - 레코드에 저장된 데이터를 나타내는 바이트 어레이

**반환 값**

해당 레코드가 정렬에 포함된다면 true, 아니면 false

---

## Class DataBaseException

```text
java.lang.Object
  +--java.lang.Throwable
    +--java.lang.Exception
      +--org.kwis.msp.db.DataBaseException
```

```java
public class DataBaseException extends Exception
```

데이터베이스와 관련된 일반적인 예외 상황에서 발생한다.

*Methods inherited from class java.lang.Throwable: getMessage, printStackTrace, toString*

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, wait, wait, wait*

## 생성자 상세

### DataBaseException

```java
public DataBaseException(String message)
```

새 DataBaseException 인스턴스를 메시지와 함께 생성한다.

**매개 변수**

- `message` - 예외에 대한 자세한 메시지. DataBaseException

### DataBaseException

```java
public DataBaseException()
```

새 DataBaseException 인스턴스를 생성한다.
- `Class` - DataBaseRecordException java.lang.Object | +--java.lang.Throwable | +--java.lang.Exception | +--org.kwis.msp.db.DataBaseRecordException
- `public` - class DataBaseRecordException extends Exception 데이터베이스의 레코드와 관련된 일반적인 예외 상황에서 발생한다.
- `Methods` - inherited from class java.lang.Throwable getMessage, printStackTrace, toString
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명 DataBaseRecordException

### DataBaseRecordException

```java
public DataBaseRecordException(String message)
```

새 DataBaseRecordException 인스턴스를 메시지와 함께 생성한다.

**매개 변수**

- `message` - 예외에 대한 자세한 메시지. DataBaseRecordException

### DataBaseRecordException

```java
public DataBaseRecordException()
```

새 DataBaseRecord 인스턴스를 생성한다.
