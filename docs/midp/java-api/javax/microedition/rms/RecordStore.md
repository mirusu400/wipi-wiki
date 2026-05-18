# Class RecordStore

`package javax.microedition.rms`

```text
java.lang.Object
  |
  +--javax.microedition.rms.RecordStore
```

## 설명

**extends Object:**

레코드 저장소를 나타내는 클래스. 
레코드 저장소는 MIDlet을 여러 번 호출하는 경우에도 
영구적으로 남아 있는 레코드의 모음으로 구성되어 있습니다. 
플랫폼에서는 재부트, 배터리 변경 등을 포함하는 
플랫폼의 정상적 사용에 대해 MIDlet 레코드 저장소의 무결성을 
최대한 유지할 수 있도록 해야 합니다.

레코드 저장소는 플랫폼에 따라 다른 위치에 만들어지며 
이러한 위치는 MIDlet에 제공되지 않습니다. 
레코드 저장소의 이름 지정 공간은 MIDlet Suite 단위로 제어됩니다. 
MIDlet Suite 내 MIDlet은 이름만 다르게 지정하면 
여러 레코드 저장소를 만들 수 있습니다. 
MIDlet Suite가 플랫폼에서 제거되면 해당 MIDlet에 연관된 
모든 레코드 저장소도 제거됩니다. 
MIDlet Suite 내의 MIDlet은 서로 다른 레코드 저장소에 
직접 액세스할 수 있습니다. RecordStore를 만드는 MIDlet이 이러한 권한을 
제공하도록 선택하면 MIDP 2.0의 새 API가 레코드 저장소를 명시적으로 공유할 수 있습니다.

공유는 다른 MIDlet Suite가 만든 RecordStore를 지정하는 기능을 
사용하여 수행됩니다.

RecordStore는 MIDlet Suite의 고유 이름과 
RecordStore의 이름을 사용하여 고유하게 지정됩니다. 
응용 프로그램 설명자의 MIDlet-Vendor 및 MIDlet-Name 속성이 
MIDlet Suite를 식별합니다.

공유할 RecordStore를 만들 때 액세스 컨트롤이 정의됩니다. 
액세스 컨트롤은 RecordStore를 열 때 적용됩니다. 
액세스 모드는 다른 MIDlet Suite와 공유할 수 있거나 
개인 사용을 허용합니다.

레코드 저장소 이름은 대소문자를 구분하고 
최대 32자의 유니코드 문자 조합으로 구성될 수 있습니다. 
레코드 저장소 이름은 주어진 MIDlet Suite 범위 내에서 고유해야 합니다. 
즉, 하나의 MIDlet Suite에 있는 여러 MIDlet은 동일한 이름을 갖는 
레코드 저장소를 둘 이상 만들 수 없지만, 
하나의 MIDlet Suite에 있는 하나의 MIDlet은 
다른 MIDlet Suite의 MIDlet과 동일한 이름을 갖는 
레코드 저장소를 가질 수 있습니다. 
이럴 경우에도 레코드 저장소는 여전히 고유하고 구분되어 있습니다.

이 API에는 잠금 작업이 제공되지 않습니다. 
레코드 저장소 구현 시 모든 개별 레코드 저장소 작업이 최소 단위이고 
동기적이며 일련화되어 있는지 확인하여 
다중 액세스로 손상이 발생하지 않도록 합니다. 
하지만 MIDlet이 다중 스레드를 사용하여 레코드 저장소를 액세스하면 
MIDlet에서 이 액세스를 조정해야 하며, 
그렇지 않은 경우 예상치 못한 결과가 발생할 수 있습니다. 
마찬가지로, 플랫폼이 레코드 저장소의 투명한 동기화를 수행하면 
해당 플랫폼에서 MIDlet과 동기화 엔진 사이의 레코드 저장소에 대한 
배타적 액세스를 적용해야 합니다.

