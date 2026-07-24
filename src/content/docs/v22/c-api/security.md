---
title: "2.14. 보안통신"
---

## 2.14.1. 관련 자료형

본 절은 WIPI 응용프로그램이 SSL 프로토콜 기능을 제공하는 SSL 라이브러리에 대 한 함수 설명이다. 데이터타입의 이름은 대문자와 „_‟ 그리고 숫자로 이루어진다. 데이터타입 중에서 내 부를 노출하지 않는 데이터타입의 경우에는 handle을 나타내는 H로 시작하고, „_‟을 사용하지 않는다. SSL에서는 대부분의 데이터를 structure가 아닌 handle 형태로 다루어서, 데이터에 대한 직접적인 사용보다는 SSL API에서 제공되는 함수를 통해서 사용하도록 하고 있다.

#### HSSL

HSSL는 SSL handle을 나타내는 데이터타입이다. SSL handle은 메모리 상에 SSL 를 나타낸다.

#### SSL_VERSION

SSL 프로토콜 버전을 나타낸다.

```c
enum SSL_VERSION_E{
    SSL_VER_SSLv3 =0x0300,
    SSL_VER_TLSv1 =0x0301};
typedef enum SSL_VERSION_E SSL_VERSION;
```

Values SSL_VER_SSLv3 – 프로토콜 SSLv3 SSL_VER_TLSv1 – 프로토콜 TLSv1

#### SSL_CIPHERSUITE

SSL의 Cipher Suite Code를 나타낸다.

```c
enum SSL_CIPHERSUITE_E{
    SSL_CS_RSA_DES_192_CBC3_SHA = 0x0300000A,
    SSL_CS_RSA_SEED_CBC_MD5 = 0x0300ff01,
    SSL_CS_RSA_SEED_CBC_SHA = 0x0300ff02};
typedef enum SSL_CIPHERSUITE_E SSL_CIPHERSUITE;
```

Values SSL_CS_RSA_DES_192_CBC3_SHA – CipherSuite SSL3 RSA with 3DES EDE CBC SHA SSL_CS_RSA_SEED_CBC_MD5 – CipherSuite SSL3 RSA with SEED CBC MD5 SSL_CS_RSA_SEED_CBC_SHA – CipherSuite SSL3 RSA with SEED CBC SHA

**반환 값**

- `M_E_SSL_OK` - 성공적으로 수행 했음을 알림.
- `M_E_SSL_OUTOFMEMORY` - 메모리가 부족함을 알림.
- `M_E_SSL_INVALIDARG` - 하나, 혹은 그 이상의 인자가 잘못 되었음을 알림.
- `M_E_SSL_POINTER` - 잘못된 포인터 임을 알림.
- `M_E_SSL_HANDLE` - 잘못된 핸들임을 알림.
- `M_E_SSL_ABORT` - 진행이 취소되었음을 알림
- `M_E_SSL_FAIL` - 진행이 실패 하였음을 알림.
- `M_E_SSL_WOULDBLOCK` - SSL 통신 도중 Blocking 현상이 일어났음을 알림.
- `M_E_SSL_CERTIFICATE` - SSL 핸드쉐이킹 수행 중 인증서가 유효하지 않음을 알림.

## 2.14.2. 관련 API

SSL API는 WIPI 응용 프로그램이 SSL 프로토콜을 사용할 수 있도록 한다. 이 API 에서는 SSLv3, TLSv1 프로토콜과 인증서 처리 기능을 지원한다. SSLCONNECTCB

**프로토타입**

```c
void (*SSLCONNECTCB)(HSSL hSSL, M_Int32 nError, void* pParam);
```

**설명**

SSL 접속(`MC_secSSLConnect`)에 대한 결과 및 SSL 종료(`MC_secSSLShutdown`)에 대한 결과를 알려주는 콜백함수.

**매개 변수**

- `hSSL` - [in] SSL 핸들.
- `nError` - [in] `M_E_SSL_OK`: SSL 접속이 성공적으로 완료됨. `M_E_SSL_CERTIFICATE`: SSL 접속에 사용되는 인 증서가 유효하지 않음. `M_E_SSL_CLOSED`: SSL 접속이 종료됨. `M_E_SSL_FAIL`: 핸드쉐이크를 시도할수 있는 상태가 아닌 경우.
- `pParam` - [in] `MC_secSSLConnect()` 호출시에 입력한 값.

**부작용**

없음.

