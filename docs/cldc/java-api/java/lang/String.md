# Class String

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.String
```

## 설명

**extends Object:**

`String` 클래스는 문자열을 나타냅니다. 
 `"abc"`와 같은 Java 프로그램의 모든 문자열 리터럴은 
 이 클래스의 인스턴스로 구현됩니다.

문자열은 상수이므로 만든 후에 값을 변경할 수 없습니다. 
 문자열 버퍼는 가변 문자열을 지원합니다. 문자열 객체는 
 불변이기 때문에 공유할 수 있습니다. 예를 들면 다음과 같습니다.

위의 결과 값은 다음 표현식의 결과와 같습니다.

아래에는 문자열 사용 방법에 대한 다른 예가 나와 있습니다.

`String` 클래스에는 시퀀스의 
 개별 문자 검사, 문자열 비교, 문자열 검색, 하위 문자열 추출, 
 모든 문자를 대문자 또는 소문자로 변환한 
 문자열 복사본 만들기 등을 위한 메소드가 포함되어 
 있습니다.

Java 언어는 문자열 연결 연산자( + )와 
 다른 객체를 문자열로 변환하는 메소드를 제공합니다. 
 문자열 연결은 `StringBuffer` 클래스와 
 해당 `append` 메소드를 통해 구현됩니다. 
 문자열 변환은 `Object`에 정의된 
 `toString` 메소드를 통해 구현되며 
 Java의 모든 클래스가 상속 받습니다. 
 문자열 연결과 변환에 대한 자세한 내용은 
 Gosling, Joy, and Steele, *The Java Language Specification*을 
 참조하십시오.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``Object.toString()``, 
``StringBuffer``, 
``StringBuffer.append(boolean)``, 
``StringBuffer.append(char)``, 
``StringBuffer.append(char[])``, 
``StringBuffer.append(char[], int, int)``, 
``StringBuffer.append(int)``, 
``StringBuffer.append(long)``, 
``StringBuffer.append(java.lang.Object)``, 
``StringBuffer.append(java.lang.String)``

## 생성자 요약

- String () 빈 문자 시퀀스를 나타내도록 새로 만든 String 객체를 
 초기화합니다.
- String (byte[] bytes) 플랫폼의 기본 문자 인코딩을 사용하여 지정된 바이트 배열을 
 변환함으로써 새로운 String 을 구성합니다.
- String (byte[] bytes,
 int off,
 int len) 플랫폼의 기본 문자 인코딩을 사용하여 지정된 바이트 하위 배열을 
 변환함으로써 새로운 String 을 구성합니다.
- String (byte[] bytes,
 int off,
 int len, String enc) 지정된 문자 인코딩을 사용하여 지정된 바이트 하위 배열을 변환함으로써 
 새로운 String 을 구성합니다.
- String (byte[] bytes, String enc) 지정된 문자 인코딩을 사용하여 지정된 바이트 배열을 변환함으로써 
새로운 String 을 구성합니다.
- String (char[] value) 현재 문자 배열 인자에 포함된 문자 시퀀스를 나타내도록 
 새로운 String 을 할당합니다.
- String (char[] value,
 int offset,
 int count) 문자 배열 인자의 하위 배열 문자가 포함되는 
 새로운 String 을 할당합니다.
- String ( String value) 인자와 같은 문자 시퀀스를 나타내도록 새로 만든 String 객체를 초기화합니다.
- String ( StringBuffer buffer) 현재 문자열 버퍼 인자에 있는 문자 시퀀스가 포함되는 
 새로운 문자열을 할당합니다.

## 메서드 요약

- `char charAt (int index)` — 지정된 색인의 문자를 반환합니다.
- `int compareTo ( String anotherString)` — 두 문자열을 사전적으로 비교합니다.
- `String concat ( String str)` — 지정된 문자열을 이 문자열의 끝에 연결합니다.
- `boolean endsWith ( String suffix)` — 이 문자열이 지정된 접미어로 끝나는지 테스트합니다.
- `boolean equals ( Object anObject)` — 이 문자열을 지정된 객체와 비교합니다.
- `boolean equalsIgnoreCase ( String anotherString)` — 대소문자와 상관없이 이 String 을 다른 String 과 비교합니다.
- `byte[] getBytes ()` — 플랫폼의 기본 문자 인코딩에 따라 이 String 을 바이트로 변환하여 결과를 새로운 바이트 배열에 저장합니다.
- `byte[] getBytes ( String enc)` — 지정된 문자 인코딩에 따라 이 String 을 바이트로 변환하여 결과를 새로운 바이트 배열에 저장합니다.
- `void getChars (int srcBegin, int srcEnd, char[] dst, int dstBegin)` — 이 문자열의 문자를 대상 문자 배열에 복사합니다.
- `int hashCode ()` — 이 문자열의 해시 코드를 반환합니다.
- `int indexOf (int ch)` — 이 문자열에서 지정된 문자의 첫 항목 색인을 반환합니다.
- `int indexOf (int ch, int fromIndex)` — 지정된 색인부터 찾기 시작하여 이 문자열에서 지정된 문자의 첫 항목 색인을 반환합니다.
- `int indexOf ( String str)` — 이 문자열에서 지정된 하위 문자열의 첫 항목 색인을 반환합니다.
- `int indexOf ( String str, int fromIndex)` — 지정된 색인부터 시작하여 이 문자열에서 지정된 하위 문자열의 첫 항목 색인을 반환합니다.
- `String intern ()` — 이 문자열 객체의 표준 표현을 반환합니다.
- `int lastIndexOf (int ch)` — 이 문자열에서 지정된 문자의 마지막 항목 색인을 반환합니다.
- `int lastIndexOf (int ch, int fromIndex)` — 지정된 색인부터 역순으로 검색하여 이 문자열에서 지정된 문자의 마지막 항목 색인을 반환합니다.
- `int length ()` — 이 문자열의 길이를 반환합니다.
- `boolean regionMatches (boolean ignoreCase, int toffset, String other, int ooffset, int len)` — 두 문자열 영역이 같은지 테스트합니다.
- `String replace (char oldChar, char newChar)` — 이 문자열의 모든 oldChar 항목을 newChar 로 바꾼 새 문자열을 반환합니다.
- `boolean startsWith ( String prefix)` — 이 문자열이 지정된 접두어로 시작하는지 테스트합니다.
- `boolean startsWith ( String prefix, int toffset)` — 이 문자열이 지정된 색인에서 시작하는 지정된 접두어로 시작하는지 테스트합니다.
- `String substring (int beginIndex)` — 이 문자열의 하위 문자열인 새 문자열을 반환합니다.
- `String substring (int beginIndex, int endIndex)` — 이 문자열의 하위 문자열인 새 문자열을 반환합니다.
- `char[] toCharArray ()` — 이 문자열을 새 문자 배열로 변환합니다.
- `String toLowerCase ()` — 이 String 의 모든 문자를 소문자로 변환합니다.
- `String toString ()` — 문자열 객체가 그대로 반환됩니다.
- `String toUpperCase ()` — 이 String 의 모든 문자를 대문자로 변환합니다.
- `String trim ()` — 이 문자열의 양 끝에서 공백을 제거합니다.
- `static String valueOf (boolean b)` — boolean 인자의 문자열 표현을 반환합니다.
- `static String valueOf (char c)` — char 인자의 문자열 표현을 반환합니다.
- `static String valueOf (char[] data)` — char 배열 인자의 문자열 표현을 반환합니다.
- `static String valueOf (char[] data, int offset, int count)` — char 배열 인자의 특정 하위 배열의 문자열 표현을 반환합니다.
- `static String valueOf (double d)` — double 인자의 문자열 표현을 반환합니다.
- `static String valueOf (float f)` — float 인자의 문자열 표현을 반환합니다.
- `static String valueOf (int i)` — int 인자의 문자열 표현을 반환합니다.
- `static String valueOf (long l)` — long 인자의 문자열 표현을 반환합니다.
- `static String valueOf ( Object obj)` — Object 인자의 문자열 표현을 반환합니다.

## 생성자 상세

### String

```java
public String()
```

- 빈 문자 시퀀스를 나타내도록 새로 만든 `String` 객체를 
 초기화합니다.

### String

```java
public String(String value)
```

- 인자와 같은 문자 시퀀스를 나타내도록 새로 만든 `String` 
 객체를 초기화합니다. 즉, 새로 만든 문자열은 
 인자 문자열의 복사본입니다.

**Parameters:**
- `value` - `String`

### String

```java
public String(char[] value)
```

- 현재 문자 배열 인자에 포함된 문자 시퀀스를 나타내도록 
 새로운 `String`을 할당합니다. 
 문자 배열의 내용이 복사됩니다. 이후에 문자 배열을 수정해도 
 새로 만든 문자열에는 영향을 주지 
 않습니다.

**Parameters:**
- `value` - 문자열의 초기 값

**Throws:**
- `NullPointerException` - `value`가 `null`인 경우

### String

```java
public String(char[] value,
              int offset,
              int count)
