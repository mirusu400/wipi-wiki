---
title: "OTA (Over-The-Air) 규격"
---

# Over The Air User Initiated Provisioning 사양

#### MIDP (Mobile Information Device Profile)용

---

## 머리말

*Over The Air User Initiated Provisioning* 문서는  MIDP (Mobile Information Device Profile) 사양 버전 2.0을 위한 것입니다. 원본 JSR과 전문가 그룹 세부 정보는 http://jcp.org/jsr/detail/118.jsp에서 찾을 수 있습니다. 여기서 사용되는 용어는 별도의 지침이 없는 한 MIDP 2.0 사양의 정의 절에 정의되어 있습니다.

### 본 사양의 구성 방법

본 사양의 주제는 다음과 같은 절로 구성되어 있습니다.

- *1절, "Over The Air User Initiated Provisioning"*에서는 MIDP 응용 프로그램을 어떻게 무선 장치에 배포해야 하는지에 대해 정의합니다.
- *2절, "WAP June2000 환경에서의 MIDP 프로비저닝 및 네트워킹"*에서는 프록시 WAP 게이트웨이를 통해 MIDP 응용 프로그램을 배포할 때의 특정 요구 사항에 대해 설명합니다.

### 참조 자료

1. Connected, Limited Device Configuration (CLDC)  
    http://jcp.org/jsr/detail/30.jsp
2. Mobile Information Device Profile (MIDP 1.0)  
    http://jcp.org/jsr/detail/37.jsp
3. Mobile Information Device Profile 2.0 (MIDP 2.0)  
    http://jcp.org/jsr/detail/118.jsp
4. HTTP 1.1 Specification  
    http://www.ietf.org/rfc/rfc2616.txt
5. HTTP Authentication: Basic and Digest Access Authentication  
    http://www.ietf.org/rfc/rfc2617.txt
6. Java(tm) Servlet 2.3 Specification  
    http://jcp.org/jsr/detail/53.jsp

### OTA 권장 방법 이후의 변경 사항

MIDP 1.0 사양이 발행된 후 *Over The Air User Initiated Provisioning Recommended Practice for the Mobile Information Device Profile* 문서가 발행되었습니다. 본 사양은 이 문서를 대신하며, MIDP 2.0에 대해 다음과 같은 사항이 변경되었습니다.

- 쿠키 지원 요구 사항이 제거되었습니다. 일부 네트워크 구조에서 쿠키 정보를 클라이언트에 전송하지 못할 수도 있기 때문에 변경된 사항입니다. 쿠키는 응용 프로그램 설명자, JAR 다운로드 및 Install-Notify 보고서 간에 상태 정보를 유지 관리하는 데 사용됩니다. URL을 다시 쓰는 대안적 방법도 같은 용도로 사용할 수 있습니다. 예를 들어, 응용 프로그램 설명자를 보낼 때 서버에서 특정 다운로드 세션과 연결하는 고유 JAR, MIDlet-Install-Notify 및 MIDlet-Delete-Notify URL을 삽입할 수 있습니다. 다른 옵션을 사용할 수도 있습니다.

## 1절, Over The Air User Initiated Provisioning

### 개요 및 목적

본 문서는 MIDlet Suite를 어떻게 Over-The-Air (OTA)로 배포할 수 있는지, 그리고 이러한 배포를 지원하기 위해 클라이언트 장치에 어떤 요구 사항을 두어야 하는지 설명하기 위해 작성되었습니다. 이러한 권장 사항은 모든 제조업체의 클라이언트와 서버 간에 상호 운용성을 보장하는 데 도움이 되며 MIDP 장치를 배포하는 모바일 네트워크 운영자에게 지침을 제공합니다.

장치는 사용자가 MIDlet Suite를 찾아서 장치에 로드할 수 있도록 하는 기법을 제공해야 합니다. 어떤 경우에는 장치에 있는 브라우저(예: i-mode 또는 WAP)를 통해 MIDlet Suite를 찾습니다. 사용자가 다운로드할 MIDlet Suite를 확인할 수 있도록 특별히 작성된 상주 응용 프로그램이 이러한 기법으로 이용될 수도 있습니다. 본 문서에서는 이 기능을 가진 응용 프로그램을 발견 응용 프로그램, 즉 *DA*라고 합니다.

장치가 다른 설치 기법(예: BluetoothTM 무선 기술, 직렬 케이블, IrDATM 등)을 지원할 수도 있지만 이것은 본 사양의 범위를 벗어납니다.

Application Management Software (AMS)는 MIDlet의 다운로드와 라이프사이클을 관리하는 장치상의 소프트웨어를 설명하는 데 사용되는 일반 용어입니다. 이 용어는 어떠한 특정 구현을 나타내지 않으며 편의상으로만 사용됩니다. 일부 구현에서는 Java Application Manager (JAM)란 용어를 대신 사용합니다.

