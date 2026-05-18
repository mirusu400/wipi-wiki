# 4.10. UTILITY

플랫폼에서 유용하게 사용할 수 있는 함수들을 제공한다. 문자셋을 변환한다.

### MH_utilConvertLocalCodeToUnicode

**설명**

내부 로컬 코드 문자열을 유니코드 문자열로 변환한다. 변환 도중에 변환할 수 없는 문자를 만나면 Space(0x20)로 변경한다.

**프로토타입**

```c
M_Int32 MH_utilConvertLocalCodesToUnicodes (M_Char *psz, int len, M_Uint16 *puni, int buflen)
```

**매개 변수**

- `psz` - [in] 내부 “C” 문자열 (로컬 코드로 되어 있는 문자열; 한국의 경우 EUC_KR임)
- `len` - [in] 문자열의 길이
- `puni` - [out] 변환된 “Unicode” 문자열이 복사될 버퍼
- `buflen` - [in] 버퍼의 길이

**반환 값**

성공

- 변환된 유니코드 문자열 길이

실패

- `M_E_SHORTBUF` - puni버퍼가 충분하지 않은 경우

**부작용**

없음 

**참고항목**

없음

### MH_utilConvertUnicodeToLocalCode

**설명**

유니 코드 문자열을 내부 로컬 코드 문자열로 변환한다. 유니 코드가 내부 로컬 코드 문자열에 대응되지 않는 경우에는 0x20(Space)으로 변환한다.

**프로토타입**

```c
M_Int32 MH_utilConvertUnicodeToLocalCode(M_Uint16 *puni, M_Int32 len, M_Uint8 *plocal, M_Int32 buflen);
```

**매개 변수**

- `puni` - [in]  “Unicode” 문자열
- `len` - [in] 문자열의 길이
- `plocal` - [out] 변환된 “C” 문자열이 복사될 버퍼(로컬 코드로 되어 있는 문자열; 한국의 경우 EUC_KR임)
- `buflen` - [in] 버퍼의 길이

**반환 값**

성공

- 변환된 로컬 코드 문자열 길이

실패

- `M_E_SHORTBUF` - plocal버퍼가 충분하지 않은 경우

**부작용**

없음

**참고항목**

없음

### MH_utilUnConvertLocalCodeToUnicodeChar

**설명**

내부 로컬 코드 버퍼를 유니코드로 변환할 때 첫번째 변환되는 유니코드와 첫 유니코드 변환시 사용된 로컬 코드 개수를 반환한다.

**프로토타입**

```c
M_UInt16 MH_utilConvertLocalCodeToUnicodeChar(M_Uint8 *psz, M_Int32 len, M_Int32 *pconsumed);
```

**매개 변수**

- `psz` - [in] 로컬 코드 문자 버퍼
- `len` - [in] 로컬 코드 문자 버퍼의 길이
- `pconsumed` - [out] 첫 유니코드로 만들기 위해서 사용된 로컬 코드 개수.

**반환 값**

변환된 Unicode

**부작용**

없음

**참고항목**

없음


### MH_utilGetLocalCodeSizeInUnicode

**설명**

유니코드 문자 버퍼를 내부 코드 문자 버퍼로 변경할 때 내부 코드 문자 버퍼의 크기를 바이트 단위로 돌려준다.

**프로토타입**

```c
M_UInt32 MH_utilLocalCodeSizeToUnicodeChar(M_Uint16 *psz, M_Int32 len);
```

**매개 변수**

- `psz` - [in] 유니코드 문자 버퍼
- `len` - [in] 유니코드의 문자 버퍼 크기(단위:M_Uint16)

**반환 값**

변환시에 필요로 하는 내부 코드 문자 버퍼의 크기(단위: 바이트)

**부작용**

없음

### 참고항목

없음

### MH_utilGetUnicodeSizeInLocalCode 설명

내부 로컬 코드 문자 버퍼을 유니코드 문자 버퍼 변환할 때 유니코드 문자 버퍼 크기를 M_Uint16 단위로 돌려준다.

**프로토타입**

```c
M_UInt32 MH_utilGetUnicodeSizeInLocalCode (M_Uint8 *psz, M_Int32 len);
```

**매개 변수**

- `psz` - [in]  로컬 코드 문자 버퍼
- `len` - [in] 로컬 코드 문자 버퍼 길이

**반환 값**

변환시에 필요로 하는 유니코드 문자 버퍼 크기(단위:M_Uint16)

**부작용**

없음

**참고항목**

없음
