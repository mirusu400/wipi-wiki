---
title: "2.8. 유틸리티"
---

각종 유틸리티 함수를 정의하였다.

### MC_utilHtonl

**프로토타입**

```c
M_Int32 MC_utilHtonl(M_Int32 val)
```

**설명**


```c
M_Int32 타입의 값의 Host Byte Ordering 을 Network Byte Ordering 으로 전환한다.
```

**반환 값**

정수 값

**부작용**

없음

**참고 항목**

없음

### MC_utilHtons

**프로토타입**

```c
M_Int16 MC_utilHtons(M_Int16 val)
```

**설명**


```c
M_Int16 타입의 값의 Host Byte Ordering 을 Network Byte Ordering 으로 전환한다.
```

**반환 값**

정수 값

**부작용**

없음

**참고 항목**

없음

### MC_utilNtohl

**프로토타입**

```c
M_Int32 MC_utilNtohl(M_Int32 val)
```

**설명**


```c
M_Int32 타입의 값의 Network Byte Ordering 을 Host Byte Ordering 으로 전환한다.
```

**반환 값**

정수 값

**부작용**

없음

**참고 항목**

없음

### MC_utilNtohs

**프로토타입**

```c
M_Int16 MC_utilNtohs(M_Int16 val)
```

**설명**


```c
M_Int16 타입의 값의 Network Byte Ordering 을 Host Byte Ordering 으로 전환한다.
```

**반환 값**

정수 값

**부작용**

없음

**참고 항목**

없음

### MC_utilInetAddrInt

**프로토타입**

```c
M_int32 MC_utilInetAddrInt(M_Byte* addr)
```

**설명**

문자열로 된 IP 주소로부터 정수형의 IP 값을 얻다. 반환되는 IP 값은 Network Byte Ordering 이다.

**반환 값**

성공

Network Byte Order의 IP값
실패

`M_E_ERROR`

**부작용**

없음

**참고 항목**

없음

### MC_utilInetAddrStr

**프로토타입**

```c
void MC_utilInetAddrStr(M_Int32 ip, M_Byte* addr)
```

**설명**

정수형의 IP 값으로부터 IP 문자열을 얻다. 정수형 값은 Network Byte Ordering 이어 야 한다.

**매개 변수**

- `ip` - 정수형의 IP 주소
- `addr` - IP 문자열이 저장될 버퍼

**부작용**

없음

**참고 항목**

없음
