class Parser:
  def __init__(self, tokens):
      self.tokens = tokens
      self.pos = 0

  def verificar_sintaxe(self):
      paren_balance = 0
      for token in self.tokens:
          if token.tipo == "PARÊNTESE ABERTO":
              paren_balance += 1
          elif token.tipo == "PARÊNTESE FECHADO":
              paren_balance -= 1
          if paren_balance < 0:
              raise SyntaxError("Parênteses desbalanceados")
      if paren_balance != 0:
          raise SyntaxError("Parênteses desbalanceados")
      # Poderia expandir com uma gramática completa
      return True