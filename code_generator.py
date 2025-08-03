class CodeGenerator:
  def __init__(self, tokens):
      self.tokens = tokens

  def gerar_codigo(self):
      expressao = ''.join(token.lexema for token in self.tokens)
      try:
          resultado = eval(expressao)
          return resultado
      except Exception as e:
          raise RuntimeError(f"Erro na execução: {e}")