레코드는 주어진 레코드 저장소 내에서 정수 값인 
recordId로 고유하게 식별됩니다. 
이 recordId는 레코드의 기본 키로 사용됩니다. 
레코드 저장소에서 만든 첫 번째 레코드의 recordId는 1입니다. 
RecordStore에 추가되는 이후 레코드에는 전에 추가된 레코드에 비해 
1만큼 큰 recordId가 할당됩니다. 
즉, 두 개의 레코드가 레코드 저장소에 추가되는 경우 
첫 번째 레코드의 recordId가 'n'이면 다음 레코드의 recordId는 'n + 1'이 됩니다. 
MIDlet은 `RecordEnumeration` 클래스를 사용하여 
RecordStore에 다른 순서의 레코드를 만들 수 있습니다.

이 레코드 저장소는 시간/날짜 스탬프에 대해 
System.currentTimeMillis()에서 사용하는 형식의 long형 정수를 사용합니다. 
레코드 저장소는 수정된 마지막 시간을 타임 스탬프로 사용합니다. 
레코드 저장소는 RecordStore의 내용을 수정할 때마다 증가하는 정수인 
*버전* 번호를 유지합니다. 
이러한 특성은 동기화 엔진뿐 아니라 
다른 응용 프로그램에도 유용합니다.

**Since:**
- MIDP 1.0

## 필드 요약

- `static int AUTHMODE_ANY` — MIDlet Suite에 대한 액세스를 허용하는 인증.
- `static int AUTHMODE_PRIVATE` — 현재 MIDlet Suite에만 액세스를 허용하는 인증.

## 메서드 요약

- `int addRecord (byte[] data, int offset, int numBytes)` — 레코드 저장소에 새 레코드를 추가합니다.
- `void addRecordListener ( RecordListener listener)` — 지정된 RecordListener를 추가합니다.
- `void closeRecordStore ()` — 레코드 저장소를 갖는 MIDlet 요청이 닫힐 때 이 메소드가 호출됩니다.
- `void deleteRecord (int recordId)` — 레코드가 레코드 저장소에서 삭제됩니다.
- `static void deleteRecordStore ( String recordStoreName)` — 명명된 레코드 저장소를 삭제합니다.
- `RecordEnumeration enumerateRecords ( RecordFilter filter, RecordComparator comparator, boolean keepUpdated)` — 선택적으로 지정된 순서로 레코드 저장소의 레코드 집합을 순회하는 열거를 반환합니다.
- `long getLastModified ()` — 레코드 저장소가 수정된 마지막 시간을 System.currentTimeMillis()에서 사용하는 형식으로 반환합니다.
- `String getName ()` — 이 RecordStore의 이름을 반환합니다.
- `int getNextRecordID ()` — 레코드 저장소에 추가될 다음 레코드의 recordId를 반환합니다.
- `int getNumRecords ()` — 레코드 저장소의 현재 레코드 수를 반환합니다.
- `byte[] getRecord (int recordId)` — 주어진 레코드에 저장된 데이터의 복사본을 반환합니다.
- `int getRecord (int recordId, byte[] buffer, int offset)` — 주어진 레코드에 저장된 데이터를 반환합니다.
- `int getRecordSize (int recordId)` — 주어진 레코드에서 사용할 수 있는 MIDlet 데이터의 크기(바이트)를 반환합니다.
- `int getSize ()` — 레코드 저장소가 차지하고 있는 바이트 단위의 공간 크기를 반환합니다.
- `int getSizeAvailable ()` — 레코드 저장소 증가에 사용할 수 있는 추가 공간(바이트)의 양을 반환합니다.
- `int getVersion ()` — addRecord , setRecord 또는 deleteRecord 메소드가 레코드 저장소를 수정할 때마다 버전 이 증가합니다.
- `static String [] listRecordStores ()` — MIDlet Suite가 소유한 레코드 저장소의 이름 배열을 반환합니다.
- `static RecordStore openRecordStore ( String recordStoreName, boolean createIfNecessary)` — 주어진 MIDlet Suite에 연관된 레코드 저장소를 엽니다(또는 만듭니다).
- `static RecordStore openRecordStore ( String recordStoreName, boolean createIfNecessary, int authmode, boolean writable)` — 다른 MIDlet Suite와 공유할 수 있는 레코드 저장소를 엽니다(또는 만듭니다).
- `static RecordStore openRecordStore ( String recordStoreName, String vendorName, String suiteName)` — 명명된 MIDlet Suite에 연관된 레코드 저장소를 엽니다.
- `void removeRecordListener ( RecordListener listener)` — 지정된 RecordListener를 제거합니다.
- `void setMode (int authmode, boolean writable)` — 이 RecordStore의 액세스 모드를 변경합니다.
- `void setRecord (int recordId, byte[] newData, int offset, int numBytes)` — 전달된 레코드에 데이터를 설정합니다.

