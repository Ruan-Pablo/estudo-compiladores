from Repl import *
from ASM import ASM
from Util import Util
from Consts import Consts

def prompt():
  ASM.newFile()
  ASM.setStart("_start")
  Repl().cmdloop()
  ASM.setReturnDefault(1)
  for s in ASM.stack:
    Util.writeFileAppend(Consts.ASM, s)
    print(s, end='')

if __name__ == "__main__":
  prompt()

