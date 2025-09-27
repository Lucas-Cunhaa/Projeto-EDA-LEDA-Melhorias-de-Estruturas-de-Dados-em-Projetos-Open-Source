# Análise de Desempenho do Algoritmo de Sudoku

## 1. O Desafio: Antes e Depois
São dois códigos para resolver Sudoku: uma versão original e uma versão otimizada. O objetivo era provar que a otimização realmente funcionou e mostrar a diferença de performance.

## 2. A Otimização por Trás dos Bastidores
A principal diferença entre os dois códigos está em como eles **validam** um número.

* **Versão Original (`GUI.py`):** Para saber se um número pode ser colocado em uma célula, o código percorre a linha, a coluna e a "caixa" do tabuleiro. Essa busca é uma operação lenta, especialmente porque o algoritmo de resolução (chamado de "backtracking") faz essa checagem milhares de vezes.

* **Versão Otimizada (`GUI_otimizado.py`):** A versão otimizada usa uma técnica inteligente: em vez de buscar, ela cria três conjuntos (ou "sets") para cada linha, coluna e caixa. A cada número adicionado, o código simplesmente o insere no conjunto correspondente. Para validar, ele apenas checa se o número já existe no conjunto, o que é quase instantâneo.

## 3. O Teste de Campo: Como Provamos a Mudança
Para provar a melhoria, existe um script que faz o seguinte:
* Gera vários tabuleiros de Sudoku com diferentes níveis de dificuldade (ou seja, com um número crescente de células vazias).
* Para cada tabuleiro, ele mede o tempo de execução para resolver com o código original e com o código otimizado.
* Ele mede o tempo total e também o tempo que cada função gasta, como `solve`, `valid` e `place`.

## 4. O Resultado nos Gráficos: Entendendo os Dados

### Gráfico Geral e da Função `solve()`

Você notou que, no gráfico que compara o tempo total de execução (`solve`), a versão original teve um pico gigante e depois voltou a cair. Isso pode parecer estranho, mas é a prova mais importante da melhoria.

* **O Pico:** O algoritmo de resolução, chamado **backtracking**, é como tentar sair de um labirinto. Às vezes, você faz uma escolha errada e precisa voltar (backtrack) muitas vezes até encontrar a saída. O pico de tempo da versão original significa que o tabuleiro gerado para aquele teste específico era um "labirinto" muito difícil, que fez o algoritmo se perder e precisar de muitos retrocessos. A lentidão da função `valid()` original fez com que cada retrocesso custasse muito tempo.
* **A Queda:** A performance do backtracking não é linear! Um tabuleiro com 40 células vazias pode, por pura sorte, ter uma estrutura que permite ao algoritmo encontrar a solução mais rápido, com menos "erros" no caminho. O pico prova que o código original não é resiliente a essas dificuldades.
* **A Linha Otimizada:** A linha da versão otimizada é muito mais plana. Isso mostra que, mesmo em tabuleiros difíceis, a checagem rápida de validade evita que o algoritmo perca tempo em becos sem saída, tornando-o consistentemente mais rápido.

### Gráficos de `valid()` e `place()`

Esses gráficos mostram o impacto direto da otimização:
* A função `valid()` (checar se um número é válido) na versão otimizada é **muitas vezes mais rápida** que a original.
* A função `place()` (colocar um número) na versão otimizada também é mais rápida, já que ela também se beneficia da validação instantânea.

## 5. Conclusão Final

A otimização no código não é apenas uma pequena melhora; é uma mudança fundamental na forma como a validade é checada. Isso torna o algoritmo de resolução **muito mais robusto e eficiente**, especialmente em cenários mais desafiadores. O trabalho realmente valeu a pena!
