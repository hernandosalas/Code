'''
Creational - Singleton - Design Pattern

Usage examples: A lot of developers consider the Singleton pattern an antipattern. That’s why its usage is on the decline in Python code.

Identification: Singleton can be recognized by a static creation method, which returns the same cached object.
'''

class Singleton:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
s = Singleton()
print (s)

s = Singleton.getInstance()
print (s)

s = Singleton.getInstance()
print (s)

a = Singleton()
print(a)