**참고 항목**

HSSL, `MC_secSSLConnect`, SSL_CIPHERSUITE

#### SSLWRITECB

**프로토타입**

```c
void (*SSLWRITECB)(HSSL hSSL, M_Int32 nError, void* pParam);
```

**설명**

`MC_secSSLWrite`()가 바로 SSL 쓰기를 수행할 수 없어 M_ESSL_E_WOULDBLOCK 을 반환할 경우 SSL 쓰기가 가능한 시점에 불리워지는 콜백함수.

**매개 변수**

- `hSSL` - [in] SSL 핸들.
- `nError` - [in] `M_E_SSL_OK`: SSL 쓰기가 가능함. `M_E_SSL_FAIL`: SSL 쓰기에 실패함.
- `pParam` - [in] `MC_secSSLWrite()` 호출시에 입력한 값.

**부작용**

없음.

**참고 항목**

HSSL, `MC_secSSLWrite`, SSL_CIPHERSUITE

#### SSLREADCB

**프로토타입**

```c
void (*SSLREADCB)(HSSL hSSL, M_Int32 nError, void* pParam);
```

**설명**

`MC_secSSLRead`()가 바로 SSL 읽기를 수행할 수 없어 M_E_SSL_E_WOULDBLOCK을 반환할 경우 SSL 읽기가 가능한 시점에 불리워지는 콜백함수.

**매개 변수**

- `hSSL` - [in] SSL 핸들.
- `nError` - [in] `M_E_SSL_OK`: SSL 읽기가 가능함. `M_E_SSL_FAIL`: SSL 읽기에 실패함.
- `pParam` - [in] `MC_secSSLRead()` 호출시에 입력한 값.

**부작용**

없음.

**참고 항목**

HSSL, `MC_secSSLRead`, SSL_CIPHERSUITE

### MC_secSSLNew

**프로토타입**

```c
HSSL MC_secSSLNew(void);
```

**설명**

SSL 핸들을 생성하고 값을 초기화 한다. 이 함수는 SSL 라이브러리를 사용하기 전 에 반드시 호출 되어야 한다. 이 함수가 돌려준 SSL 핸들은 모든 SSL API 함수를 실행하는데 필요하다.

**매개 변수**

없음

**반환 값**

성공

SSL 핸들
실패

`NULL`.

**부작용**

없음

**참고 항목**

`MC_secSSLFree`, HSSL, SSL_CIPHERSUITE

### MC_secSSLFree

**프로토타입**

```c
void MC_secSSLFree(HSSL hSSL);
```

**설명**

SSL 핸들을 제거한다.

**매개 변수**

- `hSSL` - [in] SSL 핸들

**반환 값**

없음

**부작용**

없음

**참고 항목**

HSSL, `MC_secSSLNew`, SSL_CIPHERSUITE

### MC_secSSLConnect

**프로토타입**

```c
M_Int32 MC_secSSLConnect(HSSL hSSL, M_Int32 nSocket, M_Char* szCN,
SSLCONNECTCB cbSSLConnect, void* pParam);
```

**설명**

주어진 SSL 핸들을 이용하여 지정한 서버에 SSL 접속을 시도한다.

**매개 변수**

- `hSSL` - [in] SSL 핸들.
- `nSocket` - [in] 외부에서 연결에 성공한 소켓 핸들.
- `szCN` - [in] 서버 인증시에 필요한 서버의 주소.
- `cbSSLConnect` - [in] 연결에 성공하거나 실패할 경우 불리는 콜백함수.
- `pParam` - [in] 콜백함수가 불릴 때 전달되는 값.

**반환 값**

성공

`M_E_SSL_OK`
실패

- `M_E_SSL_HANDLE` - 잘못된 SSL 핸들.
- `M_E_SSL_INVALIDARG` - 잘못된 소켓 핸들.
- `M_E_SSL_OUTOFMEMORY` - 메모리 에러.
- `M_E_SSL_WOULDBLOCK` - SSL 접속(handshake 과정) 진행중 (결과는 콜백 함수 를 통해 전달됨).
- `M_E_SSL_FAIL` - handshake를 시도할 수 있는 상태 가 아닌 경우

**부작용**

없음

**참고 항목**

HSSL, SSLCONNECTCB, SSL_CIPHERSUITE

### MC_secSSLAddCipherSuite

**프로토타입**

```c
M_Int32 MC_secSSLAddCipherSuite(HSSL hSSL, SSL_CIPHERSUITE nCipherSuite);
```

