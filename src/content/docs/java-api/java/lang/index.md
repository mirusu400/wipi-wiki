---
title: "package java.lang"
---

## Interface Summary

- [Runnable](runnable/) — Thread.start를 사용해서 active되는 클래스는 모두 이 인터페이스를 구현 해야 된다.

## Class Summary

- [Boolean](boolean/) — Primitive 타입인 Boolean 타입을 지원하기 위한 Wrap 클래스.
- [Byte](byte/) — Primitive 타입인 Byte 타입을 지원하기 위한 Wrap 클래스.
- [Character](character/) — Primitive 타입인 char 타입을 지원하기 위한 Wrap 클래스.
- [Class](class/) — Java에서 사용하는 class나 Interface를 대표하는 클래스.
- [Double](double/) — 
- [Float](float/) — 
- [Integer](integer/) — Primitive 타입인 Int 타입을 지원하기 위한 Wrap 클래스.
- [Long](long/) — Primitive 타입인 Long 타입을 지원하기 위한 Wrap 클래스.
- [Math](math/) — 기본적인 수칙연산을 포함한 클래스.
- [Object](object/) — Java 클래스 계층의 루트 클래스.
- [Runtime](runtime/) — VM에 Runtime객체는 하나만 존재하며 이 객체를 통해 프로그램이 동작하는 환경에 대한 정보를 얻을 수 있다.
- [Short](short/) — Primitive 타입인 Short 타입을 지원하기 위한 Wrap 클래스.
- [String](string/) — 문자열을 지원하는 클래스.
- [StringBuffer](stringbuffer/) — 문자들이 저장될 버퍼와 버퍼에 대한 삽입,확장,제거등에 대한 메소드가 정의 된 클래스.
- [System](system/) — VM에 관련된 기능과 유용한 메소드 등을 모아놓은 클래스.
- [Thread](thread/) — VM에서 사용하는 쓰레드에 관한 클래스.
- [Throwable](throwable/) — Java에서 발생하는 Error나Exception의 최상위 클래스.

## Exception Summary

- [ArithmeticException](arithmeticexception/) — 0으로 나누기와 같은 수칙 연산 시 올바르게 대처할 수 없는 문제 발생 시 발생되는 Exception 클래스.
- [ArrayIndexOutOfBoundsException](arrayindexoutofboundsexception/) — 배열 참조시 배열 범위를 벋어나는 인덱스를 사용할 때 발생하는 Exception 클래스.
- [ArrayStoreException](arraystoreexception/) — 배열에 저장할 수 없는 종류의 객체를 저장하려 할 때 발생하는 Exception 클래스.
- [ClassCastException](classcastexception/) — 객체를 변환할 수 없는 타입으로 변환할 때 발생하는 exception 클래스.
- [ClassNotFoundException](classnotfoundexception/) — 찾고자하는 클래스가 없을 때 발생하는 exception 클래스.
- [Exception](exception/) — application에서 대응할 수 있는 오류를 나타낼 때 사용한다.
- [IllegalAccessException](illegalaccessexception/) — 접근 권한이 없는 클래스에 접근하려 할 때 발생하는 exception 클래스.
- [IllegalArgumentException](illegalargumentexception/) — 함수 매개변수 값에 적절하지 않은 값이 할당되면 발생하는 exception 클래스.
- [IllegalMonitorStateException](illegalmonitorstateexception/) — 한 쓰레드가 소유하지 않은 모니터를 사용해서 wait아 notify를 할 때 발생하는 exception 클래스.
- [IllegalStateException](illegalstateexception/) — Signals that a method has been invoked at an illegal or inappropriate time.
- [IllegalThreadStateException](illegalthreadstateexception/) — 쓰레드의 현 상태가 주어진 동작을 취하기에 적절치않은 경우에 발생하는 exception 클래스.
- [IndexOutOfBoundsException](indexoutofboundsexception/) — Vector나 문자열, 배열 같이 인데스를 통해 접근가는한 객체에 범위 밖의 인덱스를 사용할 때 발생하는 exception 클래스.
- [InstantiationException](instantiationexception/) — newInstace를 통해 객체를 생성할 때 클래스가 추상 클래스나 인터페이스일 때 발생하는 exception 클래스.
- [InterruptedException](interruptedexception/) — 한 쓰레드가 wait,sleep,pause瑛

## 기타

- [Error](error/)
- [NegativeArraySizeException](negativearraysizeexception/)
- [NullPointerException](nullpointerexception/)
- [NumberFormatException](numberformatexception/)
- [OutOfMemoryError](outofmemoryerror/)
- [RuntimeException](runtimeexception/)
- [SecurityException](securityexception/)
- [StringIndexOutOfBoundsException](stringindexoutofboundsexception/)
- [VirtualMachineError](virtualmachineerror/)
