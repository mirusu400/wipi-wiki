# 5.1.10. UTILITY

플랫폼에서 유용하게 사용할 수 있는 함수들을 제공한다. 문자셋을 변환한다.

```c
MH_utilConvertLocalCodeToUnicode
```

**설명**

내부 로컬 코드 문자열을 유니코드 문자열로 변환한다. 변환 도중에 변환할 수 없 는 문자를 만나면 Space(0x20)로 변경한다.

**프로토타입**

```c
M_Int32 MH_utilConvertLocalCodesToUnicodes (M_Char *psz, int len, M_Uint16
*puni, int buflen)
```

**매개 변수**

[in] psz 내부 “C” 문자열(로컬 코드로 되어 있는 문자열; 한국의 경우 EUC_KR임) [in] len 문자열의 길이

[out] puni 변환된 “Unicode” 문자열이 복사될 버퍼 [in] buflen 버퍼의 길이

**반환 값**

```c
성공
실패
변환된 유니코드 문자열 길이
M_E_SHORTBUF - puni버퍼가 충분하지 않은 경우
```

**부작용**

없음 참고항목 없음

```c
MH_utilConvertUnicodeToLocalCode 설명
```

유니 코드 문자열을 내부 로컬 코드 문자열로 변환한다. 유니 코드가 내부 로컬 코드 문자열에 대응되지 않는 경우에는 0x20(Space)으로 변환한다.

**프로토타입**

```c
M_Int32	MH_utilConvertUnicodeToLocalCode(M_Uint16	*puni,	M_Int32	len, M_Uint8 *plocal, M_Int32 buflen);
```

**매개 변수**

[in] unicode 유니코드값

[in] puni “Unicode” 문자열 [in] len 문자열의 길이

[out] puni 변환된 “C” 문자열이 복사될 버퍼(로컬 코드로 되어 있는 문자열; 한 국의 경우 EUC_KR임)

[in] buflen 버퍼의 길이

**반환 값**

```c
성공
실패
변환된 로컬 코드 문자열 길이
M_E_SHORTBUF - plocal버퍼가 충분하지 않은 경우
```

**부작용**

없음

### 참고항목

없음

```c
MH_utilUnConvertLocalCodeToUnicodeChar 설명
```

내부 로컬 코드 버퍼를 유니코드로 변환할 때 첫번째 변환되는 유니코드와 첫 유 니코드 변환시 사용된 로컬 코드 개수를 반환한다.

**프로토타입**

```c
M_UInt16 MH_utilConvertLocalCodeToUnicodeChar(M_Uint8 *psz, M_Int32 len, M_Int32 *pconsumed);
```

**매개 변수**

[in] psz 로컬 코드 문자 버퍼

[in] len 로컬 코드 문자 버퍼의 길이

[out] pconsumed  첫 유니코드로 만들기 위해서 사용된 로컬 코드 개수.

**반환 값**

변환된 Unicode

**부작용**

없음

### 참고항목

없음

```c
MH_utilGetLocalCodeSizeInUnicode 설명
```

유니코드 문자 버퍼를 내부 코드 문자 버퍼로 변경할 때 내부 코드 문자 버퍼의 크기를 바이트 단위로 돌려준다.

**프로토타입**

```c
M_UInt32 MH_utilLocalCodeSizeToUnicodeChar(M_Uint16 *psz, M_Int32 len);
```

**매개 변수**

[in]	psz	유니 코드 문자 버퍼

[in] len 유니 코드의 문자 버퍼 크기(단위:M_Uint16)

**반환 값**

변환시에 필요로 하는 내부 코드 문자 버퍼의 크기(단위: 바이트)

**부작용**

없음

### 참고항목

없음

```c
MH_utilGetUnicodeSizeInLocalCode 설명
```

내부 로컬 코드 문자 버퍼을 유니코드 문자 버퍼 변환할 때 유니코드 문자 버퍼 크기를 M_Uint16 단위로 돌려준다.

**프로토타입**

```c
M_UInt32 MH_utilGetUnicodeSizeInLocalCode (M_Uint8 *psz, M_Int32 len);
```

**매개 변수**

[in] psz 로컬 코드 문자 버퍼 [in] len 로컬 코드 문자 버퍼 길이

**반환 값**

변환시에 필요로 하는 유니코드 문자 버퍼 크기(단위:M_Uint16)

**부작용**

없음

### 참고항목

없음

## FILE

File System 함수들이다.

모두 API 의 파일 path 는 절대 path 로 접근 된다. 파일 관련 함수는 모두 blocking 함수들이다. 파일식별자는 플랫폼에서 조사하여 HAL API 를 부르므로 HAL 에서 잘못된 식별자인지를 다시 조사할 필요는 없다.

관련 자료형

```c
#define MH_FILE_OPEN_RDONLY	0x1	// (O_RDONLY) #define MH_FILE_OPEN_WRONLY	 0x2	// (O_WRONLY|O_CREAT) #define MH_FILE_OPEN_WRTRUNC	 0x4	// (O_WRONLY|O_CREAT|O_TRUNC)
#define MH_FILE_OPEN_RDWR	0x8	// (O_RDWR|O_CREAT|O_BINARY) #define MH_FILE_SEEK_SET		0
#define MH_FILE_SEEK_CUR	1
#define MH_FILE_SEEK_END	2
#define MH_FILE_IS_DIR	0x01
typedef struct _fileInfo MH_FileInfo {
```

M_Int32 attrib	// 파일의 특성을 표시한 bit mask 들 (디렉토 리 여부, 읽기 전용)

M_Uint32 creationTime	// 파일이 생성된 시간을 초단위로 표현되며 지 역별 시간

M_Uint32 size	// 파일의 크기

```c
};
MH_fileAttribute
```

