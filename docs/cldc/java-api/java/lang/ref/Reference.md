# Class Reference

`package java.lang.ref`

```text
java.lang.Object
  |
  +--java.lang.ref.Reference
```

## 설명

**Direct Known Subclasses:**
- `WeakReference`

**extends Object:**

참조 객체의 추상 기본 클래스. 
이 클래스는 모든 참조 객체에 공통적인 작업을 정의합니다. 
참조 객체는 가비지 컬렉터와 긴밀히 협력하도록 구현되기 때문에 
이 클래스의 서브 클래스를 직접 구성하지 못할 수도 있습니다.

**Since:**
- JDK1.2, CLDC 1.1

## 메서드 요약

- `void clear ()` — 이 참조 객체를 제거합니다.
- `Object get ()` — 이 참조 객체의 참조 대상을 반환합니다.

## 메서드 상세

### get

```java
public Object get()
```

**Returns:**
- 이 참조가 참조하는 객체 또는 참조 객체가 제거된 경우 
 `null`

### clear

```java
public void clear()
```

이 참조 객체를 제거합니다.
