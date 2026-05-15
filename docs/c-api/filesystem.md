# 5.1.4. 파일시스템

파일에 관련된 모듈이다.

계층적 디렉토리 구조를 가진 파일 시스템이 운영체제에서 지원함을 가정한다. 파일을 열고, 읽고, 쓰며, 파일의 정보를 읽어오는 것과 관련된 API 들이 포함된 다.

파일이름은 모두 절대경로로 되어 있다. 실제로는 플랫폼에서 허용하는 디렉토리 안에서 모든 파일을 만들고 지울 수 있게 되어있다. 사용자입장에서는 플랫폼에서 어떤 식으로 지원하든 상관없이 절대경로로 사용하면 된다.

구분자(separator)의 경우 유닉스 시스템의 관행을 따랐다. 그러므로 "/"를 사용하 면 된다.

다음과 같이 파일 경로를 인수로 갖는 API 는 접근 레벨도 함께 인수로 넣어주어야 한다.

- `MC_fsOpen`
- `MC_fsFileAttribute`
- `MC_fsRemove`
- `MC_fsRename`
- `MC_fsMkDir`
- `MC_fsRmDir`
- `MC_fsList`

접근 레벨은 다음과 같이 세가지가 있다. 

- `MC_DIR_PRIVATE_ACCESS`: 자기 자신의 디렉토리로 접근
- `MC_DIR_SHARED_ACCESS` : 공유 디렉토리로 접근
- `MC_DIR_SYSTEM_ACCESS` : 시스템 공유 디렉토리로 접근

모든 응용프로그램은 자기 자신의 디렉토리로는 접근이 가능하고, 나머지 접근 수준은 권한을 받은 프로그램만이 접근 가능하도록 되어있다. 파일 공유시에 한 응 용 프로그램에서 Read/Write 로 열린 경우는 다른 응용 프로그램에서는 Read 만 할 수 있다. 위의 모든 API 는 blocking 이다. 곧, 모든 파일 operation 을 마친 후에 리턴 된다.

**참고 항목**

없음

### MC_FILE_OPEN_RDONLY

**프로토타입**

```c
#define MC_FILE_OPEN_RDONLY
```

**설명**

읽기만 가능. `MH_FILE_OPEN_RDONLY` 로 정의한다.

### MC_FILE_OPEN_WRONLY

**프로토타입**

```c
#define MC_FILE_OPEN_WRONLY
```

**설명**

쓰기만 가능. `MH_FILE_OPEN_WRONLY` 로 정의한다.

### MC_FILE_OPEN_WRTRUNC

**프로토타입**

```c
#define MC_FILE_OPEN_WRTRUNC
```

**설명**

쓰기만 가능하고 파일이 존재하면 파일 크기를 0 으로 만듬. `MH_FILE_OPEN_WRTRUNC` 로 정의한다.

### MC_FILE_OPEN_RDWR

**프로토타입**

```c
#define MC_FILE_OPEN_RDWR
```

**설명**

읽기와 쓰기 모두 가능. `MH_FILE_OPEN_RDWR` 로 정의한다.

### MC_FILE_IS_DIR

**프로토타입**

```c
#define MC_FILE_IS_DIR
```

**설명**

파일 attribute 중 디렉토리를 나타내는 bit. `MH_FILE_IS_DIR` 로 정의한다.

### MC_MAX_FILENAME_LENGTH

**프로토타입**

```c
#define MC_MAX_FILENAME_LENGTH
```

**설명**

파일이름 최대 길이. `MH_MAX_FILENAME_LENGTH` 로 정의한다.


### MC_DIR_PRIVATE_ACCESS

**프로토타입**

```c
#define MC_DIR_PRIVATE_ACCESS
```

**설명**

자기 자신의 디렉토리로 접근. 1 로 정의한다.


### MC_DIR_SHARED_ACCESS

**프로토타입**

```c
#define MC_DIR_SHARED_ACCESS
```

