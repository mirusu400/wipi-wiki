# package java.io

**See:**
 

          **Description**

## Interface Summary

- [DataInput](DataInput.md) — DataInput 인터페이스는 이진 스트림에서 바이트를 읽어 Java 프리미티브 유형 중 하나로 데이터를 재구성합니다.
- [DataOutput](DataOutput.md) — DataOutput 인터페이스는 Java 프리미티브 유형의 데이터를 일련의 바이트로 변환하여 이진 스트림으로 쓰는 기능을 제공합니다.

## Class Summary

- [ByteArrayInputStream](ByteArrayInputStream.md) — ByteArrayInputStream 에는 스트림에서 읽을 수 있는 바이트가 포함되는 내부 버퍼가 있습니다.
- [ByteArrayOutputStream](ByteArrayOutputStream.md) — 이 클래스는 데이터를 바이트 배열에 쓰는 출력 스트림을 구현합니다.
- [DataInputStream](DataInputStream.md) — 데이터 입력 스트림은 응용 프로그램이 시스템에 독립적인 방법으로 기본 입력 스트림에서 프리미티브 Java 데이터 유형을 읽을 수 있도록 합니다.
- [DataOutputStream](DataOutputStream.md) — 데이터 출력 스트림은 응용 프로그램이 이식 가능한 방법으로 프리미티브 Java 데이터 유형을 출력 스트림에 쓸 수 있도록 합니다.
- [InputStream](InputStream.md) — 이 추상 클래스는 바이트 입력 스트림을 나타내는 모든 클래스의 수퍼 클래스입니다.
- [InputStreamReader](InputStreamReader.md) — InputStreamReader가 바이트 스트림에서 문자 스트림으로의 브릿지 역할을 하는 경우 바이트를 읽어 문자로 변환합니다.
- [OutputStream](OutputStream.md) — 이 추상 클래스는 바이트 출력 스트림을 나타내는 모든 클래스의 수퍼 클래스입니다.
- [OutputStreamWriter](OutputStreamWriter.md) — OutputStreamWriter가 문자 스트림에서 바이트 스트림으로의 브릿지 역할을 하는 경우 기록된 문자를 바이트로 변환합니다.
- [PrintStream](PrintStream.md) — PrintStream 은 다양한 데이터 값 표현의 편리한 인쇄 기능 등을 다른 출력 스트림에 추가합니다.
- [Reader](Reader.md) — 문자 스트림을 읽기 위한 추상 클래스.
- [Writer](Writer.md) — 문자 스트림에 쓰기 위한 추상 클래스 서브 클래스가 구현해야 하는 유일한 메소드는 write(char[], int, int), flush() 및 close()입니다.

## Exception Summary

- [EOFException](EOFException.md) — 입력 중에 예기치 않게 파일 또는 스트림의 끝에 도달하였음을 나타냅니다.
- [InterruptedIOException](InterruptedIOException.md) — I/O 작업이 중단되었음을 나타냅니다.
- [IOException](IOException.md) — 일종의 I/O 예외가 발생했음을 나타냅니다.
- [UnsupportedEncodingException](UnsupportedEncodingException.md) — 문자 인코딩은 지원되지 않습니다.
- [UTFDataFormatException](UTFDataFormatException.md) — 데이터 입력 스트림이나 데이터 입력 스트림을 구현하는 클래스에서 형식이 잘못된 UTF-8 문자열을 읽었음을 나타냅니다.
