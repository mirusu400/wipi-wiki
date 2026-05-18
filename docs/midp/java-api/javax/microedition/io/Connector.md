# Class Connector

`package javax.microedition.io`

```text
java.lang.Object
  |
  +--javax.microedition.io.Connector
```

## 설명

**extends Object:**

새로운 연결 객체를 만들기 위한 팩토리 클래스

시스템 등록 정보에서 읽은 플랫폼 이름에서 형성된 이름을 가진 
프로토콜 구현 클래스와 응용 프로그램 프로그래머가 
제공한 매개 변수 문자열에서 
추출한 요청된 연결의 프로토콜 이름을 
조회하여 동적으로 연결을 만듭니다. 

대상을 설명하는 매개 변수 문자열은 RFC 2396에 설명된 
URL 형식을 따라야 합니다. 
일반적인 형식은 다음과 같습니다.

`{scheme}:[{target}][{parms}]`

여기서 `{scheme}`은 *http*와 같은 
프로토콜 이름입니다.

`{target}`은 일반적으로 
일종의 네트워크 주소입니다.

모든 `{parms}`는 ";x=y" 형식의 일련의 등식으로 
형성됩니다(예: ";type=a").

선택 사항인 두 번째 매개 변수를 open 함수에 지정할 수도 있습니다. 
이것은 호출 코드의 의도를 프로토콜 핸들러에 표시하는 모드 플래그입니다. 
여기서 옵션은 연결이 읽기(READ), 쓰기(WRITE) 또는 
둘 다(READ_WRITE)가 될 것인지를 지정합니다. 
이러한 플래그 설정의 유효성은 프로토콜에 따라 결정됩니다. 
예를 들어, 프린터 연결은 읽기 액세스를 허용하지 않으며 
IllegalArgumentException을 발생시킵니다. 
모드 매개 변수를 지정하지 않으면 
기본적으로 READ_WRITE가 사용됩니다.

선택 사항인 세 번째 매개 변수는 호출 모드가 시간 초과 예외를 
처리할 수 있는지를 나타내는 부울 플래그입니다. 
이 플래그를 설정하면 프로토콜 구현에서 시간 초과 상황을 감지할 때 
InterruptedIOException을 발생시킬 수도 있습니다. 
이 플래그는 프로토콜 핸들러에게 제공되는 힌트일 뿐이며 
실제로 이러한 예외가 발생한다는 것을 보장하지는 않습니다. 
이 매개 변수를 설정하지 않으면 시간 초과 예외가 
발생하지 않습니다.

단순히 특정 입력 또는 출력 스트림에 액세스하기 위해 
연결을 여는 경우가 많기 때문에 이러한 용도로 4개의 편리한 함수가 제공됩니다. 
데이터그램 주소 지정에 대한 자세한 내용은 

``DatagramConnection``을 
참조하십시오.

**Since:**
- CLDC 1.0

## 필드 요약

- `static int READ` — 액세스 모드 READ.
- `static int READ_WRITE` — 액세스 모드 READ_WRITE.
- `static int WRITE` — 액세스 모드 WRITE.

## 메서드 요약

- `static Connection open ( String name)` — 연결을 만들어 엽니다.
- `static Connection open ( String name, int mode)` — 연결을 만들어 엽니다.
- `static Connection open ( String name, int mode, boolean timeouts)` — 연결을 만들어 엽니다.
- `static DataInputStream openDataInputStream ( String name)` — 연결 입력 스트림을 만들어 엽니다.
- `static DataOutputStream openDataOutputStream ( String name)` — 연결 출력 스트림을 만들어 엽니다.
- `static InputStream openInputStream ( String name)` — 연결 입력 스트림을 만들어 엽니다.
- `static OutputStream openOutputStream ( String name)` — 연결 출력 스트림을 만들어 엽니다.

## 필드 상세

### READ

```java
public static final int READ
```

**See Also:**
- `Constant Field Values`

### WRITE

```java
public static final int WRITE
```

**See Also:**
- `Constant Field Values`

### READ_WRITE

```java
public static final int READ_WRITE
```

**See Also:**
- `Constant Field Values`

### open

```java
public static Connection open(String name)
                       throws IOException
```

**Parameters:**
- `name` - 연결할 URL

**Returns:**
- 새로운 연결 객체