## 필드 상세

### AUTHMODE_PRIVATE

```java
public static final int AUTHMODE_PRIVATE
```

**See Also:**
- `Constant Field Values`

### AUTHMODE_ANY

```java
public static final int AUTHMODE_ANY
```

**See Also:**
- `Constant Field Values`

### deleteRecordStore

```java
public static void deleteRecordStore(String recordStoreName)
                              throws RecordStoreException,
                                     RecordStoreNotFoundException
```

**Parameters:**
- `recordStoreName` - 삭제할 MIDlet Suite 
고유 레코드 저장소

**Throws:**
- `RecordStoreNotFoundException` - 레코드 저장소를 
찾을 수 없는 경우

### openRecordStore

```java
public static RecordStore openRecordStore(String recordStoreName,
                                          boolean createIfNecessary)
                                   throws RecordStoreException,
                                          RecordStoreFullException,
                                          RecordStoreNotFoundException
```

**Parameters:**
- `createIfNecessary` - true인 경우 필요하면 
레코드 저장소를 만듭니다.

**Returns:**
- 레코드 저장소의 `RecordStore` 객체

**Throws:**
- `IllegalArgumentException` - recordStoreName이 
유효하지 않은 경우

### openRecordStore

```java
public static RecordStore openRecordStore(String recordStoreName,
                                          boolean createIfNecessary,
                                          int authmode,
                                          boolean writable)
                                   throws RecordStoreException,
                                          RecordStoreFullException,
                                          RecordStoreNotFoundException
```

**Parameters:**
- `writable` - 액세스를 부여할 수 있는 
다른 MIDlet Suite에서 RecordStore를 쓸 수 있으면 true. 
RecordStore가 존재하면 이 인자는 무시됩니다.

**Returns:**
- 레코드 저장소의 `RecordStore` 객체

**Throws:**
- `IllegalArgumentException` - authmode 또는 
recordStoreName이 유효하지 않은 경우

**Since:**
- MIDP 2.0

### openRecordStore

```java
public static RecordStore openRecordStore(String recordStoreName,
                                          String vendorName,
                                          String suiteName)
                                   throws RecordStoreException,
                                          RecordStoreNotFoundException
```

**Parameters:**
- `suiteName` - MIDlet Suite의 이름

**Returns:**
- 레코드 저장소의 `RecordStore` 객체

**Throws:**
- `IllegalArgumentException` - recordStoreName이 
유효하지 않은 경우

**Since:**
- MIDP 2.0

### setMode

```java
public void setMode(int authmode,
                    boolean writable)
             throws RecordStoreException
```

**Parameters:**
- `writable` - 액세스를 부여할 수 있는 다른 MIDlet Suite에서 
RecordStore를 쓸 수 있으면 true

**Throws:**
- `IllegalArgumentException` - authmode가 유효하지 않은 경우

**Since:**
- MIDP 2.0

### closeRecordStore

```java
public void closeRecordStore()
                      throws RecordStoreNotOpenException,
                             RecordStoreException
```

**Throws:**
- `RecordStoreException` - 다른 레코드 저장소 관련 
예외가 발생한 경우

### listRecordStores

```java
public static String[] listRecordStores()
```

**Returns:**
- MIDlet Suite가 소유한 레코드 저장소의 이름 배열. 
MIDlet Suite에 레코드 저장소가 없는 경우 
이 함수는 null을 반환합니다.