본 문서에서는 장치 기능에 대한 일반 요구 사항과 MIDlet Suite 라이프사이클을 지원하는 기능에 대해 설명합니다. MIDlet Suite의 라이프사이클은 발견, 설치, 업데이트, 호출 및 제거로 이루어져 있습니다. MIDlet Suite를 제공하는 서버에 장치 유형과 특성을 확인해 주는 기법 및 추가 응용 프로그램 설명자 속성에 대해서도 설명합니다.

### 기능 요구 사항

MIDP 호환 장치는 다음과 같은 기능을 제공해야 합니다.

- 찾아보기 또는 네트워크에서 MIDlet Suite 응용 프로그램 설명자 찾기
- MIDlet Suite 및 관련된 응용 프로그램 설명자를 본 문서에 규정된 대로 HTTP 1.1을 사용하는 서버나 HTTP 1.1 기능(헤더와 엔티티 필드 포함)을 구현하는 세션 프로토콜의 장치로 변환
- 사용자에게 사용자 이름과 암호를 묻고 제공된 인증서를 사용하여 HTTP 요청을 다시 보냄으로써 HTTP 요청에 대한 401(*Unauthorized*) 또는 407(*Proxy Authentication Required*) 응답에 응답. 장치는 최소한 RFC2617 기본 인증 체계를 지원할 수 있어야 합니다.
- 장치에 MIDlet Suite 설치
- MIDlet 호출
- 사용자가 장치에 저장된 MIDlet Suite를 삭제할 수 있도록 허용. MIDlet Suite는 전송 및 설치의 단위가 되기 때문에 단일 MIDlet은 삭제할 수 없습니다.

### MIDlet Suite 발견

응용 프로그램 발견은 사용자가 장치를 사용하여 MIDlet Suite를 찾는 프로세스입니다. 사용자가 시작하는 MIDlet Suite 발견 및 설치를 다음과 같은 고급 방법으로 지원해야 합니다.

- DA를 사용하는 동안 사용자에게 MIDlet Suite나 응용 프로그램 설명자에 대한 링크를 표시합니다.
- 사용자가 설치 프로세스를 시작하는 링크를 선택합니다.
- 사용 가능한 경우, 응용 프로그램 설명자를 먼저 장치로 전송합니다. 이 설명자에는 MIDlet Suite에 대한 정보가 포함되어 있으며 장치의 AMS에서 설치를 시작하기 위해 사용할 수 있습니다.
- 응용 프로그램 설명자를 사용할 수 없거나 AMS가 응용 프로그램을 다운로드하여 설치를 계속하도록 결정한 후 MIDlet Suite JAR 파일 다운로드가 시작됩니다.

DA를 사용하여 네트워크 위치를 액세스할 수 있는 기능과, 선택하면 MIDlet Suite 설치를 시작하는 링크와 함께 MIDlet Suite에 대한 설명을 볼 수 있는 기능을 사용자에게 제공하는 것이 좋습니다. MIDP 사양에 설명된 것처럼 링크가 JAR 파일을 참조하면 설치 프로세스를 시작하기 위해 JAR 파일과 해당 URL이 장치상의 AMS로 전달됩니다. MIDP 사양에 설명된 것처럼 링크가 응용 프로그램 설명자를 참조하는 경우에는 다음과 같습니다.

1. 링크를 선택하면 서버가 이에 대한 응답으로 전송되는 데이터(즉, 응용 프로그램 설명자)에 "*text/vnd.sun.j2me.app-descriptor*"의 MIME 유형이 있음을 표시해야 합니다.
2. 이 전송이 완료되면 설치 프로세스를 시작하기 위해 응용 프로그램 설명자와 해당 URL이 장치상의 AMS로 전달됩니다. AMS는 응용 프로그램 설명자를 사용하여 연결된 MIDlet Suite를 장치에 올바로 설치하여 실행할 수 있는지 확인합니다. 올바로 설치하여 실행할 수 없는 경우에는 사용자에게 설치를 방해하는 요인을 알려야 합니다. 비정상적 상황이 발생하면 시간과 네트워크 대역폭 낭비를 최소화하기 위해 가능하면 일찍 사용자에게 알려주는 것이 좋습니다. 응용 프로그램 설명자를 검색할 때는 장치 식별 및 요청 헤더에 설명된 요청 헤더 속성을 사용하는 것이 좋습니다.
3. 응용 프로그램 설명자를 사용하려면 먼저 전송 형식에서 MIDP 사양에 규정된 유니코드 인코딩으로 변환해야 합니다. MIME 유형 "*text/vnd.sun.j2me.app-descriptor*"에 지정된 기본 문자 집합은 "*UTF-8*"입니다. 장치가 다른 문자 집합을 지원하면 해당 *Accept-Charset* 헤더를 요청에 포함시키고, *Content-Type* 헤더에 있는 반환된 *charset* 속성에 따라 내용을 변환하는 것이 좋습니다. *charset*이 정의되어 있지 않으면 인코딩은 기본적으로 "*UTF-8*"로 지정되며 이에 따라 내용을 변환하는 것이 좋습니다. 설명자의 속성은 MIDP 사양의 구문에 따라 서식을 지정해야 하며, MIDP 사양에서 요구되는 모든 속성이 설명자에 있어야 합니다. 그렇지 않으면 클라이언트가 상태 보고서에 *상태 코드 906*을 반환해야 합니다.
4. 공급업체, 이름, 버전, 크기 속성 등 응용 프로그램 설명자의 정보를 사용하여 사용자에게 MIDlet Suite 설치를 확인할 수 있는 기회를 주는 것이 좋습니다. 이전 버전을 설치하거나 동일한 버전을 설치하려고 시도하는 경우에는 사용자에게 이를 알려주는 것이 좋습니다. MIDlet Suite의 성공적인 설치와 실행을 방해하는 요인을 확인하여 사용자에게 알려주는 것이 좋습니다. 예를 들어, 메모리가 부족하면 소프트웨어는 사용자가 메모리 사용을 확인하여 새로운 MIDlet Suite의 설치 공간을 확보할 수 있도록 지원하는 것이 좋습니다.

