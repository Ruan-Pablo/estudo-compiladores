
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
	
	def success(self, node):
		self.node = node
		return self

	def fail(self, errorMsg):
		if not self.error:
			self.error = Error(errorMsg)
		return self

	def registry(self, ast_info):
		if ast_info.error: self.error = ast_info.error
		return ast_info.node

	@staticmethod
	def resetSingletonErrorForNewParsing():
		AstInfo.singleton.error = None
		
	@staticmethod
	def singletonInstance():
		if AstInfo.singleton == None:
			AstInfo.singleton = AstInfo()
		return AstInfo.singleton


# será codificado
class Parser:
	singleton = None
	def __init__(self):
		if Parser.singleton!=None: 
			raise Exception(f"{Error.singletonMsg(self)}.instance()'!")
		
		self.__start([])
		Parser.singleton = self

	def nextTok(self):
		self.tokIdx += 1
		if self.tokIdx < len(self.tokens): # so avança se nn passar do tamanho
			self.currentToken = self.tokens[self.tokIdx]
		return self.currentToken
	
	def __start(self, _tokens):
		self.tokens = _tokens
		self.tokIdx = -1
		self.currentToken = None
		self.manager = AstInfo.singletonInstance()
		self.manager.resetSingletonErrorForNewParsing()

	def manager(self):
		return self.manager
	def currentTok(self):
		return self.currentToken
	def __reset(self, _tokens):
		self.start(_tokens)
		self.nextTok()
	
	@staticmethod
	def instance():
		if Parser.singleton==None:
			Parser.singleton = Parser()
		return Parser.singleton

	def parsing(self, _tokens):
		self.__reset(_tokens)
		return Grammar.StartSymbol(self)