```

- 문자 배열 인자의 하위 배열 문자가 포함되는 
 새로운 `String`을 할당합니다. 
 `offset` 인자는 하위 배열에서 
 첫 문자의 색인이며 `count` 인자는 
 하위 배열의 길이를 지정합니다. 하위 배열의 내용이 복사됩니다. 
 이후에 문자 배열을 수정해도 새로 만든 문자열에는 
 영향을 주지 않습니다.

**Parameters:**
- `count` - 길이

**Throws:**
- `NullPointerException` - `value`가 
 `null`인 경우

### String

```java
public String(byte[] bytes,
              int off,
              int len,
              String enc)
       throws UnsupportedEncodingException
```

- 지정된 문자 인코딩을 사용하여 지정된 바이트 하위 배열을 변환함으로써 
 새로운 `String`을 구성합니다. 새로운 
 `String`의 길이는 인코딩 기능이므로 
 하위 배열의 길이와 다를 수도 있습니다.

**Parameters:**
- `enc` - 문자 인코딩 이름

**Throws:**
- `UnsupportedEncodingException` - 명명된 인코딩이 지원되지 않는 경우

**Since:**
- JDK1.1

### String

```java
public String(byte[] bytes,
              String enc)
       throws UnsupportedEncodingException
```

- 지정된 문자 인코딩을 사용하여 지정된 바이트 배열을 변환함으로써 
새로운 `String`을 구성합니다. 새로운 
`String`의 길이는 인코딩 기능이므로 
바이트 배열의 길이와 다를 수도 있습니다.

**Parameters:**
- `enc` - 지원되는 문자 인코딩 이름

**Throws:**
- `UnsupportedEncodingException` - 명명된 인코딩이 지원되지 않는 경우

**Since:**
- JDK1.1

### String

```java
public String(byte[] bytes,
              int off,
              int len)