**설명**

파일이나 디렉터리의 특성을 읽어온다.

예를 들어 이 파일이 디렉터리 인지 파일인지, 만든 시간은 언제인지 등을 읽어온 다.

**프로토타입**

```c
M_Int32 MH_fileAttribute (M_Char* pathname, MH_FileInfo* fi)
```

**매개 변수**

[in]	pathname		파일이나 디렉터리의 절대 경로명 [out]	fi	파일의 특성을 담을 구조체

**반환 값**

성공 실패

M_E_BADFILENAME - 경로명 형식이 잘못된 경우

M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_ERROR - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음

```c
MH_fileAvailable 설명
```

파일 시스템의 여유공간을 알려준다.

**프로토타입**

```c
M_Int32 MH_fileAvailable (void)
```

**매개 변수**

없음

**반환 값**

성공 실패

시스템의 여유 공간의 바이트 단위의 크기를 반환한다. M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

```c
MH_fileClose 설명
```

파일을 닫는다.

**프로토타입**

```c
M_Int32 MH_fileClose (M_Int32 fd)
```

**매개 변수**

[in]	fd	파일 식별자

**반환 값**

성공 실패

```c
M_E_ERROR
```

**부작용**

없음

**참고 항목**

없음

```c
MH_fileList
```

**설명**

해당 디렉터리 내에 있는 파일과 하위 디렉터리를 보여준다. 파일과 디렉터리 이 름은 buf 에 NULL 문자 ('\0')로 구분되며 끝은 연속된 NULL 문자 두 개로 표시된 다.

**프로토타입**

```c
M_Int32 MH_fileList (M_Char *root, M_Char* buf, M_Int32 bufSize)
```

**매개 변수**

[in]	root	디렉터리 이름

[out]	buf	파일과 디렉터리 이름을 담을 버퍼

[in]	bufSize	buf 의 크기

**반환 값**

성공 실패

M_E_SHORTBUF - 버퍼 사이즈가 모자랄 경우 M_E_BADFILENAME - 파일이름 형식이 잘못된 경우 M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_ERROR - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음

```c
MH_fileMkDir 설명
```

디렉터리를 만든다.

**프로토타입**

```c
M_Int32 MH_fileMkDir (M_Char * dirname)
```

**매개 변수**

[in]	dirname	만들 디렉터리 절대 경로명

**반환 값**

성공 실패

M_E_BADFILENAME - 파일 이름 형식이 잘못된 경우 M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_NOENT - 만들고자 하는 디렉터리의 상위 디렉터리가 없을 경우 M_E_EXIST - 이미 디렉터리가 존재할 경우

M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

```c
MH_fileOpen 설명
```

파일을 연다.

flag 는 다음과 같은 값을 가질 수 있다.

flag

**설명**

```c
MH_FILE_OPEN_RDONLY
읽기 전용으로 파일을 연다.
MH_FILE_OPEN_WRONLY
쓰기 전용으로 파일을 쓰는 내용은 파일의 끝에 붙다.
MH_FILE_OPEN_WRTRUNC
쓰기 전용으로 파일을 열고 기존의 파일의 길이를 0으로 만든다.
MH_FILE_OPEN_RDWR
파일을 읽기 쓰기 모두 가능하도록 연다.
```

**프로토타입**

```c
M_Int32 MH_fileOpen (M_Char* pathname, M_Int32 flag)
```

**매개 변수**

[in]	pathname		파일의 절대 경로 [in]	flag	위 표 참조

**반환 값**

성공 실패

을 경우

file 식별자를 반환

M_E_NOENT - MH_FILE_OPEN_RDONLY 로 열 때 파일이 없을 경우 M_E_BADFILENAME - 파일이름 형식이 잘못되었을 경우

M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우

M_E_INVALID - 정해진 open option 이외의 option 이 parameter 로 들어왔

M_E_NOSPACE - 파일시스템에 여유 공간이 없을 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

```c
MH_fileRead 설명
```

파일에서 buf 로 크기만큼 읽어온다.

**프로토타입**

```c
M_Int32 MH_fileRead (M_Int32 fd, M_Char* buf, M_Int32 size)
```

**매개 변수**

[in]	fd	파일 식별자

[out]	buf	buffer pointer

[in]	size	buffer size

**반환 값**

성공

실패

읽은 바이트 수

Size 가 0 인 경우는 0 를 반환한다. 0 인 경우는 EOF 이다.

M_E_EOF - 파일의 끝까지 읽었을 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

```c
MH_fileRemove 설명
```

파일을 지운다. 이미 열려 있는 파일일 경우는 지울 수 없다.

**프로토타입**

```c
M_Int32 MH_fileRemove ( M_Char* pathname)
```

**매개 변수**

[in]	pathname	파일 절대 경로

**반환 값**

성공 실패

M_E_NOENT - 파일이 존재하지 않을 경우

```c
M_E_INUSE -파일이 이미 열려 있는 경우
```

M_E_BADFILENAME - 파일이름 형식이 잘못되었을 경우

M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_ERROR - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음

```c
MH_fileRename 설명
```

파일 이름을 바꾼다

**프로토타입**

```c
M_Int32 MH_fileRename ( M_Char *oldname, M_Char *newname)
```

**매개 변수**

[in]	oldname	바꾸기 전 절대 경로명 [in]	newname	바뀐 후 절대 경로명

**반환 값**

성공 실패

M_E_BADFILENAME - 파일이름 형식이 잘못된 경우

M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_NOSPACE - 파일시스템에 여유공간이 없을 경우 M_E_ERROR - 기타 이유로 실패한 경우

```c
M_E_NOENT – 바꾸기 전 파일이 존재하지 않을 경우	M_E_EXIST
- 새롭게 바꿀 파일 이름이 이미 존재하는 경우
M_E_INUSE - 바꾸기 전 파일이 이미 열려 있을 경우
```

