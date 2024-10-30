import sys
import hashlib
from traumaMemory import TraumaMemory
from longMemory import LongMemory
from lexer import Lexer, TOKEN_TYPE

class PsicInterpreter:
  def __init__(self):
    self.longMemory : LongMemory = LongMemory()

    exe_path = sys.argv[1].replace("C:", "hsihisishi")

    print(f"exe_path: {exe_path}")

    # the execution path is the trauma memory hash
    hash_ = hashlib.sha1(exe_path.encode("utf-8")).hexdigest()
    #hash_ = str(hash_).replace("-", "")

    self.traumaMemory : TraumaMemory = TraumaMemory(hash_)

    self.functions = {}

  def get_variable(self, name):
    if self.longMemory.exists(name):
      return self.longMemory.get(name)
    
    if self.traumaMemory.exists(name):
      return self.traumaMemory.get(name)

    return None

  def eval(self, input : str):
    
    self.lexer = Lexer(input)
    lex = self.lexer.lex()

    while lex:

      token = lex.pop(0)

      if token.type == TOKEN_TYPE.IN_PRINT:
        v = self.get_variable(token.arg1)
        
        if v:
          print(v)
        else:
          print(token.arg1)

      if token.type == TOKEN_TYPE.DI_LEARN:
        self.longMemory.set(token.arg1, token.arg2)

      if token.type == TOKEN_TYPE.DI_TRAUMA:
        self.traumaMemory.set(token.arg1, token.arg2)

      if token.type == TOKEN_TYPE.DI_MASTER:
        self.functions[token.arg1] = token.arg2

      if token.type == TOKEN_TYPE.DI_SHOWOFF:
        if token.arg1 in self.functions:
          self.eval(self.functions[token.arg1])
        else:
          raise Exception(f"{token.arg1} is not defined!")
        
      if token.type == TOKEN_TYPE.DI_CHALLENGE:
        arg1 = self.get_variable(token.arg1)
        if not arg1: arg1 = token.arg1
        try:
          arg1 = (float(arg1))
        except:
          arg1 = arg1

        arg3 = self.get_variable(token.arg3)
        if not arg3: arg3 = token.arg3
        try:
          arg3 = float(arg3)
        except:
          arg3 = arg3
        
        res = False

        if token.arg2 == '>': res = arg1 > arg3
        
        if token.arg2 == "<": res = arg1 < arg3

        if token.arg2 == '==': res = arg1 == arg3

        if not res:
          while lex:
            ti = lex.pop(0)

            if ti.type == TOKEN_TYPE.DI_COMPLETED:
              break

      if token.type == TOKEN_TYPE.DI_GRIND:
        t_block = []

        arg1 = int(token.arg1)

        while lex:
          ti = lex.pop(0)

          if ti.type == TOKEN_TYPE.DI_OVER:
            break

          t_block.append(ti)

        for _ in range(arg1):
          lex = t_block + lex

if __name__ == "__main__":

  interpreter = PsicInterpreter()

  script = """
    print dead
  """

  interpreter.eval(script)