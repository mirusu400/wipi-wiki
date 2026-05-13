# 4.1. TYPE DEFINITION

변수 타입을 정의한다.

```c
typedef unsigned char M_Boolean	// unsigned 8bit. TRUE 또는 FALSE 를 CHECK 한다.
typedef unsigned int M_Uint32	// unsigned 32 bit type typedef unsigned short M_Uint16	// unsigned 16bit type
typedef unsigned char M_Uint8	// unsigned 8bit type, unsigned char type
typedef signed int M_Int32	// signed 32bit type. signed int type
typedef signed short M_Int16	// signed 16bit type. signed short typedef signed char M_Int8	// signed 8bit type. signed char typedef char M_Char	// char
typedef unsigned char M_Byte	// unsigned 8bit type. unsigned char type
typedef signed long long M_Int64	// signed 64bit type. signed long long type
typedef unsigned long long M_Uint64	// unsigned 64bit type. unsigned long long type
typedef unsigned short M_Ucode		// unsigned 16bit. unicode character typedef signed long M_Sint31		// signed 32bit. singed long type typedef signed short M_Sint15		// signed 16bit. signed short type typedef M_Uint32 M_Addr	// unsigned 32bit. unsigned int type
#define NULL	0	//NULL 정의
#define TRUE  1	//TRUE 정의
#define FALSE  0	//FALSE 정의
#define inline __inline	//inline 정의
```
