'''
Memento Design Pattern
[https://www.oodesign.com/images/design_patterns/structural/memento-design-pattern-implementation-uml-class-diagram.png]


The intent of this pattern is to capture the internal state of an object without violating encapsulation and thus providing a mean for restoring the object into initial state when needed.


Implementation

The figure below shows a UML class diagram for the Memento Pattern:
Memento Pattern Implementation - UML Class Diagram

Memento
- Stores internal state of the Originator object. The state can include any number of state variables.
- The Memento must have two interfaces, an interface to the caretaker. This interface must not allow any operations or any access to internal state stored by the memento and thus honors encapsulation. The other interface is to the originator and allows the originator to access any state variables necessary to for the originator to restore previous state.

Originator
- Creates a memento object capturing the originators internal state.
- Use the memento object to restore its previous state.

Caretaker
- Responsible for keeping the memento.
- The memento is opaque to the caretaker, and the caretaker must not operate on it.

'''

class Memento:
    def __init__(self,value):
        self.state = value

    def SetState(self,value):
        self.state = value

    def GetState(self):
        return self.state


class Originator:
    def SetState(self,value):
        self.state = value
    def GetState(self):
        return self.state

    def CreateMemento(self):
        return(Memento(self.state))

    def SetMemento(self,memento):
        print("going to previous state")
        self.state = memento.GetState()

class Caretaker:
    def __init__(self,originatorObj):
        self.memento = None
        self.origin = originatorObj

    def Execute(self):
        self.memento = self.origin.CreateMemento()
        self.origin.SetState(0)

    def Unexecute(self):
        self.origin.SetMemento(self.memento)

originator = Originator()
#Setting initial state to 1
originator.SetState(1)
print(f"The state value is: {originator.GetState()}")

caretaker = Caretaker(originator)
#change the state to 0
caretaker.Execute()
print(f"The state value is: {originator.GetState()}")

#Back to state 1
caretaker.Unexecute()
print(f"The state value is: {originator.GetState()}")