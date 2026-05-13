# 5.1.3. 데이터베이스

데이터베이스 함수.

데이터를 레코드 단위로 저장하고, 찾으며 관리하기 위한 API 들이다.

레코드는 문자 어레이의 형태로 저장된다. 저장되는 데이터의 의미는 무시된다. 저장된 데이터의 논리적인 의미를 파악하는 것은 사용자의 몫이다. 레코드 크기는 처음 데이터베이스를 생성할 때 지정한 크기를 초과할 수 없다.

각 레코드는 데이터베이스 상에서 레코드 식별자라는 정수값으로 표현된다. 레코 드가 중간에 삭제되면 다음 레코드를 저장할 때 삭제된 레코드 식별자를 재사용한 다. 레코드 식별자는 음수가 될 수 없다.

레코드의 빈번한 추가/삭제로 데이터베이스에 저장된 레코드의 개수와 데이터베이 스가 실제 플랫폼의 물리적인 영역에 저장된 용량이 차이가 날 수 있다.

하나의 응용 프로그램은 여러개의 데이터베이스를 생성할 수 있으며 자신이 생성 한 데이터베이스 모두에 접근이 가능한다. 하지만 대부분의 경우 다른 응용프로그 램이 생성한 데이터베이스에 접근할 수 없다. 데이터베이스를 공유디렉토리에 생 성시키는 방법으로 여러 응용프로그램이 공유할 수도 있으며, 해당 응용프로그램 이 권한이 있다면 시스템 프로그램이 사용하는 데이터베이스에 접근할 수 있다. 이는 데이터베이스를 열 때 플래그를 지정해서 이루어진다.

모든 데이터베이스 함수는 함수의 수행이 끝난 후에 반환된다. 예를 들어 MC_dbInsertRecord 함수의 경우 데이터가 물리적인 저장영역에 쓰여진 후에 반환된 다. 따라서 이 함수가 반환된 즉시 MC_dbSelectRecord 로 바로 이전에 저장한 레코 드를 가져 올 수 있다.

응용프로그램이 종료되더라도 데이터베이스는 수행이 종료된 시점의 상태대로 보 존되어 다음 수행시에 이용할 수 있다. 하지만 응용프로그램이 플랫폼 상에서 지 워지면 해당 응용프로그램이 생성한 데이터베이스는 삭제된다.

**참고 항목**

없음

```c
MC_dbOpenDataBase 설명
```

데이터베이스를 연다.

데이터베이스의 공유 모드는 플래그로 지정할 수 있다. 고정크기의 레코드만 지원 한다. 레코드는 연속된 문자 어레이로 표현되며 레코드의 논리적인 의미는 데이터 베이스 사용자가 파악하고 있어야 한다.

**프로토타입**

```c
M_Int32 MC_dbOpenDataBase(M_Char* dataBaseName, M_Int32 recordSize, M_Boolean create, M_Int32 mode)
```

**매개 변수**

- `dataBaseName` — 데이터베이스 이름, 이름으로 쓸 수 있는 문자는 파일 시스템의 제한사항을 따른다.
- `recordSize` — 생성할 데이터베이스의 레코드 하나의 크기(byte 단위). 데이터베이 스가 이미 존재하는 경우 지정된 recordSize 는 무시되고 기존의 레코드 크기가 적 용됨
- `create` — 만약 데이터베이스가 존재하지 않으면 새로 만들 것인지 여부
- `mode` — 데이터베이스의  공유  방법을  지정,  DIR_PRIVATE_ACCESS,

DIR_SHARED_ACCESS, DIR_SYSTEM_ACCESS 중 하나가 가능

**반환 값**

성공

실패

**부작용**

없음

**참고 항목**

데이터베이스 식별자(0 보다 큰 정수)

M_E_NOENT - create 가 거짓인데 데이터베이스가 존재하지 않는 경우 M_E_INVALID - create 가 참인데 recordSize 가 0 이거나 음수인 경우, dataBaseName 이 NULL 인 경우, mode 가 위에서 기술한 셋 중 하나가 아닌 경우

M_E_ERROR - 기타 데이터베이스를 열 수 없는 경우

```c
MC_dbCloseDataBase
MC_fsOpen
MC_dbCloseDataBase 설명
```

데이터베이스를 닫는다.

**프로토타입**

```c
M_Int32 MC_dbCloseDataBase(M_Int32 dbId)
```

**매개 변수**

- `dbId` — 데이터베이스 식별자

**반환 값**

성공

실패

**부작용**

없음

**참고 항목**

M_E_BADFD - 데이터베이스 식별자가 잘못된 경우 M_E_ERROR - 기타 이유로 실패할 경우

```c
MC_dbOpenDataBase
MC_dbDeleteDataBase 설명
```

데이터베이스를 삭제한다.

