# Interface ImageObserver

`package org.kwis.msp.lcdui`

```
public static final int FRAME_END
```

## 설명

### IMAGE_END

### NOT_EXIST

### DECODE_ERROR

### OUT_OF_MEMORY

Method Detail

### notify

**See Also:**
- ``Image.loadImage(java.lang.String, org.kwis.msp.lcdui.ImageObserver)``, 
``Image.play(org.kwis.msp.lcdui.ImageObserver)``## 필드 요약

- `static int DECODE_ERROR`
- `static int FRAME_END`
- `static int IMAGE_END`
- `static int NOT_EXIST`
- `static int OUT_OF_MEMORY`

## 메서드 요약

- `void notify ( Image img, int status)` — 이미지 한 프레임이 완성되었음을 알립니다.

## 필드 상세

### FRAME_END

```java
public static final int FRAME_END
```

### IMAGE_END

```java
public static final int IMAGE_END
```

### NOT_EXIST

```java
public static final int NOT_EXIST
```

### DECODE_ERROR

```java
public static final int DECODE_ERROR
```

### OUT_OF_MEMORY

```java
public static final int OUT_OF_MEMORY
```

### notify

```java
public void notify(Image img,
                   int status)
```

**See Also:**
- ``Image.loadImage(java.lang.String, org.kwis.msp.lcdui.ImageObserver)``, 
``Image.play(org.kwis.msp.lcdui.ImageObserver)``## 메서드 상세

### notify

```java
public void notify(Image img,
                   int status)
```

**See Also:**
- ``Image.loadImage(java.lang.String, org.kwis.msp.lcdui.ImageObserver)``, 
``Image.play(org.kwis.msp.lcdui.ImageObserver)``

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
