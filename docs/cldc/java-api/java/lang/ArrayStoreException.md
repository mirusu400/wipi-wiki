# Class ArrayStoreException

`package java.lang`

```
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.lang.RuntimeException
                    |
                    +--java.lang.ArrayStoreException
```

## 설명

**extends RuntimeException:**

잘못된 유형의 객체를 객체 배열에 저장하려고 시도했음을 
나타냅니다. 예를 들어, 
다음 코드는 `ArrayStoreException`을 생성합니다.

**Since:**
- JDK1.0, CLDC 1.0

## 생성자 요약

- ArrayStoreException () 세부 정보 메시지 없이 ArrayStoreException 을 구성합니다.
- ArrayStoreException ( String s) 지정한 세부 정보 메시지를 사용하여 ArrayStoreException 을 
구성합니다.

## 생성자 상세

### ArrayStoreException

```java
public ArrayStoreException()
```

- 세부 정보 메시지 없이 `ArrayStoreException`을 구성합니다.

### ArrayStoreException

```java
public ArrayStoreException(String s)
```

- 지정한 세부 정보 메시지를 사용하여 `ArrayStoreException`을 
구성합니다.

**Parameters:**
- `s` - 세부 정보 메시지
