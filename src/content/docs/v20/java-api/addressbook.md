---
title: "3.1.7. 주소록"
---

---

## Class Address

```text
java.lang.Object
  +--org.kwis.msp.handset.Address
```

```java
public static class Address extends java.lang.Object
```

주소록의 개별 주소 레코드를 나타내는 클래스이다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 메서드 상세

### getRecordId

```java
public int getRecordId()
```

주소 객체의 레코드 아이디

**반환 값**

주소 객체의 레코드 아이디

### getField

```java
public Object getField(int fieldIndex)
```

주소 객체의 필드값을 얻어온다

**매개 변수**

- `fieldIndex` - 주소 필드의 인덱스

**반환 값**

주소 객체의 필드 객체

### setField

```java
public boolean setField(int fieldIndex, Object field)
```

필드를 설정한다.

**매개 변수**

- `fieldIndex` - 주소 필드의 인덱스 field

**반환 값**

true 필드값 변경 성공 false 필드값 변경 실패

### getFields

```java
public Object[] getFields()
```

복수개의 필드를 가져온다

**반환 값**

필드 객체의 배열

### setFields

```java
public boolean setFields(Object[] fields)
```

복수개의 필드를 설정한다.

**매개 변수**

- `fields` - 필드 객체의 배열

**반환 값**

true 필드값 변경 성공 false 필드값 변경 실패

### getLockStatus

```java
public int getLockStatus()
```

주소 객체의 Lock 상태를 반환한다. Lock status에는 LOCKED, UNLOCKED가 있다.

**반환 값**

Lock status를 리턴한다.

### setLockStatus

```java
public int setLockStatus(int status)
```

주소 객체의 Lock을 설정/해제한다.

**매개 변수**

- `status` - Lock status (LOCKED, UNLOCKED)

**반환 값**

성공하면 0, 아니면 에러코드 (음수)

---

## Class AddressBook

```text
java.lang.Object
  +--org.kwis.msp.handset.AddressBook
```

```java
public static class AddressBook extends java.lang.Object
```

단말의 주소록에 접근하기 위한 클래스이다.

*Methods inherited from class java.lang.Object: equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait*

## 필드 상세

SEARCH_NAME public static final int SEARCH_NAME 검색 기준 필드가 이름이 될 경우 사용 SEARCH_PHONE_NO public static final int SEARCH_PHONE_NO 검색 기준 필드가 전화번호가 될 경우 사용 SEARCH_EMAIL public static final int SEARCH_EMAIL 검색 기준 필드가 E-Mail 주소가 될 경우 사용 SEARCH_GROUP public static final int SEARCH_GROUP 검색 기준 필드가 그룹이 될 경우 사용 TYPE_INT public static int TYPE_INT 필드의 타입. 필드가 숫자임을 나타낸다. TYPE_STRING public static int TYPE_STRING 필드의 타입. 필드가 문자열임을 나타낸다. TYPE_IMAGE public static int TYPE_IMAGE 필드의 타입. 필드가 이미지 데이터임을 나타낸다. TYPE_SOUND public static int TYPE_SOUND 필드의 타입. 필드가 오디오 클립임을 나타낸다. TYPE_BINARY public static int TYPE_BINARY 필드의 타입. 필드가 이진 데이터임을 나타낸다. getAddressBook static
```java
public AddressBook getAddressBook()
```

Global한 AddressBook 인스턴스를 가져온다 .

**반환 값**

Global한 AddressBook 객체

## 메서드 상세

### getGroupCount

```java
public int getGroupCount()
```

주소록에서 사용가능한 그룹 (카테고리)의 개수 를 가져온다 .

**반환 값**

주소록에서 사용가능한 그룹 (카테고리)의 개수

### getGroupName

```java
public String getGroupName(int groupId)
```

그룹(카테고리)의 이름을 얻는다.

**매개 변수**

- `groupId` - 그룹의 인덱스

**반환 값**

그룹이름

### createGroup

```java
public int createGroup(String groupName)
```

새 그룹(카테고리)을 생성한다.

**매개 변수**

- `groupName` - 그룹이름

**반환 값**

그룹인덱스