**설명**

공유 디렉토리로 접근. 2 로 정의한다.


### MC_DIR_SYSTEM_ACCESS

**프로토타입**

```c
#define MC_DIR_SYSTEM_ACCESS
```

**설명**

시스템 디렉토리로 접근. 3 으로 정의한다.

### MC_FILE_SEEK_SET

**프로토타입**

```c
#define MC_FILE_SEEK_SET
```

**설명**

파일의 처음을 기준으로 파일포인터의 위치를 설정. `MH_FILE_SEEK_SET` 로 정의한다.

### MC_FILE_SEEK_CUR

**프로토타입**

```c
#define MC_FILE_SEEK_CUR
```

**설명**

파일의 current position 을 기준으로 파일포인터의 위치를 설정. `MH_FILE_SEEK_CUR` 로 정의한다.

### MC_FILE_SEEK_END

**프로토타입**

```c
#define MC_FILE_SEEK_SET
```

**설명**

파일의 끝을 기준으로 파일포인터의 위치를 설정. `MH_FILE_SEEK_SET` 로 정의한다.

### MC_fsOpen

**설명**

파일을 엽니다. aMode의 값에 따라 열고자 하는 디렉토리의 위치가 달라집니다. 파일 이름은 30 자로 제한합니다.

**프로토타입**

```c
M_Int32 MC_fsOpen(M_Char* name, M_Int32 flag, M_Int32 aMode)
```

**매개 변수**

- `name` - 파일이름
- `flag`
  - `MC_FILE_OPEN_RDONLY` 읽기만 가능 MC_FILE_OPEN_WRONLY 쓰기만 가능
  - `MC_FILE_OPEN_WRTRUNC` 열기만 가능하고 파일이 존재하면 파일크기가 0 이 됩니다.
  - `MC_FILE_OPEN_RDWR` 읽기와 쓰기가 모두 가능
- `aMode`
  - `MC_DIR_PRIVATE_ACCESS` private 디렉토리에 접근
  - `MC_DIR_SHARED_ACCESS` shared 디렉토리에 접근
  - `MC_DIR_SYSTEM_ACCESS` system 디렉토리에 접근

**반환 값**

성공
- 파일 식별자

실패
- `M_E_ERROR` - 기타 이유로 실패
- `M_E_NOENT` - `MC_FILE_OPEN_RDONLY` 로 열 경우 파일이 없음
- `M_E_BADFILENAME` - 파일이름 형식이 잘못됨
- `M_E_LONGNAME` - 파일이름의 길이가 최대 길이를 초과할 경우
- `M_E_INVALID` - flag 가 잘못됨
- `M_E_NOSPACE` - 파일 시스템의 남은 공간이 없음
- `M_E_ACCESS` - 파일을 접근할 수 없음

**부작용**

없음

**참고 항목**

mkdir aMode의미 참조

### MC_fsRead

**설명**

파일을 읽는다. len 크기의 byte 만큼 buf 로 읽는다.

**프로토타입**

```c
M_Int32 MC_fsRead(M_Int32 fd, M_Byte* buf, M_Int32 len)
```

**매개 변수**

- `fd` - 파일 식별자
- `buf` - 파일에서 읽어들인 데이타가 저장되는 버퍼
- `len` - 읽어들일 byte 수

**반환 값**

성공
- 실제 읽어들인 byte 수

실패
- `M_E_ERROR` – 기타 이유로 실패
- `M_E_BADFD` - 파일 식별자가 잘못됨
- `M_E_EOF` - 파일 끝임

**부작용**

없음

**참고 항목**

없음


### MC_fsWrite

**설명**

파일을 쓴다. buf 에 있는 내용을 len 크기의 byte 만큼 쓴다.

**프로토타입**

```c
M_Int32 MC_fsWrite(M_Int32 fd, M_Byte* buf, M_Int32 len)
```

**매개 변수**

