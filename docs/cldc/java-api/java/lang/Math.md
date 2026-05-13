# Class Math

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Math
```

## 설명

**extends Object:**

`Math` 클래스에는 기본 수식 작업을 수행하기 위한 
메소드가 포함되어 있습니다.

**Since:**
- JDK1.0, CLDC 1.0

## 필드 요약

- `static double E` — 자연 로그의 기수인 e 에 가장 가까운 double 값
- `static double PI` — 원주와 지름의 비율인 pi 에 가장 가까운 double 값

## 메서드 요약

- `static double abs (double a)` — double 값의 절대값을 반환합니다.
- `static float abs (float a)` — float 값의 절대값을 반환합니다.
- `static int abs (int a)` — int 값의 절대값을 반환합니다.
- `static long abs (long a)` — long 값의 절대값을 반환합니다.
- `static double ceil (double a)` — 인자보다 작지 않고 연산 정수와 같은 가장 작은(음의 무한대에 가장 가까운) double 값을 반환합니다.
- `static double cos (double a)` — 각도의 삼각 코사인을 반환합니다.
- `static double floor (double a)` — 인자보다 크지 않고 연산 정수와 같은 가장 큰(양의 무한대에 가장 가까운) double 값을 반환합니다.
- `static double max (double a, double b)` — 두 double 값 중에서 큰 값을 반환합니다.
- `static float max (float a, float b)` — 두 float 값 중에서 큰 값을 반환합니다.
- `static int max (int a, int b)` — 두 int 값 중에서 큰 값을 반환합니다.
- `static long max (long a, long b)` — 두 long 값 중에서 큰 값을 반환합니다.
- `static double min (double a, double b)` — 두 double 값 중에서 작은 값을 반환합니다.
- `static float min (float a, float b)` — 두 float 값 중에서 작은 값을 반환합니다.
- `static int min (int a, int b)` — 두 int 값 중에서 작은 값을 반환합니다.
- `static long min (long a, long b)` — 두 long 값 중에서 작은 값을 반환합니다.
- `static double sin (double a)` — 각도의 삼각 사인을 반환합니다.
- `static double sqrt (double a)` — double 값을 올바로 반올림한 양의 제곱근을 반환합니다.
- `static double tan (double a)` — 각도의 삼각 탄젠트를 반환합니다.
- `static double toDegrees (double angrad)` — 라디안 값을 해당 각도로 변환합니다.
- `static double toRadians (double angdeg)` — 각도를 해당 라디안 값으로 변환합니다.

## 필드 상세

### E

```java
public static final double E
```

**Since:**
- CLDC 1.1

**See Also:**
- `Constant Field Values`

### PI

```java
public static final double PI
```

**Since:**
- CLDC 1.1

**See Also:**
- `Constant Field Values`

### sin

```java
public static double sin(double a)
```

**Parameters:**
- `a` - 각도(라디안)

**Returns:**
- 인자의 사인

**Since:**
- CLDC 1.1

### cos

```java
public static double cos(double a)
```

**Parameters:**
- `a` - 각도(라디안)

**Returns:**
- 인자의 코사인

**Since:**
- CLDC 1.1

### tan

```java
public static double tan(double a)
```

**Parameters:**
- `a` - 각도(라디안)

**Returns:**
- 인자의 탄젠트

**Since:**
- CLDC 1.1

### toRadians

```java
public static double toRadians(double angdeg)
```

**Parameters:**
- `angdeg` - 각도(도)

**Returns:**
- `angdeg`에 해당하는 
 라디안 값

**Since:**
- CLDC 1.1

### toDegrees

```java
public static double toDegrees(double angrad)
```

**Parameters:**
- `angrad` - 각도(라디안)

**Returns:**
- `angrad`에 해당하는 
 각도

**Since:**
- CLDC 1.1

### sqrt

```java
public static double sqrt(double a)
```

**Parameters:**
- `a` - `double` 값

**Returns:**
- `a`의 양의 제곱근. 
 인자가 NaN이거나 0보다 작으면 결과 값은 NaN입니다.

**Since:**
- CLDC 1.1

### ceil

```java
public static double ceil(double a)
```

**Parameters:**
- `a` - `double` 값

**Returns:**
- 인자보다 작지 않고 연산 정수와 같은 
 가장 작은(음의 무한대에 가장 가까운) 
 `double` 값

**Since:**
- CLDC 1.1

### floor

```java
public static double floor(double a)
```

**Parameters:**
- `a` - `double` 값

**Returns:**
- 인자보다 크지 않고 연산 정수와 같은 
 가장 큰(양의 무한대에 가장 가까운) 
 `double` 값

**Since:**
- CLDC 1.1

### abs

```java
public static int abs(int a)
```

**Parameters:**
- `a` - `int` 값

**Returns:**
- 인자의 절대값

**See Also:**
- ``Integer.MIN_VALUE``

### abs

```java
public static long abs(long a)
```

**Parameters:**
- `a` - `long` 값

**Returns:**
- 인자의 절대값

**See Also:**
- ``Long.MIN_VALUE``

### abs

```java
public static float abs(float a)
```

**Parameters:**
- `a` - `float` 값

**Returns:**
- 인자의 절대값

**Since:**
- CLDC 1.1

### abs

```java
public static double abs(double a)
```

**Parameters:**
- `a` - `double` 값

**Returns:**
- 인자의 절대값

**Since:**
- CLDC 1.1

### max

```java
public static int max(int a,
                      int b)
```

**Parameters:**
- `b` - `int` 값

**Returns:**
- `a`와 `b` 중에서 큰 값

**See Also:**
- ``Long.MAX_VALUE``

### max

```java
public static long max(long a,
                       long b)
