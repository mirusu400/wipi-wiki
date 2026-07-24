---
title: "3.1.4. 고수준 사용자 인터페이스"
---

Interface ActionListener public interface ActionListener 어떤 액션이 발생하면 불리는 인터페이스이다. 버튼과 같이 사용자가 누르는 경우에 발생하는 이벤트를 처리하는 Listener이다. 메쏘드 상세 설명

#### action

public void action(Component cmp, Object obj) 버튼이나 리스트에서 action이 발생하면 불린다.

**매개 변수**

- `cmp` - action이 발생한 컴포넌트
- `obj` - setActionListener시에 넣은 Object 인수
- `Interface` - ChangeListener
- `public` - interface ChangeListener
- `Selection이` - 변경되면 불리는 인터페이스. 리스트나 초이스그룹 등에서 선택상태가 변경되는 경우에 발생하는 이벤트를 처리하는 listener이다. 메쏘드 상세 설명 changed
- `public` - void changed(Component cmp, Object obj)
- `ChangeListener를` - 설정한 Component에서 CHANGE 이벤트가 발생한 경우 불리게 된다. CheckboxComponent또는 ListComponent 등의 상태가 변경되게 되면 등록된
- `Listener의` - changed함수가 불려 진다

**매개 변수**

- `cmp` - 이벤트가 발생된 Component
- `obj` - setChangeListener에서 설정한 Object(확장 파라메터)

**참고 항목**

CheckboxComponent.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object), CheckboxGroup.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object), ListComponent.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object), ListComponent.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object), ProgressComponent.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object) Interface CommandListener public interface CommandListener 커맨드의 선택/변경을 알려주는 인터페이스이다. 커맨드를 내용을 선택하거나, 커맨드의 포커스를 변경하였을 경우 알려주는 인터페이스이다. 필드 상세 설명

#### FOCUS_CHANGE

public static final int FOCUS_CHANGE 커맨드의 포커스가 변경된 경우의 상수이다.

#### SELECT

public static final int SELECT 커맨드를 선택한 경우의 상수이다. 메쏘드 상세 설명

#### commandAction

public void commandAction(Command c, int type, Object obj) 커맨드의 내용이 선택되었거나 커맨드의 포커스가 변경되었을 경우에 이 함수를 호출하여 준다.

**매개 변수**

- `c` - 선택된 커맨드나 포커스를 받은 커맨드
- `type` - 커맨드 선택 시 SELECT, 커맨드 포커스 변경 시 FOCUS_CHANGE
- `obj` - setCommandListener( CommandListener c, Object obj )로 전달된 obj 객체.
- `Interface` - EventListener
- `public` - interface EventListener
- `Component의` - 이벤트 발생을 알려주는 인터페이스이다. 컴포넌트에 발생되는 key, show, focus, pointer이벤트 발생시 이를 알려주는 인터페이스이다. 메쏘드 상세 설명 eventNotify
- `public` - boolean eventNotify(int type, int arg1, int arg2, int arg3, Object obj) 컴포넌트에서 Key, Show, Focus, Pointer이벤트가 발생한 경우 이 함수를 호출하여 준다.

**매개 변수**

- `type` - 발생된 이벤트의 종류를 나타낸다(Component.KEY_NOTIFY, Component.SHOW_NOTIFY, Component.FOCUS_NOTIFY, Component.POINTER_NOTIFY)
- `arg1` - type의 값에 따라 다양하게 사용
- `arg2` - type의 값에 따라 다양하게 사용
- `arg3` - type의 값에 따라 다양하게 사용
- `obj` - setEventListner에서 설정한 Object
- `Interface` - GrabKeyListener
- `public` - interface GrabKeyListener
- `Key` - Grab이 설정된 경우 그랩된 키 이벤트 발생을 알려주는 인터페이스이다. 메쏘드 상세 설명 grabKeyNotify
- `public` - boolean grabKeyNotify(int type, int chr, Object obj) 컴포넌트에서 Key, Show, Focus, Pointer이벤트가 발생한 경우 이 함수를 호출하여 준다.

**매개 변수**

- `type` - 발생된 키 이벤트의 종류를 나타낸다 (EventQueue.KEY_RELEASED,EventQueue.KEY_RELEASED, EventQueue.KEY_REPEATED, EventQueue.KEY_TYPED)
- `chr` - 발생된 키 값
- `obj` - setEventListner에서 설정한 Object
- `Class` - AnnunciatorComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.ContainerComponent | +--org.kwis.msp.lwc.ShellComponent | +--org.kwis.msp.lwc.AnnunciatorComponent
- `public` - class AnnunciatorComponent extends ShellComponent 사용자에게 전파 세기와 배터리 사용 용량을 화면에 보여주는 클래스이다. 이 클래스는 능동적으로 각종 내부 값이 바뀌면 화면의 내용도 바뀐다.
- `Fields` - inherited from class org.kwis.msp.lwc.ShellComponent cd, cmpCommand, cmpTitle, cmpWork, RESIZE_MASK
- `Fields` - inherited from class org.kwis.msp.lwc.ContainerComponent cmpFocus, cmps, insetBottom, insetLeft, insetRight, insetTop, ncomp, offsetX, offsetY, useFrame
- `Fields` - inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y
- `Methods` - inherited from class org.kwis.msp.lwc.ShellComponent addComponent, configure, getCard, getCommand, getNextTraversalComponent, getPrevTraversalComponent, getTitle, getWorkComponent, getX, getY, grabKey, isShown, keyNotify, processEvent, removeAllComponents, repaint, serviceRepaints, setCommand, setGrabKeyListener, setTitle, setTitle, setWorkComponent, showNotify, ungrabKey
- `Methods` - inherited from class org.kwis.msp.lwc.ContainerComponent getComponent, getIndexOf, getNumberOfComponent, paintFrame, removeComponent, repaint, scrollTo, setComponent, useFrame, validate
- `Methods` - inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, focusNotify, getBackground, getForeground, getHeight, getPreferredHeight, getPreferredHeight, getPreferredWidth, getWidth, getXOnScreen, getYOnScreen, hasFocus, invalidate, isValid, paintContent, pointerNotify, setBackground, setEventListener, setFocus, setForeground, toString
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명 AnnunciatorComponent
- `public` - AnnunciatorComponent(boolean bTrans) 어넌시에이터 컴포넌트를 생성한다. bTrans를 false로 세팅하면 화면 상단의 일정 부분의 내용에 어넌시에이터 내용이 출력되며 이 부분은 응용 프로그램이 사용할 수 없다. 그러나 true로 세팅하면 화면 윗부분을 응용 프로그램이 사용이 가능하며 응용 프로그램이 그린 내용 위에 어넌시에이터 내용이 출력된다.

**매개 변수**

- `bTrans` - 어넌시에이터가 화면에 투명하게 출력될지 아니면 투명하지 않 게 출력될지 여부 메쏘드 상세 설명 addComponent
- `public` - void addComponent(int idx, Component cmp) 자식 컴포넌트를 하나 추가한다. 지정한 위치에 cmp가 가리키는 컴포넌트를 추가한다. 이 함수는 AnnunciatorComponent에서는 제공 하지 않는다. 그러므로 이 함수를 부르게 되면 IllegalStateException이 발생 된다. Overrides
- `addComponent` - in class ShellComponent

**매개 변수**

- `index` - 넣을 위치
- `cmp` - 넣을 컴포넌트 Throws
- `IllegalStateException` - 항상 발행 removeComponent
- `public` - void removeComponent(Component cmp) 지정된 컴포넌트를 삭제한다. 이 함수는 AnnunciatorComponent에서는 제공 하지 않는다. 그러므로 이 함수를 부르게 되면 항상 IllegalStateException이 발생 된다. Overrides
- `removeComponent` - in class ShellComponent

**매개 변수**

- `Cmp` - 삭제할 컴포넌트 Throws
- `IllegalStateException` - 항상 발행 layout
- `public` - void layout() 하위 컴포넌트의 크기와 위치를 결정한다. Overrides
- `layout` - in class ShellComponent show
- `public` - void show() 컴포넌트를 화면상에 보여준다. 컴포넌트를 화면상에 보여주기 전에 컴포넌트의 위치와 크기를 validate함수를 통해서 계산한다. 이 컴포넌트는 Display에 직접 추가 되므로 다른 컴포넌트를 Show하기 전에 가장 먼저 Show되어야 한다. Overrides
- `show` - in class ShellComponent hide
- `public` - void hide() 컴포넌트를 감춘다. 이 함수는 AnnunciatorComponent에서 제공되지 않는다. 즉 한번 AnnunciatorComponent가 show되면 hide될 수 없으며, 이 함수를 부르게 되면 항상 IllegalStateException이 발생한다. Overrides
- `hide` - in class ShellComponent Throws
- `IllegalStateException` - 항상 발행 paint
- `protected` - void paint(Graphics g) Overrides
- `paint` - in class ContainerComponent 그래픽스 g를 가지고 컨테이너 컴포넌트를 그린다. 이때 컨테이너 컴포넌트는 자식 컴포넌트의 paintContent함수를 이용하여 자식 컴포넌트 까지 그려준다.

**매개 변수**

- `g` - 컴포넌트를 그릴 그래픽스 개체
- `Class` - ButtonComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.ButtonComponent
- `public` - class ButtonComponent extends Component 버튼 컴포넌트. "select"키가 눌렸다 떼어 졌을 때 자신에게 등록된 ActionListener를 호출한다. 버튼은 문자열과 이미지 두개로 구성된다.
- `Fields` - inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y
- `Methods` - inherited from class org.kwis.msp.lwc.Component canHandleInput, configure, focusNotify, getBackground, getCard, getForeground, getHeight, getPreferredHeight, getPreferredHeight, getPreferredWidth, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString, validate
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명 ButtonComponent
- `public` - ButtonComponent() 버튼을 생성한다. ButtonComponent
- `public` - ButtonComponent(String str, Image img) 지정된 Image와 문자열을 버튼을 생성한다. 버튼을 생성시키며, 이때 이미지와 문자열을 지정한다. img와 str 둘 다 null이 될 수도 있다.

**매개 변수**

- `str` - 버튼의 문자열
- `img` - 버튼의 이미지 메쏘드 상세 설명 setFont
- `public` - void setFont(Font ft) 버튼의 폰트를 설정한다.

**매개 변수**

- `ft` - 지정할 폰트 getFont
- `public` - Font getFont() 폰트를 돌려준다. 내부에 지정된 폰트를 돌려준다.

**반환 값**

지정된 폰트 setActionListener public void setActionListener(ActionListener l, Object obj) ActionListener를 등록한다. 버튼이 눌리면 해당 컴포넌트와 obj를 인수로 ActionListener의 action을 불러준다. 만일 기존에 등록된 ActionListener는 새로운 ActionListener로 대체된다.

**매개 변수**

- `l` - ActionListener
- `obj` - 불려질 때 넘겨질 인수

**참고 항목**

ActionListener.action(org.kwis.msp.lwc.Component, java.lang.Object)

#### keyNotify

public boolean keyNotify(int type, int ch) 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력 값이 된다. Overrides keyNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. setString public void setString(String str) 버튼의 문자열을 지정한다.

**매개 변수**

- `str` - 지정할 문자열 getString
- `public` - String getString() 현재 버튼의 문자열을 돌려준다.

**반환 값**

현재 버튼의 문자열 getImage public Image getImage() 현재 버튼의 이미지를 돌려준다.

**반환 값**

버튼의 이미지 setImage public void setImage(Image img) 버튼의 이미지를 지정한다.

**매개 변수**

- `img` - 지정할 이미지. img가 null인 경우 기존 이미지를 삭제한다. paintContent
- `public` - void paintContent(Graphics g) 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides
- `paintContent` - in class Component
- `Following` - copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics

#### layout

protected void layout() 하위 컴포넌트의 크기와 위치를 결정한다. Overrides layout in class Component

#### calcPreferredSize

protected void calcPreferredSize(int w) 컴포넌트의 적절한 크기를 계산한다. Overrides calcPreferredSize in class Component Class CheckboxComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.LabelComponent | +--org.kwis.msp.lwc.CheckboxComponent public class CheckboxComponent extends LabelComponent CheckboxComponent는 개별 선택 가능한 체크버튼과 라디오버튼을 만들기 위한 클래스 이다. CheckboxGroup의 지정이 없이 생성되는 CheckboxComponent 의 경우는 독립적인 체크박스로 동작하며, CheckboxGroup이 지정되는 경우 같은 CheckboxGroup으로 묶여진 CheckboxComponent들은 엮여진 라디오버튼으로 동작하게 된다. 동일한 CheckboxGroup으로 묶여진 CheckBox 들은 초기 값으로 선택되지 않은 상태로 되며, 그 중 맨 처음에 추가 된 것만 선택된 상태로 초기화 된다. 이 값을 바꾸기 위해서는 setState를 사용한다. Fields inherited from class org.kwis.msp.lwc.LabelComponent layout, m_ft, m_image, m_str Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.LabelComponent calcPreferredSize, getFont, getImage, getLabel, invalidate, setFont, setImage, setLabel, setLayout Methods inherited from class org.kwis.msp.lwc.Component canHandleInput, configure, focusNotify, getBackground, getCard, getForeground, getHeight, getPreferredHeight, getPreferredHeight, getPreferredWidth, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, isShown, isValid, layout, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString, validate Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명

#### CheckboxComponent

public CheckboxComponent(String str, Image img) 새로운 CheckboxComponent를 생성한다. 주어진 문자열과 이미지를 가지게 된다. CheckboxComponent의 초기값은 false가 된다.

**매개 변수**

- `str` - 체크박스의 문자열.
- `img` - 체크박스의 이미지.

**참고 항목**

CheckboxComponent(String, Image, CheckboxGroup) CheckboxComponent(String, Image, boolean) CheckboxComponent(String, Image, CheckboxGroup, boolean) CheckboxGroup

#### CheckboxComponent

public CheckboxComponent(String str, Image img, CheckboxGroup cb) 새로운 CheckboxComponent를 생성한다. 주어진 문자열과 이미지를 가지며 CheckboxGroup에 의해 그룹핑이 된다. CheckboxGroup이 null인 경우에는 그룹핑 되지 않는 독립 형 Checkbox가 된다.

**참고 항목**

CheckboxComponent(String, Image) CheckboxComponent(String, Image, boolean) CheckboxComponent(String, Image, CheckboxGroup, boolean) CheckboxGroup

#### CheckboxComponent

public CheckboxComponent(String str, Image img, boolean bSet) 새로운 CheckboxComponent를 생성한다. 주어진 문자열과 이미지를 가지며 bSet에 의해 초기 상태가 결정된다.

**참고 항목**

CheckboxComponent(String, Image) CheckboxComponent(String, Image, CheckboxGroup), CheckboxComponent(String, Image, CheckboxGroup, boolean) setState(boolean) CheckboxGroup 메쏘드 상세 설명

#### setState

public void setState(boolean bState) CheckboxComponent의 선택상태를 변경한다. 그룹핑 된 CheckboxComponent인 경우에는 현재 선택상태의 관리를 CheckboxGroup에서 하게 되므로 setState에 false값을 지정하면 CheckboxGroup에서 그룹핑 된 다른 CheckboxComponent 중 어느 것이 선택되어야 하는지 알 수 없으므로 이 입력을 무시하게 된다. 따라서 아무런 동작도 하지 않는다. 이 함수에 의해 선택상태가 변경되는 경우 ChangeListener가 불려진다.

**참고 항목**

getState()

#### getState

public boolean getState() CheckboxComponent의 선택상태를 구한다.

**참고 항목**

setState(boolean)

#### paintContent

public void paintContent(Graphics g) 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides paintContent in class LabelComponent Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics

#### keyNotify

public boolean keyNotify(int type, int key) 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력 값이 된다. Overrides keyNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. setChangeListener public void setChangeListener(ChangeListener listener, Object obj) CheckboxComponent에 ChangeListener를 등록 한다. CheckboxComponent의 선택상태가 변경되게 되면 등록된 Listener의 changed함수가 불려 진다

**매개 변수**

- `listener` - 불려진 Listener
- `obj` - Listener가 불려질 때 넘겨 받을 Object (확장 파라메터)

**참고 항목**

CheckboxGroup.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object) Class CheckboxGroup java.lang.Object | +--org.kwis.msp.lwc.CheckboxGroup public class CheckboxGroup extends Object CheckboxGroup은 여러 개의 CheckboxComponent들을 엮어 그룹 된 라디오버튼처럼 움직이게 한다. 하나의 CheckboxGroup으로 등록된 CheckBoxComponent들은 동시에 여러 개가 ON상태가 될 수 없고 동시에는 하나의 CheckboxComponent만 ON될 수 있다. 그러므로 하나의 Checkbox가 ON 되면 다른 모든 Group으로 묵인 Checkbox들은 OFF 가 된다. 초기 값으로는 맨 처음에 등록된 CheckboxComponent가 ON이 된다. Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 생성자 상세 설명

#### CheckboxGroup

public CheckboxGroup() 새로운 CheckboxGroup을 생성한다.

**참고 항목**

CheckboxComponent 메쏘드 상세 설명

#### select

public void select(CheckboxComponent cb) CheckboxGroup으로 묶여 있는 CheckboxComponent중에 주어진 컴포넌트를 ON상태로 한다. 같은 그룹으로 묶여진 다른 체크박스들은 모두 OFF상태가 된다.

**매개 변수**

- `cb` - select할 CheckboxComponent.

**참고 항목**

getSelectedCheckbox()

#### getSelectedCheckbox

public CheckboxComponent getSelectedCheckbox() 이 CheckboxGroup에 등록된 Checkbox중 현재 ON 상태인 CheckboxComponent를 구한다

**반환 값**

현재 ON상태인 CheckboxComponent

**참고 항목**

select(org.kwis.msp.lwc.CheckboxComponent)

#### setChangeListener

public void setChangeListener(ChangeListener listener, Object obj) CheckboxGroup에 ChangeListener를 등록 한다. CheckboxGroup에 등록된 CheckboxComponent의 상태가 변경되게 되면 등록된 Listener의 changed함수가 불려 진다

**매개 변수**

- `listener` - 불려진 Listener
- `obj` - Listener가 불려질 때 넘겨 받을 Object (확장 파라메터)

**참고 항목**

CheckboxComponent#CheckboxComponent(String, Image, CheckboxGroup, boolean) CheckboxComponent.CheckboxComponent(String, Image, CheckboxGroup) CheckboxComponent.setChangeListener(org.kwis.msp.lwc.ChangeListener, java.lang.Object) Class ComboComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.ComboComponent public class ComboComponent extends Component ComboComponent는 팝업메뉴 기능을 제공하는 클래스이다. ComboComponent는 팝업 메뉴 항목 중 선택된 항목를 보여주는 영역과 팝업 메뉴의 리스트를 보여주는 영역으로 나뉘어 있다. 선택항목을 보여주는 화면에서 SELECT키 입력 시 팝업 메뉴 리스트가 보여지며 이 중 어떤 항목를 선택하면 팝업 메뉴 리스트는 화면에서 제거되고 새로운 선택 항목만이 보여지게 된다. ComboComponent에서는 선택항목의 변경을 감시할 수 있는 ChangeListener를 등록하여 사용할 수 있으며, 팝업메뉴에서 새로운 항목을 선택 시 ChangeListener의 changed 메소드를 호출하게 된다. 팝업 메뉴 리스트를 선택하지 않아도 ComboComponent가 사라질 경우 리스트도 함께 사라져야 한다. Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, configure, focusNotify, getBackground, getCard, getForeground, getHeight, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, layout, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString, validate Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명

#### ComboComponent

public ComboComponent() ComboComponent의 인스턴스를 생성한다. 메쏘드 상세 설명

#### append

public int append(String str) 주어진 문자데이타로 팝업메뉴의 새로운 항목을 생성하여 팝업메뉴 리스트의 맨 아래 위치에 추가한다.

**매개 변수**

- `str` - 추가될 문자열

**반환 값**

추가된 문자열의 인덱스 Throws IllegalArgumentException str이 null 일 경우 발생. insert public int insert(int index, String str) 주어진 index 위치에 주어진 문자데이타로 팝업메뉴의 새로운 항목을 생성하여 팝업메뉴 리스트에 삽입한다. 인덱스값이 '0'보다 작거나 ListItemComponent에 추가된 엘리먼트의 개수보다 큰 경우 IndexOutOfBoundsException이 발생한다.

**매개 변수**

- `index` - 삽입할 항목의 인덱스

**반환 값**

삽입된 인덱스값 Throws IndexOutOfBoundsException 인덱스 값이 잘못 지정된 경우

**참고 항목**

ListComponent.insert(int, java.lang.String, org.kwis.msp.lcdui.Image)

#### set

public void set(int index, String str) 주어진 index 위치에 주어진 문자데이타로 팝업메뉴 항목을 생성하여 새로 지정한다. 인덱스값이 '0'보다 작거나 ListItemComponent에 추가된 엘리먼트의 개수보다 큰 경우 IndexOutOfBoundsException이 발생한다.

**매개 변수**

- `index` - 대치할 항목의 인덱스
- `str` - 대치할 항목의 문자데이터 Throws
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우 delete
- `public` - void delete(int index) 팝업메뉴 리스트의 주어진 index 위치에 있는 항목을 삭제한다. 인덱스값이 '0'보다 작거나 ListItemComponent에 추가된 엘리먼트의 개수보다 큰 경우
- `IndexOutOfBoundsException이` - 발생한다.

**매개 변수**

- `index` - 삭제할 항목의 인덱스 Throws
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우 getString
- `public` - String getString() 현재 선택되어 있는 항목의 문자열을 구한다.

**반환 값**

선택된 항목의 문자열, 선택되지 않은 경우 null이 반환. getSize public int getSize() ComboComponent의 팝업메뉴 리스트 항목들의 개수를 구한다.

**반환 값**

가지고 있는 항목들의 개수 getSelectedIndex public int getSelectedIndex() 이하 메소스 설명은 component 클래스에서 복사되었음 팝업메뉴 리스트의 항목들 중 선택되어 있는 항목의 인덱스를 구한다

**반환 값**

선택되어있는 항목의 인덱스. 선택된것이 없는 경우 -1을 반환. getPreferredHeight public int getPreferredHeight() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. ContainerComponent에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 높이 getPreferredHeight public int getPreferredHeight(int w) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. 지정된 제한된 폭을 가질 경우의 컴포넌트의 높이를 돌려준다. 만일 LabelComponent 나 TextFieldComponent, TextAreaComponent와 같이 포맷팅이 가능한 컴포넌트인 경우에는 가변 폭을 가질 수가 있다. 가변 폭을 가지게 되면, 폭에 따라서 높이가 달라지게 된다. 이때 이 함수를 통해서 컴포넌트의 높이를 얻어 온다. 만일, w가 -1이 면 폭에 제한이 없는 것으로 계산된다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `w` - 가변 폭.

**반환 값**

컴포넌트의 높이. getPreferredWidth public int getPreferredWidth() 컴포넌트의 적절한 폭을 결정한다. Container에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredWidth in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 폭. paintContent public void paintContent(Graphics g) 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides paintContent in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics

#### keyNotify

protected boolean keyNotify(int type, int key) 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력 값이 된다. Overrides keyNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. setChangeListener public void setChangeListener(ChangeListener listener, Object obj) ComboComponent에서 팝업메뉴 리스트의 항목들 중 선택된 항목이 변경된 경우, 변경상태를 감시할 ChangeListener를 설정한다.

**매개 변수**

- `listener` - 구현된 ChangeListener, 이 값이 null인 경우 등록된
- `Listener가` - 취소된다.
- `obj` - 설정할 Object, 사용하지 않을 때는 null을 넣는다. 이
- `Object는` - Change이벤트가 발생되어 ChangeListener의
- `changed` - 함수가 불려질 때 인자로 넘겨진다. select
- `public` - void select(int index) 팝업메뉴 리스트에서 주어진 index의 항목을 선택한다.

**매개 변수**

- `index` - 선택할 항목의 인덱스 Throws
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우
- `Class` - Command java.lang.Object | +--org.kwis.msp.lwc.Command
- `public` - class Command extends Object 사용자가 내릴 수 있는 명령을 가리키는 클래스이다. 사용자가 UI컴포넌트 상에서 사용하고자 하는 커맨드를 정의한다. 커맨드는 문자열과 이미지로 표현하며
- `CommandBarComponent에` - 등록되어 사용한다. 이미지의 크기는 20x20pixel이어야 한다.

**참고 항목**

CommandBarComponent Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait 생성자 상세 설명

#### Command

