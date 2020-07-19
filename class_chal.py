# Parent class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
      msg = "Hello my name is {} I am {} years old.".format(self.name,self.age)
      return msg
    
# child class instance
class Child(Person):
  def __init__(self, name, age, parent):
    self.name = name
    self.age = age
    self.parent = parent

  def childfunc(self):
      msg = "Hello my name is {} I am {} years old my parents name is {}.".format(self.name,self.age,self.parent)
      return msg


    
if __name__ == "__main__":
    person = Person("John", 36)
    print(person.myfunc())

    child = Child("Billy", 12, "John")
    print(child.childfunc())
        