```

- 플랫폼의 기본 문자 인코딩을 사용하여 지정된 바이트 하위 배열을 
 변환함으로써 새로운 `String`을 구성합니다. 새로운 
 `String`의 길이는 인코딩 기능이므로 
 하위 배열의 길이와 다를 수도 있습니다.

**Parameters:**
- `len` - 변환할 바이트 수

**Since:**
- JDK1.1

### String

```java
public String(byte[] bytes)
```

- 플랫폼의 기본 문자 인코딩을 사용하여 지정된 바이트 배열을 
 변환함으로써 새로운 `String`을 구성합니다. 새로운 
 `String`의 길이는 인코딩 기능이므로 
 바이트 배열의 길이와 다를 수도 있습니다.

**Parameters:**
- `bytes` - 문자로 변환되는 바이트

**Since:**
- JDK1.1

### String

```java
public String(StringBuffer buffer)
```

- 현재 문자열 버퍼 인자에 있는 문자 시퀀스가 포함되는 
 새로운 문자열을 할당합니다. 문자열 버퍼의 내용이 복사됩니다. 이후에 
 문자열 버퍼를 수정해도 새로 만든 문자열에는 
 영향을 주지 않습니다.

**Parameters:**
- `buffer` - `StringBuffer`

**Throws:**
- `NullPointerException` - `buffer`가 
 `null`인 경우

### length

```java
public int length()
```

**Returns:**
- 이 객체가 나타내는 문자 시퀀스의 
 길이

### charAt

```java
public char charAt(int index)
```

**Parameters:**
- `index` - 문자 색인

**Returns:**
- 이 문자열에서 지정된 색인의 문자. 
 첫 문자는 색인 `0`에 지정되어 있습니다.

**Throws:**
- `IndexOutOfBoundsException` - `index` 
 인자가 음수이거나 이 문자열의 길이보다 
 작지 않은 경우

### getChars

```java
public void getChars(int srcBegin,
                     int srcEnd,
                     char[] dst,
                     int dstBegin)
```

**Parameters:**
- `dstBegin` - 대상 배열의 시작 오프셋

**Throws:**
- `NullPointerException` - `dst`가 `null`인 경우

### getBytes

```java
public byte[] getBytes(String enc)
                throws UnsupportedEncodingException
```

**Parameters:**
- `enc` - 문자 인코딩 이름

**Returns:**
- 결과로 생성된 바이트 배열

**Throws:**
- `UnsupportedEncodingException` - 명명된 인코딩이 지원되지 않는 경우

**Since:**
- JDK1.1

### getBytes

```java
public byte[] getBytes()
```

**Returns:**
- 결과로 생성된 바이트 배열

**Since:**
- JDK1.1

### equals

```java
public boolean equals(Object anObject)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `anObject` - 이 `String`과 비교할 
 객체

**Returns:**
- `String`이 같으면 `true`, 다르면 
 `false`

**See Also:**
- ``compareTo(java.lang.String)``, 
``equalsIgnoreCase(java.lang.String)``

### equalsIgnoreCase

```java
public boolean equalsIgnoreCase(String anotherString)
```

**Parameters:**
- `anotherString` - 이 `String`과 비교할 
 `String`

**Returns:**
- 인자가 `null`이 아니고 
 `String`이 같으면 대소문자와 상관없이 
 `true`, 그렇지 않으면 `false`

**See Also:**
- ``equals(Object)``, 
``Character.toLowerCase(char)``, 
``Character.toUpperCase(char)``

### compareTo

