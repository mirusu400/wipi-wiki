# Class InputMethodHandler

`package org.kwis.msp.lcdui`

```
java.lang.Object
  |
  +--org.kwis.msp.lcdui.InputMethodHandler
```

## 설명

**extends Object:**

`InputMethodHandler`는 사용자 키 입력를 오토마타에게 전달하는 
 일을 담당합니다.

사용자의 키 입력을 처리하는 메소드는 `#notifyKeyInput(int keyCode)`입니다.
 따라서 이 메소드를 호출하여 현재 입력된 키 값을 넘겨줘야 합니다.
 또한 키 입력에 따라 처리된 문자를 전달받기 위해서 반드시 구현된 특정
 `InputMethodListener`를 지정해야 합니다.
 지정된 `InputMethodListener`가 존재하지 않은 경우
 ``notifyKeyInput(int, int)``에서 `false`를 리턴하고 아무런 일을 하지
 않습니다. `InputMethodListener`는 ``setInputMethodListener(org.kwis.msp.lcdui.InputMethodListener)``를
 통해 지정할 수 있습니다.

## 생성자 요약

- InputMethodHandler (int constraint) 주어진 입력제한자로 InputMethodHandler 의
 인스턴스를 생성합니다.

## 메서드 요약

- `void changeCurrentModeToNext ()` — 현재 지정된 constraint에 따라 현재 입력모드를 기준으로 다음 입력 모드를 계산하여 현재 입력모드를 계산된 다음 입력모드로 변경합니다.
- `int getCurrentInputMode ()` — 현재의 입력모드를 얻어옵니다.
- `int getCurrentMode ()` — 현재 입력모드를 얻어옵니다.
- `String getCurrentModeCode ()` — 현재 입력모드에 해당하는 표준언어코드를 얻어옵니다.
- `void hideSymbolCard ()` — 현재 화면에서 CandidateWindow 를 제거합니다.
- `boolean notifyKeyInput (int keyCode, int type)` — InputMethodHandler 에서 키입력을 처리해야하는 경우 호출되는 메소드입니다.
- `boolean setCurrentMode (int mode)` — 주어진 모드값으로 현재 입력모드를 지정합니다.
- `void setInputMethodListener ( InputMethodListener imListener)` — InputMethodHandler 에서 키 입력에 따라 처리한 문자를 전달할 InputMethodListener 를 지정합니다.
- `void setSymbolPosition (int x, int y, int w, int h)` — InputMethodHandler 의 현재 입력 모드가 IM_SYMBOL 경우 화면에 특수문자카드를 출력할 위치와 넓이, 높이를 설정합니다.

## 생성자 상세

### InputMethodHandler

```java
public InputMethodHandler(int constraint)
```

**Parameters:**
- `constraint` - 입력 제한자

### getCurrentModeCode

```java
public String getCurrentModeCode()
```

**Returns:**
- 입력모드에 해당하는 언어코드.

### notifyKeyInput

```java
public final boolean notifyKeyInput(int keyCode,
                                    int type)
```

**Parameters:**
- `type` - 키의 타입(EventQueue.KEY_PRESSED, EventQueue.KEY_RELEASED)

**Returns:**
- 키 입력에 따른 문자 처리가 이루어진 경우 `true`,
 그 외의 경우`false` 리턴.

### getCurrentInputMode

```java
public int getCurrentInputMode()
```

**Returns:**
- 현재 입력 모드

**See Also:**
- `#setInputMode(int inputMode)`

### setInputMethodListener

```java
public void setInputMethodListener(InputMethodListener imListener)
```

**Parameters:**
- `imListener` - `InputMethodListener` 혹은 `null`

### changeCurrentModeToNext

```java
public void changeCurrentModeToNext()
```

- 현재 지정된 constraint에 따라 현재 입력모드를 
 기준으로 다음 입력 모드를 계산하여 현재 입력모드를
 계산된 다음 입력모드로 변경합니다.

### getCurrentMode

```java
public int getCurrentMode()
```

- 현재 입력모드를 얻어옵니다.

### setCurrentMode

```java
public boolean setCurrentMode(int mode)
```

**Parameters:**
- `mode` - 새로지정할 입력모드값

### hideSymbolCard

```java
public void hideSymbolCard()
```

- 현재 화면에서 `CandidateWindow`를 제거합니다.

### setSymbolPosition

```java
public void setSymbolPosition(int x,
                              int y,
                              int w,
                              int h)
```

**Parameters:**
- `h` - height값.

**Throws:**
- `IllegalArgumentException` - `w,h`값이 '0'이하값인 경우

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 메서드 상세

### getCurrentModeCode

```java
public String getCurrentModeCode()
```

**Returns:**
- 입력모드에 해당하는 언어코드.

### notifyKeyInput

```java
public final boolean notifyKeyInput(int keyCode,
                                    int type)
```

**Parameters:**
- `type` - 키의 타입(EventQueue.KEY_PRESSED, EventQueue.KEY_RELEASED)

**Returns:**
- 키 입력에 따른 문자 처리가 이루어진 경우 `true`,
 그 외의 경우`false` 리턴.

### getCurrentInputMode

```java
public int getCurrentInputMode()
```

**Returns:**
- 현재 입력 모드

**See Also:**
- `#setInputMode(int inputMode)`

### setInputMethodListener

```java
public void setInputMethodListener(InputMethodListener imListener)
```

**Parameters:**
- `imListener` - `InputMethodListener` 혹은 `null`

### changeCurrentModeToNext

```java
public void changeCurrentModeToNext()
```

- 현재 지정된 constraint에 따라 현재 입력모드를 
 기준으로 다음 입력 모드를 계산하여 현재 입력모드를
 계산된 다음 입력모드로 변경합니다.

### getCurrentMode

```java
public int getCurrentMode()
```

- 현재 입력모드를 얻어옵니다.

### setCurrentMode

```java
public boolean setCurrentMode(int mode)
```

**Parameters:**
- `mode` - 새로지정할 입력모드값

### hideSymbolCard

```java
public void hideSymbolCard()
```

- 현재 화면에서 `CandidateWindow`를 제거합니다.

### setSymbolPosition

```java
public void setSymbolPosition(int x,
                              int y,
                              int w,
                              int h)
```

**Parameters:**
- `h` - height값.

**Throws:**
- `IllegalArgumentException` - `w,h`값이 '0'이하값인 경우

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