- `fd` - 파일 식별자
- `buf` - 파일에 쓸 데이타가 저장되는 버퍼
- `len` - 쓸 byte 수

**반환 값**

성공
- 실제 써진 byte 수

실패
- `M_E_ERROR` - fail
- `M_E_BADFD` - 파일 식별자가 잘못됨
- `M_E_NOSPACE` - 파일시스템의 여유공간이 없음

**부작용**

없음

**참고 항목**

없음


### MC_fsClose

**설명**

파일을 닫다

**프로토타입**

```c
M_Int32 MC_fsClose(M_Int32 fd)
```

**매개 변수**

- `fd` - 파일 식별자

**반환 값**

성공
- 0

실패
- `M_E_ERROR` – 기타 이유로 실패
- `M_E_BADFD` - 파일 식별자가 잘못됨

**부작용**

없음

**참고 항목**

없음



### MC_fsSeek

**설명**

파일을 읽고 쓸 때 현재 읽고 쓰는 위치를 나타내는 파일 포인터의 위치를 조정한 다

**프로토타입**

```c
M_Int32 MC_fsSeek(M_Int32 fd, M_Int32 pos, M_Int32 where)
```

**매개 변수**

- `fd` - 파일 식별자
- `pos` - 새로 설정할 파일포인터의 위치
- `where`
  - `MC_FILE_SEEK_SET` 파일의 처음을 기준으로 파일포인터의 위치를 설정
  - `MC_FILE_SEEK_CUR` 파일의 current position 을 기준으로 파일포인터의 위치를 설정
  - `MC_FILE_SEEK_END` 파일의 끝을 기준으로 파일포인터의 위치를 설정

**반환 값**

성공
- 파일포인터의 현재 위치

실패
- `M_E_ERROR` – 기타 이유로 실패
- `M_E_BADFD` - 파일 식별자가 잘못됨
- `M_E_INVALID` - where 가 잘못된 값
- `M_E_BADSEEKPOS` - 파일포인터가 파일크기의 범위를 벗어남

**부작용**

없음

**참고 항목**

없음

### MC_fsFileAttribute

**설명**

파일의 현재 특성을 구한다. 인수로 들어가는 `MC_FileInfo` 의 구조는 다음과 같다.

```c
struct _fileInfo{ 
    M_Int32     attrib;   // 파일의 특성을 표시한 bit mask들 
    M_Uint32    creationTime; // 파일이 생성된 시간을 1970 년 1 월 1 일 이후 초단위로 나타낸다.  
    M_Uint32    size;           // 파일의 크기 
 };
 ```

위 구조체에서 파일 특성을 표시하는 bit mask 의 경우는 아래의 예제와 같이 사 용할 수 있다.

fa->attrib 에 `MC_FILE_IS_DIR` bit 가 설정되어 있으면 directory 임.

```c
// program A
MC_FileInfo fi;
...
int rtn = MC_fsFileAttribute("B", &fi, MC_DIR_PRIVATE_ACCESS);
if ( fi.attrib & MC_FILE_IS_DIR ) {
// direcorty임
} else {

}
...
```

**프로토타입**

```c
M_Int32 MC_fsFileAttribute(M_Char* name, MH_FileInfo* fa, M_Int32 aMode)
```

**매개 변수**

- `name` - 파일 이름
- `fa` - 파일 attribute structure 포인터
- `aMode`
  - `MC_DIR_PRIVATE_ACCESS` - private 디렉토리에 접근
  - `MC_DIR_SHARED_ACCESS` - shared 디렉토리에 접근
  - `MC_DIR_SYSTEM_ACCESS` - system 디렉토리에 접근

**반환 값**

성공
- 0

실패
- `M_E_ERROR` – 기타 이유로 실패
- `M_E_BADFILENAME` - 파일이름 형식이 잘못됨
- `M_E_LONGNAME` - 파일이름의 길이가 최대 길이를 초과할 경우
- `M_E_ACCESS` - 파일을 접근할 수 없음

