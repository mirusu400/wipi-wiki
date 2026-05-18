# Class IllegalStateException

`package java.lang`

```text
java.lang.Object
  |
  +--java.lang.Throwable
        |
        +--java.lang.Exception
              |
              +--java.lang.RuntimeException
                    |
                    +--java.lang.IllegalStateException
```

## 설명

**extends RuntimeException:**

Signals that a method has been invoked at an illegal or
 inappropriate time. In other words, the Java environment or
 Java application is not in an appropriate state for the requested
 operation.

**Since:**
- JDK1.1

## 생성자 요약

- IllegalStateException () Constructs an IllegalStateException with no detail message.
- IllegalStateException ( String s) Constructs an IllegalStateException with the specified detail
 message.

## 생성자 상세

### IllegalStateException

```java
public IllegalStateException()
```

- Constructs an IllegalStateException with no detail message.
 A detail message is a String that describes this particular exception.

### IllegalStateException

```java
public IllegalStateException(String s)
```

**Parameters:**
- `s` - the String that contains a detailed message

***AromaSoft Corp. Proprietary and Confidential***

*(C)opyright 2003 AromaSoft Corp. All right reserved. 
Contact : [contact@aromasoft.com](mailto:contact@aromasoft.com)*