**부작용**

없음

**참고 항목**

없음

```c
MH_fileRmDir 설명
```

디렉터리를 지운다.

지울 디렉터리 안에는 파일이나 디렉터리가 존재하지 않아야 한다

**프로토타입**

```c
M_Int32 MH_fileRmDir (M_Char * dirname)
```

**매개 변수**

[in]	dirname	지울 디렉터리 절대 경로

**반환 값**

성공 실패

M_E_BADFILENAME - 파일 이름 형식이 잘못된 경우 M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우

M_E_NOTEMPTY - 디렉터리 내에 파일이나 디렉터리가 존재할 경우 M_E_NOENT - 디렉터리가 이미 없을 경우

M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

```c
MH_fileSeek 설명
```

파일 포인터를 특정 위치로 옮긴다.

옮길 위치계산은 파일의 제일 처음부터 pos 만큼 또는 제일 끝에서 pos 만큼, 아니 면 현재 위치에서 pos 만큼 과 같이 3 가지로 구분 지을 수 있다

**프로토타입**

```c
M_Int32 MH_fileSeek (M_Int32 fd, M_Int32 pos, M_Int32 where)
```

**매개 변수**

[in]	fd	파일 식별자

[in]	pos	기준점으로부터 옮길 위치, 파일의 크기내에서 양수/음 수 모두 가능

[in]	where	MH_FILE_SEEK_SET, MH_FILE_SEEK_CUR, MH_FILE_SEEK_END

중 하나

**반환 값**

성공 실패

옮겨진 파일 포인터의 위치

```c
M_E_INVALID - 기준점이 MH_FILE_SEEK_SET,MH_FILE_SEEK_CUR,
```

MH_FILE_SEEK_END 중 하나에 포함되지 않을 경우

M_E_BADSEEKPOS - 파일 포인터를 옮길 위치가 파일의 범위를 넘어설 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

```c
MH_fileWrite 설명
```

fd 라는 식별자를 가지는 파일에 buf 가 가리키는 위치의 데이터를 지정한 size 만 큼 쓴다. 파일 시스템에 공간이 부족해서 요청한 파일을 다 쓸 수 없을 경우 쓴 바이트 수를 반환한다.

**프로토타입**

```c
M_Int32 MH_fileWrite (M_Int32 fd, M_Char* buf, M_Int32 size)
```

**매개 변수**

[in]	fd	파일 식별자

[in]	buf	버퍼 포인터

[in]	size	write 할 바이트 개수

**반환 값**

성공 실패

write 한 바이트 수

M_E_ERROR - 기타 이유로 실패할 경우

```c
M_E_NOSPACE - 파일시스템에 여유공간이 없을 경우
```

**부작용**

없음

**참고 항목**

없음

```c
MH_fileTotalSpace 설명
```

파일 시스템의 여유공간을 알려준다.

**프로토타입**

```c
M_Int32 MH_fileTotalSpace (void)
```

**매개 변수**

없음

**반환 값**

성공 실패

파일 시스템의 전체 공간의 바이트 단위의 크기를 반환한다. M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

```c
MH_fileSetMode 설명
파일의 속성을 변경한다. 변경가능 한 속성은 아래의 매개변수 table의 fmode값
을 참조한다.
```

**프로토타입**

```c
M_Int32 MH_fileSetMode(char* pathName, M_Int32 mode)
```

**매개 변수**

[in] pathName	파일의 절대 경로명 [in] fmode	파일 속성 mode

fmode

의미

값

```c
MH_FILEMODE_RDONLY
```

읽기 전용모드이면 세팅된다

```c
MH_FILEMODE_WRONLY
```

쓰기 전용모드이면 세팅된다.

```c
MH_FILEMODE_RDWR
```

읽기/쓰기 모드이면 세팅된다.

**반환 값**

성공 실패

```c
M_E_SUCCESS – 성공
```

M_E_ERROR - 기타 이유로 실패 M_E_BADFILENAME – 파일이름 형식이 잘못됨

M_E_LONGNAME - 파일이름의 길이가 최대 길이를 초과할 경우 M_E_INVALID - mode 가 잘못됨

M_E_NOENT – 파일이 존재하지 않음

**부작용**

없음

**참고 항목**

```c
없음
MH_fileGetCounts 설명
디렉토리내의 파일의 개수를 가져온다. 파일의 개수는 서브디렉토리를 포함한 값
이다.
```

**프로토타입**

```c
M_Int32 MH_fileGetCounts(char* pathName)
```

**매개 변수**

```c
[in] pathName	디렉토리의 절대 경로 명
```

**반환 값**

```c
성공
디렉토리내 파일 및 디렉토리의 개수
실패
```

M_E_ACCESS - 파일을 접근할 수 없음 M_E_ERROR - 기타 이유로 실패 M_E_BADFILENAME - 잘못된 경로 이름

M_E_LONGNAME - 디렉토리 이름의 길이가 최대 길이를 초과할 경우

**부작용**

```c
없음
```

**참고 항목**

```c
없음
MH_fileIsExist 설명
```

특정 경로상의 파일이 있는지 없는지를 알려준다.

**프로토타입**

```c
M_Int32 MH_fileIsExist(char* pathName)
```

**매개 변수**

```c
[in]	pathName	파일의 절대 경로 명
```

**반환 값**

```c
성공
M_E_SUCCESS – 파일이 존재함
실패
```

M_E_ACCESS - 파일을 접근할 수 없음 M_E_ERROR – 기타 이유로 실패 M_E_BADFILENAME – 잘못된 경로 이름

