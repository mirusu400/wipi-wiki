---
title: "Interface Certificate"
---

`package javax.microedition.pki`

```text
public String getSubject()
```

## 설명

**Returns:**
- 이 `Certificate`의 제목. 
이 값은 `null`일 수 없습니다.

### getIssuer

**Returns:**
- 이 `Certificate`의 발행인. 
이 값은 `null`일 수 없습니다.

### getType

**Returns:**
- `Certificate`의 유형. 
이 값은 `null`일 수 없습니다.

### getVersion

**Returns:**
- `Certificate`의 버전 번호. 
이 값은 `null`일 수 없습니다.

### getSigAlgName

**Returns:**
- 서명 알고리즘 이름. 
이 값은 `null`일 수 없습니다.

### getNotBefore

**Returns:**
- `Certificate`를 사용할 수 있는 
밀리초 단위의 시작 시간. 
반드시 양수여야 합니다. 
인증서의 유효성에 시간적인 제한이 없을 경우 `0`이 반환됩니다.

### getNotAfter

**Returns:**
- `Certificate`를 사용할 수 있는 
밀리초 단위의 끝 시간(만료 날짜). 
반드시 양수여야 합니다. 
인증서의 유효성에 시간적인 제한이 없을 경우 
`Long.MAX_VALUE`가 반환됩니다.

### getSerialNumber

**Returns:**
- 사용자에게 친숙한 형식의 
일련 번호를 포함하는 문자열. 
일련 번호가 없는 경우 `null`이 반환됩니다.

## 메서드 요약

- `String getIssuer ()` — 이 인증서 발행인의 이름을 가져옵니다.
- `long getNotAfter ()` — 유효 기간 중 Certificate 를 사용할 수 있는 끝 시간을 가져옵니다.
- `long getNotBefore ()` — 유효 기간 중 Certificate 를 사용할 수 있는 시작 시간을 가져옵니다.
- `String getSerialNumber ()` — 이 Certificate 의 인쇄 가능한 일련 번호 형식을 가져옵니다.
- `String getSigAlgName ()` — Certificate 서명에 사용된 알고리즘 이름을 가져옵니다.
- `String getSubject ()` — 이 인증서 제목의 이름을 가져옵니다.
- `String getType ()` — Certificate 의 유형을 가져옵니다.
- `String getVersion ()` — 이 Certificate 의 버전 번호를 가져옵니다.

## 메서드 상세

### getSubject

```java
public String getSubject()
```

**Returns:**
- 이 `Certificate`의 제목. 
이 값은 `null`일 수 없습니다.

### getIssuer

```java
public String getIssuer()
```

**Returns:**
- 이 `Certificate`의 발행인. 
이 값은 `null`일 수 없습니다.

### getType

```java
public String getType()
```

**Returns:**
- `Certificate`의 유형. 
이 값은 `null`일 수 없습니다.

### getVersion

```java
public String getVersion()
```

**Returns:**
- `Certificate`의 버전 번호. 
이 값은 `null`일 수 없습니다.

### getSigAlgName

```java
public String getSigAlgName()
```

**Returns:**
- 서명 알고리즘 이름. 
이 값은 `null`일 수 없습니다.

### getNotBefore

```java
public long getNotBefore()
```

**Returns:**
- `Certificate`를 사용할 수 있는 
밀리초 단위의 시작 시간. 
반드시 양수여야 합니다. 
인증서의 유효성에 시간적인 제한이 없을 경우 `0`이 반환됩니다.

### getNotAfter

```java
public long getNotAfter()
```

**Returns:**
- `Certificate`를 사용할 수 있는 
밀리초 단위의 끝 시간(만료 날짜). 
반드시 양수여야 합니다. 
인증서의 유효성에 시간적인 제한이 없을 경우 
`Long.MAX_VALUE`가 반환됩니다.

### getSerialNumber

```java
public String getSerialNumber()
```

**Returns:**
- 사용자에게 친숙한 형식의 
일련 번호를 포함하는 문자열. 
일련 번호가 없는 경우 `null`이 반환됩니다.
