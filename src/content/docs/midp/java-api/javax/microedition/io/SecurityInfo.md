---
title: "Interface SecurityInfo"
---

`package javax.microedition.io`

```text
public Certificate getServerCertificate()
```

## 설명

**Returns:**
- 서버와의 보안 연결을 설정하는 데 사용되는 
`Certificate`

### getProtocolVersion

**Returns:**
- 프로토콜의 버전이 포함된 String. 반환 값은 
 `null`이 될 수 없습니다.

### getProtocolName

**Returns:**
- 보안 프로토콜 식별자가 포함된 `String`. 
TLS(RFC 2246) 또는 WAP TLS 프로필 및 터널링(WAP-219-TLS)이 
연결에 사용되면 "TLS", SSL V3(The SSL Protocol Version 3.0)이 
연결에 사용되면 "SSL", 
WTLS(WAP 199)가 연결에 사용되면 
"WTLS"가 반환됩니다.

### getCipherSuite

**Returns:**
- 사용 중인 암호 제품군 이름이 포함된 
`String`

## 메서드 요약

- `String getCipherSuite ()` — 연결에 사용 중인 암호 제품군의 이름을 반환합니다.
- `String getProtocolName ()` — 보안 프로토콜 이름을 반환합니다.
- `String getProtocolVersion ()` — 프로토콜 버전을 반환합니다.
- `Certificate getServerCertificate ()` — 서버와의 보안 연결을 설정하는 데 사용되는 Certificate 를 반환합니다.

## 메서드 상세

### getServerCertificate

```java
public Certificate getServerCertificate()
```

**Returns:**
- 서버와의 보안 연결을 설정하는 데 사용되는 
`Certificate`

### getProtocolVersion

```java
public String getProtocolVersion()
```

**Returns:**
- 프로토콜의 버전이 포함된 String. 반환 값은 
 `null`이 될 수 없습니다.

### getProtocolName

```java
public String getProtocolName()
```

**Returns:**
- 보안 프로토콜 식별자가 포함된 `String`. 
TLS(RFC 2246) 또는 WAP TLS 프로필 및 터널링(WAP-219-TLS)이 
연결에 사용되면 "TLS", SSL V3(The SSL Protocol Version 3.0)이 
연결에 사용되면 "SSL", 
WTLS(WAP 199)가 연결에 사용되면 
"WTLS"가 반환됩니다.

### getCipherSuite

```java
public String getCipherSuite()
```

**Returns:**
- 사용 중인 암호 제품군 이름이 포함된 
`String`
