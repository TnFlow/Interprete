class ShortMemory:
  def __init__(self):
    self.memory_limit = 10
    self.__memory = []

  def set(self, name, value):
    if len(self.__memory) > self.memory_limit:
      self.__memory.pop()

    self.__memory.append((name, value))

  def exists(self, name):
    for mem in self.__memory:
      if mem[0] == name:
        return True
      
    return False
  
  def get(self, name):
    if self.exists(name):
      for mem in self.__memory:
        if mem[0] == name:
          return mem[1]

