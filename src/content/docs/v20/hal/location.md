---
title: "2.19. 위치정보"
---

위치정보 API 는 GPS 정보와 기지국 위치 정보를 동시에 포괄하고 있는 API 이나 HAL 에서는 기지국 위치 정보를 system property 를 통해서 가져올 수 있기 때문에 GPS 에 대한 HAL API 만이 필요하다. GPS 관련 API 들은 Qualcomm, Inc. 의 gpsOne™ 솔루션의 단말기들을 대상으로 준비된 것이며 GSM 계열이나 일반 GPS 장치에 대한 것은 아니다.

## 2.19.1. EVENT

위치정보 HAL API 를 위해 `MH_GPS_EVENT` 라는 EVENT 를 하나 추가로 정 의해야 하며, 그 argument 로는 `MH_GPSEvent` 구조체가 전달 되어야 한다. 플랫폼은 단말로부터 이 `MH_GPS_EVENT` 를 전달 받았을 경우, 이 EVENT 를 GPS 정보를 요청했던 application 에 전달 해서 GPS 관련 결과가 왔음을 알려 야 한다. 플랫폼은 GPS 관련 요청을 복수의 application 이 겹쳐서 요청할 수 있도록 허 용해서는 안되고, 항상 하나의 요청만이 존재하도록 제어해야 한다. 발생된 event 는 다음 과 같은 값을 가진다

```c
typedef enum MH_GPSSubEvent {
    MH_GPSEV_SUCCESS=0x01, // GPS 정보 수신 성공
    MH_GPSEV_FAILED, // GPS 정보 수신 실패
    MH_GPSEV_NOTAVAILABLE // GPS 장치 없음
    MH_GPSEV_NOTACKNOWLEDGED // GPS 인증 실패
} MH_GPSSubEvent;
```

상기 sub event 는 다음 구조체를 통해 전달 된다.

```c
typedef struct MH_GPSEvent{
    MH_GPSSubEvent event; //발생된 GPS event,
} MH_GPSEvent ;
```

## 2.19.2. Global structure

위치정보 HAL API 를 위해 다음과 같이 구조체가 정의 되어야 한다.

```c
typedef struct MH_gpsConfig {
    M_Uint8 mode;
    M_Uint8 optimization;
    M_Uint8 qos;
    M_Uint16 transport;
    M_Uint32 pde_addr;
    M_Uint16 pde_port;
} MH_gpsConfig;
typedef enum MH_gpsOptimization {
    OPT_SPEED=0x1;
    OPT_ACCURACY=0x2;
}
typedef enum MH_gpsTransport {
    SERVER_TCPIP=0x1;
    SERVER_DBURST=0x2;
}
typedef enum MH_gpsTransport {
    MS_ASSISTED=0x1;
    MS_BASED =0x2;
}
typedef struct MH_locationInfo {
    M_Int32 latitude;
    M_Int32 longitude;
    M_Int16 altitude;
    M_Uint16 heading;
    M_Uint16 velocityHor;
    M_Int8 velocityVer;
    M_Int8 accuracy;
    M_Char* timeString;
} MH_locationInfo;
typedef enum MH_gpsCfgMask {
    MH_GPSCFG_OPTI=0x1, // gpsOne™ 동작 최적화 방식 적용
    MH_GPSCFG_QOS=0x2, // gpsOne™ 품질 수준 적용
    MH_GPSCFG_TRANSPORT=0x4, // gpsOne™ 정보 전송 계층 적용
    MH_GPSCFG_SVRADDR=0x8, // PDE 서버 주소값 적용
    MH_GPSCFG_SVRPORT=0x10 // PDE 접속 포트 값 적용
    MH_GPSCFG_ALL=0xFFFF, // 모든 구성정보 설정
} MH_gpsCfgMask;
```

## 2.19.3. Return Value

위치정보 HAL API 를 위해 다음과 같이 return value 가 정의 되어야 한다.

```c
typedef enum MH_gpsRet {
    MH_GPSRET_OK=0, // 성공
    MH_GPSRET_PARAMINVALID=-1, // parameter 가 invalid
    MH_GPSRET_NODEVICE=-2, //GPS 기능 없음
    MH_GPSRET_UNAVAILABLE=-3, // 현재 사용 중
    MH_GPSRET_NOTACKED=-4, // 인증 실패
    MH_GPSRET_CANNOTCONNECT=-5, //서버 접속이 안됨
    MH_GPSRET_NOTREQUESTED=-6, // 요청한 적 없음
    MH_GPSRET_PROCESSING=-7, // 통신 중
    MH_GPSERR_TIMEOUT=-8, // 못받고 timeout
    MH_GPSRET_FAILED=-9 // 기타 사유로 실패
} MH_gpsRet
```

