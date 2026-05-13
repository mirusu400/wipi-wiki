# Interface Player

`package javax.microedition.media`

```
 try {
     Player p = Manager.createPlayer(Manager.TONE_DEVICE_LOCATOR);
     p.start();
 } catch (MediaException me) {}
 } catch (IOException ioe) {
 }
```

## 필드 요약

- `static int CLOSED` — Player 가 종료되었음을 나타내는 Player 의 상태.
- `static int PREFETCHED` — 재생하는 데 필요한 모든 자원을 획득했음을 나타내는 Player 의 상태.
- `static int REALIZED` — 작동하는 데 필요한 정보를 획득했지만 자원은 획득하지 않았음을 나타내는 Player 의 상태.
- `static int STARTED` — Player 가 이미 시작되었음을 나타내는 Player 의 상태.
- `static long TIME_UNKNOWN` — 요청된 시간을 알 수 없음을 나타내는 반환 값.
- `static int UNREALIZED` — 작동하는 데 필요한 정보와 자원을 획득하지 않았음을 나타내는 Player 의 상태.

## 메서드 요약

- `void addPlayerListener ( PlayerListener playerListener)` — 이 플레이어에 플레이어 수신기를 추가합니다.
- `void close ()` — Player 를 종료하고 자원을 해제합니다.
- `void deallocate ()` — Player 에서 획득한 오디오 장치와 같은 희귀 자원이나 독점 자원을 해제합니다.
- `String getContentType ()` — 이 Player 로 재생 중인 미디어의 내용 유형을 가져옵니다.
- `long getDuration ()` — 미디어의 재생 시간을 가져옵니다.
- `long getMediaTime ()` — 이 Player 의 현재 미디어 시간 을 가져옵니다.
- `int getState ()` — 이 Player 의 현재 상태를 가져옵니다.
- `void prefetch ()` — 희귀 자원이나 독점 자원을 획득하고 시작 대기 시간을 줄이는 데 필요한 만큼의 데이터를 처리합니다.
- `void realize ()` — 희귀 자원이나 독점 자원을 획득하지 않고 Player 의 일부를 구성합니다.
- `void removePlayerListener ( PlayerListener playerListener)` — 이 플레이어의 플레이어 수신기를 제거합니다.
- `void setLoopCount (int count)` — Player 가 내용을 루프 및 재생할 횟수를 설정합니다.
- `long setMediaTime (long now)` — Player 의 미디어 시간 을 설정합니다.
- `void start ()` — 가능한 빨리 Player 를 시작합니다.
- `void stop ()` — Player 를 정지합니다.

## 필드 상세

### UNREALIZED

```java
public static final int UNREALIZED
```

**See Also:**
- `Constant Field Values`

### REALIZED

```java
public static final int REALIZED
```

**See Also:**
- `Constant Field Values`

### PREFETCHED

```java
public static final int PREFETCHED
```

**See Also:**
- `Constant Field Values`

### STARTED

```java
public static final int STARTED
```

**See Also:**
- `Constant Field Values`

### CLOSED

```java
public static final int CLOSED
```

**See Also:**
- `Constant Field Values`

### TIME_UNKNOWN

```java
public static final long TIME_UNKNOWN
```

**See Also:**
- `Constant Field Values`

### realize

```java
public void realize()
             throws MediaException
```

**Throws:**
- `SecurityException` - 호출자에게 `Player`를 
인식하기 위한 보안 권한이 없는 경우 발생합니다.

### prefetch

```java
public void prefetch()
              throws MediaException
```

**Throws:**
- `SecurityException` - 호출자에게 `Player`를 
프리패치할 보안 권한이 없는 경우 발생합니다.

### start

```java
public void start()
           throws MediaException
```

**Throws:**
- `SecurityException` - 호출자에게 `Player`를 
시작할 보안 권한이 없는 경우 발생합니다.

### stop

```java
public void stop()
          throws MediaException
```

**Throws:**
- `MediaException` - `Player`를 정지할 수 없는 경우 
발생합니다.

### deallocate

```java
public void deallocate()
```

**Throws:**
- `IllegalStateException` - `Player`가 
*CLOSED* 상태인 경우 발생합니다.

### close

```java
public void close()
```

Player 를 종료하고 자원을 해제합니다. 메소드가 반환되면 Player 는 CLOSED 상태가 되어 더 이상 사용할 수 없습니다. CLOSED 이벤트는 등록된 PlayerListener 에 
전달됩니다. 종료된 Player 에서 close 를 
호출하면 요청은 무시됩니다.

### setMediaTime

```java
public long setMediaTime(long now)
                  throws MediaException
```

**Parameters:**
- `now` - 밀리초 단위로 된 새 미디어 시간

**Returns:**
- 밀리초 단위로 설정된 실제 미디어 시간

**Throws:**
- `MediaException` - 미디어 시간을 설정할 수 없는 경우 
발생합니다.

**See Also:**
- ``getMediaTime()``

### getMediaTime

```java
public long getMediaTime()
```

**Returns:**
- 밀리초로 된 현재 *미디어 시간* 또는 
`TIME_UNKNOWN`

**Throws:**
- `IllegalStateException` - `Player`가 
*CLOSED* 상태인 경우 발생합니다.

**See Also:**
- ``setMediaTime(long)``

### getState

```java
public int getState()
```

**Returns:**
- `Player`의 현재 상태

### getDuration

```java
public long getDuration()
```

**Returns:**
- 밀리초 단위로 된 재생 시간이나 `TIME_UNKNOWN`

**Throws:**
- `IllegalStateException` - `Player`가 
*CLOSED* 상태인 경우 발생합니다.

### getContentType