해당 응용프로그램이 접근 가능한 데이터베이스만 삭제가 가능한다. 열려있는 데 이터베이스는 삭제할 수 없다.

**프로토타입**

```c
M_Int32 MC_dbDeleteDataBase(M_Char* dataBaseName, M_Int32 mode)
```

**매개 변수**

- `dataBaseName` — 삭제할 데이터베이스 이름
- `mode` — 어떤	접근권한에	있는	데이터베이스를	지울	것인지를	나타냄,

DIR_PRIVATE_ACCESS , DIR_SHARED_ACCESS, DIR_SYSTEM_ACCESS 중 하나가 가능

**반환 값**

성공

실패

**부작용**

없음

**참고 항목**

M_E_NOENT - 데이터베이스가 존재하지 않는 경우 M_E_INUSE - 데이터베이스가 닫혀 있지 않은 경우

M_E_INVALID - dataBaseName 이 NULL 이거나, mode 가 위에서 기술한 셋 중 하나가 아닌 경우

M_E_ACCESS – 접근 권한이 없는 데이터베이스를 지우려 하는 경우 M_E_ERROR - 기타 이유로 실패할 경우

```c
MC_dbCloseDataBase
MC_fsOpen
MC_dbInsertRecord 설명
```

새로운 레코드를 데이터베이스에 추가한다.

버퍼에 저장된 데이터를 하나의 레코드로 데이터베이스에 저장한다. 저장할 버퍼 의 크기가 데이터베이스를 생성할 때 지정한 레코드 크기보다 작으면, 남는 영역 에 쓰레기값(garbage)이 저장되어 있을 수 있다.

MC_dbSelectRecord 는 레코드 크기 단위로 데이터를 읽어오기 때문에 레코드 크기보 다 작은 데이터를 저장했다면, 이후 다시 읽어들인 문자 어레이에서 실제 데이터 뒤에 쓰레기값(garbage)이 들어 있을 수 있다.

**프로토타입**

```c
M_Int32 MC_dbInsertRecord(M_Int32 dbId, M_Byte* buf, M_Int32 len)
```

**매개 변수**

- `dbId` — 레코드를 추가할 데이터베이스 식별자 buf - 데이터가 저장되어 있는 버퍼
- `len` — 저장할 데이터의 크기

**반환 값**

성공

실패

**부작용**

없음

**참고 항목**

레코드 식별자(0 보다 큰 정수)

M_E_BADFD - 데이터베이스 식별자가 잘못된 경우

M_E_DATABIG - 데이터베이스의 레코드 크기보다 더 큰 데이터를 저장하려 하는 경우

M_E_INVALID - len 이 0 이거나 음수인 경우, buf 가 NULL 인 경우 M_E_ERROR - 기타 데이터를 저장할 수 없는 경우

```c
MC_dbSelectRecord MC_dbUpdateRecord MC_dbDeleteRecord
MC_dbSelectRecord 설명
```

특정 레코드 식별자에 저장된 데이터를 돌려준다.

읽어들인 데이터는 버퍼에 복사되어 돌려진다. 이 함수를 호출한 이후에 버퍼의 내용을 바꾸더라도 데이터베이스에 저장된 레코드는 변하지 않는다. 버퍼의 크기 는 해당 데이터베이스의 레코드 크기보다 크거나 같아야 한다. 데이터베이스의 하 나의 레코드의 크기는 MC_dbGetRecordSize 함수로 알아올 수 있다.

**프로토타입**

```c
M_ Int32 MC_dbSelectRecord(M_Int32 dbId, M_Int32 recId, M_Byte* buf, M_Int32 len)
```

**매개 변수**

- `dbId` — 데이터베이스 식별자 recId - 레코드 식별자
- `buf` — 데이터를 받을 버퍼 len - 버퍼의 길이

**반환 값**

성공

실패

**부작용**

없음

**참고 항목**

M_E_BADFD - 데이터베이스 식별자가 잘못된 경우 M_E_BADRECID - 해당 레코드 식별자가 존재하지 않는 경우

M_E_INVALID - len 이 0 이거나 음수인 경우, buf 가 NULL 인 경우 M_E_SHORTBUF - 주어진 버퍼가 레코드 크기보다 작은 경우 M_E_ERROR - 기타 이유로 레코드를 읽어올 수 없는 경우

```c
MC_dbInsertRecord MC_dbUpdateRecord MC_dbDeleteRecord
MC_dbUpdateRecord 설명
```

특정 레코드의 데이터의 내용을 바꾼다. 해당 레코드 식별자에 저장되어 있던 내 용을 새로운 내용으로 바꾼다.

**프로토타입**

```c
M_ Int32 MC_dbUpdateRecord(M_Int32 dbId, M_Int32 recId, M_Byte* buf, M_Int32 len)
```

