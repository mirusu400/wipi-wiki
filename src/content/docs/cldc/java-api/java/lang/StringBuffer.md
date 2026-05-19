---
title: "Class StringBuffer"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.StringBuffer
```

## 설명

**extends Object:**

문자열 버퍼는 가변 문자 시퀀스를 구현합니다. 
 문자열 버퍼는 ``String``과 같지만 수정할 수 있습니다. 
 항상 특정 문자 시퀀스가 포함되지만 특정 메소드 호출을 통해 
 시퀀스 길이와 내용을 변경할 수 
 있습니다.

문자열 버퍼는 여러 스레드에서 안전하게 사용할 수 있습니다. 
 특정 인스턴스의 모든 작업이 관련된 개별 스레드의 
 메소드 호출 순서에 따라 순차적으로 
 발생하는 것처럼 동작하도록 
 필요할 경우 메소드가 동기화됩니다.

컴파일러는 문자열 버퍼를 사용하여 이진 문자열 연결 연산자 
 `+`를 구현합니다. 예를 들어, 다음과 같은 코드가 있습니다.

위의 코드는 다음 코드와 같은 값으로 컴파일됩니다.

이 코드는 초기에 비어 있는 새로운 문자열 버퍼를 만들고 
 각 피연산자의 문자열 표현을 순서대로 문자열 버퍼에 추가한 다음, 
 문자열 버퍼 내용을 문자열로 변환합니다. 이렇게 하면 
 많은 임시 문자열을 만들지 않아도 됩니다.

`StringBuffer`에서의 주요 작업은 
 `append` 메소드와 `insert` 메소드로, 
 모든 유형의 데이터를 받아들이도록 오버로드됩니다. 각 메소드는 
 지정된 데이터를 효과적으로 문자열로 변환한 다음, 
 해당 문자열의 문자를 문자열 버퍼에 추가 또는 삽입합니다. 
 `append` 메소드는 이러한 문자를 항상 버퍼 끝에 
 추가하고 `insert` 메소드는 지정된 위치에 
 문자를 추가합니다.

예를 들어, `z`가 현재 내용이 
 "`start`"인 문자열 버퍼 객체를 참조하면 
 메소드 호출 `z.append("le")`는 문자열 버퍼에 
 "`startle`"을 포함시키고 
 `z.insert(4, "le")`는 문자열 버퍼에 
 "`starlet`"를 포함시킵니다.

일반적으로 sb가 `StringBuffer`의 한 인스턴스를 참조하면 
 `sb.append(x)`는 `sb.insert(sb.length(), x)`와 
 동일한 기능을 합니다.

모든 문자열 버퍼에는 용량이 있습니다. 문자열 버퍼에 
 포함된 문자 시퀀스의 길이가 용량을 초과하지 않으면 
 새로운 내부 버퍼 배열을 할당할 필요가 없습니다. 
 내부 버퍼에 오버플로가 발생하면 자동으로 
 크기가 확대됩니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``ByteArrayOutputStream``, 
``String``

## 생성자 요약

- StringBuffer () 문자가 포함되어 있지 않으며 초기 용량이 16자인 
 문자열 버퍼를 구성합니다.
- StringBuffer (int length) 문자가 포함되어 있지 않으며 length 인자로 
 지정된 초기 용량을 가진 문자열 버퍼를 구성합니다.
- StringBuffer ( String str) 문자열 인자와 동일한 문자 시퀀스를 나타내도록 
 문자열 버퍼를 구성합니다.

## 메서드 요약

- `StringBuffer append (boolean b)` — boolean 인자의 문자열 표현을 이 문자열 버퍼에 추가합니다.
- `StringBuffer append (char c)` — char 인자의 문자열 표현을 이 문자열 버퍼에 추가합니다.
- `StringBuffer append (char[] str)` — char 배열 인자의 문자열 표현을 이 문자열 버퍼에 추가합니다.
- `StringBuffer append (char[] str, int offset, int len)` — char 배열 인자의 하위 배열의 문자열 표현을 이 문자열 버퍼에 추가합니다.
- `StringBuffer append (double d)` — double 인자의 문자열 표현을 이 문자열 버퍼에 추가합니다.
- `StringBuffer append (float f)` — float 인자의 문자열 표현을 이 문자열 버퍼에 추가합니다.
- `StringBuffer append (int i)` — int 인자의 문자열 표현을 이 문자열 버퍼에 추가합니다.
- `StringBuffer append (long l)` — long 인자의 문자열 표현을 이 문자열 버퍼에 추가합니다.
- `StringBuffer append ( Object obj)` — Object 인자의 문자열 표현을 이 문자열 버퍼에 추가합니다.
- `StringBuffer append ( String str)` — 문자열을 이 문자열 버퍼에 추가합니다.
- `int capacity ()` — 문자열 버퍼의 현재 용량을 반환합니다.
- `char charAt (int index)` — 현재 문자열 버퍼가 나타내는 시퀀스에서 index 인자로 지정된 문자가 반환됩니다.
- `StringBuffer delete (int start, int end)` — 이 StringBuffer 의 하위 문자열에서 문자를 제거합니다.
- `StringBuffer deleteCharAt (int index)` — 이 StringBuffer 에서 지정된 위치의 문자를 제거하여 StringBuffer 를 한 자 줄입니다.
- `void ensureCapacity (int minimumCapacity)` — 버퍼 용량이 최소한 지정된 최소값과 같은지 확인합니다.
- `void getChars (int srcBegin, int srcEnd, char[] dst, int dstBegin)` — 이 문자열 버퍼의 문자를 대상 문자 배열 dst 에 복사합니다.
- `StringBuffer insert (int offset, boolean b)` — boolean 인자의 문자열 표현을 이 문자열 버퍼에 삽입합니다.
- `StringBuffer insert (int offset, char c)` — char 인자의 문자열 표현을 이 문자열 버퍼에 삽입합니다.
- `StringBuffer insert (int offset, char[] str)` — char 배열 인자의 문자열 표현을 이 문자열 버퍼에 삽입합니다.
- `StringBuffer insert (int offset, double d)` — double 인자의 문자열 표현을 이 문자열 버퍼에 삽입합니다.
- `StringBuffer insert (int offset, float f)` — float 인자의 문자열 표현을 이 문자열 버퍼에 삽입합니다.
- `StringBuffer insert (int offset, int i)` — 두 번째 int 인자의 문자열 표현을 이 문자열 버퍼에 삽입합니다.
- `StringBuffer insert (int offset, long l)` — long 인자의 문자열 표현을 이 문자열 버퍼에 삽입합니다.
- `StringBuffer insert (int offset, Object obj)` — Object 인자의 문자열 표현을 이 문자열 버퍼에 삽입합니다.
- `StringBuffer insert (int offset, String str)` — 문자열을 이 문자열 버퍼에 삽입합니다.
- `int length ()` — 이 문자열 버퍼의 길이(문자 수)를 반환합니다.
- `StringBuffer reverse ()` — 이 문자열 버퍼에 포함된 문자 시퀀스가 역순 시퀀스로 바뀝니다.
- `void setCharAt (int index, char ch)` — 이 문자열 버퍼에서 지정된 색인의 문자는 ch 로 설정됩니다.
- `void setLength (int newLength)` — 이 문자열 버퍼의 길이를 설정합니다.
- `String toString ()` — 이 문자열 버퍼의 데이터를 나타내는 문자열로 변환합니다.

## 생성자 상세

### StringBuffer

```java
public StringBuffer()
```

- 문자가 포함되어 있지 않으며 초기 용량이 16자인 
 문자열 버퍼를 구성합니다.

### StringBuffer

```java
public StringBuffer(int length)
```

- 문자가 포함되어 있지 않으며 `length` 인자로 
 지정된 초기 용량을 가진 문자열 버퍼를 구성합니다.

**Parameters:**
- `length` - 초기 용량

**Throws:**
- `NegativeArraySizeException` - `length` 인자가 
 `0`보다 작은 경우

### StringBuffer

```java
public StringBuffer(String str)
```

- 문자열 인자와 동일한 문자 시퀀스를 나타내도록 
 문자열 버퍼를 구성합니다. 즉, 문자열 버퍼의 
 초기 내용은 인자 문자열의 복사본입니다. 
 문자열 버퍼의 초기 용량은 
 `16`에 문자열 인자의 길이를 더한 값입니다.

**Parameters:**
- `str` - 버퍼의 초기 내용

### length

```java
public int length()
```

**Returns:**
- 현재 이 문자열 버퍼가 
 나타내는 문자 시퀀스의 길이

### capacity

```java
public int capacity()
```

**Returns:**
- 이 문자열 버퍼의 현재 용량

### ensureCapacity

```java
public void ensureCapacity(int minimumCapacity)
```

**Parameters:**
- `minimumCapacity` - 최소 필요 용량

### setLength

```java
public void setLength(int newLength)
```

**Parameters:**
- `newLength` - 새로운 버퍼 길이

**Throws:**
- `IndexOutOfBoundsException` - `newLength` 인자가 
 음수인 경우

**See Also:**
- ``length()``

### charAt

```java
public char charAt(int index)
```

**Parameters:**
- `index` - 원하는 문자의 색인

**Returns:**
- 이 문자열 버퍼에서 지정된 색인의 문자

**Throws:**
- `IndexOutOfBoundsException` - `index`가 
 음수이거나 `length()`보다 크거나 같은 경우

**See Also:**
- ``length()``

### getChars

```java
public void getChars(int srcBegin,
                     int srcEnd,
                     char[] dst,
                     int dstBegin)
