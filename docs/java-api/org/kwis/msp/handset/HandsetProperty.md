# Class HandsetProperty

`package org.kwis.msp.handset`

```text
java.lang.Object
  |
  +--org.kwis.msp.handset.HandsetProperty
```

## 설명

**extends Object:**

단말기에 특화된 값들을 관리하는 클래스이다

## 메서드 요약

- `static String getSystemProperty ( String id)` — 단말기에 특화된 값을 읽어 온다
- `static boolean setSystemProperty ( String id, String val)` — 단말기에 특화된 값을 설정 한다

## 메서드 상세

### getSystemProperty

```java
public static String getSystemProperty(String id)
```

**Parameters:**
- `id` - 특화된 값에 대한 식별 문자열

**Returns:**
- 특화된 값

### setSystemProperty

```java
public static boolean setSystemProperty(String id,
                                        String val)
```

**Parameters:**
- `val` - 설정 할 값

**Returns:**
- true면 설정성공, false면 설정 실패

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
