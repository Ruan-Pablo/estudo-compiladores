from Consts import Consts
from Error import Error

""" i é int
 E-> iK
 K -> +iK
 K -> 
"""
class RecDescendente:
    def __init__(self, toks):
        self.tokens = toks
        self.id = -1
        self.current = None
        self.txt = ''
    def nextToken(self):
        self.id +=1
        if self.id<len(self.tokens):
            self.current = self.tokens[self.id]
        return self.current    
    def CurrentTok(self): return self.current
    def start(self):
        self.nextToken()
        a, e = self.E()
        if self.CurrentTok().type != Consts.EOF: 
            return None, (e+":Erro nao $ no final")
        return a, e
    def E(self):
        if self.CurrentTok().type == Consts.INT:
            self.txt +="i"
            self.nextToken()
            a, e = self.K()
            return a, e
        return None, "Falha E(), precisa iniciar com inteiro"
    
    def K(self):
        if self.CurrentTok().type == Consts.PLUS:
            self.nextToken()
            if self.CurrentTok().type == Consts.INT:
                self.nextToken()
                self.txt +="+i"
                a, e = self.K()
                return self.txt, e
            else: 
                return self.txt, "erro + no final"
        self.txt +="e"
        return self.txt, None