public Command(String str, Object obj) 커맨드를 생성한다. 지정한 문자열을 가지는 커맨드를 생성한다. 이때 이미지는 null 이 된다. obj는 사용자가 임의로 특정 Object를 설정 가능하며 getExtObject함수를 이용하여 읽을 수 있다.

**매개 변수**

- `str` - 문자열
- `obj` - 확장Object Command
- `public` - Command(String str, Image img, Object obj) 커맨드를 생성한다. 지정한 문자열과 이미지를 가지는 커맨드를 생성한다. obj는 사용자가 임의로 특정 Object를 설정 가능하며 getExtObject함수를 이용하여 읽을 수 있다.

**매개 변수**

- `str` - 문자열
- `img` - 이미지
- `obj` - 확장Object Command
- `public` - Command(String str, Image img, Image imgActive, Object obj) 커맨드를 생성한다. 지정한 문자열과 이미지와 선택되었을 때 이미지를 가지는 커맨드를 생성한다. obj는 사용자가 임의로 특정 Object를 설정 가능하며
- `getExtObject함수를` - 이용하여 읽을 수 있다.

**매개 변수**

- `str` - 문자열
- `img` - 이미지
- `imgActive` - 선택되었을 때 이미지
- `obj` - 확장Object Command
- `public` - Command(String str, String imgString, Object obj) 커맨드를 생성한다. 지정한 문자열과 지정한 자원에서 읽어 들이는 이미지로 커맨드를 생성한다. 이미지는 getNormalImage함수가 불릴 때 Image.loadImage함수를 호출해서 차후에 읽혀지도록 한다. 이때 선택되었을 때의 이미지는 지정한 이미지가 된다. obj는 사용자가 임의로 특정 Object를 설정 가능하며 getExtObject함수를 이용하여 읽을 수 있다.

**매개 변수**

- `str` - 문자열
- `imgString` - 이미지 자원의 경로명을 나타내는 문자열
- `obj` - 확장Object Command
- `public` - Command(String str, String imgString1, String imgString2,
- `Object` - obj) 커맨드를 생성한다. 지정한 문자열과 지정한 자원에서 읽혀진 이미지로 커맨드를 생성한다. 이미지는 getNormalImage함수가 불릴 때 Image.loadImage함수를 호출해서 차후에 읽혀지도록 한다. imgString1은 일반 이미지의 자원 경로명을, imgString2는 선택되었을 때의 이미지의 자원 경로명을 지정한다. obj는 사용자가 임의로 특정
- `Object를` - 설정 가능하며 getExtObject함수를 이용하여 읽을 수 있다.

**매개 변수**

- `str` - 문자열
- `imgString1` - 이미지 자원의 경로명을 나타내는 문자열
- `imgString2` - 이미지 자원의 경로명을 나타내는 문자열
- `obj` - 확장 Object 메쏘드 상세 설명 getString
- `public` - String getString() 명령을 나타내는 문자열을 돌려준다. 내부에 저장되어 있는 명령을 기술하는 문자열을 돌려준다.

**반환 값**

명령을 나타내는 문자열 getExtObject public Object getExtObject() 생성시 설정한 Object객체를 돌려준다 내부에 저장되어 있는 명령을 확장하기 위한 객체를 돌려준다.

**반환 값**

확장Object getNormalImage public Image getNormalImage() 일반적인 이미지를 얻어 온다. 이미지가 지정되어 있으면 이미지를 돌려주고, 이미지를 가지고 있는 자원의 문자열이 지정되어 있으면, 문자열로부터 자원을 Image.loadImage함수로 로드한다.

**반환 값**

이미지

**참고 항목**

Image.loadImage(java.lang.String, org.kwis.msp.lcdui.ImageObserver)

#### getActiveImage

public Image getActiveImage() 활성화되었을 때 사용하는 이미지를 얻어 온다. 이미지가 지정되어 있으면 이미지를 돌려주고, 이미지를 가지고 있는 자원의 문자열이 지정되어 있으면, 문자열로부터 자원을 Image.loadImage함수로 로드한다.

**반환 값**

이미지 Class CommandBarComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.CommandBarComponent public class CommandBarComponent extends Component Command 컴포넌트. 등록된 하나 이상의 커맨드를 바 형태로 구성한다. 화면에 현재 화면에 사용자가 내릴 수 있는 명령어를 보여주며, 사용자로부터 명령을 선택 받다. Active된 Index의 초기값은 -1이다. Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, configure, focusNotify, getBackground, getCard, getForeground, getHeight, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, layout, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString, validate Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명 CommandBarComponent public CommandBarComponent() 커맨드 바 컴포넌트를 생성한다. 메쏘드 상세 설명 getPreferredHeight public int getPreferredHeight(int w) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. 지정된 제한된 폭을 가질 경우의 컴포넌트의 높이를 돌려준다. 만일 LabelComponent 나 TextFieldComponent, TextAreaComponent와 같이 포맷팅이 가능한 컴포넌트인 경우에는 가변 폭을 가질 수가 있다. 가변 폭을 가지게 되면, 폭에 따라서 높이가 달라지게 된다. 이때 이 함수를 통해서 컴포넌트의 높이를 얻어 온다. 만일, w가 -1이 면 폭에 제한이 없는 것으로 계산된다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `w` - 가변 폭.

**반환 값**

컴포넌트의 높이. getPreferredHeight public int getPreferredHeight() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. ContainerComponent에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 높이 getPreferredWidth public int getPreferredWidth() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 폭을 결정한다. Container에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredWidth in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 폭. getSize public int getSize() 등록된 커맨드의 개수를 구한다

**반환 값**

등록된 Command의 개수 addCommand public int addCommand(Command cmd) 커맨드를 하나 추가 시킨다. 초기에 커맨드가 추가된 상태에서는 Active된 Index는 - 1이다. setActiveIndex를 이용하여 원하는 인덱스의 Command를 Active하여야 한다.

**매개 변수**

- `cmd` - 추가할 커맨드

**반환 값**

추가된 Command의 Index , 실패한 경우 -1을 반환한다.

**참고 항목**

Command, setActiveIndex(int)

#### removeCommand

public void removeCommand(Command cmd) 커맨드를 삭제한다. 지정한 커맨드를 삭제한다.

**매개 변수**

- `cmd` - 삭제할 커맨드

**참고 항목**

Command

#### removeAll

public void removeAll() 모든 커맨드를 삭제한다.

**참고 항목**

Command

#### setActiveIndex

public void setActiveIndex(int index) 선택된 커맨드를 지정한다.

**매개 변수**

- `index` - 선택할 커맨드의 인덱스 getActiveIndex
- `public` - int getActiveIndex() 선택된 커맨드의 인덱스를 돌려준다. 만일 선택된 인덱스가 없는 경우라면 -1을 돌려준다.

**반환 값**

선택된 커맨드의 인덱스 getCommand public Command getCommand(int index) 커맨드를 돌려준다. 인덱스에 대응하는 커맨드를 돌려준다. 만일 해당하는 인덱스에 커맨드가 존재하지 않으면 null을 돌려준다.

**매개 변수**

- `index` - 가져올 커맨드의 인덱스

**반환 값**

지정한 커맨드 setCommandListener public void setCommandListener(CommandListener cl, Object obj) 커맨드 Listener를 지정한다. 커맨드가 선택되었거나 커맨드의 포커스가 변경되었을 때 이 함수를 호출한다.

**매개 변수**

- `cl` - 커맨드 Listener
- `obj` - commandAction시에 넘어가는 Object keyNotify
- `protected` - boolean keyNotify(int type, int chr) 이하 메소스 설명은 Component 클래스에서 복사되었음 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력 값이 된다. Overrides
- `keyNotify` - in class Component
- `Following` - copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. pointerNotify protected boolean pointerNotify(int type, int x, int y) 이하 메소스 설명은 Component 클래스에서 복사되었음 포인터 입력을 받으면 호출된다. 현재 모든 휴대폰이 포인팅 디바이스가 없으므로 이 함수는 불리지 않는다. Overrides pointerNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 포인팅 디바이스의 타입
- `x` - 디바이스의 'x'축 좌표
- `y` - 디바이스의 'y'축 좌표

**반환 값**

만일 컴포넌트가 인수로 넘어오는 이벤트를 이 컴포넌트가 처리했다면, false를 넘김 paintContent public void paintContent(Graphics g) 이하 메소스 설명은 Component 클래스에서 복사되었음 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides paintContent in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics Class Component java.lang.Object | +--org.kwis.msp.lwc.Component Direct Known Subclasses: ButtonComponent, ComboComponent, CommandBarComponent, ContainerComponent, DateFieldComponent, ImageComponent, LabelComponent, ProgressComponent, ScrollbarComponent, TextComponent, TickerComponent public abstract class Component extends Object 가장 기본이 되는 화면에 보여지는 클래스이다. 위치와 크기를 가지며, 사용자의 입력을 받아서 적절한 행동을 하는 클래스이다. 화면에 보여지는 모든 UI 컴포넌트는 이 클래스를 상속 받아서 구현되어야 한다. Component 클래스를 상속 받은 자식 클래스들의 상위 부모 컴포넌트 상에서의 위치와 폭과 넓이를 가지며, 배경색과 컴포넌트의 특성(입력 가능인지, 입력 포커스 등)을 가진다. Component의 내부에 포커스나 커서가 존재할 경우 화면에는 언제나 포커스나 커서가 보여야 한다. Component클래스는 항상 상위 부모가 있어야 하며, 상위 부모가 없어도 되는 Component 는 ShellComponent가 된다. 즉, 화면에 적어도 하나 이상의 ShellComponent 가 있어야지만, Component가 화면에 보이게 된다. 컴포넌트는 addComponent한 후에 다른 부모 컴포넌트에 더 이상 addComponent할 수 없다. 모든 컴포넌트는 자신의 폭과 넓이를 프로그램에 의해서 결정할 수 있지만, 때에 따라서는 상위 컴포넌트에 의해서 그 크기가 결정이 된다. 예를 들면, FormComponent위에 있는 LabelComponent와 같은 컴포넌트는 내부의 문자열의 길이에 따라서, Component의 크기가 달라진다. 수행 도중에 사용자가 컴포넌트의 내용을 변경함으로써, 컴포넌트의 크기가 다시 계산될 필요가 있다면, invalidate함수를 호출한다. 그러면, Component가 화면에 보여질 때나, paintContent함수가 호출될 때에 validate()함수를 호출하며, 이 함수에 의해 하위 컴포넌트까지 다시 모두 적당한 크기가 계산이 된다. 컴포넌트는 자신의 적절한 크기를 계산하여 돌려주는 기능을 가진다. 컴포넌트의 내용에 따라서 적당한 크기를 돌려주며, 이 함수는 상위의 ContainerComponent의 layout함수에서 하위 컴포넌트의 크기를 결정하기 위해서 사용된다. 포맷팅을 할 수 있는 컴포넌트(Label, TextField, TextArea)를 위해서 특정 폭을 주었을 때 적당한 높이를 얻어오는 함수도 있다. 컴포넌트의 크기 결정은 자신이 하는 것이 아니라 상위 컴포넌트가 결정한다. 그 상위 컴포넌트의 전체 크기는 상위 컴포넌트의 상위 컴포넌트가 한다. 모든 UI컴포넌트는 맨 마지막 상위 컴포넌트는 항상 ShellComponent가 되어야 한다. 컴포넌트는 이벤트에 대해서 처리할 책임을 가진다. 만일 컴포넌트의 CanHandleInput함수가 true를 돌려주면, 그 컴포넌트는 ContainerComponent의 setFocus함수에 의해서 입력 포커스를 가질 수 있으며, 입력 포커스를 가지는 경우에 keyNotify함수가 불릴 수 있다. 이외에도 showNotify함수와 focusNotify함수, pointerNotify함수가 불리며, 특히나 화면에 어떤 내용을 칠해야 하는 경우에는 paintContent함수가 불린다. keyNotify함수나 pointerNotify함수는 자기 자신이 이벤트를 처리했으면, true를 돌려준다. 그러면, 상위 컴포넌트에 키 이벤트가 전달되지 않는다. 만일 false를 돌려주면, 상위 컴포넌트에 키 이벤트가 전달된다. 모든 이벤트에 대해서는 setEventListener함수를 통하여 지정된 이벤트 Listener에게 모든 발생한 이벤트를 알려준다. 이 이벤트 Listener가 true로 돌려주는 경우에는 더 이상 이벤트가 처리되지 않고 false로 돌려주는 경우에는 이벤트는 정상적으로 처리 된다. paintContent함수를 구현할 때에는 Graphics내용이 컴포넌트의 위치와 크기에 맞도록 원점과 클리핑 영역이 변경되어서 되어서 넘어 온다. 만일 이 클리핑의 내용을 setClip함수로 변경하거나, reset 함수로 재 초기화를 시키면 컴포넌트의 내용이 엉뚱한 곳에 출력되거나 화면에 나중에 나타나는 등의 문제가 생길 수 있다. 정렬 조합 규칙 Component에서제공하고 있는 정렬형태는 LAYOUT_LEFT와 LAYOUT_RIGHT,LAYOUT_HCENTER,LAYOUT_TOP, LAYOUT_BOTTOM,LAYOUT_VCENTER이다. 아래의 경우 IllegalArgumentException이 발생한다. LAYOUT_LEFT|LAYOUT_RIGHT LAYOUT_TOP|LAYOUT_BOTTOM Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 필드 상세 설명

#### LAYOUT_LEFT

public static final int LAYOUT_LEFT Component의 좌측 정렬 값. 이미지나 문자 데이타의 위치를 컴포넌트의 영역에서 좌측으로 정렬한다. '1'값이 지정되어 있다.

#### LAYOUT_RIGHT

public static final int LAYOUT_RIGHT Component의 우측 정렬 값. 이미지나 문자 데이타의 위치를 컴포넌트의 영역에서 우측으로 정렬한다. '2'값이 지정되어 있다.

#### LAYOUT_HCENTER

public static final int LAYOUT_HCENTER Component의 가운데 수평 정렬 값. 이미지나 문자 데이타의 위치를 컴포넌트의 수평에서 중앙 위치로 정렬한다. '4'값이 지정되어 있다.

#### LAYOUT_TOP

public static final int LAYOUT_TOP Component의 위쪽 정렬 값. 이미지나 문자 데이타의 위치를 컴포넌트의 영역에서 위쪽 위치로 정렬한다. '8'값이 지정되어 있다.

#### LAYOUT_BOTTOM

public static final int LAYOUT_BOTTOM Component의 아래쪽 정렬 값. 이미지나 문자 데이타의 위치를 전체 컴포넌트의 영역에서 아래쪽 위치로 정렬한다. '16'값이 지정되어 있다.

#### LAYOUT_VCENTER

public static final int LAYOUT_VCENTER Component의 가운데 수직 정렬 값. 이미지나 문자 데이타의 위치를 컴포넌트의 수직 영역에서 중앙 위치로 정렬한다. '32'값이 지정되어 있다.

#### x

protected int x 상위 부모 Component로 부터의 x축 픽셀 위치.

#### y

protected int y 상위 부모 Component로 부터의 y축 픽셀 위치.

#### w

protected int w 컴포넌트의 폭의 픽셀 크기.

#### h

protected int h 컴포넌트의 높이의 픽셀 크기.

#### parent

protected ContainerComponent parent 상위 부모 컴포넌트.

#### bg

protected int bg 배경색. 만일 -1 이면 투명한 색이 된다.

#### fg

protected int fg 전경색 기본값은 각 컴포넌트에 따라 다르게 지정된다.

#### evtListener

protected EventListener evtListener

#### evtListenerObj

protected Object evtListenerObj

#### prefW

protected int prefW

#### prefH

protected int prefH

#### POS_MASK

public static final int POS_MASK 위치 이동이 됨을 알리는 상수.

**참고 항목**

configure(int, int, int, int, int)

#### SIZE_MASK

public static final int SIZE_MASK 크기 변경이 됨을 알리는 상수.

**참고 항목**

configure(int, int, int, int, int)

#### mask

protected int mask

#### VALID_MASK

protected static final int VALID_MASK

#### HAS_FOCUS_MASK

protected static final int HAS_FOCUS_MASK

#### INPUT_MASK

protected static final int INPUT_MASK

#### PREFER_SIZE_MASK

protected static final int PREFER_SIZE_MASK

#### FOCUS_NOTIFY

public static final int FOCUS_NOTIFY 포커스가 왔음을 알리는 상수. 1로 지정되어 있다.

**참고 항목**

setEventListener(org.kwis.msp.lwc.EventListener, java.lang.Object)

#### SHOW_NOTIFY

public static final int SHOW_NOTIFY 보여지거나 가려짐을 알리는 상수. 2로 지정되어 있다.

**참고 항목**

setEventListener(org.kwis.msp.lwc.EventListener, java.lang.Object)

#### KEY_NOTIFY

public static final int KEY_NOTIFY 키 관련 이벤트가 생성됨을 알리는 상수. 3로 지정되어 있다.

**참고 항목**

setEventListener(org.kwis.msp.lwc.EventListener, java.lang.Object)

#### POINTER_NOTIFY

public static final int POINTER_NOTIFY 포인터 관련 이벤트가 생성됨을 알리는 상수. 4로 지정되어 있다.

**참고 항목**

setEventListener(org.kwis.msp.lwc.EventListener, java.lang.Object)

#### KEY_PRESSED

public static final int KEY_PRESSED 키가 눌렸을 때 이벤트 타입.

**참고 항목**

setEventListener(org.kwis.msp.lwc.EventListener, java.lang.Object)

#### KEY_RELEASED

public static final int KEY_RELEASED 키가 떼어졌을 때 이벤트 타입.

**참고 항목**

setEventListener(org.kwis.msp.lwc.EventListener, java.lang.Object)

#### KEY_REPEATED

public static final int KEY_REPEATED 키가 반복해서 눌렸을 때 이벤트 타입.

**참고 항목**

setEventListener(org.kwis.msp.lwc.EventListener, java.lang.Object)

#### KEY_TYPED

public static final int KEY_TYPED 키가 눌렸을 때 이벤트 타입.

**참고 항목**

setEventListener(org.kwis.msp.lwc.EventListener, java.lang.Object)

#### POINT_PRESSED

public static final int POINT_PRESSED 포인터 기기가 눌렸을 때 이벤트 타입.

**참고 항목**

setEventListener(org.kwis.msp.lwc.EventListener, java.lang.Object)

#### POINT_RELEASED

public static final int POINT_RELEASED 포인터 기기가 떼어졌을 때 이벤트 타입.

**참고 항목**

setEventListener(org.kwis.msp.lwc.EventListener, java.lang.Object)

#### POINT_DRAGGED

public static final int POINT_DRAGGED 포인터 기기가 눌린 상태에서 움직였을 때 이벤트 타입.

**참고 항목**

setEventListener(org.kwis.msp.lwc.EventListener, java.lang.Object) 생성자 상세 설명

#### Component

protected Component() 생성자이다. 상속된 컴포넌트에 의해서 사용된다. 메쏘드 상세 설명

#### getWidth

public int getWidth() 컴포넌트의 폭을 돌려 준다.

**반환 값**

컴포넌트의 폭. getHeight public int getHeight() 컴포넌트의 높이를 돌려 준다.

**반환 값**

컴포넌트의 높이. canHandleInput public boolean canHandleInput() 컴포넌트가 입력을 받을 수 있는 여부를 돌려준다. 이 함수의 반환값이 true이면 현재 컴포넌트는 포커스를 받을 수 있는(입력을 처리할 수 있는) 컴포넌트임을 알려준다. ContainerComponent의 setFocus함수를 수행함으로써, 그때부터 모든 키 입력을 사용자로부터 받아들일 수 있게 된다. 컴포넌트의 입력 가능 여부는 클래스 생성자에서 mask 값을 변경함으로써 결정된다.

**반환 값**

입력을 받을 수 있는지의 여부 hasFocus public boolean hasFocus() 컴포넌트가 입력 포커스를 가지고 있는지의 여부를 돌려준다. 현재 입력 포커스를 가지고 있고, 사용자가 버튼을 누르면, 이 컴포넌트의 keyNotify함수가 호출되며, 사용자가 입력하는 키는 그 함수의 인자로 넘어 온다.

**반환 값**

포커스를 가지고 있는지의 여부 configure public void configure(int x, int y, int w, int h, int mask) 컴포넌트의 위치나 크기를 변경한다. mask에 따라서 컴포넌트의 크기나 위치를 변경한다. mask값과 POS_MASK를 논리적 AND 연산을 해서 그 값이 POS_MASK이면, 상위 컴포넌트 내에서 위치 x, y로 변경해 준다. mask값과 SIZE_MASK를 논리적 AND 연산을 해서 그 값이 SIZE_MASK이면, 컴포넌트의 크기를 (w, h)로 변경해 준다. 즉 컴포넌트의 크기와 위치를 동시에 변경할 수 있다. 이 함수는 변경된 부분에 대해서 repaint함수를 호출하므로, 칠해질 영역이 paintContent함수에 의해서 칠해지도록 한다. 컴포넌트의 크기는 상위 부모 컴포넌트의 layout함수에 의해서 그 크기가 결정된다.

**매개 변수**

- `x` - 컴포넌트의 상위 컴포넌트 상에서의 'x'축 위치
- `y` - 컴포넌트의 상위 컴포넌트 상에서의 'y'축 위치
- `w` - 컴포넌트의 폭
- `h` - 컴포넌트의 높이
- `mask` - POS_MASK | SIZE_MASK가 올 수 있으며, POS_MASK가 오는 경우에 x, y값 이 유효한 값이 오며, SIZE_MASK가 오는 경우에 w, h값이 유효한 값이 된다. getX
- `public` - int getX()
- `x축의` - 좌표를 돌려준다. 컴포넌트의 상위 부모 컴포넌트 상에서의 x축 좌표를 돌려준다.

**반환 값**

x축 좌표 getY public int getY() y축의 좌표를 돌려준다. 컴포넌트의 상위 부모 컴포넌트 상에서의 y축 좌표를 돌려준다.

**반환 값**

y축 좌표 calcPreferredSize protected void calcPreferredSize(int w) 컴포넌트의 적절한 크기를 계산한다. getPreferredHeight public int getPreferredHeight() 컴포넌트의 적절한 높이를 반환한다. ContainerComponent에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다.

**반환 값**

컴포넌트의 높이 getPreferredHeight public int getPreferredHeight(int w) 컴포넌트의 적절한 높이를 반환한다. 지정된 제한된 폭을 가질 경우의 컴포넌트의 높이를 돌려준다. 만일 TextBoxComponent와 같이 포맷팅이 가능한 컴포넌트인 경우에는 가변 폭을 가질 수가 있다. 가변 폭을 가지게 되면, 폭에 따라서 높이가 달라지게 된다. 이때 이 함수를 통해서 컴포넌트의 높이를 얻어 온다. 만일, w가 -1이 면 폭에 제한이 없는 것으로 계산된다.

**매개 변수**

- `w` - 가변 폭.

**반환 값**

컴포넌트의 높이. getPreferredWidth public int getPreferredWidth() 컴포넌트의 적절한 폭을 반환한다. Container에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다.

**반환 값**

컴포넌트의 폭. setBackground public void setBackground(int bg) 배경색을 지정한다. 만일 배경색이 -1이면 투명색이 되어 배경색을 칠하지 않는다. 색은 0x00RRGGBB 값이 된다.

**매개 변수**

- `bg` - 컴포넌트 배경색

**참고 항목**

getBackground()

#### setForeground

public void setForeground(int fg) 전경색을 지정한다. 전경색을 사용하는 컴포넌트에서 사용되며 기본값은 각 컴포넌트에 따라 다르게 설정 된다.

**매개 변수**

- `fg` - 컴포넌트의 전경생

**참고 항목**

setBackground(int bg),

#### getBackground

public int getBackground() 배경색을 돌려 준다.

**반환 값**

컴포넌트의 배경색

**참고 항목**

setBackground(int)

#### getForeground

public int getForeground() 전경색을 돌려준다.

**반환 값**

컴포넌트의 전경색

**참고 항목**

setForeground(int)

#### paintContent

public void paintContent(Graphics g) 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다.

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics

#### isValid

protected boolean isValid() 컴포넌트가 유효한 좌표와 크기를 가지는지 여부를 돌려준다. 이 함수는 컴포넌트가 유효한 좌표와 크기를 가지는지 여부를 돌려준다. 컴포넌트의 내부의 내용이 바뀌어서 크기가 달라져야 하는 경우에는 이 함수는 false를 돌려주고, 그렇지 않은 경우에는 true를 돌려준다.