```java
public int compareTo(String anotherString)
```

**Parameters:**
- `anotherString` - 비교되는 `String`

**Returns:**
- 인자 문자열이 이 문자열과 같으면 값 
 `0`, 이 문자열이 
 사전적으로 문자열 인자보다 작으면 
 `0`보다 작은 값, 이 문자열이 문자열 인자보다 
 사전적으로 크면 `0`보다 큰 값

**Throws:**
- `NullPointerException` - `anotherString`이 
 `null`인 경우

### regionMatches

```java
public boolean regionMatches(boolean ignoreCase,
                             int toffset,
                             String other,
                             int ooffset,
                             int len)
```

**Parameters:**
- `len` - 비교할 문자 수

**Returns:**
- 이 문자열의 지정된 하위 영역이 문자열 인자의 
 지정된 하위 영역과 일치하면 `true`, 
 그렇지 않으면 `false`. 
 정확한 일치인지 또는 대소문자를 무시한 일치인지는 `ignoreCase` 
 인자에 따라 결정됩니다.

### startsWith

```java
public boolean startsWith(String prefix,
                          int toffset)
```

**Parameters:**
- `toffset` - 문자열에서 찾기 시작할 위치

**Returns:**
- 인자가 나타내는 문자 시퀀스가 색인 
 `toffset`에서 시작하는 이 객체의 하위 문자열 
 접두어이면 `true`, 
 그렇지 않으면 `false`. 
 `toffset`이 음수이거나 이 `String` 
 객체보다 크면 결과는 `false`가 됩니다. 
 그렇지 않으면 결과는 다음 표현식의 결과와 같습니다.
 
 this.subString(toffset).startsWith(prefix)

**Throws:**
- `NullPointerException` - `prefix`가 
 `null`인 경우

### startsWith

```java
public boolean startsWith(String prefix)
```

**Parameters:**
- `prefix` - 접두어

**Returns:**
- 인자가 나타내는 문자 시퀀스가 이 문자열이 나타내는 
 문자 시퀀스의 접두어이면 `true`, 
 그렇지 않으면 `false`. 인자가 빈 문자열이거나 
 ``equals(Object)`` 메소드로 확인하여 
 이 `String` 객체와 같은 경우에도 
 `true`가 
 반환됩니다.

**Throws:**
- `NullPointerException` - `prefix`가 
 `null`인 경우

**Since:**
- JDK1.0

### endsWith

```java
public boolean endsWith(String suffix)
```

**Parameters:**
- `suffix` - 접미어

**Returns:**
- 인자가 나타내는 문자 시퀀스가 이 객체가 나타내는 문자 시퀀스의 접미어이면 
 `true`, 그렇지 않으면 `false`. 
 인자가 빈 문자열이거나 ``equals(Object)`` 
 메소드로 확인하여 
 이 `String` 객체와 같은 경우에도 
 결과는 `true`가 됩니다.

**Throws:**
- `NullPointerException` - `suffix`가 
 `null`인 경우

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 이 객체의 해시 코드 값

**See Also:**
- ``Object.equals(java.lang.Object)``, 
``Hashtable``

### indexOf

```java
public int indexOf(int ch)
```

**Parameters:**
- `ch` - 문자

**Returns:**
- 이 객체가 나타내는 문자 시퀀스에서 문자의 
 첫 항목 색인 또는 해당 문자가 없는 경우 
 `-1`

### indexOf

```java
public int indexOf(int ch,
                   int fromIndex)
```

**Parameters:**
- `fromIndex` - 검색이 시작되는 색인

**Returns:**
- 이 객체가 나타내는 문자 시퀀스에서 
 `fromIndex`보다 크거나 같은, 
 문자의 첫 항목 색인 또는 
 해당 문자가 없는 경우 `-1`

### lastIndexOf

```java
public int lastIndexOf(int ch)
```

**Parameters:**
- `ch` - 문자

**Returns:**
- 이 객체가 나타내는 문자 시퀀스에서 
 문자의 마지막 항목 색인 
 또는 해당 문자가 없는 경우 `-1`

### lastIndexOf

```java
public int lastIndexOf(int ch,
                       int fromIndex)
```

**Parameters:**
- `fromIndex` - 검색이 시작되는 색인. 
 `fromIndex` 값에는 어떤 제한도 없습니다. 
 값이 문자열 길이보다 크거나 같으면 
 문자열 길이보다 하나 작은 값과 
 같은 경우처럼 전체 문자열이 검색될 수도 있습니다. 
 값이 음수이면 값이 -1인 경우와 
 마찬가지로 -1이 반환됩니다.

**Returns:**
- 이 객체가 나타내는 문자 시퀀스에서 
 `fromIndex`보다 작거나 같은, 
 문자의 마지막 항목 색인 또는 해당 문자가 이 위치 앞에 없는 경우 
 `-1`

