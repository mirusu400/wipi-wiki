# Class Throwable

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Throwable
```

## 설명

**Direct Known Subclasses:**
- `Error`, `Exception`

**extends Object:**

`Throwable` 클래스는 Java 언어에서 모든 오류와 
 예외의 수퍼 클래스입니다. 이 클래스 또는 
 서브 클래스 중 하나의 인스턴스인 객체만 Java 가상 머신이나 
 Java `throw` 문에서 발생할 수 있습니다. 
 이와 유사하게, 이 클래스 또는 서브 클래스 중 하나만 
 `catch` 문에서 인자 유형으로 사용될 수 
 있습니다.

두 서브 클래스인 ``Error``와 ``Exception``의 
 인스턴스는 일반적으로 예외 상황이 발생했음을 나타내는 데 
 사용됩니다. 대체로 이러한 인스턴스는 예외 상황의 맥락에서 
 스택 추적 데이터와 같은 해당 정보를 
 포함하도록 새로 만들어집니다.

관례적으로 `Throwable` 클래스와 서브 클래스에는 
 인자를 사용하지 않는 구성자와 오류 메시지를 만들 수 있는 
 `String` 인자를 사용하는 구성자가 
 있습니다.

`Throwable` 클래스에는 작성 당시의 스레드 실행 스택의 
 스냅샷이 있습니다. 오류에 대한 추가 정보를 제공하는 
 메시지 문자열도 포함될 수 
 있습니다.

아래에서는 예외를 파악하는 한 가지 예를 보여 줍니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- Throwable () null 을 오류 메시지 문자열로 사용하여 새로운 Throwable 을 
 구성합니다.
- Throwable ( String message) 지정한 오류 메시지를 사용하여 새로운 Throwable 을 
 구성합니다.

## 메서드 요약

- `String getMessage ()` — 이 Throwable 객체의 오류 메시지 문자열을 반환합니다.
- `void printStackTrace ()` — 이 Throwable 객체와 해당 역추적을 표준 오류 스트림으로 인쇄합니다.
- `String toString ()` — 이 Throwable 객체에 대한 짧은 설명을 반환합니다.

## 생성자 상세

### Throwable

```java
public Throwable()
```

- `null`을 오류 메시지 문자열로 사용하여 새로운 `Throwable`을 
 구성합니다.

### Throwable

```java
public Throwable(String message)
```

- 지정한 오류 메시지를 사용하여 새로운 `Throwable`을 
 구성합니다.

**Parameters:**
- `message` - 오류 메시지. 오류 메시지는 저장되어 
 나중에 ``getMessage()`` 메소드로 검색할 수 있습니다.

### getMessage

```java
public String getMessage()
```

**Returns:**
- 오류 메시지 문자열을 사용하여 ``만들어진`` 경우에는 `Throwable` 객체의 오류 메시지 
 문자열, 오류 메시지 없이 ``만들어진`` 경우에는 
 `null`

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 `Throwable`의 문자열 표현

### printStackTrace

```java
public void printStackTrace()
```

이 Throwable 객체와 해당 역추적을 
 표준 오류 스트림으로 인쇄합니다. 이 메소드는 오류 출력 스트림에서 System.err 필드 값인 이 Throwable 객체의 
 스택 추적을 인쇄합니다. 출력의 첫 행에는 이 객체에 대한 toString() 메소드가 결과가 
 포함됩니다. 역추적 정보의 형식은 구현별로 다릅니다.

## 메서드 상세

### getMessage

```java
public String getMessage()
```

**Returns:**
- 오류 메시지 문자열을 사용하여 ``만들어진`` 경우에는 `Throwable` 객체의 오류 메시지 
 문자열, 오류 메시지 없이 ``만들어진`` 경우에는 
 `null`

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 이 `Throwable`의 문자열 표현

### printStackTrace

```java
public void printStackTrace()
```

이 Throwable 객체와 해당 역추적을 
 표준 오류 스트림으로 인쇄합니다. 이 메소드는 오류 출력 스트림에서 System.err 필드 값인 이 Throwable 객체의 
 스택 추적을 인쇄합니다. 출력의 첫 행에는 이 객체에 대한 toString() 메소드가 결과가 
 포함됩니다. 역추적 정보의 형식은 구현별로 다릅니다.