**반환 값**

컴포넌트가 유효한지 안 한지 여부. invalidate public void invalidate() 컴포넌트가 유효한 좌표와 크기를 가지 않음을 알려준다. validate public void validate() 컴포넌트에 유효한 좌표와 크기를 가지게 한다. paintContent와 showNotify에서 호출이 되며, 컴포넌트에 유효한 좌표가 가지도록 layout함수를 호출한다. layout은 자기 자신의 크기를 결정하지 않고, 자기 자신 크기를 바탕으로 하위 자식 컴포넌트의 크기를 결정한다. layout protected void layout() 하위 컴포넌트의 크기와 위치를 결정한다. setFocus public void setFocus() 키 이벤트가 전달되도록 설정한다. 사용자의 키 입력을 자기 자신 컴포넌트에게 오도록 한다.

**참고 항목**

focusNotify(boolean)

#### focusNotify

public void focusNotify(boolean b) 포커스를 받으면 호출된다. 컴포넌트가 포커스를 가지거나 가지고 있지 않음을 보여주기 위해서 repaint함수를 호출하여, 다시 자기 자신을 그리도록 한다.

**매개 변수**

- `b` - 포커스를 가질 땐 true가 넘어오고, 가지지 않을 땐 false keyNotify
- `protected` - boolean keyNotify(int type, int chr) 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력 값이 된다.

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. pointerNotify protected boolean pointerNotify(int type, int x, int y) 포인터 입력을 받으면 호출된다. 현재 모든 휴대폰이 포인팅 디바이스가 없으므로 이 함수는 불리지 않는다.

**매개 변수**

- `type` - 포인팅 디바이스의 타입
- `x` - 디바이스의 'x'축 좌표
- `y` - 디바이스의 'y'축 좌표

**반환 값**

만일 컴포넌트가 인수로 넘어오는 이벤트를 이 컴포넌트가 처리했다면, false를 넘김 showNotify protected void showNotify(boolean bShow) 화면의 내용이 보이면 호출된다. addComponent나 removeComponent에 의해서 불리거나, 자신의 맨 상위의 부모 컴포넌트(ShellComponent)가 show에 의해서 화면에 나타날 때 호출된다.

**매개 변수**

- `bShow` - 컴포넌트가 나타나는지 안 나타나는지 여부 repaint
- `public` - void repaint() 화면의 내용을 갱신할 필요가 있을 때 부른다. 컴포넌트 전체를 갱신한다. 이 함수는 최종적으로 Card의 repaint를 호출하며, 호출된 repaint함수는 일정 시간 이후에 해당 컴포넌트의 paintContent함수를 자동적으로 부르는 과정을 거친다. isShown
- `public` - boolean isShown() 현재 컴포넌트가 보이는지 안 보이는지 여부를 돌려준다. 현재 컴포넌트가 화면에 보이면 true, 그렇지 않으면 false를 돌려준다.

**반환 값**

화면에 보이는 여부 processEvent protected boolean processEvent(int type, int subtype, int param1, int param2) 이벤트를 처리한다.

**매개 변수**

- `type` - 이벤트 타입
- `subtype` - 이벤트 타입에 따른 서브 이벤트 타입
- `param1` - 부가적인 인수
- `param2` - 부가적인 인수 repaint
- `public` - void repaint(int x, int y, int w, int h) 화면의 내용을 갱신할 필요가 있을 때 부른다. 이 함수는 최종적으로 Card의
- `repaint를` - 호출하며, 호출된 repaint함수는 일정 시간 이후에 해당 컴포넌트의 paint()함수를 자동적으로 부르는 과정을 거친다.

**매개 변수**

- `x` - 갱신할 영역의 x축 좌표
- `y` - 갱신할 영역의 y축 좌표
- `w` - 갱신할 영역의 폭
- `h` - 갱신할 영역의 높이 serviceRepaints
- `public` - void serviceRepaints() 갱신된 내용을 즉시 화면에 출력해준다. repaint에 의한 paint를 나중에 부르는 것이 아니라, 직접 paint함수를 불러서 화면에 출력한다. toString
- `public` - String toString()
- `Object를` - string으로 변환하는 함수이다. 컴포넌트를 문자열로 나타낸다. Overrides
- `toString` - in class Object

**반환 값**

컴포넌트를 나타내는 문자열 getXOnScreen public int getXOnScreen() 화면상에 대응되는 실제 좌표를 구한다. Component의 왼쪽 상단의 화면상에서 X좌표를 구한다.

**반환 값**

화면상에서의 X좌표 getYOnScreen public int getYOnScreen() 화면상에 대응되는 실제 좌표를 구한다. Component의 왼쪽 상단의 화면상에서의 Y좌표를 구한다.

**반환 값**

화면상에서의 Y좌표 getCard public Card getCard() 현재 컴포넌트에 연결된 카드를 돌려준다. ShellComponent와 같이 상위 컴포넌트는 내부에 Card를 가지게 된다. 현재 컴포넌트의 맨 상위 부모 컴포넌트의 Card를 돌려주게 된다. 그러나, 만일 상위 부모 컴포넌트가 존재하는 경우가 아닌 경우에는 null이 넘어 갈 수 있다.

**반환 값**

컴포넌트와 연관 있는 Card

**참고 항목**

Card

#### setEventListener

public void setEventListener(EventListener listener, Object obj) 이벤트 Listener를 등록한다. 지정된 이벤트 Listener에게 이벤트를 일단 보내준다. 만일 이벤트 Listener가 true를 돌려주면 이벤트 처리를 하지 않으며, false를 돌려주면 이벤트를 처리한다.

**매개 변수**

- `listener` - 이벤트 Listener
- `obj` - 이벤트 Listener 불릴 때의 파라미터

**참고 항목**

EventListener Class ContainerComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.ContainerComponent Direct Known Subclasses: FormComponent, ShellComponent public abstract class ContainerComponent extends Component 다른 컴포넌트의 상위 부모 컴포넌트가 될 수 있는 컴포넌트. 자식 컴포넌트의 위치와 크기를 결정해 주며, 포커스 관리를 해준다. 컴포넌트는 addComponent함수로 자식 컴포넌트로 등록할 수 있으며, removeComponent함수로 삭제할 수 있다. 컴포넌트는 상위 부모 컴포넌트가 있으며, 그 맨 상위 부모 컴포넌트가 ShellComponent이며 show함수로 보여질 때 화면에 나타나게 된다. 컨테이너 컴포넌트는 layout함수를 통해서 하위 자식 컴포넌트들의 크기와 위치를 결정해준다. 컨테이너 내에는 인셋(Inset)이 있어 하위 자식 컴포넌트들이 인셋내부에만 나타나고, 인셋 밖에는 출력되지 않도록 되어 있다. 특정 컴포넌트가 키 입력을 받기 위해서는 setFocus 함수를 호출해 주어야만 한다.

**참고 항목**

ShellComponent, Component Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, configure, focusNotify, getBackground, getCard, getForeground, getHeight, getPreferredHeight, getPreferredHeight, getPreferredWidth, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, layout, paintContent, pointerNotify, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 필드 상세 설명

#### cmps

protected Component[] cmps 내부 자식 컴포넌트들

#### ncomp

protected int ncomp 내부 자식 컴포넌트의 개수

#### cmpFocus

protected Component cmpFocus 포커스를 가진 컴포넌트

#### offsetX

protected int offsetX 내부 컴포넌트들의 스크롤된 위치.

#### offsetY

protected int offsetY 내부 컴포넌트들의 스크롤된 위치.

#### insetTop

protected short insetTop 내부 공간의 상위 높이

#### insetBottom

protected short insetBottom 내부 공간의 하위 높이.

#### insetLeft

protected short insetLeft 내부 공간의 좌측 폭.

#### insetRight

protected short insetRight 내부 공간의 우측 폭.

#### useFrame

protected boolean useFrame 프레임의 사용여부. 생성자 상세 설명

#### ContainerComponent

protected ContainerComponent() 생성자이다. 상속된 컴포넌트에 의해서 사용된다. 메쏘드 상세 설명

#### addComponent

public void addComponent(int index, Component cmp) 자식 컴포넌트를 하나 추가한다. 지정한 위치에 cmp가 가리키는 컴포넌트를 추가한다. cmp가 null인 경우 NullPointerException이 발생한다. 또한 cmp가 이미 다른 부모 컴포넌트를 가지는 경우 IllegalArgumentException이 발생 한다. index값이 '0'보다 작거나 추가된 컴포넌트의 개수보다 큰 경우 IndexOutOfBoundsException이 발생한다.

**매개 변수**

- `index` - 넣을 위치
- `cmp` - 넣을 컴포넌트 Throws
- `IllegalArgumentException` - cmp가 이미 다른 부모 컴포넌트를 가지고 있 는 경우 발생
- `IndexOutOfBoundsException` - index가 유효한 영역을 벗어나 있는 경우
- `NullPointerException` - cmp이 null인 경우 addComponent
- `public` - int addComponent(Component cmp) 자식 컴포넌트를 하나 추가한다. 맨 위에 자식 컴포넌트를 추가한다.

**매개 변수**

- `cmp` - 추가할 자식 컴포넌트 Throws
- `IllegalArgumentException` - cmp가 이미 다른 부모 컴포넌트를 가지는 경 우
- `NullPointerException` - cmp이 null인 경우 setComponent
- `public` - void setComponent(int index, Component cmp) 자식 컴포넌트를 하나 대치한다. 지정한 인덱스의 컴포넌트를 주어진 컴포넌트로 대치한다. cmp가 null인 경우 NullPointerException이 발생한다. 또한 cmp가 이미 다른 부모 컴포넌트를 가지는 경우 IllegalArgumentException이 발생 한다.
- `index값이` - '0'보다 작거나 추가된 컴포넌트의 개수보다 큰 경우
- `IndexOutOfBoundsException이` - 발생한다.

**매개 변수**

- `index` - 바꿀 위치
- `cmp` - 바뀔 컴포넌트 Throws
- `IllegalArgumentException` - cmp가 이미 다른 부모 컴포넌트를 가지고 있는 경우
- `NullPointerException` - cmp가 null인 경우
- `IndexOutOfBoundsException` - index가 유효한 영역을 벗어나 있는 경우 removeComponent
- `public` - void removeComponent(int index) 지정된 순서의 컴포넌트를 삭제한다. index번째 있는 컴포넌트를 삭제한다.
- `index값이` - '0'보다 작거나 추가된 컴포넌트의 개수보다 큰 경우
- `IndexOutOfBoundsException이` - 발생한다.

**매개 변수**

- `index` - 삭제할 컴포넌트 Throws
- `IndexOutOfBoundsException` - index가 유효한 영역을 벗어나 있는 경우 removeComponent
- `public` - void removeComponent(Component cmp) 지정된 컴포넌트를 삭제한다. 만일 지정된 컴포넌트가 자식 컴포넌트로 등록되어 있지 않은 경우 IllegalArgumentException이 발생한다.

**매개 변수**

- `cmp` - 삭제할 컴포넌트 removeAllComponents
- `public` - void removeAllComponents() 모든 컴포넌트를 삭제한다. getComponent
- `public` - Component getComponent(int i) 특정 stack 순서의 컴포넌트를 가져온다. 만일 인덱스가 유효한 영역을 벋어 나는 경우에는 null을 돌려준다.

**매개 변수**

- `i` - 가져올 컴포넌트의 스택 순서

**반환 값**

컴포넌트 getIndexOf public int getIndexOf(Component cmp) 컴포넌트의 stack 순서를 가져온다.

**매개 변수**

- `cmp` - 순서를 가져올 컴포넌트

**반환 값**

스택 순서 validate public void validate() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트에 유효한 좌표와 크기를 가지게 한다. paintContent와 showNotify에서 호출이 되며, 컴포넌트에 유효한 좌표가 가지도록 layout함수를 호출한다. layout은 자기 자신의 크기를 결정하지 않고, 자기 자신 크기를 바탕으로 하위 자식 컴포넌트의 크기를 결정한다. Overrides validate in class Component getNextTraversalComponent protected Component getNextTraversalComponent() 포커스 가질 수 있는 다음 컴포넌트를 돌려준다. 포커스를 가질 수 있는 다음 컴포넌트를 돌려준다. 돌려지는 컴포넌트는 현재 컴포넌트의 자식 컴포넌트 중 하나가 된다. 만일 포커스를 가질 수 있는 컴포넌트가 없는 경우에는 null을 돌려준다.

**반환 값**

포커스를 가질 수 있는 다음 컴포넌트 getPrevTraversalComponent protected Component getPrevTraversalComponent() 포커스 가질 수 있는 이전 컴포넌트를 돌려준다. 포커스를 가질 수 있는 다음 컴포넌트를 돌려준다. 돌려지는 컴포넌트는 현재 컴포넌트의 자식 컴포넌트 중 하나가 된다. 만일 포커스를 가질 수 있는 컴포넌트가 없는 경우에는 null을 돌려준다.

**반환 값**

포커스를 가질 수 있는 이전 컴포넌트 keyNotify protected boolean keyNotify(int type, int key) 이하 메소스 설명은 Component 클래스에서 복사되었음 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력 값이 된다. Overrides keyNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. processEvent protected boolean processEvent(int type, int subtype, int param1, int param2) 이하 메소스 설명은 Component 클래스에서 복사되었음 이벤트를 처리한다. Overrides processEvent in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 이벤트 타입
- `subtype` - 이벤트 타입에 따른 서브 이벤트 타입
- `param1` - 부가적인 인수
- `param2` - 부가적인 인수 paint
- `protected` - void paint(Graphics g) 그래픽스 g를 가지고 컨테이너 컴포넌트를 그린다. 이때 컨테이너 컴포넌트는 자식 컴포넌트의 paintContent함수를 이용하여 자식 컴포넌트 까지 그려준다.

**매개 변수**

- `g` - 컴포넌트를 그릴 그래픽스 개체 scrollTo
- `protected` - boolean scrollTo(int dx, int dy) 특정 위치로 화면을 이동한다. dx, dy가 가리키는 오프셋(offset)값을 가지도록 스크롤한다. 만일 값이 처리할 수 없는 값이라면, 상위 컴포넌트의 scrollTo를 호출한다.

**매개 변수**

- `dx` - x축으로의 이동할 거리
- `dy` - y축으로의 이동할 거리

**반환 값**

제대로 스크롤되는 경우 true, 그렇지 않으면 false repaint public void repaint(int x, int y, int w, int h) 이하 메소스 설명은 Component 클래스에서 복사되었음 화면의 내용을 갱신할 필요가 있을 때 부른다. 이 함수는 최종적으로 Card의 repaint를 호출하며, 호출된 repaint함수는 일정 시간 이후에 해당 컴포넌트의 paint()함수를 자동적으로 부르는 과정을 거친다. Overrides repaint in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `x` - 갱신할 영역의 x축 좌표
- `y` - 갱신할 영역의 y축 좌표
- `w` - 갱신할 영역의 폭
- `h` - 갱신할 영역의 높이 repaint
- `public` - void repaint() 이하 메소스 설명은 Component 클래스에서 복사되었음 화면의 내용을 갱신할 필요가 있을 때 부른다. 컴포넌트 전체를 갱신한다. 이 함수는 최종적으로 Card의 repaint를 호출하며, 호출된 repaint함수는 일정 시간 이후에 해당 컴포넌트의 paintContent함수를 자동적으로 부르는 과정을 거친다. Overrides
- `repaint` - in class Component useFrame
- `public` - void useFrame(boolean useFrame)
- `ContainerComponent가` - 화면에 보이는 영역에서 테두리를 화면에 출력할 것인지를 지정한다. true값인 경우 각 ContainerComponent에서 지정한 테두리 두께 값을 적용하고, false인 경우 현재 지정된 테두리 두께 값을 '0'으로 초기화 한다. paintFrame
- `protected` - void paintFrame(Graphics g)
- `useFrame의` - 인수를true으로 호출하는 경우에 화면을 그릴 때 호출된다.

**매개 변수**

- `g` - 그릴 그래픽 개체 getNumberOfComponent
- `public` - int getNumberOfComponent() 등록된 Component의 수를 수한다

**반환 값**

현재 등록되어 있는 Component의 수 Class DateFieldComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.DateFieldComponent public class DateFieldComponent extends Component DateFieldComponent는 날짜와 시간을 보여주는 필드를 화면에 표시해주고 이 값을 수정할 수 있다. DateFieldComponent를 생성할 때 지정한 모드에 관계없이 시스템에 설정된 기본 TimeZone과 Date를 사용하여 현재 시간과 날짜로 초기화된 데이타를 가지게 된다. 이 값은 getDate,setDate를 통해서 값을 얻어오거나 수정할 수 있다. DateFieldComponent의 날짜와 시간은 지정한 모드에 따라 화면에 출력되고 그 값을 방향키 입력에 의해서 수정할 수 있다. DateFieldComponent에서는 시간과 날짜를 지정하거나 수정 할 수 있는 3가지 타입의 모드를 제공한다. MODE_TIME는 시간을 보여주는 필드를 화면에 출력하고 시간을 수정할 수 있다. MODE_DATE는 날짜를 보여주는 필드를 화면에 출력하고 날짜를 수정할 수 있다. MODE_TIME_DATE는 날짜와 시간을 보여주는 필드를 화면에 출력하고 각 시간과 날짜를 수정할 수 있다.

**참고 항목**

Date, Calendar, TimeZone Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, configure, focusNotify, getBackground, getCard, getForeground, getHeight, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, layout, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, toString, validate Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 필드 상세 설명

#### MODE_TIME

public static final int MODE_TIME 시간 표시모드. 이 모드를 사용하면 DateFieldComponent에서는 시간을 보여주는 필드를 화면에 출력하고 시간을 수정할 수 있다. MODE_TIME값으로 '0'이 지정되어 있다.

#### MODE_DATE

public static final int MODE_DATE 날자 표시모드. 이 모드를 사용하면 DateFieldComponent에서는 날짜를 보여주는 필드를 화면에 출력하고 날짜를 수정할 수 있다. MODE_DATE값으로 '1'이 지정되어 있다.

#### MODE_TIME_DATE

public static final int MODE_TIME_DATE 날짜와 시간 표시모드. 이 모드를 사용하면 DateFieldComponent에서는 시간과 날짜를 보여주는 필드를 화면에 출력하고 시간과 날짜를 수정할 수 있다. MODE_TIME_DATE값으로 '2'이 지정되어 있다. 생성자 상세 설명

#### DateFieldComponent

public DateFieldComponent(int mode) 시스템의 기본 TimeZone과 Date를 사용하여 현재 시간과 날짜로 초기화된 DateFieldComponent의 인스턴스를 생성한다. 주어진 모드 값에 따라 사용되는 필드가 결정된다. 모드 값이 MODE_TIME인 경우 시간를 보여주는 필드를 화면에 출력하고 시간을 수정할 수 있다 . MODE_DATE이 모드 값으로 지정된 경우 날짜를 보여주는 필드를 화면에 출력하고 날짜를 수정할 수 있다. MODE_TIME_DATE는 시간과 날짜를 보여주는 필드를 화면에 출력해 주고 시간과 날짜를 모두 수정 할 수 있다. 위의 모드 이외의 값을 모드로 지정하면 IllegalArgumentException 이 발생한다.

**매개 변수**

- `mode` - 생성할 DateFieldComponent의 모드 값 Throws
- `IllegalArgumentException` - 선언된 3가지 모드. (MODE_TIME, MODE_DATE, MODE_DATE) 외의 값을 지정한 경우

**참고 항목**

MODE_TIME, MODE_DATE, MODE_TIME_DATE, TimeZone, Date 메쏘드 상세 설명

#### getDate

public Date getDate() DateFieldComponent에서 현재 설정되어 있는 날짜 정보를 가지고 있는 Date객체를 얻어온다. 이 값은 지정된 모드에 관계없이 현재 설정된 Date객체를 반환한다. DateFieldComponent생성시 기본적으로 설정된 Date는 1970/1/00:00:00 GMT 를 기준으로 계산된 milliseconds단위의 시간 값을 가지고 있다.

**참고 항목**

setDate(Date dt), Date

#### getMode

public int getMode() DateFieldComponent에 설정된 모드를 얻어 온다.

**참고 항목**

setMode(int mode)

#### getTimeZone

public TimeZone getTimeZone() DateFieldComponent에 설정되어 있는 TimeZone을 얻어 온다. 기본적으로 설정된 TimeZone은 시스템의 기본 TimeZone이며, TimeZone.TimeZone.getDefault()를 통해 생성된다.

**반환 값**

DateFieldComponent에 설정된 TimeZone

**참고 항목**

setTimeZone(TimeZone tz), TimeZone

#### showNotify

protected void showNotify(boolean bShow) 이하 메소스 설명은 Component 클래스에서 복사되었음 화면의 내용이 보이면 호출된다. addComponent나 removeComponent에 의해서 불리거나, 자신의 맨 상위의 부모 컴포넌트(ShellComponent)가 show에 의해서 화면에 나타날 때 호출된다. Overrides showNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `bShow` - 컴포넌트가 나타나는지 안 나타나는지 여부 setDate
- `public` - void setDate(Date dt)
- `DateFieldComponent에` - Date를 설정한다. 인자 값이 null인 경우
- `NullPointerException이` - 발생한다. 기본적으로 설정된 Date는 1970/1/00:00:00 GMT 를 기준으로 계산된 milliseconds단위의 시간 값을 가지고 있다.

**매개 변수**

- `dt` - DateFieldComponent에 설정할 Date객체 Throws
- `NullPointerException` - Date가 null인 경우

**참고 항목**

getDate(), Date

#### setMode

public void setMode(int mode) DateFieldComponent의 모드를 설정한다. 설정 가능한 값은 MODE_TIME, MODE_DATE, MODE_TIME_DATE이며, 이외의 값을 설정한 경우 IllegalArgumentException이 발생한다.

**매개 변수**

- `mode` - DateFieldComponent에 설정할 모드 Throws
- `IllegalArgumentException` - 지정된 모드 외의 값이 인자로 주어진 경우

**참고 항목**

getMode(), MODE_TIME, MODE_DATE, MODE_TIME_DATE

#### setTimeZone

public void setTimeZone(TimeZone tz) DateFieldComponent의 TimeZone을 설정한다. 기본적으로 설정된 TimeZone은 시스템의 기본 TimeZone이며, TimeZone.TimeZone.getDefault()를 통해 생성된다.

**매개 변수**

- `tz` - DateFieldComponent에 설정할 TimeZone Throws
- `NullPointerException` - TimeZone이 null인 경우

**참고 항목**

getTimeZone(), TimeZone

#### getPreferredHeight

public int getPreferredHeight(int w) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. 지정된 제한된 폭을 가질 경우의 컴포넌트의 높이를 돌려준다. 만일 LabelComponent 나 TextFieldComponent, TextAreaComponent와 같이 포맷팅이 가능한 컴포넌트인 경우에는 가변 폭을 가질 수가 있다. 가변 폭을 가지게 되면, 폭에 따라서 높이가 달라지게 된다. 이때 이 함수를 통해서 컴포넌트의 높이를 얻어 온다. 만일, w가 -1이 면 폭에 제한이 없는 것으로 계산된다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `w` - 가변 폭.

**반환 값**

컴포넌트의 높이. getPreferredHeight public int getPreferredHeight() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. ContainerComponent에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 높이 getPreferredWidth public int getPreferredWidth() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 폭을 결정한다. Container에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredWidth in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 폭. paintContent public void paintContent(Graphics g) 이하 메소스 설명은 Component 클래스에서 복사되었음 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides paintContent in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics

#### keyNotify

public boolean keyNotify(int type, int key) 이하 메소스 설명은 Component 클래스에서 복사되었음 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력값이 된다. Overrides keyNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. getStringValue public String getStringValue(int mode) 인자로 주어진 모드값에 따라 날짜나 시간 값을 스트링 형태로 얻어 온다. 각 모드에 따라 반환되는 형태는 다음과 같다. MODE_DATE Mon, 10 Dec 2001 MODE_TIME 03 : 28 ( am ) MODE_TINE_DATE Mon, 10 Dec 2001 03 : 28 ( am )

**매개 변수**

- `mode` - DateFieldComponent의 모드

**반환 값**