```

**Parameters:**
- `dstBegin` - `dst`의 오프셋

**Throws:**
- `IndexOutOfBoundsException` - 다음 중 최소 하나 이상이 true인 경우 
 
`srcBegin`이 음수입니다.
 `dstBegin`이 음수입니다.
 `srcBegin` 인자가 
 `srcEnd` 인자보다 큽니다.
 `srcEnd`가 이 
 문자열 버퍼의 현재 길이인 
 `this.length()`보다 큽니다.
 `dstBegin+srcEnd-srcBegin`이 
 `dst.length`보다 큽니다.

### setCharAt

```java
public void setCharAt(int index,
                      char ch)
```

**Parameters:**
- `ch` - 새 문자

**Throws:**
- `IndexOutOfBoundsException` - `index`가 
 음수이거나 `length()`보다 크거나 같은 경우

**See Also:**
- ``length()``

### append

```java
public StringBuffer append(Object obj)
```

**Parameters:**
- `obj` - `Object`

**Returns:**
- `StringBuffer` 객체 참조

**See Also:**
- ``String.valueOf(java.lang.Object)``, 
``append(java.lang.String)``

### append

```java
public StringBuffer append(String str)
```

**Parameters:**
- `str` - 문자열

**Returns:**
- `StringBuffer` 참조

### append

```java
public StringBuffer append(char[] str)
```

**Parameters:**
- `str` - 추가되는 문자

**Returns:**
- `StringBuffer` 객체 참조

### append

```java
public StringBuffer append(char[] str,
                           int offset,
                           int len)
