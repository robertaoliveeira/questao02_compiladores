import re

OPERADORES = {
    '+': 'ADIÇÃO',
    '-': 'SUBTRAÇÃO',
    '*': 'MULTIPLICAÇÃO',
    '/': 'DIVISÃO'
}


class Token:

    def __init__(self, lexema, tipo, valor):
        self.lexema = lexema
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"{self.lexema:<10} {self.tipo:<20} {self.valor:<15}"


class Lexer:

    def __init__(self, texto):
        self.texto = texto

    def analisar(self):
        tokens = []
        padrao = re.findall(r'\d+|[+\-*/()]', self.texto)

        for lexema in padrao:
            if lexema.isdigit():
                tokens.append(Token(lexema, "NÚMERO", lexema))
            elif lexema in OPERADORES:
                tokens.append(Token(lexema, "OPERADOR", OPERADORES[lexema]))
            elif lexema == '(':
                tokens.append(Token(lexema, "PARÊNTESE ABERTO", lexema))
            elif lexema == ')':
                tokens.append(Token(lexema, "PARÊNTESE FECHADO", lexema))
            else:
                tokens.append(Token(lexema, "DESCONHECIDO", lexema))
        return tokens