모드에 맞는 날짜/시간 값의 스트링 형태. Throws IllegalArgumentException 잘못된 모드값을 지정한 경우 Class DialogComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.ContainerComponent | +--org.kwis.msp.lwc.ShellComponent | +--org.kwis.msp.lwc.DialogComponent public class DialogComponent extends ShellComponent DialogComponent는 다양한 형태의 다이얼로그박스를 지원하기 위해서 만들어진 컴포넌트이다. 기본적으로 DialogComponent는 타이틀영역과 데이타 영역, 버튼영역으로 구성되어있다. 타이틀영역을 다이얼로그박스의 타이틀이 존재하는 경우 타이틀을 출력해주는 영역이고, 데이타 영역을 사용자에 의해서 추가된 여러 형태의 컴포넌트를 출력해주는 영역이며, 버튼영역은 각 타입에 따라 사용되는 버튼을 출력해주는 영역이다. 각 영역의 위치는 변경할 수 없으며, 단지 각 영역의 문자 데이타나 컴포넌트만을 변경할 수 있다. DialogCompoent의 데이타 영역에는 한 개의 Component만을 추가 할 수 있다. 따라서 여러 개의 Component를 가지는 다이얼로그를 만들려면 ContainerComponent를 활용하여 데이타 영역에 추가한다. DialogComponent에서는 기본적으로 3가지 타입을 지원하고 있다. 확인기능을 제공하는 TYPE_OK타입과 확인과 취소기능을 제공하는 TYPE_OK_CANCEL 타입, 일정 시간 동안 화면에 데이타를 출력해주는 기능을 제공하는 TYPE_NONE이다. TYPE_NONE의 경우 기본적으로 화면에 출력되는 시간은 3초이며, 이 시간값을 setTimeout(int)메소드를 통해서 사용자가 지정할 수 있다. 타입이 TYPE_NONE인 경우 TIMEOUT_INFINITE값을 timeout값으로 지정하면 TYPE_OK로 타입이 변경된다. 타입값이 잘못 지정된 경우, 즉 TYPE_NONE,TYPE_OK,TYPE_OK_CANCEL이외의 값이 지정된 경우, IllegalArgumentException발생된다. Fields inherited from class org.kwis.msp.lwc.ShellComponent cd, cmpCommand, cmpTitle, cmpWork, RESIZE_MASK Fields inherited from class org.kwis.msp.lwc.ContainerComponent cmpFocus, cmps, insetBottom, insetLeft, insetRight, insetTop, ncomp, offsetX, offsetY, useFrame Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.ShellComponent addComponent, addComponent, configure, getCard, getCommand, getNextTraversalComponent, getPrevTraversalComponent, getTitle, getWorkComponent, getX, getY, grabKey, hide, isShown, keyNotify, processEvent, removeAllComponents, removeComponent, repaint, serviceRepaints, setCommand, setGrabKeyListener, setTitle, setTitle, setWorkComponent, showNotify, ungrabKey Methods inherited from class org.kwis.msp.lwc.ContainerComponent getComponent, getIndexOf, getNumberOfComponent, paint, removeComponent, repaint, scrollTo, setComponent, useFrame, validate Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, focusNotify, getBackground, getForeground, getHeight, getPreferredHeight, getPreferredHeight, getPreferredWidth, getWidth, getXOnScreen, getYOnScreen, hasFocus, invalidate, isValid, paintContent, pointerNotify, setBackground, setEventListener, setFocus, setForeground, toString Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 필드 상세 설명 TYPE_NONE public static final int TYPE_NONE 버튼이 없는 형태의 다이얼로그타입. 기본 화면 출력시간은 3초이고, '0'값이 지정되어 있다. TYPE_OK public static final int TYPE_OK OK 버튼만 있는 형태의 다이얼로그타입. '1'값이 지정되어 있다. TYPE_OK_CANCEL public static final int TYPE_OK_CANCEL OK, CANCEL 버튼이 있는 형태의 다이얼로그타입. '2'값이 지정되어 있다. DLG_TIMEOUT public static final int DLG_TIMEOUT doModal시 반환되는 값으로 TIMEOUT되어 종료된것을 나타냄. '10'값이 지정되어 있다. DLG_OK public static final int DLG_OK doModal시 반환되는 값으로 OK버튼이 선택되었음을 나타냄. '11'값이 지정되어 있다. DLG_CANCEL public static final int DLG_CANCEL doModal시 반환되는 값으로 CANCEL버튼이 선택되었음을 나타냄. '12'값이 지정되어 있다. OK_BUTTON public static final int OK_BUTTON OK 버튼타입. '20'이 지정되어 있다. CANCEL_BUTTON public static final int CANCEL_BUTTON CANCEL버튼타입. '21'이 지정되어 있다. TIMEOUT_INFINITE public static final int TIMEOUT_INFINITE timeout 값 중 무한대의 값을 나타냄. '-1'이 지정되어 있다. actionState protected int actionState 현재 어떤 액션(이벤트)이 발생한 것인지를 기억하는 필드. 버튼 액션이 발생한 경우 발생한 버튼의 값을 지정하고, 타임아웃 액션이 발생한 경우타임아웃 값을 지정한다. 액션이 발생하여 현재 값이 -2에서 다른 값으로 변경되는 경우 현재 DialogComponent의 doModal()을 종료하고 DialogComponent가 화면에서 제거된다. 생성자 상세 설명 DialogComponent public DialogComponent(int type) 데이타 컴포넌트와 타이틀이 없고 주어진 타입을 가지는 새로운 DialogComponent의 인스턴스를 생성한다. DialogComponent의 넓이와 높이는 DialogComponent에 추가된 컴포넌트의 넓이값과 높이값에 따라 자동으로 지정된다. 데이타의 넓이 값과 높이 값이 화면의 넓이값과 높이값을 초과한 경우 화면 넓이와 높이값을 사용한다. 타입값이 잘못 지정된 경우, 즉, TYPE_NONE,TYPE_OK,TYPE_OK_CANCEL이외의 값이 지정된 경우, IllegalArgumentException발생된다.

**매개 변수**

- `type` - 대화상자의 형태 Throws
- `IllegalArgumentException` - type이 TYPE_NONE, TYPE_OK,
- `TYPE_OK_CANCEL이외의` - 타입이 지정된 경 우 발생
- `IllegalArgumentException` - cmp가 이미 다른 부모 컴포넌트를 가지고 있 는 경우 발생

**참고 항목**

TYPE_NONE, TYPE_OK, TYPE_OK_CANCEL

#### DialogComponent

public DialogComponent(Component cmp, String title, int type) 새로운 DialogComponent의 인스턴스를 생성한다. DialogComponent의 넓이와 높이는 DialogComponent에 추가된 컴포넌트의 넓이값과 높이값에 따라 지정된다. 데이타의 넓이 값과 높이 값이 화면의 넓이값과 높이값을 초과한 경우 화면 넓이와 높이값을 사용한다. 타입값이 잘못 지정된 경우, 즉, TYPE_NONE,TYPE_OK,TYPE_OK_CANCEL이외의 값이 지정된 경우, IllegalArgumentException발생된다. 타이틀 영역에 지정될 컴포넌트와 데이타 영역에 지정될 컴포넌트는 모두 null이 될 수 있다.

**매개 변수**

- `cmp` - 대화상자의 내용을 담은 컴포넌트 혹은 null
- `title` - 대화상자의 타이틀 혹은 null
- `type` - 대화상자의 형태 Throws
- `IllegalArgumentException` - type이 TYPE_NONE, TYPE_OK, TYPE_OK_CANCEL 이외의 타입이 지정된 경우 발생
- `IllegalArgumentException` - cmp가 이미 다른 부모 컴포넌트를 가지고 있는 경우 발생

**참고 항목**

TYPE_NONE, TYPE_OK, TYPE_OK_CANCEL

#### DialogComponent