M_E_LONGNAME – 경로 이름이 최대 길이 보다 긴 경우 M_E_NOENT – 파일이 존재하지 않음

**부작용**

```c
없음
MH_fileTell 설명
현재 파일의 입출력 포인터를 반환해 준다.
```

**프로토타입**

```c
M_Int32 MH_fileTell(M_Int32 fd)
```

**매개 변수**

```c
[in] fd	파일 식별자
```

**반환 값**

```c
성공
현재 입출력 포인터 위치
실패
```

M_E_INVALIDFD	- 잘못된 파일 식별자 M_E_ERROR – 기타 이유로 실패

**부작용**

```c
없음
```

**참고 항목**

```c
없음
```

### InputMethod

InputMethod Automata 관련 함수들이다. 각 단말기 환경에 따라 작성된 오토마타 에서 현재 입력 키 값에 따라 문자(열)를 처리하여 InputMethod 에 넘겨주게 된다. InputMethod 에 전달되는 문자(열)를 현재 조합중인 문자(열)과 조합이 끝나서 완 성된 문자(열)이 존재할 경우 완성된 문자(열)을 넘겨주게 된다.

InputMethod 와 사용자 텍스트 입력 컴포넌트에서는 오토마타로부터 넘겨받은 문 자(열)을 삽입하거나 삭제, 수정하는 작업을 처리한다.

현재	오토마타에서		지원하는	입력	모드에		대한		정보는 MH_IMAgetSurpportModeCount()와  MH_IMAgetSupportedModes(), MH_IMAgetCurrentMode	를	통해서		얻을		수	있다.	여기서 MH_IMAgetSupportedModes()의 경우 리턴값은 오토마타에서 지원하는 언어코드를 넘겨주게 되며, 언어코드는 ISO 639 코드를 따른다. 단, 해당 언어가 대소문자를 구분하는 경우 각 언어코드에 "/S","/L"를 추가하여 지정할 수 있다. 예를 들어 영문 소문자의 경우 "EN/S"의 언어코드를 넘겨주게 된다.

한글의 경우에는 "KO"의 언어코드를 넘겨주게 된다. 숫자의 경우 언어코드에서 정 의되어 있지 않으므로, "N123"으로 정한다. 심볼 코드는 폰에서 제공하는 코드의 형태가 다양하므로 HAL 에서 정의 하지 않고, 상위의 사용자 컴포넌트에서 공통적 으로 구현하도록 한다.

관련 자료형

# #define MH_IMA_NUM_MODE "N123" // 숫자 입력모드. 숫자의 경우 표준언어코드 에서 지원하지 않으므로 숫자입력에 대한 코드를 지정한다.

#define MH_IMA_FLUSH –99 // 사용자에 의해서 현재 조합중인 문자를 강제로 완성 시켜야 할 경우 사용되는 특수 키. 이 키가 MH_IMAhandleInput 로 입력된 경우 현 재 조합중이 문자를 완성하여 반환한다. 키 입력을 받아서 일정 시간 후 키가 완 성되는 방식의 오토마타구현시 이 키값을 MH_pltEvent 를 이용하여 플랫폼으로 전 달 하여 구현할 수 있다.

```c
MH_IMAgetSurpportModeCount 설명
오토마타에서 지원는 입력모드의 수를 얻어온다.
```

**프로토타입**

```c
_Int32 MH_IMAgetSurpportModeCount()
```

**매개 변수**

```c
없음
```

**반환 값**

```c
입력모드의 수
```

**부작용**

없음

**참고 항목**

없음

```c
MH_IMAgetSupportedModes() 설명
오토마타에서 지원하는 입력모드의 언어코드를 얻어온다. 언어코드는 ISO 639 코드를
따른다. 단, 해당 언어가 대소문자를 구분하는 경우 각 언어코드에 "/S","/L"를 추가하 여 지정할 수 있다. 예를 들어 영문 소문자의 경우 "EN/S"의 언어코드를 넘겨주게 된 다. 한글의 경우에는 "KO"의 언어코드를 넘겨주게 된다.
```

**프로토타입**

```c
char** MH_IMAgetSupportedModes()
```

**매개 변수**

없음

**반환 값**

```c
언어코드 (스트링 어레이 포인터)
```

**부작용**

없음

**참고 항목**

없음

```c
MH_IMAsetCurrentMode 설명
오토마타에서 사용할 모드를	지정한다.이  값은 MH_IMAgetSupportedModes()로  얻은
언어코드의 인덱스값이다.
```

**프로토타입**

```c
M_Int32 MH_IMAsetCurrentMode (M_Int32 mode)
```

**매개 변수**

```c
입력모드
```

**반환 값**

```c
지정한 입력모드가 바르게 적용된 경우 "1". 그렇지 않은 경우 "0".
```

**부작용**

없음

**참고 항목**

없음

```c
MH_IMAgetCurrentMode() 설명
오토마타의 현재 입력모드를 얻어온다.	이  값은 MH_IMAgetSupportedModes()로 얻
은 언어코드의 인덱스값이다.
```

**프로토타입**

```c
M_Int32 MH_IMAgetCurrentMode()
```

**매개 변수**

```c
없음
```

**반환 값**

```c
오토마타의 현재 입력모드.
```

**부작용**

없음

**참고 항목**

없음

```c
MH_IMAhandleInput 설명
```

사용자 컴포넌트로 부터받은 키 입력을 현재 입력모드에 따라 처리하며 문자를 생 성하고, 생성된 문자를 넘긴다. (주의)MH_IMA_FLUSH 가 키값으로 입력된 경우 현 재 조합중이 문자를 완성하여 반환한다.

**프로토타입**

```c
M_Int32 MH_IMAhandleInput ( char key,
M_Int32 type, char *buf1, M_Int32 *size1, char *buf2, M_Int32 *size2
);
```

