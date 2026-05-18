# Interface RecordEnumeration

`package javax.microedition.rms`

```text
public int numRecords()
```

## 설명

**Returns:**
- 이 열거 세트에서 사용 가능한 레코드 수. 
즉, 필터 기준과 일치하는 레코드 수가 
반환됩니다.

### nextRecord

**Returns:**
- 이 열거의 다음 레코드

**Throws:**
- `RecordStoreException` - 일반 레코드 저장소 
예외가 발생한 경우

### nextRecordId

**Returns:**
- 이 열거에 있는 다음 레코드의 recordId

**Throws:**
- `InvalidRecordIDException` - 사용할 수 있는 
레코드가 없는 경우, `reset()`을 호출하여 
열거를 재설정할 때까지 메소드의 
후속 호출 시 
계속 이 예외가 발생합니다.

### previousRecord

**Returns:**
- 이 열거의 이전 레코드

**Throws:**
- `RecordStoreException` - 일반 레코드 저장소 
예외가 발생한 경우

### previousRecordId

**Returns:**
- 이 열거에 있는 이전 레코드의 recordId

**Throws:**
- `InvalidRecordIDException` - 사용할 수 있는 
레코드가 없는 경우, 
`reset()`을 호출하여 
열거를 재설정할 때까지 메소드의 후속 호출 시 
계속 이 예외가 발생합니다.

### hasNextElement

**Returns:**
- *다음* 방향에 요소가 
더 많으면 true

### hasPreviousElement

**Returns:**
- *이전* 방향에 요소가 
더 많으면 true

### reset

열거가 작성된 직후와 동일한 상태로 
열거 색인을 반환합니다.

### rebuild

**See Also:**
- ``keepUpdated(boolean)``

### keepUpdated

**Parameters:**
- `keepUpdated` - true인 경우 열거자는 
레코드 저장소의 레코드가 변경되면 
열거를 최신 상태로 유지합니다. 
성능 문제가 발생할 가능성이 있으므로 주의해서 사용합니다. 
`keepUpdated(true)`를 호출하면 
현재 레코드 세트를 반영하기 위해 열거가 갱신된다는 면에서 
`RecordEnumeration.rebuild`를 호출하는 것과 
동일한 효과를 갖습니다. 
false인 경우 열거는 최신 상태로 유지되지 않으며 
삭제된 레코드의 레코드 ID를 반환하거나 
나중에 추가된 레코드를 누락시킬 수 있습니다. 
열거가 만들어진 후 수정된 순서와 
상관 없이 레코드를 반환할 수도 있습니다. 
레코드 저장소의 레코드에 대한 변경 내용은 
나중에 레코드를 직접 검색하거나 
열거를 통해 검색할 때 정확하게 반영됩니다. 
이 매개 변수를 false로 설정할 때 
주의해야 할 점은 레코드가 수정, 
추가 또는 삭제될 때 열거의 필터링 및 정렬 순서입니다.

**See Also:**
- ``rebuild()``

### isKeptUpdated

**Returns:**
- 레코드의 변경과 함께 열거를 
최신 상태로 유지하는 경우 true

### destroy

이 RecordEnumeration에서 사용하는 내부 자원을 해제합니다. 
MIDlet이 RecordEnumeration을 사용하여 수행한 경우 
이 메소드를 호출해야 합니다. 
MIDlet이 RecordEnumeration이 호출된 다음에 
이 메소드를 사용하려고 하면 IllegalStateException 이 
발생합니다. 더 이상 이 열거가 필요하지 않은 경우 
즉각적인 자원 요구 사항을 최소화하기 위해 
이 메소드가 수동으로 사용됩니다.

## 메서드 요약

- `void destroy ()` — 이 RecordEnumeration에서 사용하는 내부 자원을 해제합니다.
- `boolean hasNextElement ()` — 다음 방향에 요소가 더 많으면 true를 반환합니다.
- `boolean hasPreviousElement ()` — 이전 방향에 요소가 더 많으면 true를 반환합니다.
- `boolean isKeptUpdated ()` — 레코드의 변경과 함께 열거를 최신 상태로 유지하는 경우 true를 반환합니다.
- `void keepUpdated (boolean keepUpdated)` — 레코드 저장소의 레코드가 추가/삭제/변경됨에 따라 열거의 내부 색인을 최신 상태로 유지할 수 있는지 여부를 설정할 때 사용됩니다.
- `byte[] nextRecord ()` — 열거의 다음 레코드 사본을 반환합니다.
- `int nextRecordId ()` — 이 열거에 있는 다음 레코드의 recordId를 반환합니다.
- `int numRecords ()` — 이 열거 세트에서 사용 가능한 레코드 수를 반환합니다.
- `byte[] previousRecord ()` — 이 열거의 이전 레코드 사본을 반환합니다.
- `int previousRecordId ()` — 이 열거에 있는 이전 레코드의 recordId를 반환합니다.
- `void rebuild ()` — 현재 레코드 세트를 반영하기 위해 열거를 갱신하도록 요청합니다.
- `void reset ()` — 열거가 작성된 직후와 동일한 상태로 열거 색인을 반환합니다.