### MH_gpsAvailable

```c
M_Int32 MH_gpsAvailable(void)
```

**설명**

gpsOne 장치가 있는지 문의하는 API 이다

**매개 변수**

없음

**반환 값**

성공

- 0 장치 사용 가능힘
실패

- `M_E_ERROR` - 장치 없음

**부작용**

없음

**참고 항목**

없음.

### MH_gpsRequestLocationInfo

`MH_gpsRet` `MH_gpsRequestLocationInfo`(`M_Int32` repeat)

**설명**

gpsOne 에 의한 위치 정보를 요청하는 API 이다. 이 API 는 asynchronous 하게 동 작하며, 그 결과는 EVENT 로 통보될 것이고, `MH_gpsGetResult()` 에 의해서 상세 정 보를 얻어낼 수 있다.

**매개 변수**

- `repeat` - [in] -1 시 전송 정지, 0 일때 한번 요청, 1보다 클 때 매 repeat 초마다 보고(가능한한)

**반환 값**

성공

`MH_GPSRET_OK`
실패

`MH_GPSRET_PARAMINVALID` parameter 가 invalid `MH_GPSRET_NODEVICE` GPS 기능 없음 `MH_GPSRET_UNAVAILABLE` 현재 사용 중 `MH_GPSRET_NOTACKED` 인증 실패 `MH_GPSRET_CANNOTCONNECT` 서버 접속이 안됨

**부작용**

없음

**참고 항목**

없음

### MH_gpsGetResult

`MH_gpsRet` `MH_gpsGetResult`(`MH_locationInfo`* pInfo)

**설명**

return 값이 success 일 때 pInfo 에 위치 정보 결과가 담겨서 돌아와야 한다.

**매개 변수**

- `pInfo` - [out] `MH_locationInfo` 구조체에 의한 위치 정보

**반환 값**

성공

`MH_GPSRET_OK`
실패

`MH_GPSRET_PARAMINVALID` parameter 가 invalid `MH_GPSRET_NODEVICE` GPS 기능 없음 `MH_GPSRET_UNAVAILABLE` 현재 사용 중 `MH_GPSRET_NOTACKED` 인증 실패 `MH_GPSRET_CANNOTCONNECT` 서버 접속이 안됨 `MH_GPSRET_NOTREQUESTED` 요청한 적 없음 `MH_GPSRET_PROCESSING` 통신 중 `MH_GPSRET_TIMEOUT` 못받고 timeout `MH_GPSRET_FAILED` 기타 사유로 전송 실패

**부작용**

없음

**참고 항목**

없음

### MH_gpsGetConfig

```c
M_Int32 MH_gpsGetConfig(MH_gpsConfig *config)
```

**설명**

gpsOne™ 설정정보를 얻어올 수 있다.

**매개 변수**

- `config` - [out] 단말기의 gpsOne™ 설정정보를 수신할 구조체의 포인터

**반환 값**

성공

- 0 정보 획득 성공
실패

- `M_E_ERROR` - 정보 획득 실패

**부작용**

없음

**참고 항목**

없음

### MH_gpsSetConfig

```c
M_Int32 MH_gpsSetConfig(MH_gpsConfig *config, MH_gpsCfgMask
mask)
```

**설명**

gpsOne™ 정보를 설정한다.

**매개 변수**

- `config` - [in] 설정할 구성정보를 포함하는 구조체의 포인터
- `mask` - [in] 구조체 내용중의 적용대상 항목 마스크

**반환 값**

성공

- 0 설정 성공
실패

- `M_E_ERROR` - 설정 실패

**부작용**

없음

**참고 항목**

없음

### MH_gpsControl

```c
M_Int32 MH_gpsControl(M_Int32 function, M_Int32 command, void*
argument)
```

**설명**

추후 확장을 위해서 준비된 API 로 현 버전의 규격서에는 어떠한 function 도 정의되 어 있지 않으므로 무조건 `M_E_ERROR` 을 return 해야 한다.

**매개 변수**

- `function` - [in] 확장 기능 종류
- `command` - [in] 확장 기능에 대한 명령 종류
- `argument` - [in] 명령에 대한 인자의 구조체에 대한 포인터

**반환 값**

성공

실패

`M_E_ERROR`

**부작용**

없음

**참고 항목**

없음