### MIDlet Suite 설치

응용 프로그램 설치는 MIDlet Suite를 장치에 다운로드하여 사용자가 이용할 수 있도록 하는 프로세스입니다. 응용 프로그램 설치를 지원해야 합니다. 장치를 지원하는 네트워크와 프로비저닝 중에 사용되는 모든 프록시 및 원본 서버가 이 요구 사항을 지원할 수 있어야 합니다. 사용자가 장치상의 MIDlet Suite가 사용하는 자원을 제어하고, MIDlet Suite를 삭제하거나 설치할 수 있어야 합니다.

장치는 사용자가 MIDlet Suite의 MIDlet을 실행할 수 있도록 해야 합니다. MIDlet Suite에 여러 개의 MIDlet이 포함되어 있으면 사용자가 두 개 이상의 MIDlet이 있다는 것을 알아야 할 수도 있습니다. 장치는 사용자 선택에 따라 MIDlet Suite의 MIDlet을 즉시 실행할 수도 있습니다.

설치 중에 사용자에게 진행 상황을 알려주는 것이 좋으며, 프로세스를 취소할 수 있는 기회를 주어야 합니다. 설치가 중단되면 장치를 설치가 시작되기 전의 상태로 두어야 합니다.

MIDlet Suite가 이미 장치에 설치되어 있으면 업데이트로 처리되는 것이 좋습니다. 업데이트 처리 방법에 대한 자세한 내용은 MIDlet Suite 업데이트를 참조하십시오.

MIDlet Suite를 설치하기 위해 AMS는 다음과 같은 일련의 단계를 수행하며, 진행 상황을 확인하여 사용자에게 피드백을 제공합니다.

1. 장치가 HTTP를 통해 MIDlet Suite의 다운로드를 시작합니다. MIDlet Suite 발견 절에 설명된 것처럼 응용 프로그램 설명자가 먼저 다운로드된 경우에는 MIDlet Suite에 대한 요청이 정확히 설명자에 지정된 URL에 대한 것이어야 합니다. 다른 헤더는 불필요합니다.
2. 서버 또는 프록시가 MIDlet Suite에 대한 요청에 401(*Unauthorized*) 또는 407(*Proxy Authentication Required*)로 응답하면 장치는 RFC2617에 규정된 *Authorization* 또는 *Proxy-Authorization* 헤더 필드의 사용자 제공 인증서를 사용하여 요청을 다시 보내는 것이 좋습니다. 인증서는 사용자가 제공하는 것이 좋습니다. 예를 들어, 일반 기법에서는 사용자 이름과 암호를 입력할 수 있는 대화 상자를 사용자에게 표시합니다. 장치는 최소한 RFC2617에 설명된 기본 인증 체계를 지원할 수 있어야 합니다.
3. MIDlet Suite와 수신된 헤더를 검토하여 검색한 MIDlet Suite가 유효하며 장치에 설치할 수 있는지 확인해야 합니다. 최소한 설치를 방해하는 다음과 같은 문제점을 사용자에게 경고해야 합니다.

