# 4.11. FILE

File System 함수들이다.

모두 API 의 파일 path 는 절대 path 로 접근 된다. 파일 관련 함수는 모두 blocking함수들이다. 파일식별자는 플랫폼에서 조사하여 HAL API를 부르므로 HAL 에서 잘못된 식별자인지를 다시 조사할 필요는 없다.

- 관련 자료형
```c
#define MH_FILE_OPEN_RDONLY 0x1 // (O_RDONLY)
#define MH_FILE_OPEN_WRONLY 0x2 // (O_WRONLY|O_CREAT)
#define MH_FILE_OPEN_WRTRUNC 0x4 //
(O_WRONLY|O_CREAT|O_TRUNC)
#define MH_FILE_OPEN_RDWR 0x8 // (O_RDWR|O_CREAT|O_BINARY)
#define MH_FILE_SEEK_SET 0
#define MH_FILE_SEEK_CUR 1
#define MH_FILE_SEEK_END 2
#define MH_FILE_IS_DIR 0x01
typedef struct _fileInfo MH_FileInfo {
M_Int32 attrib // 파일의 특성을 표시한 bit mask 들 (디렉토
리 여부, 읽기 전용)
M_Uint32 creationTime // 파일이 생성된 시간을 초단위로 표현되며 지
역별 시간
M_Uint32 size // 파일의 크기
};
```

### MH_fileAttribute

**설명**

파일이나 디렉터리의 특성을 읽어온다.

예를 들어 이 파일이 디렉터리 인지 파일인지, 만든 시간은 언제인지 등을 읽어온 다.

**프로토타입**

```c
M_Int32 MH_fileAttribute (M_Char* pathname, MH_FileInfo* fi)
```

**매개 변수**

[in] pathname 파일이나 디렉터리의 절대 경로명 [out] fi 파일의 특성을 담을 구조체

**반환 값**

성공 실패 M_E_BADFILENAME - 경로명 형식이 잘못된 경우 M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_ERROR - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileAvailable

**설명**

파일 시스템의 여유공간을 알려준다.

**프로토타입**

```c
M_Int32 MH_fileAvailable (void)
```

**매개 변수**

없음

**반환 값**

성공 시스템의 여유 공간의 바이트 단위의 크기를 반환한다.

실패 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileClose

**설명**

파일을 닫는다.

**프로토타입**

```c
M_Int32 MH_fileClose (M_Int32 fd)
```

**매개 변수**

[in] fd 파일 식별자

**반환 값**

성공 실패 M_E_ERROR

**부작용**

없음

**참고 항목**

없음

### MH_fileList

**설명**

해당 디렉터리 내에 있는 파일과 하위 디렉터리를 보여준다. 파일과 디렉터리 이 름은 buf 에 NULL 문자 ('\0')로 구분되며 끝은 연속된 NULL 문자 두 개로 표시된 다.

**프로토타입**

```c
M_Int32 MH_fileList (M_Char *root, M_Char* buf, M_Int32 bufSize)
```

**매개 변수**

[in] root 디렉터리 이름 [out] buf 파일과 디렉터리 이름을 담을 버퍼 [in] bufSize buf의 크기

**반환 값**

성공 실패 M_E_SHORTBUF - 버퍼 사이즈가 모자랄 경우 M_E_BADFILENAME - 파일이름 형식이 잘못된 경우 M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_ERROR - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileMkDir

**설명**

디렉터리를 만든다.

**프로토타입**

```c
M_Int32 MH_fileMkDir (M_Char * dirname)
```

**매개 변수**

[in] dirname 만들 디렉터리 절대 경로명

**반환 값**

성공 실패 M_E_BADFILENAME - 파일 이름 형식이 잘못된 경우 M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_NOENT - 만들고자 하는 디렉터리의 상위 디렉터리가 없을 경우 M_E_EXIST - 이미 디렉터리가 존재할 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileOpen

**설명**

파일을 연다.

flag는 다음과 같은 값을 가질 수 있다.

flag 설명 MH_FILE_OPEN_RDONLY 읽기 전용으로 파일을 연다.

MH_FILE_OPEN_WRONLY 쓰기 전용으로 파일을 쓰는 내용은 파일의 끝에 붙다.

MH_FILE_OPEN_WRTRUNC 쓰기 전용으로 파일을 열고 기존의 파일의 길이를 0으로 만든다.