**매개 변수**

key [in] 입력된 키값 (MH_KeyCode에 정의된 것, MH_IMA_FLUSH) type [in] 입력된 키 타입 (MH_Event에 정의된 것.)

buf1 [out] 완성된 문자열버퍼

size1 [in] 완성된 문자열 버퍼의 크기 buf2 [out] 조합중인 문자열버퍼

size2 [in] 조합중인 문자열 버퍼의 크기

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

### Font

다양한 폰트를 화면에 출력하거나 화면 출력 시에 다양한 정보들을 얻어오는 함수 로 구성되어 있다.

폰트는 시스템에 마다 형태와 크기와 페이스(Face)가 일정하지 않으므로 각 폰트 를 정확히 지정하는 것이 아니라, 추상화된 내용으로 지정한다. 즉 크기(작음|보 통|큼)과 스타일(굵게|이탤릭|밑줄|보통)과 페이스를 가지고 실제적인 폰트를 얻 어옴으로써 각 단말기 마다 쉽게 적용될 수 있도록 하였다.

```c
Ascent
e
L
Descent
Width
```

#### 그림 2 폰트정보

폰트의 각 부분은 폰트의 높이(Height)는 어센트(Ascent)와 디센트(Descent)를 합 한 값이 된다.

베어(Bear)는 폰트를 그릴 때 실제적으로 화면에 이미지를 어디서부터 어디까지 그릴 것인지를 결정한다. 대부분의 경우 왼쪽 베어(Left Bear)는 0 이 된다만, 이

탤릭 체와 같은 경우에는 오른쪽 베어(Right Bear)가 폰트의 폭(Width)보다 큰 경 우가 있다. 오른쪽 베어는 실제적으로 폰트의 이미지의 폭이 되고, 폭(Width)는 그 폰트를 그린 후에 얼마만큼 이동한 후에 다음 문제를 그릴지를 결정하는 값이 된다. 폭이 오른쪽 베어(Right Bear)보다 작은 경우에는 위의 그림과 같이 겹쳐지 는 부분이 있을 수 있다.

관련 자료형

```c
typedef struct _MH_CharGlyphInfo {
```

// 문자의 왼쪽 베어(bear) int lbear;

// 문자의 오른쪽 베어(bear) int rbear;

// 문자의 화면상의 폭 int width;

// 문자의 화면상의 높이 int height;

} MH_CharGlyphInfo;

```c
#define MH_FB_FT_SIZE_SMALL
#define MH_FB_FT_SIZE_MEDIUM
#define MH_FB_FT_SIZE_LARGE
#define MH_FB_FT_FACE_SYSTEM
#define MH_FB_FT_FACE_MONOSPACE
#define MH_FB_FT_FACE_PROPORTIONAL
#define MH_FB_FT_STYLE_PLAIN
#define MH_FB_FT_STYLE_BOLD
#define MH_FB_FT_STYLE_ITALIC
#define MH_FB_FT_STYLE_UNDERLINE
MH_fnGetFont
```

**설명**

지정된 폰트 아이디를 얻어 온다.

face 는 MH_FB_FT_FACE_SYSTEM, MH_FB_FT_FACE_MONOSPACE(문자들의 폭이 일정한 폰트), MH_FB_FT_FACE_PROPORTIONAL(문자들의 폭이 일정하지 않은 폰트) 중에 하 나이며, size 는 MH_FB_FT_SIZE_SMALL, MH_FB_FT_SIZE_MEDIUM, MH_FB_FT_SIZE_LARGE 중에 하나가 된다. style 은 MH_FB_FT_STYLE_ITALIC, MH_FB_FT_STYLE_BOLD,  MH_FB_FT_STYLE_UNDERLINED  의  OR  값이나  혹은

MH_FB_FT_STYLE_PLAIN 을 사용할 수 있다. 지정된 폰트가 없으면 가장 근접한 폰 트를 돌려준다.

지정된 폰트 아이디로 “C” 로컬 문자 코드의 전체 문자를 출력할 수 있어야 한다.

**프로토타입**

```c
M_Int32 MH_fnGetFont (M_Int32 face, M_Int32 size, M_Int32 style)
```

**매개 변수**

[in]	face	폰트 페이스(MH_FB_FT_FACE_SYSTEM, MH_FB_FT_FACE_MONOSPACE, MH_FB_FT_FACE_PROPORTIONAL)

[in]	size	폰트	크기	(MH_FB_FT_SIZE_SMALL,	MH_FB_FT_SIZE_MEDIUM, MH_FB_FT_SIZE_LARGE)

[in]	style	폰트	스타일(MH_FB_FT_STYLE_ITALIC,	MH_FB_FT_STYLE_BOLD, MH_FB_FT_STYLE_UNDERLINED)

**반환 값**

폰트 아이디

**부작용**

없음

**참고 항목**

없음

```c
MH_fnGetFontHeight 설명
```

지정된 폰트의 높이를 돌려준다

**프로토타입**

```c
M_Int32 MH_fnGetFontHeight (M_Int32 font)
```

**매개 변수**

[in]	font	폰트 아이디

**반환 값**

폰트의 높이

**부작용**

없음

**참고 항목**

없음

```c
MH_fnGetFontAscent
```

**설명**

지정된 폰트의 어센트(Ascent)를 돌려준다

**프로토타입**

```c
M_Int32 MH_fnGetFontAscent (M_Int32 font)
```

**매개 변수**

[in]	font	폰트 아이디

**반환 값**

폰트의 어센트(Ascent)

**부작용**

없음

**참고 항목**

없음

```c
MH_fnGetFontDescent
```

**설명**

지정된 폰트의 디센트(Descent)를 돌려준다.

**프로토타입**