### indexOf

```java
public int indexOf(String str)
```

**Parameters:**
- `str` - 모든 문자열

**Returns:**
- 문자열 인자가 이 객체 내의 하위 문자열이면 
 첫 하위 문자열의 첫 문자 색인이 반환됩니다. 
 하위 문자열이 아니면 
 `-1`이 반환됩니다.

**Throws:**
- `NullPointerException` - `str`이 
 `null`인 경우

### indexOf

```java
public int indexOf(String str,
                   int fromIndex)
```

**Parameters:**
- `fromIndex` - 검색이 시작되는 색인

**Returns:**
- 문자열 인자가 `fromIndex`보다 작지 않은 
 색인에서 시작하는 이 객체 내의 하위 문자열이면 
 첫 하위 문자열의 첫 문자 색인이 반환됩니다. 
 `fromIndex` 이상에서 
 시작하는 하위 문자열이 아니면 
 `-1`이 반환됩니다.

**Throws:**
- `NullPointerException` - `str`이 
 `null`인 경우

### substring

```java
public String substring(int beginIndex)
```

**Parameters:**
- `beginIndex` - 시작 색인(포함)

**Returns:**
- 지정된 하위 문자열

**Throws:**
- `IndexOutOfBoundsException` - `beginIndex`가 음수이거나 
 `String` 객체의 길이보다 큰 경우

### substring

```java
public String substring(int beginIndex,
                        int endIndex)
```

**Parameters:**
- `endIndex` - 끝 색인(포함하지 않음)

**Returns:**
- 지정된 하위 문자열

**Throws:**
- `IndexOutOfBoundsException` - `beginIndex`가 음수이거나, 
 `endIndex`가 `String` 
 객체의 길이보다 크거나 
 `beginIndex`가 
 `endIndex`보다 큰 경우

### concat

```java
public String concat(String str)
```

**Parameters:**
- `str` - 이 `String`의 끝에 연결되는 
 `String`

**Returns:**
- 이 객체의 문자 뒤에 문자열 인자의 
 문자를 연결한 문자열

**Throws:**
- `NullPointerException` - `str`이 
 `null`인 경우

### replace

```java
public String replace(char oldChar,
                      char newChar)
```

**Parameters:**
- `newChar` - 새 문자

**Returns:**
- 이 문자열의 모든 `oldChar` 항목을 
 `newChar`로 바꿔서 파생된 문자열

### toLowerCase

```java
public String toLowerCase()
```

**Returns:**
- 소문자로 변환된 String

**See Also:**
- ``Character.toLowerCase(char)``, 
``toUpperCase()``

### toUpperCase

```java
public String toUpperCase()
```

**Returns:**
- 대문자로 변환된 String

**See Also:**
- ``Character.toLowerCase(char)``, 
``toUpperCase()``

### trim

```java
public String trim()
```

**Returns:**
- 앞과 끝에서 공백을 제거한 이 문자열

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 문자열 자체

### toCharArray

```java
public char[] toCharArray()
```

**Returns:**
- 이 문자열의 길이와 같고 문자열이 나타내는 
 문자 시퀀스를 포함하도록 내용이 초기화된 
 새로 할당된 문자 배열

### valueOf

```java
public static String valueOf(Object obj)
```

**Parameters:**
- `obj` - `Object`

**Returns:**
- 인자가 `null`이면 `"null"`과 같은 문자열, 
 그렇지 않으면 `obj.toString()` 
 값이 반환됩니다.

**See Also:**
- ``Object.toString()``

### valueOf

```java
public static String valueOf(char[] data)
```

**Parameters:**
- `data` - `char` 배열

**Returns:**
- 문자 배열 인자에 포함된 문자 시퀀스를 
 나타내는 새로 할당된 문자열

### valueOf

```java
public static String valueOf(char[] data,
                             int offset,
                             int count)
```

**Parameters:**
- `count` - `String` 값의 길이

**Returns:**
- 문자 배열 인자의 하위 배열에 
 포함된 문자 시퀀스를 
 나타내는 새로 할당된 문자열

**Throws:**
- `IndexOutOfBoundsException` - `offset`이 음수 또는 `count`가 
 음수이거나 `offset+count`가 
 `data.length`보다 큰 경우

### valueOf

```java
public static String valueOf(boolean b)
```

**Parameters:**
- `b` - `boolean`

**Returns:**
- 인자가 `true`이면 
 `"true"`와 같은 문자열이 반환됩니다. 
 그렇지 않으면 `"false"`와 같은 문자열이 반환됩니다.

### valueOf

```java
public static String valueOf(char c)
```

**Parameters:**
- `c` - `char`

**Returns:**
- 인자 `c`를 단일 문자로 포함하는 길이가 
 `1`인 새로 할당된 문자열

### valueOf

```java
public static String valueOf(int i)
```

