# Class ListComponent

`package org.kwis.msp.lwc`

```text
java.lang.Object
  |
  +--org.kwis.msp.lwc.Component
        |
        +--org.kwis.msp.lwc.ContainerComponent
              |
              +--org.kwis.msp.lwc.FormComponent
                    |
                    +--org.kwis.msp.lwc.ListComponent
```

## 설명

**extends FormComponent:**

`ListComponent`는 ``FormComponent``를 상속하여
 구현된 클래스입니다.
 이 다른 `ContainerComponent`와는 달리
 ``ListItemComponent``만을 추가할 수 있고, 그 순서에 따라 각 아이템들이
 화면에 출력됩니다.

`ListItemComponent`는 3가지 타입이 있습니다. *
 현재 포커스를 받고 있는 아이템이 선택된 상태와 같게 되는 타입인
 ``SELECT_IMPLICIT``, 여러 아이템을 선택할 수 있는 ``SELECT_MULTIPLE``,
 한 아이템만 선택할 수 있는 ``SELECT_EXCLUSIVE``입니다.
 이때 `SELECT_MULTIPLE,SELECT_EXCLUSIVE`의 경우에는 포커스를 가지는
 아이템과 선택된 아이템이 반드시 일치하지는 않습니다.

추가된 `ListItemComponent`를 `SELECT`키 입력에 의해서
 선택하거나 번호에 해당 위치에 대한 숫자키 입력을 받은경우
 ``ActionListener``를 등록하여 선택 액션에 대한 감지를 할 수 있고, 방향키 입력에
 의해 선택된 아이템이 변경된 경우 이것을 알 수 있도록 ``ChangeListener``를
 등록 할 수 있는 기능을 제공하고 있습니다.

기본적으로 `ListComponent`를 사용하면 번호 이미지가 출력됩니다.
 번호 이미지에 대한 제어는 ``controlNumber(boolean showImage)``에서 담당
 하고있으며, `true`값을 지정한 경우 번호이미지가 화면에 출력되고,
 `false`값을 지정한 경우 번호이미지가 출력되지 않습니다.

**See Also:**
- ``ListItemComponent``, 
``ActionListener``, 
``ChangeListener``

## 필드 요약

- `static int SELECT_EXCLUSIVE` — 단 하나의 아이템만 선택할 수 있는 타입.
- `static int SELECT_IMPLICIT` — ListComponent 에 포커스를 가지는 경우에 현재 포커스 된 아이템과 선택된 아이템이 동일한 타입.
- `static int SELECT_MULTIPLE` — 여러개의 아이템을 선택할 수 있는 타입.

## 생성자 요약

- ListComponent (int type) 아이템을 포함하지 않은 사이즈가 '0'인 ListComponent의 인스턴스를 주어진 타입으로
 생성합니다.

## 메서드 요약

- `int addComponent ( Component cmp)` — 컴포넌트를 하나 추가합니다.맨 위에 자식 컴포넌트를 추가합니다.
- `void addComponent (int index, Component cmp)` — index 위치에 컴포넌트를 하나 추가합니다.
- `int append ( String str, Image img)` — ListComponent 에 주어진 이미지 데이타와 문자데이타로 `ListItemComponent` 를 생성하여 추가합니다.
- `void controlNumber (boolean showImage)` — 번호키 컨트롤 여부를 지정합니다.
- `Image getImage (int index)` — 주어진 위치에