```c
M_Int32 MH_fnGetFontDescent (M_Int32 font)
```

**매개 변수**

[in]	font	폰트 아이디

**반환 값**

폰트의 디센트(Descent)

**부작용**

없음

**참고 항목**

없음

```c
MH_fnGetCharGlyph
```

**설명**

지정된 문자를 화면에 바로 찍을 수 있는 이미지 형태로 만들어 돌려준다. 돌려주는 버퍼는 주 화면 LCD 와 같은 색상수를 가지며 주화면 LCD 에 바로 복사할 수 있는 형태의 이미지이다. 이미지 내용은 반환하는 값이 가리키는 버퍼에 (0, 0)에서 부터 (1, 0), (2, 0), ... (0, 1), (1, 1) ... 의 순서 대로 저장된다.

```c
Pixel 단위
LCD가 16bit 컬러를 지원할 때.
M_Uint8 *pbuf = MH_fnGetCharGlyph(fontid, ‘H’, blackPixel, whitePixel, &bpl); M_Uint16 *ppxls = (M_Uint16 *)pbuf;
와 같은  코드가  수행되었다면,  , ppxls[0] 은 whitePixel이 되고 ppxls[bpl*1] 은 whitePixel, ppxls[bpl * 1 + 1]은 blackPixel이 된다.
```

**프로토타입**

```c
const M_Uint8 *MH_fnGetCharGlyph( const M_Int32 fontid, const M_Uint16 ch,
const M_Uint32 fgPxl,
const M_Uint32 bgPxl,
M_Int32 *pbpl,
)
```

**매개 변수**

[in]	fontid 폰트아이디

[in]	ch	문자 (문자는 로컬 코드 이다. 즉 유니 코드가 아니다)

```c
[in]	fgPxl	문자의 전경색 [in]	bgPxl	문자의 배경색
```

[out]  bpl	프레임 버퍼의 한 줄 당 차지하는 바이트 수

**반환 값**

복사 할 수 있는 형태의 이미지 내부 버퍼. 이 버퍼는 밖에서 해제되면 안되며 내 용이 바뀌어서도 안된다. 만일 ch 에 대응하는 문자가 없는 경우에는 NULL 을 돌려 준다.

**부작용**

없음

**참고 항목**

없음

```c
MH_fnGetCharInfo
```

**설명**

지정된 문자의 폭과 왼쪽 베어(Left Bear)와 오른쪽(Right Bear)와 높이를 얻어 온다.

**프로토타입**

```c
M_Int32 MH_fnGetCharInfo(M_Int32 font, M_Uint16 char, MH_CharGlyphInfo *pcg)
```

**매개 변수**

[in]	font	폰트

[in]	char	문자(문자는 로컬 코드 이다. 즉 유니 코드가 아니다) [out]	pcg	문자의 정보 반환

**반환 값**

성공 실패:

M_E_ERROR – 대응하는 문자 인덱스에 폰트가 없는 경우

**부작용**

없음

**참고 항목**

없음

### Frame Buffer

LCD 화면에 프레임 버퍼의 내용을 출력하거나, 화면의 정보를 얻어오는 함수로 구 성되어 있다.

LCD 에 화면 내용을 변경하는 것을 시간을 요하는 작업이므로, Double Buffering 개념을 이용하여 화면 출력 시간을 최소화 한다. MG_fbGetScreenBuffer() 를 사용 하면, 시스템에서 사용하는 이미지 버퍼를 얻어 올 수 있다. 얻어온 메모리 이미 지 버퍼에 화면에 출력될 내용을 다 그리고 나서 MG_fbFlushLcd() 를 사용하여 이 미지 버퍼의 내용을 LCD 화면에 출력 한다.

단말기 기본 소프트웨어의 프레임 버퍼를 사용한다.

관련 자료형

```c
typedef struct _MH_DisplayInfo MH_DisplayInfo {
```

// 한 픽셀이 차지하는 비트수 M_Int32 bpp;

// 한 픽셀이 차지하는 유효한 비트수 24bit 인 경우에 bpp 는 32 가 되고, depth 는 24 가 될 수 있다. 2 의 depth 승은 실제 화면에서 출력할 수 있는 컬러의 색상 이 된다.

```c
M_Int32 depth;
```

// 화면의 폭; 픽셀 단위 M_Int32 width;

// 화면의 높이; 픽셀 단위 M_Int32 height;

// 화면의 한라인이 차지하는 바이트 수; 내부에 PADDING 도 포함이 된다.

```c
M_Int32 bpl;
```

// LCD 가 GrayScale 인지 TRUE COLOR 인지를 알려준다.

```c
M_Int32 colortype;
```

// TRUE 컬러인 경우에 픽셀 값 내에 red 값이 쓰여지는 부분의 mask M_Int32 redmask;

// TRUE 컬러인 경우에 픽셀 값 내에 blue 값이 쓰여지는 부분의 mask M_Int32 bluemask;

// TRUE 컬러인 경우에 픽셀 값 내에 green 값이 쓰여지는 부분의 mask M_Int32 greenmask;

```c
};
#define MH_FB_MAIN_LCD	1
#define MH_FB_SUB_LCD	2
MH_GRP_DIRECT_COLOR_TYPE
```

**프로토타입**

```c
#define MH_GRP_DIRECT_COLOR_TYPE
```

**설명**

팔레트를 사용하지 않는 경우의 컬러 타입. (1 << 0)로 정의한다.

```c
MH_GRP_GRAY_TYP E
```

**프로토타입**

```c
#define MH_GRP_GRAY_TYPE
```

**설명**

흑백 타입. (1 << 1)로 정의한다.

```c
MH_GRP_COLOR_TYPE
```

**프로토타입**

```c
#define MH_GRP_COLOR_TYPE
```

