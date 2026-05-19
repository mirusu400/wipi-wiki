---
title: "Class Ticker"
---

`package javax.microedition.lcdui`

```text
java.lang.Object
  |
  +--javax.microedition.lcdui.Ticker
```

## 설명

**extends Object:**

디스플레이에 텍스트의 일부가 계속하여 지나가는 
"티커 테이프"를 구현합니다. 
스크롤의 방향과 속도는 구현에 따라 다릅니다. 
티커 문자열은 애니메이션이 지속되는 동안 계속하여 스크롤됩니다. 
즉, 문자열이 디스플레이 밖에서 스크롤을 마치면 티커는 다시 문자열의 처음부터 스크롤을 시작합니다.

티커를 시작하거나 중지하는 API는 제공되지 않습니다. 
응용 프로그램 모델에서는 티커가 항상 계속하여 스크롤하도록 되어 있습니다. 
하지만 구현 시에는 예를 들어, 사용자가 일정 시간 동안 장치를 
사용하지 않을 경우 전력 소모를 방지하기 위해 스크롤을 
일시 중지할 수 있습니다. 사용자가 장치를 다시 사용하면 
티커 스크롤을 다시 시작해야 합니다.

티커의 텍스트에는 `줄 바꿈`이 
포함될 수 있습니다. 티커 내에 
전체 텍스트가 표시되어야 하므로 
줄 바꿈 문자는 표시되지 않아야 하지만 
구분자로 사용될 수 있습니다.

같은 티커를 여러 `Displayable` 
객체("screens")에서 공유할 수 있습니다. 
이는 각각의 객체에서 ``setTicker()``를 
호출하여 수행할 수 있습니다. 전형적인 사용법은 응용 프로그램이 
같은 티커를 모든 화면에 배치하는 것입니다. 
응용 프로그램이 같은 티커가 있는 두 개의 화면 사이를 전환하면 
티커가 디스플레이의 같은 위치에 표시되고 같은 위치에서 
내용이 계속 스크롤되도록 하는 것이 좋습니다. 
이렇게 하면 티커가 각 화면이 아닌 해당 디스플레이에 연결된 것처럼 보입니다.

다른 사용 모델에서는 응용 프로그램이 서로 다른 화면 세트나 
각 화면마다 서로 다른 티커를 사용합니다. 
티커는 `Displayable` 클래스의 속성이므로, 
응용 프로그램은 사용자가 여러 화면을 전환할 때 티커를 
업데이트하여 표시되도록 하지 않고도 
이 모델을 구현할 수 있습니다.

**Since:**
- MIDP 1.0

## 생성자 요약

- Ticker ( String str) 초기 내용 문자열을 제공하는 새 Ticker 객체를 구성합니다.

## 메서드 요약

- `String getString ()` — 현재 티커가 스크롤하는 문자열을 가져옵니다.
- `void setString ( String str)` — 티커가 해당 문자열을 표시하도록 설정합니다.

## 생성자 상세

### Ticker

```java
public Ticker(String str)
```

- 초기 내용 문자열을 제공하는 새 `Ticker` 
객체를 구성합니다.

**Parameters:**
- `str` - `Ticker`에 설정될 문자열

**Throws:**
- `NullPointerException` - `str`이 `null`인 경우

### setString

```java
public void setString(String str)
```

**Parameters:**
- `str` - `Ticker`에 설정될 문자열

**Throws:**
- `NullPointerException` - `str`이 `null`인 경우

**See Also:**
- ``getString()``

### getString

```java
public String getString()
```

**Returns:**
- 티커의 문자열

**See Also:**
- ``setString(java.lang.String)``

## 메서드 상세

### setString

```java
public void setString(String str)
```

**Parameters:**
- `str` - `Ticker`에 설정될 문자열

**Throws:**
- `NullPointerException` - `str`이 `null`인 경우

**See Also:**
- ``getString()``

### getString

```java
public String getString()
```

**Returns:**
- 티커의 문자열

**See Also:**
- ``setString(java.lang.String)``