**Parameters:**
- `i` - `int`

**Returns:**
- `int` 인자의 문자열 표현이 포함된 
 새로 할당된 문자열

**See Also:**
- ``Integer.toString(int, int)``

### valueOf

```java
public static String valueOf(long l)
```

**Parameters:**
- `l` - `long`

**Returns:**
- `long` 인자의 문자열 표현이 포함된
 새로 할당된 문자열

**See Also:**
- ``Long.toString(long)``

### valueOf

```java
public static String valueOf(float f)
```

**Parameters:**
- `f` - `float`

**Returns:**
- `float` 인자의 문자열 표현이 포함된 
 새로 할당된 문자열

**Since:**
- CLDC 1.1

**See Also:**
- ``Float.toString(float)``

### valueOf

```java
public static String valueOf(double d)
```

**Parameters:**
- `d` - `double`

**Returns:**
- `double` 인자의 문자열 표현이 포함된 
 새로 할당된 문자열

**Since:**
- CLDC 1.1

**See Also:**
- ``Double.toString(double)``

### intern

```java
public String intern()
```

**Returns:**
- 이 문자열과 내용이 같지만 고유 문자열 풀에서 
 가져온 문자열

**Since:**
- CLDC 1.1

## 메서드 상세

### length

```java
public int length()
```

**Returns:**
- 이 객체가 나타내는 문자 시퀀스의 
 길이

### charAt

```java
public char charAt(int index)
```

**Parameters:**
- `index` - 문자 색인

**Returns:**
- 이 문자열에서 지정된 색인의 문자. 
 첫 문자는 색인 `0`에 지정되어 있습니다.

**Throws:**
- `IndexOutOfBoundsException` - `index` 
 인자가 음수이거나 이 문자열의 길이보다 
 작지 않은 경우

### getChars

```java
public void getChars(int srcBegin,
                     int srcEnd,
                     char[] dst,
                     int dstBegin)
```

**Parameters:**
- `dstBegin` - 대상 배열의 시작 오프셋

**Throws:**
- `NullPointerException` - `dst`가 `null`인 경우

### getBytes

```java
public byte[] getBytes(String enc)
                throws UnsupportedEncodingException
```

**Parameters:**
- `enc` - 문자 인코딩 이름

**Returns:**
- 결과로 생성된 바이트 배열

**Throws:**
- `UnsupportedEncodingException` - 명명된 인코딩이 지원되지 않는 경우

**Since:**
- JDK1.1

### getBytes

```java
public byte[] getBytes()
```

**Returns:**
- 결과로 생성된 바이트 배열

**Since:**
- JDK1.1

### equals

```java
public boolean equals(Object anObject)
```

**Overrides:**
- `equals` in class `Object`

**Parameters:**
- `anObject` - 이 `String`과 비교할 
 객체

**Returns:**
- `String`이 같으면 `true`, 다르면 
 `false`

**See Also:**
- ``compareTo(java.lang.String)``, 
``equalsIgnoreCase(java.lang.String)``

### equalsIgnoreCase

```java
public boolean equalsIgnoreCase(String anotherString)
```

**Parameters:**
- `anotherString` - 이 `String`과 비교할 
 `String`

**Returns:**
- 인자가 `null`이 아니고 
 `String`이 같으면 대소문자와 상관없이 
 `true`, 그렇지 않으면 `false`

**See Also:**
- ``equals(Object)``, 
``Character.toLowerCase(char)``, 
``Character.toUpperCase(char)``

### compareTo

```java
public int compareTo(String anotherString)
```

**Parameters:**
- `anotherString` - 비교되는 `String`

**Returns:**
- 인자 문자열이 이 문자열과 같으면 값 
 `0`, 이 문자열이 
 사전적으로 문자열 인자보다 작으면 
 `0`보다 작은 값, 이 문자열이 문자열 인자보다 
 사전적으로 크면 `0`보다 큰 값

**Throws:**
- `NullPointerException` - `anotherString`이 
 `null`인 경우

### regionMatches

```java
public boolean regionMatches(boolean ignoreCase,
                             int toffset,
                             String other,
                             int ooffset,
                             int len)
```

**Parameters:**
- `len` - 비교할 문자 수

**Returns:**
- 이 문자열의 지정된 하위 영역이 문자열 인자의 
 지정된 하위 영역과 일치하면 `true`, 
 그렇지 않으면 `false`. 
 정확한 일치인지 또는 대소문자를 무시한 일치인지는 `ignoreCase` 
 인자에 따라 결정됩니다.

### startsWith

```java
public boolean startsWith(String prefix,
                          int toffset)
```

**Parameters:**
- `toffset` - 문자열에서 찾기 시작할 위치

