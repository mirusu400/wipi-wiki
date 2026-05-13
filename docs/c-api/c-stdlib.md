# 5.1.12. 표준 C 라이브러리 함수

C언어 개발자의 개발 편의를 위해 다음의 표준 C 라이브러리를 지원 해야 한다. 지원 되는 함수들은 ANSI-C 인터페이스와 동일하게 지원한다. 자세한 내역은 다음과 같다.

- 문자열 관련 함수(string.h)
strcpy, strncpy, strcat, strncat, strcmp, strncmp, strchr, strrchr, strspn, strcspn, strpbrk, strstr, strlen, strtok, memcpy, memmove, memcmp, memchr, memset

- 표준 라이브러리 함수(stdlib.h)
atof, atoi, atoll, strtod, strtol, strtoul

- 가변 매개변수 관련 함수(stdarg.h)
va_list, va_start, va_arg, va_end

- 시간 관련(time.h)
clock, time, difftime, mktime, localtime, gmtime
