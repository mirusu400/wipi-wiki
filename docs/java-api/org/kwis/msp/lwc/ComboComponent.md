# Class ComboComponent

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.ComboComponent
```

## 설명

**extends Component:**

`ComboComponent`는 팝업메뉴 기능을 제공하는 클래스입니다.

`ComboComponent`는 팝업 메뉴 항목 중 선택된 항목를 보여주는
 영역과 팝업 메뉴의 리스트를 보여주는 영역으로 나뉘어 있습니다.
 선택항목을 보여주는 화면에서 `SELECT`키 입력시 팝업 메뉴 리스트가 보여지며
 이 중 어떤 항목를 선택하면 팝업 메뉴 리스트는 화면에서 제거되고 새로운 선택 항목만이
 보여지게 됩니다.

`ComboComponent`에서는 선택항목의 변경을 감시할 수 있는
 `ChangeListener`를 등록하여 사용할 수 있으며, 팝업메뉴에서 새로운 항목을
 선택시 `ChangeListener`의 `changed` 메소드를 호출하게됩니다.

Fields inherited from class org.kwis.msp.lwc. Component bg , evtListener , evtListenerObj , fg , FOCUS_NOTIFY , h , HAS_FOCUS_MASK , INPUT_MASK , KEY_NOTIFY , KEY_PRESSED , KEY_RELEASED , KEY_REPEATED , KEY_TYPED , LAYOUT_BOTTOM , LAYOUT_HCENTER , LAYOUT_LEFT , LAYOUT_RIGHT , LAYOUT_TOP , LAYOUT_VCENTER , mask , parent , POINT_DRAGGED , POINT_PRESSED , POINT_RELEASED , POINTER_NOTIFY , POS_MASK , PREFER_SIZE_MASK , prefH , prefW , SHOW_NOTIFY , SIZE_MASK , VALID_MASK , w , x , y

Constructor Summary ComboComponent () ComboComponent 의 인스턴스를 생성합니다.

Method Summary int append ( String str) 주어진 문자데이타로 팝업메뉴의 새로운 항목을 생성하여 팝업메뉴 리스트의 맨 아래
 위치에 추가합니다. void delete (int index) 팝업메뉴 리스트의 주어진 index 위치에 있는 항목을 삭제합니다. int getPreferredHeight () 컴포넌트의 적절한 높이를 결정합니다. int getPreferredHeight (int w) 컴포넌트의 적절한 높이를 결정합니다. int getPreferredWidth () 컴포넌트의 적절한 폭을 결정합니다. int getSelectedIndex () 팝업메뉴 리스트의 항목들 중 선택되어 있는 항목의 인덱스를 구합니다 int getSize () ComboComponent 의 팝업메뉴 리스트 항목들의 개수를 구합니다. String getString () 현재 선택되어 있는 항목의 문자열을 구합니다. int insert (int index, String str) 주어진 index 위치에 주어진 문자데이타로 팝업메뉴의 새로운 항목을
 생성하여 팝업메뉴 리스트에 삽입합니다. protected  boolean keyNotify (int type,
 int key) 키 입력을 받으면 호출됩니다. void paintContent ( Graphics g) 내부를 칠합니다. void select (int index) 팝업메뉴 리스트에서 주어진 index 의 항목을 선택합니다. void set (int index, String str) 주어진 index 위치에 주어진 문자데이타로 팝업메뉴 항목을 생성하여
 새로 지정합니다. void setChangeListener ( ChangeListener listener, Object obj) ComboComponent 에서 팝업메뉴 리스트의 항목들 중 선택된 항목이
 변경된 경우, 변경상태를 감시할 ChangeListener 를 설정합니다.

Methods inherited from class org.kwis.msp.lwc. Component calcPreferredSize , canHandleInput , configure , focusNotify , getBackground , getCard , getForeground , getHeight , getWidth , getX , getXOnScreen , getY , getYOnScreen , hasFocus , invalidate , isShown , isValid , layout , pointerNotify , processEvent , repaint , repaint , serviceRepaints , setBackground , setEventListener , setFocus , setForeground , showNotify , toString , validate

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , wait , wait , wait

Constructor Detail

### ComboComponent

- `ComboComponent`의 인스턴스를 생성합니다.

Method Detail

### append

**Parameters:**
- `str` - 추가될 문자열

**Returns:**
- 추가된 문자열의 인덱스

**Throws:**
- `IllegalArgumentException` - str이 null 일 경우 발생.

### insert

**Parameters:**
- `index` - 삽입할 항목의 인덱스

**Returns:**
- 삽입된 인덱스값

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우

**See Also:**
- ``ListComponent.insert(int, java.lang.String, org.kwis.msp.lcdui.Image)``

### set

**Parameters:**
- `index` - 대치할 항목의 인덱스

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우

### delete

**Parameters:**
- `index` - 삭제할 항목의 인덱스

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우

### getString

**Returns:**
- 선택된 항목의 문자열, 선택되지 않은경우 null이 리턴.

### getSize

**Returns:**
- 가지고 있는 항목들의 개수

### getSelectedIndex

**Returns:**
- 선택되어있는 항목의 인덱스. 선택된것이 없는 경우 -1을 리턴.

### getPreferredHeight

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 높이

### getPreferredHeight

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `w` - 가변폭.

**Returns:**
- 컴포넌트의 높이.

### getPreferredWidth

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredWidth` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 폭.