### getName

```java
public String getName()
               throws RecordStoreNotOpenException
```

**Returns:**
- 이 RecordStore의 이름

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 열려 있지 않은 경우

### getVersion

```java
public int getVersion()
               throws RecordStoreNotOpenException
```

**Returns:**
- 현재 레코드 저장소 버전

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

### getNumRecords

```java
public int getNumRecords()
                  throws RecordStoreNotOpenException
```

**Returns:**
- 레코드 저장소의 현재 레코드 수

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

### getSize

```java
public int getSize()
            throws RecordStoreNotOpenException
```

**Returns:**
- 바이트 단위의 레코드 저장소 크기

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

### getSizeAvailable

```java
public int getSizeAvailable()
                     throws RecordStoreNotOpenException
```

**Returns:**
- 이 레코드 저장소의 증가에 사용할 수 있는 
추가 공간의 양(바이트)

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

### getLastModified

```java
public long getLastModified()
                     throws RecordStoreNotOpenException
```

**Returns:**
- System.currentTimeMillis()에서 사용하는 형식의 
레코드 저장소가 수정된 마지막 시간

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

### addRecordListener

```java
public void addRecordListener(RecordListener listener)
```

**Parameters:**
- `listener` - RecordChangedListener

**See Also:**
- ``removeRecordListener(javax.microedition.rms.RecordListener)``

### removeRecordListener

```java
public void removeRecordListener(RecordListener listener)
```

**Parameters:**
- `listener` - RecordChangedListener

**See Also:**
- ``addRecordListener(javax.microedition.rms.RecordListener)``

### getNextRecordID

```java
public int getNextRecordID()
                    throws RecordStoreNotOpenException,
                           RecordStoreException
```

**Returns:**
- 레코드 저장소에 추가될 다음 레코드의 
recordId

**Throws:**
- `RecordStoreException` - 다른 레코드 저장소 관련 
예외가 발생한 경우

### addRecord

```java
public int addRecord(byte[] data,
                     int offset,
                     int numBytes)
              throws RecordStoreNotOpenException,
                     RecordStoreException,
                     RecordStoreFullException
```

**Parameters:**
- `numBytes` - 이 레코드에 사용할 데이터 버퍼의 
바이트 수(0일 수 있음)

**Returns:**
- 새 레코드의 recordId

**Throws:**
- `SecurityException` - MIDlet에 RecordStore에 대한 
읽기 전용 액세스가 있는 경우

### deleteRecord

```java
public void deleteRecord(int recordId)
                  throws RecordStoreNotOpenException,
                         InvalidRecordIDException,
                         RecordStoreException
```

**Parameters:**
- `recordId` - 삭제할 레코드 ID

**Throws:**
- `SecurityException` - MIDlet에 RecordStore에 대한 
읽기 전용 액세스가 있는 경우

### getRecordSize

```java
public int getRecordSize(int recordId)
                  throws RecordStoreNotOpenException,
                         InvalidRecordIDException,
                         RecordStoreException
```

**Parameters:**
- `recordId` - 이 작업에서 사용할 레코드 ID

**Returns:**
- 주어진 레코드에서 사용할 수 있는 
MIDlet 데이터의 크기(바이트)

**Throws:**
- `RecordStoreException` - 일반 레코드 저장소 
예외가 발생한 경우

### getRecord

```java
public int getRecord(int recordId,
                     byte[] buffer,
                     int offset)
              throws RecordStoreNotOpenException,
                     InvalidRecordIDException,
                     RecordStoreException
```

**Parameters:**
- `offset` - 복사를 시작할 버퍼의 색인

**Returns:**
- 색인 `offset`에서 시작하여 버퍼에 
복사한 바이트 수

**Throws:**
- `ArrayIndexOutOfBoundsException` - 레코드가 제공된 버퍼보다 
큰 경우

**See Also:**
- ``setRecord(int, byte[], int, int)``

### getRecord

