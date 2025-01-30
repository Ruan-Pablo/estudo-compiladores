from Error import Error
import abc
from TValue import *
from Consts import Consts
"""

# * Aqui são incluídos os NO's da AST (Abstract Syntax Tree).
# * Eles aceitam visitas de operadores de memoria, visando semantica e controle de tipos (para execucao ou compilacao).
# * Tipos: - criamos a classe TValue especializada em tratar tipos e valores.
#         - Partimos da ideia de que todo dado possui um tipo e valor.

"""
class Visitor(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def visit(self, operator): operator.fail(Error(f"{Error.runTimeError}: Nenhum metodo visit para a classe '{Error.classNameOf(self)}' foi definido!"))

	def __repr__(self): (f"TODO: implements __repr__ of '{Error.classNameOf(self)}' class")
	
class NoNumber(Visitor):
	def __init__(self, tok):
		self.tok = tok

	def visit(self, operator):
		return operator.success(TNumber(self.tok.value).setMemory(operator))

	def __repr__(self):
		return f'{self.tok}'
	
class NoOpUnaria(Visitor):
	def __init__(self, opTok, node):
		self.opTok = opTok
		self.node = node

	def visit(self, ast):
		num = ast.registry(self.node.visit(ast))
		if ast.error: return ast
		error = None
		if self.opTok.type == Consts.MINUS:
			num, error = num.mult(TNumber(-1))
		if error:
			return ast.fail(error)
		else:
			return ast.success(num)

	def __repr__(self):
		return f'({self.opTok}, {self.node})'
