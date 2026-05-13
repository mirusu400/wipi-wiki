# Class Random

`package java.util`

```
java.lang.Object
  |
  +--java.util.Random
```

## 설명

**extends Object:**

이 클래스의 인스턴스는 의사 난수 스트림을 생성하는 데 사용됩니다. 
클래스는 선형 일치 공식으로 수정되는 48비트 시드를 사용합니다. 
(Donald Knuth, *The Art of Computer Programming, Volume 2*, 3.2.1절을 
참조하십시오.)

동일한 시드를 사용하여 `Random`의 두 인스턴스를 만들고 
각각에 대해 동일한 메소드 호출 시퀀스를 구성하면 
두 인스턴스는 동일한 숫자 시퀀스를 생성하여 반환합니다. 
이 등록 정보를 보장하기 위해 `Random` 클래스에 특정 
알고리즘이 지정됩니다. Java 구현 시에는 Java 코드의 완벽한 
이식성을 위해 여기에 나열된 모든 알고리즘을 `Random` 클래스에 
사용해야 합니다. 하지만 `Random` 클래스의 서브 클래스는 
모든 메소드의 일반 계약에 따르기만 하면 
다른 알고리즘을 사용할 수도 있습니다.

`Random` 클래스에서 구현하는 알고리즘은 각 호출마다 
의사 난수로 생성된 최대 32개의 비트를 제공할 수 있는 
`protected` 유틸리티 메소드를 사용합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- Random () 새로운 난수 생성기를 만듭니다.
- Random (long seed) 단일 long 시드를 사용하여 새로운 난수 생성기를 만듭니다.

## 메서드 요약

- `protected  int next (int bits)` — 다음 의사 난수를 생성합니다.
- `double nextDouble ()` — 이 난수 생성기 시퀀스에서 생성된 0.0 과 1.0 사이의 균일하게 분산된 다음 의사 난수 double 값을 반환합니다.
- `float nextFloat ()` — 이 난수 생성기 시퀀스에서 생성된 0.0 과 1.0 사이의 균일하게 분산된 다음 의사 난수 float 값을 반환합니다.
- `int nextInt ()` — 이 난수 생성기 시퀀스에서 균일하게 분산된 다음 의사 난수 int 값을 반환합니다.
- `int nextInt (int n)` — 이 난수 생성기 시퀀스에서 가져온 0(포함)과 지정된 값(포함하지 않음) 사이의 균일하게 분산된 의사 난수 int 값을 반환합니다.
- `long nextLong ()` — 이 난수 생성기 시퀀스에서 균일하게 분산된 다음 의사 난수 long 값을 반환합니다.
- `void setSeed (long seed)` — 단일 long 시드를 사용하여 이 난수 생성기의 시드를 설정합니다.

## 생성자 상세

### Random

```java
public Random()
```

- 새로운 난수 생성기를 만듭니다. 
해당 시드는 현재 시간을 기반으로 하는 값으로 초기화됩니다.

 public Random() { this(System.currentTimeMillis()); }

**See Also:**
- ``System.currentTimeMillis()``

### Random

```java
public Random(long seed)
```

- 단일 `long` 
시드를 사용하여 새로운 난수 생성기를 만듭니다.

 public Random(long seed) { setSeed(seed); }
`next` 메소드에서 의사 난수 생성기의 
상태를 유지하기 위해 사용합니다.

**Parameters:**
- `seed` - 초기 시드

**See Also:**
- ``setSeed(long)``

### setSeed

```java
public void setSeed(long seed)
```

**Parameters:**
- `seed` - 초기 시드

### next

```java
protected int next(int bits)
```

**Parameters:**
- `bits` - 임의 비트

**Returns:**
- 난수 생성기 시퀀스에서 다음 의사 난수 값

### nextInt

```java
public int nextInt()
```

**Returns:**
- 이 난수 생성기 시퀀스에서 균일하게 분산된 다음 의사 난수 
 `int` 값

### nextInt

```java
public int nextInt(int n)
```

**Parameters:**
- `n` - 반환되는 난수의 범위. 
 양수여야 합니다.

**Returns:**
- 0(포함)과 n(포함하지 않음) 사이의 균일하게 분산된 의사 난수 
 `int` 값

**Throws:**
- `IllegalArgumentException` - n이 양수가 아닐 경우

**Since:**
- CLDC 1.1

### nextLong

```java
public long nextLong()
```

**Returns:**
- 이 난수 생성기 시퀀스에서 균일하게 분산된 다음 
 의사 난수 `long` 값

### nextFloat

```java
public float nextFloat()
```

**Returns:**
- 이 난수 생성기 시퀀스에서 생성된 `0.0`과 
 `1.0` 사이의 균일하게 분산된 다음 
 의사 난수 `float` 값

**Since:**
- CLDC 1.1

### nextDouble

```java
public double nextDouble()
```

**Returns:**
- 이 난수 생성기 시퀀스에서 생성된 
 `0.0`과 `1.0` 사이의 균일하게 
 분산된 다음 의사 난수 `double` 값

**Since:**
- CLDC 1.1

## 메서드 상세

### setSeed

```java
public void setSeed(long seed)
```

**Parameters:**
- `seed` - 초기 시드

### next

```java
protected int next(int bits)
```

**Parameters:**
- `bits` - 임의 비트

**Returns:**
- 난수 생성기 시퀀스에서 다음 의사 난수 값

### nextInt

```java
public int nextInt()
```

**Returns:**
- 이 난수 생성기 시퀀스에서 균일하게 분산된 다음 의사 난수 
 `int` 값

### nextInt

```java
public int nextInt(int n)
```

**Parameters:**
- `n` - 반환되는 난수의 범위. 
 양수여야 합니다.

**Returns:**
- 0(포함)과 n(포함하지 않음) 사이의 균일하게 분산된 의사 난수 
 `int` 값

**Throws:**
- `IllegalArgumentException` - n이 양수가 아닐 경우

**Since:**
- CLDC 1.1

### nextLong

```java
public long nextLong()
```

**Returns:**
- 이 난수 생성기 시퀀스에서 균일하게 분산된 다음 
 의사 난수 `long` 값

### nextFloat

```java
public float nextFloat()
```

**Returns:**
- 이 난수 생성기 시퀀스에서 생성된 `0.0`과 
 `1.0` 사이의 균일하게 분산된 다음 
 의사 난수 `float` 값

**Since:**
- CLDC 1.1

### nextDouble

```java
public double nextDouble()
```

**Returns:**
- 이 난수 생성기 시퀀스에서 생성된 
 `0.0`과 `1.0` 사이의 균일하게 
 분산된 다음 의사 난수 `double` 값

**Since:**
- CLDC 1.1
