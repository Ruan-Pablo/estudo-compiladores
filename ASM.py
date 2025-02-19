from Util import Util
from Consts import Consts
class ASM:
	fileName = Consts.ASM
	space = "  "
	ini = True
	stack = []

	@staticmethod
	def setStart(_start: str, nSpace=0):
		gbl = f"{ASM.tab(nSpace)}.globl {_start}\n"
		startDecl = f"{ASM.tab(nSpace)}{_start}:\n"
		ASM.stack.append(gbl + startDecl)
		return gbl + startDecl
	
	@staticmethod
	def setReturnDefault(nSpace=0):
		retA = f"{ASM.tab(nSpace)}mov $1, %eax\n"
		retB = f"{ASM.tab(nSpace)}int $0x80\n"
		ASM.stack.append(retA + retB)
		return retA + retB
	
	@staticmethod
	def addRegReg(n1: int, n2: int, regx="eax", regy="ebx", nSpace=0, preserveRY=False):
		setReg = ASM.setPreserve(n1, n2, regx, regy, nSpace, preserveRY)
		addCode = f"{ASM.tab(nSpace)}add %{regx}, %{regy}\n"
		ASM.stack.append(setReg + addCode)
		return setReg + addCode
	
	@staticmethod
	def subRegReg(n1: int, n2: int, regx="eax", regy="ebx", nSpace=0, preserveRY=False):
		setReg = ASM.setPreserve(n1, n2, regx, regy, nSpace, preserveRY)
		subCal = f"{ASM.tab(nSpace)}sub %{regx}, %{regy}\n"
		negCal = f"{ASM.tab(nSpace)}neg %{regy}\n"
		ASM.stack.append(setReg + subCal + negCal)
		return setReg + subCal + negCal

	@staticmethod
	def swapRegReg(regSource="eax", regTarget="ebx", nSpace=0):
		swap = f"{ASM.tab(nSpace)}mov %{regSource}, %{regTarget}\n"
		ASM.stack.append(swap)
		return swap

	@staticmethod
	def newFile():
		Util.createFile(ASM.fileName)
	
	def tab(n: int):
		s = ""
		for i in range(n):
			s = s + ASM.space
		return s

	@staticmethod
	def __movNumToRegister(num, regx="eax", nSpace=0):
		nReg = f"{ASM.tab(nSpace)}mov ${num}, %{regx}\n"
		return nReg

	@staticmethod
	def __setToRegs(n1: int, n2: int, regx="eax", regy="ebx", nSpace=0):
		nReg1 = ASM.__movNumToRegister(n1, regx, nSpace)
		nReg2 = ASM.__movNumToRegister(n2, regy, nSpace)
		return nReg1 + nReg2

	@staticmethod
	def setPreserve(n1: int, n2: int, regx="eax", regy="ebx", nSpace=0, preserveRY=False):
		if preserveRY:
			return ASM.__movNumToRegister(n1, regx, nSpace)
		return ASM.__setToRegs(n1, n2, regx, regy, nSpace)
