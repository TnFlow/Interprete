class LongMemory:
  def __init__(self):
    self.__memory = {}

  def set(self, name, value):
    self.__memory[name] = value

  def exists(self, name):
    return name in self.__memory
  
  def get(self, name):
    if self.exists(name):
      return self.__memory[name]
  