```

**Parameters:**
- `b` - `long` 값

**Returns:**
- `a`와 `b` 중에서 큰 값

**See Also:**
- ``Long.MAX_VALUE``

### max

```java
public static float max(float a,
                        float b)
```

**Parameters:**
- `b` - `float` 값

**Returns:**
- `a`와 `b` 중에서 큰 값

### max

```java
public static double max(double a,
                         double b)
```

**Parameters:**
- `b` - `double` 값

**Returns:**
- `a`와 `b` 중에서 큰 값

### min

```java
public static int min(int a,
                      int b)
```

**Parameters:**
- `b` - `int` 값

**Returns:**
- `a`와 `b` 중에서 작은 값

**See Also:**
- ``Long.MIN_VALUE``

### min

```java
public static long min(long a,
                       long b)
```

**Parameters:**
- `b` - `long` 값

**Returns:**
- `a`와 `b` 중에서 작은 값

**See Also:**
- ``Long.MIN_VALUE``

### min

```java
public static float min(float a,
                        float b)
```

**Parameters:**
- `b` - `float` 값

**Returns:**
- `a`와 `b` 중에서 작은 값

**Since:**
- CLDC 1.1

### min

```java
public static double min(double a,
                         double b)
```

**Parameters:**
- `b` - `double` 값

**Returns:**
- `a`와 `b` 중에서 작은 값

**Since:**
- CLDC 1.1

## 메서드 상세

### sin

```java
public static double sin(double a)
```

**Parameters:**
- `a` - 각도(라디안)

**Returns:**
- 인자의 사인

**Since:**
- CLDC 1.1

### cos

```java
public static double cos(double a)
```

**Parameters:**
- `a` - 각도(라디안)

**Returns:**
- 인자의 코사인

**Since:**
- CLDC 1.1

### tan

```java
public static double tan(double a)
```

**Parameters:**
- `a` - 각도(라디안)

**Returns:**
- 인자의 탄젠트

**Since:**
- CLDC 1.1

### toRadians

```java
public static double toRadians(double angdeg)
```

**Parameters:**
- `angdeg` - 각도(도)

**Returns:**
- `angdeg`에 해당하는 
 라디안 값

**Since:**
- CLDC 1.1

### toDegrees

```java
public static double toDegrees(double angrad)
```

**Parameters:**
- `angrad` - 각도(라디안)

**Returns:**
- `angrad`에 해당하는 
 각도

**Since:**
- CLDC 1.1

### sqrt

```java
public static double sqrt(double a)
```

**Parameters:**
- `a` - `double` 값

**Returns:**
- `a`의 양의 제곱근. 
 인자가 NaN이거나 0보다 작으면 결과 값은 NaN입니다.

**Since:**
- CLDC 1.1

### ceil

```java
public static double ceil(double a)
```

**Parameters:**
- `a` - `double` 값

**Returns:**
- 인자보다 작지 않고 연산 정수와 같은 
 가장 작은(음의 무한대에 가장 가까운) 
 `double` 값

**Since:**
- CLDC 1.1

### floor

```java
public static double floor(double a)
```

**Parameters:**
- `a` - `double` 값

**Returns:**
- 인자보다 크지 않고 연산 정수와 같은 
 가장 큰(양의 무한대에 가장 가까운) 
 `double` 값

**Since:**
- CLDC 1.1

### abs

```java
public static int abs(int a)
```

**Parameters:**
- `a` - `int` 값

**Returns:**
- 인자의 절대값

**See Also:**
- ``Integer.MIN_VALUE``

### abs

```java
public static long abs(long a)
```

**Parameters:**
- `a` - `long` 값

**Returns:**
- 인자의 절대값

**See Also:**
- ``Long.MIN_VALUE``

### abs

```java
public static float abs(float a)
```

**Parameters:**
- `a` - `float` 값

**Returns:**
- 인자의 절대값

**Since:**
- CLDC 1.1

### abs

```java
public static double abs(double a)
```

**Parameters:**
- `a` - `double` 값

**Returns:**
- 인자의 절대값

**Since:**
- CLDC 1.1

### max

```java
public static int max(int a,
                      int b)
```

**Parameters:**
- `b` - `int` 값

**Returns:**
- `a`와 `b` 중에서 큰 값

**See Also:**
- ``Long.MAX_VALUE``

### max

```java
public static long max(long a,
                       long b)
```

**Parameters:**
- `b` - `long` 값

**Returns:**
- `a`와 `b` 중에서 큰 값

**See Also:**
- ``Long.MAX_VALUE``

### max

```java
public static float max(float a,
                        float b)
```

**Parameters:**
- `b` - `float` 값

**Returns:**
- `a`와 `b` 중에서 큰 값

### max

```java
public static double max(double a,
                         double b)
```

**Parameters:**
- `b` - `double` 값

**Returns:**
- `a`와 `b` 중에서 큰 값

### min

```java
public static int min(int a,
                      int b)
```

**Parameters:**
- `b` - `int` 값

**Returns:**
- `a`와 `b` 중에서 작은 값

**See Also:**
- ``Long.MIN_VALUE``

### min

```java
public static long min(long a,
                       long b)
```

**Parameters:**
- `b` - `long` 값

**Returns:**
- `a`와 `b` 중에서 작은 값

**See Also:**
- ``Long.MIN_VALUE``

### min

```java
public static float min(float a,
                        float b)
```

**Parameters:**
- `b` - `float` 값

**Returns:**
- `a`와 `b` 중에서 작은 값

**Since:**
- CLDC 1.1

### min

```java
public static double min(double a,
                         double b)
```

**Parameters:**
- `b` - `double` 값

**Returns:**
- `a`와 `b` 중에서 작은 값

**Since:**
- CLDC 1.1
