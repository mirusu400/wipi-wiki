---
title: "2.14. 위치정보 API"
---

위치정보 API 는 GPS 정보와 기지국 위치 정보를 동시에 포괄하고 있는 API 이다.

## 2.14.1. 기지국 위치정보 API

단말이 통신중인 기지국의 위치정보를 돌려주는 API 가 준비되어 있다.

### MC_lbsGetStationLocationInfo

```c
M_Int32 MC_lbsGetStationLocationInfo(M_Int32 *baseID, M_Int32 *baseLat,
M_Int32 *baseLong)
```

단말이 통신중인 기지국의 위치 정보를 요청하는 API 이다.

**매개 변수**

- `baseID` - [out] 기지국 ID
- `baseLat` - [out] 기지국의 위도 정보
- `baseLong` - [out] 기지국의 경도 정보

**반환 값**

성공

실패

`M_E_ERROR`

**부작용**

없음

**참고 항목**

없음

## 2.14.2. GPS 위치정보 API

GPS 관련 API 들은 퀄컴의 gpsOne 솔루션의 단말기들을 대상으로 준비된 것이며 GSM 계열이나 일반 GPS 장치에 대한 것은 아니다. gpsOne 에서는 이동통신사에 준비된 gpsOne 관련 서버에 IS801-1 프로토콜을 사용해서 접속해서 위치 정보를 전 달 받도록 되어 있으며, 본 절의 C API 들 또한 그러한 시나리오에 맞게 준비되어 있다.

#### EVENT

GPS API 를 위해 `MH_GPS_EVENT` 라는 EVENT 가 정의 되었으며 param1 에 `MH_GPSEvent` 구조체의 포인터가 전달 된다. 그 구조체에 담긴 값은 다음과 같이 정의 되어 있다.

```c
typedef enum MH_GPSSubEvent {
    MH_GPSEV_SUCCESS=0x01, // GPS 정보 수신 성공
    MH_GPSEV_FAILED, // GPS 정보 수신 실패
    MH_GPSEV_NOTAVAILABLE, // GPS 장치 없음
    MH_GPSEV_NOTACKNOWLEDGED // GPS 인증 실패
} MH_GPSSubEvent;
```

상기 sub event 는 다음 구조체를 통해 전달 되어야 한다.

```c
typedef struct MH_GPSEvent{
    MH_GPSSubEvent event; //발생된 GPS event,
} MH_GPSEvent ;
```

#### Global structure

GPS API 를 위해 다음과 같이 구조체가 정의 되어야 한다.

```c
typedef struct MC_gpsConfig {
    M_Uint8 mode;
    M_Uint8 optimization;
    M_Uint8 qos;
    M_Uint16 transport;
    M_Uint32 pde_addr;
    M_Uint16 pde_port;
} MC_gpsConfig;
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
typedef struct MC_locationInfo {
    M_Int32 latitude;
    M_Int32 longitude;
    M_Int16 altitude;
    M_Uint16 heading;
    M_Uint16 velocityHor;
    M_Int8 velocityVer;
    M_Int8 accuracy;
    M_Char* timeString;
} MC_locationInfo;
typedef enum MC_gpsCfgMask {
    MC_GPSCFG_OPTI=0x1, // gpsOne™ 동작 최적화 방식 적용
    MC_GPSCFG_QOS=0x2, // gpsOne™ 품질 수준 적용
    MC_GPSCFG_TRANSPORT=0x4, // gpsOne™ 정보 전송 계층 적용
    MC_GPSCFG_SVRADDR=0x8, // PDE 서버 주소값 적용
    MC_GPSCFG_SVRPORT=0x10 // PDE 접속 포트 값 적용
    MC_GPSCFG_ALL=0xFFFF, // 모든 구성정보 설정
} MC_gpsCfgMask;
```

#### Return Value

GPS API 의 return 값을 위해 다음과 같이 구조체가 정의 되어야 한다.

```c
typedef enum MC_gpsRet {
    MC_GPSRET_OK=0, // 성공
    MC_GPSRET_PARAMINVALID=-1, // parameter 가 invalid
    MC_GPSRET_NODEVICE=-2, // GPS 기능 없음
    MC_GPSRET_UNAVAILABLE=-3, // 현재 사용 중
    MC_GPSRET_NOTACKED=-4, // 인증 실패
    MC_GPSRET_CANNOTCONNECT=-5, //서버 접속이 안됨
    MC_GPSRET_NOTREQUESTED=-6, // 요청한 적 없음
    MC_GPSRET_PROCESSING=-7, // 통신 중
    MC_GPSERR_TIMEOUT=-8, // 못받고 timeout
    MC_GPSRET_FAILED=-9 // 기타 사유로 실패
} MC_gpsRet
```

