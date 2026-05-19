---
title: "Class TextComponent.ModeViewer"
---

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lcdui.Card
        |
        +--org.kwis.msp.lwc.TextComponent.ModeViewer
```

## 설명

**Enclosing class:**
- `TextComponent`

**extends Card:**

현재의 입력모드만을 보여주는 카드입니다.

Fields inherited from class org.kwis.msp.lcdui. Card bTrans , h , w , x , y

Constructor Summary TextComponent.ModeViewer ( Display d)

Method Summary void notifyChangeMode () 현재의입력 모드가 변경되면 이 카드를 사용중이 TextComponent에서
 현재 입력 모드가 변경되었다는 것을 알려주기위해 호출되는
 메소드입니다. protected  void paint ( Graphics g) Card의 내용을 그려줍니다.

Methods inherited from class org.kwis.msp.lcdui. Card getDisplay , getHeight , getWidth , getX , getY , isShown , keyNotify , move , pointerNotify , repaint , repaint , resize , serviceRepaints , showNotify

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , toString , wait , wait , wait

Constructor Detail

### TextComponent.ModeViewer

Method Detail

### notifyChangeMode

- 현재의입력 모드가 변경되면 이 카드를 사용중이 TextComponent에서
 현재 입력 모드가 변경되었다는 것을 알려주기위해 호출되는
 메소드입니다.
 이 메소드가 호출되면 이 카드를 다시 화면에 그려주는
 페이트 메소드를 호출합니다.

### paint

- **Description copied from class: `Card`**

**Overrides:**
- `paint` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `g` - 칠해질 graphics## 생성자 요약

- TextComponent.ModeViewer ( Display d)

## 메서드 요약

- `void notifyChangeMode ()` — 현재의입력 모드가 변경되면 이 카드를 사용중이 TextComponent에서 현재 입력 모드가 변경되었다는 것을 알려주기위해 호출되는 메소드입니다.
- `protected  void paint ( Graphics g)` — Card의 내용을 그려줍니다.

## 생성자 상세

### TextComponent.ModeViewer

```java
public TextComponent.ModeViewer(Display d)
```

### notifyChangeMode

```java
public void notifyChangeMode()
```

- 현재의입력 모드가 변경되면 이 카드를 사용중이 TextComponent에서
 현재 입력 모드가 변경되었다는 것을 알려주기위해 호출되는
 메소드입니다.
 이 메소드가 호출되면 이 카드를 다시 화면에 그려주는
 페이트 메소드를 호출합니다.

### paint

```java
protected void paint(Graphics g)
```

- **Description copied from class: `Card`**

**Overrides:**
- `paint` in class `Card`
- Following copied from class: `org.kwis.msp.lcdui.Card`

**Parameters:**
- `g` - 칠해질 graphics## 메서드 상세

### notifyChangeMode

```java
public void notifyChangeMode()
```

- 현재의입력 모드가 변경되면 이 카드를 사용중이 TextComponent에서
 현재 입력 모드가 변경되었다는 것을 알려주기위해 호출되는
 메소드입니다.
 이 메소드가 호출되면 이 카드를 다시 화면에 그려주는
 페이트 메소드를 호출합니다.

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

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
