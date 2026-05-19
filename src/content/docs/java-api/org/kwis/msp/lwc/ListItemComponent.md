---
title: "Class ListItemComponent"
---

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.LabelComponent
              |
              +--org.kwis.msp.lwc.ListItemComponent
```

## 설명

**extends LabelComponent:**

``ListComponent``에 추가되어 사용되는 `ListItemComponent`입니다.
 이 컴포넌트는 `LabelComponent`를 상속하여 구현된 클래스로 기본 기능은
 `LabelComponent`와 유사합니다. 반면 이 컴포넌트는 `INPUT_MASK`
 를 가지고 있으므로 포커스와 입력을 받을 수 있습니다.

**See Also:**
- ``ListComponent``

Fields inherited from class org.kwis.msp.lwc. LabelComponent layout , m_ft , m_image , m_str

Fields inherited from class org.kwis.msp.lwc. Component bg , evtListener , evtListenerObj , fg , FOCUS_NOTIFY , h , HAS_FOCUS_MASK , INPUT_MASK , KEY_NOTIFY , KEY_PRESSED , KEY_RELEASED , KEY_REPEATED , KEY_TYPED , LAYOUT_BOTTOM , LAYOUT_HCENTER , LAYOUT_LEFT , LAYOUT_RIGHT , LAYOUT_TOP , LAYOUT_VCENTER , mask , parent , POINT_DRAGGED , POINT_PRESSED , POINT_RELEASED , POINTER_NOTIFY , POS_MASK , PREFER_SIZE_MASK , prefH , prefW , SHOW_NOTIFY , SIZE_MASK , VALID_MASK , w , x , y

Constructor Summary ListItemComponent ( String str) 주어진 문자열로 ListItemComponent 의 인스턴스를 생성합니다. ListItemComponent ( String str, Image img) ListItemComponent 의 인스턴스를 생성합니다. ListItemComponent ( String str, String imgString) 주어진 문자열과 지정한 자원에서 읽어들이는 이미지 데이타로 ListItemComponent 의 인스턴스를 생성합니다.

Method Summary boolean getState () 현재의 선택 상태를 얻어옵니다. void setState (boolean bState) ListItemComponent 의 선택 상태를 지정합니다.

Methods inherited from class org.kwis.msp.lwc. LabelComponent calcPreferredSize , getFont , getImage , getLabel , paintContent , setFont , setImage , setLabel , setLayout

Methods inherited from class org.kwis.msp.lwc. Component canHandleInput , configure , focusNotify , getBackground , getCard , getForeground , getHeight , getPreferredHeight , getPreferredHeight , getPreferredWidth , getWidth , getX , getXOnScreen , getY , getYOnScreen , hasFocus , invalidate , isShown , isValid , keyNotify , layout , pointerNotify , processEvent , repaint , repaint , serviceRepaints , setBackground , setEventListener , setFocus , setForeground , showNotify , toString , validate

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , wait , wait , wait

Constructor Detail

### ListItemComponent

**Parameters:**
- `str` - `ListItemComponent`가 보여줄 문자열
 혹은 `null`

### ListItemComponent

**Parameters:**
- `img` - ListItem의 이미지 데이타 혹은 `null`

### ListItemComponent

**Parameters:**
- `imgString` - 이미지 자원의 경로명을 나타내는 문자열 혹은 `null`

Method Detail

### setState

**Parameters:**
- `bState` - 선택시 `true`, 선택 해제시 `false`

### getState

**Returns:**
- 선택된 상태면 `true`, 선택안된 상태면 `false`## 생성자 요약

- ListItemComponent ( String str) 주어진 문자열로 ListItemComponent 의 인스턴스를 생성합니다.
- ListItemComponent ( String str, Image img) ListItemComponent 의 인스턴스를 생성합니다.
- ListItemComponent ( String str, String imgString) 주어진 문자열과 지정한 자원에서 읽어들이는 이미지 데이타로 ListItemComponent 의 인스턴스를 생성합니다.

## 메서드 요약

- `boolean getState ()` — 현재의 선택 상태를 얻어옵니다.
- `void setState (boolean bState)` — ListItemComponent 의 선택 상태를 지정합니다.

## 생성자 상세

### ListItemComponent

```java
public ListItemComponent(String str)
```

**Parameters:**
- `str` - `ListItemComponent`가 보여줄 문자열
 혹은 `null`

### ListItemComponent

```java
public ListItemComponent(String str,
                         Image img)
```

**Parameters:**
- `img` - ListItem의 이미지 데이타 혹은 `null`

### ListItemComponent

```java
public ListItemComponent(String str,
                         String imgString)
```

**Parameters:**
- `imgString` - 이미지 자원의 경로명을 나타내는 문자열 혹은 `null`

### setState

```java
public void setState(boolean bState)
```

**Parameters:**
- `bState` - 선택시 `true`, 선택 해제시 `false`

### getState

```java
public boolean getState()
```

**Returns:**
- 선택된 상태면 `true`, 선택안된 상태면 `false`## 메서드 상세

### setState

```java
public void setState(boolean bState)
```

**Parameters:**
- `bState` - 선택시 `true`, 선택 해제시 `false`

### getState

```java
public boolean getState()
```

**Returns:**
- 선택된 상태면 `true`, 선택안된 상태면 `false`

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