### MC_gpsAvailable

`MC_gpsRet` `MC_gpsAvailable`(void) gpsOne 장치가 있는지 확인한다.

**매개 변수**

없음

**반환 값**

성공

`MC_GPSRET_OK` 장치 사용 가능힘
실패

`MC_GPSRET_NODEVICE` 장치 없음 `MC_GPSRET_UNAVAILABLE` 현재 다른 app 가 사용 중

**부작용**

없음

**참고 항목**

없음

### MC_gpsRequestLocationInfo

`MC_gpsRet` `MC_gpsRequestLocationInfo`(`M_Int32` repeat) gpsOne 에 의한 위치 정보를 요청하는 API 이다. 이 API 는 asynchronous 하게 동 작하며, 그 결과는 EVENT 로 통보될 것이고, `MC_gpsGetResult()` 에 의해서 상세 정 보를 얻어낼 수 있다.

**매개 변수**

- `repeat` - [in] -1 시 전송 정지, 0 일때 한번 요청, 1보다 클 때 매 repeat 초 마다 보고(가능한한)

**반환 값**

성공

`MC_GPSRET_OK`
실패

`MC_GPSRET_PARAMINVALID` parameter 가 invalid `MC_GPSRET_NODEVICE` GPS 기능 없음 `MC_GPSRET_UNAVAILABLE` 현재 다른 app 가 사용 중 `MC_GPSRET_NOTACKED` 인증 실패 `MC_GPSRET_CANNOTCONNECT` 서버 접속이 안됨

**부작용**

없음

**참고 항목**

없음

### MC_gpsGetResult

`MC_gpsRet` `MC_gpsGetResult`(`MC_locationInfo`* pInfo) return 값이 success 일 때 pInfo 에 위치 정보 결과가 담겨서 돌아와야 한다.

**매개 변수**

- `pInfo` - [out] `MC_locationInfo` 구조체에 의한 위치 정보

**반환 값**

성공

`MC_GPSRET_OK`
실패

`MC_GPSRET_PARAMINVALID` parameter 가 invalid `MC_GPSRET_NODEVICE` GPS 기능 없음 `MC_GPSRET_UNAVAILABLE` 현재 다른 app 가 사용 중 `MC_GPSRET_NOTACKED` 인증 실패 `MC_GPSRET_CANNOTCONNECT` 서버 접속이 안됨 `MC_GPSRET_NOTREQUESTED` 요청한 적 없음 `MC_GPSRET_PROCESSING` 통신 중 `MC_GPSRET_TIMEOUT` 못받고 timeout `MC_GPSRET_FAILED` 기타 사유로 전송 실패

**부작용**

없음

**참고 항목**

없음

### MC_gpsGetConfig

```c
M_Int32 MC_gpsGetConfig(MC_gpsConfig *config)
gpsOne™ 설정정보를 얻어올 수 있다.
```

**매개 변수**

- `config` - [out] : 단말기의 gpsOne™ 설정정보를 수신할 구조체의 포인터

**반환 값**

성공

실패

`M_E_ERROR`

**부작용**

없음

**참고 항목**

없음.

### MC_gpsSetConfig

```c
M_Int32 MC_gpsSetConfig(MC_gpsConfig *config, MC_gpsCfgMask mask)
gpsOne™ 정보를 설정한다.
```

**매개 변수**

- `config` - [in] : 설정할 구성정보를 포함하는 구조체의 포인터
- `mask` - [in] : 구조체 내용중의 적용대상 항목 마스크

**반환 값**

성공

실패

`M_E_ERROR`

**부작용**

없음

**참고 항목**

없음

### MC_gpsControl

```c
M_Int32 MC_gpsControl(M_Int32 function, M_Int32 command, void*
argument)
```

추후 확장을 위해서 준비된 API 로 현 버전의 규격서에는 어떠한 function 도 정의되 어 있지 않으므로 무조건 `M_E_ERROR` 을 return 해야 한다.

**매개 변수**

- `function` - [in] : 확장 기능 종류
- `command` - [in] : 확장 기능에 대한 명령 종류
- `argument` - [in] : 명령에 대한 인자의 구조체에 대한 포인터

**반환 값**

성공

실패

`M_E_ERROR`

**부작용**

없음

**참고 항목**

없음
