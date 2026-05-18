# 5.1.10 UTILITY

각종 유틸리티 함수를 정의하였다.

### MC_utilHtonl

**설명**

M_Int32 타입의 값의 Host Byte Odering 을 Network Byte Odering 으로 전환한다.

**프로토타입**

```c
M_Int32 MC_utilHtonl(M_Int32 val)
```

**반환 값**

정수값

**부작용**

없음

**참고 항목**

없음

### MC_utilHtons

**설명**

M_Int16 타입의 값의 Host Byte Odering 을 Network Byte Odering 으로 전환한다.

**프로토타입**

```c
M_Int16 MC_utilHtons(M_Int16 val)
```

**반환 값**

정수값

**부작용**

없음

**참고 항목**

없음

### MC_utilNtohl

**설명**

M_Int32 타입의 값의 Network Byte Ordering 을 Host Byte Ordering 으로 전환한다.

**프로토타입**

```c
M_Int32 MC_utilNtohl(M_Int32 val)
```

**반환 값**

정수값

**부작용**

없음

**참고 항목**

없음

### MC_utilNtohs

**설명**

M_Int16 타입의 값의 Network Byte Ordering 을 Host Byte Ordering 으로 전환한다.

**프로토타입**

```c
M_Int16 MC_utilNtohs(M_Int16 val)
```

**반환 값**

정수값

**부작용**

없음

**참고 항목**

없음

### MC_utilInetAddrInt

**설명**

문자열로 된 IP 주소로 부터 정수형의 IP 값을 얻다. 리턴되는 IP 값은 Network Byte Ordering 이다.

**프로토타입**

```c
M_int32 MC_utilInetAddrInt(M_Byte* addr)
```

**반환 값**

성공

- `-1` 이 아닌 값

실패

- `-1`

**부작용**

없음

**참고 항목**

없음

### MC_utilInetAddrStr

**설명**

정수형의 IP 값으로 부터 IP 문자열을 얻다. 정수형 값은 Network Byte Ordering 이어야 한다.

**프로토타입**

```c
void MC_utilInetAddrStr(M_Int32 ip, M_Byte* addr)
```

**매개 변수**

- `ip` - 정수형의 IP 주소
- `addr` - IP 문자열이 저장될 버퍼

**부작용**

없음

**참고 항목**

없음