MH_FILE_OPEN_RDWR 파일을 읽기 쓰기 모두 가능하도록 연다.

**프로토타입**

```c
M_Int32 MH_fileOpen (M_Char* pathname, M_Int32 flag)
```

**매개 변수**

[in] pathname 파일의 절대 경로 [in] flag 위 표 참조

**반환 값**

성공 file 식별자를 반환 실패 M_E_NOENT - MH_FILE_OPEN_RDONLY로 열 때 파일이 없을 경우 M_E_BADFILENAME - 파일이름 형식이 잘못되었을 경우 M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_INVALID - 정해진 open option 이외의 option이 parameter로 들어왔 을 경우 M_E_NOSPACE - 파일시스템에 여유 공간이 없을 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileRead

**설명**

파일에서 buf로 크기만큼 읽어온다.

**프로토타입**

```c
M_Int32 MH_fileRead (M_Int32 fd, M_Char* buf, M_Int32 size)
```

**매개 변수**

[in] fd 파일 식별자 [out] buf buffer pointer [in] size buffer size

**반환 값**

성공 읽은 바이트 수 Size가 0인 경우는 0를 반환한다.

0인 경우는 EOF이다.

실패 M_E_EOF - 파일의 끝까지 읽었을 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileRemove

**설명**

파일을 지운다. 이미 열려 있는 파일일 경우는 지울 수 없다.

**프로토타입**

```c
M_Int32 MH_fileRemove (M_Char* pathname)
```

**매개 변수**

[in] pathname 파일 절대 경로

**반환 값**

성공 실패 M_E_NOENT - 파일이 존재하지 않을 경우 M_E_INUSE -파일이 이미 열려 있는 경우 M_E_BADFILENAME - 파일이름 형식이 잘못되었을 경우 M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_ERROR - 기타 이유로 실패한 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileRename

**설명**

파일 이름을 바꾼다

**프로토타입**

```c
M_Int32 MH_fileRename (M_Char *oldname, M_Char *newname)
```

**매개 변수**

[in] oldname 바꾸기 전 절대 경로명 [in] newname 바뀐 후 절대 경로명

**반환 값**

성공 실패 M_E_BADFILENAME - 파일이름 형식이 잘못된 경우 M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_NOSPACE - 파일시스템에 여유공간이 없을 경우 M_E_ERROR - 기타 이유로 실패한 경우 M_E_NOENT – 바꾸기 전 파일이 존재하지 않을 경우 M_E_EXIST - 새롭게 바꿀 파일 이름이 이미 존재하는 경우 M_E_INUSE - 바꾸기 전 파일이 이미 열려 있을 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileRmDir

**설명**

디렉터리를 지운다.

지울 디렉터리 안에는 파일이나 디렉터리가 존재하지 않아야 한다

**프로토타입**

```c
M_Int32 MH_fileRmDir (M_Char * dirname)
```

**매개 변수**

[in] dirname 지울 디렉터리 절대 경로

**반환 값**

성공 실패 M_E_BADFILENAME - 파일 이름 형식이 잘못된 경우 M_E_LONGNAME - 파일 이름이 최대 길이 보다 긴 경우 M_E_NOTEMPTY - 디렉터리 내에 파일이나 디렉터리가 존재할 경우 M_E_NOENT - 디렉터리가 이미 없을 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileSeek

**설명**

파일 포인터를 특정 위치로 옮긴다.

옮길 위치계산은 파일의 제일 처음부터 pos만큼 또는 제일 끝에서 pos만큼, 아니 면 현재 위치에서 pos만큼 과 같이 3가지로 구분 지을 수 있다

**프로토타입**

```c
M_Int32 MH_fileSeek (M_Int32 fd, M_Int32 pos, M_Int32 where)
```

**매개 변수**

[in] fd 파일 식별자 [in] pos 기준점으로부터 옮길 위치, 파일의 크기내에서 양수/음 수 모두 가능 [in] where MH_FILE_SEEK_SET, MH_FILE_SEEK_CUR, MH_FILE_SEEK_END 중 하나

**반환 값**

성공 옮겨진 파일 포인터의 위치 실패 M_E_INVALID - 기준점이 MH_FILE_SEEK_SET,MH_FILE_SEEK_CUR, MH_FILE_SEEK_END 중 하나에 포함되지 않을 경우 M_E_BADSEEKPOS - 파일 포인터를 옮길 위치가 파일의 범위를 넘어설 경우 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileWrite

