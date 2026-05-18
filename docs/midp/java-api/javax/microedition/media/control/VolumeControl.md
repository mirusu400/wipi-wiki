# Interface VolumeControl

`package javax.microedition.media.control`

```text
public void setMute(boolean mute)
```

## 설명

**Parameters:**
- `mute` - 신호를 뮤트하려면 `true`를 지정하고 
신호의 뮤트를 해제하려면 `false`를 지정합니다.

**See Also:**
- ``isMuted()``

### isMuted

**Returns:**
- 뮤트 상태

**See Also:**
- ``setMute(boolean)``

### setLevel

**Parameters:**
- `level` - 수준 스케일에 지정된 새 볼륨

**Returns:**
- 실제로 설정된 수준

**See Also:**
- ``getLevel()``

### getLevel

**Returns:**
- 현재 볼륨 수준 또는 `-1`

**See Also:**
- ``setLevel(int)``

## 메서드 요약

- `int getLevel ()` — 현재 볼륨 수준 설정을 가져옵니다.
- `boolean isMuted ()` — 이 VolumeControl 과 연관된 신호의 뮤트 상태를 가져옵니다.
- `int setLevel (int level)` — 값이 0부터 100 사이인 선형 스케일을 사용하여 볼륨을 설정합니다.
- `void setMute (boolean mute)` — 이 VolumeControl 에 연결된 Player 의 뮤트를 설정하거나 해제합니다.

## 메서드 상세

### setMute

```java
public void setMute(boolean mute)
```

**Parameters:**
- `mute` - 신호를 뮤트하려면 `true`를 지정하고 
신호의 뮤트를 해제하려면 `false`를 지정합니다.

**See Also:**
- ``isMuted()``

### isMuted

```java
public boolean isMuted()
```

**Returns:**
- 뮤트 상태

**See Also:**
- ``setMute(boolean)``

### setLevel

```java
public int setLevel(int level)
```

**Parameters:**
- `level` - 수준 스케일에 지정된 새 볼륨

**Returns:**
- 실제로 설정된 수준

**See Also:**
- ``getLevel()``

### getLevel

```java
public int getLevel()
```

**Returns:**
- 현재 볼륨 수준 또는 `-1`

**See Also:**
- ``setLevel(int)``