**설명**

컬러 타입. (1 << 2)로 정의한다.

```c
MH_fbGetDisplayInfo
```

**설명**

화면 관련된 정보를 얻어 온다.

screen 에 해당하는 화면 정보를 얻어 온다. screen 값은 MH_FB_MAIN_LCD 나 MH_FB_SUB_LCD 둘 중 하나가 될 수 있다. MH_FB_MAIN_LCD 는 모든 단말기에 존재하 는 LCD 이지만, MH_FB_SUB_LCD 는 듀얼 폴더와 같이 부가적인 LCD 로써 단말기에 따라서 존재할 수도 있고 존재 하지 않을 수도 있다.

**프로토타입**

```c
void MH_fbGetDisplayInfo (M_Int32 screen,MH_DisplayInfo*  displayinfo)
```

**매개 변수**

[in]	screen	스크린 번호: MH_FB_MAIN_LCD, MH_FB_SUB_LCD 둘 중 하나가 될 수 있다.

[out]displayinfo	스크린 정보

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

```c
MH_fbFlushLcd 설명
```

LCD 화면에 내부 스크린 프레임 버퍼의 내용을 출력시킨다.

이 함수를 통해서 출력된 내용은 다음 이 함수를 부르기 전까지 그 내용이 계속 화면에 출력된다.

**프로토타입**

```c
void MH_fbFlushLcd (
M_Int32 screen, M_Int32 x, M_Int32 y, M_Int32 w, M_Int32 h
)
```

**매개 변수**

- `screen` — 스크린 번호: MH_FB_MAIN_LCD, MH_FB_SUB_LCD 둘중 하나가 될 수 있다. x - 출력시킬 영역의 x 좌표
- `y` — 출력시킬 영역의 y 좌표 w - 출력시킬 영역의 폭
- `h` — 출력시킬 영역의 높이

**반환 값**

없음

**부작용**

없음

**참고 항목**

없음

```c
MH_fbMakePixel 설명
```

지정한 0xRRGGBB 값에 해당하는 픽셀 값을 얻어 온다.

**프로토타입**

```c
M_Int32 MH_fbMakePixel (M_Int32 color)
```

**매개 변수**

- `color` — 0xRRGGBB 의 color 값

**반환 값**

픽셀 값

**부작용**

없음

**참고 항목**

없음

```c
MH_fbGetPixelFromRGB 설명
```

지정한 r, g, b 값에 해당하는 픽셀 값을 얻어 온다.

**프로토타입**

```c
M_Int32 MH_fbGetPixelFromRGB (M_Int32 r, M_Int32 g, M_Int32 b)
```

**매개 변수**

- `r` — 빨강색(0-255)
- `g` — 녹색(0-255)
- `b` — 파랑색(0-255)

**반환 값**

픽셀 값

**부작용**

없음

**참고 항목**

없음

```c
MH_fbGetRGBFromPixel 설명
```

지정한 픽셀 값의 빨강, 파랑, 녹색의 값을 얻어 온다.

**프로토타입**

```c
M_Int32 MH_fbGetRGBFromPixel (M_Int32 pixel, M_Int32 *r, M_Int32	*g, M_Int32 *b)
```

**매개 변수**

```c
pixel – 픽셀 값
```
- `r` — 빨강색(0-255)
- `g` — 녹색(0-255)
- `b` — 파랑색(0-255)

**반환 값**

픽셀 값

**부작용**

없음

**참고 항목**

없음

```c
MH_fbGetScreenBuffer 설명
```

스크린 프레임 버퍼를 돌려준다.

기본적으로 LCD 인터페이스 하는 속도가 현저하게 느리므로 LCD 의 출력되고 있는 내용을 호스트 메모리에 저장해 놓고 있어야 한다. 이러한 시스템에서 사용하는 스크린 프레임 버퍼를 돌려준다. 스크린 프레임 버퍼는 LCD 에 출력할 수 있는 크 기 -(bits per pixel * width + padding) / 8 * height-만큼 잡혀야 하며, 그 위 치가 변경 되서는 안된다.

Dual LCD 의 경우에 대부분 주 LCD 와 보조 LCD 의 depth(색상 표현 개수)가 다른 경우가 있지만, 넘겨 주는 타입은 주 LCD 와 같은 형태의 데이타가 넘어가는 것을 가정한다. 만일 보조 LCD 의 데이타 타입이 다르다면, MG_fbFlushLcd 함수 내에서 적절한 변형 과정(가장 근접한 색상을 해당 점에 출력하는 과정)을 거쳐 LCD 에 출력하도록 한다. 데이타는 LCD 화면의 상단 좌측의 점으로 부터 시작하여 좌측으 로 가는 방향의 픽셀 값을 연속적으로 저장한다. 아래 그림을 참조하십시요.

```c
(1,1) (2,1) (3,1)	…	(1,2) (2,2) (3,2)	…
```

### …

### …

```c
Pixel 크기(LCD가 16bit 색상일때는 2byte가 되고, 8bit일때는 1byte가 됨)
```

**프로토타입**

```c
M_Uint8* MH_fbGetScreenBuffer (M_Int32 lcd_num)
```

**매개 변수**

- `lcd_num` — [in] 화면 인덱스(0; 주화면 1; 보조 LCD 화면)

**반환 값**

스크린 프레임 버퍼

**부작용**

없음

**참고 항목**

없음

### Virtual Key