public DialogComponent(Component cmp, String ttl, int type, int x, int y,

```c
int w, int h)
새로운 DialogComponent의 인스턴스를 생성한다.
```

DialogComponent의 위치와 넓이,높이를 지정할 수 있으며, 지정한 값이 위치값이 '0'보다 작거나 크기값이 '0'이하의 값인 경우 IllegalArgumentException이 발생한다. 타입값이 잘못 지정된 경우, 즉, TYPE_NONE,TYPE_OK,TYPE_OK_CANCEL이외의 값이 지정된 경우, IllegalArgumentException발생된다. 타이틀 영역에 지정될 컴포넌트와 데이타 영역에 지정될 컴포넌트는 모두 null이 될 수 있다.

**매개 변수**

- `cmp` - 대화상자의 내용을 담은 컴포넌트 혹은 null
- `title` - 대화상자의 타이틀 혹은 null
- `type` - 대화상자의 형태. TYPE_NONE,TYPE_OK ,TYPE_OK_CANCEL 중에서 지정
- `x` - 대화상자의 x좌표
- `Y` - 대화상자의 y좌표
- `w` - 대화상자의 넓이값
- `h` - 대화상자의 높이값 Throws
- `IllegalArgumentException` - type이 TYPE_NONE, TYPE_OK, TYPE_OK_CANCEL 이외의 타입이 지정된 경우 발생
- `IllegalArgumentException` - x,y값이 '0'보다 작거나 w,h값이 '0'이하의 값이 경우 발생
- `IllegalArgumentException` - cmp가 이미 다른 부모 컴포넌트를 가지고 있는 경우 발생

**참고 항목**

TYPE_NONE, TYPE_OK, TYPE_OK_CANCEL 메쏘드 상세 설명

#### setButtonString

public void setButtonString(int buttonType, String buttonStr) 버튼의 문자를 지정한다. DialogComponent의 타입이 TYPE_NONE이 아닌 경우 각 타입에 따라 사용되는 버튼의 문자를 변경할 수 있다. 변경을 원하는 버튼의 타입과 버튼의 새로운 문자를 입력하여 변경하게 된다. 지정할 수 있는 버튼 타입은 OK_BUTTON과 CANCEL_BUTTON이며, 이외의 버튼 타입을 지정한 경우 IllegalArgumentException이 발생한다. 타입이 TYPE_NONE인 경우에는 아무런 일을 하지 않는다. setButtonString()으로 설정한 문자열에 의해 Button의 크기는 자동으로 변경된다. 단, 표시할 수 있는 영역보다 긴 문자열을 할당할 경우, 표시할 수 있는 최대 길이만 보여주고 나머지는 표시되지 않는다. setButtonString()으로 설정한 문자열에 의해 다른 Button의 출력에 지장이 생길 경우에도 표시할 수 있는 최대 길이만 보여준다.

**매개 변수**

- `buttonType` - 지정할 버튼타입. OK_BUTTON와 CANCEL_BUTTON지정.
- `buttonStr` - 버튼의 새로운 문자열 Throws
- `IllegalArgumentException` - 잘못된 버튼 타입을 지정한 경우 발생.

**참고 항목**

OK_BUTTON, CANCEL_BUTTON

#### setType

public void setType(int type) DialogComponent의 타입을 지정한다. 타입이 변경되면 현재 지정되어 있는 타임아웃 값이 각 타입에 따른 기본 타임아웃값으로 변경된다. TYPE_NONE의 기본 타임아웃 값은 3초이고, 그 외의 타입에 대한 기본값은 TIMEOUT_INFINITE이다. 타입값이 잘못 지정된 경우, 즉, TYPE_NONE,TYPE_OK,TYPE_OK_CANCEL이외의 값이 지정된 경우, IllegalArgumentException발생된다. 기본적으로 TYPE_OK와TYPE_OK_CANCEL는 사용자의 입력이 있을 때까지 화면에 보여주도록 되어있다. 따라서 일정 시간 후 화면에서 삭제되도록 하기를 원한다면 setTimeout(int)를 통해 그 시간값을 지정할 수 있다.

**매개 변수**

- `tp` - DialogComponent의 타입. Throws
- `IllegalArgumentException` - 타입값이 잘못 지정된 경우

**참고 항목**

setTimeout(int timeout), TYPE_NONE, TYPE_OK, TYPE_OK_CANCEL

#### setTimeout

public void setTimeout(int timeout) DialogComponent를 화면에 보여줄 타임아웃 시간을 지정한다. 이 값은 현재 타입에 대해서만 적용되며, 타입이 변경되면 타임아웃값도 각 타입에 맞는 기본값으로 변경된다. setType(int)을 참고하세요. 타임아웃 값의 단위는 milliseconds이다. 현재 타입이 TYPE_NONE인 경우 TIMEOUT_INFINITE값을 지정하면 현재의 타입이 TYPE_OK로 변경된다. 한번 지정된 timeout값은 타입이 변경되지 않은 상태에서 재 지정이 있을 때까지 계속 사용된다.

**매개 변수**

- `timeout` - 화면출력시간

**참고 항목**

getTimeout(), setType(int type)

#### getTimeout

public int getTimeout() 현재 설정되어 있는 타임아웃값을 얻어온다. 타임아웃 값의 단위는 milliseconds이다.

**반환 값**

현재 타임아웃값

**참고 항목**

setTimeout(int timeout)

#### doModal

public int doModal() DialogComponent를 화면에 나타나게 한다. 이 함수를 호출하면 다이얼로그가 화면에 출력되며 버튼이나 Timeout에 의한 액션이 발생한 경우 화면에서 제거된다. 이때 발생한 액션값을 반환한다.

**반환 값**

발생한 액션값 DLG_OK,DLG_CANCEL, DLG_TIMEOUT show public void show() 이하 메소스 설명은 ShellComponent 클래스에서 복사되었음 컴포넌트를 화면상에 보여준다. 컴포넌트를 화면상에 보여주기 전에 컴포넌트의 위치와 크기를 validate함수를 통해서 계산한다. Overrides show in class ShellComponent getActionState public int getActionState() DialogComponent에서 발생한 마지막 액션을 얻어온다.

**반환 값**

발생한 마지막 액션 layout public void layout() 이하 메소스 설명은 Component 클래스에서 복사되었음 하위 컴포넌트의 크기와 위치를 결정한다. Overrides layout in class ShellComponent paintFrame protected void paintFrame(Graphics g) 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 useFrame의 인수를true으로 호출하는 경우에 화면을 그릴 때 호출된다. Overrides paintFrame in class ContainerComponent Following copied from class: org.kwis.msp.lwc.ContainerComponent

**매개 변수**

- `g` - 그릴 그래픽 개체
- `Class` - FormComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.ContainerComponent | +--org.kwis.msp.lwc.FormComponent
- `Direct` - Known Subclasses: ListComponent
- `public` - class FormComponent extends ContainerComponent 다양한 컴포넌트를 일렬로 배열하여 화면을 구성하는 컴포넌트. FormComponent는
- `ContainerComponent를` - 확장하여 자식 컴포넌트로서 다양한 컴포넌트를 담아서 화면을 구성하는 컴포넌트이다. 또한 각 컴포넌트들의 배치와 스크롤 여부를 관리한다. 자식 컴포넌트들이 포커스 이동은 상하만 동작하도록 되어 있다. UP/DOWN키를 사용하여 자식 컴포넌트들의 포커스 이동을 할 수 있다. 내부의 컴포넌트가 많으면 자동적으로 scrollbar가 생성되도록 되어 있다.
- `FormComponent의` - 내부에 FormComponent가 추가될 경우 내부 FormComponent에는
- `ScrollBar가` - 생성되지 않는다.
- `Fields` - inherited from class org.kwis.msp.lwc.ContainerComponent cmpFocus, cmps, insetBottom, insetLeft, insetRight, insetTop, ncomp, offsetX, offsetY, useFrame
- `Fields` - inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y
- `Methods` - inherited from class org.kwis.msp.lwc.ContainerComponent addComponent, addComponent, getComponent, getIndexOf, getNumberOfComponent, paintFrame, processEvent, removeAllComponents, removeComponent, removeComponent, repaint, repaint, setComponent, useFrame, validate
- `Methods` - inherited from class org.kwis.msp.lwc.Component canHandleInput, configure, getBackground, getCard, getForeground, getHeight, getPreferredHeight, getPreferredHeight, getPreferredWidth, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, paintContent, pointerNotify, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명 FormComponent
- `public` - FormComponent() 폼 컴포넌트를 생성한다. FormComponent
- `public` - FormComponent(boolean bVertical) 수직형 혹은 수평형 폼 컴포넌트를 생성한다. bVertical 이 true면 수직으로 컴포넌트를 정렬하며, 반대로 false이면 수평으로 컴포넌트를 정렬한다.

**매개 변수**

- `bVertical` - 수평으로 정렬할지 수직으로 정렬할지 여부 메쏘드 상세 설명 setPacked
- `public` - void setPacked(boolean b) 폼의 내부의 컴포넌트의 폭을 폼의 폭으로 맞출 것인지 여부를 지정한다.

**매개 변수**

- `b` - 폭에 맞추면 true, 그렇지 않으면 false getPacked
- `public` - boolean getPacked() 자식 컴포넌트의 폭을 맞출 것인지 여부를 돌려준다.

**반환 값**

폭에 맞추는지 여부 setGab public void setGab(int gab) 컴포넌트 간의 간격을 결정한다.

**매개 변수**

- `gab` - 컴포넌트 간의 간격 getGab
- `public` - int getGab() 컴포넌트 간의 간격을 돌려준다.

**반환 값**

컴포넌트 간의 간격 focusNotify public void focusNotify(boolean b) 이하 메소스 설명은 Component 클래스에서 복사되었음 포커스를 받으면 호출된다. 컴포넌트가 포커스를 가지거나 가지고 있지 않음을 보여주기 위해서 repaint함수를 호출하여, 다시 자기 자신을 그리도록 한다. Overrides focusNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `b` - 포커스를 가질 땐 true가 넘어오고, 가지지 않을 땐 false keyNotify
- `protected` - boolean keyNotify(int type, int key) 이하 메소스 설명은 Component 클래스에서 복사되었음 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력값이 된다. Overrides
- `keyNotify` - in class ContainerComponent
- `Following` - copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. calcPreferredSize protected void calcPreferredSize(int cw) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 크기를 계산한다. Overrides calcPreferredSize in class Component layout public void layout() 이하 메소스 설명은 Component 클래스에서 복사되었음 하위 컴포넌트의 크기와 위치를 결정한다. Overrides layout in class Component paint public void paint(Graphics g) 그래픽스 g를 가지고 컨테이너 컴포넌트를 그린다. 이때 컨테이너 컴포넌트는 자식 컴포넌트의 paintContent함수를 이용하여 자식 컴포넌트 까지 그려준다. Overrides paint in class ContainerComponent

**매개 변수**

- `g` - 컴포넌트를 그릴 그래픽스 개체 getNextTraversalComponent
- `protected` - Component getNextTraversalComponent() 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 포커스 가질 수 있는 다음 컴포넌트를 돌려준다. 포커스를 가질 수 있는 다음 컴포넌트를 돌려준다. 돌려지는 컴포넌트는 현재 컴포넌트의 자식 컴포넌트 중 하나가 된다. 만일 포커스를 가질 수 있는 컴포넌트가 없는 경우에는 null을 돌려준다. Overrides
- `getNextTraversalComponent` - in class ContainerComponent
- `Following` - copied from class: org.kwis.msp.lwc.ContainerComponent

**반환 값**

포커스를 가질 수 있는 다음 컴포넌트 getPrevTraversalComponent protected Component getPrevTraversalComponent() 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 포커스 가질 수 있는 이전 컴포넌트를 돌려준다. 포커스를 가질 수 있는 다음 컴포넌트를 돌려준다. 돌려지는 컴포넌트는 현재 컴포넌트의 자식 컴포넌트 중 하나가 된다. 만일 포커스를 가질 수 있는 컴포넌트가 없는 경우에는 null을 돌려준다. Overrides getPrevTraversalComponent in class ContainerComponent Following copied from class: org.kwis.msp.lwc.ContainerComponent

**반환 값**

포커스를 가질 수 있는 이전 컴포넌트 scrollTo protected boolean scrollTo(int dx, int dy) 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 특정 위치로 화면을 이동한다. dx, dy가 가리키는 오프셋(offset)값을 가지도록 스크롤한다. 만일 값이 처리할 수 없는 값이라면, 상위 컴포넌트의 scrollTo를 호출한다. Overrides scrollTo in class ContainerComponent Following copied from class: org.kwis.msp.lwc.ContainerComponent

**매개 변수**

- `dx` - x축으로의 이동할 거리
- `dy` - y축으로의 이동할 거리

**반환 값**

제대로 스크롤되는 경우 true, 그렇지 않으면 false Class ImageComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.ImageComponent public class ImageComponent extends Component ImageComponent는 이미지데이타를 지정한 정렬형태로 화면에 출력하는 클래스 이다. ImageComponent는 setLayout(int)를 사용하여 정렬형태를 지정 할 수 있다. ImageComponent에서 제공하고 있는 정렬형태는 Component.LAYOUT_LEFT와 Component.LAYOUT_RIGHT, Component.LAYOUT_HCENTER,Component.LAYOUT_TOP, Component.LAYOUT_BOTTOM,Component.LAYOUT_HCENTER이다. 정렬 조합 규칙을 참고하여 각 정렬형태를 조합할 수 있다. ImageComponent생성시 정렬 형태는 LAYOUT_LEFT|LAYOUT_TOP로 초기화 된다.

**참고 항목**

Image Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, configure, focusNotify, getBackground, getCard, getForeground, getHeight, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, keyNotify, layout, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, toString, validate Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 필드 상세 설명

#### imgStr

protected String imgStr 이미지 리소스

#### img

protected Image img 이미지 생성자 상세 설명

#### ImageComponent

public ImageComponent() 새로운 ImageComponent의 인스턴스를 생성한다. 이미지 데이타는 null로 초기화 된다.

#### ImageComponent

public ImageComponent(Image img) 새로운 ImageComponent의 인스턴스를 생성한다. img에 null을 지정할 수 있다.

**매개 변수**

- `img` - 초기값으로 사용할 이미지 혹은 null ImageComponent
- `public` - ImageComponent(String str) 새로운 ImageComponent의 인스턴스를 생성한다. 생성시 주어인 이미지의 리소스
- `str를` - 가지고 이미지를 생성하게 된다.

**매개 변수**

- `str` - 초기값으로 사용할 이미지의 리소스 혹은 null 메쏘드 상세 설명 setImage
- `public` - void setImage(Image img)
- `ImageComponent에` - 이미지를 설정한다. 이미 설정된 이미지가 존재하면 주어진 새로운 이미지로 재 설정한다. 변경된 후 자동적으로 repaint가 된다. img가 null이면 설정된 이미지가 삭제 된다.

**매개 변수**

- `img` - 설정할 이미지 getImage
- `public` - Image getImage()
- `ImageComponent에` - 설정된 이미지를 얻어온다.

**반환 값**

설정된 이미지 setImage public void setImage(String str) ImageComponent에 주어진 이미지 리소스 경로명을 가지고 이미지를 생성하여 설정한다. String가 null인 경우 기존 이미지를 삭제한다. 이외에 경로명이 올바르지 못한 경우, IllegalArgumentException 이 발생한다..

**매개 변수**

- `str` - 설정할 이미지의 리소스 Throws
- `IllegalArgumentException` - 이미지 리소스 경로명이 null이거나 올바르지 못한 경우 setLayout
- `public` - void setLayout(int layout) 이미지의 정렬형태를 설정한다. 기본적으로 설정되어 있는 정렬형태는 Component.LAYOUT_LEFT이다. ImageComponent에서 사용되는 정렬형태는 Component.LAYOUT_LEFT와 Component.LAYOUT_RIGHT, Component.LAYOUT_TOP, Component.LAYOUT_BOTTOM Component.LAYOUT_HCENTER, Component.LAYOUT_VCENTER이다. 이 정렬 값은
- `Component에서` - 참조하고 있다.

**매개 변수**

- `type` - Layout Type값.

**참고 항목**

Component.LAYOUT_LEFT, Component.LAYOUT_RIGHT, Component.LAYOUT_HCENTER, Component.LAYOUT_TOP, Component.LAYOUT_BOTTOM, Component.LAYOUT_VCENTER

#### getPreferredHeight

public int getPreferredHeight(int w) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. 지정된 제한된 폭을 가질 경우의 컴포넌트의 높이를 돌려준다. 만일 LabelComponent 나 TextFieldComponent, TextAreaComponent와 같이 포맷팅이 가능한 컴포넌트인 경우에는 가변 폭을 가질 수가 있다. 가변 폭을 가지게 되면, 폭에 따라서 높이가 달라지게 된다. 이때 이 함수를 통해서 컴포넌트의 높이를 얻어 온다. 만일, w가 -1이 면 폭에 제한이 없는 것으로 계산된다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `w` - 가변폭.

**반환 값**

컴포넌트의 높이. getPreferredHeight public int getPreferredHeight() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. ContainerComponent에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 높이 getPreferredWidth public int getPreferredWidth() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 폭을 결정한다. Container에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredWidth in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 폭. paintContent public void paintContent(Graphics g) 이하 메소스 설명은 Component 클래스에서 복사되었음 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides paintContent in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics

#### showNotify

protected void showNotify(boolean bShow) 이하 메소스 설명은 Component 클래스에서 복사되었음 화면의 내용이 보이면 호출된다. addComponent나 removeComponent에 의해서 불리거나, 자신의 맨 상위의 부모 컴포넌트(ShellComponent)가 show에 의해서 화면에 나타날 때 호출된다. Overrides showNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `bShow` - 컴포넌트가 나타나는지 안 나타나는지 여부 play
- `public` - void play() 이미지가 애니메이션 이미지인 경우에 애니메이션을 시작한다. stop
- `public` - void stop() 이미지가 애니메이션 이미지인 경우에 애니메이션을 멈춘다.
- `Class` - LabelComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.LabelComponent
- `Direct` - Known Subclasses: CheckboxComponent, ListItemComponent
- `public` - class LabelComponent extends Component 문자열을 보여주는 컴포넌트 이다. 사용자에게 보여줄 때 문자열과 이미지를 포맷팅 해서 출력해 준다. LabelComponent는 setLayout(int)를 사용하여 정렬형태를 지정 할 수 있다. LabelComponent에서 사용되는 정렬형태는 Component에서 제공하는 정렬 조합 규칙을 참조하고 있다. LabelComponent생성시 기본 정렬 형태는 LAYOUT_LEFT이다. 문자열이나 이미지는 null이 될 수도 있다.
- `Fields` - inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y
- `Methods` - inherited from class org.kwis.msp.lwc.Component canHandleInput, configure, focusNotify, getBackground, getCard, getForeground, getHeight, getPreferredHeight, getPreferredHeight, getPreferredWidth, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, isShown, isValid, keyNotify, layout, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString, validate
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 필드 상세 설명 layout
- `protected` - int layout
- `LabelComoponent의` - 정렬형태. 기본 정렬형태는 Component.LAYOUT_LEFT이다. m_ft
- `protected` - Font m_ft 문자 데이타에서 사용하는 폰트 m_str
- `protected` - String m_str 문자 데이타 m_image
- `protected` - Image m_image 이미지 데이타 생성자 상세 설명 LabelComponent
- `public` - LabelComponent() 레이블 컴포넌트를 생성한다. 문자열과 이미지는 모두 null로 지정되며, 기본 정렬형태는 LAYOUT_LEFT이다. LabelComponent
- `public` - LabelComponent(String str) 주어진 문자열로 레이블 컴포넌트를 생성한다. 이미지 데이타는 null로 지정된다. 문자열 데이타는 null값이 될 수 있다. 기본 정렬형태는 LAYOUT_LEFT이다.

**매개 변수**

- `str` - 레이블 컴포넌트가 보여줄 문자열 혹은 null LabelComponent
- `public` - LabelComponent(String str, Image img) 주어진 문자열과 이미지 데이타로 레이블 컴포넌트를 생성한다. 문자열과 이미지데이타는 모두 null이 될 수 있으며, 기본 정렬형태는 LAYOUT_LEFT이다.

**매개 변수**

- `str` - 레이블 컴포넌트가 보여줄 문자열 혹은 null
- `img` - 이미지 혹은 null LabelComponent
- `public` - LabelComponent(String str, String imgString) 주어진 문자열과 지정한 자원에서 읽어 들이는 이미지 데이타로 레이블 컴포넌트를 생성한다. 문자열과 이미지데이타는 모두 null이 될 수 있으며, 기본 정렬형태는 LAYOUT_LEFT이다.

**매개 변수**

- `str` - 레이블 컴포넌트가 보여줄 문자열 혹은 null
- `imgString` - 이미지 자원의 경로명을 나타내는 문자열 혹은 null 메쏘드 상세 설명 invalidate
- `public` - void invalidate() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트가 유효한 좌표와 크기를 가지 않음을 알려준다. Overrides
- `invalidate` - in class Component setLabel
- `public` - void setLabel(String str) 내부 문자열을 주어진 문자열값으로 지정한다. 현재 문자열 데이터를 null로 지정할 수 있다

**매개 변수**

- `str` - 변경할 문자열 혹은 null setImage
- `public` - void setImage(Image img) 내부 이미지를 주어진 이미지로 지정한다. 현재의 이미지 데이타를 null로 지정할 수 있다

**매개 변수**

- `img` - 변경할 이미지 혹은 null getLabel
- `public` - String getLabel() 내부 문자열을 가져온다.

**반환 값**

내부 출력 문자열 getImage public Image getImage() 내부 이미지를 가져온다.

**반환 값**

내부 출력 이미지 setFont public void setFont(Font font) 폰트를 지정한다. 기본적으로 폰트는 Font.getDefaultFont()를 통해 설정되어 있다.

**매개 변수**

- `font` - 사용자 폰트 getFont
- `public` - Font getFont() 폰트를 얻어온다. 기본적으로 폰트는 Font.getDefaultFont()를 통해 설정되어 있다

**반환 값**

설정된 폰트 calcPreferredSize protected void calcPreferredSize(int cw) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 크기를 계산한다. Overrides calcPreferredSize in class Component paintContent public void paintContent(Graphics g) 이하 메소스 설명은 Component 클래스에서 복사되었음 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides paintContent in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics

#### setLayout

public void setLayout(int layout) 레이블의 정렬 형태를 지정한다. LabelComponent에서 사용되는 정렬형태는 Component에서 제공하는 정렬 조합 규칙을 참조하고 있으며, 정의된 정렬 형태 외의 값을 지정한 경우 IllegalArgumentException이 발생한다.

**매개 변수**

- `type` - 정렬 형태 Throws
- `IllegalArgumentException` - 컴포넌트에 정의된 정렬 형태 외의 값을 지정한 경우 발생

**참고 항목**

Component.LAYOUT_LEFT, Component.LAYOUT_RIGHT Component.LAYOUT_HCENTER, Component.LAYOUT_TOP Component#LYAOUT_VCENTER, Component.LAYOUT_BOTTOM Class ListComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.ContainerComponent | +--org.kwis.msp.lwc.FormComponent | +--org.kwis.msp.lwc.ListComponent public class ListComponent extends FormComponent ListComponent는 FormComponent를 상속하여 구현된 클래스이다. 이 다른 ContainerComponent와는 달리 ListItemComponent만을 추가할 수 있고, 그 순서에 따라 각 아이템들이 화면에 출력된다. ListItemComponent는 3가지 타입이 있다. * 현재 포커스를 받고 있는 아이템이 선택된 상태와 같게 되는 타입인 SELECT_IMPLICIT, 여러 아이템을 선택할 수 있는 SELECT_MULTIPLE, 한 아이템만 선택할 수 있는 SELECT_EXCLUSIVE이다. 이때 SELECT_MULTIPLE,SELECT_EXCLUSIVE의 경우에는 포커스를 가지는 아이템과 선택된 아이템이 반드시 일치하지는 않는다. 추가된 ListItemComponent를 SELECT키 입력에 의해서 선택하거나 번호에 해당 위치에 대한 숫자키 입력을 받은 경우 ActionListener를 등록하여 선택 액션에 대한 감지를 할 수 있고, 방향키 입력에 의해 선택된 아이템이 변경된 경우 이것을 알 수 있도록 ChangeListener를 등록 할 수 있는 기능을 제공하고 있다. 기본적으로 ListComponent를 사용하면 번호 이미지가 출력된다. 번호 이미지에 대한 제어는 #controlNumberImage(boolean showImage)에서 담당 하고 있으며, true값을 지정한 경우 번호이미지가 화면에 출력되고, false값을 지정한 경우 번호이미지가 출력되지 않는다.

**참고 항목**

ListItemComponent, ActionListener, ChangeListener Fields inherited from class org.kwis.msp.lwc.ContainerComponent cmpFocus, cmps, insetBottom, insetLeft, insetRight, insetTop, ncomp, offsetX, offsetY, useFrame Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.FormComponent calcPreferredSize, focusNotify, getGab, getPacked, layout, ../../../../com/aroma/qtp/lwc/FormComponent.html - layoutChildHorizontal()scrollTo, ../../../../com/aroma/qtp/lwc/FormComponent.html - setFocus(com.aroma.qtp.lwc.Component)setGab, setPacked Methods inherited from class org.kwis.msp.lwc.ContainerComponent getComponent, getIndexOf, getNumberOfComponent, paintFrame, processEvent, removeAllComponents, removeComponent, removeComponent, repaint, repaint, useFrame, validate Methods inherited from class org.kwis.msp.lwc.Component canHandleInput, configure, getBackground, getCard, getForeground, getHeight, getPreferredHeight, getPreferredHeight, getPreferredWidth, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, paintContent, pointerNotify, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 필드 상세 설명

#### SELECT_IMPLICIT

public static final int SELECT_IMPLICIT ListComponent에 포커스를 가지는 경우에 현재 포커스 된 아이템과 선택된 아이템이 동일한 타입. 따라서 하나의 아이템만 선택된다.

#### SELECT_EXCLUSIVE

public static final int SELECT_EXCLUSIVE 단 하나의 아이템만 선택할 수 있는 타입. 현재 포커스 된 아이템과 선택된 아이템이 반드시 일치하지는 않는다.

#### SELECT_MULTIPLE

public static final int SELECT_MULTIPLE 여러 개의 아이템을 선택할 수 있는 타입. 현재 포커스 된 아이템이 반드시 선택된 경우는 아니다. 생성자 상세 설명

#### ListComponent

public ListComponent(int type) 아이템을 포함하지 않은 사이즈가 '0'인 ListComponent의 인스턴스를 주어진 타입으로 생성한다. ListComponent에서 지원하는 SELECT_IMPLICIT ,SELECT_EXCLUSIVE,SELECT_MULTIPLE외의 타입값이 지정된 경우 IllegalArgumentException이 발생한다.

**매개 변수**

- `type` - ListComponent의 타입 Throws
- `IllegalArgumentException` - 타입이 잘못 지정된 경우 발생

**참고 항목**

ListComponent() 메쏘드 상세 설명

#### append

public int append(String str, Image img) ListComponent에 주어진 이미지 데이타와 문자데이타로 ListItemComponent를 생성하여 추가한다. 문자 데이타와 이미지 데이타는 모두 null이 될 수 있다.

**매개 변수**

- `str` - ListItemComponent의 문자데이타 혹은 null
- `img` - ListItemComponent의 이미지데이타 혹은 null

**반환 값**

새로운 엘리먼트 추가 후 그 아이템의 인덱스값. addComponent public void addComponent(int index, Component cmp) index위치에 컴포넌트를 하나 추가한다. 추가하고자 하는 컴포넌트가 ListItemComponent이 아닌 경우 IllegalArgumentException이 발생한다. cmp가 null인 경우 NullPointerException이 발생한다. 또한 cmp가 이미 다른 부모 컴포넌트를 가지는 경우 IllegalArgumentException이 발생 한다. index값이 '0'보다 작거나 ListComponent에 추가된 아이템의 개수보다 큰 경우 IndexOutOfBoundsException이 발생한다. Overrides addComponent in class ContainerComponent

**매개 변수**

- `index` - 새로운 컴포넌트를 추가할 위치.
- `cmp` - 새로 추가할 컴포넌트. Throws
- `IllegalArgumentException` - 새로 추가할 컴포넌트가 ListItemComponent이 아닌 경우 발생.
- `IllegalArgumentException` - cmp가 이미 다른 부모 컴포넌트를 가지고 있는 경우 발생
- `IndexOutOfBoundsException` - index가 유효한 영역을 벗어나 있는 경우
- `NullPointerException` - cmp이 null인 경우

**참고 항목**

addComponent(Component cmp), setComponent(int index, Component cmp)

#### addComponent

public int addComponent(Component cmp) 컴포넌트를 하나 추가한다.맨 위에 자식 컴포넌트를 추가한다. 추가하고자 하는 컴포넌트가 ListItemComponent이 아닌 경우 IllegalArgumentException이 발생한다. cmp가 null인 경우 NullPointerException이 발생한다. 또한 cmp가 이미 다른 부모 컴포넌트를 가지는 경우 IllegalArgumentException이 발생 한다. Overrides addComponent in class ContainerComponent

**매개 변수**

- `cmp` - 새로 추가할 컴포넌트.

**반환 값**

넣어진 위치 인덱스 Throws IllegalArgumentException 새로 추가할 컴포넌트가 ListItemComponent 이 아닌 경우 발생. IllegalArgumentException cmp가 이미 다른 부모 컴포넌트를 가지는 경우 NullPointerException cmp이 null인 경우

**참고 항목**

addComponent(int index, Component cmp), setComponent(int index, Component cmp)

#### setComponent

public void setComponent(int index, Component cmp) 자식 컴포넌트를 하나 대치한다. 지정한 인덱스의 컴포넌트를 주어진 컴포넌트로로 대치한다. index값이 '0'보다 작거나 ListComponent에 추가된 아이템의 개수보다 큰 경우 IndexOutOfBoundsException이 발생한다. 새로 지정하고자 하는 컴포넌트가 ListItemComponent이 아닌 경우 IllegalArgumentException이 발생한다. cmp가 null인 경우 NullPointerException이 발생한다. 또한 cmp가 이미 다른 부모 컴포넌트를 가지는 경우 IllegalArgumentException이 발생 한다. Overrides setComponent in class ContainerComponent

**매개 변수**

- `index` - 지정할 컴포넌트의 위치.
- `cmp` - 새로 지정할 컴포넌트. Throws
- `IllegalArgumentException` - 새로 지정할 컴포넌트가 ListItemComponent이 아닌 경우 발생
- `IllegalArgumentException` - cmp가 이미 다른 부모 컴포넌트를 가지는 경우 IndexOutOfBoundsException
- `index값이` - 유효하지 않은 값으로 지정 된 경우 발생
- `NullPointerException` - cmp이 null인 경우

**참고 항목**

addComponent(int index, Component cmp), addComponent(Component cmp)

#### insert

public int insert(int index, String str, Image img) 해당 위치에 주어진 문자데이타와 이미지 데이타로 ListItemComponent을 생성하여 추가한다. 인덱스값이 '0'보다 작거나 ListComponent에 추가된 엘리먼트의 개수보다 큰 경우 IndexOutOfBoundsException이 발생한다. 새로 지정하고자 하는 컴포넌트가 ListItemComponent이 아닌 경우 IllegalArgumentException이 발생한다.

**매개 변수**

- `index` - 추가할 인덱스 값.
- `srt` - 추가할 문자 데이타.
- `img` - 문자 데이타와 함께 추가된 이미지 데이타.

**반환 값**

추가된 위치 인덱스 값. Throws IndexOutOfBoundsException 인덱스 값이 잘못 지정된 경우 IllegalArgumentException 새로 지정할 컴포넌트가 ListItemComponent이 아닌 경우 발생 IllegalArgumentException cmp가 이미 다른 부모 컴포넌트를 가지는 경우 IndexOutOfBoundsException index가 '0'보다 작거나 , 추가된 컴포넌트의 개수 보다 큰 경우 set public void set(int index, String str, Image img) 해당 위치에 주어진 문자데이타와 이미지 데이타로 ListItemComponent을 생성하여 새로 지정한다. 이미지 데이타와 문자 데이타는 null이 될 수 있으며, 인덱스값이 '0'보다 작거나 ListItemComponent에 추가된 엘리먼트의 개수 보다 큰 경우 IndexOutOfBoundsException이 발생한다.

**매개 변수**

- `index` - 인덱스 값.
- `srt` - 새로 지정할 문자 데이타.
- `img` - 문자 데이타와 함께 추가된 이미지 데이타. Throws
- `IndexOutOfBoundsException` - 인덱스 값이 잘못 지정된 경우 getString
- `public` - String getString(int index) 주어진 위치에 있는 ListItemComponent의 문자열 데이타를 얻어온다. 인덱스값이 '0'보다 작거나 ListItemComponent에 추가된 엘리먼트의 개수보다 크거나 같은 경우
- `IndexOutOfBoundsException이` - 발생한다.

**매개 변수**

- `index` - 원하는 엘리먼트의 인덱스

**반환 값**

주어진 index에 해당하는 엘리먼트의 문자열 Throws IndexOutOfBoundsException 인덱스 값이 잘못 지정된 경우 getImage public Image getImage(int index) 주어진 위치에 있는 ListItemComponent의 이미지 데이타를 얻어온다. 이미지가 존재하지 않는 경우 null을 반환한다. 인덱스값이 '0'보다 작거나 ListItemComponent에 추가된 엘리먼트의 수보다 크거나 같은 경우 IndexOutOfBoundsException이 발생한다.

**매개 변수**

- `index` - 원하는 엘리먼트의 인덱스

**반환 값**

주어진 index에 해당하는 엘리먼트의 이미지 Throws IndexOutOfBoundsException 인덱스 값이 잘못 지정된 경우 getSize public int getSize() ListComponent에 추가된 엘리먼트의 개수를 알려준다.

**반환 값**

ListComponent가 가지고 있는 엘리먼트들의 개수 isSelected public boolean isSelected(int index) 주어진 인덱스의 엘리먼트가 현재 선택되어 있는지의 여부를 알려준다. index가 ListComponent에 등록된 ListItemComponent의 인덱스 범위 - '0'보다 작거나 '전체 사이즈-1'보다 큰 값 - 를 벗어난 경우 IndexOutOfBoundsException이 발생한다.

**반환 값**

선택되어 있다면 true/ 선택되어 있지 않다면 false. Throws IndexOutOfBoundsException index가 범위('0'보다 작거나 '전체 사이즈- 1'보다 큰 값)를 벗어난 경우 getSelectedIndexs public int[] getSelectedIndexs() ListComponent의 엘리먼트들 중 현재 선택되어 있는 엘리먼트들의 인덱스를 얻어온다. 현재 선택된 엘리먼트가 없으면 null을 반환한다.

**반환 값**

현재 선택되어있는 엘리먼트들의 인덱스. 선택된것이 없는 경우 null을 반환한다. getSelectedIndex public int getSelectedIndex() ListComponent의 엘리먼트들 중 현재 선택되어 있는 엘리먼트의 인덱스를 얻어온다. 현재 선택된 엘리먼트가 없으면 '-1'을 반환한다.

**반환 값**

현재 선택되어있는 엘리먼트의 인덱스. 선택된것이 없는 경우 -1을 반환. setActionListener public void setActionListener(ActionListener l, Object o) ListComponent에 ActionListener를 등록한다. ListComponent내에 추가된 ListItemComponent들 중 한 아이템이 EventQueue.FIRE키 입력에 의해서 선택된 경우 등록된 ActionListener의 ActionListener.action(Component cmp, Object o)을 실행한다.

**매개 변수**

- `l` - ListComponent에 등록 할 ActionListener.
- `o` - ListComponent에 ActionListener와 함께 등록될 객체. setChangeListener
- `public` - void setChangeListener(ChangeListener l, Object o)
- `ListComponent에` - ChangeListener를 등록한다. ListComponent내에 추가된
- `ListItemComponent들의` - 선택상태가 변경된 경우 등록된 ChangeListener의 ChangeListener.changed(Component cmp, Object o)를 실행한다.

**매개 변수**

- `l` - ListComponent에 등록 할 ChangeListener.
- `o` - ListComponent에 ChangeListener와 함께 등록될 객체. keyNotify
- `protected` - boolean keyNotify(int type, int key) 이하 메소스 설명은 Component 클래스에서 복사되었음 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력값이 된다. Overrides
- `keyNotify` - in class FormComponent
- `Following` - copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. select public void select(int index) 주어진 위치의 엘리먼트를 선택한다. index값이 '-1'보다 작거나,전체 엘리먼트의 수보다 큰 경우 IndexOutOfBoundsException이 발생한다. '-1'값을 지정하면 선택된 엘리먼트가 없게 된다. 단, 현재 ListComponent의 타입이 SELEC_EXCLUSIVE인 경우에는 첫번째 아이템이 선택되게 된다.

**매개 변수**

- `index` - 새로 선택할 엘리먼트의 위치값. Throws
- `IndexOutOfBoundsException` - index가 유효한 영역을 벗어나 있는 경우 (index<-1 || index>(리스트 아이템의 전체 수)) select
- `public` - void select(ListItemComponent cmpp) 주어진 엘리먼트의 선택상태를 변경한다. 현재 ListComponent의 타입이 SELECT_IMPLICIT, SELECT_MULTIPLE의 경우에는 주어진 엘리먼트를 선택된 상태로 지정하고, SELECT_MULTIPLE의 경우 현재 주어진 엘리먼트의 상태가 선택된 상태의 경우에는 선택이 안된 상태로, 선택이 안된 상태의 경우에는 선택된 상태로 지정한다.

**매개 변수**

- `cmpp` - 새로 선택할 엘리먼트 controlNumber
- `public` - void controlNumber(boolean showImage) 번호키 컨트롤 여부를 지정한다. true값이 지정된 경우 번호가 화면에 출력되고(1~9,0까지), 숫자키에 의해 리스트항목을 선택이 가능하다. false값이 지정된 경우 번호를 출력하지 않으며, 숫자키에 의한 선택이 Disable된다. 기본적으로 지정된 상태는 true며, 화면에 번호가 출력된다. 이 값이 false로 설정된 경우 숫자키에 의한 선택이 Disable된다

**매개 변수**

- `useImage` - 번호이미지를 사용할 지의 여부. true / false

**참고 항목**

isControlNumber()

#### isControlNumber

public boolean isControlNumber() 번호키 컨트롤 상태를 반환한다.

**반환 값**

번호 컨트롤 상태

**참고 항목**

controlNumber(boolean)

#### paint

public void paint(Graphics g) Overrides paint in class FormComponent 그래픽스 g를 가지고 컨테이너 컴포넌트를 그린다. 이때 컨테이너 컴포넌트는 자식 컴포넌트의 paintContent함수를 이용하여 자식 컴포넌트 까지 그려준다.

**매개 변수**

- `g` - – 컴포넌트를 그릴 그래픽스 개체 getNextTraversalComponent
- `protected` - Component getNextTraversalComponent() 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 포커스 가질 수 있는 다음 컴포넌트를 돌려준다. 포커스를 가질 수 있는 다음 컴포넌트를 돌려준다. 돌려지는 컴포넌트는 현재 컴포넌트의 자식 컴포넌트 중 하나가 된다. 만일 포커스를 가질 수 있는 컴포넌트가 없는 경우에는 null을 돌려준다. Overrides
- `getNextTraversalComponent` - in class FormComponent
- `Following` - copied from class: org.kwis.msp.lwc.ContainerComponent

**반환 값**

포커스를 가질 수 있는 다음 컴포넌트 getPrevTraversalComponent protected Component getPrevTraversalComponent() 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 포커스 가질 수 있는 이전 컴포넌트를 돌려준다. 포커스를 가질 수 있는 다음 컴포넌트를 돌려준다. 돌려지는 컴포넌트는 현재 컴포넌트의 자식 컴포넌트 중 하나가 된다. 만일 포커스를 가질 수 있는 컴포넌트가 없는 경우에는 null을 돌려준다. Overrides getPrevTraversalComponent in class FormComponent Following copied from class: org.kwis.msp.lwc.ContainerComponent

**반환 값**

포커스를 가질 수 있는 이전 컴포넌트 Class ListItemComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.LabelComponent | +--org.kwis.msp.lwc.ListItemComponent public class ListItemComponent extends LabelComponent ListComponent에 추가되어 사용되는 ListItemComponent이다. 이 컴포넌트는 LabelComponent를 상속하여 구현된 클래스로 기본 기능은 LabelComponent와 유사한다. 반면 이 컴포넌트는 INPUT_MASK 를 가지고 있으므로 포커스와 입력을 받을 수 있다.

**참고 항목**

ListComponent Fields inherited from class org.kwis.msp.lwc.LabelComponent layout, m_ft, m_image, m_str Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.LabelComponent calcPreferredSize, getFont, getImage, getLabel, paintContent, setFont, setImage, setLabel, setLayout Methods inherited from class org.kwis.msp.lwc.Component canHandleInput, configure, focusNotify, getBackground, getCard, getForeground, getHeight, getPreferredHeight, getPreferredHeight, getPreferredWidth, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, keyNotify, layout, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString, validate Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명

#### ListItemComponent

public ListItemComponent(String str) 주어진 문자열로 ListItemComponent의 인스턴스를 생성한다. 이미지 데이타는 null로 지정된다. 문자열 데이타는 null값이 될 수 있다. 기본 정렬형태는 LAYOUT_LEFT이다.

**매개 변수**

- `str` - ListItemComponent가 보여줄 문자열 혹은 null ListItemComponent
- `public` - ListItemComponent(String str, Image img)
- `ListItemComponent의` - 인스턴스를 생성한다. 주어진 문자 데이타와 이미지 데이타로 새로운 ListItemComponent를 생성한다.

**매개 변수**

- `str` - ListItem의 문자 데이타 혹은 null
- `img` - ListItem의 이미지 데이타 혹은 null ListItemComponent
- `public` - ListItemComponent(String str, String imgString) 주어진 문자열과 지정한 자원에서 읽어 들이는 이미지 데이타로
- `ListItemComponent의` - 인스턴스를 생성한다. 문자열과 이미지데이타는 모두 null이 될 수 있으며, 기본 정렬형태는 LAYOUT_LEFT이다. 이때 이미지 경로명이 잘못 지정된 경우 이미지 데이타는 null이 된다.

**매개 변수**

- `str` - 레이블 컴포넌트가 보여줄 문자열 혹은 null
- `imgString` - 이미지 자원의 경로명을 나타내는 문자열 혹은 null 메쏘드 상세 설명 setState
- `public` - void setState(boolean bState)
- `ListItemComponent의` - 선택 상태를 지정한다.

**매개 변수**

- `bState` - 선택 시 true, 선택 해제 시 false getState
- `public` - boolean getState() 현재의 선택 상태를 얻어온다.

**반환 값**

선택된 상태면 true, 선택 안된 상태면 false Class ProgressComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.ProgressComponent public class ProgressComponent extends Component 프로그래스 컴포넌트는 진행상태 등을 나타내기 위해 사용하는 컴포넌트이다. Interactive NoneInteractive두 가지 모드가 있으며 생성시에 결정된다. Interactive의 경우 사용자의 키 입력을 받아 setStep에서 정의 된 값만큼 증가 혹은 감소하게 된다. NoneInteractive모드에서는 사용자의 입력은 받지 않으며 setValue에 의해 값이 변경 된다. 기본적으로 step값은 1로 되어 있으며 setStep함수를 사용하여 변경한다. ProgressComponent의 최소값은 0으로 고정되어 있으며 최대값만 변경할 수 있다. Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, configure, focusNotify, getBackground, getCard, getForeground, getHeight, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, layout, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString, validate Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명 ProgressComponent public ProgressComponent(boolean bInteractive, int max) 생성자함수 0을 최소값으로 하는 새로운 프로그래스 컴포넌트를 만든다.

**매개 변수**

- `bInteractive` - 사용자 입력을 받는 Progress 인지를 설정한다.
- `max` - 프로그래스의 최대값을 설정한다. 메쏘드 상세 설명 setStep
- `public` - void setStep(int step) 프로그래스 바의 증감 단위를 설정한다 Interactive인 경우 사용자의 입력에 의한 증가랑이므로 사용되며, setValue등에 의한 입력 시에도 주어진 단위 별로 증감이 된다. step값이 변경되는 경우 현재 값도 step단위로 변경된다. 기본값은 1이다.

**매개 변수**

- `nStep` - 증가랑. Throws
- `IllegalArgumentException` - step 값이 0이하거나 최대값보다 큰 경우

**참고 항목**

getStep()

#### getStep

public int getStep() 프로그래스바의 증감 단위를 구한다

**반환 값**

설정된 증가량.

**참고 항목**

#setStep()

#### setMargin

public void setMargin(int top, int bottom) 프로그래스바의 상하 여백을 설정한다(픽셀단위)

**참고 항목**

#setStep()

#### setMaxValue

public void setMaxValue(int maxValue) Progress의 최대 값을 설정한다. 만일 현재 값이 주어진 최대값보다 크다면 현재 값은 설정한 최대값으로 된다.

**매개 변수**

- `maxValue` - 설정할 최대값 Throws
- `IllegalArgumentException` - maxValue 값이 0이하인 경우 setValue
- `public` - int setValue(int value)
- `Progress의` - 현재 값을 설정한다. setStep에 의해 step이 설정된 경우 설정한 step 단위로 값이 변경된다. 결과값 = value - value % step의 방식으로 적용된다. value 가 0보다 작은 경우 0으로 설정되며 MAX 보다 큰 경우 MAX로 설정된다.

**매개 변수**

- `value` - 설정할 값

**반환 값**

설정된 값 getValue public int getValue() 프로그래스의 설정되어 있는 현재 값을 구하는 함수.

**반환 값**

설정되어 있는 현재 값 getMaxValue public int getMaxValue() 설정되어 있는 최대값을 구하는 함수.

**반환 값**

설정되어 있는 최대값 getPreferredHeight public int getPreferredHeight(int w) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. 지정된 제한된 폭을 가질 경우의 컴포넌트의 높이를 돌려준다. 만일 LabelComponent 나 TextFieldComponent, TextAreaComponent와 같이 포맷팅이 가능한 컴포넌트인 경우에는 가변 폭을 가질 수가 있다. 가변 폭을 가지게 되면, 폭에 따라서 높이가 달라지게 된다. 이때 이 함수를 통해서 컴포넌트의 높이를 얻어 온다. 만일, w가 -1이 면 폭에 제한이 없는 것으로 계산된다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `w` - 가변폭.

**반환 값**

컴포넌트의 높이. getPreferredHeight public int getPreferredHeight() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. ContainerComponent에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 높이 getPreferredWidth public int getPreferredWidth() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 폭을 결정한다. Container에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredWidth in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 폭. paintContent public void paintContent(Graphics g) 이하 메소스 설명은 Component 클래스에서 복사되었음 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides paintContent in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics

#### keyNotify

public boolean keyNotify(int type, int key) 이하 메소스 설명은 Component 클래스에서 복사되었음 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력값이 된다. Overrides keyNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. setChangeListener public void setChangeListener(ChangeListener listener, Object obj) ProgressComponent에 ChangeListener를 등록한다. ProgressComponent내에 값이 변경된 경우 등록된 ChangeListener의 ChangeListener.changed(Component cmp, Object o)를 실행한다.

**매개 변수**

- `l` - ListComponent에 등록 할 ChangeListener.
- `o` - ListComponent에 ChangeListener와 함께 등록될 객체.
- `Class` - ScrollbarComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.ScrollbarComponent
- `public` - class ScrollbarComponent extends Component
- `ScrollBarComponent는` - 최대,최소값을 가지고 그 영역 내에서 값을 유동적으로 변경할 수 있는 컴포넌트이다.
- `ScrollBarComponent에서는` - 좌우스크롤 HORIZONTAL과 상하스크롤 VERTICAL의 두 가지 스크롤 방향값을 제공한다. 이 값은 setDirection(int direction)을 통해서 지정할 수 있으며, HORIZONTAL과 VERTICAL 이외의 값이 지정된 경우
- `IllegalArgumentException이` - 발생한다. 스크롤 바의 값은 사용자의 키 입력에 따라 값이 변경될 수도 있으며
- `setCurrentValue등의` - 함수를 이용하여 값을 변경할 수도 있다. [그림 3-1-4-1] 스크롤바 값 설정 예시 예를 들어 [그림 3-1-4-1]과 같은 크기값을 갖는 ScrollbarComponent를 생성하려면 ScrollbarComponent(int direction, int currentValue, int viewAmount, int minimum, int maximum, int chAmount) 생성자를 사용하고, 아래와 같이 지정한다.
- `scrollBar` - = new ScrollbarComponent(HORIZONTAL, 0, 30, 0, 100,10); [그림 3-1-4-2] 스크롤바 현재값의 최대치 설정 예시 값을 지정할 때 주의할 점은 [그림 3-1-4-2]에서 보듯이 현재 위치값을 지정할 수 있는 최대값은 스크롤바의 최대값이 아니고, 스크롤바의 최대값에서 영역값을 뺀 값이 현재 위치값의 최대값으로 지정될 수 있다. 스크롤바의 각 크기값은 아래의 표를 참고하시기 바란다. <표 3-1-4-1> 스크롤 크기값 설명 기본값 영역 스크롤 방향. VERTICAL와
- `HORIZONTAL값을` - VERTICAL 방향값(direction) VERTICAL 지정할 수 있고 이외의 값이 HORIZONTAL 지정된 경우 IllegalArgumentException발생 현재 ScrollbarComponent의 위치값. 주의 할 점은 현재값이 실질적으로 지정될 수 있는 최소값(minimum)<=현재값(currentValue)<=(최대값(maximum)- 현재값(currentValue) 0 영역은 영역값(viewAmount)) 최대값이 아니고, 최대값과 영역값의 차이 값은 최대값으로 가질 수 있다. ScrollbarComponent에서 0 < 영역값(viewAmount) <= (최대값(maximum) - 영역값(viewAmount) 전체 영역 중 현재 1 최소값(minimum)) 사용되는 영역의 크기값. ScrollbarComponent의 최소값(minimum) 0 최소(minimum)값<최대값(maximum) 최소값 ScrollbarComponent의 최대값(maximum) 10 최소(minimum)값<최대값(maximum) 최대값 ScrollbarComponent에서 방향키 입력과 같은 이동 증감값(chAmount) 액션이 1 0 < 증감값(chAmount) <= 영역값(viewAmount) 발생하면 스크롤바가 움직이는 크기값.
- `Fields` - inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y
- `Methods` - inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, configure, getBackground, getCard, getForeground, getHeight, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, layout, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString, validate
- `Methods` - inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 필드 상세 설명 HORIZONTAL
- `public` - static final int HORIZONTAL 좌우 스크롤 방향값. '1'값이 지정되어 있다. VERTICAL
- `public` - static final int VERTICAL 상하 스크롤 방향값. '2'값이 지정되어 있다. 생성자 상세 설명 ScrollbarComponent
- `public` - ScrollbarComponent() 스크롤 바의 인스턴스를 생성한다. 기본값으로 상하 스크롤 방향값인 VERTICAL를 지정하고, ScrollbarComponent의 각 크기값들은 최소값으로 '0'이 지정되고, 최대값은 '10'으로 지정한다. 시작 위치 값은 '0'이고, 영역값은 '1',증감값은 '1'로 지정 한다.

**참고 항목**

ScrollbarComponent(int direction) ScrollbarComponent(int direction, int currentValue, int viewAmount, int minimum, int maximum, int chAmount)

#### ScrollbarComponent

public ScrollbarComponent(int direction) 지정한 스크롤 바의 방향값으로 스크롤 바의 인스턴스를 생성한다. 지정할 수 있는 스크롤 방향값은 HORIZONTAL과VERTICAL이며, 이외의 값으로 지정된 경우 IllegalArgumentException이 발생 한다. ScrollbarComponent의 각 크기값들은 최소값으로 '0'이 지정되고, 최대값은 '10'으로 지정한다. 시작 위치 값은 '0'이고, 영역값은 '1', 증감값은 '1'로 지정 한다.

**매개 변수**

- `direction` - 스크롤 바의 방향값 Throws
- `IllegalArgumentException` - 스크롤 바의 방향값이 HORIZONTAL나
- `VERTICAL이외의` - 값으로 잘못 지정된 경우 발생.

**참고 항목**

ScrollbarComponent() ScrollbarComponent(int direction, int currentValue, int viewAmount, int minimum,

```c
int maximum, int chAmount)
ScrollbarComponent
```

public ScrollbarComponent(int direction, int currentValue, int viewAmount,

```c
int minimum,int maximum, int chAmount)
주어진 스크롤 바의 각 크기값과 스크롤 방향값을 ScrollbarComponent 의
```

인스턴스를 생성한다. 지정할 수 있는 스크롤 방향값은 HORIZONTAL과VERTICAL이며, 이외의 값으로 지정된 경우 IllegalArgumentException이 발생 한다. ScrollbarComponent의 크기값은 스크롤 크기값에 설명된 영역에 맞도록 지정되어야 하며, 지정한 값이 영역에서 벗어난 경우 IllegalArgumentException이 발생한다.

**매개 변수**

- `direction` - 스크롤 바의 방향값.
- `currentValue` - 현재 스크롤바의 위치값.
- `viewAmount` - 스크롤 바의 영역크기값.
- `minimum` - 스크롤 바의 minimum값.
- `maximum` - 스크롤 바의 maximum값. Throws
- `IllegalArgumentException` - 스크롤 바의 방향값이 HORIZONTAL나 VERTICAL 이외의 값으로 잘못 지정된 경우 발생.
- `IllegalArgumentException` - 각 크기값에서 오류가 발생한 경우

**참고 항목**

ScrollbarComponent() ScrollbarComponent(int direction) 메쏘드 상세 설명

#### getDirection

public int getDirection() 현재 지정된 ScrollbarComponent의 스크롤 방향값을 반환한다. 특정 스크롤 방향값을 지정하지 않은 경우 기본적으로 지정되는 스크롤 방향값은 VERTICAL이다.

**반환 값**

스크롤의 방향값.

**참고 항목**

setDirection(int direction)

#### setDirection

public void setDirection(int direction) 스크롤바의 스크롤 방향값을 지정한다. 지정할 수 있는 스크롤 방향값은 HORIZONTAL과VERTICAL이며, 이외의 값으로 지정된 경우 IllegalArgumentException이 발생 한다.

**매개 변수**

- `direction` - 스크롤 방향값. Throws
- `IllegalArgumentException` - 스크롤 바의 방향값이 HORIZONTAL나 VERTICAL 이외의 값으로 지정된 경우

**참고 항목**

getDirection()

#### getCurrentValue

public int getCurrentValue() 스크롤바의 현재 위치값(currentValue)을 반환한다.

**반환 값**

현재 위치값.

**참고 항목**

setCurrentValue(int newValue)

#### setCurrentValue

public void setCurrentValue(int newValue) 스크롤바의 현재 위치값(currentValue)을 지정한다. 이 값은 스크롤 크기값에 설명된 영역에 맞도록 지정되어야 하며, 지정한 값이 최소값보다 작거나 최대값보다 큰 경우 최대값 혹은 최소값으로 설정된다. 값을 지정할 때 주의할 점은 그림에서 보듯이 현재 위치값을 지정할 수 있는 최대값은 스크롤바의 최대값이 아니고, 스크롤바의 최대값에서 영역값을 뺀 값이 현재 위치값의 최대값으로 지정될 수 있다.

**매개 변수**

- `newValue` - 새로 지정할 현재 스크롤 값

**참고 항목**

getCurrentValue()

#### getMinimum

public int getMinimum() 스크롤바의 최소값을 반환한다.

**반환 값**

스크롤바의 최소값.

**참고 항목**

setMinimum(int newMinimum)

#### setMinimum

public void setMinimum(int newMinimum) 스크롤바의 최소값을 지정한다. 이 값은 스크롤 크기값에 지정된 영역에 맞도록 지정되어야 한다. Minimum값이 변경에 따라 현재 값이 변경 될 수 있다.

**매개 변수**

- `newMinimum` - 스크롤 가능한 최소값.

**참고 항목**

getMinimum()

#### getMaximum

public int getMaximum() 스크롤바의 최대값을 반환한다.

**반환 값**

스크롤바의 최대값.

**참고 항목**

setMaximum(int newMaximum)

#### setMaximum

public void setMaximum(int newMaximum) 스크롤바의 최대값을 지정한다. 이 값은 스크롤 크기값에 설명된 영역에 맞도록 지정되어야 한다. Maximum 값의 변경에 따라 현재 값이 변경 될 수 있다. 값을 지정할 때 주의할 점은 그림에서 보듯이 현재 위치값을 지정할 수 있는 최대값은 스크롤바의 최대값이 아니고, 스크롤바의 최대값에서 영역값을 뺀 값이 현재 위치값의 최대값으로 지정될 수 있다.

**매개 변수**

- `newMaximum` - 스크롤바의 최대값.

**참고 항목**

getMaximum()

#### getViewAmount

public int getViewAmount() 스크롤바의 영역크기값을 얻어온다.

**반환 값**

영역크기값.

**참고 항목**

setViewAmount(int newAmount)

#### setViewAmount

public void setViewAmount(int newAmount) 스크롤바의 영역크기값을 지정한다. 이 값은 스크롤 크기값에 설명된 영역에 맞도록 지정되어야 한다. 값을 지정할 때 주의할 점은 그림에서 보듯이 현재 위치값을 지정할 수 있는 최대값은 스크롤바의 최대값이 아니고, 스크롤바의 최대값에서 영역값을 뺀 값이 현재 위치값의 최대값으로 지정될 수 있다.

**매개 변수**

- `newAmount` - 화면에 보여지는 데이타의 양.

**참고 항목**

getViewAmount()

#### getChangeAmount

public int getChangeAmount() 스크롤 시 증감되는 증감값의 크기를 얻어온다.

**반환 값**

증감값

**참고 항목**

setChangeAmount(int newChAmount)

#### setChangeAmount

public void setChangeAmount(int newChAmount) 스크롤 시 증감되는 값의 크기를 세팅한다. 이 값은 스크롤 크기값에 설명된 영역에 맞도록 지정되어야 한다.

**매개 변수**

- `newChAmount` - 스크롤 증감값.

**참고 항목**

getChangeAmount()

#### getForegroundColor

public int getForegroundColor() 스크롤바의 전경색을 돌려준다. 전경생을 지정하지 않은 경우 기본값은 '0x00000000'이다.

**반환 값**

현재 스크롤 바의 전경색.

**참고 항목**

setForegroundColor(int).

#### setForegroundColor

public void setForegroundColor(int fg) 스크롤바의 전경색을 지정한다. 지정한 색은 0x00RRGGBB 값이 된다. 기본 전경색 값은 '0x00000000'이다.

**매개 변수**

- `fg` - 전경색 값.

**참고 항목**

getForegroundColor().

#### paintContent

public void paintContent(Graphics g) 이하 메소스 설명은 Component 클래스에서 복사되었음 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides paintContent in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics

#### focusNotify

public void focusNotify(boolean b) 이하 메소스 설명은 Component 클래스에서 복사되었음 포커스를 받으면 호출된다. 컴포넌트가 포커스를 가지거나 가지고 있지 않음을 보여주기 위해서 repaint함수를 호출하여, 다시 자기 자신을 그리도록 한다. Overrides focusNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `b` - 포커스를 가질 땐 true가 넘어오고, 가지지 않을 땐 false keyNotify
- `public` - boolean keyNotify(int type, int key) 이하 메소스 설명은 Component 클래스에서 복사되었음 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력값이 된다. Overrides
- `keyNotify` - in class Component
- `Following` - copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. getPreferredHeight public int getPreferredHeight() 컴포넌트의 적절한 높이를 결정한다. ContainerComponent에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 높이 getPreferredHeight public int getPreferredHeight(int w) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. 지정된 제한된 폭을 가질 경우의 컴포넌트의 높이를 돌려준다. 만일 LabelComponent 나 TextFieldComponent, TextAreaComponent와 같이 포맷팅이 가능한 컴포넌트인 경우에는 가변 폭을 가질 수가 있다. 가변 폭을 가지게 되면, 폭에 따라서 높이가 달라지게 된다. 이때 이 함수를 통해서 컴포넌트의 높이를 얻어 온다. 만일, w가 -1이 면 폭에 제한이 없는 것으로 계산된다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `w` - 가변폭.

**반환 값**

컴포넌트의 높이. getPreferredWidth public int getPreferredWidth() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 폭을 결정한다. Container에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredWidth in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 폭. Class ShellComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.ContainerComponent | +--org.kwis.msp.lwc.ShellComponent Direct Known Subclasses: AnnunciatorComponent, DialogComponent public class ShellComponent extends ContainerComponent Card와의 연결을 해주며, 제목과 명령 입력 컴포넌트와 작업 컴포넌트를 가진다. UI컴포넌트를 화면에 보여주기 위해서 맨 상단에는 이 컴포넌트를 사용해야 한다. ShellComponent는 AddComponent를 통해서 하나의 작업 컴포넌트 만을 가질 수 있다. 이 컴포넌트는 lcdui의 Card에 연결하여 카드로부터 들어오는 이벤트를 해당 컴포넌트에게 전달해 주는 역할을 한다. 또한 화면에 타이틀과 프레임을 보여준다. Fields inherited from class org.kwis.msp.lwc.ContainerComponent cmpFocus, cmps, insetBottom, insetLeft, insetRight, insetTop, ncomp, offsetX, offsetY, useFrame Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.ContainerComponent getComponent, getIndexOf, getNumberOfComponent, paint, paintFrame, removeComponent, repaint, scrollTo, setComponent, useFrame, validate Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, focusNotify, getBackground, getForeground, getHeight, getPreferredHeight, getPreferredHeight, getPreferredWidth, getWidth, getXOnScreen, getYOnScreen, hasFocus, invalidate, isValid, paintContent, pointerNotify, setBackground, setEventListener, setFocus, setForeground, toString Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 필드 상세 설명 cd protected Card cd 연결되는 카드를 저장하는 필드 cmpTitle protected Component cmpTitle 타이틀이 되는 컴포넌트 cmpWork protected Component cmpWork 타이틀과 커맨드 사이에 위치하는 컴포넌트. cmpCommand protected Component cmpCommand 커맨드 컴포넌트 생성자 상세 설명 ShellComponent public ShellComponent() 쉘 컴포넌트를 생성한다. 화면 크기로 쉘 컴포넌트를 생성한다.

**매개 변수**

ShellComponent
- `public` - ShellComponent(boolean inflate) 쉘 컴포넌트를 생성한다. inflate에 따라서 전체 화면에 맞출 것인지, 내부 컴포넌트에 크기를 맞출 것인지를 결정한다.

**매개 변수**

- `inflate` - 컴포넌트의 크기에 맞추어서 커질 것인지의 여부. ShellComponent
- `public` - ShellComponent(int x, int y, int w, int h) 쉘 컴포넌트를 생성한다. 지정한 크기로 쉘 컴포넌트를 생성한다.

**매개 변수**

- `x` - 컴포넌트 화면상의 위치.
- `y` - 컴포넌트 화면상의 위치.
- `w` - 컴포넌트 화면상에서의 폭.
- `h` - 컴포넌트 화면상에서의 높이. Throws
- `IllegalArgumentException` - w나 h가 0 이하일 경우 ShellComponent
- `public` - ShellComponent(int x, int y, int w, int h, boolean bTrans) 쉘 컴포넌트를 생성한다. 지정한 크기가 되며 bTrans의 여부에 따라서 투명한 쉘이 될 수도 있다.

**매개 변수**

- `x` - 컴포넌트 화면상의 위치.
- `y` - 컴포넌트 화면상의 위치.
- `w` - 컴포넌트 화면상에서의 폭.
- `h` - 컴포넌트 화면상에서의 높이.
- `bTrans` - 컴포넌트 투명 여부. 메쏘드 상세 설명 layout
- `public` - void layout() 이하 메소스 설명은 Component 클래스에서 복사되었음 하위 컴포넌트의 크기와 위치를 결정한다. Overrides
- `layout` - in class Component repaint
- `public` - void repaint(int x, int y, int w, int h) 이하 메소스 설명은 Component 클래스에서 복사되었음 화면의 내용을 갱신할 필요가 있을 때 부른다. 이 함수는 최종적으로 Card의
- `repaint를` - 호출하며, 호출된 repaint함수는 일정 시간 이후에 해당 컴포넌트의 paint()함수를 자동적으로 부르는 과정을 거친다. Overrides
- `repaint` - in class ContainerComponent
- `Following` - copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `x` - 갱신할 영역의 x축 좌표
- `y` - 갱신할 영역의 y축 좌표
- `w` - 갱신할 영역의 폭
- `h` - 갱신할 영역의 높이 show
- `public` - void show() 컴포넌트를 화면상에 보여준다. 컴포넌트를 화면상에 보여주기 전에 컴포넌트의 위치와 크기를 validate함수를 통해서 계산한다. hide
- `public` - void hide() 컴포넌트를 감춘다. isShown
- `public` - boolean isShown() 이하 메소스 설명은 Component 클래스에서 복사되었음 현재 컴포넌트가 보이는지 안 보이는지 여부를 돌려준다. 현재 컴포넌트가 화면에 보이면 true, 그렇지 않으면 false를 돌려준다. Overrides
- `isShown` - in class Component
- `Following` - copied from class: org.kwis.msp.lwc.Component

**반환 값**

화면에 보이는 여부 configure public void configure(int x, int y, int w, int h, int mask) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 위치나 크기를 변경한다. mask에 따라서 컴포넌트의 크기나 위치를 변경한다. mask값과 POS_MASK를 논리적 AND 연산을 해서 그 값이 POS_MASK이면, 상위 컴포넌트 내에서 위치 x, y로 변경해 준다. mask값과 SIZE_MASK를 논리적 AND 연산을 해서 그 값이 SIZE_MASK이면, 컴포넌트의 크기를 (w, h)로 변경해 준다. 즉 컴포넌트의 크기와 위치를 동시에 변경할 수 있다. 이 함수는 변경된 부분에 대해서 repaint함수를 호출하므로, 칠해질 영역이 paintContent함수에 의해서 칠해지도록 한다. 컴포넌트의 크기는 상위 부모 컴포넌트의 layout함수에 의해서 그 크기가 결정된다. Overrides configure in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `x` - 컴포넌트의 상위 컴포넌트 상에서의 'x'축 위치
- `y` - 컴포넌트의 상위 컴포넌트 상에서의 'y'축 위치
- `w` - 컴포넌트의 폭
- `h` - 컴포넌트의 높이
- `mask` - POS_MASK | SIZE_MASK가 올 수 있으며, POS_MASK가 오는 경우에 x, y값 이 유효한 값이 오며, SIZE_MASK가 오는 경우에 w, h값이 유효한 값이 된다. getX
- `public` - int getX() 이하 메소스 설명은 Component 클래스에서 복사되었음
- `x축의` - 좌표를 돌려준다. 컴포넌트의 상위 부모 컴포넌트 상에서의 x축 좌표를 돌려준다. Overrides
- `getX` - in class Component
- `Following` - copied from class: org.kwis.msp.lwc.Component

**반환 값**

x축 좌표 getY public int getY() 이하 메소스 설명은 Component 클래스에서 복사되었음 y축의 좌표를 돌려준다. 컴포넌트의 상위 부모 컴포넌트 상에서의 y축 좌표를 돌려준다. Overrides getY in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

y축 좌표 showNotify public void showNotify(boolean b) 이하 메소스 설명은 Component 클래스에서 복사되었음 화면의 내용이 보이면 호출된다. addComponent나 removeComponent에 의해서 불리거나, 자신의 맨 상위의 부모 컴포넌트(ShellComponent)가 show에 의해서 화면에 나타날 때 호출된다. Overrides showNotify in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `bShow` - 컴포넌트가 나타나는지 안 나타나는지 여부 serviceRepaints
- `public` - void serviceRepaints() 이하 메소스 설명은 Component 클래스에서 복사되었음 갱신된 내용을 즉시 화면에 출력해준다. repaint에 의한 paint를 나중에 부르는 것이 아니라, 직접 paint함수를 불러서 화면에 출력한다. Overrides
- `serviceRepaints` - in class Component addComponent
- `public` - void addComponent(int index, Component cmp) 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 자식 컴포넌트를 하나 추가한다. 지정한 위치에 cmp가 가리키는 컴포넌트를 추가한다.
- `cmp가` - null인 경우 NullPointerException이 발생한다. 또한 cmp가 이미 다른 부모 컴포넌트를 가지는 경우 IllegalArgumentException이 발생 한다.
- `index값이` - '0'보다 작거나 추가된 컴포넌트의 개수보다 큰 경우
- `IndexOutOfBoundsException이` - 발생한다. Overrides
- `addComponent` - in class ContainerComponent
- `Following` - copied from class: org.kwis.msp.lwc.ContainerComponent

**매개 변수**

- `index` - 넣을 위치
- `cmp` - 넣을 컴포넌트 Throws
- `IllegalArgumentException` - cmp가 이미 다른 부모 컴포넌트를 가지고 있는 경우 발생
- `IndexOutOfBoundsException` - index가 유효한 영역을 벗어나 있는 경우
- `NullPointerException` - cmp이 null인 경우 addComponent
- `public` - int addComponent(Component cmp) 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 자식 컴포넌트를 하나 추가한다. 맨 위에 자식 컴포넌트를 추가한다. Overrides
- `addComponent` - in class ContainerComponent
- `Following` - copied from class: org.kwis.msp.lwc.ContainerComponent

**매개 변수**

- `cmp` - 추가할 자식 컴포넌트 Throws
- `IllegalArgumentException` - cmp가 이미 다른 부모 컴포넌트를 가지는 경우
- `NullPointerException` - cmp이 null인 경우 processEvent
- `protected` - boolean processEvent(int type, int subtype, int param1,
- `int` - param2) 이하 메소스 설명은 Component 클래스에서 복사되었음 이벤트를 처리한다. Overrides
- `processEvent` - in class ContainerComponent
- `Following` - copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 이벤트 타입
- `subtype` - 이벤트 타입에 따른 서브 이벤트 타입
- `param1` - 부가적인 인수
- `param2` - 부가적인 인수 setTitle
- `public` - void setTitle(Component cmp) 타이틀을 지정한다. 특정 레이블 컴포넌트로 타이틀을 출력하도록 한다.

**매개 변수**

- `cmp` - 타이틀로 지정할 레이블 컴포넌트 getTitle
- `public` - Component getTitle() 지정된 타이틀을 돌려준다.

**반환 값**

타이틀 컴포넌트 getWorkComponent public Component getWorkComponent() 지정된 Component 돌려준다.

**반환 값**

add된 Work컴포넌트 setWorkComponent public void setWorkComponent(Component cmp) Component를 설정 한다

**매개 변수**

- `cmp` - 설정할 Work컴포넌트 removeAllComponents
- `public` - void removeAllComponents() 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 모든 컴포넌트를 삭제한다. Overrides
- `removeAllComponents` - in class ContainerComponent removeComponent
- `public` - void removeComponent(Component cmp) 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 지정된 컴포넌트를 삭제한다. 만일 지정된 컴포넌트가 자식 컴포넌트로 등록되어 있지 않은 경우 IllegalArgumentException이 발생한다. Overrides
- `removeComponent` - in class ContainerComponent
- `Following` - copied from class: org.kwis.msp.lwc.ContainerComponent

**매개 변수**

- `cmp` - 삭제할 컴포넌트 setCommand
- `public` - void setCommand(Component cmp, boolean bGrab) 커맨드를 지정한다. 화면 하단에 나타나는 커맨드를 지정한다. 이때 컴포넌트는 모든 키 이벤트에 대해서 keyNotify()함수가 불려지도록 할 수 있다. 이 기능은 bGrab이
- `true일때` - 작동된다.

**매개 변수**

- `cmp` - 커맨드가 될 컴포넌트
- `bGrab` - 모든 키를 이 컴포넌트가 우선적으로 가로 챈다. getCommand
- `public` - Component getCommand() 지정된 커맨드 컴포넌트를 돌려준다.

**반환 값**

지정된 커맨드 컴포넌트 getNextTraversalComponent protected Component getNextTraversalComponent() 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 포커스 가질 수 있는 다음 컴포넌트를 돌려준다. 포커스를 가질 수 있는 다음 컴포넌트를 돌려준다. 돌려지는 컴포넌트는 현재 컴포넌트의 자식 컴포넌트 중 하나가 된다. 만일 포커스를 가질 수 있는 컴포넌트가 없는 경우에는 null을 돌려준다. Overrides getNextTraversalComponent in class ContainerComponent Following copied from class: org.kwis.msp.lwc.ContainerComponent

**반환 값**

포커스를 가질 수 있는 다음 컴포넌트 getPrevTraversalComponent protected Component getPrevTraversalComponent() 이하 메소스 설명은 ContainerComponent 클래스에서 복사되었음 포커스 가질 수 있는 이전 컴포넌트를 돌려준다. 포커스를 가질 수 있는 다음 컴포넌트를 돌려준다. 돌려지는 컴포넌트는 현재 컴포넌트의 자식 컴포넌트 중 하나가 된다. 만일 포커스를 가질 수 있는 컴포넌트가 없는 경우에는 null을 돌려준다. Overrides getPrevTraversalComponent in class ContainerComponent Following copied from class: org.kwis.msp.lwc.ContainerComponent

**반환 값**

포커스를 가질 수 있는 이전 컴포넌트 setTitle public void setTitle(String str) 타이틀 문자열을 지정한다. 특정 문자로 타이틀을 출력하도록 한다.

**매개 변수**

- `str` - 타이틀로 지정할 문자열 getCard
- `public` - Card getCard() 이하 메소스 설명은 Component 클래스에서 복사되었음 현재 컴포넌트에 연결된 카드를 돌려준다. ShellComponent와 같이 상위 컴포넌트는 내부에 Card를 가지게 된다. 현재 컴포넌트의 맨 상위 부모 컴포넌트의 Card를 돌려주게 된다. 그러나, 만일 상위 부모 컴포넌트가 존재하는 경우가 아닌 경우에는
- `null이` - 넘어 갈 수 있다. Overrides
- `getCard` - in class Component
- `Following` - copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트와 연관 있는 Card

**참고 항목**

Card

#### grabKey

public void grabKey(int key) 특정 키코드를 그랩(Grab)하여 GrabKeyListener에게 보낸다. 이 함수를 이용하여 특정 키를 그랩하면 특정 키에 관련된 이벤트를 자식 컴포넌트에게 바로 보내지 않고 그랩 키 Listener에게 우선적으로 처리를 넘긴다. 정의 되지 않은 키코드를 구하기 위해서는 GameKey를 Display.getKeyCode()함수를 이용하여 변환하면 된다.

**매개 변수**

- `key` - grab할 키코드(EventQueue 참조)

**참고 항목**

setGrabKeyListener(org.kwis.msp.lwc.GrabKeyListener, java.lang.Object) ungrabKey(int) GrabKeyListener Display.getKeyCode(int)

#### ungrabKey

public void ungrabKey(int key) 특정 키에 대한 그랩(Grab)을 해제 한다. 특정 키코드에 대한 그랩을 해제 한다.

**매개 변수**

- `gameKey` - ungrab할 키코드(EventQueue의 키코드 참조)

**참고 항목**

grabKey(int) setGrabKeyListener(org.kwis.msp.lwc.GrabKeyListener, java.lang.Object) GrabKeyListenerDisplay.getKeyCode(int)

#### setGrabKeyListener

public void setGrabKeyListener(GrabKeyListener listener, Object obj) 그랩 키 Listener를 등록한다. grabKey에 의해 그랩이 설정된 경우 그래핑된 키 이벤트를 받을 Listener를 등록한다. 지정된 이벤트 Listener에게 키 이벤트를 일단 보내준다. 만일 이벤트 Listener가 true를 돌려주면 이벤트 처리를 하지 않으며, false를 돌려주면 이벤트를 처리한다.

**매개 변수**

- `listener` - 키 그랩 Listener
- `obj` - 키 그랩 Listener 불릴 때의 파라미터

**참고 항목**

GrabKeyListener, grabKey(int), ungrabKey(int)

#### keyNotify

protected boolean keyNotify(int type, int chr) 이하 메소스 설명은 Component 클래스에서 복사되었음 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력값이 된다. Overrides keyNotify in class ContainerComponent Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED이` - 됨
- `chr` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. Class TextBoxComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.TextComponent | +--org.kwis.msp.lwc.TextBoxComponent public class TextBoxComponent extends TextComponent TextBoxComponent는 TextComponent를 상속한 클래스로 정해진 넓이에 맞도록 문자를 편집 할 수 있다. 이 컴포넌트의 넓이는 이 컴포넌트를 추가한 ContainerComponent의 넓이와 같고 , 높이는 현재 화면에 출력된 문자 데이타에 맞도록 자동으로 변경된다. 전체 화면을 사용하여 문자 편집을 할 수 있으며, 특정 문자열만을 입력하도록 입력제한을 할 수 있다. TextComoponent에서 정의된 입력 제한자에 대한 내용을 참고하세요. 기본적으로 최대 입력 가능한 문자열에 대한 제한은 하지 않으며, TextComponent.setMaxLength(int maxLen)를 통해서 최대 입력가능한 문자 수를 제한 할 수 있다.

**참고 항목**

TextComponent, TextFieldComponent Fields inherited from class org.kwis.msp.lwc.TextComponent charCount, constChecker, constraint, CONSTRAINT_ANY, CONSTRAINT_NUMBER, CONSTRAINT_PASSWORD, display, f, imHandler, iMode, isWide, m_cPos, m_td, maxLength, modeViewer, tShell Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.TextComponent focusNotify, getConstraint, getFont, getMaxLength, getString, setMaxLength, showNotify Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, getBackground, getCard, getForeground, getHeight, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, layout, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, toString, validate Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명

#### TextBoxComponent

public TextBoxComponent(String data, int constraints) 주어진 문자 데이타와 입력 제한자로 TextComponent의 인스턴스를 생성한다. 문자 데이타는 null값을 가질 수 있다. 지정한 입력 제한자가 TextComponent.CONSTRAINT_NUMBER, TextComponent.CONSTRAINT_PASSWORD, TextComponent.CONSTRAINT_ANY이외의 값이 지정된 경우 IllegalArgumentException이 발생하며, 문자데이타가 입력 제한자에 어긋난 데이타를 포함하는 경우 IllegalArgumentException이 발생한다. 기본적으로 최대 입력 가능한 문자열에 대한 제한은 하지 않으며, TextComponent.setMaxLength(int maxLen)를 통해서 최대 입력가능한 문자 수를 제한 할 수 있다.

**매개 변수**

- `data` - 문자데이타 혹은 null
- `constraints` - 문자 입력 형태 TextBoxComponent
- `public` - TextBoxComponent(String data, int constraints, int h) 주어진 문자 데이타와 입력 제한자,컴포넌트의 높이값으로 TextComponent의 인스턴스를 생성한다. 문자 데이타는 null값을 가질 수 있고, 지정한 높이 값은 초기 컴포넌트의 높이값으로 컴포넌트내의 데이타가 증가하여 전체 높이 값이 지정한 높이 값보다 커질 경우 더 큰 값으로 현재 컴포넌트의 높이는 재 지정된다. 지정한 입력 제한자가 TextComponent.CONSTRAINT_NUMBER, TextComponent.CONSTRAINT_PASSWORD, TextComponent.CONSTRAINT_ANY이외의 값이 지정된 경우
- `IllegalArgumentException이` - 발생하며, 문자데이타가 입력 제한자에 어긋난 데이타를 포함하는 경우 IllegalArgumentException이 발생한다. 기본적으로 최대 입력 가능한 문자열에 대한 제한은 하지 않으며, TextComponent.setMaxLength(int maxLen)를 통해서 최대 입력가능한 문자 수를 제한 할 수 있다.

**매개 변수**

- `data` - 문자데이타 혹은 null
- `constraints` - 문자 입력 형태
- `h` - 컴포넌트의 높이값 메쏘드 상세 설명 setString
- `public` - void setString(String data) 이하 메소스 설명은 TextComponent 클래스에서 복사되었음 문자 데이타를 지정한다. 입력 제한자가 지정되어 있는 경우 문자 데이타가 입력 제한자에 따른 문자열이 아니면 IllegalArgumentException이 발생한다. 현재 입력가능한 최대 문자수가 제한된 상태에서 입력한 문자수가 최대 문자 수를 초과한 경우 최대 문자 수만큼만 자신의 데이타로 처리한다. 문자 데이타가 null인 경우 현재의 문자 데이타를 ""(empty String로 변경한다. 따라서 화면에 보여지는 문자열은 없게 된다. Overrides
- `setString` - in class TextComponent
- `Following` - copied from class: org.kwis.msp.lwc.TextComponent

**매개 변수**

- `data` - 문자데이타 혹은 null Throws
- `IllegalArgumentException` - 현재의 입력 제한자에 따른 문자열을 지정하지 않은 경우 발생

**참고 항목**

TextComponent.getString()

#### insert

public void insert(char[] data, int offset, int len, int index) 이하 메소스 설명은 TextComponent 클래스에서 복사되었음 현재 화면에 출력된 문자 데이타에서 인자로 주어진 문자 데이타를 index 위치에 추가한다. data가 null인 경우 NullPointerException이 발생하고, index값이 '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우 IndexOutOfBoundsException이 발생한다. 입력 가능한 최대 문자 수가 제한된 경우에 현재 출력된 문자 데이타의 길이와 len을 합한 값이 최대문자 수 보다 큰 경우 IllegalArgumentException이 발생한다. Overrides insert in class TextComponent Following copied from class: org.kwis.msp.lwc.TextComponent

**매개 변수**

- `data` - 새로 추가할 문자 데이타
- `offset` - 새로 추가할 문자 데이타에서 추가될 문자 데이타의 시작 위치
- `len` - 새로 추가할 문자데이타의 길이
- `index` - 현재 화면에 출력된 문자데이타에서 새로운 문자 데이타를 추가할 위치 Throws
- `NullPointerException` - data가 null인 경우
- `IndexOutOfBoundsException` - index값이 '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우
- `IllegalArgumentException` - 입력 가능한 최대 문자 수가 제한된 경우에 현재 출력된 문자 데이타의 길이와 len을 합한 값이 최대문자 수 보다 큰 경우
- `IllegalArgumentException` - 입력할 문자데이타에 현재의 입력제한자에 맞지 않은 문자데이타가 포함된 경우 delete
- `public` - void delete(int index, int len) 이하 메소스 설명은 TextComponent 클래스에서 복사되었음 현재 화면에 보여지고 있는 문자데이타의 index위치에서부터 len길이만큼 데이타를 삭제한다.
- `index값이` - '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우
- `IndexOutOfBoundsException이` - 발생한다. len는 현재 출력된 문자 데이타의 전체 길이를 초과 할 수 없으며 초과 할 경우 IllegalArgumentException이 발생한다. Overrides
- `delete` - in class TextComponent
- `Following` - copied from class: org.kwis.msp.lwc.TextComponent

**매개 변수**

- `index` - 삭제 위치.
- `len` - 삭제 할 문자데이타 길이 Throws
- `IndexOutOfBoundsException` - len,index값이 '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우
- `IllegalArgumentException` - len이 현재 출력된 문자 데이타의 전체 길이를 초과 한 경우 getPreferredWidth
- `public` - int getPreferredWidth() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 폭을 결정한다. Container에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides
- `getPreferredWidth` - in class Component
- `Following` - copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 폭. getPreferredHeight public int getPreferredHeight(int w) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. 지정된 제한된 폭을 가질 경우의 컴포넌트의 높이를 돌려준다. 만일 LabelComponent 나 TextFieldComponent, TextAreaComponent와 같이 포맷팅이 가능한 컴포넌트인 경우에는 가변 폭을 가질 수가 있다. 가변 폭을 가지게 되면, 폭에 따라서 높이가 달라지게 된다. 이때 이 함수를 통해서 컴포넌트의 높이를 얻어 온다. 만일, w가 -1이 면 폭에 제한이 없는 것으로 계산된다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `w` - 가변폭.

**반환 값**

컴포넌트의 높이. getPreferredHeight public int getPreferredHeight() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. ContainerComponent에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 높이 configure public void configure(int x, int y, int w, int h, int mask) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 위치나 크기를 변경한다. mask에 따라서 컴포넌트의 크기나 위치를 변경한다. mask값과 POS_MASK를 논리적 AND 연산을 해서 그 값이 POS_MASK이면, 상위 컴포넌트 내에서 위치 x, y로 변경해 준다. mask값과 SIZE_MASK를 논리적 AND 연산을 해서 그 값이 SIZE_MASK이면, 컴포넌트의 크기를 (w, h)로 변경해 준다. 즉 컴포넌트의 크기와 위치를 동시에 변경할 수 있다. 이 함수는 변경된 부분에 대해서 repaint함수를 호출하므로, 칠해질 영역이 paintContent함수에 의해서 칠해지도록 한다. 컴포넌트의 크기는 상위 부모 컴포넌트의 layout함수에 의해서 그 크기가 결정된다. Overrides configure in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `x` - 컴포넌트의 상위 컴포넌트 상에서의 'x'축 위치
- `y` - 컴포넌트의 상위 컴포넌트 상에서의 'y'축 위치
- `w` - 컴포넌트의 폭
- `h` - 컴포넌트의 높이
- `mask` - POS_MASK | SIZE_MASK가 올 수 있으며, POS_MASK가 오는 경우에 x, y값 이 유효한 값이 오며, SIZE_MASK가 오는 경우에 w, h값이 유효한 값이 된다. keyNotify
- `public` - boolean keyNotify(int type, int key) 이하 메소스 설명은 TextComponent 클래스에서 복사되었음 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력값이 된다. EventQueue.SOFT1키를 누르면 입력 모드를 변경할 수 있고, 숫자키 입력에 대한 문자 처리를 담당하고 있는 InputMethodHandler의 notifykeyInput메소드에 대한 실행을 관리하고 있다. 기타 전체 화면으로 문자 편집을 하기 위한 제어를 담당한다. Overrides
- `keyNotify` - in class TextComponent
- `Following` - copied from class: org.kwis.msp.lwc.TextComponent

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED` - 이 됨
- `key` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. setFont public void setFont(Font f) 이하 메소스 설명은 TextComponent 클래스에서 복사되었음 폰트를 지정한다. 기본적으로 폰트는 Font.getDefaultFont()를 통해서 지정되어 있다. Overrides setFont in class TextComponent Following copied from class: org.kwis.msp.lwc.TextComponent

**매개 변수**

- `f` - 새로 지정할 폰트

**참고 항목**

TextComponent.getFont()

#### paintContent

public void paintContent(Graphics g) 이하 메소스 설명은 Component 클래스에서 복사되었음 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides paintContent in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics Class TextComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.TextComponent Direct Known Subclasses: TextBoxComponent, TextFieldComponent public abstract class TextComponent extends Component 텍스트 출력 및 입력 수정 삭제를 위한 추상 클래스이다. 이 클래스를 상속받아 구현된 클래스는 TextBoxComponent와 TextFieldComponent이다. 전체 화면을 이용한 문자 편집 TextFieldComponent와 TextBoxComponen에서 EventQueue.FIRE키 입력이 있을 경우 전체 화면으로 문자 편집이 가능한 에디터가 생성된다. 이 에디터에서 편집을 마친 경우 EventQueue.FIRE키를 입력을 하여 이전 화면으로 돌아갈 수 있으며, 이전 화면의 문자 데이타는 전체 화면에서 편집하던 문자 데이타로 변경된다. 입력 제한자 TextComponent에서는 6가지 종류의 입력 제한자를 제공하고 있다. CONSTRAINT_NUMBER는 '-',' '와 숫자입력만을 허용하는 입력제한자이다. CONSTRAINT_PASSWORD는 암호입력을 위한 입력 형태로 내부적으로 사용되는 문자열은 숫자만을 허용한다. 이 경우 화면에 출력되는 형태는 '*'이다. CONSTRAINT_EMAILADDRESS는 이메일 주소 입력을 위한 입력제한자이다. 이 경우 내부적으로 사용되는 문자열은 영문 대,소문자와 숫자, 심볼이다. CONSTRAINT_URL은 URL입력을 위한 입력제한자이다. 이 경우 내부적으로 사용되는 문자열은 영문 대,소문자와 숫자, 심볼이다 CONSTRAINT_PHONENUMBER는 전화번호입력을 위한 입력 제한자이다. 이 경우 내부적으로 사용되는 문자열은 숫자이다. CONSTRAINT_ANY는 모든 문자열을 입력할 수 있는 입력 제한자 이다. * 위의 입력 제한자 외의 값을 지정할 수 없으며, 다른 값을 지정한 경우 IllegalArgumentException이 발생한다. 기본적으로 최대 입력 가능한 문자열에 대한 제한은 하지 않으며, setMaxLength(int maxLen)를 통해서 최대 입력가능한 문자 수를 제한 할 수 있다. 문자 입력 처리를 위한 InputMethodListener와 ActionListener를 구현을 내부 클래스를 포함하고 있으며, 각 내부 클래스에서는 현재 입력 모드에 따라 입력 받은 문자를 관리하고 입력 화면을 전체 화면 사이즈로 전환하거나 원래 화면, 즉 TextFieldComponent,TextBoxComponent로 복원하는 일을 담당하고 있다.

**참고 항목**

TextFieldComponent, TextBoxComponent Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, configure, getBackground, getCard, getForeground, getHeight, getPreferredHeight, getPreferredHeight, getPreferredWidth, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, layout, paintContent, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, toString, validate Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 필드 상세 설명

#### CONSTRAINT_NUMBER

public static final int CONSTRAINT_NUMBER 사용자가 입력 가능한 문자를 ' '와 '-',숫자로만 제한할 경우에 사용하는 입력제한자. CONSTRAINT_NUMBER에 할당된 값은 '1'.

#### CONSTRAINT_PASSWORD

public static final int CONSTRAINT_PASSWORD 사용자가 입력 가능한 문자를 패스워드로 제한할 경우에 사용하는 입력제한자. 이 경우 내부적으로 사용되는 문자열은 숫자이며, 화면에 출력되는 형태는 '*'이다 CONSTRAINT_PASSWORD에 할당된 값은 '2'.

#### CONSTRAINT_ANY

public static final int CONSTRAINT_ANY 사용자가 입력 가능한 문자에 제한이 없는 경우에 사용되는 입력제한자. 이 값은 사용자가 특별히 사용문자에 대한 제한을 두지 않은 경우로 특정 입력 제한자를 지정하지 않으면 기본적 사용된다. CONSTRAINT_ANY에 할당된 값은 '0'.

#### CONSTRAINT_EMAILADDRESS

public static final int CONSTRAINT_EMAILADDRESS 사용자가 입력 가능한 문자를 이메일 주소로 로 제한할 경우에 사용하는 입력제한자. 이 경우 내부적으로 사용되는 문자열은 영문 대,소문자와 숫자, 심볼이다. CONSTRAINT_EMAILADDRESS 할당된 값은 '3'.

#### CONSTRAINT_URL

public static final int CONSTRAINT_URL 사용자가 입력 가능한 문자를 URL로 제한할 경우에 사용하는 입력제한자. 이 경우 내부적으로 사용되는 문자열은 영문 대,소문자와 숫자, 심볼이다. CONSTRAINT_URL 할당된 값은 '4'.

#### CONSTRAINT_PHONENUMBER

public static final int CONSTRAINT_PHONENUMBER 사용자가 입력 가능한 문자를 전화번호로 제한할 경우에 사용하는 입력제한자. 이 경우 내부적으로 사용되는 문자열은 숫자입니다 CONSTRAINT_PHONENUMBER 할당된 값은 '5'.

#### imHandler

protected InputMethodHandler imHandler 키 입력에 다른 문자 데이타 처리를 위해 사용되는 입력 메소드핸들러.

#### m_cPos

protected int m_cPos 현재 문자 데이타의 위치

#### charCount

protected int charCount 문자의 수

#### constraint

protected int constraint 입력 형태지정

#### m_td

protected char[] m_td 문자 데이타

#### iMode

protected int iMode 현재 사용중인 문자열 입력모드

#### display

protected Display display 카드 사용을 위한 Display객체

#### modeViewer

protected org.kwis.msp.lwc.TextComponent.ModeViewer modeViewer 현재의 입력 모드 상황을 보여주는 카드

#### isWide

protected boolean isWide 전체 화면을 사용한 문자 입력 상태. true면 전체 화면을 사용한 문자 입력상태이다. 기본값은 false

#### tShell

protected ShellComponent tShell 전체화면 전환시 사용

#### maxLength

protected int maxLength 입력 가능한 최대 문자 길이 -1값인 경우 최대 문자 길이 제한 없음.

#### constChecker

protected org.kwis.msp.lwc.ConstraintChecker constChecker 문자 데이타가 지정한 입력 제한자에 맞는 데이타인지를 검사

#### f

protected Font f TextComponent에서 사용하는 폰트. 기본적으로 Font.getDefaultFont()를 통해 생성된다. 다른 폰트를 사용하기 원하는 경우 setFont(org.kwis.msp.lcdui.Font)를 통해 변경할 수 있다.

**참고 항목**

setFont(Font f) 메쏘드 상세 설명

#### setString

public void setString(String data) 문자 데이타를 지정한다. 입력 제한자가 지정되어 있는 경우 문자 데이타가 입력 제한자에 따른 문자열이 아니면 IllegalArgumentException이 발생한다. 현재 입력가능한 최대 문자수가 제한된 상태에서 입력한 문자수가 최대 문자 수를 초과한 경우 최대문자 수만큼만 자신의 데이타로 처리한다. 문자 데이타가 null인 경우 현재의 문자 데이타를 ""(empty String로 변경한다. 따라서 화면에 보여지는 문자열은 없게 된다.

**매개 변수**

- `data` - 문자데이타 혹은 null Throws
- `IllegalArgumentException` - 현재의 입력 제한자에 따른 문자열을 지정하지 않은 경우 발생

**참고 항목**

getString()

#### setMaxLength

public void setMaxLength(int maxLen) 입력가능한 최대문자수를 지정한다. 기본적으로 지정된 값은 '-1'로 이 경우 입력 문자수의 제한을 두지 않는다. 이미 입력된 문자의 길이가 현재 지정한 문자의 길이보다 긴 경우 최대 입력 가능한 문자길이 까지만 데이타로 재 설정한다. 입력 가능한 최대 문자수가 지정된 경우 문자수가 최대 문자수보다 작은 경우에만 입력이 이루어 지며, 그 외의 경우에는 입력이 무시된다. 입력 가능한 최대 문자수가 '0'이거나 '-1'보다 작은 경우 IllegalArgumentException이 발생한다.

**매개 변수**

- `maxLen` - 입력가능한 최대 문자수 Throws
- `IllegalArgumentException` - '0'이거나 '-1'보다 작은 경우 getMaxLength
- `public` - int getMaxLength() 현재 설정된 최대 입력가능한 문자수를 반환한다. 기본적으로 설정된 값을 '-1'이며, 이 경우 입력 가능한 문자수를 제한하지 않는다.

**반환 값**

최대 입력 가능한 문자수 getString public String getString() 현재의 문자 데이타를 반환한다. 현재 문자열에 null을 지정한 경우 ""(empty string)를 반환한다.

**반환 값**

문자 데이타.

**참고 항목**

setString(String data)

#### insert

public void insert(char[] data, int offset, int len, int index) 현재 화면에 출력된 문자 데이타에서 인자로 주어진 문자 데이타를 index 위치에 추가한다. data가 null인 경우 NullPointerException이 발생하고, index값이 '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우 IndexOutOfBoundsException이 발생한다. 입력 가능한 최대 문자 수가 제한된 경우에 현재 출력된 문자 데이타의 길이와 len을 합한 값이 최대문자수 보다 큰 경우 IllegalArgumentException이 발생한다.

**매개 변수**

- `data` - 새로 추가할 문자 데이타
- `offset` - 새로 추가할 문자 데이타에서 추가될 문자 데이타의 시작 위치
- `len` - 새로 추가할 문자데이타의 길이
- `index` - 현재 화면에 출력된 문자데이타에서 새로운 문자 데이타를 추가할 위치 Throws
- `NullPointerException` - data가 null인 경우
- `IndexOutOfBoundsException` - index값이 '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우
- `IllegalArgumentException` - 입력 가능한 최대 문자 수가 제한된 경우에 현재 출력된 문자 데이타의 길이와 len을 합한 값이 최대문자수 보다 큰 경우
- `IllegalArgumentException` - 입력할 문자데이타에 현재의 입력제한자에 맞지 않은 문자데이타가 포함된 경우 delete
- `public` - void delete(int index, int len) 현재 화면에 보여지고 있는 문자데이타의 index위치에서부터 len길이만큼 데이타를 삭제한다.
- `index값이` - '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우
- `IndexOutOfBoundsException이` - 발생한다. len는 현재 출력된 문자 데이타의 전체 길이를 초과 할 수 없으며 초과 할 경우 IllegalArgumentException이 발생한다.

**매개 변수**

- `index` - 삭제 위치.
- `len` - 삭제 할 문자데이타 길이 Throws
- `IndexOutOfBoundsException` - len,index값이 '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우
- `IllegalArgumentException` - len이 현재 출력된 문자 데이타의 전체 길이를 초과 한 경우 getConstraint
- `public` - int getConstraint() 현재 지정된 문자 데이타 입력 제한자를 반환한다. 기본적으로 지정되어 있는 입력 제한자는 CONSTRAINT_ANY이다.

**반환 값**

constraints 입력 제한자 focusNotify public void focusNotify(boolean b) 포커스를 받게 되면 불려진다. 현재 화면에 출력된 상태에서 포커스를 받으면 현재 화면에 입력 상태를 알려주는 입력 모드 카드를 화면에 출력하고, 포커스를 받지 않게 되면 입력 상태를 알려주는 입력 모드 카드를 화면에서 제거한다. Overrides focusNotify in class Component

**매개 변수**

- `b` - focus를 가질 땐 true,가지지 않을 땐 false showNotify
- `protected` - void showNotify(boolean bShow) 이하 메소스 설명은 Component 클래스에서 복사되었음 화면의 내용이 보이면 호출된다. addComponent나 removeComponent에 의해서 불리거나, 자신의 맨 상위의 부모 컴포넌트(ShellComponent)가 show에 의해서 화면에 나타날 때 호출된다. Overrides
- `showNotify` - in class Component
- `Following` - copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `bShow` - 컴포넌트가 나타나는지 안 나타나는지 여부 setFont
- `public` - void setFont(Font f) 폰트를 지정한다. 기본적으로 폰트는 Font.getDefaultFont()를 통해서 지정되어 있다.

**매개 변수**

- `f` - 새로 지정할 폰트

**참고 항목**

getFont()

#### getFont

public Font getFont() 폰트를 얻어온다.

**반환 값**

현재 사용중인 폰트

**참고 항목**

setFont(Font f)

#### keyNotify

public boolean keyNotify(int type, int key) 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력값이 된다. EventQueue.SOFT1키를 누르면 입력 모드를 변경할 수 있고, 숫자키 입력에 대한 문자 처리를 담당하고 있는 InputMethodHandler의 notifykeyInput메소드에 대한 실행을 관리하고 있다. 기타 전체 화면으로 문자 편집을 하기 위한 제어를 담당한다. 방향키에 대한 처리는 각 하위 클래스인 TextFieldComponent와 TextBoxComponent에서 구현하고 있다. Overrides keyNotify in class Component

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED` - 이 됨
- `key` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. Class TextFieldComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.TextComponent | +--org.kwis.msp.lwc.TextFieldComponent public class TextFieldComponent extends TextComponent TextFieldComponent는 TextComponent를 상속한 클래스로 한 라인에서 문자 편집을 한다. 이 컴포넌트의 넓이는 입력된 문자 데이타에 맞도록 자동으로 변경된다. 전체 화면을 사용하여 문자 편집을 할 수 있으며, 특정 문자열만을 입력하도록 입력제한을 할 수 있다. TextComoponent에서 정의된 입력 제한자에 대한 내용을 참고하세요. 기본적으로 최대 입력 가능한 문자열에 대한 제한은 하지 않으며, TextComponent.setMaxLength(int maxLen)를 통해서 최대 입력가능한 문자수를 제한 할 수 있다.

**참고 항목**

TextComponent, TextBoxComponent Fields inherited from class org.kwis.msp.lwc.TextComponent charCount, constChecker, constraint, CONSTRAINT_ANY, CONSTRAINT_NUMBER, CONSTRAINT_PASSWORD, display, f, imHandler, iMode, isWide, m_cPos, m_td, maxLength, modeViewer, tShell Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.TextComponent focusNotify, getConstraint, getFont, getMaxLength, getString, setFont, setMaxLength, setString, showNotify Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, configure, getBackground, getCard, getForeground, getHeight, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, layout, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, toString, validate Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 생성자 상세 설명

#### TextFieldComponent

public TextFieldComponent(String data, int constraint) 주어진 문자 데이타와 입력 제한자로 TextFieldComponent의 인스턴스를 생성한다. 문자 데이타는 null값을 가질 수 있다. 지정한 입력 제한자가 TextComponent.CONSTRAINT_NUMBER, TextComponent.CONSTRAINT_PASSWORD, TextComponent.CONSTRAINT_ANY이외의 값이 지정된 경우 IllegalArgumentException이 발생하며, 문자데이타가 입력 제한자에 어긋난 데이타를 포함하는 경우 IllegalArgumentException이 발생한다. 기본적으로 최대 입력 가능한 문자열에 대한 제한은 하지 않으며, TextComponent.setMaxLength(int maxLen)를 통해서 최대 입력가능한 문자수를 제한 할 수 있다.

**매개 변수**

- `data` - 문자데이타 혹은 null
- `constraints` - 문자 입력 형태 메쏘드 상세 설명 insert
- `public` - void insert(char[] data, int offset, int len, int index) 이하 메소스 설명은 TextComponent 클래스에서 복사되었음 현재 화면에 출력된 문자 데이타에서 인자로 주어진 문자 데이타를 index 위치에 추가한다.
- `data가` - null인 경우 NullPointerException이 발생하고, index값이 '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우 IndexOutOfBoundsException이 발생한다. 입력 가능한 최대 문자 수가 제한된 경우에 현재 출력된 문자 데이타의 길이와 len을 합한 값이 최대문자수 보다 큰 경우 IllegalArgumentException이 발생한다. Overrides
- `insert` - in class TextComponent
- `Following` - copied from class: org.kwis.msp.lwc.TextComponent

**매개 변수**

- `data` - 새로 추가할 문자 데이타
- `offset` - 새로 추가할 문자 데이타에서 추가될 문자 데이타의 시작 위치
- `len` - 새로 추가할 문자데이타의 길이
- `index` - 현재 화면에 출력된 문자데이타에서 새로운 문자 데이타를 추가할 위치 Throws
- `NullPointerException` - data가 null인 경우
- `IndexOutOfBoundsException` - index값이 '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우
- `IllegalArgumentException` - 입력 가능한 최대 문자 수가 제한된 경우에 현재 출력된 문자 데이타의 길이와 len을 합한 값이 최대문자수 보다 큰 경우
- `IllegalArgumentException` - 입력할 문자데이타에 현재의 입력제한자에 맞 지 않은 문자데이타가 포함된 경우 delete
- `public` - void delete(int index, int len) 이하 메소스 설명은 TextComponent 클래스에서 복사되었음 현재 화면에 보여지고 있는 문자데이타의 index위치에서부터 len길이만큼 데이타를 삭제한다.
- `index값이` - '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우
- `IndexOutOfBoundsException이` - 발생한다. len는 현재 출력된 문자 데이타의 전체 길이를 초과 할 수 없으며 초과 할 경우 IllegalArgumentException이 발생한다. Overrides
- `delete` - in class TextComponent
- `Following` - copied from class: org.kwis.msp.lwc.TextComponent

**매개 변수**

- `index` - 삭제 위치.
- `len` - 삭제 할 문자데이타 길이 Throws
- `IndexOutOfBoundsException` - len,index값이 '0'보다 작거나 현재 화면에 출력된 문자 데이타의 전체 길이보다 큰 경우
- `IllegalArgumentException` - len이 현재 출력된 문자 데이타의 전체 길이를 초과 한 경우 getPreferredWidth
- `public` - int getPreferredWidth() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 폭을 결정한다. Container에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides
- `getPreferredWidth` - in class Component
- `Following` - copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 폭. getPreferredHeight public int getPreferredHeight() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. ContainerComponent에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 높이 getPreferredHeight public int getPreferredHeight(int wr) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. 지정된 제한된 폭을 가질 경우의 컴포넌트의 높이를 돌려준다. 만일 LabelComponent 나 TextFieldComponent, TextAreaComponent와 같이 포맷팅이 가능한 컴포넌트인 경우에는 가변 폭을 가질 수가 있다. 가변 폭을 가지게 되면, 폭에 따라서 높이가 달라지게 된다. 이때 이 함수를 통해서 컴포넌트의 높이를 얻어 온다. 만일, w가 -1이 면 폭에 제한이 없는 것으로 계산된다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `w` - 가변폭.

**반환 값**

컴포넌트의 높이. paintContent public void paintContent(Graphics g) 이하 메소스 설명은 Component 클래스에서 복사되었음 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides paintContent in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics

#### keyNotify

public boolean keyNotify(int type, int key) 이하 메소스 설명은 TextComponent 클래스에서 복사되었음 키 입력을 받으면 호출된다. 사용자가 키를 입력하면, setFocus함수에 의해서 입력 포커스를 가지는 컴포넌트의 이 함수가 호출된다. type은 KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED이며, chr는 키 입력값이 된다. EventQueue.SOFT1키를 누르면 입력 모드를 변경할 수 있고, 숫자키 입력에 대한 문자 처리를 담당하고 있는 InputMethodHandler의 notifykeyInput메소드에 대한 실행을 관리하고 있다. 기타 전체 화면으로 문자 편집을 하기 위한 제어를 담당한다. Overrides keyNotify in class TextComponent Following copied from class: org.kwis.msp.lwc.TextComponent

**매개 변수**

- `type` - 키 입력의 타입; 키를 누르는 경우 KEY_PRESSED, 키를 떼면 KEY_RELEASED, 키를 연속적으로 누르면 KEY_REPEATED, 한번 눌려서 떼 인 경우라면
- `KEY_TYPED` - 이 됨
- `key` - 눌린 키의 문자; '0'-'9'와 '*', '#'은 기본이며 이외의 문자도 넘어 올 수 있다.

**반환 값**

만일 컴포넌트가 인수로 넘어오는 키를 이 컴포넌트가 처리했다면, true를 넘겨 준다. 그렇지 않았다면 false를 돌려준다. Class TickerComponent java.lang.Object | +--org.kwis.msp.lwc.Component | +--org.kwis.msp.lwc.TickerComponent public class TickerComponent extends Component TickerComponent는 문자열과 이미지로 구성되면 우측에서 좌측으로 움직이는 컴포넌트이다. 좌측으로 이동하여 문자열의 끝이 좌측으로 사라지면 다시 문자열의 처음부터 우측에서 보여지게 되어 동일한 방향으로 이동을 계속한다. TickerComponent의 넓이 값은 TickerComponent를 추가한 ContainerComponent의 넓이 값과 같으며, 높이는 이미지가 문자의 한 줄 높이보다 작은 경우 한 줄 높이 값을 가지며, 이미지의 높이가 더 큰 경우 이미지 높이 값을 가지게 된다. 움직이는 속도는 setDelay(int)메소드를 사용하여 변경할 수 있다. 이 때 지정해주는 시간 값은 milliseconds 단위이다. 기본으로 설정된 값은 DEFAULT_DELAY이다. 움직임 속도 값은 '-'값은 지정될 수 없으며, '-'값이 지정된 경우 IllegalArgumentException이 발생된다. TickerComponent에서는 움직임을 제어할 수 있는 기능을 제공하고 있다. 움직임 상태는 setTickerState(boolean)메소드를 사용하여 제어할 수 있다. true값이 지정되면 움직이고, false값이 지정되면 움직임을 멈추게 된다. 기본적으로 움직임 상태에 지정된 값은 true이다. TickerComponent는 서로 다른 ContainerComponent에 공유되어 사용될 수 없다. 공유되어 사용될 경우 IllegalArgumentException이 발생된다. Fields inherited from class org.kwis.msp.lwc.Component bg, evtListener, evtListenerObj, fg, FOCUS_NOTIFY, h, HAS_FOCUS_MASK, INPUT_MASK, KEY_NOTIFY, KEY_PRESSED, KEY_RELEASED, KEY_REPEATED, KEY_TYPED, LAYOUT_BOTTOM, LAYOUT_HCENTER, LAYOUT_LEFT, LAYOUT_RIGHT, LAYOUT_TOP, LAYOUT_VCENTER, mask, parent, POINT_DRAGGED, POINT_PRESSED, POINT_RELEASED, POINTER_NOTIFY, POS_MASK, PREFER_SIZE_MASK, prefH, prefW, SHOW_NOTIFY, SIZE_MASK, VALID_MASK, w, x, y Methods inherited from class org.kwis.msp.lwc.Component calcPreferredSize, canHandleInput, configure, focusNotify, getBackground, getCard, getForeground, getHeight, getWidth, getX, getXOnScreen, getY, getYOnScreen, hasFocus, invalidate, isShown, isValid, keyNotify, layout, pointerNotify, processEvent, repaint, repaint, serviceRepaints, setBackground, setEventListener, setFocus, setForeground, showNotify, toString, validate Methods inherited from class java.lang.Object equals, getClass, hashCode, notify, notifyAll, wait, wait, wait 필드 상세 설명 DEFAULT_DELAY public int DEFAULT_DELAY TickerComponent의 기본 움직임 속도 값. 500 milliseconds 생성자 상세 설명 TickerComponent public TickerComponent(String str, Image img) TickerComponent의 인스턴스를 생성한다. 기본적으로 움직임 상태 값에는 true값이 지정되어 있고, 데이타가 움직이는 상태이다. 또한 움직이는 속도 값은 DEFAULT_DELAY이다. 문자 데이타는 null값을 가질 수 없으며, null인 경우 NullPointerException이 발생한다. 이미지 데이타는 null값을 가질 수 있다.

**매개 변수**

- `str` - TickerComponent의 문자 데이타
- `img` - TickerComponent의 이미지 데이타 혹은 null Throws
- `NullPointerException` - 문자 데이타가 null인 경우 메쏘드 상세 설명 setString
- `public` - void setString(String str) 화면에 출력될 TickerComponent의 문자 데이타를 지정한다. 이미 지정된 데이타가 존재하면 새로 지정한 데이타로 문자열이 변경된다. 문자 데이타는 null이 될 수 없으며, null 값을 지정한 경우 NullPointerException이 발생된다.

**매개 변수**

- `str` - TickerComponent의 문자 데이타 Throws
- `NullPointerException` - 문자데이타 str이 null인 경우

**참고 항목**

getString(), setImage(Image img)

#### getString

public String getString() TickerComponent의 문자 데이타를 얻어온다.

**반환 값**

string TickerComponent의 문자 데이타

**참고 항목**

setString(String str)

#### setImage

public void setImage(Image img) TickerComponent의 이미지 데이타를 지정한다. 이미 지정된 데이타가 존재하면 새로 지정한 데이타로 변경 된다.

**매개 변수**

- `img` - TickerComponent의 이미지 데이타. img가 null인 경우 기존 이미지를 삭제한다.

**참고 항목**

getImage(), setString(String str)

#### getImage

public Image getImage() TickerComponent의 이미지 데이타를 전달한다.

**반환 값**

img TickerComponent의 이미지 데이타.

**참고 항목**

setImage(Image img)

#### setDelay

public void setDelay(int delay) TickerComponent의 문자 흐름 속도를 설정한다. 기본으로 설정된 흐름 속도값은 DEFAULT_DELAY이다. 흐름 속도값이 큰 값일 수록 문자 흐름 속도가 느려진다. 이 값을 milliseconds 단위이며, '-'의 값을 지정할 수 없다. '-'값을 지정하면 IllegalArgumentException이 발생한다.

**매개 변수**

- `delay` - 문자 속도 값.milliseconds 단위 Throws
- `IllegalArgumentException` - delay값이 '-'값인 경우 setTickerState
- `public` - boolean setTickerState(boolean st)
- `TickerComponent의` - 움직임/정지 상태를 설정한다.
- `true값이` - 지정되면 움직이고, false값이 지정되면 움직임을 멈추게 된다. 기본적으로 움직임 상태에 지정된 값은 true이다.

**매개 변수**

- `st` - true : 문자,이미지 움직임 false: 움직임 정지. getPreferredHeight
- `public` - int getPreferredHeight(int w) 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. 지정된 제한된 폭을 가질 경우의 컴포넌트의 높이를 돌려준다. 만일 LabelComponent 나 TextFieldComponent,
- `TextAreaComponent와` - 같이 포맷팅이 가능한 컴포넌트인 경우에는 가변 폭을 가질 수가 있다. 가변 폭을 가지게 되면, 폭에 따라서 높이가 달라지게 된다. 이때 이 함수를 통해서 컴포넌트의 높이를 얻어 온다. 만일, w가 -1이 면 폭에 제한이 없는 것으로 계산된다. Overrides
- `getPreferredHeight` - in class Component
- `Following` - copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `w` - 가변폭.

**반환 값**

컴포넌트의 높이. getPreferredHeight public int getPreferredHeight() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 높이를 결정한다. ContainerComponent에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredHeight in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 높이 getPreferredWidth public int getPreferredWidth() 이하 메소스 설명은 Component 클래스에서 복사되었음 컴포넌트의 적절한 폭을 결정한다. Container에서 컴포넌트의 크기를 결정할 때에 이 함수가 돌려주는 값을 참조하여 결정한다. Overrides getPreferredWidth in class Component Following copied from class: org.kwis.msp.lwc.Component

**반환 값**

컴포넌트의 폭. paintContent public void paintContent(Graphics g) 이하 메소스 설명은 Component 클래스에서 복사되었음 내부를 칠한다. 먼저 validate함수를 호출하여, 컴포넌트의 위치를 유효화(컴포넌트의 위치와 크기 재 계산)한 후 내부의 색상으로 화면을 칠하게 된다. 색상이 -1이면, 칠하진 않는다. Overrides paintContent in class Component Following copied from class: org.kwis.msp.lwc.Component

**매개 변수**

- `g` - 칠할 Graphics.

**참고 항목**

Graphics
