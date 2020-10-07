'''
Behavioral - State - Design Pattern
[https://refactoring.guru/design-patterns/state/python/example]

Usage examples: The State pattern is commonly used in Python to convert massive switch-base state machines into the objects.

Identification: State pattern can be recognized by methods that change their behavior depending on the objects’ state, controlled externally.

Conceptual Example
This example illustrates the structure of the State design pattern. It focuses on answering these questions:

- What classes does it consist of?
- What roles do these classes play?
- In what way the elements of the pattern are related?
'''

# States of a computer

class ComputerState(object):
    """ Abstract base class of state of a computer """
    
    name = "state"
    allowed = []
    
    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print ('Current:',self) # => switched to new state',state.name         
            self.__class__ = state
        else:
            print ('Current:',self) # => switching to',state.name,'not possible.'

    def __str__(self):
        return self.name
    
class Off(ComputerState):
    """ State being switched off """

    name = "off"
    allowed = ['on']

class On(ComputerState):
    """ State of being powered on and working """

    name = "on"
    allowed = ['off','suspend','hibernate']

class Suspend(ComputerState):
    """ State of being in suspended mode after switched on """

    name = "suspend"
    allowed = ['on']

class Hibernate(ComputerState):
    """ State of being in hibernation after powered on """

    name = "hibernate"
    allowed = ['on']

class Computer(object):
    """ A class representing a computer """

    def __init__(self, model='HP'):
        self.model = model
        # State of the computer - default is off.
        self.state = Off()

    def change(self, state):
        """ Change state """

        self.state.switch(state)

if __name__ == "__main__":
    comp = Computer()
    # Switch on
    comp.change(On)
    # Switch off
    comp.change(Off)

    # Switch on again
    comp.change(On)
    # Suspend
    comp.change(Suspend)
    # Try to hibernate - cannot!
    comp.change(Hibernate)
    # switch on back
    comp.change(On)
    # Finally off
    comp.change(Off)