```

**Parameters:**
- `len` - 추가할 문자 수

**Returns:**
- `StringBuffer` 객체 참조

### append

```java
public StringBuffer append(boolean b)
```

**Parameters:**
- `b` - `boolean`

**Returns:**
- `StringBuffer` 참조

**See Also:**
- ``String.valueOf(boolean)``, 
``append(java.lang.String)``

### append

```java
public StringBuffer append(char c)
```

**Parameters:**
- `c` - `char`

**Returns:**
- `StringBuffer` 객체 참조

### append

```java
public StringBuffer append(int i)
```

**Parameters:**
- `i` - `int`

**Returns:**
- `StringBuffer` 객체 참조

**See Also:**
- ``String.valueOf(int)``, 
``append(java.lang.String)``

### append

```java
public StringBuffer append(long l)
```

**Parameters:**
- `l` - `long`

**Returns:**
- `StringBuffer` 객체 참조

**See Also:**
- ``String.valueOf(long)``, 
``append(java.lang.String)``

### append

```java
public StringBuffer append(float f)
```

**Parameters:**
- `f` - `float`

**Returns:**
- `StringBuffer` 객체 참조

**Since:**
- CLDC 1.1

**See Also:**
- ``String.valueOf(float)``, 
``append(java.lang.String)``

### append

```java
public StringBuffer append(double d)
```

**Parameters:**
- `d` - `double`

**Returns:**
- `StringBuffer` 객체 참조

**Since:**
- CLDC 1.1

**See Also:**
- ``String.valueOf(double)``, 
``append(java.lang.String)``

### delete

```java
public StringBuffer delete(int start,
                           int end)
```

**Parameters:**
- `end` - 끝 색인(포함하지 않음)

**Returns:**
- 이 문자열 버퍼

**Throws:**
- `StringIndexOutOfBoundsException` - `start`가 
 음수이거나 `length()`보다 크거나 
 `end`보다 큰 경우

**Since:**
- JDK1.2

### deleteCharAt

```java
public StringBuffer deleteCharAt(int index)
```

**Parameters:**
- `index` - 제거할 문자의 색인

**Returns:**
- 이 문자열 버퍼

**Throws:**
- `StringIndexOutOfBoundsException` - `index`가 
 음수이거나 `length()`보다 
 크거나 같은 경우

**Since:**
- JDK1.2

### insert

```java
public StringBuffer insert(int offset,
                           Object obj)