### getFieldCount

```java
public int getFieldCount()
```

하나의 레코드를 구성하는 필드의 개수를 얻어온다. 가져온 필드의 개수 를 통해 필 드 인덱스를 알 수있다 필드 인덱스는 ( 0 ~ (getFieldCount()-1))가 된다

**반환 값**

필드의 개수

### getFieldName

```java
public String getFieldName(int fieldIndex)
```

각 필드의 이름을 얻어온다.

**매개 변수**

- `fieldIndex` - 이름을 가져올 필드 인덱스 ( 0 ~ (getFieldCount()-1))

**반환 값**

필드이름

### getFieldType

```java
public int getFieldType(int fieldIndex)
```

각 필드의 데이터 타입을 얻어온다.

**매개 변수**

- `fieldIndex` - 필드 인덱스 ( 0 ~ (getFieldCount()-1))

**반환 값**

데이터 타입, TYPE_INT, TYPE_STRING, ...

### getFieldMaxLength

```java
public int getFieldMaxLength(int fieldIndex)
```

각 필드의 데이타 길이를 알아온다.

**매개 변수**

- `fieldIndex` - fieldIndex 필드 인덱스 ( 0 ~ (getFieldCount()-1))

**반환 값**

필드의 길이

### getAddressMaxCount

```java
public int getAddressMaxCount()
```

주소록에서 최대로 생성할수있는 record의 개수 를 얻어온다.

**반환 값**

주소록에서 최대로 생성할수있는 record의 개수

### getAddressCount

```java
public int getAddressCount()
```

주소록에서 사용중인 record의 개수 를 얻어온다.

**반환 값**

주소록에서 사용중인 record의 개수

### getAddressRecordIdsAll

```java
public int[] getAddressRecordIdsAll()
```

현재 사용중인 모든 레코드의 id들을 가져온다.

**반환 값**

현재 사용중인 모든 레코드의 id들

### getAddress

```java
public AddressBook.Address getAddress(int recordId)
```

어드레스 객체를 가져온다

**매개 변수**

- `recordId` - 레코드 아이디

**반환 값**

Address 객체

### createRecord

```java
public int createRecord(Object[] fields)
```

레코드를 생성한다

**매개 변수**

- `fields` - 생성할 레코드의 필드 데이타들

**반환 값**

생성된 레코드의 아아디

### createRecords

```java
public int[] createRecords(Object[] records)
```

복수개의 레코드를 생성한다

**매개 변수**

- `records` - 레코드 데이타들의 배열, 각 레코드 데이타는 필드데이타의 배열임

**반환 값**

생성된 레코드의 아이디의 배열

### isSupportFieldShortCut

```java
public boolean isSupportFieldShortCut()
```

단축키가 레코드마다 할당이 되는지 필드마다 할당이 되는지 구분한다.

**반환 값**

true 필드별 단축키가 지원됨 false 필드별 단축키가 지원되지 않음

### isSupportShortCut

```java
public boolean isSupportShortCut(int fieldIndex)
```

필드별 단축키가 지원될경우 만 지원되는 API이며 단축키가 지원되는 필드인지를 검 사한다.

**매개 변수**

- `fieldIndex` - 필드 인덱스

**반환 값**

true 단축키가 지원되는 필드임 false 단축키가 지원되지 않는 필드임

### getMaxShortCut

```java
public int getMaxShortCut()
```

최대로 설정할 수 있는 단축키의 개수를 가져온다

**반환 값**

최대로 설정할 수 있는 단축키의 개수

### getFirstFreeShortCut

```java
public int getFirstFreeShortCut(int startShortCut)
```

필드별 단축키가 지원될경우 만 지원되는 API이며 startShortCut 보다 크거나 같은 사용 가능한 단축키중 가장 작은 값을 얻어온다.

**매개 변수**

- `startShortCut` - 검색을 시작할 단축키 번호

**반환 값**

startShortCut보다 크거나 같은 사용 가능한 단축키중 가장 작은 값.

### setShortCut

```java
public boolean setShortCut(int shortCut, int recordId, int fieldId)
```