```java
public String getContentType()
```

**Returns:**
- 이 `Player`가 재생 중인 
내용 유형

**Throws:**
- `IllegalStateException` - `Player`가 
*UNREALIZED* 또는 *CLOSED* 상태인 경우 발생합니다.

### setLoopCount

```java
public void setLoopCount(int count)
```

**Parameters:**
- `count` - 내용을 재생할 횟수를 나타냅니다. 
1이 기본값입니다. 0은 유효하지 않습니다. 
-1은 무기한으로 루프함을 나타냅니다.

**Throws:**
- `IllegalStateException` - `Player`가 
*STARTED* 또는 *CLOSED* 
상태인 경우 발생합니다.

### addPlayerListener

```java
public void addPlayerListener(PlayerListener playerListener)
```

**Parameters:**
- `playerListener` - 추가할 수신기. `null`이 
사용되면 요청은 무시됩니다.

**Throws:**
- `IllegalStateException` - `Player`가 
*CLOSED* 상태인 경우 발생합니다.

**See Also:**
- ``removePlayerListener(javax.microedition.media.PlayerListener)``

### removePlayerListener

```java
public void removePlayerListener(PlayerListener playerListener)
```

**Parameters:**
- `playerListener` - 제거할 수신기. `null`이 
사용되거나 주어진 `playerListener`가 
이 `Player`의 수신기가 아닌 
경우 요청은 무시됩니다.

**Throws:**
- `IllegalStateException` - `Player`가 
*CLOSED* 상태인 경우 발생합니다.

**See Also:**
- ``addPlayerListener(javax.microedition.media.PlayerListener)``

## 메서드 상세

### realize

```java
public void realize()
             throws MediaException
```

**Throws:**
- `SecurityException` - 호출자에게 `Player`를 
인식하기 위한 보안 권한이 없는 경우 발생합니다.

### prefetch

```java
public void prefetch()
              throws MediaException
```

**Throws:**
- `SecurityException` - 호출자에게 `Player`를 
프리패치할 보안 권한이 없는 경우 발생합니다.

### start

```java
public void start()
           throws MediaException
```

**Throws:**
- `SecurityException` - 호출자에게 `Player`를 
시작할 보안 권한이 없는 경우 발생합니다.

### stop

```java
public void stop()
          throws MediaException
```

**Throws:**
- `MediaException` - `Player`를 정지할 수 없는 경우 
발생합니다.

### deallocate

```java
public void deallocate()
```

**Throws:**
- `IllegalStateException` - `Player`가 
*CLOSED* 상태인 경우 발생합니다.

### close

```java
public void close()
```

Player 를 종료하고 자원을 해제합니다. 메소드가 반환되면 Player 는 CLOSED 상태가 되어 더 이상 사용할 수 없습니다. CLOSED 이벤트는 등록된 PlayerListener 에 
전달됩니다. 종료된 Player 에서 close 를 
호출하면 요청은 무시됩니다.

### setMediaTime

```java
public long setMediaTime(long now)
                  throws MediaException
```

**Parameters:**
- `now` - 밀리초 단위로 된 새 미디어 시간

**Returns:**
- 밀리초 단위로 설정된 실제 미디어 시간

**Throws:**
- `MediaException` - 미디어 시간을 설정할 수 없는 경우 
발생합니다.

**See Also:**
- ``getMediaTime()``

### getMediaTime

```java
public long getMediaTime()
```

**Returns:**
- 밀리초로 된 현재 *미디어 시간* 또는 
`TIME_UNKNOWN`

**Throws:**
- `IllegalStateException` - `Player`가 
*CLOSED* 상태인 경우 발생합니다.

**See Also:**
- ``setMediaTime(long)``

### getState

```java
public int getState()
```

**Returns:**
- `Player`의 현재 상태

### getDuration

```java
public long getDuration()
```

**Returns:**
- 밀리초 단위로 된 재생 시간이나 `TIME_UNKNOWN`

**Throws:**
- `IllegalStateException` - `Player`가 
*CLOSED* 상태인 경우 발생합니다.

### getContentType

```java
public String getContentType()
```

**Returns:**
- 이 `Player`가 재생 중인 
내용 유형

**Throws:**
- `IllegalStateException` - `Player`가 
*UNREALIZED* 또는 *CLOSED* 상태인 경우 발생합니다.

### setLoopCount

```java
public void setLoopCount(int count)
```

**Parameters:**
- `count` - 내용을 재생할 횟수를 나타냅니다. 
1이 기본값입니다. 0은 유효하지 않습니다. 
-1은 무기한으로 루프함을 나타냅니다.

**Throws:**
- `IllegalStateException` - `Player`가 
*STARTED* 또는 *CLOSED* 
상태인 경우 발생합니다.

### addPlayerListener

```java
public void addPlayerListener(PlayerListener playerListener)
```

**Parameters:**
- `playerListener` - 추가할 수신기. `null`이 
사용되면 요청은 무시됩니다.

**Throws:**
- `IllegalStateException` - `Player`가 
*CLOSED* 상태인 경우 발생합니다.

**See Also:**
- ``removePlayerListener(javax.microedition.media.PlayerListener)``

### removePlayerListener

```java
public void removePlayerListener(PlayerListener playerListener)
```

**Parameters:**
- `playerListener` - 제거할 수신기. `null`이 
사용되거나 주어진 `playerListener`가 
이 `Player`의 수신기가 아닌 
경우 요청은 무시됩니다.

**Throws:**
- `IllegalStateException` - `Player`가 
*CLOSED* 상태인 경우 발생합니다.

**See Also:**
- ``addPlayerListener(javax.microedition.media.PlayerListener)``