```java
public byte[] getRecord(int recordId)
                 throws RecordStoreNotOpenException,
                        InvalidRecordIDException,
                        RecordStoreException
```

**Parameters:**
- `recordId` - 이 작업에서 사용할 레코드 ID

**Returns:**
- 주어진 레코드에 저장된 데이터. 레코드에 데이터가 없는 경우 
이 메소드는 null을 반환합니다.

**Throws:**
- `RecordStoreException` - 일반 레코드 저장소 
예외가 발생한 경우

**See Also:**
- ``setRecord(int, byte[], int, int)``

### setRecord

```java
public void setRecord(int recordId,
                      byte[] newData,
                      int offset,
                      int numBytes)
               throws RecordStoreNotOpenException,
                      InvalidRecordIDException,
                      RecordStoreException,
                      RecordStoreFullException
```

**Parameters:**
- `numBytes` - 이 레코드에 사용할 
데이터 버퍼의 바이트 수

**Throws:**
- `SecurityException` - MIDlet에 RecordStore에 대한 
읽기 전용 액세스가 있는 경우

**See Also:**
- ``getRecord(int, byte[], int)``

### enumerateRecords

```java
public RecordEnumeration enumerateRecords(RecordFilter filter,
                                          RecordComparator comparator,
                                          boolean keepUpdated)
                                   throws RecordStoreNotOpenException
```

**Parameters:**
- `keepUpdated` - true인 경우 열거자는 
레코드 저장소 레코드의 변경 사항을 
사용하여 열거를 최신 상태로 유지합니다. 
성능 관련 문제가 생길 수 있으므로 
주의해서 사용합니다. 
false인 경우 열거는 최신 상태로 유지되지 않으며 삭제된 레코드의 
레코드 ID를 반환하거나 나중에 추가된 
레코드를 누락시킬 수 있습니다. 
열거가 만들어진 후 수정된 순서와 
상관 없이 레코드를 반환할 수도 있습니다. 
레코드 저장소의 레코드에 대한 변경 내용은 나중에 레코드를 
직접 검색하거나 열거를 통해 
검색할 때 정확하게 반영됩니다. 
이 매개 변수를 false로 설정할 때 주의해야 할 점은 레코드가 
수정, 추가 또는 삭제될 때 열거의 필터링 및 정렬 순서입니다.

**Returns:**
- 선택적으로 지정된 순서로 레코드 
저장소의 레코드 집합을 순회하는 열거

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

**See Also:**
- ``RecordEnumeration.rebuild()``

## 메서드 상세

### deleteRecordStore

```java
public static void deleteRecordStore(String recordStoreName)
                              throws RecordStoreException,
                                     RecordStoreNotFoundException
```

**Parameters:**
- `recordStoreName` - 삭제할 MIDlet Suite 
고유 레코드 저장소

**Throws:**
- `RecordStoreNotFoundException` - 레코드 저장소를 
찾을 수 없는 경우

### openRecordStore

```java
public static RecordStore openRecordStore(String recordStoreName,
                                          boolean createIfNecessary)
                                   throws RecordStoreException,
                                          RecordStoreFullException,
                                          RecordStoreNotFoundException
```

**Parameters:**
- `createIfNecessary` - true인 경우 필요하면 
레코드 저장소를 만듭니다.

**Returns:**
- 레코드 저장소의 `RecordStore` 객체

**Throws:**
- `IllegalArgumentException` - recordStoreName이 
유효하지 않은 경우

### openRecordStore

```java
public static RecordStore openRecordStore(String recordStoreName,
                                          boolean createIfNecessary,
                                          int authmode,
                                          boolean writable)
                                   throws RecordStoreException,
                                          RecordStoreFullException,
                                          RecordStoreNotFoundException
```

**Parameters:**
- `writable` - 액세스를 부여할 수 있는 
다른 MIDlet Suite에서 RecordStore를 쓸 수 있으면 true. 
RecordStore가 존재하면 이 인자는 무시됩니다.

**Returns:**
- 레코드 저장소의 `RecordStore` 객체

