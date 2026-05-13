# Class WeakReference

`package java.lang.ref`

```
java.lang.Object
  |
  +--java.lang.ref.Reference
        |
        +--java.lang.ref.WeakReference
```

## 설명

**extends Reference:**

이 클래스는 약한 참조를 지원합니다. 
약한 참조는 주로 표준 매핑을 구현하는 데 사용됩니다. 

가비지 컬렉터는 특정 시점에서 
객체 접근 가능성이 약하다고 판단하는 경우, 
해당 객체에 대한 약한 참조와, 
강하고 약한 참조 체인을 통해 
해당 객체에 접근 가능한 접근 가능성이 약한 다른 
모든 객체에 대한 약한 참조를 자동으로 모두 제거합니다.

**Since:**
- JDK1.2, CLDC 1.1

## 생성자 요약

- WeakReference ( Object ref) 지정된 객체를 참조하는 새로운 약한 참조를 만듭니다.

## 생성자 상세

### WeakReference

```java
public WeakReference(Object ref)
```

- 지정된 객체를 참조하는 새로운 약한 참조를 만듭니다.
