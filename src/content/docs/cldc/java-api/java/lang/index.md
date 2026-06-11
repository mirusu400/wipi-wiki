---
title: "package java.lang"
---

**See:**
 

          **Description**

## Interface Summary

- [Runnable](Runnable) — Runnable 인터페이스는 스레드가 해당 인스턴스를 실행하는 모든 클래스에서 구현해야 합니다.

## Class Summary

- [Boolean](Boolean) — Boolean 클래스는 프리미티브 유형의 boolean 값을 객체에 포함합니다.
- [Byte](Byte) — Byte 클래스는 바이트 값의 표준 래퍼입니다.
- [Character](Character) — Character 클래스는 프리미티브 유형의 char 값을 객체에 포함합니다.
- [Class](Class) — Class 클래스의 인스턴스는 실행 중인 Java 응용 프로그램의 클래스와 인터페이스를 나타냅니다.
- [Integer](Integer) — Integer 클래스는 프리미티브 유형의 int 값을 객체에 포함합니다.
- [Long](Long) — Long 클래스는 프리미티브 유형의 long 값을 객체에 포함합니다.
- [Math](Math) — Math 클래스에는 기본 수식 작업을 수행하기 위한 메소드가 포함되어 있습니다.
- [Object](Object) — Object 클래스는 클래스 계층 구조의 루트입니다.
- [Runtime](Runtime) — 모든 Java 응용 프로그램에는 응용 프로그램이 실행되는 환경과 상호 작용할 수 있도록 해주는 Runtime 클래스의 단일 인스턴스가 있습니다.
- [Short](Short) — Short 클래스는 short 값의 표준 래퍼입니다.
- [String](String) — String 클래스는 문자열을 나타냅니다.
- [StringBuffer](StringBuffer) — 문자열 버퍼는 가변 문자 시퀀스를 구현합니다.
- [System](System) — System 클래스에는 여러 개의 유용한 클래스 필드와 메소드가 포함되어 있습니다.
- [Thread](Thread) — Thread 는 프로그램의 실행 스레드입니다.
- [Throwable](Throwable) — Throwable 클래스는 Java 언어에서 모든 오류와 예외의 수퍼 클래스입니다.

## Exception Summary

- [ArithmeticException](ArithmeticException) — 예외적인 연산 조건에서 발생합니다.
- [ArrayIndexOutOfBoundsException](ArrayIndexOutOfBoundsException) — 유효하지 않은 색인으로 배열을 액세스했음을 나타냅니다.
- [ArrayStoreException](ArrayStoreException) — 잘못된 유형의 객체를 객체 배열에 저장하려고 시도했음을 나타냅니다.
- [ClassCastException](ClassCastException) — 코드가 객체를 인스턴스가 아닌 서브 클래스로 캐스트하려고 시도했음을 나타냅니다.
- [ClassNotFoundException](ClassNotFoundException) — 응용 프로그램이 Class 클래스의 forName 메소드를 사용하여 문자열 이름을 통해 클래스를 로드하려고 시도하지만 지정된 이름을 가진 클래스 정의를 찾을 수 없을 때 발생합니다.
- [Exception](Exception) — Exception 클래스와 해당 서브 클래스는 합리적 응용 프로그램이라면 파악해야 하는 동작을 나타내는 Throwable 의 한 형태입니다.
- [IllegalAccessException](IllegalAccessException) — 응용 프로그램이 클래스를 로드하려고 시도하지만 클래스가 공용이 아니고 다른 패키지에 있기 때문에 현재 실행 중인 메소드가 지정된 클래스의 정의에 액세스할 수 없을 때 발생합니다.
- [IllegalArgumentException](IllegalArgumentException) — 메소드에 유효하지 않거나 잘못된 인자가 전달되었음을 나타냅니다.
- [IllegalMonitorStateException](IllegalMonitorStateException) — 스레드가 객체의 모니터에서 대기하거나, 지정된 모니터를 소유하지 않고 객체의 모니터에서 대기 중인 다른 스레드에게 알리려고 시도했음을 나타냅니다.
- `IllegalStateException` — 메소드가 부적절하거나 잘못된 시간에 호출되었음을 나타냅니다.
- [IllegalThreadStateException](IllegalThreadStateException) — 스레드가 요청된 작업에 적합한 상태가 아님을 나타냅니다.
- [IndexOutOfBoundsException](IndexOutOfBoundsException) — 배열, 문자열 또는 벡터 등에 대한 색인이 범위를 벗어났음을 나타냅니다.
- [InstantiationException](InstantiationException) — 응용 프로그램이 Class 클래스의 newInstance 메소드를 사용하여 클래스의 인스턴스를 만들려고 시도하지만 지정된 클래스 객체가 인터페이스이거나 추상 클래스여서 인스턴스화할 수 없을 때 발생합니다.
- [InterruptedException](InterruptedException) — 스레드가 대기 또는 휴면 상태이거나 오랫동안 중지되어 다른 스레드가 Thread 클래스의 interrupt 메소드를 사용하여 이를 중단한 경우에 발생합니다.
- [NegativeArraySizeException](NegativeArraySizeException) — 응용 프로그램이 음수 크기를 사용하여 배열을 만들려고 시도하면 발생합니다.
- [NullPointerException](NullPointerException) — 객체가 요구되는 경우에 응용 프로그램이 null 을 사용하려고 시도하면 발생합니다.
- [NumberFormatException](NumberFormatException) — 응용 프로그램이 문자열을 숫자 유형 중 하나로 변환하려고 시도했지만 해당 문자열의 형식이 잘못되었음을 나타냅니다.
- [RuntimeException](RuntimeException) — RuntimeException 은 Java 가상 머신의 정상 작동 중에 발생할 수 있는 예외 수퍼 클래스입니다.
- [SecurityException](SecurityException) — 보안 위반을 나타내기 위해 보안 관리자에서 발생합니다.
- [StringIndexOutOfBoundsException](StringIndexOutOfBoundsException) — 색인이 음수이거나 문자열 크기보다 크거나 같다는 것을 나타내기 위해 String 클래스의 charAt 메소드와 다른 String 메소드에서 발생합니다.

## Error Summary

- [Error](Error) — Error 는 합리적 응용 프로그램이라면 파악하려고 시도해서는 안 되는 심각한 문제를 나타내는 Throwable 의 서브 클래스입니다.
- [OutOfMemoryError](OutOfMemoryError) — Java 가상 머신이 메모리 부족으로 객체를 할당할 수 없으며 가비지 컬렉터에서 추가 메모리를 제공할 수 없는 경우에 발생합니다.
- [VirtualMachineError](VirtualMachineError) — Java 가상 머신에 장애가 발생했거나 계속 작동하는 데 필요한 자원이 떨어졌음을 나타냅니다.

## 기타

- [Double](Double)
- [Float](Float)
- [NoClassDefFoundError](NoClassDefFoundError)