```

**Parameters:**
- `obj` - `Object`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``String.valueOf(java.lang.Object)``, 
``insert(int, java.lang.String)``, 
``length()``

### insert

```java
public StringBuffer insert(int offset,
                           String str)
```

**Parameters:**
- `str` - 문자열

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``length()``

### insert

```java
public StringBuffer insert(int offset,
                           char[] str)
```

**Parameters:**
- `str` - 문자 배열

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

### insert

```java
public StringBuffer insert(int offset,
                           boolean b)
```

**Parameters:**
- `b` - `boolean`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``String.valueOf(boolean)``, 
``insert(int, java.lang.String)``, 
``length()``

### insert

```java
public StringBuffer insert(int offset,
                           char c)
```

**Parameters:**
- `c` - `char`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `IndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``length()``

### insert

```java
public StringBuffer insert(int offset,
                           int i)
```

**Parameters:**
- `i` - `int`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``String.valueOf(int)``, 
``insert(int, java.lang.String)``, 
``length()``

### insert

```java
public StringBuffer insert(int offset,
                           long l)
```

**Parameters:**
- `l` - `long`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``String.valueOf(long)``, 
``insert(int, java.lang.String)``, 
``length()``

### insert

```java
public StringBuffer insert(int offset,
                           float f)
```

**Parameters:**
- `f` - `float`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``String.valueOf(float)``, 
``insert(int, java.lang.String)``, 
``length()``

### insert

```java
public StringBuffer insert(int offset,
                           double d)
```

**Parameters:**
- `d` - `double`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``String.valueOf(double)``, 
``insert(int, java.lang.String)``, 
``length()``

### reverse

```java
public StringBuffer reverse()
```

**Returns:**
- `StringBuffer` 객체 참조

**Since:**
- JDK1.0.2

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 문자열 버퍼의 문자열 표현

## 메서드 상세

### length

```java
public int length()
```

**Returns:**
- 현재 이 문자열 버퍼가 
 나타내는 문자 시퀀스의 길이

### capacity

```java
public int capacity()
```

**Returns:**
- 이 문자열 버퍼의 현재 용량

### ensureCapacity

```java
public void ensureCapacity(int minimumCapacity)
```

**Parameters:**
- `minimumCapacity` - 최소 필요 용량

### setLength

```java
public void setLength(int newLength)
```

**Parameters:**
- `newLength` - 새로운 버퍼 길이

**Throws:**
- `IndexOutOfBoundsException` - `newLength` 인자가 
 음수인 경우

**See Also:**
- ``length()``

### charAt

```java
public char charAt(int index)
```

**Parameters:**
- `index` - 원하는 문자의 색인

**Returns:**
- 이 문자열 버퍼에서 지정된 색인의 문자

**Throws:**
- `IndexOutOfBoundsException` - `index`가 
 음수이거나 `length()`보다 크거나 같은 경우

**See Also:**
- ``length()``

### getChars

```java
public void getChars(int srcBegin,
                     int srcEnd,
                     char[] dst,
                     int dstBegin)
```

**Parameters:**
- `dstBegin` - `dst`의 오프셋

**Throws:**
- `IndexOutOfBoundsException` - 다음 중 최소 하나 이상이 true인 경우 
 
`srcBegin`이 음수입니다.
 `dstBegin`이 음수입니다.
 `srcBegin` 인자가 
 `srcEnd` 인자보다 큽니다.
 `srcEnd`가 이 
 문자열 버퍼의 현재 길이인 
 `this.length()`보다 큽니다.
 `dstBegin+srcEnd-srcBegin`이 
 `dst.length`보다 큽니다.

### setCharAt

```java
public void setCharAt(int index,
                      char ch)
```

**Parameters:**
- `ch` - 새 문자

**Throws:**
- `IndexOutOfBoundsException` - `index`가 
 음수이거나 `length()`보다 크거나 같은 경우

**See Also:**
- ``length()``

### append

```java
public StringBuffer append(Object obj)
```

**Parameters:**
- `obj` - `Object`

**Returns:**
- `StringBuffer` 객체 참조

**See Also:**
- ``String.valueOf(java.lang.Object)``, 
``append(java.lang.String)``

### append

```java
public StringBuffer append(String str)
```

**Parameters:**
- `str` - 문자열

**Returns:**
- `StringBuffer` 참조

### append

```java
public StringBuffer append(char[] str)
```

**Parameters:**
- `str` - 추가되는 문자

**Returns:**
- `StringBuffer` 객체 참조

### append

```java
public StringBuffer append(char[] str,
                           int offset,
                           int len)
```

