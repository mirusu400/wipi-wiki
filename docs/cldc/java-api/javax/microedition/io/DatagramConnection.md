# Interface DatagramConnection

`package javax.microedition.io`

```text
 {protocol}://[{host}]:[{port}]
```

## 설명

데이터그램 연결은 "클라이언트" 모드나 "서버" 모드로 열 수 있습니다. 
 "//{host}" 부분이 없으면 연결은 
 "서버"로 열립니다. "서버"로 열린다는 것은 클라이언트 응용 프로그램에서 
 통신을 시작한다는 것을 의미합니다. "//{host}" 부분이 지정되어 있으면 
 연결은 "클라이언트"로 열립니다.

예:

데이터그램을 받아들이기 위한 데이터그램 연결
 
 datagram://:1234

서버로 보내기 위한 데이터그램 연결 
 
 datagram://123.456.789.12:1234

호스트 이름이 지정되지 않은 "서버 모드"에서의 포트 번호는 
 수신 포트 번호입니다. 호스트 이름이 지정된 "클라이언트 모드"에서의 
 포트 번호는 대상 포트 번호입니다. 두 경우 모두, 회신 포트는 
 반드시 지정해야 합니다. "서버 모드"에서는 수신 및 전송에 
 모두 동일한 포트 번호가 사용됩니다. "클라이언트 모드"에서 회신 포트는 
 항상 동적으로 할당됩니다.

또한 데이터그램 객체가 J2SE (Java 2 Standard Edition)보다 
 추상적인 방법으로 할당됩니다. 
 구체적인 `DatagramPacket` 클래스를 제공하는 대신 
 추상적인 `Datagram` 인터페이스가 제공됩니다. 이를 통해 
 단일 플랫폼에서 여러 개의 다른 데이터그램 인터페이스를 
 동시에 지원할 수 있습니다. 데이터그램 객체는 
 `DatagramConnection` 객체의 `newDatagram` 메소드를 
 호출하여 할당해야 합니다. 
 결과로 만들어지는 객체는 다른 인터페이스 유형인 
 `javax.microedition.io.Datagram`을 사용하여 정의합니다.

**Since:**
- CLDC 1.0

## 메서드 요약

- `int getMaximumLength ()` — 데이터그램이 가질 수 있는 최대 길이를 가져옵니다.
- `int getNominalLength ()` — 데이터그램의 명목상의 길이를 가져옵니다.
- `Datagram newDatagram (byte[] buf, int size)` — 새로운 데이터그램 객체를 만듭니다.
- `Datagram newDatagram (byte[] buf, int size, String addr)` — 새로운 데이터그램 객체를 만듭니다.
- `Datagram newDatagram (int size)` — 새로운 데이터그램 객체를 만듭니다.
- `Datagram newDatagram (int size, String addr)` — 새로운 데이터그램 객체를 만듭니다.
- `void receive ( Datagram dgram)` — 데이터그램을 받습니다.
- `void send ( Datagram dgram)` — 데이터그램을 보냅니다.

## 메서드 상세

### getMaximumLength

```java
public int getMaximumLength()
                     throws IOException
```

**Returns:**
- 데이터그램의 최대 길이

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### getNominalLength

```java
public int getNominalLength()
                     throws IOException
```

**Returns:**
- 데이터그램의 명목상의 길이

**Throws:**
- `IOException` - I/O 오류가 발생한 경우

### send

```java
public void send(Datagram dgram)
          throws IOException
```

**Parameters:**
- `dgram` - 데이터그램

**Throws:**
- `InterruptedIOException` - 시간 초과 또는 중단이 발생한 경우

### receive

```java
public void receive(Datagram dgram)
             throws IOException
```

**Parameters:**
- `dgram` - 데이터그램

**Throws:**
- `InterruptedIOException` - 시간 초과 또는 중단이 발생한 경우

### newDatagram

```java
public Datagram newDatagram(int size)
                     throws IOException
```

**Parameters:**
- `size` - 데이터그램에 필요한 
 버퍼 크기

**Returns:**
- 새 데이터그램

**Throws:**
- `IllegalArgumentException` - 크기가 음수이거나 
 최대 크기보다 큰 경우

### newDatagram

```java
public Datagram newDatagram(int size,
                            String addr)
                     throws IOException
```

**Parameters:**
- `addr` - 데이터그램이 전송되는 
 I/O 주소

**Returns:**
- 새 데이터그램

**Throws:**
- `IllegalArgumentException` - 크기가 음수이거나 
 최대 크기보다 큰 경우 또는 
 주소 매개 변수가 유효하지 않은 경우

### newDatagram

```java
public Datagram newDatagram(byte[] buf,
                            int size)
                     throws IOException
```

**Parameters:**
- `size` - 데이터그램에 필요한 
 버퍼 크기

**Returns:**
- 새 데이터그램

**Throws:**
- `IllegalArgumentException` - 크기가 음수이거나 
 최대 크기 또는 지정된 버퍼의 길이보다 큰 경우 
 또는 버퍼 매개 변수가 유효하지 않은 
 경우

### newDatagram

```java
public Datagram newDatagram(byte[] buf,
                            int size,
                            String addr)
                     throws IOException
```

**Parameters:**
- `addr` - 데이터그램이 전송되는 
 I/O 주소

**Returns:**
- 새 데이터그램

**Throws:**
- `IllegalArgumentException` - 크기가 음수이거나 
 최대 크기 또는 지정된 버퍼의 길이보다 큰 경우 
 또는 주소나 버퍼 매개 변수가 
 유효하지 않은 경우