**매개 변수**

- `dbId` — 데이터베이스 식별자
- `recId` — 데이터 내용을 변경시킬 레코드 식별자 buf - 새로이 저장할 데이터가 들어있는 버퍼 len - 버퍼의 크기

**반환 값**

성공

실패

**부작용**

없음

**참고 항목**

M_E_BADFD 데이터베이스 식별자가 잘못된 경우 M_E_BADRECID - 해당 레코드 식별자가 존재하지 않는 경우

M_E_DATABIG - 갱신하려는 데이터가 데이터베이스 생성시에 지정한 레코 드 크기보다 큰 경우

M_E_INVALID - len 이 0 이거나 음수인 경우, buf 가 NULL 인 경우 M_E_ERROR - 기타 이유로 레코드를 갱신할 수 없는 경우

```c
MC_dbInsertRecord MC_dbSelectRecord MC_dbDeleteRecord
MC_dbDeleteRecord 설명
```

레코드를 데이터베이스에서 삭제한다.

매개변수로 받은 레코드 식별자에 해당하는 레코드를 지운다.

**프로토타입**

```c
M_Int32 MC_dbDeleteRecord(M_Int32 dbId, M_Int32 recId)
```

**매개 변수**

- `dbId` — 데이터베이스 식별자 recId - 지울 레코드의 식별자

**반환 값**

성공

실패

**부작용**

없음

**참고 항목**

M_E_BADFD - 데이터베이스 식별자가 잘못된 경우 M_E_BADRECID - 해당 레코드 식별자가 존재하지 않는 경우 M_E_ERROR - 기타 이유로 레코드를 지울 수 없는 경우

```c
MC_dbInsertRecord MC_dbSelectRecord MC_dbUpdateRecord
MC_dbListRecords 설명
```

데이터베이스에 저장된 레코드들의 레코드 식별자를 돌려준다.

매개변수로 받은 정수형 배열에 데이터베이스에 저장된 레코드들의 레코드 식별자 를 저장해서 돌려준다. 돌려지는 레코드 식별자의 순서는 실제 레코드를 저장한 순서와 다를 수 있다.

**프로토타입**

```c
M_Int32 MC_dbListRecords(M_Int32 dbID, M_Int32* buf, M_Int32 len)
```

**매개 변수**

- `dbId` — 데이터베이스 식별자
- `buf` — 받아온 레코드 식별자를 저장할 버퍼 len - 버퍼의 크기

**반환 값**

성공

실패

**부작용**

없음

**참고 항목**

레코드 개수

M_E_BADFD - 데이터베이스 식별자가 잘못된 경우

M_E_INVALID - len 이 0 이거나 음수인 경우, buf 가 NULL 인 경우 M_E_SHORTBUF - 레코드 식별자를 받아올 버퍼가 너무 작은 경우 M_E_ERROR - 기타 이유로 실패한 경우

```c
MC_dbSortRecords
MC_dbSortRecords 설명
```

데이터베이스에 저장된 레코드들의 정렬된 레코드 식별자를 돌려준다. 각 레코드를 바이트별로 비교해 정렬한다.

예를 들어 어떤 데이터베이스의 레코드 크기가 2 이고 아래와 같이 4 개의 레코드 가 저장되어 있다면,

============================

| 레코드식별자 |	데이터	|

============================

|

|

0x33

0x22

|

|

|

0x11

0x22

|

|

|

0x22

0xff

|

|

|

0x11

0xff

|

============================

*

이 함수를 호출하면 매개변수로 받은 정수형 버퍼에 1, 3, 2, 0 순서로 레코드 식 별자가 저장되어 돌려지며 4(레코드 개수)가 반환된다(매개 변수인 compare 와 filter 를 모두 NULL 로 넣은 경우).

응용 프로그램 작성자가 정렬 방법을 지정하거나 정렬에 사용할 레코드를 제한하 는 기능은 이 함수의 매개 변수를 사용해 구현할 수 있다.

정렬할 때 두 개의 레코드의 순서를 정하는 방법을 compare 를 구현해 지정할 수 있다. compare 가 받는 매개 변수는 데이터베이스에 저장한 레코드이다. 이 함수 는 두 개의 레코드를 비교해서 첫번째 매개변수로 받은 레코드가 두번째 매개변수 로 받은 레코드보다 앞에 오면 0 보다 큰 정수를, 뒤에 오면 0 보다 작은 정수를, 두 개의 순서가 동일하면 0 을 반환해야 한다.

filter 는 특정 레코드를 정렬에 포함시킬 것인지 결정하는 함수이다. 레코드를 정렬에 포함시키려면 0 보다 큰 정수를, 정렬에서 제외하려면 0 을 반환해야 한다. filter 가 받는 매개 변수도 레코드이다.

