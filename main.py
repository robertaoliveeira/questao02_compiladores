from lexer import Lexer
from parser import Parser
from code_generator import CodeGenerator

def main():
    # Ler o arquivo txt
    with open("expressao.txt", "r") as arq:
        codigo = arq.read().strip()

    # Lexer
    lexer = Lexer(codigo)
    tokens = lexer.analisar()

    # Exibir tabela de tokens
    print("{:<10} {:<20} {:<15}".format("TOKEN", "TIPO", "VALOR"))
    print("-" * 45)
    for token in tokens:
        print(token)

    # Parser (verificação sintática)
    parser = Parser(tokens)
    try:
        parser.verificar_sintaxe()
    except SyntaxError as e:
        print("\nErro de sintaxe:", e)
        return

    # Execução
    gerador = CodeGenerator(tokens)
    try:
        resultado = gerador.gerar_codigo()
        print("\nResultado da expressão:", resultado)
    except RuntimeError as e:
        print("\nErro no código:", e)

if __name__ == "__main__":
    main()