**Returns:**
- 인자가 나타내는 문자 시퀀스가 색인 
 `toffset`에서 시작하는 이 객체의 하위 문자열 
 접두어이면 `true`, 
 그렇지 않으면 `false`. 
 `toffset`이 음수이거나 이 `String` 
 객체보다 크면 결과는 `false`가 됩니다. 
 그렇지 않으면 결과는 다음 표현식의 결과와 같습니다.
 
 this.subString(toffset).startsWith(prefix)

**Throws:**
- `NullPointerException` - `prefix`가 
 `null`인 경우

### startsWith

```java
public boolean startsWith(String prefix)
```

**Parameters:**
- `prefix` - 접두어

**Returns:**
- 인자가 나타내는 문자 시퀀스가 이 문자열이 나타내는 
 문자 시퀀스의 접두어이면 `true`, 
 그렇지 않으면 `false`. 인자가 빈 문자열이거나 
 ``equals(Object)`` 메소드로 확인하여 
 이 `String` 객체와 같은 경우에도 
 `true`가 
 반환됩니다.

**Throws:**
- `NullPointerException` - `prefix`가 
 `null`인 경우

**Since:**
- JDK1.0

### endsWith

```java
public boolean endsWith(String suffix)
```

**Parameters:**
- `suffix` - 접미어

**Returns:**
- 인자가 나타내는 문자 시퀀스가 이 객체가 나타내는 문자 시퀀스의 접미어이면 
 `true`, 그렇지 않으면 `false`. 
 인자가 빈 문자열이거나 ``equals(Object)`` 
 메소드로 확인하여 
 이 `String` 객체와 같은 경우에도 
 결과는 `true`가 됩니다.

**Throws:**
- `NullPointerException` - `suffix`가 
 `null`인 경우

### hashCode

```java
public int hashCode()
```

**Overrides:**
- `hashCode` in class `Object`

**Returns:**
- 이 객체의 해시 코드 값

**See Also:**
- ``Object.equals(java.lang.Object)``, 
``Hashtable``

### indexOf

```java
public int indexOf(int ch)
```

**Parameters:**
- `ch` - 문자

**Returns:**
- 이 객체가 나타내는 문자 시퀀스에서 문자의 
 첫 항목 색인 또는 해당 문자가 없는 경우 
 `-1`

### indexOf

```java
public int indexOf(int ch,
                   int fromIndex)
```

**Parameters:**
- `fromIndex` - 검색이 시작되는 색인

**Returns:**
- 이 객체가 나타내는 문자 시퀀스에서 
 `fromIndex`보다 크거나 같은, 
 문자의 첫 항목 색인 또는 
 해당 문자가 없는 경우 `-1`

### lastIndexOf

```java
public int lastIndexOf(int ch)
```

**Parameters:**
- `ch` - 문자

**Returns:**
- 이 객체가 나타내는 문자 시퀀스에서 
 문자의 마지막 항목 색인 
 또는 해당 문자가 없는 경우 `-1`

### lastIndexOf

```java
public int lastIndexOf(int ch,
                       int fromIndex)
```

**Parameters:**
- `fromIndex` - 검색이 시작되는 색인. 
 `fromIndex` 값에는 어떤 제한도 없습니다. 
 값이 문자열 길이보다 크거나 같으면 
 문자열 길이보다 하나 작은 값과 
 같은 경우처럼 전체 문자열이 검색될 수도 있습니다. 
 값이 음수이면 값이 -1인 경우와 
 마찬가지로 -1이 반환됩니다.

**Returns:**
- 이 객체가 나타내는 문자 시퀀스에서 
 `fromIndex`보다 작거나 같은, 
 문자의 마지막 항목 색인 또는 해당 문자가 이 위치 앞에 없는 경우 
 `-1`

### indexOf

```java
public int indexOf(String str)
```

**Parameters:**
- `str` - 모든 문자열

**Returns:**
- 문자열 인자가 이 객체 내의 하위 문자열이면 
 첫 하위 문자열의 첫 문자 색인이 반환됩니다. 
 하위 문자열이 아니면 
 `-1`이 반환됩니다.

**Throws:**
- `NullPointerException` - `str`이 
 `null`인 경우

### indexOf

```java
public int indexOf(String str,
                   int fromIndex)
```

**Parameters:**
- `fromIndex` - 검색이 시작되는 색인

**Returns:**
- 문자열 인자가 `fromIndex`보다 작지 않은 
 색인에서 시작하는 이 객체 내의 하위 문자열이면 
 첫 하위 문자열의 첫 문자 색인이 반환됩니다. 
 `fromIndex` 이상에서 
 시작하는 하위 문자열이 아니면 
 `-1`이 반환됩니다.

**Throws:**
- `NullPointerException` - `str`이 
 `null`인 경우

### substring

```java
public String substring(int beginIndex)
```

**Parameters:**
- `beginIndex` - 시작 색인(포함)

**Returns:**
- 지정된 하위 문자열

