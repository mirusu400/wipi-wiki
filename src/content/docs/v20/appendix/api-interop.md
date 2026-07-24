---
title: "1. MSF/MSP와 CLDC/MIDP의 API 혼용"
---

기준 WIPI2.0에서는 MSF/MSP와 CLDC/MIDP API 중에는 같은 기능을 하는 것들이 중복되어 있다. 따라서, 구현된 플랫폼에 따라 혼용 시 문제가 될 수 있으므로 플랫폼은 다음에 기술된 사항을 준수하는 수준에서 호환성이 보장 되어야 한다. WIPI2.0에서 CLDC/MIDP API 사용 기준을 규정하기 위해 관련 패키지들을 다음 3가지 유형으로 분류하여 기준을 정하였다. 첫째, 동일한 패키지 이름을 가지는 부분으로 플랫폼은 동일한 기능을 제공해야 한다.

> **<표-1> 동일한 패키지**

패키지 그룹 MSF/MSP 패키지 CLDC/MIDP 패키지
IO java.io
Language java.lang
Utility java.util
둘째, 같은 기능을 가지지만, 구현된 내용이 달라 독립적으로 사용되어야 하는 부분이다.
이 경우 플랫폼은 동일 패키지 그룹에 속하는 MSF/MSP와 CLDC/MIDP 패키지(하위 패
키지 포함)들을 혼용하지 않고 각기 독립적으로 사용한 경우에 호환성을 보장해야 한다.
예를 들어, org.kwis.msp.lcdui를 사용한 경우, MSF/MSP의 Graphics 패키지를 선택한
것이므로 javax.microedition.midlet과 javax.microedition.lcdui을 사용할 수 없지만, 다른
패키지 그룹은 지정하여 사용할 수 있고 이 경우 플랫폼은 호환성을 보장해야 한다.
즉, org.kwis.msp.lcdui, javax.microedition.rms, org.kwis.msp.media,
javax.microedition.io를 동시에 사용하는 것은 동일 패키지 그룹에 속하는 것을 혼용하
지 않았으므로 사용이 가능하지만, org.kwis.msp.lcuio, javax.microedition.lcdui,
org.kwis.msp.io, javax.microedition.io를 동시에 사용하는 것은 동일 패키지 그룹에 속
하는 것을 혼용하였으므로 호환성을 유지되지 않으므로 사용할 수 없다.
<표-2 > MSF/MSP와 CLDC/MIDP간의 동일 그룹별 대응 패키지
패키지 그룹 MSF/MSP 패키지 CLDC/MIDP 패키지
Graphics org.kwis.msp.lcdui (jlet) javax.microedition.midlet
org.kwis.msp.lwc javax.microedition.lcdui
DB org.kwis.msp.db javax.microedition.rms
Media org.kwis.msp.media javax.microedition.media
javax.microedition.mediacontrol
High level IO org.kwis.msp.io javax.microedition.io
셋째, 기능이 어느 한 프로파일에만 존재하여 타 프로파일의 기능을 불러 사용할 수 있
는 경우이다.
이 경우 서로 대응하는 패키지가 없으므로 플랫폼은 상호 참조하여 사용할 수 있도록 호
환성을 보장해야 한다.

> **<표-3> MSP/MSF와 CLDC/MIDP간의 각각의 고유 패키지**

패키지그룹 MSF/MSP 패키지 CLDC/MIDP 패키지
Low level IO org.kwis.msf.io 없음
Kernel org.kwisf.core 없음
Devices org.kwis.msp.handset 없음
org.kwis.msp.address
Address book 없음
org.kwis.msp.addressbook
본 규격에서는 플랫폼의 구현 방법을 제시하고 있지 않기 때문에 위에서 언급한 패키지
를 혼용하여 사용시 실제 플랫폼 구현 방법에 따라 추가로 제약사항이 식별될 수 있다.
이 경우 이 장절의 내용은 소정의 규격 개정 절차를 거쳐 개정될 수 있다.