## 메서드 상세

### numRecords

```java
public int numRecords()
```

**Returns:**
- 이 열거 세트에서 사용 가능한 레코드 수. 
즉, 필터 기준과 일치하는 레코드 수가 
반환됩니다.

### nextRecord

```java
public byte[] nextRecord()
                  throws InvalidRecordIDException,
                         RecordStoreNotOpenException,
                         RecordStoreException
```

**Returns:**
- 이 열거의 다음 레코드

**Throws:**
- `RecordStoreException` - 일반 레코드 저장소 
예외가 발생한 경우

### nextRecordId

```java
public int nextRecordId()
                 throws InvalidRecordIDException
```

**Returns:**
- 이 열거에 있는 다음 레코드의 recordId

**Throws:**
- `InvalidRecordIDException` - 사용할 수 있는 
레코드가 없는 경우, `reset()`을 호출하여 
열거를 재설정할 때까지 메소드의 
후속 호출 시 
계속 이 예외가 발생합니다.

### previousRecord

```java
public byte[] previousRecord()
                      throws InvalidRecordIDException,
                             RecordStoreNotOpenException,
                             RecordStoreException
```

**Returns:**
- 이 열거의 이전 레코드

**Throws:**
- `RecordStoreException` - 일반 레코드 저장소 
예외가 발생한 경우

### previousRecordId

```java
public int previousRecordId()
                     throws InvalidRecordIDException
```

**Returns:**
- 이 열거에 있는 이전 레코드의 recordId

**Throws:**
- `InvalidRecordIDException` - 사용할 수 있는 
레코드가 없는 경우, 
`reset()`을 호출하여 
열거를 재설정할 때까지 메소드의 후속 호출 시 
계속 이 예외가 발생합니다.

### hasNextElement

```java
public boolean hasNextElement()
```

**Returns:**
- *다음* 방향에 요소가 
더 많으면 true

### hasPreviousElement

```java
public boolean hasPreviousElement()
```

**Returns:**
- *이전* 방향에 요소가 
더 많으면 true

### reset

```java
public void reset()
```

열거가 작성된 직후와 동일한 상태로 
열거 색인을 반환합니다.

### rebuild

```java
public void rebuild()
```

**See Also:**
- ``keepUpdated(boolean)``

### keepUpdated

```java
public void keepUpdated(boolean keepUpdated)
```

**Parameters:**
- `keepUpdated` - true인 경우 열거자는 
레코드 저장소의 레코드가 변경되면 
열거를 최신 상태로 유지합니다. 
성능 문제가 발생할 가능성이 있으므로 주의해서 사용합니다. 
`keepUpdated(true)`를 호출하면 
현재 레코드 세트를 반영하기 위해 열거가 갱신된다는 면에서 
`RecordEnumeration.rebuild`를 호출하는 것과 
동일한 효과를 갖습니다. 
false인 경우 열거는 최신 상태로 유지되지 않으며 
삭제된 레코드의 레코드 ID를 반환하거나 
나중에 추가된 레코드를 누락시킬 수 있습니다. 
열거가 만들어진 후 수정된 순서와 
상관 없이 레코드를 반환할 수도 있습니다. 
레코드 저장소의 레코드에 대한 변경 내용은 
나중에 레코드를 직접 검색하거나 
열거를 통해 검색할 때 정확하게 반영됩니다. 
이 매개 변수를 false로 설정할 때 
주의해야 할 점은 레코드가 수정, 
추가 또는 삭제될 때 열거의 필터링 및 정렬 순서입니다.

**See Also:**
- ``rebuild()``

### isKeptUpdated

```java
public boolean isKeptUpdated()
```

**Returns:**
- 레코드의 변경과 함께 열거를 
최신 상태로 유지하는 경우 true

### destroy

```java
public void destroy()
```

이 RecordEnumeration에서 사용하는 내부 자원을 해제합니다. 
MIDlet이 RecordEnumeration을 사용하여 수행한 경우 
이 메소드를 호출해야 합니다. 
MIDlet이 RecordEnumeration이 호출된 다음에 
이 메소드를 사용하려고 하면 IllegalStateException 이 
발생합니다. 더 이상 이 열거가 필요하지 않은 경우 
즉각적인 자원 요구 사항을 최소화하기 위해 
이 메소드가 수동으로 사용됩니다.