**설명**

fd 라는 식별자를 가지는 파일에 buf가 가리키는 위치의 데이터를 지정한 size만 큼 쓴다. 파일 시스템에 공간이 부족해서 요청한 파일을 다 쓸 수 없을 경우 쓴 바이트 수를 반환한다.

**프로토타입**

```c
M_Int32 MH_fileWrite (M_Int32 fd, M_Char* buf, M_Int32 size)
```

**매개 변수**

[in] fd 파일 식별자 [in] buf 버퍼 포인터 [in] size write할 바이트 개수

**반환 값**

성공 write한 바이트 수 실패 M_E_ERROR - 기타 이유로 실패할 경우 M_E_NOSPACE - 파일시스템에 여유공간이 없을 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileTotalSpace

**설명**

파일 시스템의 여유공간을 알려준다.

**프로토타입**

```c
M_Int32 MH_fileTotalSpace (void)
```

**매개 변수**

없음

**반환 값**

성공 파일 시스템의 전체 공간의 바이트 단위의 크기를 반환한다.

실패 M_E_ERROR - 기타 이유로 실패할 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileSetMode

**설명**

파일의 속성을 변경한다. 변경가능 한 속성은 아래의 매개변수 table 의 fmode 값 을 참조한다.

**프로토타입**

```c
M_Int32 MH_fileSetMode(char* pathName, M_Int32 mode)
```

**매개 변수**

[in] pathName 파일의 절대 경로명 [in] fmode 파일 속성 mode fmode 의미 값 MH_FILEMODE_RDONLY 읽기 전용모드이면 세팅된다 1 MH_FILEMODE_WRONLY 쓰기 전용모드이면 세팅된다. 2 MH_FILEMODE_RDWR 읽기/쓰기 모드이면 세팅된다. 3

**반환 값**

성공 M_E_SUCCESS – 성공 실패 M_E_ERROR - 기타 이유로 실패 M_E_BADFILENAME – 파일이름 형식이 잘못됨 M_E_LONGNAME - 파일이름의 길이가 최대 길이를 초과할 경우 M_E_INVALID - mode가 잘못됨 M_E_NOENT – 파일이 존재하지 않음

**부작용**

없음

**참고 항목**

없음

### MH_fileGetCounts

**설명**

디렉토리내의 파일의 개수를 가져온다. 파일의 개수는 서브디렉토리를 포함한 값 이다.

**프로토타입**

```c
M_Int32 MH_fileGetCounts(char* pathName)
```

**매개 변수**

[in] pathName 디렉토리의 절대 경로 명

**반환 값**

성공 디렉토리내 파일 및 디렉토리의 개수 실패 M_E_ACCESS - 파일을 접근할 수 없음 M_E_ERROR - 기타 이유로 실패 M_E_BADFILENAME - 잘못된 경로 이름 M_E_LONGNAME - 디렉토리 이름의 길이가 최대 길이를 초과할 경우

**부작용**

없음

**참고 항목**

없음

### MH_fileIsExist

**설명**

특정 경로상의 파일이 있는지 없는지를 알려준다.

**프로토타입**

```c
M_Int32 MH_fileIsExist(char* pathName)
```

**매개 변수**

[in] pathName 파일의 절대 경로 명

**반환 값**

성공 M_E_SUCCESS – 파일이 존재함 실패 M_E_ACCESS - 파일을 접근할 수 없음 M_E_ERROR – 기타 이유로 실패 M_E_BADFILENAME – 잘못된 경로 이름 M_E_LONGNAME – 경로 이름이 최대 길이 보다 긴 경우 M_E_NOENT – 파일이 존재하지 않음

**부작용**

없음

### MH_fileTell

**설명**

현재 파일의 입출력 포인터를 반환해 준다.

**프로토타입**

```c
M_Int32 MH_fileTell(M_Int32 fd)
```

**매개 변수**

[in] fd 파일 식별자

**반환 값**

성공 현재 입출력 포인터 위치 실패 M_E_INVALIDFD - 잘못된 파일 식별자 M_E_ERROR – 기타 이유로 실패

**부작용**

없음

**참고 항목**

없음
