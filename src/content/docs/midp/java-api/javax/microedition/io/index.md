---
title: "package javax.microedition.io"
---

**See:**
 

          **Description**

## Interface Summary

- [CommConnection](CommConnection.md) — 이 인터페이스는 논리적 직렬 포트 연결을 정의합니다.
- [Connection](../../../../../cldc/java-api/javax/microedition/io/Connection.md) — 일반 연결의 가장 기본적인 유형으로, close 메소드만 정의됩니다.
- [ContentConnection](../../../../../cldc/java-api/javax/microedition/io/ContentConnection.md) — 이 인터페이스는 내용이 전달되는 스트림 연결을 정의합니다.
- [Datagram](../../../../../cldc/java-api/javax/microedition/io/Datagram.md) — 이것은 일반 데이터그램 인터페이스로, 데이터그램 연결에서 보내거나 수신되는 데이터의 소유자 역할을 하는 객체를 나타냅니다.
- [DatagramConnection](../../../../../cldc/java-api/javax/microedition/io/DatagramConnection.md) — 이 인터페이스는 데이터그램 연결에 반드시 필요한 기능을 정의합니다.
- [HttpConnection](HttpConnection.md) — 이 인터페이스는 HTTP 연결에 필요한 메소드와 상수를 정의합니다.
- [HttpsConnection](HttpsConnection.md) — 이 인터페이스는 보안 네트워크 연결을 설정하는 데 필요한 메소드와 상수를 정의합니다.
- [InputConnection](../../../../../cldc/java-api/javax/microedition/io/InputConnection.md) — 이 인터페이스는 입력 스트림 연결에 반드시 필요한 기능을 정의합니다.
- [OutputConnection](../../../../../cldc/java-api/javax/microedition/io/OutputConnection.md) — 이 인터페이스는 출력 스트림 연결에 반드시 필요한 기능을 정의합니다.
- [SecureConnection](SecureConnection.md) — 이 인터페이스는 보안 소켓 스트림 연결을 정의합니다.
- [SecurityInfo](SecurityInfo.md) — 이 인터페이스는 보안 네트워크 연결에 대한 정보를 액세스하는 메소드를 정의합니다.
- [ServerSocketConnection](ServerSocketConnection.md) — 이 인터페이스는 서버 소켓 스트림 연결을 정의합니다.
- [SocketConnection](SocketConnection.md) — 이 인터페이스는 소켓 스트림 연결을 정의합니다.
- [StreamConnection](../../../../../cldc/java-api/javax/microedition/io/StreamConnection.md) — 이 인터페이스는 스트림 연결에 반드시 필요한 기능을 정의합니다.
- [StreamConnectionNotifier](../../../../../cldc/java-api/javax/microedition/io/StreamConnectionNotifier.md) — 이 인터페이스는 연결 알림기에 반드시 필요한 기능을 정의합니다.
- [UDPDatagramConnection](UDPDatagramConnection.md) — 이 인터페이스는 로컬 종점 주소를 알고 있는 데이터그램 연결을 정의합니다.

## Class Summary

- [Connector](Connector.md) — 새로운 연결 객체를 만들기 위한 팩토리 클래스 시스템 등록 정보에서 읽은 플랫폼 이름에서 형성된 이름을 가진 프로토콜 구현 클래스와 응용 프로그램 프로그래머가 제공한 매개 변수 문자열에서 추출한 요청된 연결의 프로토콜 이름을 조회하여 동적으로 연결을 만듭니다.
- [PushRegistry](PushRegistry.md) — PushRegistry 는 인바운드 연결 목록을 유지 관리합니다.

## Exception Summary

- [ConnectionNotFoundException](../../../../../cldc/java-api/javax/microedition/io/ConnectionNotFoundException.md) — 이 클래스는 연결 대상을 찾을 수 없음을 나타내는 데 사용됩니다.
