---
title: "Class Runtime"
---

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Runtime
```

## 설명

**extends Object:**

모든 Java 응용 프로그램에는 응용 프로그램이 실행되는 
환경과 상호 작용할 수 있도록 해주는 `Runtime` 클래스의 
단일 인스턴스가 있습니다. 
현재 런타임은 `getRuntime` 메소드에서 가져올 수 있습니다.

응용 프로그램은 이 클래스의 자체 인스턴스를 만들 수 없습니다.

**Since:**
- JDK1.0, CLDC 1.0

**See Also:**
- ``getRuntime()``

## 메서드 요약

- `void exit (int status)` — 현재 실행 중인 Java 응용 프로그램을 종료합니다.
- `long freeMemory ()` — 시스템에서 사용 가능한 메모리 양을 반환합니다.
- `void gc ()` — 가비지 컬렉터를 실행합니다.
- `static Runtime getRuntime ()` — 현재 Java 응용 프로그램과 연결된 런타임 객체를 반환합니다.
- `long totalMemory ()` — Java 가상 머신의 총 메모리 양을 반환합니다.

## 메서드 상세

### getRuntime

```java
public static Runtime getRuntime()
```

**Returns:**
- 현재 Java 응용 프로그램과 연결된 
 `Runtime` 객체

### exit

```java
public void exit(int status)
```

**Parameters:**
- `status` - 종료 상태

**Since:**
- JDK1.0

### freeMemory

```java
public long freeMemory()
```

**Returns:**
- 나중에 할당된 객체에 사용할 수 있는 
 총 메모리 양의 근사값(바이트)

### totalMemory

```java
public long totalMemory()
```

**Returns:**
- 현재 및 이후의 객체에 사용할 수 있는 
 총 메모리 양(바이트)

### gc

```java
public void gc()
```

가비지 컬렉터를 실행합니다. 
이 메소드를 호출하면 Java 가상 머신은 현재 사용 중인 메모리를 
빨리 다시 이용할 수 있도록 사용되지 않는 객체를 재활용하려고 시도합니다. 
메소드 호출에서 다시 제어가 반환되면 Java 가상 머신은 삭제된 
모든 객체를 재활용하려고 
노력합니다. gc 라는 이름은 "가비지 컬렉터"를 나타냅니다. 
Java 가상 머신은 gc 메소드를 명시적으로 호출하지 않아도 
필요에 따라 자동으로 
재활용 프로세스를 수행합니다. System.gc() 메소드는 이 메소드를 호출하는 
일반적이고 편리한 방법입니다.