함수를 호출한다 하더라도 저장된 데이터베이스의 구조는 변하지 않는다.

**프로토타입**

```c
M_Int32 MC_dbSortRecords(M_Int32 dbID, M_Int32* buf, M_Int32 len, M_Int32 (*compare)(const void *, const void *), M_Int32 (*filer)(const void *))
```

**매개 변수**

- `dbId` — 데이터베이스 식별자

### buf - 받아온 레코드 식별자들를 저장할 버퍼 len - 버퍼의 크기

### compare – 두 레코드를 비교하기 위한 함수 포인터, NULL 이면 앞의 예제처 럼 각 byte 별로 올림차순으로 정렬됨

- `filter` — 정렬에 사용할 레코드를 제한하는 함수 포인터, NULL이면 모든 레코드 를 정렬에 사용함 반환 값

성공

실패

**부작용**

없음

**참고 항목**

레코드 개수

M_E_BADFD - 데이터베이스 식별자가 잘못된 경우

M_E_INVALID - len 이 0 이거나 음수인 경우, buf 가 NULL 인 경우 M_E_SHORTBUF - 레코드 식별자를 받아올 버퍼가 너무 작은 경우 M_E_ERROR - 기타 이유로 실패한 경우

```c
MC_dbListRecords
MC_dbGetAccessMode 설명
```

데이터베이스의 접근 권한을 돌려 준다.

해당 응용프로그램이 생성한 데이터베이스와, 서로 공유할 수 있는 데이터베이스, 시스템에서 사용하는 데이터베이스의 접근권한을 알아 볼 수 있다. 단 해당 응용 프로그램이 접근할 수 있는 데이터베이스만 접근 권한을 알아 볼 수 있다.

**프로토타입**

```c
M_Int32 MC_dbGetAccessMode(M_Char* dataBaseName)
```

**매개 변수**

- `dataBaseName` — 접근 권한을 알아볼 데이터베이스 이름

**반환 값**

성공

값 실패

**부작용**

없음

**참고 항목**

DIR_PRIVATE_ACCESS, DIR_SHARED_ACCESS, DIR_SYSTEM_ACCESS  중  한가지

M_E_NOENT - 데이터베이스가 존재하지 않는 경우 M_E_INVALID - dataBaseName 이 NULL 인 경우 M_E_ERROR - 기타 이유로 실패한 경우

```c
MC_dbOpenDataBase MC_fsOpen
MC_dbGetNumberOfRecords 설명
```

데이터베이스에 저장된 레코드 개수를 돌려준다.

**프로토타입**

```c
M_Int32 MC_dbGetNumberOfRecords(M_Int32 dbId)
```

**매개 변수**

- `dbId` — 데이터베이스 식별자

**반환 값**

성공

실패

**부작용**

없음

**참고 항목**

없음

레코드 개수

M_E_BADFD - 데이터베이스 식별자가 잘못된 경우 M_E_ERROR - 기타 이유로 실패한 경우

```c
MC_dbGetRecordSize 설명
```

데이터베이스의 하나의 레코드 크기를 돌려준다.

**프로토타입**

```c
M_Int32 MC_dbGetRecordSize(M_Int32 dbId)
```

**매개 변수**

- `dbId` — 데이터베이스 식별자

**반환 값**

성공

실패

**부작용**

없음

**참고 항목**

레코드의 크기(byte)

M_E_BADFD - 데이터베이스 식별자가 잘못된 경우 M_E_ERROR - 기타 이유로 실패한 경우

```c
MC_dbOpenDataBase
MC_dbListDataBases 설명
```

데이터베이스의 이름의 어레이를 돌려준다.

DIR_PRIVATE_ACCESS 로 생성한 데이터베이스와 DIR_SHARED_ACCESS, DIR_SYSTEM_ACCESS 로 생성한 데이터베이스 중 응용프로그램이 접근 가능한 데이 터베이스의 이름을 돌려준다. 버퍼를 통해 돌려지는 각각의 데이터베이스는 NULL(\0)로 구분이 되며 리스트의 끝은 두개의 연속된 NULL 로 표현된다.

**프로토타입**

```c
M_Int32 MC_dbListDataBases(M_Byte* buf, M_Int32 len)
```

**매개 변수**

- `buf` — 데이터베이스 이름을 저장할 버퍼 len - 버퍼의 크기

**반환 값**

성공

실패

**부작용**

없음

**참고 항목**

데이터베이스의 개수(데이터베이스가 하나도 없는 경우도 성공한 것으로 간주함)

M_E_SHORTBUF - 어레이를 받아오기에 버퍼가 너무 작은 경우 M_E_INVALID - len 이 0 이거나 음수인 경우, buf 가 NULL 인 경우 M_E_ERROR - 기타 이유로 실패한 경우

```c
MC_dbOpenDataBase MC_fsOpen
```