- 장치에 MIDlet Suite를 저장할 메모리가 부족하면 장치가 상태 보고서에 *상태 코드 901*을 반환해야 합니다.
- 설명자의 *MIDlet-Jar-URL* 속성에서 JAR을 사용할 수 없으면 장치가 상태 보고서에 *상태 코드 907*을 반환해야 합니다.
- 수신된 JAR 파일 크기가 응용 프로그램 설명자에 지정된 크기와 일치하지 않으면 장치가 상태 보고서에 *상태 코드 904*를 반환해야 합니다.
- 상세 목록이나 다른 파일을 JAR에서 추출할 수 없으면 장치가 상태 보고서에 *상태 코드 907*을 반환해야 합니다.
- JAR 상세 목록의 구문이 잘못되었거나 JAR 상세 목록에 필수 속성이 없으면 장치가 상태 보고서에 *상태 코드 907*을 반환해야 합니다.
- 설명자의 필수 속성인 "*MIDlet-Name*", "*MIDlet-Version*" 및 "*MIDlet-Vendor*"가 JAR 상세 목록의 속성과 일치하지 않으면 장치가 상태 보고서에 *상태 코드 905*를 반환해야 합니다.
- MIDlet Suite를 신뢰할 수 있으면 MIDlet-\* 속성의 응용 프로그램 설명자에 있는 값이 상세 목록에 있는 해당 속성 값과 일치해야 합니다. 그렇지 않으면 장치가 상태 보고서에 *상태 코드 905*를 반환해야 합니다.
- 응용 프로그램 인증에 실패하면 장치가 상태 보고서에 *상태 코드 909*를 반환해야 합니다.
- 응용 프로그램이 동일한 응용 프로그램의 서명된 설치 버전의 서명되지 않은 버전이면 장치가 상태 보고서에 *상태 코드 910*을 반환해야 합니다.
- *MIDlet-Permissions* 속성에 나열된 권한이 응용 프로그램에 부여되지 않으면 장치가 상태 보고서에 *상태 코드 910*을 반환해야 합니다.
- 권한이 부여되지 않았다는 것 이외의 이유로 정적 푸시 등록에 실패하면 장치가 상태 보고서에 *상태 코드 911*을 반환해야 합니다.
- 설치 중에 네트워크 서비스가 끊어진 경우, 가능하면 상태 보고서에 *상태 코드 903*을 사용하는 것이 좋습니다(네트워크 서비스 장애로 인해 상태 보고서를 전송하지 못할 수도 있음).

4. 설치를 방해하는 요인이 하나도 없을 경우 MIDlet Suite에 포함된 MIDlet이 설치되어야 하며 사용자가 장치의 MIDlet 선택 기법을 통해 실행할 수 있어야 합니다.
5. 장치에서 MIDlet Suite을 사용할 수 있게 되거나 복구할 수 없는 오류가 발생하면 설치가 완료됩니다. 두 경우 모두, 설치 상태 보고서에 설명된 것처럼 상태가 보고되어야 합니다.

## MIDlet Suite 업데이트

MIDlet Suite 업데이트는 동일한 MIDlet Suite(동일한 버전 또는 다른 버전)가 이미 장치에 설치되어 있을 때 특정 MIDlet Suite를 설치하는 작업으로 정의됩니다. 장치는 MIDlet Suite의 업데이트를 지원해야 합니다. 사용자에게 도움이 되도록 장치는 사용자가 장치상의 MIDlet Suite에 대한 정보를 보고 어떤 버전의 소프트웨어가 설치되어 있는지 확인할 수 있도록 해야 합니다. 업데이트에 적용되는 속성은 장치 식별 및 요청 헤더를 참조하십시오.

MIDlet Suite 업데이트가 시작되면 장치는 MIDlet Suite가 기존 MIDlet Suite보다 최신 또는 이전 버전인지, 아니면 동일한 버전인지 사용자에게 알려야 하며 계속하기 전에 사용자 확인을 받아야 합니다.

업데이트되는 MIDlet Suite의 RMS 레코드 저장소는 다음과 같이 관리해야 합니다.

- 새로운 MIDlet Suite와 기존 MIDlet Suite의 암호 서명자가 동일하면 RMS 레코드 저장소를 유지하여 새로운 MIDlet Suite가 사용할 수 있도록 해야 합니다.
- 새로운 응용 프로그램 설명자를 다운로드하는 URL의 체계, 호스트 및 경로가 기존 응용 프로그램 설명자를 다운로드한 URL의 체계, 호스트 및 경로와 일치하면 RMS를 유지하여 새로운 MIDlet Suite가 사용할 수 있도록 해야 합니다.
- 새로운 MIDlet Suite를 다운로드하는 URL의 체계, 호스트 및 경로가 기존 MIDlet Suite를 다운로드한 URL의 체계, 호스트 및 경로와 일치하면 RMS를 유지하여 새로운 MIDlet Suite가 사용할 수 있도록 해야 합니다.
- 위의 요구 사항이 충족되지 않으면 장치는 기존 MIDlet Suite의 데이터를 유지하여 새로운 MIDlet Suite가 사용할 수 있도록 할지 여부를 사용자에게 물어야 합니다.

모든 경우에서 서명되지 않은 MIDlet은 서명된 MIDlet Suite를 업데이트할 수 없도록 해야 합니다. 레코드 저장소의 형식, 내용 및 버전은 MIDlet Suite에서 관리합니다. 사용자가 기존 MIDlet Suite에 부여한 권한이 새로운 MIDlet Suite의 보안 도메인에 있으면 새로운 MIDlet Suite에도 부여하는 것이 좋습니다.

## MIDlet Suite 실행

사용자가 실행할 MIDlet을 선택하면 장치는 MIDP 사양에서 요구되는 CLDC 및 MJIDP 클래스를 사용하여 MIDlet을 호출해야 합니다. 여러 개의 MIDlet이 있으면 사용자 인터페이스에서 사용자가 각 MIDlet을 선택하여 실행할 수 있도록 지원해야 합니다.

