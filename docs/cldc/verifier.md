# CLDC 바이트 코드 유형 검사기 규격

> CLDC Appendix 1 — Bytecode Type Verifier Specification (Sun Microsystems, 2003년 1월). `vendor/cldc-1_1-fr-spec-ko/Appendix1-verifier.pdf` 한국어 원본을 텍스트 추출한 결과.

<!-- page 1/68 -->

Gilad Bracha, Tim Lindholm, Wei Tao, Frank Yellin Sun Microsystems 2003년 1월 14일

## 1. 개요

이 설명서에서는 CLDC 런타임 검증자 또는 KVM 런타임 검증자라고도 하는 CLDC 유형 검사기의 규격에 대해 설명합니다. 이 설명서의 목적은 CLDC 규격에 대한 추가 설명과 함께 CLDC 규격을 준수하는 가상 머신 고유의 런타임 확인프로세스에 대한 자세한 설명을 제공하는 것입니다.

유형 검사기가 적용하는 유형(type) 규칙은 Prolog 절로 지정됩니다. 영어 텍스트는 유형 규칙을 약식으로 설명할 때 사용되며 Prolog 코드는 형식적 규격을 제공합니다.

다음 절은 유형 검사기를 사용할 수 있는 유형(type) 주석의 형식을 설명합니다. 적절한 유형 검사기의 규격은 §3.에 나와있습니다.

### 1.1 표기법 및 용어

이 규격에서 java 패키지나 해당 부속 패키지에 선언되어 있는 클래스나 인터페이스를 언급하는 경우 이는 Java 가상머신의 부트스트랩 클래스 로더에 의해 로드되는 클래스나 인터페이스를 언급하는 것입니다. 단일 식별자 N을 사용하여클래스나 인터페이스를 언급하는 경우 이는 클래스 java.lang.N을 언급하는 것입니다.

이 규격을 통해 발생하는 예외나 오류 클래스를 지원하지 않는 컨피규레이션에서 유형 검사기는 해당 예외나 오류에 대한신호를 보내기 위해 이러한 컨피규레이션의 규격이 규정하는 내용을 수행해야 합니다.

Prolog 코드 및 코드 조각에 대해서는 이 글꼴을 사용합니다.

Java 가상 머신 명령 및 클래스 파일 구조에 대해서는 다른 글꼴을 사용합니다.

규격을 명확히 설명하기 위해 제공되는 주석은 다음과 같이 가로줄 사이에서 들여쓴 텍스트로 제공됩니다.

주석은 직관적 지식, 동기화, 이론적 설명, 예 등을 제공합니다.

유형 검사기는 메소드 로컬 변수와 피연산자 스택의 예상 유형을 다루고 조작합니다. 이 설명서에서 위치는 단일 로컬변수나 단일 피연산자 스택 항목을 언급합니다.

여기에서는 피연산자 스택의 위치와 메소드 및 확인 유형(type)의 로컬 변수 사이의 매핑을 설명하기 위해 스택 프레임맵과 유형 상태라는 용어를 상호 교체 가능한 의미로 사용합니다. 일반적으로 매핑이 클래스 파일에 제공되어 있으면스택 프레임 맵이란 용어를 사용하고 유형 검사기에 의해 매핑이 추론되면 유형 상태란 용어를 사용합니다.

<!-- page 2/68 -->

## 2. 구문 분석

유형 검사기에는 Code 속성을 갖는 각 메소드에 대해 스택 프레임 맵 목록이 필요합니다. 유형 검사기는 이러한 각 메소드에 대해 스택 프레임 맵을 읽은 다음 이러한 맵을 사용하여 Code 속성에 있는 명령의 유형 안정성에 대한 증거를 생성합니다. 스택 프레임 맵의 목록은 스택 맵 속성에 의해 주어집니다. 이 절은 스택 맵 속성의 형식을 지정합니다. 스택 맵속성이 이 절에서 지정한 형식과 일치하지 않는 경우 Java 가상 머신은 java.lang.ClassFormatError를 발생시킵니다.

스택 프레임 맵이 메소드의 각 기본 블록의 시작 부분에 표시하도록 하는 것이 목적입니다. 스택 프레임맵은 각 기본 블록의 시작 부분에서 각 피연산자 스택 항목과 각 로컬 변수의 확인 유형(type)을 지정합니다.

### 2.1 스택 맵 형식

스택 맵 속성은 Code 속성의 속성 테이블에 있는 선택적 가변 길이 속성입니다. 이 속성의 이름은 StackMap입니다. 스택 맵 속성은 0개 이상의 스택 맵 프레임으로 구성됩니다. 각 스택 맵 프레임은 오프셋, 로컬 변수에 대한 확인 유형 배열및 피연산자 스택에 대한 확인 유형 배열을 지정합니다.

메소드의 Code 속성에 StackMap 속성이 없는 경우 암시적 스택 맵 속성을 갖습니다. 이 암시적 스택 맵 속성은 number_of_entries가 0인 StackMap 속성에 해당합니다. 메소드의 Code 속성에는 0 또는 1개의 StackMap 속성이있어야 하며 그렇지 않은 경우 java.lang.ClassFormatError가 발생됩니다.

클래스 파일의 스택 맵 형식은 아래에 있습니다. 다음에서 메소드 바이트 코드1의 길이가 65535 이하이면 uoffset은 유형 u2를 나타내며 그렇지 않은 경우 uoffset은 유형 u4를 나타냅니다. 메소드 로컬 변수의 최대 개수가 65535 이하인경우 ulocalvar는 유형 u2를 나타내며 그렇지 않은 경우 ulocalvar는 유형 u4를 나타냅니다. 피연산자 스택의 최대크기가 65535 이하인 경우 ustack은 유형 u2를 나타내며 ustack은 유형 u42를 나타냅니다.

