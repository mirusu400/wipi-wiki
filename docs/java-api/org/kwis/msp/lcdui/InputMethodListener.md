# Interface InputMethodListener

`package org.kwis.msp.lcdui`

```
public void notifyTextChanged(char[] chText,
                              int length,
                              int pMode)
```

## 설명

**Parameters:**
- `pMode` - 처리상태 - Insert(-1) / replace(0) / delete(1)

========= END OF CLASS DATA =========

========== START OF NAVBAR ==========

=========== END OF NAVBAR ===========## 메서드 요약

- `void notifyTextChanged (char[] chText, int length, int pMode)` — InputMethod를 통해 전달된 문자객체를 받아 처리합니다.

## 메서드 상세

### notifyTextChanged

```java
public void notifyTextChanged(char[] chText,
                              int length,
                              int pMode)
```

**Parameters:**
- `pMode` - 처리상태 - Insert(-1) / replace(0) / delete(1)

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