## MIDlet Suite 제거

장치는 사용자가 MIDlet Suite를 제거할 수 있도록 지원해야 합니다. 장치에서 MIDlet Suite를 제거하는 경우 사용자에게 MIDlet Suite를 제거할 것인지 확인하는 메시지를 표시하는 것이 좋습니다. 장치는 MIDlet Suite를 삭제하는 동안 발생하는 특수 상황에 대해 사용자에게 경고하는 것이 좋습니다. 예를 들어, MIDlet Suite에 여러 개의 MIDlet이 포함되어 있을 수도 있으므로 사용자에게 모든 MIDlet 및 연결된 RMS 레코드 저장소가 제거된다고 알려주는 것이 좋습니다.

응용 프로그램 설명자에 MIDlet-Delete-Confirm 속성이 있으면 프롬프트에 해당 값을 포함시키는 것이 좋습니다. 이렇게 하면 MIDlet Suite 공급자가 MIDlet Suite를 제거할 경우 발생할 수 있는 모든 특정 상황을 강조할 수 있습니다.

## 설치/삭제 상태 보고서

MIDlet Suite를 제공하는 서비스에서 MIDlet Suite의 설치, 업그레이드 또는 삭제 성공 여부는 매우 중요합니다. 서비스는 설치 및 삭제 상태를 보고하는 데 사용해야 하는 URL을 응용 프로그램 설명자에 지정할 수도 있습니다. 자세한 내용은 추가 설명자 속성을 참조하십시오. 장치에서 설치 상태 보고서를 보낼 수 없는 경우에도 요청된 작업을 완료해야 합니다. 예를 들어, 장치가 설치 상태 보고서를 MIDlet-Install-Notify URL로 보낼 수 없어도 MIDlet Suite를 여전히 사용 가능해야 하며 사용자가 MIDlet Suite를 사용할 수 있어야 합니다. 이와 마찬가지로 장치가 삭제 상태 보고서를 MIDlet-Delete-Notify URL로 보낼 수 없는 경우에도 MIDlet Suite를 삭제해야 합니다.

운영자 상태는 HTTP POST를 통해 설치의 경우 *MIDlet-Install-Notify* 속성에 지정된 URL로, 삭제의 경우 *MIDlet-Delete-Notify* 속성에 지정된 URL로 보고됩니다. 유일하게 지원되는 프로토콜은 "*http://*"입니다. 다른 프로토콜은 장치에서 무시할 수도 있습니다.

POST 요청의 본문 내용에서 첫 번째 줄에는 상태 코드와 상태 메시지가 있어야 합니다. 유효한 코드와 상태 메시지 목록은 상태 코드 및 메시지를 참조하십시오.

삭제 상태 보고서의 경우 알림은 MIDlet을 삭제하는 경우에만 전송됩니다. *상태 코드 912*를 보내 삭제가 발생했다고 알려야 합니다.

서버는 상태 보고서에 응답하여 "*200 OK*"로 응답해야 합니다. 어떠한 내용도 장치로 반환하지 않는 것이 좋으며, 전송될 경우 이 내용을 무시해야 합니다. 응답이 수신되면 요청을 다시 시도하지 않는 것이 좋습니다. MIDP 1.0 OTA 권장 방법과 달리, *cookie*를 삭제하도록 요청하기 위해 *Max-Age=0* 속성이 있는 *Set-Cookie* 헤더를 서버에 포함해서는 안 됩니다. 이러한 속성이 수신되면 장치에서 무시해야 합니다. 일례로, 예: HTTP Post 요청을 통한 설치 상태를 참조하십시오.

설치의 경우, 상태 보고서를 보낼 수 없거나 서버 응답이 수신되지 않으면 이 Suite의 MIDlet을 실행하고 장치에 데이터 네트워크 연결이 있을 때마다 위에서 설명한 것처럼 설치 상태 보고서를 다시 보낼 수도 있습니다. 이렇게 하면 상태 보고서를 보내는 데 성공할 가능성이 커집니다. 재시도를 할 때마다 사용자에게 요금이 청구되므로 재시도 횟수는 작게 유지하는 것이 좋습니다. 설치 상태 보고서의 전송 여부와 응답 수신 여부에 관계 없이 MIDlet Suite를 사용할 수 있도록 해야 합니다.

삭제의 경우, 다음에 OTA 설치를 수행하거나 설치 상태 보고서를 전송할 때 상태 보고서를 보내려고 시도해야 합니다. 이렇게 하면 상태 보고서를 보내는 데 성공할 가능성이 커지며, 네트워크 활동을 볼 때의 사용자 혼동을 최소화할 수 있습니다. 상태 보고서를 보낼 수 없거나 서버 응답이 수신되지 않으면 OTA 설치를 수행하거나 설치 상태 보고서를 보낼 때마다 위에서 설명한 것처럼 삭제 상태 보고서를 다시 보낼 수도 있습니다. 재시도를 할 때마다 사용자에게 요금이 청구되므로 재시도 횟수는 작게 유지하는 것이 좋습니다. 설치 상태 보고서의 전송 여부와 응답 수신 여부에 관계 없이 MIDlet Suite를 메모리에서 제거해야 합니다.

   
**설치 상태 코드 및 메시지**

