---
title: "Class CheckboxGroup"
---

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.CheckboxGroup
```

## 설명

**extends Object:**

`CheckboxGroup`은 여러개의 `CheckboxComponent`들을 역어 구릅된 라디오버튼 처럼 움직이게
 합니다.

하나의 `CheckboxGroup`으로 등록된 `CheckBoxComponent`들은 동시에 여러개가 ON상태가 될 수 
 없고 동시에는 하나의 `CheckboxComponent`만 ON될수 있습니다.
 그러므로 하나의 Checkbox가 ON 되면 다른 모든 Group으로 묵인 Checkbox들은 
 OFF 가 됩니다.
 초기 값으로는 맨 처음에 등록된 CheckboxComponent가 ON이 됩니다.

**See Also:**
- ``CheckboxComponent``

## 생성자 요약

- CheckboxGroup () 새로운 CheckboxGroup을 생성합니다.

## 메서드 요약

- `CheckboxComponent getSelectedCheckbox ()` — 이 CheckboxGroup 에 등록된 Checkbox중 현재 ON 상태인 CheckboxComponent 를 구합니다
- `void select ( CheckboxComponent cb)` — CheckboxGroup 으로 묶여 있는 CheckboxComponent 중에 주어진 컴포넌트를 ON상태로 합니다.
- `void setChangeListener ( ChangeListener listener, Object obj)` — CheckboxGroup 에 ChangeListener 를 등록 합니다.

## 생성자 상세

### CheckboxGroup

```java
public CheckboxGroup()
```

**See Also:**
- ``CheckboxComponent``

### select

```java
public void select(CheckboxComponent cb)
```

**Parameters:**
- `cb` - select할 CheckboxComponent.

**Throws:**
- `NullPointerException` - `cb`가 null인 경우.

**See Also:**
- ``getSelectedCheckbox()``

### getSelectedCheckbox

```java
public CheckboxComponent getSelectedCheckbox()
```

**Returns:**
- 현재 ON상태인 `CheckboxComponent`

**See Also:**
- ``select(org.kwis.msp.lwc.CheckboxComponent)``

### setChangeListener

```java
public void setChangeListener(ChangeListener listener,
                              Object obj)
```

**Parameters:**
- `obj` - Listener가 불려질때 넘겨 받을 Object (확장 파라메터)

**See Also:**
- `CheckboxComponent#CheckboxComponent(String, Image, CheckboxGroup, boolean)`, 
``CheckboxComponent.CheckboxComponent(String, Image, CheckboxGroup)``, 
``CheckboxComponent.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object)``## 메서드 상세

### select

```java
public void select(CheckboxComponent cb)
```

**Parameters:**
- `cb` - select할 CheckboxComponent.

**Throws:**
- `NullPointerException` - `cb`가 null인 경우.

**See Also:**
- ``getSelectedCheckbox()``

### getSelectedCheckbox

```java
public CheckboxComponent getSelectedCheckbox()
```

**Returns:**
- 현재 ON상태인 `CheckboxComponent`

**See Also:**
- ``select(org.kwis.msp.lwc.CheckboxComponent)``

### setChangeListener

```java
public void setChangeListener(ChangeListener listener,
                              Object obj)
```

**Parameters:**
- `obj` - Listener가 불려질때 넘겨 받을 Object (확장 파라메터)

**See Also:**
- `CheckboxComponent#CheckboxComponent(String, Image, CheckboxGroup, boolean)`, 
``CheckboxComponent.CheckboxComponent(String, Image, CheckboxGroup)``, 
``CheckboxComponent.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object)``

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
