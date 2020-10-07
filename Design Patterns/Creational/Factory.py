'''
Creational - Factory - Design Pattern

Usage examples: The Factory Method pattern is widely used in Python code. It’s very useful when you need to provide a high level of flexibility for your code.

Identification: Factory methods can be recognized by creation methods, which create objects from concrete classes, but return them as objects of abstract type or interface.

Conceptual Example

This example illustrates the structure of the Factory Method design pattern. It focuses on answering these questions:

What classes does it consist of?
What roles do these classes play?
In what way the elements of the pattern are related?
'''

class Button(object):
   html = ""
   def get_html(self):
      return self.html

class Image(Button):
   html = "<img></img>"

class Input(Button):
   html = "<input></input>"

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():
   def create_button(self, typeButton):
        if typeButton == "Image":
           return Image()
        elif typeButton == "Input":
           return Input()
        elif typeButton == "Flash":
           return Flash()


button_factory = ButtonFactory()
button = button_factory.create_button("Image").get_html()
print(button)
button = button_factory.create_button("Input").get_html()
print(button)
button = button_factory.create_button("Flash").get_html()
print(button)