### paintContent

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `g` - 칠할 Graphics.

**See Also:**
- ``Graphics``

### keyNotify

- **Description copied from class: `Component`**

**Overrides:**
- `keyNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며
 이외의 문자도 넘어 올 수 있습니다.

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 키를 이 컴포넌트가 처리했다면,
 `true`를 넘겨 줍니다. 그렇지 않았다면 `false`를
 돌려줍니다.

### setChangeListener

**Parameters:**
- `obj` - 설정할 Object ,사용하지 않을때는 null을 넣는다. 이 Object는 Change이벤트가 발생되어 ChangeListener의 changed 함수가 불려질때 인자로 넘겨집니다.

### select

**Parameters:**
- `index` - 선택할 항목의 인덱스

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우

## 생성자 요약

- ComboComponent () ComboComponent 의 인스턴스를 생성합니다.

## 메서드 요약

- `int append ( String str)` — 주어진 문자데이타로 팝업메뉴의 새로운 항목을 생성하여 팝업메뉴 리스트의 맨 아래 위치에 추가합니다.
- `void delete (int index)` — 팝업메뉴 리스트의 주어진 index 위치에 있는 항목을 삭제합니다.
- `int getPreferredHeight ()` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredHeight (int w)` — 컴포넌트의 적절한 높이를 결정합니다.
- `int getPreferredWidth ()` — 컴포넌트의 적절한 폭을 결정합니다.
- `int getSelectedIndex ()` — 팝업메뉴 리스트의 항목들 중 선택되어 있는 항목의 인덱스를 구합니다
- `int getSize ()` — ComboComponent 의 팝업메뉴 리스트 항목들의 개수를 구합니다.
- `String getString ()` — 현재 선택되어 있는 항목의 문자열을 구합니다.
- `int insert (int index, String str)` — 주어진 index 위치에 주어진 문자데이타로 팝업메뉴의 새로운 항목을 생성하여 팝업메뉴 리스트에 삽입합니다.
- `protected  boolean keyNotify (int type, int key)` — 키 입력을 받으면 호출됩니다.
- `void paintContent ( Graphics g)` — 내부를 칠합니다.
- `void select (int index)` — 팝업메뉴 리스트에서 주어진 index 의 항목을 선택합니다.
- `void set (int index, String str)` — 주어진 index 위치에 주어진 문자데이타로 팝업메뉴 항목을 생성하여 새로 지정합니다.
- `void setChangeListener ( ChangeListener listener, Object obj)` — ComboComponent 에서 팝업메뉴 리스트의 항목들 중 선택된 항목이 변경된 경우, 변경상태를 감시할 ChangeListener 를 설정합니다.

## 생성자 상세

### ComboComponent

```java
public ComboComponent()
```

- `ComboComponent`의 인스턴스를 생성합니다.

### append

```java
public int append(String str)
```

**Parameters:**
- `str` - 추가될 문자열

**Returns:**
- 추가된 문자열의 인덱스

**Throws:**
- `IllegalArgumentException` - str이 null 일 경우 발생.

### insert

```java
public int insert(int index,
                  String str)
```

**Parameters:**
- `index` - 삽입할 항목의 인덱스

**Returns:**
- 삽입된 인덱스값

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우

**See Also:**
- ``ListComponent.insert(int, java.lang.String, org.kwis.msp.lcdui.Image)``

### set

```java
public void set(int index,
                String str)
```

**Parameters:**
- `index` - 대치할 항목의 인덱스

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우

### delete

```java
public void delete(int index)
```

**Parameters:**
- `index` - 삭제할 항목의 인덱스

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우

### getString

```java
public String getString()
```

**Returns:**
- 선택된 항목의 문자열, 선택되지 않은경우 null이 리턴.

