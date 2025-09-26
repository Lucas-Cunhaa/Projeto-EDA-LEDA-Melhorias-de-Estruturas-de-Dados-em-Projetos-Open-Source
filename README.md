# Projeto de Otimização de Performance - EDA/LEDA
## 🎯 Propósito do Projeto
Este projeto foi desenvolvido como parte da disciplina de Estrutura de Dados com o objetivo principal de demonstrar e implementar otimizações de algoritmos, reduzindo drasticamente o tempo de execução de operações críticas. Através de otimizações, transformamos algoritmos lentos e ineficientes em soluções rápidas e escaláveis, assim, como na alteração de estrutura de dados, buscando uma implementação mais adequada para o caso de uso.
## 🔍 O Que Foi Otimizado:

#### *Antes: Algoritmos lentos com complexidade O(n) - o tempo de execução crescia linearmente com o tamanho dos dados*
#### *Depois: Algoritmos eficientes com complexidade O(1) - tempo de execução constante, independente do tamanho dos dados*

## 🧪 COMO RODAR O TESTE DE EXECUÇÃO

### Compilação e Execução via Terminal:

```bash
# Navegue até a pasta do projeto
cd LAB-3-LP2

# Comando para compilar o projeto
javac -d bin .\ufcg.lp2.default.implementation\src\*.java

# Comando para executar o programa principal
java -cp bin ufcg.lp2.default.implementation.src.MainDefault
````

## 📊 COMO GERAR OS GRÁFICOS

### Pré-requisitos:
```bash
# Instale as dependências Python necessárias
pip install matplotlib

# rode o main.py que esta na raiz do reposítorio
python main.py
````

### Entendendo como gerar o gráfico dos dados no arquivos .txt:

````bash
# Exemplo de opções:

(1) resultCadastraFilmesBeforeOptimization.txt -> teste do méthodo Cadastra Filme antes da otimização {O(n)}
(2) resultCadastraFilmesAfterOptimization.txt -> teste do méthodo Cadastra Filme depois da otimização {O(1)}
.
.
.
# basta escolher uma opção e ele gerará o gráfico do número de caso de entrada de dados e seus tempos de execução
````
## Conclusão
As modificações realizadas comprovaram a eficácia da substituição de arrays por HashMaps no projeto analisado. Tanto a análise assintótica quanto os testes práticos comprovaram ganhos significativos de desempenho nas operações anteriormente de complexidade O(n) em operações de tempo constante O(1), sem comprometer a funcionalidade original do sistema.
	Esses resultados destacam a importância da escolha adequada de estruturas de dados em projetos de software, evidenciando que decisões arquiteturais bem fundamentadas podem impactar diretamente a eficiência e a escalabilidade de sistemas computacionais.
	A partir de agora, cada integrante vai escolher o seu próprio projeto open source e realizar as mudanças necessárias.
  
# Projeto 1 - Henrique Sudoku (Henrique de Freitas e Sousa)
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
- **`solve()`**: Algoritmo adaptado para gerenciar estados durante backtracking com operações O(1)
- **`solve_gui()`**: Versão visual com atualização eficiente de conjuntos durante animação

## 📊 Inicializando o ambiente para os testes

### Arquivos do projeto
Certifique-se que os três arquivos a seguir estão na mesma pasta (/Henrique Sudoku/Sudoku-GUI-otimizado)
- **`GUI.py`**: O código-fonte da versão original do solucionador de Sudoku.
- **`GUI_otimizado.py`**: O código-fonte da versão otimizada do solucionador.
- **`benchmark.py`**: O script que executa os testes de benchmark, compara o tempo de ambas as versões e gera os gráficos.

### Bibliotecas Python
Você precisará de duas bibliotecas instaladas em seu ambiente Python. Use o gerenciador de pacotes pip para instalá-las:
```bash
# matplotlib: Utilizada para gerar os gráficos de performance.
# pygame: Necessária para as classes e funções das interfaces gráficas (GUI.py e GUI_otimizado.py), que são usadas como base para o script de benchmark.
pip install matplotlib pygame
````
## 🧪 Como gerar os gráficos de Desempenho
Com os arquivos no lugar e as bibliotecas instaladas, o processo é direto e simples.

1. **Abra o Terminal ou Prompt de Comando**  
   Navegue até a pasta onde você salvou os arquivos.

   ```bash
   cd [caminho_da_sua_pasta]
   ````
   
2. **Execute o Script de Comparação**
   Execute o script benchmark.py com o seguinte comando:
   ```bash
   # O script começará a rodar os testes. Você verá mensagens de progresso no terminal, como "Testando com X células vazias...". O processo pode levar alguns minutos, dependendo da sua máquina.
   python benchmark.py
   ````
3. **Visualize os resultados**
  Após a conclusão dos testes, uma nova pasta chamada resultados será criada na mesma pasta que os arquivos. Dentro dela, você encontrará:
  - Quatro gráficos em formato PNG **`.png`**, que visualizam a performance de ambas as versões.
  - Um arquivo de texto **`.txt`** com um relatório detalhado das métricas de tempo.

## Conclusão 
A otimização com sets demonstrou ser decisiva para o desempenho do algoritmo de Sudoku. A mudança de validações O(n) para O(1) transformou operações críticas, resultando em ganhos de performance que se multiplicam exponencialmente durante o backtracking.