**설명**

SSL 통신을 위해 수행하는 Handshake 에서 사용할 클라이언트쪽 Cipher Suite 의 리스트에 Cipher Suite 을 추가 한다. Cipher Suite 은 `MC_secSSLConnect` 를 실행 하기 위해 필요한 것으로 `MC_secSSLConnect` 를 시도하기 전에 호출하여 Cipher Suite 을 추가한다. 또한 추 가할 수 있는 Cipher Suite 의 최대 가지수는 3개 이다. 이 함수를 호출하지 않고 SSL 접속을 시도하게 되면 기본값으로 지원하는 모든 Cipher Suite를 추가한다.

**매개 변수**

- `hSSL` - [in] SSL 핸들.
- `nCipherSuite` - [in] 추가할 Cipher Suite

**반환 값**

성공

`M_E_SSL_OK`
실패

- `M_E_SSL_HANDLE` - 잘못된 SSL 핸들.
- `M_E_SSL_INVALIDARG` - 잘못된 CipherSuite.
- `M_E_SSL_FAIL` - 이미 SSL 접속이 이루어져 있거나 종료중. 또는 더 이상 추가 할 수 없 거나 이미 추가되어 있음

**부작용**

없음

**참고 항목**

HSSL, SSL_CIPHERSUITE, `MC_secSSLClearCipherSuite`

### MC_secSSLClearCipherSuite

**프로토타입**

```c
M_Int32 MC_secSSLClearCipherSuite(HSSL hSSL);
```

**설명**

MC_secSSLAddCipherSuite로 추가한 Cipher Suite의 리스트를 모두 제거한다.

**매개 변수**

없음

**반환 값**

성공

`M_E_SSL_OK`
실패

- `M_E_SSL_HANDLE` - 잘못된 SSL 핸들.
- `M_E_SSL_FAIL` - 이미 SSL 접속이 이루어져 있거나 종료중

**부작용**

없음

**참고 항목**

HSSL, `MC_secSSLAddCipherSuite`, SSL_CIPHERSUITE

### MC_secSSLWrite

**프로토타입**

```c
M_Int32 MC_secSSLWrite(HSSL hSSL, M_Uint8* pData, M_Int32 nSize,
SSLWRITECB cbSSLWrite, void* pParam);
```

**설명**

SSL 핸들을 이용하여 접속된 채널을 통해 지정한 크기만큼 데이터를 전송을 시도한 다.

**매개 변수**

- `hSSL` - [in] SSL 핸들
- `pData` - [in] 전송할 데이터
- `nSize` - [in] 전송할 데이터의 크기
- `cbSSLWrite` - [in] SSL 통신이 blocking 상태가 되어 SSL_E_WOULDBLOCK를 반환할 경우에 데 이터 전송 결과를 알려줄 콜백함수
- `pParam` - [in] 콜백함수가 불리어 질 때 전달 되는 값.

**반환 값**


**반환 값**

성공

전송된 데이터 길이를 반환
실패

- `M_E_SSL_HANDLE` - 잘못된 SSL 핸들
- `M_E_SSL_HANDLE` - 잘못된 SSL 핸들
- `M_E_SSL_INVALIDARG` - 잘못된 버퍼 또는 버퍼 크기
- `M_E_SSL_OUTOFMEMORY` - 메모리 에러
- `M_E_SSL_WOULDBLOCK` - SSL이 즉시 데이터를 전송할 수 없 는 상태(결과는 콜 백 함수를 통해 알 려줌)
- `M_E_SSL_FAIL` - SSL 쓰기에 실패하였음

**부작용**

없음

**참고 항목**

HSSL, SSLREADCB, SSL_CIPHERSUITE

#### MC_secSSLRead()

**프로토타입**

```c
M_Int32 MC_secSSLRead(HSSL hSSL, M_Uint8* pData, M_Int32 nSize,
SSLREADCB cbSSLRead, void* pParam);
```

**설명**

주어진 SSL 핸들을 이용해 접속한 채널을 통해 주어진 크기만큼 데이터 읽기를 시 도한다.

**매개 변수**

- `hSSL` - [in] SSL 핸들
- `pData` - [out] 읽어들인 데이터를 저장할 버퍼
- `nSize` - [in] 읽어들일 데이터 크기
- `cbSSLRead` - [in] Socket이 blocking 상태가 되어 M_E_SSL_WOULDBLOCK를 반환할 경우에 데이터를 읽은 결과를 알려줄 콜백함수
- `pParam` - [in] 콜백함수가 불리어 질 때 전달되는 값.

