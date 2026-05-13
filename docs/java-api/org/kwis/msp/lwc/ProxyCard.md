# Class ProxyCard

`package org.kwis.msp.lwc`

```
java.lang.Object
  |
  +--org.kwis.msp.lcdui.Card
        |
        +--org.kwis.msp.lwc.ProxyCard
```

## 설명

**extends Card:**

======== INNER CLASS SUMMARY ======== 
 =========== FIELD SUMMARY ===========

Fields inherited from class org.kwis.msp.lcdui. Card bTrans , h , w , x , y

======== CONSTRUCTOR SUMMARY ========

Constructor Summary ProxyCard ( ContainerComponent cmp) ProxyCard ( ContainerComponent cmp,
 boolean bTrans) ProxyCard ( ContainerComponent cmp,
 int x,
 int y,
 int w,
 int h) ProxyCard ( ContainerComponent cmp,
 int x,
 int y,
 int w,
 int h,
 boolean bTrans)

========== METHOD SUMMARY ===========

Method Summary protected  boolean keyNotify (int type,
 int chr) 사용자 키 입력이 생성되면 불립니다. protected  void paint ( Graphics g) Card의 내용을 그려줍니다. protected  boolean pointerNotify (int type,
 int x,
 int y) 사용자 포인팅 디바이스의 입력이 생성되면 불립니다. protected  void showNotify (boolean bShow) 이 카드가 보이기 바로 직전이나, 카드가 화면에서 삭제되는 
 경우에 불립니다.

Methods inherited from class org.kwis.msp.lcdui. Card getDisplay , getHeight , getWidth , getX , getY , isShown , move , repaint , repaint , resize , serviceRepaints

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , toString , wait , wait , wait

============ FIELD DETAIL =========== 
 ========= CONSTRUCTOR DETAIL ========

Constructor Detail

### ProxyCard

### ProxyCard

### ProxyCard

### ProxyCard

============ METHOD DETAIL ==========

Method Detail

### paint

- **Description copied from class: `Card`**

**Overrides:**
- `paint` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `g` - 칠해질 graphics

### keyNotify

- **Description copied from class: `Card`**

**Overrides:**
- `keyNotify` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `key` - keyCode값; 자세한 키코드는 ``EventQueue``를 참조

**Returns:**
- 하위 카드에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### pointerNotify

- **Description copied from class: `Card`**

**Overrides:**
- `pointerNotify` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `key` - 키 코드 값

**Returns:**
- 하위 `Card`에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### showNotify

- **Description copied from class: `Card`**

**Overrides:**
- `showNotify` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `bShow` - 보이는지 안보이는지 여부

========= END OF CLASS DATA =========

========== START OF NAVBAR ==========

=========== END OF NAVBAR ===========

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 생성자 요약

- ProxyCard ( ContainerComponent cmp)
- ProxyCard ( ContainerComponent cmp,
 boolean bTrans)
- ProxyCard ( ContainerComponent cmp,
 int x,
 int y,
 int w,
 int h)
- ProxyCard ( ContainerComponent cmp,
 int x,
 int y,
 int w,
 int h,
 boolean bTrans)

## 메서드 요약

- `protected  boolean keyNotify (int type, int chr)` — 사용자 키 입력이 생성되면 불립니다.
- `protected  void paint ( Graphics g)` — Card의 내용을 그려줍니다.
- `protected  boolean pointerNotify (int type, int x, int y)` — 사용자 포인팅 디바이스의 입력이 생성되면 불립니다.
- `protected  void showNotify (boolean bShow)` — 이 카드가 보이기 바로 직전이나, 카드가 화면에서 삭제되는 경우에 불립니다.

## 생성자 상세

### ProxyCard

```java
public ProxyCard(ContainerComponent cmp)
```

### ProxyCard

```java
public ProxyCard(ContainerComponent cmp,
                 boolean bTrans)
```

### ProxyCard

```java
public ProxyCard(ContainerComponent cmp,
                 int x,
                 int y,
                 int w,
                 int h)
```

### ProxyCard

```java
public ProxyCard(ContainerComponent cmp,
                 int x,
                 int y,
                 int w,
                 int h,
                 boolean bTrans)
```

### paint

```java
protected void paint(Graphics g)
```

- **Description copied from class: `Card`**

**Overrides:**
- `paint` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `g` - 칠해질 graphics

### keyNotify

```java
protected boolean keyNotify(int type,
                            int chr)
```

- **Description copied from class: `Card`**

**Overrides:**
- `keyNotify` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `key` - keyCode값; 자세한 키코드는 ``EventQueue``를 참조

**Returns:**
- 하위 카드에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### pointerNotify

```java
protected boolean pointerNotify(int type,
                                int x,
                                int y)
```

- **Description copied from class: `Card`**

**Overrides:**
- `pointerNotify` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `key` - 키 코드 값

**Returns:**
- 하위 `Card`에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### showNotify

```java
protected void showNotify(boolean bShow)
```

- **Description copied from class: `Card`**

**Overrides:**
- `showNotify` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `bShow` - 보이는지 안보이는지 여부

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*

## 메서드 상세

### paint

```java
protected void paint(Graphics g)
```

- **Description copied from class: `Card`**

**Overrides:**
- `paint` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `g` - 칠해질 graphics

### keyNotify

```java
protected boolean keyNotify(int type,
                            int chr)
```

- **Description copied from class: `Card`**

**Overrides:**
- `keyNotify` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `key` - keyCode값; 자세한 키코드는 ``EventQueue``를 참조

**Returns:**
- 하위 카드에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### pointerNotify

```java
protected boolean pointerNotify(int type,
                                int x,
                                int y)
```

- **Description copied from class: `Card`**

**Overrides:**
- `pointerNotify` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `key` - 키 코드 값

**Returns:**
- 하위 `Card`에 이벤트 전달하려면 `true`, 
 그렇지 않으면 `false`

### showNotify

```java
protected void showNotify(boolean bShow)
```

- **Description copied from class: `Card`**

**Overrides:**
- `showNotify` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `bShow` - 보이는지 안보이는지 여부

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
