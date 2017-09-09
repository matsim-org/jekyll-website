---
layout: default
title: Prefer composition / delegation over inheritance
---

# Prefer composition / delegation over inheritance

## Inheritance is not very robust

There are numerous hints that inheritance is not very stable under refactoring; see, for example, Bloch, "Effective Java".

## The short version

- If you think you need to use inheritance, restrict it to a package.  This can be 
achieved by making classes and methods only package-visible (no public/protected).  
Having it within a package makes the situation very local, and thus much better to manage.

- If you think you need to use inheritance beyond package limits, observe the following 
rule of thumb: Public or protected methods should be final or empty.
(Which implies: If you are extending a class from elsewhere, you should make all of your public or protected methods final.)

## The long version

### The problem

The problem has something to do with the sequence of program execution.  Assume

    class Base {
      run() {
        partA();
        partB();
      }
      partA() {
        do1();
        do2();
      }
      partB() {
        do3();
        do4();
      }
    ...
    
and some derived code

    class Derived extends Base {
      partA() {
        do1();
        doMyOwnStuff();
        do2();
      }
    ...

Now assume that the maintainer of the base class decides that `do3()` should be done before `do2()`.
Thus (for example):

    class Base {
      ...
      partA() {
        do1();
        do3();
        do2();
      }
      partB() {
        do4();
      }
      ...

Now the derived code will not execute `do3()` at all.

One may argue that this is a consequence of bad design of the base class, e.g. 
that `run()` should call the `doX()` methods directly, or the designer 
should know beforehand in which sequence something needs to be done.  
In practice, these arguments do not work: Levels of abstraction are difficult to get 
right from the start; and there may be situations where sequences of execution 
originally do not matter, and when it later turns out that they matter, 
they may be in the wrong sequence.

One may also argue that this is a consequence of bad design of the derived class, 
i.e. the programmer who overrides methods that have content should always 
call the super-method. That is

    class Derived extends Base {
      partA() {
        super.partA();
        doMyOwnStuff();
      }
      ...

(Note that this is not the same thing as above.)

However, the base class maintainers cannot enforce that class users (those who 
extend the base class) do this.  One may argue that this is the problem of 
the class users, but in our setup  test failures resulting from such issues 
are, as a tendency, the responsibility of the base class maintainer 
(since her or his code change broke the tests).

### Use delegation in Eclipse

We therefore suggest to prefer composition (=delegation) over inheritance 
where this is possible.  It is only possible when the class that one wants to 
inherit from implements an interface.  In that case, the following 
is possible (with Eclipse):

1. Write a class skeleton as follows:

        class MyClass implements XXXInterface {
          private XXXInterface delegate = new XXXImplementation(...);
        }
    
2. In Eclipse, go to menu "Source"/"Generate delegate methods" and follow the instructions.

[[Somebody please add a screenshot here. thanks. kai]]

This will delegate all method calls to `MyClass` to the delegate.  Now you can 
modify some of the delegate methods as you like.

(This sometimes seems to provide less access than inheritance, but I don't think this 
is true as long as you assume that internal variables/fields are always private.)

### The typical example

It is called "composition" since you can do this with more than one interface/delegate.  
The classical example is something like

    class MyCar implements HasSteering, HasBrakes, HasGears {
      private HasSteering steeringDelegate = new PowerSteering(...) ;
      private HasBrakes   brakesDelegate   = new SimpleBrakes(...) ;
      private HasGears    gearsDelegate    = new ElectronicGears(...) ;
    }

where Eclipse's "Generate delegate methods" will produce methods such as

    public void steerToRight(double value) {
      steeringDelegate.steerToRight(value);
    }
    ...
    public void brake(double value) {
      brakesDelegate.brake(value);
    }
 
As one can see, this now allows operations such as

    MyCar car ...
    ...
    car.brake(3.);
    car.steerToRight(0.3);
 
that is, the car is now composed of its internals.

### Exposing the delegates

In MATSim, we often expose the delegation, that is, the syntax is

    car.getBrakes().brake(3.);
    car.getSteering().steerToRight(0.3);
 
This has the advantage that, if you extend the interfaces, you do not need to adapt 
every implementation.  It is, clearly, not an option if you want to write a 
class (such as a `PlanStrategy`) that is later inserted into the code – that 
has to fulfill the contract defined by the interface.