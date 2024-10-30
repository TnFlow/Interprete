import sys
from interpreter import PsicInterpreter

if __name__ == "__main__":

  interpreter = PsicInterpreter()

  with open(sys.argv[1], 'r') as file:

    script = file.read()

    interpreter.eval(script)