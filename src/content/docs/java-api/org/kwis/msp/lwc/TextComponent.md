---
title: "Class TextComponent"
---

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.TextComponent
```

## 설명

**Direct Known Subclasses:**
- `TextBoxComponent`, `TextFieldComponent`

**extends Component:**

텍스트 출력 및 입력 수정 삭제를 위한 추상 클래스입니다.

이 클래스를 상속받아 구현된 클래스는 ``TextBoxComponent``와
 ``TextFieldComponent``입니다.

와

에서

키 입력이 있을 경우 전체 화면으로
 문자 편집이 가능한 에디터가 생성됩니다. 이 에디터에서 편집을 마친경우

키를 입력을 하여 이전 화면으로 돌아갈
 수 있으며, 이전 화면의 문자 데이타는 전체 화면에서 편집하던 문자 데이타로 변경됩니다.

에서는 3가지 종류의 입력 제한자를 제공하고 있습니다.

- *CONSTRAINT_NUMBER*는 '-',' '와 숫자입력만을 허용하는 입력제한자입니다.
- *CONSTRAINT_PASSWORD*는 암호입력을 위한 입력 형태로 내부적으로
 사용되는 문자열은 숫자만을 허용합니다. 이 경우 화면에 출력되는 형태는 '*'입니다.
- *CONSTRAINT_ANY*는 모든 문자열을 입력할 수 있는 입력 제한자 입니다. *

위의 입력 제한자외의 값을 지정할 수 없으며, 다른 값을 지정한 경우

이 발생합니다.

기본적으로 최대 입력 가능한 문자열에 대한 제한은 하지 않으며,
 ``setMaxLength(int maxLen)``를 통해서 최대 입력가능한 문자수를 제한 할 수
 있습니다.

문자 입력 처리를 위한 ``InputMethodListener``와
 ``ActionListener``를 구현을 내부 클래스를 포함하고 있으며, 각 내부 클래스에서는
 현재 입력 모드에 따라 입력 받은 문자를 관리하고 입력 화면을 전체 화면 사이즈로 전환하거나
 원래 화면, 즉 `TextFieldComponent`,`TextBoxComponent`로
 복원하는 일을 담당하고 있습니다.

**Since:**
- qtp 1.0

**See Also:**
- ``TextFieldComponent``, 
``TextBoxComponent``

## 필드 요약

- `protected  int charCount` — 문자의 수
- `protected  org.kwis.msp.lwc.ConstraintChecker constChecker` — 문자 데이타가 지정한 입력 제한자에 맞는 데이타인지를 검사
- `protected  int constraint` — 입력 형태지정
- `static int CONSTRAINT_ANY` — 사용자가 입력 가능한 문자에 제한이 없는 경우에 사용되는 입력제한자.
- `static int CONSTRAINT_EMAILADDRESS` — 사용자가 입력 가능한 문자를 이메일 주소로 로 제한할 경우에 사용하는 입력제한자.
- `static int CONSTRAINT_NUMBER` — 사용자가 입력 가능한 문자를 ' '와 '-',숫자로만 제한할 경우에 사용하는 입력제한자.
- `static int CONSTRAINT_PASSWORD` — 사용자가 입력 가능한 문자를 패스워드로 제한할 경우에 사용하는 입력제한자.
- `static int CONSTRAINT_PHONENUMBER` — 사용자가 입력 가능한 문자를 전화번호로 제한할 경우에 사용하는 입력제한자.
- `static int CONSTRAINT_URL` — 사용자가 입력 가능한 문자를 URL로 제한할 경우에 사용하는 입력제한자.
- `protected Display display` — 카드 사용을 위한 Display객체
- `protected Font f` — TextComponent 에서 사용하는 폰트.
- `protected InputMethodHandler imHandler` — 키 입력에 다른 문자 데이타 처리를 위해 사용되는 입력 메소드핸들러.
- `protected  int iMode` — 현재 사용중인 문자열 입력모드
- `protected  int m_cPos` — 현재 문자 데이타의 위치
- `protected  char[] m_td` — 문자 데이타
- `protected  int maxLength` — 입력 가능한 최대 문자 길이 -1값인경우 최대 문자 길이 제한 없음.
- `TextComponent.ModeViewer modeViewer` — 현재의 입력 모드 상황을 보여주는 카드

## 메서드 요약

- `void delete (int index, int len)` — 현재 화면에 보여지고 있는 문자데이타의 index 위치에서 부터 len 길이만큼 데이타를 삭제합니다.
- `void focusNotify (boolean b)` — 포커스를 받게 되면 불려집니다.
- `int getConstraint ()` — 현재 지정된 문자 데이타 입력 제한자를 리턴합니다.
- `Font getFont ()` — 폰트를 얻어옵니다.
- `int getMaxLength ()` — 현재 설정된 최대 입력가능한 문자수를 리턴합니다.
- `String getString ()` — 현재의 문자 데이타를 리턴합니다.
- `void insert (char[] data, int offset, int len, int index)` — 현재 화면에 출력된 문자 데이타에서 인자로 주어진 문자 데이타를 index 위치에 추가합니다.
- `boolean keyNotify (int type, int keyC)` — 키 입력을 받으면 호출됩니다.
- `void setFont ( Font f)` — 폰트를 지정합니다.
- `void setMaxLength (int maxLen)` — 입력가능한 최대문자수를 지정합니다.
- `void setString ( String data)` — 문자 데이타를 지정합니다.
- `protected  void showNotify (boolean bShow)` — 화면의 내용이 보이면 호출됩니다.

## 필드 상세

### CONSTRAINT_ANY

```java
public static final int CONSTRAINT_ANY
```

- 사용자가 입력 가능한 문자에 제한이 없는 경우에 사용되는 입력제한자.
 이 값은 사용자가 특별히 사용문자에 대한 제한을 두지 않은 경우로 특정 입력 제한자를
 지정하지 않으면 기본적 사용됩니다.
 CONSTRAINT_ANY에 할당된 값은 '0'.

### CONSTRAINT_NUMBER

```java
public static final int CONSTRAINT_NUMBER
```

- 사용자가 입력 가능한 문자를 ' '와 '-',숫자로만 제한할 경우에 사용하는 입력제한자.
 CONSTRAINT_NUMBER에 할당된 값은 '1'.

### CONSTRAINT_PASSWORD

```java
public static final int CONSTRAINT_PASSWORD
```

- 사용자가 입력 가능한 문자를 패스워드로 제한할 경우에 사용하는 입력제한자.
 이 경우 내부적으로 사용되는 문자열은 숫자이며, 화면에 출력되는 형태는 '*'입니다
 CONSTRAINT_PASSWORD에 할당된 값은 '2'.

### CONSTRAINT_EMAILADDRESS

```java
public static final int CONSTRAINT_EMAILADDRESS
```

- 사용자가 입력 가능한 문자를 이메일 주소로 로 제한할 경우에 사용하는 입력제한자.
 이 경우 내부적으로 사용되는 문자열은 영문대,소문자와 숫자,심볼입니다.
 CONSTRAINT_EMAILADDRESS 할당된 값은 '3'.

### CONSTRAINT_URL

```java
public static final int CONSTRAINT_URL
```

- 사용자가 입력 가능한 문자를 URL로 제한할 경우에 사용하는 입력제한자.
 이 경우 내부적으로 사용되는 문자열은 영문대,소문자와 숫자,심볼입니다.
 CONSTRAINT_URL 할당된 값은 '4'.

### CONSTRAINT_PHONENUMBER

```java
public static final int CONSTRAINT_PHONENUMBER
```

- 사용자가 입력 가능한 문자를 전화번호로 제한할 경우에 사용하는 입력제한자.
 이 경우 내부적으로 사용되는 문자열은 숫자입니다
 CONSTRAINT_PHONENUMBER 할당된 값은 '5'.

### imHandler

```java
protected InputMethodHandler imHandler
```

- 키 입력에 다른 문자 데이타 처리를 위해 사용되는 입력 메소드핸들러.

### m_cPos

```java
protected int m_cPos
```

- 현재 문자 데이타의 위치

### charCount

```java
protected int charCount
```

- 문자의 수

### constraint

```java
protected int constraint
```

- 입력 형태지정

### m_td

```java
protected char[] m_td
```

- 문자 데이타

### iMode

```java
protected int iMode
```

- 현재 사용중인 문자열 입력모드

### display

```java
protected Display display
```

- 카드 사용을 위한 Display객체

### modeViewer

```java
public TextComponent.ModeViewer modeViewer
```

- 현재의 입력 모드 상황을 보여주는 카드

### maxLength

```java
protected int maxLength
```

- 입력 가능한 최대 문자 길이
 -1값인경우 최대 문자 길이 제한 없음.

### constChecker

```java
protected org.kwis.msp.lwc.ConstraintChecker constChecker
```

- 문자 데이타가 지정한 입력 제한자에 맞는 데이타인지를 검사

### f

```java
protected Font f
```

TextCompHR> constraint protected int constraint