**Throws:**
- `IndexOutOfBoundsException` - `beginIndex`가 음수이거나 
 `String` 객체의 길이보다 큰 경우

### substring

```java
public String substring(int beginIndex,
                        int endIndex)
```

**Parameters:**
- `endIndex` - 끝 색인(포함하지 않음)

**Returns:**
- 지정된 하위 문자열

**Throws:**
- `IndexOutOfBoundsException` - `beginIndex`가 음수이거나, 
 `endIndex`가 `String` 
 객체의 길이보다 크거나 
 `beginIndex`가 
 `endIndex`보다 큰 경우

### concat

```java
public String concat(String str)
```

**Parameters:**
- `str` - 이 `String`의 끝에 연결되는 
 `String`

**Returns:**
- 이 객체의 문자 뒤에 문자열 인자의 
 문자를 연결한 문자열

**Throws:**
- `NullPointerException` - `str`이 
 `null`인 경우

### replace

```java
public String replace(char oldChar,
                      char newChar)
```

**Parameters:**
- `newChar` - 새 문자

**Returns:**
- 이 문자열의 모든 `oldChar` 항목을 
 `newChar`로 바꿔서 파생된 문자열

### toLowerCase

```java
public String toLowerCase()
```

**Returns:**
- 소문자로 변환된 String

**See Also:**
- ``Character.toLowerCase(char)``, 
``toUpperCase()``

### toUpperCase

```java
public String toUpperCase()
```

**Returns:**
- 대문자로 변환된 String

**See Also:**
- ``Character.toLowerCase(char)``, 
``toUpperCase()``

### trim

```java
public String trim()
```

**Returns:**
- 앞과 끝에서 공백을 제거한 이 문자열

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 문자열 자체

### toCharArray

```java
public char[] toCharArray()
```

**Returns:**
- 이 문자열의 길이와 같고 문자열이 나타내는 
 문자 시퀀스를 포함하도록 내용이 초기화된 
 새로 할당된 문자 배열

### valueOf

```java
public static String valueOf(Object obj)
```

**Parameters:**
- `obj` - `Object`

**Returns:**
- 인자가 `null`이면 `"null"`과 같은 문자열, 
 그렇지 않으면 `obj.toString()` 
 값이 반환됩니다.

**See Also:**
- ``Object.toString()``

### valueOf

```java
public static String valueOf(char[] data)
```

**Parameters:**
- `data` - `char` 배열

**Returns:**
- 문자 배열 인자에 포함된 문자 시퀀스를 
 나타내는 새로 할당된 문자열

### valueOf

```java
public static String valueOf(char[] data,
                             int offset,
                             int count)
```

**Parameters:**
- `count` - `String` 값의 길이

**Returns:**
- 문자 배열 인자의 하위 배열에 
 포함된 문자 시퀀스를 
 나타내는 새로 할당된 문자열

**Throws:**
- `IndexOutOfBoundsException` - `offset`이 음수 또는 `count`가 
 음수이거나 `offset+count`가 
 `data.length`보다 큰 경우

### valueOf

```java
public static String valueOf(boolean b)
```

**Parameters:**
- `b` - `boolean`

**Returns:**
- 인자가 `true`이면 
 `"true"`와 같은 문자열이 반환됩니다. 
 그렇지 않으면 `"false"`와 같은 문자열이 반환됩니다.

### valueOf

```java
public static String valueOf(char c)
```

**Parameters:**
- `c` - `char`

**Returns:**
- 인자 `c`를 단일 문자로 포함하는 길이가 
 `1`인 새로 할당된 문자열

### valueOf

```java
public static String valueOf(int i)
```

**Parameters:**
- `i` - `int`

**Returns:**
- `int` 인자의 문자열 표현이 포함된 
 새로 할당된 문자열

**See Also:**
- ``Integer.toString(int, int)``

### valueOf

```java
public static String valueOf(long l)
```

**Parameters:**
- `l` - `long`

**Returns:**
- `long` 인자의 문자열 표현이 포함된
 새로 할당된 문자열

**See Also:**
- ``Long.toString(long)``

### valueOf

```java
public static String valueOf(float f)
```

**Parameters:**
- `f` - `float`

**Returns:**
- `float` 인자의 문자열 표현이 포함된 
 새로 할당된 문자열

**Since:**
- CLDC 1.1

**See Also:**
- ``Float.toString(float)``

### valueOf

```java
public static String valueOf(double d)
```

**Parameters:**
- `d` - `double`

**Returns:**
- `double` 인자의 문자열 표현이 포함된 
 새로 할당된 문자열

**Since:**
- CLDC 1.1

**See Also:**
- ``Double.toString(double)``

### intern

```java
public String intern()
```

**Returns:**
- 이 문자열과 내용이 같지만 고유 문자열 풀에서 
 가져온 문자열

**Since:**
- CLDC 1.1