stack_map { // attribute StackMap u2 attribute_name_index; u4 attribute_length uoffset number_of_entries; stack_map_frame entries[number_of_entries]; } 각 스택 맵 프레임은 다음 형식을 갖습니다.

stack_map_frame { uoffset offset; ulocalvar number_of_locals; verification_type_info locals[number_of_locals]; ustack number_of_stack_items; verification_type_info stack[number_of_stack_items]; } locals의 0번째 항목은 로컬 변수 0의 유형을 나타냅니다. locals[M]이 로컬 변수 N을 나타내고, locals[M]이 Top_variable_info, Integer_variable_info, Float_variable_info, Null_variable_info, UninitializedThis_variable_info, Object_variable_info, Uninitialized_variable_info 중 하나인 경우 locals[M+1]은 로컬 변수 N+1을 나타냅니다. 그렇지 않은 경우 locals[M+1]은 로컬 변수 N+2를 나타냅니다. 색인 i에 대해 locals[i]의 색인이 메소드의 최대 로컬 변수개수보다 많은 로컬 변수를 나타내면 오류입니다.

1. 바이트 코드의 길이는 Code 속성의 길이와 같지 않음을 기억해 두십시오. 바이트 코드는 다른 정보와 함께 Code 속성에 임베디드됩니다.

2. J2ME CLDC 기술의 경우 이 단락에 언급된 필드의 크기는 항상 16비트(u2)입니다.

2페이지

<!-- page 3/68 -->

stack의 0번째 항목은 스택 아래쪽의 유형을 나타내며 후속 항목은 피연산자 스택의 위쪽에 더 가까운 스택 요소의유형을 나타냅니다. 여기에서는 스택의 아래 요소를 스택 요소 0으로, 후속 요소를 스택 요소 1, 2 등으로 언급합니다.

stack[M]이 스택 요소 N을 나타내면서 stack[M]이 Top_variable_info, Integer_variable_info, Float_variable_info, Null_variable_info, UninitializedThis_variable_info, Object_variable_info, Uninitialized_variable_info 중 하나인 경우 stack[M+1]은 스택 요소 N+1을 나타내고 그렇지 않은 경우 stack[M+1]은 스택 요소 N+2를 나타냅니다. 색인 i에대해 stack[i]의 색인이 메소드의 최대 로컬 변수 개수보다 많은 로컬 변수를 나타내면 오류입니다.

스택 맵 프레임의 오프셋 필드에 있는 오프셋이 바이트 코드로 된 명령의 오프셋과 같은 경우 바이트 코드로 된 명령은해당 스택 맵 프레임을 갖습니다.

verification_type_info 구조는 태그에 대한 자세한 정보를 제공하며, 0개 이상의 바이트가 뒤에 오는 1바이트 태그로 구성됩니다. 각 verification_type_info 구조는 1-2 개 위치의 확인 유형을 지정합니다.

union verification_type_info { Top_variable_info; Integer_variable_info; Float_variable_info; Long_variable_info; Double_variable_info; Null_variable_info; UninitializedThis_variable_info; Object_variable_info; Uninitialized_variable_info; } Top_variable_info는 로컬 변수가 확인 유형 top(⊥)을 갖는다는 것을 나타냅니다.

Top_variable_info { u1 tag = ITEM_Top; /* 0 */ } Integer_variable_info 유형은 해당 위치에 확인 유형 int가 포함된다는 것을 나타냅니다.

Integer_variable_info { u1 tag = ITEM_Integer; /* 1 */ } Float_variable_info 유형은 위치에 확인 유형 float이 포함된다는 것을 나타냅니다.

Float_variable_info { u1 tag = ITEM_Float; /* 2 */ } Long_variable_info 유형은 위치에 확인 유형 long이 포함된다는 것을 나타냅니다. 위치가 로컬 변수인 경우는 다음에 해당합니다.

• 가장 큰 색인을 갖는 로컬 변수가 아니어야 합니다.

• 그 다음으로 큰 번호의 로컬 변수에는 확인 유형 ⊥이 포함됩니다.

위치가 피연산자 스택 항목인 경우는 다음에 해당합니다.

• 현재 위치는 피연산자 스택의 최상위 위치가 아니여야 합니다.

• 피연산자 스택의 맨 위와 그 다음으로 가까운 위치에는 확인 유형 ⊥이 포함됩니다.

이 구조는 stack[]이나 local[] 배열에서 두 위치의 내용을 제공합니다.

3페이지

<!-- page 4/68 -->

Long_variable_info { u1 tag = ITEM_Long; /* 4 */ } Double_variable_info 유형은 위치에 확인 유형 double이 포함된다는 것을 나타냅니다. 위치가 로컬 변수인 경우 • 가장 큰 색인을 갖는 로컬 변수가 아니어야 합니다.

• 그 다음으로 큰 번호의 로컬 변수에는 확인 유형 ⊥이 포함됩니다.

위치가 피연산자 스택 항목인 경우 • 현재 위치는 피연산자 스택의 최상위 위치가 아니여야 합니다.

• 피연산자 스택의 맨 위와 그 다음으로 가까운 위치에는 확인 유형 ⊥이 포함됩니다.

이 구조는 stack[]이나 local[] 배열에서 두 위치의 내용을 제공합니다.

Double_variable_info { u1 tag = ITEM_Double; /* 3 */ } Null_variable_info 유형은 위치에 유형 검사기 유형 null이 포함된다는 것을 나타냅니다.

Null_variable_info { u1 tag = ITEM_Null; /* 5 */ } UninitializedThis_variable_info 유형은 위치에 확인 유형 uninitializedThis가 포함된다는 것을 나타냅니다.

UninitializedThis_variable_info { u1 tag = ITEM_UninitializedThis; /* 6 */ } Object_variable_info 유형은 위치가 상수 풀 항목에 의해 참조되는 클래스를 포함한다는 것을 나타냅니다.

Object_variable_info { u1 tag = ITEM_Object; /* 7 */ u2 cpool_index; } Uninitialized_variable_info는 위치에 확인 유형 uninitialized(offset)가 포함된다는 것을 나타냅니다.

offset 항목은 위치에 저장된 객체를 만든 new 명령의 오프셋을 나타냅니다.

Uninitialized_variable_info { u1 tag = ITEM_Uninitialized /* 8 */ uoffset offset; } 4페이지

<!-- page 5/68 -->

## 3. 유형 검사

클래스 파일의 유형(type) 검사는 클래스가 성공적으로 로드된 다음 수행됩니다.

술어 classIsTypeSafe가 true가 아닌 경우 유형 검사는 예외 java.lang.VerifyError를 발생시켜 클래스 파일이 잘못되었음을 나타내야 합니다. 반대의 경우 클래스 파일이 유형 검사를 성공적으로 수행하고 바이트 코드 확인이 성공적으로 완료된 것입니다.

classIsTypeSafe(Class) :- classClassName(Class,Name), Name \= ‘java/lang/Object’, classSuperClassName(Class, SuperclassName), loadedClass(SuperclassName, Superclass), classIsNotFinal(Superclass), classMethods(Class, Methods), checklist(methodIsTypeSafe(Class), Methods). classIsTypeSafe(Class) :- classClassName(Class, ‘java/lang/Object’), classMethods(Class, Methods), checklist(methodIsTypeSafe(Class), Methods). 술어 classIsTypeSafe는 Class가 성공적으로 구문 분석된 이진 클래스를 나타내는 Prolog 용어임을 가정합니다. 이 규격은 이 용어의 정확한 구조를 요구하지 않지만 §3.2.1에 지정된 대로 특정 술어(예: classMethods)를 정의할 것을 요구합니다.

예를 들어, 위에 설명한 클래스를 첫 번째 인자로 나타내는 용어가 주어지면 술어 classMethods(Class, Methods)가 아래에 설명된 편리한 형식으로 제시된 클래스의 모든 메소드를구성하는 목록에 두 번째 인자를 바인드한다고 가정합니다.

따라서 클래스의 모든 메소드가 유형 안정적이면 해당 클래스는 유형 안정적이며, 최종 클래스에 부속되지 않습니다.

또한 Name이라는 클래스가 있음을 단언하고 그 표현(이 규격에 맞춰)이 ClassDefinition인 술어 loadedClass(Name, ClassDefinition)의 존재를 요구합니다.

개별 명령은 기능자가 명령의 이름이며 인자가 구문 분석된 피연산자인 용어로서 표현됩니다.

예를 들어 aload 명령은 해당 명령의 피연산자인 색인 N을 포함하는 용어 aload(N)로 표현됩니다.

몇 가지 명령은 메소드나 필드를 나타내는 상수 풀 항목인 피연산자를 갖습니다. JVMS에 지정한 대로 메소드는 상수풀의 CONSTANT_InterfaceMethodref_info(인터페이스 메소드의 경우)나 CONSTANT_Methodref_info(다른메소드의 경우)에 의해 표현됩니다. 이러한 구조는 인터페이스 메소드의 경우 imethod(MethodClassName, MethodName, MethodSignature) 형식이나, 다른 메소드의 경우 method(MethodClassName, MethodName, MethodDescriptor) 형식의 기능자 응용 프로그램으로 표현됩니다. 여기서 MethodClassName은 구조의 class_index 항목이 참조하는 클래스의 이름이며 MethodName과 MethodDescriptor는 구조의 name_and_type_index가 참조하는이름과 유형(type) 설명자에 해당합니다.

5페이지

<!-- page 6/68 -->

마찬가지로 필드는 클래스 파일의 CONSTANT_Fieldref_info 구조에 의해 표현됩니다. 여기서 이러한 구조는 field(FieldClassName, FieldName, FieldDescriptor) 형식의 기능자 응용 프로그램으로 표현됩니다. 여기서 FieldClassName은 구조에서 class_index 항목이 참조하는 클래스 이름이며, FieldName과 FieldDescriptor는 구조의 name_and_type_index 항목이 참조하는 이름과 유형 설명자에 해당합니다.

따라서 피연산자가 클래스 Bar에 있는 형식 F의 필드 foo를 참조하는 상수 풀의 색인인 getfield 명령은 getfield(field(‘Bar’, ‘foo’, ‘F’))로 표현됩니다.

명령은 전체적으로 instruction(Offset, AnInstruction) 형식의 용어 목록으로 표현됩니다.

예를 들어 instruction(21, aload(1))입니다.

이 목록에서 명령의 순서는 클래스 파일에서의 순서와 같아야 합니다.

StackMap 속성은 stackMap(Offset, TypeState) 형식의 용어 목록으로 표현되며, 여기서 Offset은 프레임 맵이 적용된 명령의 오프셋을 나타내는 정수이고 TypeState는 해당 명령에 대해 수신 예상 유형 상태입니다. 이 목록에서 명령의 순서는 클래스 파일에서의 순서와 같아야 합니다.

TypeState는 frame(Locals, OperandStack, Flags) 형식을 가져야 합니다.

Locals는 확인 유형 목록이며 목록의 N 번째 요소(0에서부터 시작하는 색인)는 로컬 변수 N의 유형을 나타냅니다.

Locals의 로컬 변수에 유형 uninitializedThis가 있는 경우 Flags는 [flagThisUninit]이며 그렇지 않은 경우 빈목록입니다.

OperandStack은 유형 목록이며, 여기서 첫 번째 요소는 피연산자 스택의 맨 위에 있는 유형을 나타내고 그 다음 아래에있는 요소는 적절한 순서를 따릅니다.

하지만 크기 2의 유형은 두 항목에 의해 표현되며 첫 번째 항목은 맨 위가 되고 두 번째 항목은 유형 자체가 됩니다.

따라서 double을 갖는 스택, int 및 long은 [top, double, int, top, long]으로 표현됩니다.

배열 유형은 배열의 요소 유형을 나타내는 인자에 기능자 arrayOf를 적용하여 표현됩니다. 다른 참조 유형은 클래스나인터페이스의 정규화된 이름에 기능자 class를 적용하여 표현됩니다. 유형 uninitialized(offset)는 기능자 uninitialized를 offset의 숫자 값을 나타내는 인자에 적용하여 표현됩니다. 다른 확인 유형은 이름이 해당 확인 유형을 나타내는 Prolog 기본 단위에 의해 표현됩니다.

따라서 클래스 Object는 class(‘java/lang/Object’)로 표현되며 유형 int[]와 Object[]는 arrayOf(int)와 arrayOf(class(‘java/lang/Object’))에 의해 각각 표현됩니다.

Flags는 비어 있거나 단일 요소 flagThisUninit을 갖는 목록입니다.

이 플래그는 this의 초기화가 아직 완료되지 않은 유형 상태를 표시하기 위해 구성자에서 사용됩니다. 이러한 유형 상태에서 메소드로부터 반환되는 것은 유효하지 않습니다.

6페이지

<!-- page 7/68 -->

### 3.1 유형 계층

유형 검사기는 아래의 그림에서 설명한 대로 확인 유형(type)의 계층을 기준으로 유형 시스템을 적용합니다. 대부분의 검증자 유형은 JVMS, 표 4.2에 주어진 대로 Java 가상 머신 필드 유형 설명자에 직접 대응합니다. 유일한 예외는 필드 설명자 B, C, S, Z이며 이들 모두는 검증자 유형 int에 해당합니다.

⊥ oneWord twoWord int float long double reference uninitialized java.lang.Object uninitializedThis uninitialized(offset) J a a 클래스계층 null 확인 유형 계층 7페이지

<!-- page 8/68 -->

#### 3.1.1 서브 타입 규칙

서브 타입은 재귀됩니다.

isAssignable(X, X) . isAssignable(oneWord, top). isAssignable(twoWord, top). isAssignable(int, X) :- isAssignable(oneWord, X). isAssignable(float, X) :- isAssignable(oneWord, X). isAssignable(long, X) :- isAssignable(twoWord, X). isAssignable(double, X) :- isAssignable(twoWord, X). isAssignable(reference, X) :- isAssignable(oneWord, X). isAssignable(uninitialized, X) :- isAssignable(reference, X). 이러한 서브 타입 규칙이 반드시 가장 확실한 서브 타입의 공식은 아닙니다. Java 프로그래밍 언어의참조 유형에 대한 서브 타입 규칙과 나머지 확인 유형의 규칙 사이에는 명확한 차이점이 있습니다.

Java 프로그래밍 언어에서 참조 유형의 서브 타입 규칙은 확실한 방법으로 재귀적으로 지정됩니다.

나머지 확인 유형은 다음 형식의 서브 타입 규칙을 갖습니다.

subtype(v, X) :- subtype(the_direct_supertype_of_v, X). 즉 v의 직접 수퍼 타입이 X의 서브 타입인 경우 v는 X의 서브 타입입니다.

또한 서브 타입이 재귀적이라는 규칙이 있으므로 이러한 규칙을 합하면 Java 프로그래밍 언어의 참조유형이 아닌 대부분의 확인 유형을 다룰 수 있습니다.

앞에서 언급한 분할을 사용하면 Java 프로그래밍 언어 유형과 다른 확인 유형 사이의 일반 서브 타입관계를 분명히 할 수 있습니다.

이러한 관계는 계층에서 Java 유형의 위치를 독립적으로 유지합니다. 이러한 규칙은 참조 구현에 유용하므로 중복 대답 및 과도한 클래스 로딩을 막는 데 도움이 됩니다.

예를 들어 형식 class(foo) <: twoWord의 쿼리에 응답하여 클래스 계층을 올라가지는 않습니다.

전체 계층에 같은 술어를 사용하는 경우 두 클래스를 비교하는 경우로 상향을 제한할 수 없습니다.

규격에 대해 동일한 규칙을 갖는 것이 좋을 수 있지만 참조 구현에는 적합하지 않습니다. 참조 구현은해당 규격과 가능한 한 유사하게 하는 것이 좋습니다.

isAssignable(class(_), X) :- isAssignable(reference, X). isAssignable(arrayOf(_), X) :- isAssignable(reference, X). isAssignable(uninitializedThis, X) :- isAssignable(uninitialized, X). 8페이지

<!-- page 9/68 -->

isAssignable(uninitialized(_), X) :- isAssignable(uninitialized, X). isAssignable(null, class(_)). isAssignable(null, arrayOf(_)). isAssignable(null, X) :- isAssignable(class(’java/lang/Object’), X). isAssignable(class(X), class(Y)) :- isJavaAssignable(class(X), class(Y)). isAssignable(arrayOf(X), class(Y)) :- isJavaAssignable(arrayOf(X), class(Y)). isAssignable(arrayOf(X), arrayOf(Y)) :- isJavaAssignable(arrayOf(X),arrayOf(Y)). 할당을 위해 인터페이스는 Object처럼 처리됩니다.

isJavaAssignable(class(_), class(To)) :- loadedClass(To, ToClass), classIsInterface(ToClass). isJavaAssignable(class(From), class(To)) :- isJavaSubclassOf(From, To). 배열은 Object의 서브 타입입니다.

isJavaAssignable(arrayOf(_), class(’java/lang/Object’)). 여기에서는 마지막 두 유형이 정의되어 있는 경우 배열 유형이 Cloneable과 java.io.Serializable의 서브 타입이어야 한다는 것입니다. CLDC의 경우 이러한 유형이 존재하지 않습니다. 이러한 내용은 술어 isArrayInterface에 절이 없게 만들어 항상 false가 되게 함으로써 CLDC용 Prolog 코드에 반영됩니다.

isJavaAssignable(arrayOf(_), class(X)) :- isArrayInterface(X). 프리미티브 유형 배열 사이의 유형 세분화 관계는 ID 관계입니다.

isJavaAssignable(arrayOf(X), arrayOf(Y)) :- atom(X), atom(Y), X = Y. 참조 유형 배열 사이의 유형 세분화는 공변합니다.

isJavaAssignable(arrayOf(X), arrayOf(Y)) :- compound(X), compound(Y), isJavaAssignable(X, Y). 9페이지

<!-- page 10/68 -->

서브 클래스는 재귀적입니다.

isJavaSubclassOf(SubClassName, SubClassName). isJavaSubclassOf(SubClassName, SuperClassName) :- loadedClass(SubClassName, SubClass), classSuperClassName(SubClass, SubSuperClassName), isJavaSubclassOf(SubSuperClassName, SuperClassName). sizeOf(X, 2) :- isAssignable(X, twoWord). sizeOf(X, 1) :- isAssignable(X, oneWord). sizeOf(top, 1). 서브 타입은 유형 상태 방향으로 확장됩니다.

frameIsAssignable(frame(Locals1, StackMap1, Flags1), frame(Locals2, StackMap2, Flags2)) :- length(StackMap1, StackMapLength), length(StackMap2, StackMapLength), maplist(isAssignable, Locals1, Locals2), maplist(isAssignable, StackMap1, StackMap2), subset(Flags1, Flags2).

### 3.2 유형 검사 규칙

#### 3.2.1 접근자

규정된 접근자: 이 규격에서는 규격에 없는 특정 Prolog 술어의 형식 정의가 있다고 가정합니다. 이 절에서는 이러한술어를 나열하고 술어의 예상 동작을 지정합니다.

parseFieldSignature(Signature, Type) 필드 설명자 Signature를 해당 확인 유형 Type으로 변환합니다(이러한 대응의 규격은 §3.1의 시작 부분 참조). parseMethodSignature(Signature, TypeList, ReturnType) 메소드 설명자 Signature를 메소드 인자 유형에 해당(§3.1)하는 확인 유형 목록 TypeList로 변환하면 확인 유형 ReturnType은 반환 유형에 해당합니다.

parseCodeAttribute(ClassFile, Method, FrameSize, MaxStack, ParsedCode, Handlers, StackMap) 최대 피연산자 스택 크기인 MaxStack, 로컬 변수의 최대 개수인 FrameSize, 예외 처리기인 Handlers 및 스택 맵 StackMap 을 비롯하여 ClassFile에 있는 메소드 Method의 명령 스트림 ParsedCode를 추출합니다. 명령 스트림과 스택 맵 속성표현은 §3.의 처음에 지정되어 있어야 합니다. 각 예외 처리기는 인자가 처리기에서 다루는 명령 범위의 시작과 끝, 처리기 코드의 첫 번째 명령 및 이 처리기가 처리해야 하는 예외 클래스 이름을 나타내는 형식 handler(Start, End, Target, ClassName)의 기능자 응용 프로그램에 의해 표현됩니다.

10페이지

<!-- page 11/68 -->

classClassName(Class, ClassName) 클래스 Class의 이름 ClassName을 추출합니다.

classIsInterface(Class, IsInterface) 클래스 Class가 인터페이스인 경우 True입니다.

classIsNotFinal(Class) 클래스 Class가 최종 클래스가 아닌 경우 True입니다.

classSuperClassName(Class, SuperClassName) 클래스 Class의 슈퍼 클래스 이름 SuperClassName을 추출합니다.

classInterfaces(Class, Interfaces) 클래스 Class의 직접 수퍼인터페이스 목록인 Interfaces를 추출합니다.

classMethods(Class, Methods) 클래스 Class의 메소드 목록인 Methods를 추출합니다.

classAttributes(Class, Attributes) 클래스 Class의 속성 목록인 Attributes를 추출합니다. 각 속성은 형식 속성(AttributeName, AttributeContents)의 기능자 응용 프로그램으로 표현되며, 여기서 AttributeName은 속성의 이름입니다. 속성 내용의 형식은 지정되어 있지 않습니다.

methodName(Method, Name) 메소드 Method의 이름 Name을 추출합니다.

methodAccessFlags(Method, AccessFlags) 메소드 Method의 액세스 플래그 AccessFlags를 추출합니다.

methodSignature(Method, Signature) 메소드 Method의 설명자 Signature를 추출합니다.

methodAttributes(Method, Attributes) 메소드 Method의 속성 목록인 Attributes를 추출합니다.

isNotFinal(Method, Class) 클래스 Class의 Method가 마지막이 아닌 경우 True입니다.

isProtected(MemberClassName, MemberName, MemberSignature) 클래스 MemberClassName에서 서명 MemberSignature가 있는 MemberName이라는 구성원이 보호되어 있는 경우 True입니다.

isNotProtected(MemberClassName, MemberName, MemberSignature) 클래스 MemberClassName에서 서명 MemberSignature가 있는 MemberName이라는 구성원이 보호되어 있지 않은경우 True입니다.

여기에서는 완전하게 지정할 접근자와 규정할 내용에 관한 결정을 돕는 원칙이 있으며 클래스 파일의표현을 과도하게 지정하지 않습니다. 특정 접근자를 클래스나 메소드 용어에 제공하면 클래스 파일을나타내는 Prolog 용어에 대한 형식을 완전하게 지정해야 합니다.

11페이지

<!-- page 12/68 -->

지정된 접근자 및 유틸리티: 또한 클래스 및 관련 메소드의 표현에서 필요한 정보를 추출하는 접근자 및 유틸리티규칙을 제공합니다.

환경은 클래스, 메소드, 메소드의 선언된 반환 유형, 메소드의 명령, 피연산자 스택의 최대 크기 및 예외처리기 목록 등의 6개로 구성되어 있습니다.

maxOperandStackLength(Environment, MaxStack) :- Environment = environment(_Class, _Method, _ReturnType, _All, MaxStack, _Handlers). exceptionHandlers(Environment, Handlers) :- Environment = environment(_Class, _Method, _ReturnType, _All, _, Handlers). thisMethodReturnType(Environment, ReturnType) :- Environment = environment(_Class, _Method, ReturnType, _All, _, _). thisClass(Environment, class(ClassName)) :- Environment = environment(Class, _Method, _ReturnType, _All, _, _), classClassName(Class, ClassName). allInstructions(Environment, All) :- Environment = environment(_Class, _Method, _ReturnType, All, _, _). offsetStackFrame(Environment, Offset, StackFrame) :- allInstructions(Environment, Instructions), member(stackMap(Offset, StackFrame), Instructions). notMember(_, []). notMember(X, [A | More]) :- X \= A, notMember(X, More).

#### 3.2.2 추상 메소드 및 고유 메소드

추상 메소드가 최종 메소드를 무시하지 않는 경우 유형 안정적인 것으로 간주합니다.

methodIsTypeSafe(Class, Method) :- doesNotOverrideFinalMethod(Class, Method), methodAccessFlags(Method, AccessFlags), member(abstract, AccessFlags). 12페이지

<!-- page 13/68 -->

고유 메소드가 최종 메소드를 무시하지 않는 경우 유형 안정적인 것으로 간주합니다.

methodIsTypeSafe(Class, Method) :- doesNotOverrideFinalMethod(Class, Method), methodAccessFlags(Method, AccessFlags), member(native, AccessFlags). doesNotOverrideFinalMethod(class(‘java/lang/Object’), Method). doesNotOverrideFinalMethod(Class, Method) :- classSuperClassName(Class, SuperclassName), loadedClass(SuperclassName, Superclass), classMethods(Superclass, MethodList), finalMethodNotOverridden(Method, Superclass, MethodList). finalMethodNotOverridden(Method, Superclass, MethodList) :- methodName(Method, Name), methodSignature(Method, Sig), member(method(_, Name, Sig), MethodList), isNotFinal(Method, Superclass). finalMethodNotOverridden(Method, Superclass, MethodList) :- methodName(Method, Name), methodSignature(Method, Sig), notMember(method(_, Name, Sig), MethodList), doesNotOverrideFinalMethod(Superclass, Method).

#### 3.2.3 코드 검사

비추상, 비고유 메소드에 코드가 있고 코드 유형이 올바른 경우 이들 유형은 올바른 것입니다.

methodIsTypeSafe(Class, Method) :- doesNotOverrideFinalMethod(Class, Method), methodAccessFlags(Method, AccessFlags), methodAttributes(Method, Attributes), notMember(native, AccessFlags), notMember(abstract, AccessFlags), member(attribute(’Code’, _), Attributes), methodWithCodeIsTypeSafe(Class, Method). 13페이지

<!-- page 14/68 -->

각 스택 맵이 해당하는 명령을 선행하고 병합된 결과 스트림의 유형이 올바를 수 있도록 코드와 스택프레임을 단일 스트림에 병합하는 경우 코드가 있는 메소드는 유형 안정적입니다.

methodWithCodeIsTypeSafe(Class, Method) :- parseCodeAttribute(Class, Method, FrameSize, MaxStack, ParsedCode, Handlers, StackMap), mergeStackMapAndCode(StackMap, ParsedCode, MergedCode), methodInitialStackFrame(Class, Method, FrameSize, StackFrame, ReturnType), Environment = environment(Class, Method, ReturnType, MergedCode, MaxStack, Handlers), handlersAreLegal(Environment), mergedCodeIsTypeSafe(Environment, MergedCode, StackFrame). 메소드의 초기 유형 상태는 유형 this와 인자에서 파생된 빈 피연산자 스택과 로컬 변수 유형 그리고 this가 <init> 메소드인지 여부에 따라 적절한 플래그로 구성됩니다.

methodInitialStackFrame(Class, Method, FrameSize, frame(Locals, [], Flags), ReturnType):- methodSignature(Method, Signature), parseMethodSignature(Signature, RawArgs, ReturnType), expandTypeList(RawArgs, Args), methodInitialThisType(Class, Method, ThisList), flags(ThisList, Flags), append(ThisList, Args, ThisArgs), expandToLength(ThisArgs, FrameSize, top, Locals). flags([uninitializedThis], [flagThisUninit]). flags(X, []) :- X \= [uninitializedThis]. expandToLength(List, Size, _Filler, List) :- length(List, Size). expandToLength(List, Size, Filler, Result) :- length(List, ListLength), ListLength < Size, Delta is Size - ListLength, length(Extra, Delta), checklist(=(Filler), Extra), append(List, Extra, Result). 14페이지

<!-- page 15/68 -->

정적 메소드의 경우 this는 무관하며 목록은 비어 있습니다. 인스턴스 메소드의 경우 this의 유형을얻어 목록에 둡니다.

methodInitialThisType(_Class, Method, []) :- methodAccessFlags(Method, AccessFlags), member(static, AccessFlags), methodName(Method, MethodName), MethodName \= ’<init>’. methodInitialThisType(Class, Method, [This]) :- methodAccessFlags(Method, AccessFlags), notMember(static, AccessFlags), instanceMethodInitialThisType(Class, Method, This). Object의 <init> 메소드에서 this의 유형은 Object입니다. 다른 <init> 메소드에서 this의 유형은 uninitializedThis입니다. 그 밖의 경우 인스턴스 메소드에서 this의 유형은 class(N)이며, 여기서 N은 메소드를 포함하는 클래스의 이름입니다.

instanceMethodInitialThisType(Class, Method, class(ClassName)) :- methodName(Method, MethodName), MethodName \= ’<init>’, classClassName(Class, ClassName). instanceMethodInitialThisType(Class, Method, class(’java/lang/Object’)) :- methodName(Method, ’<init>’), classClassName(Class, ’java/lang/Object’). instanceMethodInitialThisType(Class, Method, uninitializedThis) :- methodName(Method, ’<init>’), classClassName(Class, ClassName), ClassName \= ’java/lang/Object’. 아래에는 코드 스트림을 통해 반복되는 규칙이 나와 있습니다. 바이트 코드 색인 N의 스택 맵이 명령 N 바로 앞에 표시되도록 스트림이 명령과 스택 맵으로 잘 혼합되어 있다고 가정합니다.

이렇게 혼합된 스트림을 빌드하는 규칙은 술어 mergeStackMapAndCode를 사용하여 나중에 제공합니다.

특수 표시자 aftergoto는 무조건 분기를 표시하기 위해 사용됩니다.

코드의 끝에 무조건 분기가 있는 경우 중단됩니다.

mergedCodeIsTypeSafe(_Environment, [endOfCode(Offset)], afterGoto). 15페이지

<!-- page 16/68 -->

무조건 분기 뒤에 다음 명령에 대한 유형 상태를 제공하는 스택 맵이 있는 경우 스택 맵이 제공한 유형상태를 사용하여 유형 검사를 진행할 수 있습니다.

mergedCodeIsTypeSafe(Environment, [stackMap(Offset, MapFrame) | MoreCode], afterGoto):- mergedCodeIsTypeSafe(Environment, MoreCode, MapFrame). 스택 맵과 수신 유형 상태가 있는 경우 유형 상태를 스탭 맵의 한 곳에 지정할 수 있어야 합니다. 그런다음 스택 맵에 주어진 유형 상태를 사용하여 나머지 스트림의 유형 검사를 진행할 수 있습니다.

mergedCodeIsTypeSafe(Environment, [stackMap(Offset, MapFrame) | MoreCode], frame(Locals, OperandStack, Flags)) :- frameIsAssignable(frame(Locals, OperandStack, Flags), MapFrame), mergedCodeIsTypeSafe(Environment, MoreCode, MapFrame). 제공된 스택 프레임 맵이 없는 무조건 분기 다음에 코드가 있는 것은 유효하지 않습니다.

mergedCodeIsTypeSafe(_Environment, [instruction(_,_) | _MoreCode], afterGoto) :- write_ln(’No stack frame after unconditional branch’), fail. T에 관해 유형 안정적인 명령 I로 시작하고 I는 해당 예외 처리기를 만족시키며 I의 실행 뒤에 유형 상태가 온다고 가정할 때 스트림의 끝 부분이 유형 안정적인 경우 병합된 코드 스트림은 수신 유형 상태 T에 관해 유형 안정적입니다.

mergedCodeIsTypeSafe(Environment, [instruction(Offset,Parse) | MoreCode], frame(Locals, OperandStack, Flags)) :- 명령을 확인합니다. NextStackFrame은 다음 명령으로 전달될 내용을 표시합니다.

ExceptionStackFrame은 예외 처리기로 전달될 내용을 표시합니다.

instructionIsTypeSafe(Parse, Environment, Offset, frame(Locals, OperandStack, Flags), NextStackFrame, ExceptionStackFrame), instructionSatisfiesHandlers(Environment, Offset, ExceptionStackFrame), mergedCodeIsTypeSafe(Environment, MoreCode, NextStackFrame). 대상에 관련 스택 프레임 Frame이 있고 현재 스택 프레임 StackFrame을 Frame에 할당할 수 있는 경우대상으로 분기하는 것은 유형 안정적입니다.

targetIsTypeSafe(Environment, StackFrame, Target) :- offsetStackFrame(Environment, Target, Frame), frameIsAssignable(StackFrame, Frame). 16페이지

<!-- page 17/68 -->

#### 3.2.4 스택 맵과 명령 스트림 결합

스택 프레임 스트림과 명령 스트림의 병합은 이 절에 정의되어 있습니다.

빈 StackMap과 명령 목록을 병합하면 명령의 원래 목록이 만들어집니다.

mergeStackMapAndCode([], CodeList, CodeList). Offset에 있는 명령에 대해 유형 상태로 시작되는 스택 프레임 맵의 목록과 Offset에서 시작하는 명령의목록을 가정하면 병합된 목록은 스택 프레임 목록의 시작 부분 및 그 뒤에 오는 명령 목록 시작 부분과두 개 목록 끝 부분의 병합으로 구성됩니다.

mergeStackMapAndCode([stackMap(Offset, Map) | RestMap], [instruction(Offset, Parse) | RestCode], [stackMap(Offset, Map), instruction(Offset, Parse) | RestMerge]) :- mergeStackMapAndCode(RestMap, RestCode, RestMerge). 반대로 OffsetM의 명령에 대한 유형 상태로 시작하는 스택 프레임 목록과 OffsetP에서 시작하는 명령목록을 가정하면 OffsetP < OffsetM인 경우 병합된 목록은 명령 목록 시작 부분 및 그 뒤에 오는 스택프레임 목록 병합 및 명령 목록의 끝 부분으로 구성됩니다.

mergeStackMapAndCode([stackMap(OffsetM, Map) | RestMap], [instruction(OffsetP, Parse) | RestCode], [instruction(OffsetP, Parse) | RestMerge]) :- OffsetP < OffsetM, mergeStackMapAndCode([stackMap(OffsetM, Map) | RestMap], RestCode, RestMerge). 그렇지 않은 경우 두 가지 목록의 병합은 정의되어 있지 않습니다.

명령 목록에는 단순하게 증가하는 오프셋이 있으므로 두 가지 목록의 병합은 다음 경우를 제외하면정의되어 있지 않습니다.

• 각 스택 맵 오프셋에는 해당 명령 오프셋이 있습니다.

• 스택 맵은 단순하게 증가하는 순서로 되어 있습니다.

17페이지

<!-- page 18/68 -->

#### 3.2.5 예외 처리

명령에 적용 가능한 각 예외 처리기를 만족시키는 경우 명령은 해당 예외 처리기를 만족시킵니다.

instructionSatisfiesHandlers(Environment, Offset, ExceptionStackFrame) :- exceptionHandlers(Environment, Handlers), sublist(isApplicableHandler(Offset), Handlers, ApplicableHandlers), checklist(instructionSatisfiesHandler(Environment, ExceptionStackFrame), ApplicableHandlers). 명령의 오프셋이 처리기 범위의 시작 이후이고 처리기 범위의 마지막 이전인 경우 예외 처리기를 명령에 적용 가능합니다.

isApplicableHandler(Offset, handler(Start, End, _Target, _ClassName)) :- Offset >= Start, Offset < End. 수신 유형 상태가 StackFrame이고 처리기의 대상(처리기 코드의 초기 명령)이 수신 유형 상태 T를 가정하여 유형 안정적인 경우 명령은 예외 처리기를 만족시킵니다. 유형 상태 T는 피연산자 스택을 유일한 요소가 처리기의 예외 클래스인 스택으로 바꾸어 StackFrame에서 파생됩니다.

instructionSatisfiesHandler(Environment, StackFrame, Handler) :- Handler = handler(_, _, Target, _), handlerExceptionClass(Handler, ExceptionClass), /* The stack consists of just the exception. */ StackFrame = frame(Locals, _, Flags), targetIsTypeSafe(Environment, frame(Locals, [ ExceptionClass ], Flags), Target). 처리기 클래스 항목이 0인 경우 처리기의 예외 클래스는 Throwable이며 그렇지 않은 경우는 처리기에 이름이 지정되어 있는 클래스입니다.

handlerExceptionClass(handler(_, _, _, 0), class(’java/lang/Throwable’)). handlerExceptionClass(handler(_, _, _, Name), class(Name)) :- Name \= 0. handlersAreLegal(Environment) :- exceptionHandlers(Environment, Handlers), checklist(handlerIsLegal(Environment), Handlers). 18페이지

<!-- page 19/68 -->

예외 처리기의 시작(Start)이 끝(End)보다 작고 오프셋이 Start와 같은 명령, 오프셋이 End와 같은 명령이면 처리기의 예외 클래스를 클래스 Throwable에 할당할 수 있는 경우 예외 처리기는 적법합니다.

handlerIsLegal(Environment, Handler) :- Handler = handler(Start, End, Target, _), Start < End, allInstructions(Environment, Instructions), member(instruction(Start, _), Instructions), offsetStackFrame(Environment, Target, _), instructionsIncludeEnd(Instructions, End), handlerExceptionClass(Handler, ExceptionClass), isAssignable(ExceptionClass, class(’java/lang/Throwable’)). instructionsIncludeEnd(Instructions, End) :- member(instruction(End, _), Instructions). instructionsIncludeEnd(Instructions, End) :- member(endOfCode(End), Instructions). 19페이지

<!-- page 20/68 -->

### 3.3 명령

#### 3.3.1 동일 구조 명령

많은 바이트 코드에는 다른 바이트 코드의 규칙과 완전히 동일한 구조의 유형(type) 규칙이 있습니다.

바이트 코드 b1이 다른 바이트 코드 b2와 동일한 구조인 경우 b1의 유형 규칙은 b2의 유형 규칙과 같습니다.

instructionIsTypeSafe(Instruction, Environment, Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- instructionHasEquivalentTypeRule(Instruction, IsomorphicInstruction), instructionIsTypeSafe(IsomorphicInstruction, Environment, Offset, StackFrame, NextStackFrame, ExceptionStackFrame).

#### 3.3.2 피연산자 스택 조작

이 절은 유형 상태의 피연산자 스택을 적절히 조작하는 규칙을 정의합니다. 피연산자 스택의 조작은일부 유형이 스택의 두 항목을 차지한다는 사실에 의해 복잡해집니다. 이 절에 주어진 술어는 규격의나머지 부분에서 이 문제를 추출할 수 있도록 이 내용을 고려합니다.

canPop(frame(Locals, OperandStack, Flags), Types, frame(Locals, PoppedOperandStack, Flags)) :- popMatchingList(OperandStack, Types, PoppedOperandStack). popMatchingList(OperandStack, [], OperandStack). popMatchingList(OperandStack, [P | Rest], NewOperandStack) :- popMatchingType(OperandStack, P, TempOperandStack, _ActualType), popMatchingList(TempOperandStack, Rest, NewOperandStack). 스택에서 개별 유형을 제거합니다. 다시 말해 스택의 논리상 맨 위가 지정한 유형 Type의 일부 서브타입인 경우 표시합니다. 유형이 두 개의 스택 슬롯을 차지하는 경우 스택 유형의 논리상 맨 위는 맨 위바로 아래에 있는 유형이고 스택의 맨 위가 사용 가능하지 않은 유형 top입니다.

popMatchingType([ActualType | OperandStack], Type, OperandStack, ActualType) :- sizeOf(Type, 1), isAssignable(ActualType, Type). popMatchingType([top, ActualType | OperandStack], Type, OperandStack, ActualType) :- sizeOf(Type, 2), isAssignable(ActualType, Type). 20페이지

<!-- page 21/68 -->

논리 유형을 스택에 푸시합니다. 정확한 동작은 유형 크기에 따라 달라집니다. 푸시된 유형의 크기가 1인 경우 스택에 푸시하기만 하면 됩니다. 푸시된 유형의 크기가 2인 경우 푸시한 다음 top을 푸시합니다.

pushOperandStack(OperandStack, ’void’, OperandStack). pushOperandStack(OperandStack, Type, [Type | OperandStack]) :- sizeOf(Type, 1). pushOperandStack(OperandStack, Type, [top, Type | OperandStack]) :- sizeOf(Type, 2). 피연산자 스택의 길이는 선언한 최대 스택 길이를 초과하면 안 됩니다.

operandStackHasLegalLength(Environment, OperandStack) :- length(OperandStack, Length), maxOperandStackLength(Environment, MaxStack), Length =< MaxStack. JVMS에 의해 정의된 대로 범주 1 유형은 단일 스택 슬롯을 차지합니다. 스택의 맨 위가 Type이고 Type이 top이 아닌 경우(반대의 경우 범주 2 유형의 위쪽 반을 나타낼 수 있음) 범주 1의 논리 유형 Type을 스택에서 제거하는 것이 가능합니다. 결과는 맨 위 슬롯이 사라진 수신 스택입니다.

popCategory1([Type | Rest], Type, Rest) :- Type \=top, sizeOf(Type, 1). JVMS에 의해 정의된 대로 범주 2 유형은 두 개의 스택 슬롯을 차지합니다. 스택의 맨 위가 top이고 바로 그 아래에 있는 슬롯이 Type인 경우 범주 2의 논리 유형 Type을 스택에서 제거하는 것이 가능합니다. 결과는 맨 위 2개의 슬롯이 사라진 수신 스택입니다.

popCategory2([top, Type | Rest], Type, Rest) :- sizeOf(Type, 2). canSafelyPush(Environment, InputOperandStack, Type, OutputOperandStack) :- pushOperandStack(InputOperandStack, Type, OutputOperandStack), operandStackHasLegalLength(Environment, OutputOperandStack). canSafelyPushList(Environment, InputOperandStack, Types, OutputOperandStack) :- canPushList(InputOperandStack, Types, OutputOperandStack), operandStackHasLegalLength(Environment, OutputOperandStack). 21페이지

<!-- page 22/68 -->

canPushList(InputOperandStack, [Type | Rest], OutputOperandStack) :- pushOperandStack(InputOperandStack, Type, InterimOperandStack), canPushList(InterimOperandStack, Rest, OutputOperandStack). canPushList(InputOperandStack, [], InputOperandStack).

#### 3.3.3 로드

모든 로드 명령은 일반 패턴의 변형으로 명령이 로드하는 값의 유형에 변화를 줍니다.

해당 로컬 변수의 유형이 ActualType이고 ActualType을 Type에 할당할 수 있으며 ActualType을 수신피연산자 스택에 푸시하는 것이 새 유형 상태 NextStackFrame을 산출하는 유효한 유형 전이인 경우로컬 변수 Index에서 유형 Type의 값을 로드하는 것은 유형 안정적입니다. 로드 명령을 실행한 다음유형 상태는 NextStackFrame이 됩니다.

loadIsTypeSafe(Environment, Index, Type, StackFrame, NextStackFrame) :- StackFrame = frame(Locals, _OperandStack, _Flags), nth0(Index, Locals, ActualType), isAssignable(ActualType, Type), validTypeTransition(Environment, [], ActualType, StackFrame, NextStackFrame).

#### 3.3.4 저장

모든 저장 명령은 일반 패턴의 변형으로 명령이 저장하는 값의 유형에 변화를 줍니다.

참조하는 로컬 변수가 Type의 수퍼 타입인 유형이고 피연산자 스택의 맨 위가 Type의 서브 타입인경우 일반적으로 저장 명령은 유형 안정적입니다. 여기서 Type은 명령이 저장할 유형입니다.

다시 말해 Type과 “일치하는” 유형 ActualType(즉 Type의 서브 타입)을 피연산자 스택에서 제거한다음 해당 유형에 로컬 변수 L 를 올바로 할당할 수 있는 경우 저장은 유형 안정적입니다.

Index storeIsTypeSafe(_Environment, Index, Type, frame(Locals, OperandStack, Flags), frame(NextLocals, NextOperandStack, Flags)) :- popMatchingType(OperandStack, Type, NextOperandStack, ActualType), modifyLocalVariable(Index, ActualType, Locals, NextLocals). 22페이지

<!-- page 23/68 -->

로컬 변수 Locals의 경우 L 가 유형 Type을 갖도록 수정하면 로컬 변수 목록 NewLocals가 생깁 Index 니다. 일부 값(및 해당 유형)은 두 개의 로컬 변수를 차지하기 때문에 수정과 약간 관련되어 있습니다.

따라서 L 을 수정하려면 L (유형은 N과 N+1 슬롯을 모두 차지할 것이므로)이나 L (로컬 N은 로컬 N N+1 N-1 N-1에서 시작하는 두 가지 단어 값/유형의 위쪽 반이므로 로컬 N-1은 무효가 되어야 함) 또는 두 가지모두를 수정해야 할 수 있습니다. 이러한 내용은 좀 더 아래에서 설명합니다. L 부터 카운트합니다.

modifyLocalVariable(Index, Type, Locals, NewLocals) :- modifyLocalVariable(0, Index, Type, Locals, NewLocals). 색인 I에서 시작하는 로컬 변수 목록의 접미사, LocalsSuffix의 경우 로컬 변수 색인이 유형 Type을 갖게수정하면 로컬 변수 목록 접미사 NewLocalsSuffix가 생깁니다.

I < Index-1인 경우 입력을 출력에 복사만 하고 앞으로 순환합니다. I = Index-1인 경우 로컬 I의 유형은변경될 수 있습니다. L에 크기 2인 유형이 있는 경우 그렇습니다. L 을 새 유형(및 해당 값)으로 설정 I I+1 하면 위쪽 반이 비워짐에 따라 L의 유형/값은 무효화됩니다. 그런 다음 앞으로 순환합니다.

변수를 찾았는데 한 단어만 차지하는 경우 Type으로 변경하기만 하면 됩니다.

변수를 찾았는데 두 단어를 차지하는 경우 이 유형을 Type으로 변경하고 다음 단어는 top으로 변경합니다.

modifyLocalVariable(I, Index, Type, [Locals1 | LocalsRest], [Locals1 | NextLocalsRest] ) :- I < Index - 1, I1 is I + 1, modifyLocalVariable(I1, Index, Type, LocalsRest, NextLocalsRest). modifyLocalVariable(I, Index, Type, [Locals1 | LocalsRest], [NextLocals1 | NextLocalsRest] ) :- I =:= Index - 1, modifyPreIndexVariable(Locals1, NextLocals1), modifyLocalVariable(Index, Index, Type, LocalsRest, NextLocalsRest). modifyLocalVariable(Index, Index, Type, [_ | LocalsRest], [Type | LocalsRest] ) :- sizeOf(Type, 1). modifyLocalVariable(Index, Index, Type, [_, _ | LocalsRest], [Type, top | LocalsRest]) :- sizeOf(Type, 2). 23페이지

<!-- page 24/68 -->

유형을 선행 색인 변수로 수정할 로컬 바로 앞에 색인이 있는 로컬을 참조합니다. 유형 InputType의선행 색인 변수의 차후 유형은 Result입니다. 선행 색인 로컬의 유형 Value의 크기가 1인 경우 변경되지않습니다. 선행 색인 로컬 유형 Value의 크기가 2인 경우 두 단어 값 중 아래쪽 반의 유형을 top으로 설정하여 사용할 수 없음으로 표시해야 합니다.

modifyPreIndexVariable(Value, Value) :- sizeOf(Value, 1). modifyPreIndexVariable(Value, top) :- sizeOf(Value, 2). 유형 목록에서 이 절은 크기가 2인 각 유형을 두 개의 항목(하나는 자신의 유형, 다른 하나는 top 항목) 으로 대체한 목록을 만듭니다.

expandTypeList([], []). expandTypeList([Item | List], [Item | Result]) :- sizeOf(Item, 1), expandTypeList(List, Result). expandTypeList([Item | List], [Item, top | Result]) :- sizeOf(Item, 2), expandTypeList(List, Result).

#### 3.3.5 모든 명령 목록

일반적으로 명령의 유형(type) 규칙은 명령이 발생하는 클래스 및 메소드를 정의하는 Environment와 명령이 발생하는 메소드 내의 오프셋 Offset과 관련하여 주어집니다. 수신 유형 상태 StackFrame이 특정 요구 사항을 이행하는 경우 규칙은다음 상태가 됩니다.

• 명령은 유형 안정적입니다.

• 명령이 정상적으로 완료된 다음 유형 상태에 NextStackFrame에 의해 주어진 특정 형식이 있다는 것과 명령이 갑자기 완료된 다음 유형 상태는 ExceptionStackFrame에 의해 주어진다는 것을 확인할 수 있습니다.

규칙의 자연 언어 설명은 읽기 쉽고, 직관적이며 간결한 것이 목적입니다. 따라서 설명은 위에 제시된 문맥상의 가정 전체를 반복하지 않습니다. 특히 다음과 같습니다.

• 명시적으로 환경을 언급하지 않습니다.

• 다음에서 피연산자 스택이나 로컬 변수를 말하면 유형 상태(수신 상태 유형이나 송신 유형 상태 중 하나)의 피연산자 스택과 로컬 변수 구성 요소를 언급하는 것입니다.

• 명령이 갑자기 완료된 다음의 유형 상태는 거의 항상 수신 유형 상태와 같습니다. 명령이 해당하는 경우가 아니면갑자기 명령을 완료한 다음의 유형 상태만 설명합니다.

• 피연산자 스택에서 유형을 표시하고 푸시하는 것에 대해 설명합니다. 스택 언더플로나 오버플로의 문제에 대해서는명시적으로 설명하지 않지만 이러한 작업이 성공적으로 완료될 수 있다고 가정합니다. 피연산자 스택의 형식 규칙은 필요한 검사가 이루어졌다는 것을 확인합니다.

• 마찬가지로 텍스트에선 논리 유형의 조작만 설명합니다. 실제로 일부 유형은 보다 자세히 설명되어 있습니다. 여기에서는 이러한 유형의 세부 정보를 간추리고 데이터를 조작하는 논리 규칙에 대해서는 다루지 않습니다.

형식 Prolog 규칙을 참조하면 모호성이 해결됩니다.

24페이지

<!-- page 25/68 -->

aaload 일치하는 int 유형 및 요소 유형이 ElementType인 배열 유형(여기서 ElementType은 Object의 서브 타입임)을 ElementType으로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 aaload 명령은유형 안정적입니다.

instructionIsTypeSafe(aaload, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- nth1OperandStackIs(2, StackFrame, ArrayType), arrayElementType(ArrayType, ElementType), validTypeTransition(Environment, [int, arrayOf(class(’java/lang/Object’))], ElementType, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). X 배열의 요소 유형은 X입니다.

arrayElementType(arrayOf(X), X). null의 요소 유형을 null로 정의합니다.

arrayElementType(null, null). aastore: 일치하는 Object 유형, int 및 Object의 배열을 수신 피연산자 스택에서 올바로 제거하여 송신 유형상태를 산출할 수 있는 경우 aastore 명령은 유형 안정적입니다.

instructionIsTypeSafe(aastore, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [class(’java/lang/Object’), int, arrayOf(class(’java/lang/Object’))], NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). aconst_null: 유형 null을 수신 피연산자 스택에 올바로 푸시하여 송신 유형 상태를 산출할 수 있는 경우 aconst_null 명령은 유형 안정적입니다.

instructionIsTypeSafe(aconst_null, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [], null, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 25페이지

<!-- page 26/68 -->

aload 피연산자 Index와 유형 reference가 있는 로드 명령이 유형 안정적이고 송신 유형 상태 NextStackFrame을 산출하는 경우 피연산자 Index가 있는 aload 명령은 유형 안정적이며 송신 유형상태 NextStackFrame을 산출합니다.

instructionIsTypeSafe(aload(Index), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- loadIsTypeSafe(Environment, Index, reference, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). aload_<n> 명령 aload_<n> (0≤n≤3인 경우)은 동일한 aload 명령이 유형 안정적인 경우 유형 안정적입니다.

instructionHasEquivalentTypeRule(aload_0, aload(0)). instructionHasEquivalentTypeRule(aload_1, aload(1)). instructionHasEquivalentTypeRule(aload_2, aload(2)). instructionHasEquivalentTypeRule(aload_3, aload(3)). anewarray: CP가 클래스 유형이나 배열 유형 중 하나를 나타내는 상수 풀 항목을 참조하고, 수신 피연산자 스택의일치하는 int 유형을 구성 요소 유형 CP가 있는 배열로 적절하게 바꾸어 송신 유형 상태를 산출할수 있는 경우 피연산자 CP가 있는 anewarray 명령은 유형 안정적입니다.

instructionIsTypeSafe(anewarray(CP), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- (CP = class(_) ; CP = arrayOf(_)), validTypeTransition(Environment, [int], arrayOf(CP), StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). areturn: 포함 메소드에 참조 유형인 선언된 반환 유형 ReturnType이 있으며 일치하는 ReturnType 유형을 수신피연산자 스택에서 올바로 제거할 수 있는 경우 areturn 명령은 유형 안정적입니다.

instructionIsTypeSafe(areturn, Environment, _Offset, StackFrame, afterGoto, ExceptionStackFrame) :- thisMethodReturnType(Environment, ReturnType), isAssignable(ReturnType, reference), canPop(StackFrame, [ReturnType], _PoppedStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 26페이지

<!-- page 27/68 -->

arraylength: 수신 피연산자 스택의 배열 유형을 유형 int로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 arraylength 명령은 유형 안정적입니다.

instructionIsTypeSafe(arraylength, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- nth1OperandStackIs(1, StackFrame, ArrayType), arrayElementType(ArrayType, _), % ensure that it is an Array validTypeTransition(Environment, [top], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). astore: 피연산자 Index와 유형 reference가 있는 저장 명령이 유형 안정적이고 송신 유형 상태 NextStackFrame을 산출하는 경우 피연산자 Index가 있는 astore 명령은 유형 안정적이며 송신 유형상태 NextStackFrame을 산출합니다.

instructionIsTypeSafe(astore(Index), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- storeIsTypeSafe(Environment, Index, reference, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). astore_<n>: 명령 astore_<n> (0≤n≤3인 경우)은 동일한 astore 명령이 유형 안정적인 경우 유형 안정적입니다.

instructionHasEquivalentTypeRule(astore_0, astore(0)). instructionHasEquivalentTypeRule(astore_1, astore(1)). instructionHasEquivalentTypeRule(astore_2, astore(2)). instructionHasEquivalentTypeRule(astore_3, astore(3)). athrow: 피연산자 스택의 맨 위가 Throwable과 일치하는 경우 athrow 명령은 유형 안정적입니다.

instructionIsTypeSafe(athrow, _Environment, _Offset, StackFrame, afterGoto, ExceptionStackFrame) :- canPop(StackFrame, [class(’java/lang/Throwable’)], _PoppedStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 27페이지

<!-- page 28/68 -->

baload: 일치하는 int 유형 및 수신 피연산자 스택의 작은 배열 유형을 int로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 baload 명령은 유형 안정적입니다.

instructionIsTypeSafe(baload, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- nth1OperandStackIs(2, StackFrame, Array), isSmallArray(Array), validTypeTransition(Environment, [int, top], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). byte의 배열, boolean의 배열 또는 서브 타입(null)인 경우 배열 유형은 작은 배열 유형입니다.

isSmallArray(arrayOf(byte)). isSmallArray(arrayOf(boolean)). isSmallArray(null). bastore: 일치하는 int 유형, int 및 작은 배열 유형을 수신 피연산자 스택에서 올바로 제거하여 송신 유형 상태를 산출할 수 있는 경우 bastore 명령은 유형 안정적입니다.

instructionIsTypeSafe(bastore, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- nth1OperandStackIs(3, StackFrame, Array), isSmallArray(Array), canPop(StackFrame, [int, int, top], NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). bipush: 동일한 sipush 명령이 유형 안정적인 경우 bipush 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(bipush(Value), sipush(Value)). 28페이지

<!-- page 29/68 -->

caload: 일치하는 int 유형 및 수신 피연산자 스택의 char의 배열을 int로 올바로 바꾸어 송신 유형 상태를산출할 수 있는 경우 caload 명령은 유형 안정적입니다.

instructionIsTypeSafe(caload, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int, arrayOf(char)], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). castore: 일치하는 int, int 및 char의 배열을 수신 피연산자 스택에서 올바로 제거하여 송신 유형 상태를산출할 수 있는 경우 castore 명령은 유형 안정적입니다.

instructionIsTypeSafe(castore, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [int, int, arrayOf(char)], NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). checkcast: CP가 클래스나 배열 중 하나를 나타내는 상수 풀 항목을 참조하고 수신 피연산자 스택의 맨 위에 있는유형 Object를 CP가 나타내는 유형으로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 피연산자 CP가 있는 checkcast 명령은 유형 안정적입니다.

instructionIsTypeSafe(checkcast(CP), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- (CP = class(_) ; CP = arrayOf(_)), validTypeTransition(Environment, [class(’java/lang/Object’)], CP, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). d2f: 수신 피연산자 스택에서 double을 제거하고, float으로 올바로 바꾸어 송신 유형 상태를 산출할 수있는 경우 d2f 명령은 유형 안정적입니다.

instructionIsTypeSafe(d2f, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [double], float, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 29페이지

<!-- page 30/68 -->

d2i: 수신 피연산자 스택에서 double을 올바로 제거하고, int로 바꾸어 송신 유형 상태를 산출할 수 있는경우 d2i 명령은 유형 안정적입니다.

instructionIsTypeSafe(d2i, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [double], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). d2l: 수신 피연산자 스택에서 double을 올바로 제거하고 long으로 바꾸어 송신 유형 상태를 산출할 수있는 경우 d2l 명령은 유형 안정적입니다.

instructionIsTypeSafe(d2l, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [double], long, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). dadd: 일치하는 double 유형 및 수신 피연산자 스택의 double을 double로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 dadd 명령은 유형 안정적입니다.

instructionIsTypeSafe(dadd, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [double, double], double, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). daload: 일치하는 int 유형 및 수신 피연산자 스택의 double 배열을 double로 올바로 바꾸어 송신 유형 스택을 산출할 수 있는 경우 daload 명령은 유형 안정적입니다.

instructionIsTypeSafe(daload, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int, arrayOf(double)], double, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 30페이지

<!-- page 31/68 -->

dastore: 일치하는 double 유형, int 및 double의 배열을 수신 피연산자 스택에서 올바로 제거하여 송신 유형상태를 산출할 수 있는 경우 dastore 명령은 유형 안정적입니다.

instructionIsTypeSafe(dastore, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [double, int, arrayOf(double)], NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). dcmp<op>: 일치하는 double 유형 및 수신 피연산자 스택에 있는 double을 int와 올바로 바꾸어 송신 유형상태를 산출할 수 있는 경우 dcmpg 명령은 유형 안정적입니다.

instructionIsTypeSafe(dcmpg, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [double, double], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 동일한 dcmpg 명령이 유형 안정적인 경우 dcmpl 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(dcmpl, dcmpg). dconst_<d>: 유형 double을 피연산자 스택에 올바로 푸시하여 송신 유형 상태를 산출할 수 있는 경우 dconst_0 명령은 유형 안정적입니다.

instructionIsTypeSafe(dconst_0, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [], double, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 동일한 dconst_0 명령이 유형 안정적인 경우 dconst_1 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(dconst_1, dconst_0). ddiv: 동일한 dadd 명령이 유형 안정적인 경우 ddiv 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(ddiv, dadd). 31페이지

<!-- page 32/68 -->

dload: 피연산자 Index와 유형 double이 있는 로드 명령이 유형 안정적이고 송신 유형 상태 NextStackFrame을 산출하는 경우 피연산자 Index가 있는 dload 명령은 유형 안정적이며 송신 유형상태 NextStackFrame을 산출합니다.

instructionIsTypeSafe(dload(Index), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- loadIsTypeSafe(Environment, Index, double, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). dload_<n>: 명령 dload_<n> (0≤n≤3인 경우)은 동일한 dload 명령이 유형 안정적인 경우 유형 안정적입니다.

instructionHasEquivalentTypeRule(dload_0, dload(0)). instructionHasEquivalentTypeRule(dload_1, dload(1)). instructionHasEquivalentTypeRule(dload_2, dload(2)). instructionHasEquivalentTypeRule(dload_3, dload(3)). dmul: 동일한 dadd 명령이 유형 안정적인 경우 dmul 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(dmul, dadd). dneg: 수신 피연산자 스택에 일치하는 double 유형이 있는 경우 dneg 명령은 유형 안정적입니다. dneg 명령은 유형 상태를 바꾸지 않습니다.

instructionIsTypeSafe(dneg, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [double], double, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). drem: 동일한 dadd 명령이 유형 안정적인 경우 drem 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(drem, dadd). 32페이지

<!-- page 33/68 -->

dreturn: 포함 메소드에 double의 선언된 반환 유형이 있고 double과 일치하는 유형을 수신 피연산자 스택에서 올바로 제거할 수 있는 경우 dreturn 명령은 유형 안정적입니다.

instructionIsTypeSafe(dreturn, Environment, _Offset, StackFrame, afterGoto, ExceptionStackFrame) :- thisMethodReturnType(Environment, double), canPop(StackFrame, [double], _PoppedStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). dstore: 피연산자 Index와 유형 double이 있는 저장 명령이 유형 안정적이고 송신 유형 상태 NextStackFrame을 산출하는 경우 피연산자 Index가 있는 dstore 명령은 유형 안정적이고 송신 유형상태 NextStackFrame을 산출합니다.

instructionIsTypeSafe(dstore(Index), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- storeIsTypeSafe(Environment, Index, double, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). dstore_<n>: 명령 dstore_<n> (0≤n≤3인 경우)은 동일한 dstore 명령이 유형 안정적인 경우 유형 안정적입니다.

instructionHasEquivalentTypeRule(dstore_0, dstore(0)). instructionHasEquivalentTypeRule(dstore_1, dstore(1)). instructionHasEquivalentTypeRule(dstore_2, dstore(2)). instructionHasEquivalentTypeRule(dstore_3, dstore(3)). dsub: 동일한 dadd 명령이 유형 안정적인 경우 dsub 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(dsub, dadd). 33페이지

<!-- page 34/68 -->

dup: 범주 1 유형 Type을 유형 Type, Type으로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 dup 명령은 유형 안정적입니다.

instructionIsTypeSafe(dup, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- StackFrame = frame(Locals, InputOperandStack, Flags), popCategory1(InputOperandStack, Type, _), canSafelyPush(Environment, InputOperandStack, Type, OutputOperandStack), NextStackFrame = frame(Locals, OutputOperandStack, Flags), exceptionStackFrame(StackFrame, ExceptionStackFrame). dup_x1: 수신 피연산자 스택에 있는 두 가지 범주 1 유형 Type1과 Type2를 유형 Type1, Type2, Type1로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 dup_x1 명령은 유형 안정적입니다.

instructionIsTypeSafe(dup_x1, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- StackFrame = frame(Locals, InputOperandStack, Flags), popCategory1(InputOperandStack, Type1, Stack1), popCategory1(Stack1, Type2, Rest), canSafelyPushList(Environment, Rest, [Type1, Type2, Type1], OutputOperandStack), NextStackFrame = frame(Locals, OutputOperandStack, Flags), exceptionStackFrame(StackFrame, ExceptionStackFrame). dup_x2: dup_x2 명령이 dup_x2 명령의 유형 안정적인 형식인 경우 유형 안정적입니다.

instructionIsTypeSafe(dup_x2, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- StackFrame = frame(Locals, InputOperandStack, Flags), dup_x2SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack), NextStackFrame = frame(Locals, OutputOperandStack, Flags), exceptionStackFrame(StackFrame, ExceptionStackFrame). 34페이지

<!-- page 35/68 -->

dup_x2 명령이 유형 안정적인 형식 1 dup_x2 명령이거나 유형 안정적인 형식 2 dup_x2 명령인 경우 dup_x2 명령은 유형 안정적인 형식입니다.

dup_x2SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- dup_x2Form1IsTypeSafe(Environment, InputOperandStack, OutputOperandStack). dup_x2SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- dup_x2Form2IsTypeSafe(Environment, InputOperandStack, OutputOperandStack). 수신 피연산자 스택에 있는 세 개의 범주 1 유형 Type1, Type2, Type3을 유형 Type1, Type3, Type2, Type1로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 dup_x2 명령은 유형 안정적인 형식 1 dup_x2 명령입니다.

dup_x2Form1IsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- popCategory1(InputOperandStack, Type1, Stack1), popCategory1(Stack1, Type2, Stack2), popCategory1(Stack2, Type3, Rest), canSafelyPushList(Environment, Rest, [Type1, Type3, Type2, Type1], OutputOperandStack). 수신 피연산자 스택의 범주 1 유형 Type1과 범주 2 유형 Type2를 유형 Type1, Type2, Type1로 바꾸어송신 유형 상태를 산출할 수 있는 경우 dup_x2 명령은 유형 안정적인 형식 2 dup_x2 명령입니다.

dup_x2Form2IsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- popCategory1(InputOperandStack, Type1, Stack1), popCategory2(Stack1, Type2, Rest), canSafelyPushList(Environment, Rest, [Type1, Type2, Type1], OutputOperandStack). dup2: dup2 명령이 dup2 명령의 유형 안정적인 형식인 경우 유형 안정적입니다.

instructionIsTypeSafe(dup2, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- StackFrame = frame(Locals, InputOperandStack, Flags), dup2SomeFormIsTypeSafe(Environment,InputOperandStack, OutputOperandStack), NextStackFrame = frame(Locals, OutputOperandStack, Flags), exceptionStackFrame(StackFrame, ExceptionStackFrame). 35페이지

<!-- page 36/68 -->

dup2 명령이 유형 안정적인 형식 1 dup2 명령이거나 유형 안정적인 형식 2 dup2 명령인 경우 dup2 명령은 유형 안정적인 형식입니다.

dup2SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- dup2Form1IsTypeSafe(Environment,InputOperandStack, OutputOperandStack). dup2SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- dup2Form2IsTypeSafe(Environment,InputOperandStack, OutputOperandStack). 수신 피연산자 스택에 있는 두 개의 범주 1 유형 Type1, Type2를 유형 Type2, Type1로 올바로 바꾸어송신 유형 상태를 산출할 수 있는 경우 dup2 명령은 유형 안정적인 형식 1 dup2 명령입니다.

dup2Form1IsTypeSafe(Environment, InputOperandStack, OutputOperandStack):- popCategory1(InputOperandStack, Type1, Stack1), popCategory1(Stack1, Type2, _), canSafelyPushList(Environment, InputOperandStack, [Type2, Type1], OutputOperandStack). 수신 피연산자 스택에 있는 범주 2 유형 Type을 유형 Type, Type으로 올바로 바꾸어 송신 유형 상태를산출할 수 있는 경우 dup2 명령은 유형 안정적인 형식 2 dup2 명령입니다.

dup2Form2IsTypeSafe(Environment, InputOperandStack, OutputOperandStack):- popCategory2(InputOperandStack, Type, _), canSafelyPush(Environment, InputOperandStack, Type, OutputOperandStack). dup2_x1: dup2_x1 명령이 dup2_x1 명령의 유형 안정적인 형식인 경우 유형 안정적입니다.

instructionIsTypeSafe(dup2_x1, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- StackFrame = frame(Locals, InputOperandStack, Flags), dup2_x1SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack), NextStackFrame = frame(Locals, OutputOperandStack, Flags), exceptionStackFrame(StackFrame, ExceptionStackFrame). dup2_x1 명령이 유형 안정적인 형식 1 dup2_x1 명령이거나 유형 안정적인 형식 2 dup_x2 명령인경우 dup2_x1 명령은 유형 안정적인 형식입니다.

dup2_x1SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- dup2_x1Form1IsTypeSafe(Environment, InputOperandStack, OutputOperandStack). dup2_x1SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- dup2_x1Form2IsTypeSafe(Environment, InputOperandStack, OutputOperandStack). 36페이지

<!-- page 37/68 -->

수신 피연산자 스택에서 세 개의 범주 1 유형 Type1, Type2, Type3을 유형 Type2, Type1, Type3, Type2, Type1로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 dup2_x1 명령은 유형 안정적인 형식 1 dup2_x1 명령입니다.

dup2_x1Form1IsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- popCategory1(InputOperandStack, Type1, Stack1), popCategory1(Stack1, Type2, Stack2), popCategory1(Stack2, Type3, Rest), canSafelyPushList(Environment, Rest, [Type2, Type1, Type3, Type2, Type1], OutputOperandStack). 수신 피연산자 스택에 있는 범주 2 유형 Type1과 범주 1 유형 Type2를 유형 Type1, Type2, Type1로올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 dup2_x1 명령은 유형 안정적인 형식 2 dup2_x1 명령입니다.

dup2_x1Form2IsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- popCategory2(InputOperandStack, Type1, Stack1), popCategory1(Stack1, Type2, Rest), canSafelyPushList(Environment, Rest, [Type1, Type2, Type1], OutputOperandStack). dup2_x2: dup2_x2 명령이 dup2_x2 명령의 유형 안정적인 형식인 경우 유형 안정적입니다.

instructionIsTypeSafe(dup2_x2, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- StackFrame = frame(Locals, InputOperandStack, Flags), dup2_x2SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack), NextStackFrame = frame(Locals, OutputOperandStack, Flags), exceptionStackFrame(StackFrame, ExceptionStackFrame). 37페이지

<!-- page 38/68 -->

다음 중 하나가 충족된 경우 dup2_x2 명령은 dup2_x2 명령의 유형 안정적인 형식입니다.

• 유형 안정적인 형식 1 dup2_x2 명령 • 유형 안정적인 형식 2 dup_x2 명령 • 유형 안정적인 형식 3 dup_x2 명령 • 유형 안정적인 형식 4 dup_x2 명령 dup2_x2SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- dup2_x2Form1IsTypeSafe(Environment, InputOperandStack, OutputOperandStack). dup2_x2SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- dup2_x2Form2IsTypeSafe(Environment, InputOperandStack, OutputOperandStack). dup2_x2SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- dup2_x2Form3IsTypeSafe(Environment, InputOperandStack, OutputOperandStack). dup2_x2SomeFormIsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- dup2_x2Form4IsTypeSafe(Environment, InputOperandStack, OutputOperandStack). 수신 피연산자 스택에 있는 네 개의 범주 1 유형 Type1, Type2, Type3, Type4를 유형 Type2, Type1, Type4, Type3, Type2, Type1로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 dup2_x2 명령은 유형 안정적인 형식 1 dup2_x2 명령입니다.

dup2_x2Form1IsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- popCategory1(InputOperandStack, Type1, Stack1), popCategory1(Stack1, Type2, Stack2), popCategory1(Stack2, Type3, Stack3), popCategory1(Stack3, Type4, Rest), canSafelyPushList(Environment, Rest, [Type2, Type1, Type4, Type3, Type2, Type1], OutputOperandStack). 수신 피연산자 스택에 있는 범주 2 유형 Type1과 두 개의 범주 1 유형 Type2, Type3을 유형 Type1, Type3, Type2, Type1로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 dup2_x2 명령은 유형안정적인 형식 2 dup2_x2 명령입니다.

dup2_x2Form2IsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- popCategory2(InputOperandStack, Type1, Stack1), popCategory1(Stack1, Type2, Stack2), popCategory1(Stack2, Type3, Rest), canSafelyPushList(Environment, Rest, [Type1, Type3, Type2, Type1], OutputOperandStack). 38페이지

<!-- page 39/68 -->

수신 피연산자 스택에 있는 두 개의 범주 1 유형 Type1, Type2와 범주 2 유형 Type3을 유형 Type2, Type1, Type3, Type2, Type1로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 dup2_x2 명령은 유형 안정적인 형식 3 dup2_x2 명령입니다.

dup2_x2Form3IsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- popCategory1(InputOperandStack, Type1, Stack1), popCategory1(Stack1, Type2, Stack2), popCategory2(Stack2, Type3, Rest), canSafelyPushList(Environment, Rest, [Type2, Type1, Type3, Type2, Type1], OutputOperandStack). 수신 피연산자 스택에 있는 두 개의 범주 2 유형 Type1, Type2를 유형 Type1, Type2, Type1로 올바로바꾸어 송신 유형 상태를 산출할 수 있는 경우 dup2_x2 명령은 유형 안정적인 형식 4 dup2_x2 명령입니다.

dup2_x2Form4IsTypeSafe(Environment, InputOperandStack, OutputOperandStack) :- popCategory2(InputOperandStack, Type1, Stack1), popCategory2(Stack1, Type2, Rest), canSafelyPushList(Environment, Rest, [Type1, Type2, Type1], OutputOperandStack). f2d: 수신 피연산자 스택에서 float을 제거하고, double로 올바로 바꾸어 송신 유형 상태를 산출할 수있는 경우 f2d 명령은 유형 안정적입니다.

instructionIsTypeSafe(f2d, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [float], double, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). f2i: 수신 피연산자 스택에서 float을 제거하고, int를 올바로 바꾸어 송신 유형 상태를 산출할 수 있는경우 f2i 명령은 유형 안정적입니다.

instructionIsTypeSafe(f2i, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [float], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 39페이지

<!-- page 40/68 -->

f2l: 수신 피연산자 스택에서 float을 제거하고, long을 올바로 바꾸어 송신 유형 상태를 산출할 수 있는경우 f2l 명령은 유형 안정적입니다.

instructionIsTypeSafe(f2l, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [float], long, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). fadd: 일치하는 float 유형 및 수신 피연산자 스택에 있는 float을 float과 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 fadd 명령은 유형 안정적입니다.

instructionIsTypeSafe(fadd, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [float, float], float, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). faload: 일치하는 int 유형 및 수신 피연산자 스택에 있는 float의 배열을 float과 올바로 바꾸어 송신 유형상태를 산출할 수 있는 경우 faload 명령은 유형 안정적입니다.

instructionIsTypeSafe(faload, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int, arrayOf(float)], float, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). fastore: 일치하는 float 유형, int 및 float의 배열을 수신 피연산자 스택에서 올바로 제거하여 송신 유형상태를 산출할 수 있는 경우 fastore 명령은 유형 안정적입니다.

instructionIsTypeSafe(fastore, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [float, int, arrayOf(float)], NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 40페이지

<!-- page 41/68 -->

fcmp<op>: 일치하는 float 유형 및 수신 피연산자 스택에 있는 float을 int로 올바로 바꾸어 송신 유형 상태를산출할 수 있는 경우 fcmpg 명령은 유형 안정적입니다.

instructionIsTypeSafe(fcmpg, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [float, float], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 동일한 fcmpg 명령이 유형 안정적인 경우 fcmpl 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(fcmpl, fcmpg). fconst_<f>: 유형 float을 수신 피연산자 스택에 올바로 푸시하여 송신 유형 상태를 산출할 수 있는 경우 fconst_0 명령은 유형 안정적입니다.

instructionIsTypeSafe(fconst_0, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [], float, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). fconst의 다른 변형에 대한 규칙은 다음과 같습니다.

instructionHasEquivalentTypeRule(fconst_1, fconst_0). instructionHasEquivalentTypeRule(fconst_2, fconst_0). fdiv: 동일한 fadd 명령이 유형 안정적인 경우 fdiv 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(fdiv, fadd). fload: 피연산자 Index와 유형 float이 있는 로드 명령이 유형 안정적이고 송신 유형 상태 NextStackFrame 을 산출하는 경우 피연산자 Index가 있는 fload 명령은 유형 안정적이며 송신 유형 상태 NextStackFrame을 산출합니다.

instructionIsTypeSafe(fload(Index), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- loadIsTypeSafe(Environment, Index, float, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 41페이지

<!-- page 42/68 -->

fload_<n>: 명령 fload_<n> (0≤n≤3인 경우)은 동일한 fload 명령이 유형 안정적인 경우 유형 안정적입니다.

instructionHasEquivalentTypeRule(fload_0, fload(0)). instructionHasEquivalentTypeRule(fload_1, fload(1)). instructionHasEquivalentTypeRule(fload_2, fload(2)). instructionHasEquivalentTypeRule(fload_3, fload(3)). fmul: 동일한 fadd 명령이 유형 안정적인 경우 fmul 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(fmul, fadd). fneg: 수신 피연산자 스택에 float과 일치하는 유형이 있는 경우 fneg 명령은 유형 안정적입니다. fneg 명령은 유형 상태를 바꾸지 않습니다.

instructionIsTypeSafe(fneg, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [float], float, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). frem: 동일한 fadd 명령이 유형 안정적인 경우 frem 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(frem, fadd). freturn: 포함 메소드에 float의 선언된 반환 유형이 있고 일치하는 float 유형을 수신 피연산자 스택에서올바로 제거할 수 있는 경우 freturn 명령은 유형 안정적입니다.

instructionIsTypeSafe(freturn, Environment, _Offset, StackFrame, afterGoto, ExceptionStackFrame) :- thisMethodReturnType(Environment, float), canPop(StackFrame, [float], _PoppedStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 42페이지

<!-- page 43/68 -->

fstore: 피연산자 Index와 유형 float이 있는 저장 명령이 유형 안정적이고 송신 유형 상태 NextStackFrame 을 산출하는 경우 피연산자 Index가 있는 fstore 명령은 유형 안정적이며 송신 유형 상태 NextStackFrame을 산출합니다.

instructionIsTypeSafe(fstore(Index), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- storeIsTypeSafe(Environment, Index, float, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). fstore_<n>: 명령 fstore_<n> (0≤n≤3인 경우)은 동일한 fstore 명령이 유형 안정적인 경우 유형 안정적입니다.

instructionHasEquivalentTypeRule(fstore_0, fstore(0)). instructionHasEquivalentTypeRule(fstore_1, fstore(1)). instructionHasEquivalentTypeRule(fstore_2, fstore(2)). instructionHasEquivalentTypeRule(fstore_3, fstore(3)). fsub: 동일한 fadd 명령이 유형 안정적인 경우 fsub 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(fsub, fadd). getfield: 선언된 유형이 클래스 FieldClass에 선언되어 있는 FieldType인 필드를 나타내는 상수 풀 항목을 CP가참조하고 일치하는 FieldClass 유형을 수신 피연산자 스택에 있는 유형 FieldType으로 올바로 바꾸어송신 유형 상태를 산출할 수 있는 경우 피연산자 CP가 있는 getfield 명령은 유형 안정적입니다.

보호되는 필드는 추가 검사를 하기 쉽습니다.

instructionIsTypeSafe(getfield(CP), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- CP = field(FieldClass, FieldName, FieldSignature), parseFieldSignature(FieldSignature, FieldType), passesProtectedCheck(Environment, FieldClass, FieldName, FieldSignature, StackFrame), validTypeTransition(Environment, [class(FieldClass)], FieldType, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 43페이지

<!-- page 44/68 -->

보호 검사는 현재 클래스의 수퍼 클래스 구성원에게만 적용됩니다. 다른 경우는 결정 시 이루어진 액세스 검사에 의해 파악됩니다.

passesProtectedCheck(Environment, MemberClassName, MemberName, MemberSignature, StackFrame) :- thisClass(Environment, class(CurrentClassName)), superclassChain(CurrentClassName, Chain), notMemberOf(MemberClassName, Chain). 보호되지 않는 수퍼 클래스 구성원을 사용하는 것은 어느 정도 맞습니다.

passesProtectedCheck(Environment, MemberClassName, MemberName, MemberSignature, StackFrame) :- thisClass(Environment, class(CurrentClassName)), superclassChain(CurrentClassName, Chain), member(MemberClassName, Chain), isNotProtected(MemberClassName, MemberName, MemberSignature). 유형 Target 객체의 보호되는 수퍼 클래스 구성원을 사용하려면 Target을 현재 클래스의 유형에 할당할 수 있어야 합니다.

passesProtectedCheck(Environment, MemberClassName, MemberName, MemberSignature, [Target, _Rest]) :- thisClass(Environment, class(CurrentClassName)), superclassChain(CurrentClassName, Chain), member(MemberClassName, Chain), isProtected(MemberClassName, MemberName, MemberSignature), isAssignable(Target, class(CurrentClassName)). superclassChain(ClassName, [SuperclassName | Rest]) :- classSuperclassName(class(ClassName), SuperclassName), superclassChain(SuperclassName, Rest). superclassChain(‘java/lang/Object’, []). 44페이지

<!-- page 45/68 -->

getstatic: 선언된 유형이 FieldType인 필드를 나타내는 상수 풀 항목을 CP가 참조하고 수신 피연산자 스택에 FieldType을 올바로 푸시하여 송신 유형 상태를 산출할 수 있는 경우 피연산자 CP가 있는 getstatic 명령은 유형 안정적입니다.

instructionIsTypeSafe(getstatic(CP), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- CP = field(_FieldClass, _FieldName, FieldSignature), parseFieldSignature(FieldSignature, FieldType), validTypeTransition(Environment, [], FieldType, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). goto: 대상 피연산자가 유효한 분기 대상인 경우 goto 명령은 유형 안정적입니다.

instructionIsTypeSafe(goto(Target), Environment, _Offset, StackFrame, afterGoto, ExceptionStackFrame) :- targetIsTypeSafe(Environment, StackFrame, Target), exceptionStackFrame(StackFrame, ExceptionStackFrame). i2b: 동일한 ineg 명령이 유형 안정적인 경우 i2b 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(i2b, ineg). i2c: 동일한 ineg 명령이 유형 안정적인 경우 i2c 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(i2c, ineg). i2d: 수신 피연산자 스택에서 int를 올바로 제거하고, double로 바꾸어 송신 유형 상태를 산출할 수 있는경우 i2d 명령은 유형 안정적입니다.

instructionIsTypeSafe(i2d, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int], double, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 45페이지

<!-- page 46/68 -->

i2f: 수신 피연산자 스택에서 int를 올바로 제거하고, float으로 바꾸어 송신 유형 상태를 산출할 수 있는경우 i2f 명령은 유형 안정적입니다.

instructionIsTypeSafe(i2f, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int], float, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). i2l: int를 수신 피연산자 스택에서 올바로 제거하고, long으로 바꾸어 송신 유형 상태를 산출할 수 있는경우 i2l 명령은 유형 안정적입니다.

instructionIsTypeSafe(i2l, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int], long, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). i2s: 동일한 ineg 명령이 유형 안정적인 경우 i2s 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(i2s, ineg). iadd: 일치하는 int 유형 및 수신 피연산자 스택에 있는 int를 int로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 iadd 명령은 유형 안정적입니다.

instructionIsTypeSafe(iadd, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int, int], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). iaload: 일치하는 int 유형 및 수신 피연산자 스택에 있는 int를 int로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 iaload 명령은 유형 안정적입니다.

instructionIsTypeSafe(iaload, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int, arrayOf(int)], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 46페이지

<!-- page 47/68 -->

iand: 동일한 iadd 명령이 유형 안정적인 경우 iand 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(iand, iadd). iastore: 일치하는 int 유형, int 및 int의 배열을 수신 피연산자 스택에서 올바로 제거하여 송신 유형 상태를산출할 수 있는 경우 iastore 명령은 유형 안정적입니다.

instructionIsTypeSafe(iastore, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [int, int, arrayOf(int)], NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). if_acmp<cond>: 일치하는 reference 유형 및 reference를 수신 피연산자 스택에서 올바로 표시하여 송신 유형상태 NextStackFrame을 산출할 수 있으며, 명령의 피연산자 Target이 NextStackFrame의 수신 유형상태를 가정하는 유효한 분기 대상인 경우 if_acmpeq 명령은 유형 안정적입니다.

instructionIsTypeSafe(if_acmpeq(Target), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [reference, reference], NextStackFrame), targetIsTypeSafe(Environment, NextStackFrame, Target), exceptionStackFrame(StackFrame, ExceptionStackFrame). if_acmp_ne의 규칙은 동일합니다.

instructionHasEquivalentTypeRule(if_acmpne(Target), if_acmpeq(Target)). if_icmp<cond>: 일치하는 int 유형 및 int를 수신 피연산자 스택에서 올바로 표시하여 송신 유형 상태 NextStackFrame을 산출할 수 있으며, 명령의 피연산자 Target이 NextStackFrame의 수신 유형 상태를 가정하는 유효한 분기 대상인 경우 if_icmpeq 명령은 유형 안정적입니다.

instructionIsTypeSafe(if_icmpeq(Target), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [int, int], NextStackFrame), targetIsTypeSafe(Environment, NextStackFrame, Target), exceptionStackFrame(StackFrame, ExceptionStackFrame). if_icmp 명령의 모든 다른 변형에 대한 규칙은 동일합니다.

47페이지

<!-- page 48/68 -->

instructionHasEquivalentTypeRule(if_icmpge(Target), if_icmpeq(Target)). instructionHasEquivalentTypeRule(if_icmpgt(Target), if_icmpeq(Target)). instructionHasEquivalentTypeRule(if_icmple(Target), if_icmpeq(Target)). instructionHasEquivalentTypeRule(if_icmplt(Target), if_icmpeq(Target)). instructionHasEquivalentTypeRule(if_icmpne(Target), if_icmpeq(Target)). if_<cond>: 일치하는 int 유형을 수신 피연산자 스택에서 올바로 제거하여 송신 유형 상태 NextStackFrame을산출할 수 있으며, 명령의 피연산자 Target이 NextStackFrame의 수신 유형 상태를 가정하는 유효한분기 대상인 경우 if_eq 명령은 유형 안정적입니다.

instructionIsTypeSafe(ifeq(Target), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [int], NextStackFrame), targetIsTypeSafe(Environment, NextStackFrame, Target), exceptionStackFrame(StackFrame, ExceptionStackFrame). if<cond> 명령의 모든 다른 변형에 대한 규칙은 동일합니다.

instructionHasEquivalentTypeRule(ifge(Target), ifeq(Target)). instructionHasEquivalentTypeRule(ifgt(Target), ifeq(Target)). instructionHasEquivalentTypeRule(ifle(Target), ifeq(Target)). instructionHasEquivalentTypeRule(iflt(Target), ifeq(Target)). instructionHasEquivalentTypeRule(ifne(Target), ifeq(Target)). ifnonnull: 일치하는 reference 유형을 수신 피연산자 스택에서 올바로 제거하여 송신 유형 상태 NextStackFrame을 산출할 수 있으며, 명령의 피연산자 Target이 NextStackFrame의 수신 유형 상태를 가정하는 유효한 분기 대상인 경우 ifnonnull 명령은 유형 안정적입니다.

instructionIsTypeSafe(ifnonnull(Target), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [reference], NextStackFrame), targetIsTypeSafe(Environment, NextStackFrame, Target), exceptionStackFrame(StackFrame, ExceptionStackFrame). ifnull: 동일한 ifnonnull 명령이 유형 안정적인 경우 ifnull 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(ifnull(Target), ifnonnull(Target)). 48페이지

<!-- page 49/68 -->

iinc: L 에 유형 int가 있는 경우 첫 번째 피연산자 Index가 있는 iinc 명령은 유형 안정적입니다. iinc Index 명령은 유형 상태를 변경하지 않습니다.

instructionIsTypeSafe(iinc(Index, _Value), _Environment, _Offset, StackFrame, StackFrame, ExceptionStackFrame) :- StackFrame = frame(Locals, _OperandStack, _Flags), nth0(Index, Locals, int), exceptionStackFrame(StackFrame, ExceptionStackFrame). iload: 피연산자 Index와 유형 int가 있는 로드 명령이 유형 안정적이고 송신 유형 상태 NextStackFrame을산출하는 경우 피연산자 Index가 있는 iload 명령은 유형 안정적이며 송신 유형 상태 NextStackFrame을 산출합니다.

instructionIsTypeSafe(iload(Index), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- loadIsTypeSafe(Environment, Index, int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). iload_<n>: 명령 iload_<n> (0≤n≤3인 경우)은 동일한 iload 명령이 유형 안정적인 경우 유형 안정적입니다.

instructionHasEquivalentTypeRule(iload_0, iload(0)). instructionHasEquivalentTypeRule(iload_1, iload(1)). instructionHasEquivalentTypeRule(iload_2, iload(2)). instructionHasEquivalentTypeRule(iload_3, iload(3)). imul: 동일한 iadd 명령이 유형 안정적인 경우 imul 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(imul, iadd). ineg: 수신 피연산자 스택에 일치하는 int 유형이 있는 경우 ineg 명령은 유형 안정적입니다. ineg 명령은유형 상태를 바꾸지 않습니다.

instructionIsTypeSafe(ineg, Environment, _Offset, StackFrame, 49페이지

<!-- page 50/68 -->

NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). instanceof: 클래스나 배열을 나타내는 상수 풀 항목을 CP가 참조하고 있으며 수신 피연산자 스택의 맨 위에 있는유형 Object를 유형 int와 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 피연산자 CP가 있는 instanceof 명령은 유형 안정적입니다.

instructionIsTypeSafe(instanceof(CP), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- (CP = class(_) ; CP = arrayOf(_)), validTypeTransition(Environment, [class(’java/lang/Object’)], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). invokeinterface: 다음 조건 모두가 충족되는 경우 invokeinterface 명령은 유형 안정적입니다.

• 첫 번째 피연산자 CP는 인터페이스 MethodClassName의 구성원인, 서명 Signature가 있는 MethodName이라는 인터페이스 메소드를 나타내는 상수 풀 항목을 참조합니다.

• MethodName이 <init>가 아닙니다.

• MethodName이 <clinit>가 아닙니다.

• 두 번째 피연산자 Count는 유효한 카운트 피연산자입니다(아래 참조). • 유형 MethodClassName 및 수신 피연산자 스택에 있는 Signature에 주어진 인자 유형과 일치하는유형을 Signature에 주어진 반환 유형과 올바로 바꾸어 송신 유형 상태를 산출할 수 있습니다.

instructionIsTypeSafe(invokeinterface(CP, Count, 0), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- CP = imethod(MethodClassName, MethodName, Signature), MethodName \= ’<init>’, MethodName \= ’<clinit>’, parseMethodSignature(Signature, OperandArgList, ReturnType), reverse([class(MethodClassName) | OperandArgList], StackArgList), canPop(StackFrame, StackArgList, TempFrame), validTypeTransition(Environment, [], ReturnType, TempFrame, NextStackFrame), countIsValid(Count, StackFrame, TempFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 50페이지

<!-- page 51/68 -->

invokeinterface의 카운트 피연산자가 명령이 실행되기 전과 후의 피연산자 스택 크기의 차이를나타내는 경우 유효합니다.

countIsValid(Count, InputFrame, OutputFrame) :- InputFrame = frame(_Locals1, OperandStack1, _Flags1), OutputFrame = frame(_Locals2, OperandStack2, _Flags2), length(OperandStack1, Length1), length(OperandStack2, Length2), Count =:= Length1 - Length2. invokespecial: 다음 조건이 모두 충족되는 경우 invokespecial 명령은 유형 안정적입니다.

• 첫 번째 피연산자 CP는 클래스 MethodClassName의 구성원인 서명 Signature가 있는 MethodName이라는 메소드를 나타내는 상수 풀 항목을 참조합니다.

다음 중 하나가 충족되는 경우 • MethodName은 <init>가 아닙니다.

• MethodName은 <clinit>가 아닙니다.

• 수신 피연산자 스택에 있는 Signature에 주어진 현재 클래스 및 인자 유형과 일치하는 유형을 Signature에 주어진 반환 유형으로 올바로 바꾸어 송신 유형 상태를 산출할 수 있습니다.

• 수신 피연산자 스택에 있는 Signature에 주어진 클래스 MethodClassName 및 인자 유형과 일치하는 유형을 Signature에 주어진 반환 유형으로 올바로 바꿀 수 있습니다.

instructionIsTypeSafe(invokespecial(CP), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- CP = method(MethodClassName, MethodName, Signature), MethodName \= ’<init>’, MethodName \= ’<clinit>’, parseMethodSignature(Signature, OperandArgList, ReturnType), thisClass(Environment, CurrentClass), reverse([CurrentClass | OperandArgList], StackArgList), validTypeTransition(Environment, StackArgList, ReturnType, StackFrame, NextStackFrame), reverse([class(MethodClassName) | OperandArgList], StackArgList2), validTypeTransition(Environment, StackArgList2, ReturnType, StackFrame, _ResultStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 또는 • MethodName이 <init>입니다.

• Signature는 void 반환 유형을 지정합니다.

51페이지

<!-- page 52/68 -->

• Signature에 주어진 인자 유형 및 초기화되지 않은 유형 UninitializedArg와 일치하는 유형을 수신피연산자 스택에서 올바로 제거하여 OperandStack을 산출할 수 있습니다.

• 먼저 수신 피연산자 스택을 OperandStack으로 바꾸고 UninitializedArg의 모든 인스턴스를 초기화될 인스턴스 유형으로 바꾸면, 송신 유형 상태는 수신 유형 상태에서 파생됩니다.

instructionIsTypeSafe(invokespecial(CP), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- CP = method(MethodClassName, ’<init>’, Signature), parseMethodSignature(Signature, OperandArgList, void), reverse(OperandArgList, StackArgList), canPop(StackFrame, StackArgList, TempFrame), TempFrame = frame(Locals, FullOperandStack, Flags), FullOperandStack = [UninitializedArg | OperandStack], rewrittenUninitializedType(UninitializedArg, Environment, class(MethodClassName), This), rewrittenInitializationFlags(UninitializedArg, Flags, NextFlags), substitute(UninitializedArg, This, OperandStack, NextOperandStack), substitute(UninitializedArg, This, Locals, NextLocals), NextStackFrame = frame(NextLocals, NextOperandStack, NextFlags), ExceptionStackFrame = frame(NextLocals, [], Flags). <init> 메소드의 invokespecial에 대한 특수 규칙입니다.

이 규칙은 개별 예외 스택 프레임을 되돌려 보내는 유일한 동기입니다. 하지만 invokespecial로수퍼 클래스 <init> 메소드를 호출할 수 있거나 호출에 실패하여 this가 초기화되지 않은 채로 남아있을 수도 있습니다. 이러한 상황은 Java 프로그래밍 언어 소스 코드를 사용하면 발생하지 않지만 JVM 어셈블리 프로그래밍을 사용하면 발생할 수 있습니다.

원래 프레임에는 초기화되지 않은 객체와 플래그 uninitializedThis가 있습니다.

invokespecial을 정상 종료하면 초기화되지 않은 객체를 초기화하고 uninitializedThis 플래그를 끕니다. 하지만 <init> 메소드의 호출이 예외를 발생시키면 초기화되지 않은 객체는 부분적으로 초기화되지 않은 상태로 남을 수 있으므로 영구적으로 사용할 수 없게 만들어야 합니다. 이러한 내용은 파손된 객체(로컬의 새 값)가 들어 있는 예외 프레임과 uninitializedThis 플래그(이전 플래그)에 의해 표시됩니다. uninitializedThis 플래그를 가지고 있으면서 외관상 초기화되지 않은객체를 적합하게 초기화된 객체로 만들 수 있는 방법은 없으므로 해당 객체는 영구적으로 사용할 수없습니다. 이러한 경우가 아니라면 예외 스택 프레임은 입력 스택 프레임과 같을 수 있습니다.

rewrittenUninitializedType(uninitializedThis, Environment, _MethodClass, This) :- thisClass(Environment, This). rewrittenUninitializedType(uninitialized(Address), Environment, MethodClass, MethodClass) :- allInstructions(Environment, Instructions), member(instruction(Address, new(MethodClass)), Instructions). 52페이지

<!-- page 53/68 -->

초기화되지 않은 인자 유형을 다시 기록할 유형을 계산합니다.

두 가지 경우가 있습니다.

구성자 내에서 객체를 초기화하는 경우 해당 유형은 처음에는 uninitializedThis입니다. 이 유형은 <init> 메소드 클래스의 유형으로 다시 기록됩니다.

두 번째 경우는 new 명령이 객체를 초기화하는 것입니다. 초기화되지 않은 인자 유형은 <init>의메소드 홀더 유형인 MethodClass로 다시 기록됩니다. Address에 new 명령이 실제로 있는지 여부를검사합니다.

rewrittenInitializationFlags(uninitializedThis, _Flags, []). rewrittenInitializationFlags(uninitialized(_), Flags, Flags). substitute(_Old, _New, [], []). substitute(Old, New, [Old | FromRest], [New | ToRest]) :- substitute(Old, New, FromRest, ToRest). substitute(Old, New, [From1 | FromRest], [From1 | ToRest]) :- From1 \= Old, substitute(Old, New, FromRest, ToRest). invokestatic: 다음 조건이 모두 충족되는 경우 invokestatic 명령은 유형 안정적입니다.

• 첫 번째 피연산자 CP는 서명 Signature가 있는 MethodName이라는 메소드를 나타내는 상수 풀항목을 참조합니다.

• MethodName은 <clinit>가 아닙니다.

• 수신 피연산자 스택에 있는 Signature에 주어진 인자 유형과 일치하는 유형을 Signature에 주어진반환 유형으로 올바로 바꾸어 송신 유형 상태를 산출할 수 있습니다.

instructionIsTypeSafe(invokestatic(CP), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- CP = method(_MethodClassName, MethodName, Signature), MethodName \= ’<clinit>’, parseMethodSignature(Signature, OperandArgList, ReturnType), reverse(OperandArgList, StackArgList), validTypeTransition(Environment, StackArgList, ReturnType, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 53페이지

<!-- page 54/68 -->

invokevirtual: 다음 조건 모두가 충족되는 경우 invokevirtual 명령은 유형 안정적입니다.

• 첫 번째 피연산자 CP는 클래스 MethodClassName의 구성원인, 서명 Signature가 있는 MethodName이라는 메소드를 나타내는 상수 풀 항목을 참조합니다.

• MethodName은 <init>가 아닙니다.

• MethodName은 <clinit>가 아닙니다.

• 클래스 MethodClassName 및 수신 피연산자 스택에 있는 Signature에 주어진 인자 유형과 일치하는 유형을 Signature에 주어진 반환 유형과 올바로 바꾸어 송신 유형 상태를 산출할 수 있습니다.

instructionIsTypeSafe(invokevirtual(CP), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- CP = method(MethodClassName, MethodName, Signature), MethodName \= ’<init>’, MethodName \= ’<clinit>’, parseMethodSignature(Signature, OperandArgList, ReturnType), reverse([class(MethodClassName) | OperandArgList], StackArgList), validTypeTransition(Environment, StackArgList, ReturnType, StackFrame, NextStackFrame), passesProtectedCheck(Environment, MethodClassName, MethodName, Signature, StackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). ior: 동일한 iadd 명령이 유형 안정적인 경우 ior 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(ior, iadd). irem: 동일한 iadd 명령이 유형 안정적인 경우 irem 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(irem, iadd). 54페이지

<!-- page 55/68 -->

ireturn: 포함 메소드에 int의 선언된 반환 유형이 있고 일치하는 int 유형을 수신 피연산자 스택에서 올바로제거하는 경우 ireturn 명령은 유형 안정적입니다.

instructionIsTypeSafe(ireturn, Environment, _Offset, StackFrame, afterGoto, ExceptionStackFrame) :- thisMethodReturnType(Environment, int), canPop(StackFrame, [int], _PoppedStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). ishl: 동일한 iadd 명령이 유형 안정적인 경우 ishl 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(ishl, iadd). ishr: 동일한 iadd 명령이 유형 안정적인 경우 ishr 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(ishr, iadd). istore 피연산자 Index 및 유형 int가 있는 저장 명령이 유형 안정적이고 송신 유형 상태 NextStackFrame을산출하는 경우 피연산자 Index가 있는 istore 명령은 유형 안정적이며 송신 유형 상태 NextStackFrame을 산출합니다.

instructionIsTypeSafe(istore(Index), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- storeIsTypeSafe(Environment, Index, int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). istore_<n>: 명령 istore_<n> (0≤n≤3인 경우)은 동일한 istore 명령이 유형 안정적인 경우 유형 안정적입니다.

instructionHasEquivalentTypeRule(istore_0, istore(0)). instructionHasEquivalentTypeRule(istore_1, istore(1)). instructionHasEquivalentTypeRule(istore_2, istore(2)). instructionHasEquivalentTypeRule(istore_3, istore(3)). 55페이지

<!-- page 56/68 -->

isub: 동일한 iadd 명령이 유형 안정적인 경우 isub 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(isub, iadd). iushr: 동일한 iadd 명령이 유형 안정적인 경우 iushr 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(iushr,iadd). ixor: 동일한 iadd 명령이 유형 안정적인 경우 ixor 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(ixor, iadd). l2d: 수신 피연산자 스택에서 long을 올바로 제거하고 double로 바꾸어 송신 유형 상태를 산출할 수 있는경우 l2d 명령은 유형 안정적입니다.

instructionIsTypeSafe(l2d, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [long], double, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). l2f: 수신 피연산자 스택에서 long을 올바로 제거하고 float으로 바꾸어 송신 유형 상태를 산출할 수있는 경우 l2f 명령은 유형 안정적입니다.

instructionIsTypeSafe(l2f, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [long], float, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). l2i: 수신 피연산자 스택에서 long을 올바로 제거하고, int로 바꾸어 송신 유형 상태를 산출할 수 있는경우 l2i 명령은 유형 안정적입니다.

instructionIsTypeSafe(l2i, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [long], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 56페이지

<!-- page 57/68 -->

ladd: 일치하는 long 유형 및 수신 피연산자 스택에 있는 long을 long과 올바로 바꾸어 송신 유형 상태를산출할 수 있는 경우 ladd 명령은 유형 안정적입니다.

instructionIsTypeSafe(ladd, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [long, long], long, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). laload: 일치하는 int 유형 및 수신 피연산자 스택에 있는 long의 배열을 long으로 올바로 바꾸어 송신 유형상태를 산출할 수 있는 경우 laload 명령은 유형 안정적입니다.

instructionIsTypeSafe(laload, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int, arrayOf(long)], long, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). land: 동일한 ladd 명령이 유형 안정적인 경우 land 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(land, ladd). lastore: 일치하는 long, int 유형 및 long의 배열을 수신 피연산자 스택에서 올바로 제거하여 송신 유형상태를 산출할 수 있는 경우 lastore 명령은 유형 안정적입니다.

instructionIsTypeSafe(lastore, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [long, int, arrayOf(long)], NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). lcmp: 일치하는 long 및 수신 피연산자 스택에 있는 long을 int로 올바로 바꾸어 송신 유형 상태를 산출할수 있는 경우 lcmp 명령은 유형 안정적입니다.

instructionIsTypeSafe(lcmp, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [long, long], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 57페이지

<!-- page 58/68 -->

lconst_<l>: 수신 피연산자 스택에 유형 long을 올바로 푸시하여 송신 유형 상태를 산출할 수 있는 경우 lconst_0 명령은 유형 안정적입니다.

instructionIsTypeSafe(lconst_0, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [], long, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 동일한 lconst_0 명령이 유형 안정적인 경우 lconst_1 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(lconst_1,lconst_0). ldc: CP가 유형 Type(여기서 Type은 int, float, String 중 하나)의 엔티티를 나타내는 상수 풀 항목을참조하고, 수신 피연산자 스택에 Type을 올바로 푸시하여 송신 유형 상태를 산출할 수 있는 경우 피연산자 CP가 있는 ldc 명령은 유형 안정적입니다.

instructionIsTypeSafe(ldc(CP), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- functor(CP, Tag, _), member([Tag, Type], [[int, int], [float, float], [string, class(’java/lang/String’)]]), validTypeTransition(Environment, [], Type, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). ldc_w: 동일한 ldc 명령이 유형 안정적인 경우 ldc_w 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(ldc_w(CP), ldc(CP)) ldc2_w: CP가 유형 Tag(여기서 Tag는 long이나 double 중 하나)의 엔티티를 나타내는 상수 풀 항목을 참조하고, 수신 피연산자 스택에 Type을 올바로 푸시하여 송신 유형 상태를 산출할 수 있는 경우 피연산자 CP가 있는 ldc2_w 명령은 유형 안정적입니다.

instructionIsTypeSafe(ldc2_w(CP), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- functor(CP, Tag, _), member(Tag, [long, double]), validTypeTransition(Environment, [], Tag, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 58페이지

<!-- page 59/68 -->

ldiv: 동일한 ladd 명령이 유형 안정적인 경우 ldiv 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(ldiv, ladd). lload: 피연산자 Index 및 유형 long이 있는 로드 명령이 유형 안정적이고 송신 유형 상태 NextStackFrame 을 산출하는 경우 피연산자 Index가 있는 lload 명령은 유형 안정적이며 송신 유형 상태 NextStackFrame을 산출합니다.

instructionIsTypeSafe(lload(Index), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- loadIsTypeSafe(Environment, Index, long, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). lload_<n>: 명령 lload_<n> (0≤n≤3인 경우)은 동일한 lload 명령이 유형 안정적인 경우 유형 안정적입니다.

instructionHasEquivalentTypeRule(lload_0, lload(0)). instructionHasEquivalentTypeRule(lload_1, lload(1)). instructionHasEquivalentTypeRule(lload_2, lload(2)). instructionHasEquivalentTypeRule(lload_3, lload(3)). lmul: 동일한 ladd 명령이 유형 안정적인 경우 lmul 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(lmul, ladd). lneg: 수신 피연산자 스택에 일치하는 long 유형이 있는 경우 lneg 명령은 유형 안정적입니다. lneg 명령은 유형 상태를 바꾸지 않습니다.

instructionIsTypeSafe(lneg, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [long], long, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 59페이지

<!-- page 60/68 -->

lookupswitch: 키가 정렬되어 있고 수신 피연산자 스택에서 int를 올바로 제거하여 새 유형 상태 BranchStackFrame을 산출할 수 있으며 모든 명령 대상이 BranchStackFrame을 수신 유형 상태로가정하는 유효한 분기 대상인 경우 lookupswitch 명령은 유형 안정적입니다.

instructionIsTypeSafe(lookupswitch(Targets, Keys), Environment, _, StackFrame, afterGoto, ExceptionStackFrame) :- sort(Keys, Keys), canPop(StackFrame, [int], BranchStackFrame), checklist(targetIsTypeSafe(Environment, BranchStackFrame), Targets), exceptionStackFrame(StackFrame, ExceptionStackFrame). lor: 동일한 ladd 명령이 유형 안정적인 경우 lor 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(lor, ladd). lrem: 동일한 ladd 명령이 유형 안정적인 경우 lrem 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(lrem, ladd). lreturn: 포함 메소드에 long의 선언된 반환 유형이 있고, 수신 피연산자 스택에서 일치하는 long 유형을 올바로 제거할 수 있는 경우 lreturn 명령은 유형 안정적입니다.

instructionIsTypeSafe(lreturn, Environment, _Offset, StackFrame, afterGoto, ExceptionStackFrame) :- thisMethodReturnType(Environment, long), canPop(StackFrame, [long], _PoppedStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). lshl: 수신 피연산자 스택에 있는 유형 int와 long을 유형 long으로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 lshl 명령은 유형 안정적입니다.

instructionIsTypeSafe(lshl, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int, long], long, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 60페이지

<!-- page 61/68 -->

lshr: 동일한 lshl 명령이 유형 안정적인 경우 lshr 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(lshr, lshl). lstore: 피연산자 Index와 유형 long이 있는 저장 명령이 유형 안정적이고 송신 유형 상태 NextStackFrame을산출하는 경우 피연산자 Index가 있는 lstore 명령은 유형 안정적이며 송신 유형 상태 NextStackFrame을 산출합니다.

instructionIsTypeSafe(lstore(Index), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- storeIsTypeSafe(Environment, Index, long, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). lstore_<n>: 명령 lstore_<n> (0≤n≤3인 경우)은 동일한 lstore 명령이 유형 안정적인 경우 유형 안정적입니다.

instructionHasEquivalentTypeRule(lstore_0, lstore(0)). instructionHasEquivalentTypeRule(lstore_1, lstore(1)). instructionHasEquivalentTypeRule(lstore_2, lstore(2)). instructionHasEquivalentTypeRule(lstore_3, lstore(3)). lsub: 동일한 ladd 명령이 유형 안정적인 경우 lsub 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(lsub, ladd). lxor: 동일한 ladd 명령이 유형 안정적인 경우 lxor 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(lxor, ladd). lushr: 동일한 lshl 명령이 유형 안정적인 경우 lushr 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(lushr, lshl). 61페이지

<!-- page 62/68 -->

monitorenter: 일치하는 reference 유형을 수신 피연산자 스택에서 올바로 제거하여 송신 유형 상태를 산출할 수있는 경우 monitorenter 명령은 유형 안정적입니다.

instructionIsTypeSafe(monitorenter, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [reference], NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). monitorexit: 동일한 monitorenter 명령이 유형 안정적인 경우 monitorexit 명령은 유형 안정적입니다.

instructionHasEquivalentTypeRule(monitorexit, monitorenter). multinewarray: CP가 차원이 Dim 이상(Dim이 양수)인 배열 유형을 나타내는 상수 풀 항목을 참조하고 수신 피연산자스택에 있는 Dim int 유형을 CP가 나타내는 유형으로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는경우 피연산자 CP와 Dim이 있는 multinewarray 명령은 유형 안정적입니다.

instructionIsTypeSafe(multianewarray(CP, Dim), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- CP = arrayOf(_), classDimension(CP, Dimension), Dimension >= Dim, Dim > 0, /* Make a list of Dim ints */ findall(int, between(1, Dim, _), IntList), validTypeTransition(Environment, IntList, CP, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 구성 요소 유형이 또한 배열 유형인 배열 유형의 차원은 구성 요소 유형의 차원보다 1 이상 큽니다.

classDimension(arrayOf(X), Dimension) :- classDimension(X, Dimension1), Dimension is Dimension1 + 1. classDimension(_, Dimension) :- Dimension = 0. 62페이지

<!-- page 63/68 -->

new: CP가 클래스 유형을 나타내는 상수 풀 항목을 참조하고 유형 uninitialized(Offset)가 수신피연산자 스택에 표시되지 않으며 uninitialized(Offset)를 수신 피연산자 스택에 올바로 푸시할 수 있고 수신 로컬 변수에 있는 top으로 uninitialized(Offset)를 바꾸어 송신 유형 상태를산출할 수 있는 경우 오프셋 Offset에 피연산자 CP가 있는 new 명령은 유형 안정적입니다.

instructionIsTypeSafe(new(CP), Environment, Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- StackFrame = frame(Locals, OperandStack, Flags), CP = class(_), NewItem = uninitialized(Offset), notMember(NewItem, OperandStack), substitute(NewItem, top, Locals, NewLocals), validTypeTransition(Environment, [], NewItem, frame(NewLocals, OperandStack, Flags), NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). newarray: TypeCode가 프리미티브 유형 ElementType과 일치하고 수신 피연산자 스택에 있는 유형 int를 ElementType의 유형 배열로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우 피연산자 TypeCode가 있는 newarray 명령은 유형 안정적입니다.

instructionIsTypeSafe(newarray(TypeCode), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- primitiveArrayInfo(TypeCode, _TypeChar, ElementType, _VerifierType), validTypeTransition(Environment, [int], arrayOf(ElementType), StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 유형 코드와 프리미티브 유형 사이의 일치는 다음 술어가 지정합니다.

primitiveArrayInfo(4, 0'Z, boolean, int). primitiveArrayInfo(5, 0'C, char, int). primitiveArrayInfo(6, 0'F, float, float). primitiveArrayInfo(7, 0'D, double, double). primitiveArrayInfo(8, 0'B, byte, int). primitiveArrayInfo(9, 0'S, short, int). primitiveArrayInfo(10, 0'I, int, int). primitiveArrayInfo(11, 0'J, long, long). 63페이지

<!-- page 64/68 -->

nop: nop 명령은 항상 유형 안정적입니다. nop 명령은 유형 상태에 영향을 미치지 않습니다.

instructionIsTypeSafe(nop, _Environment, _Offset, StackFrame, StackFrame, ExceptionStackFrame) :- exceptionStackFrame(StackFrame, ExceptionStackFrame). pop: 수신 피연산자 스택에서 범주 1 유형을 올바로 제거하여 송신 유형 상태를 산출할 수 있는 경우 pop 명령은 유형 안정적입니다.

instructionIsTypeSafe(pop, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- StackFrame = frame(Locals, [Type | Rest], Flags), Type \= top, sizeOf(Type, 1), NextStackFrame = frame(Locals, Rest, Flags), exceptionStackFrame(StackFrame, ExceptionStackFrame). pop2: pop2 명령이 pop2 명령의 유형 안정적인 형식인 경우 유형 안정적입니다.

instructionIsTypeSafe(pop2, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- StackFrame = frame(Locals, InputOperandStack, Flags), pop2SomeFormIsTypeSafe(InputOperandStack, OutputOperandStack), NextStackFrame = frame(Locals, OutputOperandStack, Flags), exceptionStackFrame(StackFrame, ExceptionStackFrame). pop2 명령이 유형 안정적인 형식 1 pop2 명령이거나 유형 안정적인 형식 2 pop2 명령인 경우 pop2 명령은 유형 안정적인 형식입니다.

pop2SomeFormIsTypeSafe(InputOperandStack, OutputOperandStack) :- pop2Form1IsTypeSafe(InputOperandStack, OutputOperandStack). pop2SomeFormIsTypeSafe(InputOperandStack, OutputOperandStack) :- pop2Form2IsTypeSafe(InputOperandStack, OutputOperandStack). 64페이지

<!-- page 65/68 -->

수신 피연산자 스택에서 크기가 1인 두 개의 유형을 올바로 제거하여 송신 유형 상태를 산출할 수 있는경우 pop2 명령은 유형 안정적인 형식 1 pop2 명령입니다.

pop2Form1IsTypeSafe([Type1, Type2 | Rest], Rest) :- sizeOf(Type1, 1), sizeOf(Type2, 1). 수신 피연산자 스택에서 크기가 2인 유형을 올바로 제거하여 송신 유형 상태를 산출할 수 있는 경우 pop2 명령은 유형 안정적인 형식 2 pop2 명령입니다.

pop2Form2IsTypeSafe([top, Type | Rest], Rest) :- sizeOf(Type, 2). putfield: 선언된 유형이 클래스 FieldClass에 선언되어 있는 FieldType인 필드를 나타내는 상수 풀 항목을 CP 가 참조하고 일치하는 FieldType 및 FieldClass 유형을 수신 피연산자 스택에서 올바로 제거하여 송신유형 상태를 산출할 수 있는 경우 피연산자 CP가 있는 putfield 명령은 유형 안정적입니다.

instructionIsTypeSafe(putfield(CP), _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- CP = field(FieldClass, FieldName, FieldSignature), parseFieldSignature(FieldSignature, FieldType), passesProtectedCheck(Environment, FieldClass, FieldName, FieldSignature, StackFrame), canPop(StackFrame, [FieldType, class(FieldClass)], NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). putstatic: 선언된 유형이 클래스 FieldType인 필드를 나타내는 상수 풀 항목을 CP가 참조하고 일치하는 FieldType 유형을 수신 피연산자 스택에서 올바로 제거하여 송신 유형 상태를 산출할 수 있는 경우피연산자 CP가 있는 putstatic 명령은 유형 안정적입니다.

instructionIsTypeSafe(putstatic(CP), _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- CP = field(_FieldClass, _FieldName, FieldSignature), parseFieldSignature(FieldSignature, FieldType), canPop(StackFrame, [FieldType], NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 65페이지

<!-- page 66/68 -->

return: 포함 메소드가 void 반환 유형을 선언하고 다음 중 하나인 경우 return 명령은 유형 안정적입니다.

• 포함 메소드가 <init> 메소드가 아니거나 • 명령이 발생한 시점에 this 명령이 이미 완전히 초기화되었습니다.

instructionIsTypeSafe(return, Environment, _Offset, StackFrame, afterGoto, ExceptionStackFrame) :- thisMethodReturnType(Environment, void), StackFrame = frame(_Locals, _OperandStack, Flags), notMember(flagThisUninit, Flags), exceptionStackFrame(StackFrame, ExceptionStackFrame). saload: 일치하는 int 유형 및 수신 피연산자 스택에 있는 short의 배열을 int와 올바로 바꾸어 송신 유형상태를 산출할 수 있는 경우에는 saload 명령은 유형 안정적입니다.

instructionIsTypeSafe(saload, Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [int, arrayOf(short)], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). sastore: 일치하는 int 유형, int 및 short의 배열을 수신 피연산자 스택에서 올바로 제거하여 송신 유형상태를 산출할 수 있는 경우에는 sastore 명령은 유형 안정적입니다.

instructionIsTypeSafe(sastore, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- canPop(StackFrame, [int, int, arrayOf(short)], NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). sipush: 유형 int를 수신 피연산자 스택에 올바로 푸시하여 송신 유형 상태를 산출할 수 있는 경우에는 sipush 명령은 유형 안정적입니다.

instructionIsTypeSafe(sipush(_Value), Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- validTypeTransition(Environment, [], int, StackFrame, NextStackFrame), exceptionStackFrame(StackFrame, ExceptionStackFrame). 66페이지

<!-- page 67/68 -->

swap: 수신 피연산자 스택에 있는 두 개의 범주 1 유형 Type1과 Type2를 유형 Type2와 Type1로 올바로 바꾸어 송신 유형 상태를 산출할 수 있는 경우에는 swap 명령은 유형 안정적입니다.

instructionIsTypeSafe(swap, _Environment, _Offset, StackFrame, NextStackFrame, ExceptionStackFrame) :- StackFrame = frame(_Locals, [Type1, Type2 | Rest], _Flags), sizeOf(Type1, 1), sizeOf(Type2, 1), NextStackFrame = frame(_Locals, [Type2, Type1 | Rest], _Flags), exceptionStackFrame(StackFrame, ExceptionStackFrame). tableswitch: 키가 정렬되어 있고 수신 피연산자 스택에서 int를 올바로 제거하여 새 유형 상태 BranchStackFrame을 산출할 수 있으며, 모든 명령 대상이 BranchStackFrame을 수신 유형 상태로가정하는 유효한 분기 대상인 경우 tableswitch 명령은 유형 안정적입니다.

instructionIsTypeSafe(tableswitch(Targets, Keys), Environment, _Offset, StackFrame, afterGoto, ExceptionStackFrame) :- sort(Keys, Keys), canPop(StackFrame, [int], BranchStackFrame), checklist(targetIsTypeSafe(Environment, BranchStackFrame), Targets), exceptionStackFrame(StackFrame, ExceptionStackFrame). wide: wide 명령은 넓혔던 명령과 같은 규칙을 따릅니다.

instructionHasEquivalentTypeRule(wide(WidenedInstruction), WidenedInstruction). 피연산자 스택이 비어 있다는 점만 제외하면 명령이 갑자기 완료된 다음의 유형 상태는 수신 유형 상태와 같습니다.

exceptionStackFrame(StackFrame, ExceptionStackFrame) :- StackFrame = frame(Locals, _OperandStack, Flags), ExceptionStackFrame = frame(Locals, [], Flags). 67페이지

<!-- page 68/68 -->

이 규격에 있는 대부분의 유형 규칙은 유효한 유형 전이의 개념을 따릅니다.

수신 유형 상태의 피연산자 스택에서 예상 유형 목록을 제거한 다음 예상 결과 유형으로 바꾸어 새로유효한 유형 상태를 만들 수 있으면 유형 전이는 유효합니다. 특히 새 유형 상태의 피연산자 스택의크기는 선언된 최대 크기를 초과해선 안 됩니다.

validTypeTransition(Environment, ExpectedTypesOnStack, ResultType, frame(Locals, InputOperandStack, Flags), frame(Locals, NextOperandStack, Flags)) :- popMatchingList(InputOperandStack, ExpectedTypesOnStack, InterimOperandStack), pushOperandStack(InterimOperandStack, ResultType, NextOperandStack), operandStackHasLegalLength(Environment, NextOperandStack). 유형 상태에서 피연산자 스택의 I번째 요소에 액세스합니다.

nth1OperandStackIs(I, frame(_Locals, OperandStack, _Flags), Element) :- nth1(I, OperandStack, Element).

## 4. 참조 자료

William F. Clocksin and Christopher S. Mellish. Programming in Prolog, Fourth Edition. Springer-Verlag, 1994. Leon Sterling and Ehud Shapiro. The Art of Prolog, Second Edition. MIT Press, 1994. Timothy Lindholm and Frank Yellin. The JavaTM Virtual Machine Specification, Second Edition. Addison Wesley, 1999. Sheng Liang. The KVM Verifier. Unpublished internal Sun document. Frank Yellin. “Low Level Security in Java.” World Wide Web Journal, Volume I, Issue 1, Winter 1996. http://www.w3journal.com/1/f.197/paper/197.html에서 온라인으로 구할 수 있습니다.

68페이지
