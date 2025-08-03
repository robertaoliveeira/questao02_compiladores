# Questão 02
 
Equipe 3
Délis Albuquerque
Everton de Almeida
Gabriel Gomes
João Leonardo
Raul Santos
Roberta Oliveira

# Descrição da Linguagem e do Compilador
Este projeto é um mini-compilador de expressões aritméticas, escrito em Python, que simula um pipeline de compilação real, dividido em:

Componentes do Compilador:
Lexer (Analisador Léxico)
Lê o código-fonte (expressão aritmética) e o divide em tokens, como números, operadores e parênteses.

Parser (Analisador Sintático)
Valida a estrutura da expressão, garantindo que os parênteses estejam bem formados. Pode ser estendido para validar gramáticas mais complexas.

Code Generator (Gerador de Código)
Interpreta os tokens e avalia a expressão, retornando seu resultado final. Pode futuramente ser substituído por uma geração real de código intermediário (IR) ou assembly fictício.

Classe Main
Coordena o processo: lê a expressão, executa os componentes e imprime a tabela de tokens e o resultado.

# Descrição da Linguagem Suportada
A linguagem aceita expressões aritméticas simples, compostas por:

Números inteiros (ex: 1, 25, 100)

Operadores aritméticos:
+ (adição), - (subtração), * (multiplicação), / (divisão)

Parênteses para agrupar subexpressões

Exemplos válidos:
txt
Copiar
Editar
5 * (2 + 10)
10 + 3 * 2
(1 + 2) * (3 + 4)
100 / (25 - 5)

Exemplos inválidos (detectados pelo parser):
txt
Copiar
Editar
(5 + 3    # parêntese não fechado
5 + ) 4   # parêntese fechado sem abrir

# Como Usar o Compilador
1. Pré-requisitos
Python 3.x instalado

2. Coloque os seguintes arquivos no mesmo diretório:

expressao.txt           
lexer.py               
parser.py              
code_generator.py       
main.py    

3. Escreva a expressão no arquivo expressao.txt
Exemplo:

5 * (2 + 10)
4. Execute o compilador
No terminal, no mesmo diretório dos arquivos:
python main.py

# Saída Esperada

TOKEN      TIPO                 VALOR          
---------------------------------------------
5          NÚMERO              5              
*          OPERADOR            MULTIPLICAÇÃO  
(          PARÊNTESE ABERTO    (              
2          NÚMERO              2              
+          OPERADOR            SOMA           
10         NÚMERO              10             
)          PARÊNTESE FECHADO   )              

Resultado da expressão: 60
