---
title: "2.12. 전화걸기"
---

전화 걸기에 관한 API 를 모은 것이다. 전화를 걸 때는 전화번호 문자열을 넘겨 `MC_phnCallPlace`()를 호출한다.

### MC_phnCallPlace

**프로토타입**

```c
M_Int32 MC_phnCallPlace(M_Byte* phonenumber)
```

**설명**

전화를 건다.

**매개 변수**

- `phonenumber` - 전화번호 문자열(마지막은 `NULL`)

**반환 값**

성공

실패

`M_E_ERROR`(전화를 걸 수 없음)

**부작용**

없음

**참고 항목**

없음