| 상태 코드 | 상태 메시지 |
| --- | --- |
| 900 | 성공 |
| 901 | 메모리 부족 |
| 902 | 사용자가 취소함 |
| 903 | 서비스가 끊어짐 |
| 904 | JAR 크기가 일치하지 않음 |
| 905 | 속성이 일치하지 않음 |
| 906 | 잘못된 설명자 |
| 907 | 잘못된 JAR |
| 908 | 호환되지 않는 구성 또는 프로필 |
| 909 | 응용 프로그램 인증 실패 |
| 910 | 응용 프로그램 권한 부여 실패 |
| 911 | 푸시 등록 실패 |
| 912 | 삭제 알림 |

## 추가 설명자 속성

응용 프로그램 설명자에는 다음과 같은 추가 속성이 정의되어 있습니다. 각 속성은 설명자에 한 번만 사용할 수 있습니다.

  
**MIDlet 속성**

| 속성 이름 | 속성 설명 |
| --- | --- |
| MIDlet-Install-Notify | 이 MIDlet Suite의 설치 상태(새 설치 또는 MIDlet Suite 업데이트)를 보고하기 위해 POST 요청을 보내는 대상 URL. 장치는 이 URL을 수정하지 않고 사용해야 합니다. URL은 UTF-8 인코딩 문자로 256자를 넘지 않아야 합니다. UTF-8 인코딩 문자로 256자를 넘는 URL을 받을 경우 장치가 설치를 거부하고 상태 보고서에 *상태 코드 906*을 반환해야 합니다. |
| MIDlet-Delete-Notify | MIDlet Suite의 삭제를 보고하기 위해 POST 요청을 보내는 대상 URL. 장치는 이 URL을 수정하지 않고 사용해야 합니다. URL은 256자의 UTF-8 인코딩 문자를 넘지 않아야 합니다. UTF-8 인코딩 문자로 256자를 넘는 URL을 받을 경우 장치가 설치를 거부하고 상태 보고서에 *상태 코드 906*을 반환해야 합니다. |
| MIDlet-Delete-Confirm | 이 MIDlet Suite의 삭제를 확인하는 메시지를 표시할 때 사용자에게 제공하는 텍스트 메시지 |

## 장치 식별 및 요청 헤더

장치는 자신에 대한 정보를 서버로 보낼 때 DA를 통해 MIDlet Suite를 발견하는 프로세스를 사용자 정의할 수 있습니다. 서버가 장치의 기능을 확인할 수 있도록 DA는 네트워크 서버에 정보(예: 제조업체 및 장치 모델 번호)를 제공해야 합니다. 대부분의 경우 DA는 이미 네트워크 연결 및 표시 언어에 맞는 방법으로 서버에 장치 유형을 확인해 주었을 것입니다.

MIDlet Suite를 다운로드하는 동안 장치는 자신의 특성과 요청되는 내용의 유형을 가능한 한 자세히 서버에 확인해 주는 것이 좋습니다. 내용을 가져오는 데 사용되는 HTTP 요청 헤더에는 *User-Agent, Accept-Language* 및 *Accept*가 있어야 합니다. 서버는 이 추가 정보를 사용하여 장치에 적합한 응용 프로그램 설명자를 선택하는 것이 좋습니다.

### User-Agent 제품 토큰

MIDP 사양은 클라이언트를 서버에 확인해 주는 HTTP *User-Agent* 요청 헤더를 식별합니다. RFC2616은 다음과 같은 제품 토큰의 형식을 규정합니다.

*"User-Agent" ":" 1\*(product | comment)*

장치를 지원 CLDC 및 MIDP로 식별하는 데 사용되는 제품 토큰은 MIDP 사양의 네트워킹 부분에 규정되어 있습니다. RFC2616에서와 마찬가지로 설명 필드는 옵션입니다.

또한, 장치는 RFC2616에서 정의된 것처럼 장치별 제품 토큰을 *User-Agent* 헤더에 추가하여 자신을 식별하는 것이 좋습니다. 장치 식별 토큰을 첫 번째 토큰으로 사용하는 것이 좋습니다. 제품 토큰과 제품 버전 값은 각 장치에 고유하므로 본 사양의 범위에서 벗어납니다.

### Accept-Language 헤더

장치는 RFC2616에 규정된 것처럼 *Accept-Language* 요청 헤더를 제공하여 장치에서 사용하는 언어를 나타낼 수도 있습니다.

### Accept 헤더

*Accept* HTTP 헤더는 요청되는 내용의 유형을 나타내는 데 사용됩니다. MIDlet Suite를 요청할 때 이 헤더에는 *application/java-archive*를 포함시키는 것이 좋습니다. 응용 프로그램 설명자를 검색하는 경우에는 이 헤더에 *text/vnd.sun.j2me.app-descriptor*를 포함시키는 것이 좋습니다.

