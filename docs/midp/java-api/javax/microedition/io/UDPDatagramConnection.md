# Interface UDPDatagramConnection

`package javax.microedition.io`

```
public String getLocalAddress()
                       throws IOException
```

## 설명

**Returns:**
- 데이터그램 연결이 바운드되는 로컬 주소

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``ServerSocketConnection``

### getLocalPort

**Returns:**
- 데이터그램 연결이 
 연결되는 로컬 포트 번호

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``ServerSocketConnection``

## 메서드 요약

- `String getLocalAddress ()` — 데이터그램 연결이 바운드되는 로컬 주소를 가져옵니다.
- `int getLocalPort ()` — 데이터그램 연결이 바운드되는 로컬 포트를 반환합니다.

## 메서드 상세

### getLocalAddress

```java
public String getLocalAddress()
                       throws IOException
```

**Returns:**
- 데이터그램 연결이 바운드되는 로컬 주소

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``ServerSocketConnection``

### getLocalPort

```java
public int getLocalPort()
                 throws IOException
```

**Returns:**
- 데이터그램 연결이 
 연결되는 로컬 포트 번호

**Throws:**
- `IOException` - 연결이 닫힌 경우

**See Also:**
- ``ServerSocketConnection``
