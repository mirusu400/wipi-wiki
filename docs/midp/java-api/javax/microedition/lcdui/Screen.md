# Class Screen

`package javax.microedition.lcdui`

```
java.lang.Object
  |
  +--javax.microedition.lcdui.Displayable
        |
        +--javax.microedition.lcdui.Screen
```

## 설명

**Direct Known Subclasses:**
- `Alert`, `Form`, `List`, `TextBox`

**extends Displayable:**

고급 사용자 인터페이스 클래스의 공통 수퍼 클래스. 
표시되는 내용과 사용자와의 상호 작용은 
서브 클래스에서 정의합니다.

응용 프로그램은 서브 클래스가 정의한 메소드를 사용하여 
`Screen` 객체가 사용자에게 표시되는 동안 
해당 내용을 변경할 수 있습니다. 
이런 경우 `Screen` 객체가 가시적이면 디스플레이는 
자동으로 업데이트됩니다. 
즉, 응용 프로그램이 추가 작업을 
수행하기를 기다리지 않고 적절한 시기에 디스플레이를 갱신합니다. 
예를 들어, 현재 `List` 객체가 표시되어 있다면 
`List`의 모든 요소가 가시적입니다. 
응용 프로그램이 `List`의 시작 부분에 
새 요소를 삽입하면 이 요소는 즉시 표시되고 
다른 요소는 적절하게 다시 정렬됩니다. 
응용 프로그램이 디스플레이를 갱신하기 위해 다른 메소드를 
호출할 필요는 없습니다.

응용 프로그램은 `Screen`이 가시적이 아닐 때 
즉, 다른 `Displayable`이 
표시되어 있을 때에만 
그 내용을 변경하는 것이 좋습니다. 
`Screen`이 가시적일 때 
그 내용을 변경하면 일부 장치에서 
성능 문제가 발생할 수 있고 
사용자가 `Screen`과 상호 작용하고 있는 동안 
그 내용이 변경되면 혼동을 야기할 수도 있습니다.

MIDP 2.0에서는 읽기/쓰기 표시기와 
제목 속성을 정의하는 
4개의 `Screen` 메소드를 `Screen`의 
수퍼 클래스인 `Displayable`로 옮겼습니다. 
이러한 메소드의 의미는 변경되지 않았습니다.

**Since:**
- MIDP 1.0

Methods inherited from class javax.microedition.lcdui. Displayable addCommand , getHeight , getTicker , getTitle , getWidth , isShown , removeCommand , setCommandListener , setTicker , setTitle , sizeChanged

Methods inherited from class java.lang. Object equals , getClass , hashCode , notify , notifyAll , toString , wait , wait , wait