**Throws:**
- `SecurityException` - 요청한 프로토콜 핸들러가 
 허용되지 않는 경우

### open

```java
public static Connection open(String name,
                              int mode)
                       throws IOException
```

**Parameters:**
- `mode` - 액세스 모드

**Returns:**
- 새로운 연결 객체

**Throws:**
- `SecurityException` - 요청한 프로토콜 핸들러가 
 허용되지 않는 경우

### open

```java
public static Connection open(String name,
                              int mode,
                              boolean timeouts)
                       throws IOException
```

**Parameters:**
- `timeouts` - 호출자가 시간 초과 예외를 원한다는 것을 
 나타내는 플래그

**Returns:**
- 새로운 연결 객체

**Throws:**
- `SecurityException` - 요청한 프로토콜 핸들러가 
 허용되지 않는 경우

### openDataInputStream

```java
public static DataInputStream openDataInputStream(String name)
                                           throws IOException
```

**Parameters:**
- `name` - 연결할 URL

**Returns:**
- DataInputStream

**Throws:**
- `SecurityException` - 요청한 스트림에 대한 액세스가 
 허용되지 않는 경우

### openDataOutputStream

```java
public static DataOutputStream openDataOutputStream(String name)
                                             throws IOException
```

**Parameters:**
- `name` - 연결할 URL

**Returns:**
- DataOutputStream

**Throws:**
- `SecurityException` - 요청한 스트림에 대한 액세스가 
 허용되지 않는 경우

### openInputStream

```java
public static InputStream openInputStream(String name)
                                   throws IOException
```

**Parameters:**
- `name` - 연결할 URL

**Returns:**
- InputStream

**Throws:**
- `SecurityException` - 요청한 스트림에 대한 액세스가 
 허용되지 않는 경우

### openOutputStream

```java
public static OutputStream openOutputStream(String name)
                                     throws IOException
```

**Parameters:**
- `name` - 연결할 URL

**Returns:**
- OutputStream

**Throws:**
- `SecurityException` - 요청한 스트림에 대한 액세스가 
 허용되지 않는 경우

## 메서드 상세

### open

```java
public static Connection open(String name)
                       throws IOException
```

**Parameters:**
- `name` - 연결할 URL

**Returns:**
- 새로운 연결 객체

**Throws:**
- `SecurityException` - 요청한 프로토콜 핸들러가 
 허용되지 않는 경우

### open

```java
public static Connection open(String name,
                              int mode)
                       throws IOException
```

**Parameters:**
- `mode` - 액세스 모드

**Returns:**
- 새로운 연결 객체

**Throws:**
- `SecurityException` - 요청한 프로토콜 핸들러가 
 허용되지 않는 경우

### open

```java
public static Connection open(String name,
                              int mode,
                              boolean timeouts)
                       throws IOException
```

**Parameters:**
- `timeouts` - 호출자가 시간 초과 예외를 원한다는 것을 
 나타내는 플래그

**Returns:**
- 새로운 연결 객체

**Throws:**
- `SecurityException` - 요청한 프로토콜 핸들러가 
 허용되지 않는 경우

### openDataInputStream

```java
public static DataInputStream openDataInputStream(String name)
                                           throws IOException
```

**Parameters:**
- `name` - 연결할 URL

**Returns:**
- DataInputStream

**Throws:**
- `SecurityException` - 요청한 스트림에 대한 액세스가 
 허용되지 않는 경우

### openDataOutputStream

```java
public static DataOutputStream openDataOutputStream(String name)
                                             throws IOException
```

**Parameters:**
- `name` - 연결할 URL

**Returns:**
- DataOutputStream

**Throws:**
- `SecurityException` - 요청한 스트림에 대한 액세스가 
 허용되지 않는 경우

### openInputStream

```java
public static InputStream openInputStream(String name)
                                   throws IOException
```

**Parameters:**
- `name` - 연결할 URL

**Returns:**
- InputStream

**Throws:**
- `SecurityException` - 요청한 스트림에 대한 액세스가 
 허용되지 않는 경우

### openOutputStream

```java
public static OutputStream openOutputStream(String name)
                                     throws IOException
```

**Parameters:**
- `name` - 연결할 URL

**Returns:**
- OutputStream

**Throws:**
- `SecurityException` - 요청한 스트림에 대한 액세스가 
 허용되지 않는 경우
