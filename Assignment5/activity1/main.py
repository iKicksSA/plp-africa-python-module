class Chickens:

  print("Did You Know That:\n")

  class_statement = " - Chickens can remember over 100 different faces (both human and animal)."

  def __init__(self,eggs,age,fact):
    self.eggs = eggs
    self.age = age
    self.fact = fact

  def lay_eggs(self):
    print(f" - Chikens lay atleast {self.eggs} egg per day.")

  def statement(self):
    print(f"{self.fact}?")

  def longest_lived(self):
    print(f" - The world’s oldest chicken lived to be{self.age}")

  @classmethod
  def class_method(cls):
    return cls.class_statement


# Peanut class inherites the Chicken class
class Peanut(Chickens):

  # We also define the parent's attributes in the child constructor. I can say < we pass the values to the child since it inherited the parent >> then since the child has the parent's attributes it then passes the values to super(), since the attributes are constructed they are passed to the parent(chicken)
  def __init__(self,name,year,food,eggs,age,fact):

    # super() sends the values(attributes) to the parent class(chicken) that's how the values are passed to it.
    super().__init__(eggs,age,fact)
    self.name = name
    self.year = year
    self.food = food

  def peanut_details(self):
    print(f" - {self.name} was the oldest chicken to live for {self.age} years.\n - {self.name} was born in {self.year} and he very much loved eating {self.food}. ")


# All of the values are passed to the child class (aka The inheritor)
details = Peanut("Peanut",2002,"Yogurt",1,16," - Chickens are the closest living relatives of the Tyrannosaurus Rex")
fact1 = details.lay_eggs()
fact2 = details.statement()
fact3 = details.peanut_details()
fact4 = Peanut.class_method()
print(fact4)







   