**반환 값**

성공

전송받은 데이터의 길이를 반환.
실패

- `M_E_SSL_HANDLE` - 잘못된 SSL 핸들.
- `M_E_SSL_INVALIDARG` - 잘못된 버퍼 또는 버퍼 크기.
- `M_E_SSL_OUTOFMEMORY` - 메모리 에러.
- `M_E_SSL_WOULDBLOCK` - SSL이 즉시 데이터를 전송받을 수 없는 상태(결과는 콜백함수를 통해 알 려줌).
- `M_E_SSL_FAIL` - SSL 읽기에 실패하였음.

**부작용**

없음

**참고 항목**

HSSL, SSLREADCB, SSL_CIPHERSUITE

### MC_secSSLInstallCert

**프로토타입**

```c
M_Int32 MC_secSSLInstallCert(HSSL hSSL);
```

**설명**

서버 인증서(Peer 인증서)를 저장소에 저장한다.

**매개 변수**

- `hSSL` - [in] SSL 핸들.

**반환 값**

성공

`M_E_SSL_OK`
실패

- `M_E_SSL_HANDLE` - 잘못된 SSL 핸들.
- `M_E_SSL_OUTOFMEMORY` - 메모리(시 스템) 에러.
- `M_E_SSL_FAIL` - 인증서 설 치 실패.

**부작용**

없음.

**참고 항목**

HSSL, SSL_CIPHERSUITE, `MC_secSSLRemoveCertAll`

### MC_secSSLRemoveAll

**프로토타입**

```c
M_Int32 MC_secSSLRemoveAll(HSSL hSSL);
```

**설명**

인증서 저장소에 있는 모든 인증서를 제거한다.

**매개 변수**

- `hSSL` - [in] SSL 핸들.

**반환 값**

성공

`M_E_SSL_OK`
실패

- `M_E_SSL_HANDLE` - 잘못된 SSL 핸들.
- `M_E_SSL_FAIL` - 인증서 제거 실패.

**부작용**

없음.

**참고 항목**

HSSL, SSL_CIPHERSUITE, `MC_secSSLInstallCert`

### MC_secSSLContinue

**프로토타입**

```c
M_Int32 MC_secSSLContinue(HSSL hSSL);
```

**설명**

SSL 접속 수행중에 서버 인증서를 신뢰할 수 없을 경우 접속이 중단된다. 이때 중단 되었던 SSL 접속을 계속 진행하도록 한다.

**매개 변수**

- `hSSL` - [in] SSL 핸들. 반환값. 성공 `M_E_SSL_OK` 실패 `M_E_SSL_HANDLE` 잘못된 SSL 핸들. `M_E_SSL_FAIL` SSL 접속을 다시 수행하는데 실패

**부작용**

없음.

**참고 항목**

HSSL, SSL_CIPHERSUITE

### MC_secSSLVer

**프로토타입**

```c
M_Int32 MC_secSSLVer();
```

**설명**

TLS 라이브러리의 버전 정보를 얻는다.

**매개 변수**

없음
반환값.
성공
- `TLS` - 라이브러리 버전 실패
- `M_E_SSL_FAIL` - SSL 라이브러리 버전 정보 얻는데 실패.

**부작용**

없음.

**참고 항목**

HSSL, SSL_CIPHERSUITE

### MC_secSSLShutdown

**프로토타입**

```c
M_Int32 MC_secSSLShutdown(HSSL hSSL, M_Int32 nReason);
```

**설명**

주어진 SSL 핸들을 이용해 접속을 종료한다.

**매개 변수**

- `hSSL` - [in] SSL 핸들.
- `nReason` - [in] 접속 종료의 이유(외부 네트워크 종료시에는 -1을 정 상 종료시에는 0을 입력한다.

**반환 값**

성공

`M_E_SSL_OK`.
실패

- `M_E_SSL_HANDLE` - 잘못된 SSL 핸들
- `M_E_SSL_FAIL` - SSL 접속 종료 실패
- `M_E_SSL_WOULDBLOCK` - 즉시 종료할 수 없는 상 태 (SSLCONNECTCB에서 결과를 확인해야 함

**부작용**

없음

**참고 항목**

HSSL, SSL_CIPHERSUITE, SSLCONNECTCB