**Throws:**
- `IllegalArgumentException` - authmode 또는 
recordStoreName이 유효하지 않은 경우

**Since:**
- MIDP 2.0

### openRecordStore

```java
public static RecordStore openRecordStore(String recordStoreName,
                                          String vendorName,
                                          String suiteName)
                                   throws RecordStoreException,
                                          RecordStoreNotFoundException
```

**Parameters:**
- `suiteName` - MIDlet Suite의 이름

**Returns:**
- 레코드 저장소의 `RecordStore` 객체

**Throws:**
- `IllegalArgumentException` - recordStoreName이 
유효하지 않은 경우

**Since:**
- MIDP 2.0

### setMode

```java
public void setMode(int authmode,
                    boolean writable)
             throws RecordStoreException
```

**Parameters:**
- `writable` - 액세스를 부여할 수 있는 다른 MIDlet Suite에서 
RecordStore를 쓸 수 있으면 true

**Throws:**
- `IllegalArgumentException` - authmode가 유효하지 않은 경우

**Since:**
- MIDP 2.0

### closeRecordStore

```java
public void closeRecordStore()
                      throws RecordStoreNotOpenException,
                             RecordStoreException
```

**Throws:**
- `RecordStoreException` - 다른 레코드 저장소 관련 
예외가 발생한 경우

### listRecordStores

```java
public static String[] listRecordStores()
```

**Returns:**
- MIDlet Suite가 소유한 레코드 저장소의 이름 배열. 
MIDlet Suite에 레코드 저장소가 없는 경우 
이 함수는 null을 반환합니다.

### getName

```java
public String getName()
               throws RecordStoreNotOpenException
```

**Returns:**
- 이 RecordStore의 이름

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 열려 있지 않은 경우

### getVersion

```java
public int getVersion()
               throws RecordStoreNotOpenException
```

**Returns:**
- 현재 레코드 저장소 버전

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

### getNumRecords

```java
public int getNumRecords()
                  throws RecordStoreNotOpenException
```

**Returns:**
- 레코드 저장소의 현재 레코드 수

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

### getSize

```java
public int getSize()
            throws RecordStoreNotOpenException
```

**Returns:**
- 바이트 단위의 레코드 저장소 크기

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

### getSizeAvailable

```java
public int getSizeAvailable()
                     throws RecordStoreNotOpenException
```

**Returns:**
- 이 레코드 저장소의 증가에 사용할 수 있는 
추가 공간의 양(바이트)

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

### getLastModified

```java
public long getLastModified()
                     throws RecordStoreNotOpenException
```

**Returns:**
- System.currentTimeMillis()에서 사용하는 형식의 
레코드 저장소가 수정된 마지막 시간

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

### addRecordListener

```java
public void addRecordListener(RecordListener listener)
```

**Parameters:**
- `listener` - RecordChangedListener

**See Also:**
- ``removeRecordListener(javax.microedition.rms.RecordListener)``

### removeRecordListener

```java
public void removeRecordListener(RecordListener listener)
```

**Parameters:**
- `listener` - RecordChangedListener

**See Also:**
- ``addRecordListener(javax.microedition.rms.RecordListener)``

### getNextRecordID

```java
public int getNextRecordID()
                    throws RecordStoreNotOpenException,
                           RecordStoreException
```

**Returns:**
- 레코드 저장소에 추가될 다음 레코드의 
recordId

**Throws:**
- `RecordStoreException` - 다른 레코드 저장소 관련 
예외가 발생한 경우

### addRecord

```java
public int addRecord(byte[] data,
                     int offset,
                     int numBytes)
              throws RecordStoreNotOpenException,
                     RecordStoreException,
                     RecordStoreFullException
```

**Parameters:**
- `numBytes` - 이 레코드에 사용할 데이터 버퍼의 
바이트 수(0일 수 있음)

**Returns:**
- 새 레코드의 recordId

**Throws:**
- `SecurityException` - MIDlet에 RecordStore에 대한 
읽기 전용 액세스가 있는 경우

### deleteRecord