**부작용**

없음

**참고 항목**

mkdir aMode 의미 참조

### MC_fsRemove

**설명**

파일을 삭제한다. 이미 열려 있는 파일은 지울 수 없다.

**프로토타입**

```c
M_Int32 MC_fsRemove(M_Char* name, M_Int32 aMode)
```

**매개 변수**

- `name` - 파일 이름
- `aMode`
  - `MC_DIR_PRIVATE_ACCESS` - private 디렉토리에 접근
  - `MC_DIR_SHARED_ACCESS` - shared 디렉토리에 접근
  - `MC_DIR_SYSTEM_ACCESS` - system 디렉토리에 접근

**반환 값**

성공
- 0

실패
- `M_E_ERROR` – 기타 이유로 실패
- `M_E_BADFILENAME` - 파일이름 형식이 잘못됨
- `M_E_LONGNAME` - 파일이름의 길이가 최대 길이를 초과할 경우
- `M_E_NOENT` - 파일이 존재하지 않음
- `M_E_ACCESS` - 파일을 접근할 수 없음

**부작용**

없음

**참고 항목**

mkdir aMode 의미 참조

### MC_fsRename

**설명**

파일이름을 변경한다. 변경할려고 하는 파일이름이 이미 존재할 경우는 이름을 변경할 수 없다.

**프로토타입**

```c
M_Int32 MC_fsRename(M_Char* oldname, M_Char* newname, M_Int32 aMode)
```

**매개 변수**

- `oldname` - 변경전 파일이름
- `newname` - 변경할 파일이름
- `aMode`
  - `MC_DIR_PRIVATE_ACCESS` - private 디렉토리에 접근
  - `MC_DIR_SHARED_ACCESS` - shared 디렉토리에 접근
  - `MC_DIR_SYSTEM_ACCESS` - system 디렉토리에 접근

**반환 값**

성공
- 0

실패
- `M_E_ERROR` - 기타 이유로 실패
- `M_E_BADFILENAME` - 파일이름 형식이 잘못됨
- `M_E_LONGNAME` - 파일이름의 길이가 최대 길이를 초과할 경우
- `M_E_EXIST` - 변경할려고 하는 파일이름이 존재함
- `M_E_NOSPACE` - 파일시스템의 여유공간이 없음
- `M_E_ACCESS` - 파일을 접근할 수 없음

**부작용**

없음

**참고 항목**

mkdir aMode 의미 참조

### MC_fsMkDir

**설명**

디렉토리를 만든다. 프로그램은 aMode 의 값에 따라 접근 권한이 다른 영역에 디 렉토리를 만들 수 있다.

**프로토타입**

```c
M_Int32 MC_fsMkDir(M_Char* dirName, M_Int32 aMode)
```

**매개 변수**

- `dirName` - 디렉토리 이름
- `aMode`
  - `MC_DIR_PRIVATE_ACCESS` - private 디렉토리에 접근
  - `MC_DIR_SHARED_ACCESS` - shared 디렉토리에 접근
  - `MC_DIR_SYSTEM_ACCESS` - system 디렉토리에 접근

**반환 값**

성공
- 0

실패
- `M_E_ERROR` – 기타 이유로 실패
- `M_E_EXIST` - 이미 디렉토리가 존재함
- `M_E_NOENT` - parent 디렉토리가 존재하지 않음
- `M_E_BADFILENAME` - 파일이름 형식이 잘못됨
- `M_E_LONGNAME` - 디렉토리 이름의 길이가 최대 길이를 초과할 경우
- `M_E_ACCESS` - 파일을 접근할 수 없음

**부작용**

없음

**참고 항목**

없음

### MC_fsRmDir

**설명**

디렉토리를 삭제한다. 디렉토리 안에 파일이나 하위 디렉토리가 남아 있을 경우 삭제가 되지 않는다.

**프로토타입**

```c
M_Int32 MC_fsRmDir(M_Char* dirName, M_Int32 aMode)
```

