# package javax.microedition.rms

**See:**
 

          **Description**

## Interface Summary

- [RecordComparator](RecordComparator.md) — 두 레코드를 비교하여(구현 시 정의하는 방법으로) 
일치 여부 또는 상대적 정렬 순서를 확인하는 비교기를 정의하는 인터페이스.
- [RecordEnumeration](RecordEnumeration.md) — 양방향 레코드 저장소 Record 열거자를 표시하는 인터페이스.
- [RecordFilter](RecordFilter.md) — 레코드가 일치하는지(응용 프로그램이 정의한 기준에 기반하여) 
조사하는 필터를 정의하는 인터페이스.
- [RecordListener](RecordListener.md) — 레코드 저장소에서 레코드 변경/추가/삭제 
이벤트를 수신하는 수신기 인터페이스

## Class Summary

- [RecordStore](RecordStore.md) — 레코드 저장소를 나타내는 클래스.

## Exception Summary

- [InvalidRecordIDException](InvalidRecordIDException.md) — 레코드 ID가 유효하지 않아 작업이 완료될 수 없음을 
표시하기 위해 발생합니다.
- [RecordStoreException](RecordStoreException.md) — 레코드 저장소 작업에서 일반 예외가 발생했음을 표시하기 위해 발생합니다.
- [RecordStoreFullException](RecordStoreFullException.md) — 레코드 저장 시스템 저장소가 가득 차서 작업을 완료할 수 없음을 
표시하기 위해 발생합니다.
- [RecordStoreNotFoundException](RecordStoreNotFoundException.md) — 레코드 저장소를 찾을 수 없어 
작업을 완료할 수 없음을 표시하기 위해 발생합니다.
- [RecordStoreNotOpenException](RecordStoreNotOpenException.md) — 닫힌 레코드 저장소에서 작업을 시도하였음을 표시하기 위해 발생합니다.