### getSize

```java
public int getSize()
```

**Returns:**
- 가지고 있는 항목들의 개수

### getSelectedIndex

```java
public int getSelectedIndex()
```

**Returns:**
- 선택되어있는 항목의 인덱스. 선택된것이 없는 경우 -1을 리턴.

### getPreferredHeight

```java
public int getPreferredHeight()
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 높이

### getPreferredHeight

```java
public int getPreferredHeight(int w)
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `w` - 가변폭.

**Returns:**
- 컴포넌트의 높이.

### getPreferredWidth

```java
public int getPreferredWidth()
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredWidth` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 폭.

### paintContent

```java
public void paintContent(Graphics g)
```

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `g` - 칠할 Graphics.

**See Also:**
- ``Graphics``

### keyNotify

```java
protected boolean keyNotify(int type,
                            int key)
```

- **Description copied from class: `Component`**

**Overrides:**
- `keyNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며
 이외의 문자도 넘어 올 수 있습니다.

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 키를 이 컴포넌트가 처리했다면,
 `true`를 넘겨 줍니다. 그렇지 않았다면 `false`를
 돌려줍니다.

### setChangeListener

```java
public void setChangeListener(ChangeListener listener,
                              Object obj)
```

**Parameters:**
- `obj` - 설정할 Object ,사용하지 않을때는 null을 넣는다. 이 Object는 Change이벤트가 발생되어 ChangeListener의 changed 함수가 불려질때 인자로 넘겨집니다.

### select

```java
public void select(int index)
```

**Parameters:**
- `index` - 선택할 항목의 인덱스

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우

## 메서드 상세

### append

```java
public int append(String str)
```

**Parameters:**
- `str` - 추가될 문자열

**Returns:**
- 추가된 문자열의 인덱스

**Throws:**
- `IllegalArgumentException` - str이 null 일 경우 발생.

### insert

```java
public int insert(int index,
                  String str)
```

**Parameters:**
- `index` - 삽입할 항목의 인덱스

**Returns:**
- 삽입된 인덱스값

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우

**See Also:**
- ``ListComponent.insert(int, java.lang.String, org.kwis.msp.lcdui.Image)``

### set

```java
public void set(int index,
                String str)
```

**Parameters:**
- `index` - 대치할 항목의 인덱스

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우

### delete

```java
public void delete(int index)
```

**Parameters:**
- `index` - 삭제할 항목의 인덱스

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우

### getString

```java
public String getString()
```

**Returns:**
- 선택된 항목의 문자열, 선택되지 않은경우 null이 리턴.

### getSize

```java
public int getSize()
```

**Returns:**
- 가지고 있는 항목들의 개수

### getSelectedIndex

```java
public int getSelectedIndex()
```

**Returns:**
- 선택되어있는 항목의 인덱스. 선택된것이 없는 경우 -1을 리턴.

### getPreferredHeight

```java
public int getPreferredHeight()
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 높이

### getPreferredHeight

```java
public int getPreferredHeight(int w)
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredHeight` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `w` - 가변폭.

**Returns:**
- 컴포넌트의 높이.

### getPreferredWidth

```java
public int getPreferredWidth()
```

- **Description copied from class: `Component`**

**Overrides:**
- `getPreferredWidth` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Returns:**
- 컴포넌트의 폭.

### paintContent

```java
public void paintContent(Graphics g)
```

- **Description copied from class: `Component`**

**Overrides:**
- `paintContent` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `g` - 칠할 Graphics.

**See Also:**
- ``Graphics``

### keyNotify

```java
protected boolean keyNotify(int type,
                            int key)
```

- **Description copied from class: `Component`**

**Overrides:**
- `keyNotify` in class `Component`
- Following copied from class: `org.kwis.msp.lwc.Component`

**Parameters:**
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며
 이외의 문자도 넘어 올 수 있습니다.

**Returns:**
- 만일 컴포넌트가 인수로 넘오는 키를 이 컴포넌트가 처리했다면,
 `true`를 넘겨 줍니다. 그렇지 않았다면 `false`를
 돌려줍니다.

### setChangeListener

```java
public void setChangeListener(ChangeListener listener,
                              Object obj)
```

**Parameters:**
- `obj` - 설정할 Object ,사용하지 않을때는 null을 넣는다. 이 Object는 Change이벤트가 발생되어 ChangeListener의 changed 함수가 불려질때 인자로 넘겨집니다.

### select

```java
public void select(int index)
```

**Parameters:**
- `index` - 선택할 항목의 인덱스

**Throws:**
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우
