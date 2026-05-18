# Interface ContentConnection

`package javax.microedition.io`

```text
public String getType()
```

## 설명

**Returns:**
- URL이 참조하는 자원의 내용 유형 또는 
 유형을 알 수 없는 경우 `null`

### getEncoding

**Returns:**
- URL이 참조하는 자원의 내용 인코딩 또는 
 인코딩을 알 수 없는 경우 `null`

### getLength

**Returns:**
- 이 연결의 URL이 참조하는 자원의 내용 
 길이 또는 내용 길이를 알 수 없는 경우 
 `-1`

## 메서드 요약

- `String getEncoding ()` — 연결된 자원이 제공하는 내용의 인코딩을 설명하는 문자열을 반환합니다.
- `long getLength ()` — 제공되는 내용의 길이를 반환합니다.
- `String getType ()` — 연결된 자원이 제공하는 내용 유형을 반환합니다.

## 메서드 상세

### getType

```java
public String getType()
```

**Returns:**
- URL이 참조하는 자원의 내용 유형 또는 
 유형을 알 수 없는 경우 `null`

### getEncoding

```java
public String getEncoding()
```

**Returns:**
- URL이 참조하는 자원의 내용 인코딩 또는 
 인코딩을 알 수 없는 경우 `null`

### getLength

```java
public long getLength()
```

**Returns:**
- 이 연결의 URL이 참조하는 자원의 내용 
 길이 또는 내용 길이를 알 수 없는 경우 
 `-1`
