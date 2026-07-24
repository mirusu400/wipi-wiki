---
title: "2.4. 타이머"
---

플랫폼은 HAL에서 제공하는 1개의 Timer를 가지고 내부적으로 여러 개의 타이머를 생 성하여 사용한다. 그리고, HAL은 UTC기준시간 70년 1월 1일 0시 0분 0초부터 현재시 간까지의 milli-second 단위의 시간을 알려준다.

### MH_timerSet

**프로토타입**

```c
void MH_timerSet (M_Int64 timeout)
```

**설명**

타이머를 설정한다. 타이머가 만료되면 HAL은 플랫폼에 MH_TIMER_EVENT를 전달해야 한다. 타이머가 만료되기 전에 다시 `MH_timerSet`()이 불린다면 이전에 설정된 타이머는 해제되고, 새 로 설정된 타이머가 동작해야 한다.

**매개 변수**

- `timeout` - [in] milli-second 단위, 64bit

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### MH_timerClear

**프로토타입**

```c
void MH_timerClear (void)
```

**설명**

설정된 타이머를 해제한다.

**매개 변수**

없음

**반환 값**

없음

**부작용**

없음

**참고 항목**

`MH_timerSet`

### MH_timerCurrentTime

**프로토타입**

```c
M_Int64 MH_timerCurrentTime (void)
```

**설명**

현재 시간을 얻어 온다.

**매개 변수**

없음

**반환 값**

UTC기준시간 70년 1월 1일 0시 0분 0초부터 현재시간까지의 milli-second 단위의 시간 이다.

**부작용**

없음

**참고 항목**

없음
