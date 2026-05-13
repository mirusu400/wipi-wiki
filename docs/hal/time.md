# 4.9. TIME

플랫폼은 HAL 에서 제공하는 1 개의 Timer 를 가지고 내부적으로 여러 개의 타이머 를 생성하여 사용한다. 그리고, HAL 은 UTC 기준시간 70 년 1 월 1 일 0 시 0 분 0 초 부터 현재시간까지의 milli-second 단위의 시간을 알려준다.

```c
MH_timerSet
```

**설명**

타이머를 설정한다.

타이머가 만료되면 HAL 은 플랫폼에 MH_TIMER_EVENT 를 전달해야 한다. 타이머가 만료되기 전에 다시 MH_timerSet()이 불린다면 이전에 설정된 타이머는 해제되고, 새로 설정된 타이머가 동작해야 한다.

**프로토타입**

```c
void MH_timerSet (M_Int64 timeout)
```

**매개 변수**

[in]	timeout	milli-second 단위, 64bit

**반환 값**

없음

**부작용**

없음

참고항목

없음

```c
MH_timerClear 설명
```

설정된 타이머를 해제한다.

**프로토타입**

```c
void MH_timerClear (void)
```

**매개 변수**

없음

**반환 값**

없음

**부작용**

참고항목

```c
MH_timerSet
MH_timerCurrentTime 설명
```

현재 시간을 얻어 온다.

**프로토타입**

```c
M_Int64 MH_timerCurrentTime (void)
```

**매개 변수**

없음

**반환 값**

UTC 기준시간 70 년 1 월 1 일 0 시 0 분 0 초부터 현재시간까지의 milli-second 단 위의 시간 이다.

**부작용**

없음

### 참고항목

없음