### 예: 응용 프로그램 설명자에 대한 HTTP 요청

응용 프로그램 설명자의 다운로드를 요청할 때 요청 헤더는 다음과 같이 나타날 수 있습니다.

GET http://host.foo.bar/app-dir/game.jad HTTP/1.1  
 Host: host.foo.bar  
 Accept: text/vnd.sun.j2me.app-descriptor  
 User-Agent: CoolPhone/1.4 Profile/MIDP-2.0 Configuration/CLDC-1.0  
 Accept-Language: en-US, fi, fr  
 Accept-Charset: utf-8

서버로부터의 응답 헤더는 다음과 같이 나타날 수 있습니다.

HTTP/1.1 200 OK  
 Server: CoolServer/1.3.12  
 Content-Length: 2345  
 Content-Type: text/vnd.sun.j2me.app-descriptor; charset=utf-8

### 예: MIDlet Suite의 설치/업데이트에 대한 HTTP 요청

MIDlet Suite JAR 파일의 다운로드를 요청할 때 요청 헤더는 다음과 같이 나타날 수 있습니다.

GET http://host.foo.bar/app-dir/game.jar HTTP/1.1  
 Host: host.foo.bar  
 Accept: application/java, application/java-archive

서버로부터의 응답 헤더는 다음과 같이 나타날 수 있습니다.

HTTP/1.1 200 OK  
 Server: CoolServer/1.3.12  
 Content-Length: 25432  
 Content-Type: application/java-archive

### 예: HTTP Post 요청을 통한 설치 상태

아래에 지정된 응용 프로그램 설명자를 사용하여 MIDlet Suite를 설치하는 경우를 예로 들 수 있습니다.

...  
 MIDlet-Install-Notify: http://foo.bar.com/status  
 ...

MIDlet Suite가 설치되면 다음과 같은 내용이 게시됩니다.

POST http://foo.bar.com/status HTTP/1.1  
 Host: foo.bar.com  
 Content-Length: 13  
 900 Success

서버로부터의 응답은 다음과 같이 나타날 수 있습니다.

HTTP/1.1 200 OK  
 Server: CoolServer/1.3.12

## 2절, WAP June2000 환경에서의 MIDP 프로비저닝 및 네트워킹

### 이 절의 목적

이 절은 WAP June2000 환경에서의 MIDP Over The Air Provisioning 및 MIDlet 네트워킹에 고유한 요구 사항 및 권장 사항을 제공함으로써 OTA 및 MIDP 사양을 보완하기 위해 작성되었습니다. 이후의 WAP 개발에 대해서는 MIDP 이후 버전에서 다루게 될 것입니다. 이러한 권장 사항은 모든 제조업체의 WAP 요소 간에 상호 운용성을 보장하는 데 도움이 될 것입니다. 또한 WAP 프로토콜 스택을 사용하는 브라우저를 통해 프로비저닝을 수행할 때 네트워크 운영자가 MIDP 서비스를 배포하도록 도와줄 뿐만 아니라 MIDlet 개발자가 WSP를 통해 전송할 때 효과적으로 작동하는 MIDlet을 만드는 데에도 도움이 될 것입니다.

### 개요

MIDlet Suite는 HTTP를 사용하여 프로비저닝 서버에서 다운로드됩니다. 중간에 게이트웨이를 사용할 수도 있습니다. 또한 MIDP 라이브러리는 HTTP/1.1 프로토콜의 형식으로 네트워크 액세스를 지원해야 합니다.

최종 사용자 장치와 무선 네트워크에 따라 HTTP 프로토콜 종단 간을 사용하여 최종 사용자 장치와 프로비저닝 서버 간에 통신이 발생할 수 있으며, 또는 최종 사용자 장치가 다른 프로토콜을 사용하고 게이트웨이에서 이 프로토콜을 HTTP로 변환하도록 할 수도 있습니다. 동일한 서비스 공급자가 프로토콜 게이트웨이도 운영해야 할 다른 이유가 없는 한 프로비저닝 서버는 어떤 경우에서도 HTTP만 지원해야 합니다. WAP June2000 환경에서 단말기와 프로비저닝 서버 사이에는 항상 장치와의 통신에 사용되는 WSP 프로토콜과 서버와의 통신에 사용되는 TCP/IP 간에 변환하는 WAP 게이트웨이가 있습니다.

고려해야 할 두 가지 기본 인터페이스가 있습니다.

- 최종 사용자 장치에서 네트워크로의 인터페이스
- 프로비저닝 서버에서 네트워크로의 인터페이스

두 번째 인터페이스는 항상 TCP/IP를 통해 전송되는 HTTP가 사용됩니다.

첫 번째 인터페이스의 경우, 본 문서에서는 다음 두 가지 기본적인 경우 중 하나에 대해 설명합니다.

- 최종 사용자 장치가 WAP 프로토콜 스택을 사용하는 브라우저를 이용하는 경우
- WSP 프로토콜이 단말기와 WAP 게이트웨이 간의 통신에 사용되는 경우

