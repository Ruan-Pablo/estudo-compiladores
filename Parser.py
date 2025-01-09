
from Grammar import Grammar
from Error import Error

# * Representa um controlador de arvore de sintaxe abstrata.
# * Contém um node que aceita visita e um erro de sintaxe, que por padrão é None 

# padrão - singleton: uma classe so produz uma instancia e sempre será a mesma referenciada
#
# Arvore Sintatica Abstrata
class AstInfo:
	singleton = None #declando que é static
	def __init__(self):
		if AstInfo.singleton!=None: 
			raise Exception(f"{Error.singletonMsg(self)}.singletonInstance()'!")
		self.error = None
		self.node = None
		AstInfo.singleton = self
		
# será codificado
class Parser:
	singleton = None
	def __init__(self):
		if Parser.singleton!=None: 
			raise Exception(f"{Error.singletonMsg(self)}.instance()'!")
		
		self.__start([])
		Parser.singleton = self


