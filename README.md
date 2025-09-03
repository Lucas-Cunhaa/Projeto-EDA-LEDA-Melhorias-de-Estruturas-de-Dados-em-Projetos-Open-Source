# Projeto-EDA-LEDA-Melhorias-de-Estruturas-de-Dados-em-Projetos-Open-Source
## 🎯 Propósito do Projeto
Este projeto foi desenvolvido como parte da disciplina de Estrutura de Dados com o objetivo principal de demonstrar e implementar otimizações de algoritmos em projetos Open Source. O projeto escolhido dessa vez é o SudokuGUI-Solver - https://github.com/techwithtim/Sudoku-GUI-Solver - que consiste em um resolvedor de Sudoku, implementando o algoritmo de backtracking, com interface gráfica desenvolvido em Python, utilizando a biblioteca Pygame.

## 🔍 O Algoritmo de Backtracking no Sudoku

### Fundamentos do Backtracking
O backtracking é uma técnica de busca sistemática que testa possibilidades recursivamente, retrocedendo assim que detecta que uma solução parcial não pode ser completada. No Sudoku, isso significa:

- **Preenchimento progressivo**: Testar números de 1 a 9 em células vazias
- **Verificação de constraints**: Validar se o número respeita as regras do jogo
- **Retrocesso inteligente**: Voltar ao passo anterior quando nenhum número for válido

### A Importância da Eficiência na Validação
Cada etapa de validação é executada **milhares de vezes** durante o backtracking. Uma operação O(n) de validação, quando multiplicada pela natureza exponencial do algoritmo, cria um gargalo computacional crítico.

## ⚡ Problema Identificado na Implementação Original

### O Gargalo das Validações Lineares
A implementação original utilizava abordagens de validação com complexidade O(n) para verificar a viabilidade de cada movimento. O método `valid()` realizava:

- **Verificação linear em linhas**: 9 operações por validação
- **Verificação linear em colunas**: 9 operações por validação  
- **Verificação linear em regiões 3x3**: 9 operações por validação
- **Total: 27 operações O(n) por validação individual**

### Consequência do Problema
Esta abordagem tornava-se criticamente ineficiente durante o processo de backtracking, onde cada validação era executada múltiplas vezes para cada célula vazia, resultando em:
- Tempo de resolução excessivamente longo
- Interface gráfica com resposta lenta
- Experiência do usuário comprometida

## 🚀 Solução Implementada
### Estruturas de Dados Otimizadas
Implementei um sistema baseado em **conjuntos (sets)** para rastreamento eficiente do estado do tabuleiro:

- **`row_sets`**: Array de sets para controlar números presentes em cada linha
- **`col_sets`**: Array de sets para controlar números presentes em cada coluna
- **`box_sets`**: Array de sets para controlar números presentes em cada região 3x3


### Métodos Otimizados
- **`valid()`**: Reduzido de O(n) para O(1) usando operações de set
- **`place()`**: Inserção com validação O(1) e atualização de estados
- **`remove_number()`**: Nova função para remoção eficiente com O(1)
-- **`solve()`**: Algoritmo adaptado para gerenciar estados durante backtracking com operações O(1)
- **`solve_gui()`**: Versão visual com atualização eficiente de conjuntos durante animação
