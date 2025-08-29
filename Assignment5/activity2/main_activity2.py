class Bicycle:
  def move(self,action):
    self.action = action

    print(f"A bicycle can {self.action}.")

class Plane(Bicycle):
  def move(self,action):
    self.action = action 

    print(f"Aeroplane can {self.action}.")

class Animals(Bicycle):
  def move(self,action):
    self.action = action 

    print(f"Animals move with {self.action} legs.")
  
flying = Plane()
flying.move("fly")

wheels = Bicycle()
wheels.move("brake")