필드별 단축키가 지원될경우 만 지원되는 API이며 특정 레코드 특정 필드에 단축키 를 지정한다. 이미 레코드와 필드가 할당되어있는 단축키에는 새 레코드와 필드를 할당 할 수 없다 그렇게 하기위해서는 해당 단축키에 recordId = -1 을 할당 하여 단축키를 free 한 후 다시 sheShortCu()을 할당 해야 한다.

**매개 변수**

- `shortCut` - 설정하려고 하는 단축키 번호
- `recordId` - 단축 키 설정 대상 레코드의 ID
- `fieldId` - 단축 키 설정 대상 필드의 ID

**반환 값**

True
성공

False
실패

### setShortCut

```java
public boolean setShortCut(int[] shortCut int[] recordId, int[] fieldId)
```

필드별 단축키가 지원될경우 만 지원되는 API이며 특정 레코드 특정 필드에 단축키 를 지정한다.

**매개 변수**

- `shortCut` - 단축키 목록을 담은 int 배열
- `recordId` - 레코드 아이디 목록을 담은 int 배열
- `fieldId` - 필드 인덱스 목록을 담은 int 배열

**반환 값**

True
성공

False
실패

### getAllShortCut

```java
public int[] getAllShortCut()
```

필드별 단축키가 지원될경우 만 지원되는 API이며 할당되어있는 모든 단축키 목록을 가져온다.

**반환 값**

할당되어있는 모든 단축키 목록

### getShortCutItem

```java
public int[] getShortCutItem(int shortCut)
```

단축키에 할당되어 있는 레코드 아이디와 필드아이디를 알아낸다.

**매개 변수**

- `shortCut` - 조회하려고 하는 레코드와 필드에 할당된 단축 키

**반환 값**

int[0] = record Id int[1]=field Index

### getShortCutAssigned

```java
public int getShortCutAssigned(int recordId, int fieldIndex)
```

특정 레코드의 특정 필드에 short cut이 할당되어 있는지를 검사

**매개 변수**

- `recordId` - 레코드 아이디
- `fieldIndex` - 필드인덱스

**반환 값**

단축키(Short Cut) 번호, 단축키가 할당되어있지 않을 경우 -1

### searchAddress

```java
public int[] searchAddress(int searchBy, Object field, boolean exactMatch)
```

주어진 조건에 맞는 레코드를 검색한다.

**매개 변수**

- `searchBy` - 이름(SEARCH_NAME), 전화번호(SEARCH_PHONE_NO), 이메일 (SEARCH_EMAIL), 그룹(SEARCH_GROUP)
- `field` - 찾고자하는 데이타. 현재 그룹서치의 경우 Integer 타입이고 그이외에는 String 타입이다
- `exactMatch` - true field의 데이타와 정확히 일치하는 필드를 가진 레코 드를 찾는다
- `flase` - field의 데이터가 포함된 필드를 가진 레코드를 찾는 다

**반환 값**

찬아낸 레코드의 아이디

### removeAddress

```java
public boolean removeAddress(int recordId)
```

특정한 주소 레코드를 삭제한다.

**매개 변수**

- `recordId` - 삭제하려고 하는 주소 객체의 ID

**반환 값**

true
성공

false
실패

### checkPassword

```java
public int checkPassword(int index,java.lang.String password)
```

특정 인덱스(dwIndex)에 해당하는 리소스가 Lock 되어 있다면, 그 Lock을 해제하기 위해 필요한 비밀번호가 주어진 password와 맞는지 체크한다.

**매개 변수**

- `index` - 리소스 인덱스
- `password` - Password

**반환 값**

성공하면 0, 아니면 에러코드 (음수 값)

### getLockStatus

```java
public int getLockStatus()
```

주소록 객체의 Lock 상태를 반환한다. Lock status에는 LOCKED, UNLOCKED, 가 있다.

**반환 값**

Lock status를 리턴한다.

### setLockStatus

```java
public int setLockStatus(int status)
```

주소록 객체의 Lock을 설정/해제한다.

**매개 변수**

- `status` - Lock status (LOCKED, UNLOCKED)

**반환 값**

성공하면 0, 아니면 에러코드 (음수)
