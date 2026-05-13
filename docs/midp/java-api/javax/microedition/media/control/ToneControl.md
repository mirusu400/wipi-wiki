# Interface ToneControl

`package javax.microedition.media.control`

```
 sequence              = version *1tempo_definition *1resolution_definition 
		             *block_definition 1*sequence_event
 
version               = VERSION version_number
 VERSION               = byte-value
 version_number        = 1	; version # 1
 tempo_definition      = TEMPO tempo_modifier
 TEMPO                 = byte-value
 tempo_modifier        = byte-value 
              ; multiply by 4 to get the tempo (in bpm) used 
              ; in the sequence.
 
 resolution_definition = RESOLUTION resolution_unit
 RESOLUTION            = byte-value
 resolution_unit       = byte-value
 block_definition      = BLOCK_START block_number 
                            1*sequence_event 
                         BLOCK_END block_number
 BLOCK_START           = byte-value
 BLOCK_END             = byte-value
 block_number          = byte-value 
              ; block_number specified in BLOCK_END has to be the 
              ; same as the one in BLOCK_START 
 sequence_event        = tone_event / block_event / 
                           volume_event / repeat_event
 
 tone_event            = note duration
 note                  = byte-value ; note to be played
 duration              = byte-value ; duration of the note
 block_event           = PLAY_BLOCK block_number
 PLAY_BLOCK            = byte-value
 block_number          = byte-value 
              ; block_number must be previously defined 
              ; by a full block_definition
 volume_event          = SET_VOLUME volume
 SET_VOLUME            = byte-value
 volume                = byte-value ; new volume
 repeat_event          = REPEAT multiplier tone_event
 REPEAT                = byte-value
 multiplier            = byte-value  
              ; number of times to repeat a tone
 byte-value            = -128 - 127
              ; the value of each constant and additional
              ; constraints on each parameter are specified below.
```

## 필드 요약

- `static byte BLOCK_END` — 블록의 끝점을 정의합니다.
- `static byte BLOCK_START` — 블록의 시작점을 정의합니다.
- `static byte C4` — 중앙 C 60 값이 C4 에 지정됩니다.
- `static byte PLAY_BLOCK` — 정의된 블록을 재생합니다.
- `static byte REPEAT` — REPEAT 이벤트 태그 -9 값이 REPEAT 에 지정됩니다.
- `static byte RESOLUTION` — RESOLUTION 이벤트 태그.
- `static byte SET_VOLUME` — SET_VOLUME 이벤트 태그.
- `static byte SILENCE` — 무음 -1 값이 SILENCE 에 지정됩니다.
- `static byte TEMPO` — TEMPO 이벤트 태그.
- `static byte VERSION` — VERSION 속성 태그 -2 값이 VERSION 에 지정됩니다.

## 메서드 요약

- `void setSequence (byte[] sequence)` — 톤 시퀀스를 설정합니다.

## 필드 상세

### VERSION

```java
public static final byte VERSION
```

**See Also:**
- `Constant Field Values`

### TEMPO

```java
public static final byte TEMPO
```

**See Also:**
- `Constant Field Values`

### RESOLUTION

```java
public static final byte RESOLUTION
```

**See Also:**
- `Constant Field Values`

### BLOCK_START

```java
public static final byte BLOCK_START
```

**See Also:**
- `Constant Field Values`

### BLOCK_END

```java
public static final byte BLOCK_END
```

**See Also:**
- `Constant Field Values`

### PLAY_BLOCK

```java
public static final byte PLAY_BLOCK
```

**See Also:**
- `Constant Field Values`

### SET_VOLUME

```java
public static final byte SET_VOLUME
```

**See Also:**
- `Constant Field Values`

### REPEAT

```java
public static final byte REPEAT
```

**See Also:**
- `Constant Field Values`

### C4

```java
public static final byte C4
```

**See Also:**
- `Constant Field Values`

### SILENCE

```java
public static final byte SILENCE
```

**See Also:**
- `Constant Field Values`

### setSequence

```java
public void setSequence(byte[] sequence)
```

**Parameters:**
- `sequence` - 설정할 시퀀스

**Throws:**
- `IllegalStateException` - 이 컨트롤이 속해 있는 
`Player`가 *PREFETCHED* 또는 
*STARTED* 상태에 있는 경우 발생합니다.

## 메서드 상세

### setSequence

```java
public void setSequence(byte[] sequence)
```

**Parameters:**
- `sequence` - 설정할 시퀀스

**Throws:**
- `IllegalStateException` - 이 컨트롤이 속해 있는 
`Player`가 *PREFETCHED* 또는 
*STARTED* 상태에 있는 경우 발생합니다.
