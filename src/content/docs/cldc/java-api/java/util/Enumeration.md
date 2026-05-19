---
title: "Interface Enumeration"
---

`package java.util`

```text
     for (Enumeration e = v.elements() ; e.hasMoreElements() ;) {
         System.out.println(e.nextElement());
     }
```

## 메서드 요약

- `boolean hasMoreElements ()` — 이 열거에 추가 요소가 있는지 테스트합니다.
- `Object nextElement ()` — 이 열거 객체에 제공할 추가 요소가 최소 하나 이상 있으면 열거의 다음 요소를 반환합니다.

## 메서드 상세

### hasMoreElements

```java
public boolean hasMoreElements()
```

**Returns:**
- 이 열거 객체에 제공할 추가 요소가 최소 하나 이상 있으면
 `true`,
 그렇지 않으면 `false`

### nextElement

```java
public Object nextElement()
```

**Returns:**
- 이 열거의 다음 요소

**Throws:**
- `NoSuchElementException` - 추가 요소가 없는 경우
