# Class Shared

`package org.kwis.msf.core`

```
java.lang.Object
  |
  +--org.kwis.msf.core.Shared
```

## 설명

**extends Object:**

## 메서드 요약

- `static byte[] createBuf (int size)` — 공유 버퍼를 create한다.
- `static byte[] createBuf ( String name, int size)` — 네임(name) 공유 버퍼를 create한다.
- `static void destroyBuf (byte[] sharedBuf)` — 생성된 공유버퍼를 파괴한다.
- `static byte[] getBuf ()` — shared 버퍼를 얻는다.
- `static byte[] getBuf ( String name)` — 공유 버퍼를 얻는다.
- `static void initialize ()`
- `static byte[] resizeBuf (byte[] sharedBuf, int size)` — 공유버퍼의 크기를 변경한다.
- `static byte[] resizeBuf (int size)` — 공유버퍼의 크기를 변경한다.

## 메서드 상세

### initialize

```java
public static void initialize()
```

### createBuf

```java
public static byte[] createBuf(String name,
                               int size)
```

**Parameters:**
- `size` - 생성시킬 byte array 버퍼의 크기

**Returns:**
- 성공이면 생성된 buf를 돌려주고, 이미 생성된 버퍼가 존재하거나 더이상 
공유버퍼를 생성할 수 없으면 null을 돌려준다.

### getBuf

```java
public static byte[] getBuf(String name)
```

**Parameters:**
- `name` - 얻어올 공유버퍼의 이름

**Returns:**
- 성공이면 공유버퍼, 실패하면 null을 돌려줌

### resizeBuf

```java
public static byte[] resizeBuf(byte[] sharedBuf,
                               int size)
```

**Parameters:**
- `size` - 변경할 공유버퍼 크기

**Returns:**
- 크기가 변경된 공유버퍼

### destroyBuf

```java
public static void destroyBuf(byte[] sharedBuf)
```

**Parameters:**
- `sharedBuf` - 파괴시킬 공유버퍼 첨조자(reference)

### createBuf

```java
public static byte[] createBuf(int size)
```

**Parameters:**
- `size` - 생성시킬 byte array 버퍼의 크기

**Returns:**
- 성공이면 생성된 buf를 돌려주고, 이미 생성된 버퍼가 존재하면 null을 돌려준다.

### getBuf

```java
public static byte[] getBuf()
```

**Returns:**
- 성공이면 공유버퍼, 실패하면 null을 돌려줌

### resizeBuf

```java
public static byte[] resizeBuf(int size)
```

**Parameters:**
- `size` - 변경할 공유버퍼 크기

**Returns:**
- 크기가 변경된 공유버퍼

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