최종 사용자 장치가 WAP 프로토콜 스택을 사용하는 브라우저를 이용하고 WAP 전송 프로토콜이 있는 경우에는 최종 사용자 장치에서 HTTP 대신 WSP를 사용할 수도 있습니다. 연결 지향적인 WSP와 다음과 같은 WAP 프로토콜 스택 구성 및 베어러만 지원됩니다.

- WAP/UDP/IPv4/PPP/CSD
- WAP/UDP/IPv4/GPRS

여기서 WAP는 다음 중 하나일 수 있습니다.

- WSP/WTP/WTLS 또는
- WSP/WTP

([WAP\_WDPS.]에서 SMS 또는 USSD 기반의 베어러와 같은 다른 베어러는 지원되지 않습니다.) 이러한 제한 사항은 WAP 환경의 MIDP 프로비저닝에서 상호 운용성을 최대화하기 위한 것입니다.

무선 네트워크와 최종 사용자 장치의 기능에 따라 IP 연결을 얻기 위해 다른 기법을 사용할 수도 있습니다. 이러한 기법과 각 기법에 요구되는 구성은 본 문서의 범위에서 벗어납니다.

### 단말기 요구 사항 및 권장 사항

이 절에는 WAP 단말기와 관련된 요구 사항 및 권장 사항이 나열되어 있습니다. 단말기와 게이트웨이에 공통된 요구 사항과 권장 사항은 단말기 절과 게이트웨이 절에 모두 나와 있습니다.

WAP 단말기는 WAP June2000 규격이어야 합니다.

*특히 다음과 같은 사항이 중요합니다.*

- 앞의 절에서 설명한 것처럼 JAD 및 JAR MIME 유형을 지원해야 합니다.
- HTTP 인증(서버 응답 401 및 407)을 지원해야 합니다.
- 단말기에서 프로비저닝 서버로의 POST 메시지를 지원해야 합니다.

### WAP 사양에 추가된 요구 사항 및 권장 사항

WSP를 통해 HTTP 연결이 구현되는 경우, HTTP의 시스템 구현은 MIDlet이 HTTP 요청을 할 때 요청 헤더 "*Accept: \*/\**"를 GET 및 POST 요청에 추가해야 합니다. 하지만 MIDlet은 비어 있지 않은 *Accept* 헤더를 요청에 포함시키지 않습니다. 이렇게 하면 WAP 게이트웨이에 항상 명시적 유형 집합이 있게 되며 요청된 데이터를 전달합니다. 이것은 개념적으로 HTTP 요청에 대한 *Accept* 헤더를 제외시키는 것과 같습니다. 어떤 변화도 없습니다(MIDlet의 *게이트웨이의 요구 사항 및 권장 사항)

이 절에서는 WAP 게이트웨이와 관련된 요구 사항 및 권장 사항이 열거되어 있습니다. 이는 WAP 기반의 MIDlet 프로비저닝을 계획할 때 이러한 사항을 고려하도록 하기 위한 것입니다.

WAP 게이트웨이는 WAP
June2000 규격이어야 합니다.

*특히 다음과 같은 사항이 중요합니다.*

- JAD 및 JAR MIME 유형을 지원해야 합니다. WAP 게이트웨이는 이러한 MIME 유형의 HTTP 프록시 규칙(RFC2616)을 준수해야 합니다.
- HTTP 인증(서버 응답 401 및 407)을 지원해야 합니다.
- 단말기 요청에 ">*Accept: \*/\**" 헤더가 포함되어 있으면 모든 종류의 데이터를 단말기로 전달해야 합니다.
- 단말기에서 프로비저닝 서버로의 POST 메시지를 지원해야 합니다.

### MIDlet/MIDlet Suite 권장 사항

MIDlet은 연결 설정이 오래 지연되고 연결을 오래 사용하지 않는 경우에도 제대로 작동하는 것이 좋습니다. 연결 설정이 오래 지연되면 회로 전환 데이터 연결에 영향을 주고, 연결을 오래 사용하지 않으면 GPRS 연결에 영향을 줍니다.

### 참조 자료

1. OTA  
    Over The Air User Initiated Provisioning for Mobile Information Device Profile
2. MIDP  
    Mobile Information Device Profile Specification 1.0, http://jcp.org/jsr/detail/37.jsp
3. MIDP 2.0  
    Mobile Information Device Profile Specification 2.0, http://jcp.org/jsr/detail/118.jsp
4. WAP\_JUNE2000  
    WAP June2000 Conformance Release, http://www.wapforum.org/what/technical.htm
5. WAP\_WDPS  
    WAP Wireless Datagram Protocol Specification, http://www.wapforum.org/what/technical.htm

### 용어

- CSD = Circuit Switched Data
- GPRS = General Packet Radio Service
- PPP = Point-to-Point Protocol
- SMS = Short Message Service
- USSD = Unstructured Supplementary Services Data
- WAP = Wireless Application Protocol
- WSP = Wireless Session Protocol*
