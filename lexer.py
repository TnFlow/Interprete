from enum import Enum

class TOKEN_TYPE(Enum):
  IN_PRINT = 0,

  DI_LEARN = 101
  DI_TRAUMA = 102

  DI_CHALLENGE = 111
  DI_COMPLETED = 112

  DI_MASTER = 121
  DI_SHOWOFF = 122

  DI_GRIND = 131
  DI_OVER = 132

  EOF = 1000

class Token():
  def __init__(self, type : TOKEN_TYPE, string : str = '', arg1 : str = '', arg2 : str = '', arg3 : str = ''):
    self.type = type
    self.string = string
    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

  def print_attributes(self):
    print(f"t: {self.type}", end=" ")
    print(f"s: '{self.string}'", end=" ")
    print(f"arg1: '{self.arg1}'", end=" ")
    print(f"arg2: '{self.arg2}'", end=" ")
    print(f"arg3: '{self.arg3}'", end="\n")

class Lexer:
  def __init__(self, input : str):
    self.input = input

  def lex(self) -> list[Token]:
    
    #print("[DBG] lexing...")

    tokens : list[Token] = []
    strings = []

    for sl in self.input.split('\n'):
      for s in sl.split(' '):
        strings.append(s)

    #print(f"[DBG] strings: {strings}")

    while strings:
      s = strings.pop(0)

      if s == ' ': continue
      if s == '\n': continue
      if s == '\t': continue
      if s == '': continue

      if s == "print":
        arg1 = strings.pop(0)

        tokens.append(Token(TOKEN_TYPE.IN_PRINT, s, arg1))

      if s == "learn":
        arg1 = strings.pop(0)
        arg2 = strings.pop(0)

        tokens.append(Token(TOKEN_TYPE.DI_LEARN, s, arg1, arg2))

      if s == "trauma":
        arg1 = strings.pop(0)
        arg2 = strings.pop(0)

        tokens.append(Token(TOKEN_TYPE.DI_TRAUMA, s, arg1, arg2))

      if s == "master":
        arg1 = strings.pop(0)
        arg2 = ""
        while strings:
          sa = strings.pop(0)

          if sa == "skill":
            break

          arg2 += f" {sa}"

        tokens.append(Token(TOKEN_TYPE.DI_MASTER, s, arg1, arg2))

      if s == "showoff":
        arg1 = strings.pop(0)

        tokens.append(Token(TOKEN_TYPE.DI_SHOWOFF, s, arg1))

      if s == "challenge":
        arg1 = strings.pop(0)
        arg2 = strings.pop(0)
        arg3 = strings.pop(0)

        tokens.append(Token(TOKEN_TYPE.DI_CHALLENGE, s, arg1, arg2, arg3))

      if s == "completed":
        tokens.append(Token(TOKEN_TYPE.DI_COMPLETED, s))

      if s == "grind":
        arg1 = strings.pop(0)
        tokens.append(Token(TOKEN_TYPE.DI_GRIND, s, arg1))

      if s == "over":
        tokens.append(Token(TOKEN_TYPE.DI_OVER, s))

    tokens.append(Token(TOKEN_TYPE.EOF, ''))

    # print(f"[DBG] tokens:")

    # for t in tokens:
    #   t.print_attributes()

    return tokens