```java
public void deleteRecord(int recordId)
                  throws RecordStoreNotOpenException,
                         InvalidRecordIDException,
                         RecordStoreException
```

**Parameters:**
- `recordId` - 삭제할 레코드 ID

**Throws:**
- `SecurityException` - MIDlet에 RecordStore에 대한 
읽기 전용 액세스가 있는 경우

### getRecordSize

```java
public int getRecordSize(int recordId)
                  throws RecordStoreNotOpenException,
                         InvalidRecordIDException,
                         RecordStoreException
```

**Parameters:**
- `recordId` - 이 작업에서 사용할 레코드 ID

**Returns:**
- 주어진 레코드에서 사용할 수 있는 
MIDlet 데이터의 크기(바이트)

**Throws:**
- `RecordStoreException` - 일반 레코드 저장소 
예외가 발생한 경우

### getRecord

```java
public int getRecord(int recordId,
                     byte[] buffer,
                     int offset)
              throws RecordStoreNotOpenException,
                     InvalidRecordIDException,
                     RecordStoreException
```

**Parameters:**
- `offset` - 복사를 시작할 버퍼의 색인

**Returns:**
- 색인 `offset`에서 시작하여 버퍼에 
복사한 바이트 수

**Throws:**
- `ArrayIndexOutOfBoundsException` - 레코드가 제공된 버퍼보다 
큰 경우

**See Also:**
- ``setRecord(int, byte[], int, int)``

### getRecord

```java
public byte[] getRecord(int recordId)
                 throws RecordStoreNotOpenException,
                        InvalidRecordIDException,
                        RecordStoreException
```

**Parameters:**
- `recordId` - 이 작업에서 사용할 레코드 ID

**Returns:**
- 주어진 레코드에 저장된 데이터. 레코드에 데이터가 없는 경우 
이 메소드는 null을 반환합니다.

**Throws:**
- `RecordStoreException` - 일반 레코드 저장소 
예외가 발생한 경우

**See Also:**
- ``setRecord(int, byte[], int, int)``

### setRecord

```java
public void setRecord(int recordId,
                      byte[] newData,
                      int offset,
                      int numBytes)
               throws RecordStoreNotOpenException,
                      InvalidRecordIDException,
                      RecordStoreException,
                      RecordStoreFullException
```

**Parameters:**
- `numBytes` - 이 레코드에 사용할 
데이터 버퍼의 바이트 수

**Throws:**
- `SecurityException` - MIDlet에 RecordStore에 대한 
읽기 전용 액세스가 있는 경우

**See Also:**
- ``getRecord(int, byte[], int)``

### enumerateRecords

```java
public RecordEnumeration enumerateRecords(RecordFilter filter,
                                          RecordComparator comparator,
                                          boolean keepUpdated)
                                   throws RecordStoreNotOpenException
```

**Parameters:**
- `keepUpdated` - true인 경우 열거자는 
레코드 저장소 레코드의 변경 사항을 
사용하여 열거를 최신 상태로 유지합니다. 
성능 관련 문제가 생길 수 있으므로 
주의해서 사용합니다. 
false인 경우 열거는 최신 상태로 유지되지 않으며 삭제된 레코드의 
레코드 ID를 반환하거나 나중에 추가된 
레코드를 누락시킬 수 있습니다. 
열거가 만들어진 후 수정된 순서와 
상관 없이 레코드를 반환할 수도 있습니다. 
레코드 저장소의 레코드에 대한 변경 내용은 나중에 레코드를 
직접 검색하거나 열거를 통해 
검색할 때 정확하게 반영됩니다. 
이 매개 변수를 false로 설정할 때 주의해야 할 점은 레코드가 
수정, 추가 또는 삭제될 때 열거의 필터링 및 정렬 순서입니다.

**Returns:**
- 선택적으로 지정된 순서로 레코드 
저장소의 레코드 집합을 순회하는 열거

**Throws:**
- `RecordStoreNotOpenException` - 레코드 저장소가 
열려 있지 않은 경우

**See Also:**
- ``RecordEnumeration.rebuild()``