**매개 변수**

- `dirName` - 디렉토리 이름
- `aMode`
  - `MC_DIR_PRIVATE_ACCESS` - private 디렉토리에 접근
  - `MC_DIR_SHARED_ACCESS` - shared 디렉토리에 접근
  - `MC_DIR_SYSTEM_ACCESS` - system 디렉토리에 접근

**반환 값**

성공
- 0

실패
- `M_E_ERROR` – 기타 이유로 실패
- `M_E_NOENT` - 디렉토리가 존재하지 않음
- `M_E_NOTEMPTY` - 디렉토리내에 파일이나 디렉토리가 존재함
- `M_E_BADFILENAME` - 파일이름 형식이 잘못됨
- `M_E_LONGNAME` - 디렉토리 이름의 길이가 최대 길이를 초과할 경우
- `M_E_ACCESS` - 파일을 접근할 수 없음

**부작용**

없음

**참고 항목**

mkdir aMode 의미 참조

### MC_fsList

**설명**

디렉토리안에 존재하는 파일및 디렉토리 이름의 목록을 구한다. 파일및 디렉토리 이름들은 null terminator string 으로 buf 에 연속적으로 저장되어 리턴된다. 목 록의 끝은 null 이 연속적으로 두번온다.

예를 들면 아래와 같다.

만약 디렉토리 안에 파일이 file1 과 file2 라는 이름으로 있을 경우,

`file1\0file2\0\0`

**프로토타입**

```c
M_Int32 MC_fsList(M_Char* name, M_Char* buf, M_Int32 bufSize, M_Int32 aMode)
```

**매개 변수**

- `name` - 디렉토리 이름
- `buf` - 파일및 디렉토리 이름들이 저장되어 return 되는 buf
- `bufSize` - buf 크기
- `aMode`
  - `MC_DIR_PRIVATE_ACCESS` - private 디렉토리에 접근
  - `MC_DIR_SHARED_ACCESS` - shared 디렉토리에 접근
  - `MC_DIR_SYSTEM_ACCESS` - system 디렉토리에 접근

**반환 값**

성공
- 0

실패
- `M_E_ERROR` – 기타 이유로 실패
- `M_E_BADFILENAME` - 파일이름 형식이 잘못됨
- `M_E_LONGNAME` - 디렉토리 이름의 길이가 최대 길이를 초과할 경우
- `M_E_SHORTBUF` - buf 크기가 모자람
- `M_E_ACCESS` - 파일을 접근할 수 없음

**부작용**

없음

**참고 항목**

mkdir aMode 의미 참조

### MC_fsTotalSpace

**설명**

파일 시스템 총 공간을 구한다

**프로토타입**

```c
M_Int32 MC_fsTotalSpace()
```

**반환 값**

성공
- 파일 시스템 전체 크기(byte)

실패
- `M_E_ERROR` – 기타 이유로 실패

**부작용**

없음

**참고 항목**

없음

### MC_fsAvailable 설명

파일 시스템에서 남아있는 공간을 구한다

**프로토타입**

```c
M_Int32 MC_fsAvailable()
```

**반환 값**

성공
- 남아있는 파일 시스템 크기(byte) 

실패
- `M_E_ERROR` – 기타 이유로 실패

**부작용**

없음

**참고 항목**

없음


### MC_fsSetMode

**설명**
파일의 속성을 변경한다. 변경가능한 속성은 아래의 매개변수 table 의 fmode 값을 참조한다. 기본적으로 모든 응용프로그램은 자기 자신의 디렉토리로는 접근이 가능하고, 나머지 접근 수준은 권한을 받은 프로그램만이 접근 가능하도록 되어있다.


**프로토타입**

```c
M_Int32 MC_fsSetMode(char* fileName, M_Int32 fmode, M_Int32 aMode)
```

**매개 변수**

