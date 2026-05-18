# Class LED

`package org.kwis.msp.handset`

```text
java.lang.Object
  |
  +--org.kwis.msp.handset.LED
```

## 설명

**extends Object:**

LED(Light Emitting Diodes) 를 조절하는 클래스이다.

## 메서드 요약

- `static int get ()` — LED의 on/off상태를 읽어온다
- `static int getCount ()` — 시스템의 LED 개수를 리턴한다
- `static void set (int leds)` — LED on/off를 설정한다.

## 메서드 상세

### getCount

```java
public static int getCount()
```

**Returns:**
- 시스템의 LED 개수

### set

```java
public static void set(int leds)
```

- LED on/off를 설정한다. 각bit가 1이면 on, 0이면 off를 나타낸다.
 
예) 
외장 LED가 4개 존재한다면 LSB BIT 부터 4개를 사용한다.

 0 bit
 +---------------------+
 | |*|*|*|*|
 +---------------------+
 
set(0x3) led2개를 켜고, 두개를 끈다.

### get

```java
public static int get()
```

**Returns:**
- 각 led의 on/off상태의 bit OR값

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