응용프로그램에서 단말기의 키를 가상적인 기능 키로 사용할 때 필요한 함수들이 다. 예를 들어 단말기에서 방향 키가 존재하지 않는 경우 번호 키를 매핑 (mapping)해서 사용한다.게임이나 기타 응용 프로그램은 숫자키 외의 키를 받아서 수행된다. 그러나 숫자키 외의 키(조절키)의 존재 여부는 폰 모델에 따라 다르므 로 이런 조절키는 가상 기능키라 정의하고, 이런 가상 기능 키는 , MH_keyGetVirtualCode 나 MH_keyGetKeyCode 함수로 각각 가상 기능 키 값을 실제 키 값으로, 실제 키 값을 가상 기능 키 값으로 변경하여 일반 응용 프로그램에서 조절키 존재 여부에 상관없이 동작할 수 있도록 해준다. 예를 들어 “MH_VIRGAME_A”키라는 가상 키가 있으며 이 가상 키는 “7”키나 “1”키 혹은 “SOFT_2”키에 대응될 수 있다.

```c
int a;
a = MH_keyGetVirtualCode(MH_KEY_7); //
```

관련 자료형

```c
a == MH_VIRGAME_A
```

//  UP 기능 키

```c
#define	MH_VIRUP
```

//  DOWN 기능 키

```c
#define	MH_VIRDOWN
```

//  LEFT 기능 키

```c
#define	MH_VIRLEFT
```

// RIGHT 기능 키

```c
#define	MH_VIRRIGHT
```

// FIRE(SEL) 기능 키

```c
#define	MH_VIRFIRE
```

// GAME1 기능 키

```c
#define	MH_VIRGAME_A
```

// GAME2 기능 키

```c
#define	MH_VIRGAME_B
```

// GAME3 기능 키

```c
#define	MH_VIRGAME_C
```

// GAME4 기능 키

```c
#define	MH_VIRGAME_D
```

// SIDE UP 기능 키

```c
#define	MH_VIRSIDE_UP
```

// SIDE

DOWN 기능 키

```c
#define
MH_VIRSIDE_DOWN
```

// SIDE

SEL 기능 키

```c
#define
MH_VIRSIDE_SEL
```

// SIDE

CLEAR 기능 키

```c
#define
MH_VIRSIDE_CLEAR
MH_keyGetVirtualCode
```

**설명**

주어진 실제 키의 값에 매핑(mapping)되는 가상 키 값을 가져 온다

**프로토타입**

```c
M_Int32 MH_keyGetVirtualCode(M_Int32 keyCode)
```

**매개 변수**

keyCode 폰의 KeyCode 값. MH_KeyCode 참조

**반환 값**

[in]	Virtual	Keyapad

**부작용**

없음

**참고 항목**

없음

```c
MH_keyGetKeyCode 설명
```

주어진 가상 키의 값에 매핑(mapping)되는 실제 키 값을 가져 온다

**프로토타입**

```c
M_Int32 MH_keyGetKeyCode(M_Int32 gameAction)
```

**매개 변수**

[in]	gameAction	Virtual KeyPad

**반환 값**

폰의 KeyCode 값. MH_KeyCode 참조.

**부작용**

없음

**참고 항목**

없음

### API 규격

## C API

```c
Clet 에서 사용할 수 있는 모든 API를 정의 한다. Clet은 다음의 함수를 모두 구현해야 한다. 플랫폼이 필요한 경우 각종 이벤트에 따라 해당 함수를 불러 준다.
```

### handleCletEvent

```c
void CletHandleEvent(int type, int param1, int param2)
이벤트를 처리하는 함수이다. type에는 1항에 정의된 이벤트가 올 수 있다. param1과 param2는 type의 값에 따라서 달라진다.
```

이벤트(type)

**설명**

사용되는

변수

```c
MV_KEY_PRESS_EVENT
키가
눌렸을 때 발생되는 이벤트
param1 = 키 넘어 온다.
param2 = 0
코드
값이
MV_KEY_REPEAT_EVENT
키가 계속 눌려 있는 상태일 때 특 정 시간마다 반복적으로 발생되는 이벤트
param1 = 키 넘어 온다.
param2 = 0
코드
값이
MV_KEY_RELEASE_EVENT
키가
떼어졌을 때 발생되는 이벤트
param1 = 키 넘어 온다.
param2 = 0
코드
값이
MV_CHILD_APP_START_EV ENT
현재 응용 프로그램이 수행 시킨 자식 프로그램이 시작되었음을 알 려주는 이벤트.
param1 = 생성된 자식 프 로그램의 식별자
param2 = 0
MV_CHILD_APP_DESTROY
_EVENT
현재 응용 프로그램이 수행 시킨 자식 프로그램이 종료되었음을 알 려주는 이벤트
param1 = 생성된 자식 플 로그램의 식별자
param2 = 프로그램의 종 료 코드
MV_USER_EVENT
사용자 이벤트
param1 = 사용자 지정 값
param2 = 사용자 지정 값
```

startClet

```c
void startClet(int argc, char *argv[]);
프로그램이 시작될때 불리는 함수이다. argc에는 매개 변수의 갯수가 넘어 오며, argv 에는 매개 변수들이 넘어 온다. argv[0]부터 argv[argc-1]까지가 유효한 값이다.
```

pauseClet

```c
void pauseClet();
프로그램이 잠시 멈추어 질때 이 함수를 호출해 준다. 이 함수를 빠져 나가면 프로그 램은 더이상 이벤트를 받지 않는다.
```

resumeClet

```c
void resumeClet();
프로그램이 재개될 때 이 함수를 호출해 준다. 이 함수를 빠져 나가면 프로그램은 그 때 부터 새롭게 이벤트를 받는다.
```

destroyClet

```c
void destroyClet();
프로그램이 종료될 때 불린다.
```

paintClet

```c
void paintClet(int x, int y, int w, int h);
화면의 일부분을 다시 칠해야 하는 경우에 불리는 함수이다. x, y, w, h는 각각 그려져 야 하는 화면의 일부분을 가르킨다.
```
