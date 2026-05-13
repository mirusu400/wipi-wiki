# Class Runtime

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Runtime
```

## 설명

**extends Object:**

VM에 Runtime객체는 하나만 존재하며 이 객체를 통해 프로그램이 
 동작하는 환경에 대한 정보를 얻을 수 있다.

## 메서드 요약

- `void exit (int status)` — 현재 수행 중인 프로그램을 종료한다.
- `long freeMemory ()` — 현재 사용 가능한 메모리량을 구한다.
- `void gc ()` — garbage Collection을 기동 시킴니다.
- `static Runtime getRuntime ()` — 시스템내에 존재하는 Runtime객체 정보를 구한다.
- `long totalMemory ()` — 시스템 내에 존재하는 메모리 총량을 구한다.

## 메서드 상세

### exit

```java
public void exit(int status)
```

**Parameters:**
- `status` - 종료 상황에 대한 정보를 나타내는 정수값.

### freeMemory

```java
public long freeMemory()
```

**Returns:**
- long형으로 사용가능한 바이트 수.

### gc

```java
public void gc()
```

- garbage Collection을 기동 시킴니다.

### getRuntime

```java
public static Runtime getRuntime()
```

**Returns:**
- Runtime객체.

### totalMemory

```java
public long totalMemory()
```

**Returns:**
- long형으로 메모리 총 바이트 수

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
