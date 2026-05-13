# Class Command

`package org.kwis.msp.lwc`

```
java.lang.Object
  |
  +--org.kwis.msp.lwc.Command
```

## 설명

**extends Object:**

사용자가 내릴수 있는 명령을 가르키는 클래스입니다.

 사용자가 UI컴포넌트 상에서 사용하고자 하는 커맨드를 정의합니다.
 커맨드는 문자열과 이미지로 표현하며 `CommandBarComponent`에 
 에 등록되어 사용합니다.

 이미지의 크기는 20x20pixel이어야 합니다.

**See Also:**
- ``CommandBarComponent``

## 생성자 요약

- Command ( String str, Image img, Image imgActive, Object obj) 커맨드를 생성합니다.
- Command ( String str, Image img, Object obj) 커맨드를 생성합니다.
- Command ( String str, Object obj) 커맨드를 생성합니다.
- Command ( String str, String imgString, Object obj) 커맨드를 생성합니다.
- Command ( String str, String imgString1, String imgString2, Object obj) 커맨드를 생성합니다.

## 메서드 요약

- `Image getActiveImage ()` — 활성화되었을때 사용하는 이미지를 얻어 옵니다.
- `Object getExtObject ()` — 생성시 설정한 Object객체를 돌려줍니다 내부에 저장되어 있는 명령을 확장하기위한 객체돌려줍니다.
- `Image getNormalImage ()` — 일반적인 이미지를 얻어 옵니다.
- `String getString ()` — 명령을 나타내는 문자열을 돌려줍니다.

## 생성자 상세

### Command

```java
public Command(String str,
               Object obj)
```

**Parameters:**
- `obj` - 확장Object

### Command

```java
public Command(String str,
               Image img,
               Object obj)
```

**Parameters:**
- `obj` - 확장Object

### Command

```java
public Command(String str,
               Image img,
               Image imgActive,
               Object obj)
```

**Parameters:**
- `obj` - 확장Object

### Command

```java
public Command(String str,
               String imgString,
               Object obj)
```

**Parameters:**
- `obj` - 확장Object

### Command

```java
public Command(String str,
               String imgString1,
               String imgString2,
               Object obj)
```

**Parameters:**
- `obj` - 확장Object

### getString

```java
public String getString()
```

**Returns:**
- 명령을 나타내는 문자열

### getExtObject

```java
public Object getExtObject()
```

**Returns:**
- 확장Object

### getNormalImage

```java
public Image getNormalImage()
```

**Returns:**
- 이미지

**See Also:**
- ``Image.loadImage(java.lang.String, org.kwis.msp.lcdui.ImageObserver)``

### getActiveImage

```java
public Image getActiveImage()
```

**Returns:**
- 이미지## 메서드 상세

### getString

```java
public String getString()
```

**Returns:**
- 명령을 나타내는 문자열

### getExtObject

```java
public Object getExtObject()
```

**Returns:**
- 확장Object

### getNormalImage

```java
public Image getNormalImage()
```

**Returns:**
- 이미지

**See Also:**
- ``Image.loadImage(java.lang.String, org.kwis.msp.lcdui.ImageObserver)``

### getActiveImage

```java
public Image getActiveImage()
```

**Returns:**
- 이미지

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