**Parameters:**
- `len` - 추가할 문자 수

**Returns:**
- `StringBuffer` 객체 참조

### append

```java
public StringBuffer append(boolean b)
```

**Parameters:**
- `b` - `boolean`

**Returns:**
- `StringBuffer` 참조

**See Also:**
- ``String.valueOf(boolean)``, 
``append(java.lang.String)``

### append

```java
public StringBuffer append(char c)
```

**Parameters:**
- `c` - `char`

**Returns:**
- `StringBuffer` 객체 참조

### append

```java
public StringBuffer append(int i)
```

**Parameters:**
- `i` - `int`

**Returns:**
- `StringBuffer` 객체 참조

**See Also:**
- ``String.valueOf(int)``, 
``append(java.lang.String)``

### append

```java
public StringBuffer append(long l)
```

**Parameters:**
- `l` - `long`

**Returns:**
- `StringBuffer` 객체 참조

**See Also:**
- ``String.valueOf(long)``, 
``append(java.lang.String)``

### append

```java
public StringBuffer append(float f)
```

**Parameters:**
- `f` - `float`

**Returns:**
- `StringBuffer` 객체 참조

**Since:**
- CLDC 1.1

**See Also:**
- ``String.valueOf(float)``, 
``append(java.lang.String)``

### append

```java
public StringBuffer append(double d)
```

**Parameters:**
- `d` - `double`

**Returns:**
- `StringBuffer` 객체 참조

**Since:**
- CLDC 1.1

**See Also:**
- ``String.valueOf(double)``, 
``append(java.lang.String)``

### delete

```java
public StringBuffer delete(int start,
                           int end)
```

**Parameters:**
- `end` - 끝 색인(포함하지 않음)

**Returns:**
- 이 문자열 버퍼

**Throws:**
- `StringIndexOutOfBoundsException` - `start`가 
 음수이거나 `length()`보다 크거나 
 `end`보다 큰 경우

**Since:**
- JDK1.2

### deleteCharAt

```java
public StringBuffer deleteCharAt(int index)
```

**Parameters:**
- `index` - 제거할 문자의 색인

**Returns:**
- 이 문자열 버퍼

**Throws:**
- `StringIndexOutOfBoundsException` - `index`가 
 음수이거나 `length()`보다 
 크거나 같은 경우

**Since:**
- JDK1.2

### insert

```java
public StringBuffer insert(int offset,
                           Object obj)
```

**Parameters:**
- `obj` - `Object`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``String.valueOf(java.lang.Object)``, 
``insert(int, java.lang.String)``, 
``length()``

### insert

```java
public StringBuffer insert(int offset,
                           String str)
```

**Parameters:**
- `str` - 문자열

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``length()``

### insert

```java
public StringBuffer insert(int offset,
                           char[] str)
```

**Parameters:**
- `str` - 문자 배열

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

### insert

```java
public StringBuffer insert(int offset,
                           boolean b)
```

**Parameters:**
- `b` - `boolean`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``String.valueOf(boolean)``, 
``insert(int, java.lang.String)``, 
``length()``

### insert

```java
public StringBuffer insert(int offset,
                           char c)
```

**Parameters:**
- `c` - `char`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `IndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``length()``

### insert

```java
public StringBuffer insert(int offset,
                           int i)
```

**Parameters:**
- `i` - `int`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``String.valueOf(int)``, 
``insert(int, java.lang.String)``, 
``length()``

### insert

```java
public StringBuffer insert(int offset,
                           long l)
```

**Parameters:**
- `l` - `long`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**See Also:**
- ``String.valueOf(long)``, 
``insert(int, java.lang.String)``, 
``length()``

### insert

```java
public StringBuffer insert(int offset,
                           float f)
```

**Parameters:**
- `f` - `float`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``String.valueOf(float)``, 
``insert(int, java.lang.String)``, 
``length()``

### insert

```java
public StringBuffer insert(int offset,
                           double d)
```

**Parameters:**
- `d` - `double`

**Returns:**
- `StringBuffer` 객체 참조

**Throws:**
- `StringIndexOutOfBoundsException` - 오프셋이 유효하지 않은 경우

**Since:**
- CLDC 1.1

**See Also:**
- ``String.valueOf(double)``, 
``insert(int, java.lang.String)``, 
``length()``

### reverse

```java
public StringBuffer reverse()
```

**Returns:**
- `StringBuffer` 객체 참조

**Since:**
- JDK1.0.2

### toString

```java
public String toString()
```

**Overrides:**
- `toString` in class `Object`

**Returns:**
- 문자열 버퍼의 문자열 표현