- [in] `filename` - 파일의 절대 경로명
- [in] `fmode` - 파일 속성 mode
| fmode | 의미 | 값 |
|---|---|:---:|
| `MH_FILEMODE_RDONLY` | 읽기 전용 모드이면 세팅된다. | 1 |
| `MH_FILEMODE_WRONLY` | 쓰기 전용 모드이면 세팅된다. | 2 |
| `MH_FILEMODE_RDWR` | 읽기/쓰기 모드이면 세팅된다. | 3 |
- [in] `aMode`
  - `MC_DIR_PRIVATE_ACCESS` - private 디렉토리에 접근
  - `MC_DIR_SHARED_ACCESS` - shared 디렉토리에 접근
  - `MC_DIR_SYSTEM_ACCESS` - system 디렉토리에 접근

**반환 값**

성공
- `M_E_SUCCESS` – 성공

실패
- `M_E_ERROR` - 기타 이유로 실패
- `M_E_BADPATHNAME` - 파일의 절대 경로명 형식이 잘못됨
- `M_E_LONGNAME` - 파일이름의 길이가 최대 길이를 초과할 경우
- `M_E_INVALID` - mode 가 잘못됨
- `M_E_ACCESS` - 파일을 접근할 수 없음
- `M_E_NOENT` – 파일이 존재하지 않음

**부작용**

없음

**참고 항목**

없음


### MC_fsGetCounts

**설명**
디렉토리내의 파일의 개수를 가져온다. 파일의 개수는 서브디렉토리를 포함한 값 이다.

**프로토타입**

```c
M_int32 MC_fsGetCounts(char* dirName, M_Int32 aMode)
```

**매개 변수**

- `dirName` - 디렉토리 이름
- `aMode`
  - `MC_DIR_PRIVATE_ACCESS` - private 디렉토리에 접근
  - `MC_DIR_SHARED_ACCESS` - shared 디렉토리에 접근
  - `MC_DIR_SYSTEM_ACCESS` - system 디렉토리에 접근
**반환 값**

성공
- 파일 및 디렉토리의 개수

실패
- `M_E_ERROR` – 실패
- `M_E_BADFILENAME` – 잘못된 경로 이름
- `M_E_LONGNAME` – 디렉토리 이름의 길이가 최대 길이를 초과할 경우
- `M_E_ACCESS` - 파일을 접근할 수 없음

**부작용**

없음

**참고 항목**

없음

### MC_fsTell

**설명**

읽기 쓰기 동작의 기준이 되는 파일내의 현재 위치를 가져온다.

**프로토타입**

```c
M_int32 MC_fsTell(M_int32 fd)
```

**매개 변수**
- `fd` - 파일 식별자

**반환 값**

성공
- 파일 포인터 위치

실패
- `M_E_ERROR` – 기타 이유로 실패
- `M_E_BADFD` - 파일 식별자가 잘못됨

**부작용**

없음

**참고 항목**

없음

### MC_fsIsExist

**설명**

특정 경로상의 파일이 있는지 없는지를 알려준다.

**프로토타입**

```c
M_Int32 MC_fsIsExist(char* fileName, M_Int32 aMode)
```

**매개 변수**

- [in] `fiileName` - 파일 이름
- [in] `aMode`
  - `MC_DIR_PRIVATE_ACCESS` - private 디렉토리에 접근
  - `MC_DIR_SHARED_ACCESS` - shared 디렉토리에 접근
  - `MC_DIR_SYSTEM_ACCESS` - system 디렉토리에 접근

**반환 값**

성공
- `M_E_SUCCESS` – 파일이 존재함

실패
- `M_E_ERROR` – 기타 이유로 실패
- `M_E_BADFILENAME` – 잘못된 경로 이름
- `M_E_LONGNAME` – 경로 이름이 최대 길이 보다 긴 경우
- `M_E_ACCESS` - 파일을 접근할 수 없음
- `M_E_NOENT` – 파일이 존재하지 않음

**부작용**

없음

**참고 항목**

없음
