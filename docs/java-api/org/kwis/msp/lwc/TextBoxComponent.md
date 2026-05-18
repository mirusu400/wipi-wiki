# Class TextBoxComponent

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.TextComponent
              |
              +--org.kwis.msp.lwc.TextBoxComponent
```

## 설명

**extends TextComponent:**

`TextBoxComponentTextComponent`를 상속한 클래스로
 정해진 넓이에 맞도록 문자를 편집 할 수 있습니다.
 이 컴포넌트의 넓이는 이 컴포넌트를 추가한 `ContainerComponent`의 넓이와
 같고 , 높이는 현재 화면에 출력된 문자 데이타에 맞도록 자동으로 변경됩니다.

`전체 화면을 사용하여 문자 편집`을
 할 수 있으며, 특정 문자열만을 입력하도록 입력제한을 할 수 있습니다.
 `TextComoponent`에서 정의된
 `입력 제한자`에 대한 내용을 참고하세요.

기본적으로 최대 입력 가능한 문자열에 대한 제한은 하지 않으며,
 ``setMaxLength(int maxLen)``를 통해서 최대 입력가능한 문자수를 제한 할 수
 있습니다.

**See Also:**
- ``TextComponent``, 
``TextFieldComponent``

Inner classes inherited from class org.kwis.msp.lwc. TextComponent TextComponent.ModeViewer

Field Summary protected  boolean isWide 전체 화면을 사용한 문자 입력 상태.

Fields inherited from class org.kwis.msp.lwc. TextComponent charCount , constChecker , constraint , CONSTRAINT_ANY , CONSTRAINT_EMAILADDRESS , CONSTRAINT_NUMBER , CONSTRAINT_PASSWORD , CONSTRAINT_PHONENUMBER , CONSTRAINT_URL , display , f , imHandler , iMode , m_cPos , m_td , maxLength , modeViewer

Fields inherited from class org.kwis.msp.lwc. Component bg , evtListener , evtListenerObj , fg , FOCUS_NOTIFY , h , HAS_FOCUS_MASK , INPUT_MASK , KEY_NOTIFY , KEY_PRESSED , KEY_RELEASED , KEY_REPEATED , KEY_TYPED , LAYOUT_BOTTOM , LAYOUT_HCENTER , LAYOUT_LEFT , LAYOUT_RIGHT , LAYOUT_TOP , LAYOUT_VCENTER , mask , parent , POINT_DRAGGED , POINT_PRESSED , POINT_RELEASED , POINTER_NOTIFY , POS_MASK , PREFER_SIZE_MASK , prefH , prefW , SHOW_NOTIFY , SIZE_MASK , VALID_MASK , w , x , y

Constructor Summary TextBoxComponent ( String data,
 int constraints) 주어진 문자 데이타와 입력 제한자로 TextComponent 의 인스턴스를
 생성합니다. TextBoxComponent ( String data,
 int constraints,
 int h) 주어진 문자 데이타와 입력 제한자,컴포넌트의 높이값으로 TextComponent 의 인스턴스를 생성합니다.

Method Summary void configure (int x,
 int y,
 int w,
 int h,
 int mask) 컴포넌트의 위치나 크기를 변경합니다. void delete (int index,
 int len) 현재 화면에 보여지고 있는 문자데이타의 index 위치에서 부터 len 길이만큼 데이타를 삭제합니다. void focusNotify (boolean b) 포커스를 받게 되면 불려집니다. int getPreferredHeight () 컴포넌트의 적절한 높이를 결정합니다. int getPreferredHeight (int w) 컴포넌트의 적절한 높이를 결정합니다. int getPreferredWidth () 컴포넌트의 적절한 폭을 결정합니다. void insert (char[] data,
 int offset,
 int len,
 int index) 현재 화면에 출력된 문자 데이타에서 인자로 주어진 문자 데이타를 index 위치에 추가합니다. boolean keyNotify (int type,
 int key) 키 입력을 받으면 호출됩니다. void paintContent ( Graphics g) 내부를 칠합니다. void setFont ( Font f) 폰트를 지정합니다. void setMaxLength (int maxLen) 입력가능한 최대문자수를 지정합니다. void setString ( String data) 문자 데이타를 지정합니다.

Methods inherited from class org.kwis.msp.lwc. TextComponent getConstraint , getFont , getMaxLength , getString , showNotify

Methods inherited from class org.kwis.msp.lwc. Component calcPreferredSize , canHandleInput , getBackground , getCard , getForeground , getHeight , getWidth , getX , getXOnScreen , getY , getYOnScreen , hasFocus , invalidate , isShown , isValid , layout , pointerNotify , processEvent , repaint , repaint , serviceRepaints , setBackground , setEventListener , setFocus , setForeground , toString , validate

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , wait , wait , wait

Field Detail

### isWide

- 전체 화면을 사용한 문자 입력 상태. `true`면 전체 화면을 사용한
 문자 입력상태입니다. 기본값은 `false`

Constructor Detail

### TextBoxComponent

- 주어진 문자 데이타와 입력 제한자로 `TextComponent`의 인스턴스를
 생성합니다. 문자 데이타는 `null`값을 가질 수 있습니다.
 

지정한 입력 제한자가 ``TextComponent.CONSTRAINT_NUMBER``,
 ``TextComponent.CONSTRAINT_PASSWORD``,

## 필드 요약

- `protected  boolean isWide` — 전체 화면을 사용한 문자 입력 상태.

## 생성자 요약

- TextBoxComponent ( String data,
 int constraints) 주어진 문자 데이타와 입력 제한자로 TextComponent 의 인스턴스를
 생성합니다.
- TextBoxComponent ( String data,
 int constraints,
 int h) 주어진 문자 데이타와 입력 제한자,컴포넌트의 높이값으로 TextComponent 의 인스턴스를 생성합니다.

## 메서드 요약

- `void configure (int x, int y, int w, int h, int mask)` — 컴포넌트의 위치나 크기를 변경합니다.
- `void delete (int index, int len)` — 현재 화면에 보여지고 있는 문자데이타의 index 위치에서 부터 len 길이만큼 데이타를 삭제합니다.
- `void focusNotify (boolean b)` — 포커스를 받게 되면 불려집니다.
- `int getPreferredHeight ()` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredHeight (int w)` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredWidth ()` — 컴포넌트의 적절한 폭을 결정합니다.
- `void insert (char[] data, int offset, int len, int index)` — 현재 화면에 출력된 문자 데이타에서 인자로 주어진 문자 데이타를 index 위치에 추가합니다.
- `boolean keyNotify (int type, int key)` — 키 입력을 받으면 호출됩니다.
- `void paintContent ( Graphics g)` — 내부를 칠합니다.
- `void setFont ( Font f)` — 폰트를 지정합니다.
- `void setMaxLength (int maxLen)` — 입력가능한 최대문자수를 지정합니다.
- `void setString ( String data)` — 문자 데이타를 지정합니다.

## 필드 상세

### isWide

```java
protected boolean isWide
```

- 전체 화면을 사용한 문자 입력 상태. `true`면 전체 화면을 사용한
 문자 입력상태입니다. 기본값은 `false`

### TextBoxComponent

```java
public TextBoxComponent(String data,
                        int constraints)
```

- 주어진 문자 데이타와 입력 제한자로 `TextComponent`의 인스턴스를
 생성합니다. 문자 데이타는 `null`값을 가질 수 있습니다.
 

지정한 입력 제한자가 ``TextComponent.CONSTRAINT_NUMBER``,
 ``TextComponent.CONSTRAINT_PASSWORD``,

## 생성자 상세

### TextBoxComponent

```java
public TextBoxComponent(String data,
                        int constraints)
```

- 주어진 문자 데이타와 입력 제한자로 `TextComponent`의 인스턴스를
 생성합니다. 문자 데이타는 `null`값을 가질 수 있습니다.
 

지정한 입력 제한자가 ``TextComponent.CONSTRAINT_NUMBER``,
 ``TextComponent.CONSTRAINT_PASSWORD``,
