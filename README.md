# Mini Compilador de Expressões Aritméticas

## Equipe 03

- **Délis Albuquerque**;
- **Everton de Almeida**;
- **Gabriel Gomes**;
- **João Leonardo**;
- **Raul Santos**;
- **Roberta OLiveira**.

Este projeto é um compilador simples em Python que realiza a **análise léxica**, **análise sintática** e **avaliação** de expressões aritméticas. Ele simula um pipeline de compilação dividido em quatro etapas:

- **Lexer** – Tokeniza a expressão.
- **Parser** – Verifica a estrutura sintática (parênteses e ordem).
- **Code Generator** – Avalia a expressão e retorna o resultado.
- **Main** – Integra todos os componentes.

---

## Linguagem Suportada

A linguagem é composta por expressões aritméticas simples com:

- **Números inteiros**: `1`, `42`, `1000`
- **Operadores**: `+`, `-`, `*`, `/`
- **Parênteses**: para agrupar subexpressões

### Exemplos válidos:

5 * (2 + 10)
(1 + 2) * (3 - 1)
10 + 3 * 2
100 / (25 - 5)


### Exemplos inválidos:

(5 + 3 # Parêntese não fechado
5 + ) 4 # Parêntese fechado sem abrir

---

## Estrutura do Projeto

expressao.txt # Expressão de entrada
lexer.py # Analisador léxico
parser.py # Analisador sintático
code_generator.py # Gerador de código
main.py # Arquivo principal que executa tudo

---

## Como Executar

### 1. Clone este repositório

git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

2. Escreva a expressão no arquivo expressao.txt

5 * (2 + 10)
3. Execute o programa principal

python main.py

Exemplo de Saída

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



