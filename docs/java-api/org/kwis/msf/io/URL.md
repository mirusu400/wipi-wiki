# Class URL

`package org.kwis.msf.io`

```
java.lang.Object
  |
  +--org.kwis.msf.io.URL
```

## 설명

**extends Object:**

플랫폼 외부와의 데이타 통신을 위해 소켓을 생성해주는 클래스이다.

모든 소켓은 URL(RFC1738 참조) 방식으로 생성된다.
URL 의 sheme 부분에 의해 생성되는 소켓의 성격이 구분된다. 소켓의 성격은
stream 소켓과 그렇지 않은 것으로 나뉜다.

## 생성자 요약

- URL ()

## 메서드 요약

- `static Socket find ( String url)` — 매개변수 url 에 따라 소켓을 생성한다.

## 생성자 상세

### URL

```java
public URL()
```

### find

```java
public static Socket find(String url)
                   throws SchemeNotFoundException
```

**Throws:**
- `SchemeNotFoundException` - 소켓을 생성하지 못할 경우## 메서드 상세

### find

```java
public static Socket find(String url)
                   throws SchemeNotFoundException
```

**Throws:**
- `SchemeNotFoundException` - 소켓을 생성하지 못할 경우

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
