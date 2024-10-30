import os

class TraumaMemory:
  def __init__(self, hash):
    self.__memory = {}
    self.hash = hash

    self.path = f"{self.hash}.txt"

  def load_memory(self):
    if not os.path.isfile(self.path): 
      with open(self.path, 'w') as file:
        file.write('{}')

    with open(self.path, "r") as file:
      raw = file.read()

      self.__memory = eval(raw)

  def set(self, name, value):
    self.load_memory()

    self.__memory[name] = value

    with open(self.path, 'w') as file:
      file.write(str(self.__memory))

  def exists(self, name):
    self.load_memory()

    return name in self.__memory
  
  def get(self, name):
    self.load_memory()

    return self.__memory[name]

  