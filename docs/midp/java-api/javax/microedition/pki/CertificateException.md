# Class CertificateException

`package javax.microedition.pki`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.io.IOException
                    |
                    +--javax.microedition.pki.CertificateException
```

## 설명

**extends IOException:**

`CertificateException`은 
`Certificate`가 사용되는 중 발생한 오류를 캡슐화합니다. 
`Certificate`에서 여러 개의 오류가 발견되면 더 심각한 오류가 
예외로 보고됩니다.

**Since:**
- MIDP 2.0

## 필드 요약

- `static byte BAD_EXTENSIONS` — 인증서에 알 수 없는 중요 확장이 있음을 표시합니다.
- `static byte BROKEN_CHAIN` — 체인 내의 인증서를 체인의 다음 기관이 발행하지 않았음을 표시합니다.
- `static byte CERTIFICATE_CHAIN_TOO_LONG` — 서버 인증서 체인이 발행자 정책에서 허용하는 길이를 초과했음을 표시합니다.
- `static byte EXPIRED` — 인증서가 만료되었음을 표시합니다.
- `static byte INAPPROPRIATE_KEY_USAGE` — 발행자가 인증서 공용 키에 부적절하다고 판단되는 방법을 사용했음을 표시합니다.
- `static byte MISSING_SIGNATURE` — 인증서 객체에 서명이 없음을 표시합니다.
- `static byte NOT_YET_VALID` — 인증서가 아직 유효하지 않음을 표시합니다.
- `static byte ROOT_CA_EXPIRED` — 루트 CA의 공용 키가 만료되었음을 표시합니다.
- `static byte SITENAME_MISMATCH` — 인증서에 올바른 사이트 이름이 없음을 표시합니다.
- `static byte UNAUTHORIZED_INTERMEDIATE_CA` — 체인의 중간 인증서에 중간 CA가 될 권한이 없음을 표시합니다.
- `static byte UNRECOGNIZED_ISSUER` — 인증서가 알 수 없는 엔티티에 의해 발행되었음을 표시합니다.
- `static byte UNSUPPORTED_PUBLIC_KEY_TYPE` — 인증서의 공용 키 유형이 장치에서 지원되지 않음을 표시합니다.
- `static byte UNSUPPORTED_SIGALG` — 인증서가 지원되지 않는 알고리즘을 사용하여 서명되었음을 표시합니다.
- `static byte VERIFICATION_FAILED` — 인증서 확인에 실패했음을 표시합니다.

## 생성자 요약

- CertificateException ( Certificate certificate,
 byte status) Certificate 및 구체적인 오류 이유를 사용하여 
새 예외를 작성합니다.
- CertificateException ( String message, Certificate certificate,
 byte status) 메시지, Certificate 및 구체적인 오류 이유를 사용하여 
새 예외를 작성합니다.

## 메서드 요약

- `Certificate getCertificate ()` — 예외가 발생한 Certificate 를 가져옵니다.
- `byte getReason ()` — 이유 코드를 가져옵니다.

## 필드 상세

### BAD_EXTENSIONS

```java
public static final byte BAD_EXTENSIONS
```

**See Also:**
- `Constant Field Values`

### CERTIFICATE_CHAIN_TOO_LONG

```java
public static final byte CERTIFICATE_CHAIN_TOO_LONG
```

**See Also:**
- `Constant Field Values`

### EXPIRED

```java
public static final byte EXPIRED
```

**See Also:**
- `Constant Field Values`

### UNAUTHORIZED_INTERMEDIATE_CA

```java
public static final byte UNAUTHORIZED_INTERMEDIATE_CA
```

**See Also:**
- `Constant Field Values`

### MISSING_SIGNATURE

```java
public static final byte MISSING_SIGNATURE
```

**See Also:**
- `Constant Field Values`

### NOT_YET_VALID

```java
public static final byte NOT_YET_VALID
```

**See Also:**
- `Constant Field Values`

### SITENAME_MISMATCH

```java
public static final byte SITENAME_MISMATCH
```

**See Also:**
- `Constant Field Values`

### UNRECOGNIZED_ISSUER

```java
public static final byte UNRECOGNIZED_ISSUER
```

**See Also:**
- `Constant Field Values`

### UNSUPPORTED_SIGALG

```java
public static final byte UNSUPPORTED_SIGALG
```

**See Also:**
- `Constant Field Values`

### INAPPROPRIATE_KEY_USAGE

```java
public static final byte INAPPROPRIATE_KEY_USAGE
```

**See Also:**
- `Constant Field Values`

### BROKEN_CHAIN

```java
public static final byte BROKEN_CHAIN
```

**See Also:**
- `Constant Field Values`

### ROOT_CA_EXPIRED

```java
public static final byte ROOT_CA_EXPIRED
```

**See Also:**
- `Constant Field Values`

### UNSUPPORTED_PUBLIC_KEY_TYPE

```java
public static final byte UNSUPPORTED_PUBLIC_KEY_TYPE
```

**See Also:**
- `Constant Field Values`

### VERIFICATION_FAILED

```java
public static final byte VERIFICATION_FAILED
```

**See Also:**
- `Constant Field Values`

### CertificateException

```java
public CertificateException(Certificate certificate,
                            byte status)
```

- `Certificate` 및 구체적인 오류 이유를 사용하여 
새 예외를 작성합니다. 
오류 이유에 따라 새 예외에 대한 
설명 메시지가 자동으로 제공됩니다.

**Parameters:**
- `status` - 예외 이유. 상태는 BAD_EXTENSIONS 및 
VERIFICATION_FAILED 내에 있어야 합니다.

### CertificateException

```java
public CertificateException(String message,
                            Certificate certificate,
                            byte status)
```

- 메시지, `Certificate` 및 구체적인 오류 이유를 사용하여 
새 예외를 작성합니다.

**Parameters:**
- `status` - 예외 이유. 
상태는 BAD_EXTENSIONS 및 
VERIFICATION_FAILED 내에 있어야 합니다.

### getCertificate

```java
public Certificate getCertificate()
```

**Returns:**
- 오류가 있는 `Certificate`

### getReason

```java
public byte getReason()
```

**Returns:**
- 이유 코드

## 생성자 상세

### CertificateException

```java
public CertificateException(Certificate certificate,
                            byte status)
```

- `Certificate` 및 구체적인 오류 이유를 사용하여 
새 예외를 작성합니다. 
오류 이유에 따라 새 예외에 대한 
설명 메시지가 자동으로 제공됩니다.

**Parameters:**
- `status` - 예외 이유. 상태는 BAD_EXTENSIONS 및 
VERIFICATION_FAILED 내에 있어야 합니다.

### CertificateException

```java
public CertificateException(String message,
                            Certificate certificate,
                            byte status)
```

- 메시지, `Certificate` 및 구체적인 오류 이유를 사용하여 
새 예외를 작성합니다.

**Parameters:**
- `status` - 예외 이유. 
상태는 BAD_EXTENSIONS 및 
VERIFICATION_FAILED 내에 있어야 합니다.

### getCertificate

```java
public Certificate getCertificate()
```

**Returns:**
- 오류가 있는 `Certificate`

### getReason

```java
public byte getReason()
```

**Returns:**
- 이유 코드

## 메서드 상세

### getCertificate

```java
public Certificate getCertificate()
```

**Returns:**
- 오류가 있는 `Certificate`

### getReason

```java
public byte getReason()
```

**Returns:**
- 이유 코드
