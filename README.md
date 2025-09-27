# Projeto de Otimização de Performance - EDA/LEDA - LAB
## 🎯 Propósito do Projeto
Este projeto foi desenvolvido como parte da disciplina de Estrutura de Dados com o objetivo principal de demonstrar e implementar otimizações de algoritmos, reduzindo drasticamente o tempo de execução de operações críticas. Através de otimizações, transformamos algoritmos lentos e ineficientes em soluções rápidas e escaláveis, assim, como na alteração de estrutura de dados, buscando uma implementação mais adequada para o caso de uso.
## 🔍 O Que Foi Otimizado:

#### *Antes: Algoritmos lentos com complexidade O(n) - o tempo de execução crescia linearmente com o tamanho dos dados*
#### *Depois: Algoritmos eficientes com complexidade O(1) - tempo de execução constante, independente do tamanho dos dados*


## 📁 Estrutura das pastas
- **data/**  → contém os arquivos de entrada (ex: `tamanho.txt`)  
- **results/** → armazena os resultados em `.txt` após a execução dos testes  
- **graphs/** → contém os gráficos gerados no R em formato `.pdf`  
- **ufcg_lp2_implementation/** → implementação original (com arrays)  
- **ufcg_lp2_optimized_implementation/** → implementação otimizada (com HashMaps)  

---

## 📌 Fase 1 — Modificações das Estruturas de Dados

### Alterações na classe **Filme** — *Henrique*
  - Substituição do **array** por um **HashMap** para armazenar os locais onde o filme pode ser assistido.  
  - **Chave (String):** nome do local.  
  - **Valor (Integer):** ordem em que o local foi adicionado, de acordo com um contador.  
- Benefícios:
  - Evita duplicatas.
  - Busca otimizada por um local específico (`O(1)` com `containsKey`).
  - Simplicidade na verificação de capacidade e contagem de locais.

#### Principais mudanças:
- **`quantLocais()`**  
  Antes: percorria todo o array (`O(n)`), contando os elementos não nulos.  
  Agora: retorna diretamente o contador (`O(1)`).

- **`indiceLocal()`**  
  Antes: busca linear no array.  
  Agora: consulta direta no HashMap (`O(1)`).

- **`indicePermiteAdicionar()`**  
  Antes: percorria o array em busca da primeira posição vazia no array.  
  Agora: simples comparação entre contador e limite máximo.

- **`removerLocal()` e `adicionarLocalAssistir()`**  
  Antes: buscas preliminares no array.  
  Agora: remoção e inserção diretas no HashMap.

- **`getLocalAssistir()`**  
  Antes: retornava posições nulas.  
  Agora: retorna apenas os valores válidos via `keySet()`.

➡️ Todas as operações críticas passaram de **`O(n)` para `O(1)`**.

---

### Alterações na classe **FilmNow** — *Caio e Letícia*
- Substituição de dois **arrays** por **HashMaps**:
  - Um armazena todos os filmes do sistema.
  - Outro armazena os filmes da “hotlist” (favoritos).
- **Chave (String):** nome do filme (identificador único).  
- **Valor (Filme):** Filme armazenado.
#### Observação: 
- Para fins de otimização foi necessário modificar a assinatura de alguns métodos, substituindo a posição pelo nome do filme como parâmetro.

#### Benefícios:
- **`existeFilme(String nome)`**  
  Antes: busca linear (`O(n)`).  
  Agora: busca constante (`O(1)`) via `containsKey()`.

- Impacto positivo em todos os métodos dependentes que precisavam checar se o filme existia antes de realizar alguma ação:
  - `getFilme(String nome)`
  - `detalharFilme(String nome)`
  - `cadastraFilme(String nome, int ano, String local)`
  - `adicionarHot(String nome)`
  - `removerHot(String nome)`
  - `removerHot(FilmeOtimizado filmeRemover)`
  - `removerFilme(String nome)`

➡️ Assim como em **Filme**, todas as operações críticas passaram de **`O(n)` para `O(1)`**.

---


## 📌 Fase 2 — Experimentação (Testes de Desempenho)

Autores: *João e Lucas*  

Para validar as melhorias, realizamos testes práticos:

1. Foi criado um arquivo `tamanhos.txt` contendo valores de 1000 até 500.000 (em intervalos de 1000).  
2. Para cada valor:
   - Foi criada uma instância de **FilmNow** com esse tamanho.
   - Foram executados os métodos `cadastraFilme` e `adicionarHot` nas versões **antes** e **depois** da otimização.
3. Cada cenário foi repetido **~100.000 vezes** para garantir confiabilidade dos tempos médios, considerando efeitos como **garbage collector** e **sobrecarga inicial da JVM**.
4. Os resultados foram registradis em arquivos `.txt` no diretório `data`:
   - `Method` → Nome do método testado  
   - `Time` → Tempo de execução  
   - `Sample` → Tamanho da entrada  

### 📊 Análise dos resultados
- Utilizou-se **R + ggplot2** para gerar gráficos comparativos armazenados em `graphs/`.  
- Resultados confirmaram a análise teórica:
  - **Arrays:** desempenho linear (`O(n)`).  
  - **HashMaps:** desempenho constante (`O(1)`).  

---

## ✅ Conclusão
- As modificações confirmaram ganhos expressivos de desempenho.  
- Todas as operações críticas migraram de **tempo linear (`O(n)`)** para **tempo constante (`O(1)`)**.  
- A otimização se mostrou especialmente vantajosa em cenários de **grande volume de dados**, sem comprometer a **funcionalidade original** nem a **interface pública** das classes.

---



## 🧪 COMO RODAR O TESTE DE EXECUÇÃO

### Compilação e Execução via Terminal:

```bash
# Navegue até a pasta do projeto
cd LAB-3-LP2

# Comando para compilar o projeto
javac .\ufcg_lp2_implementation\src\MainDefault.java

# Comando para executar o programa principal, inserindo dados e escrevendo o processamento no arquivo .txt 
data/tamanho.txt < java ufcg_lp2_implementation\src\MainDefault  > results/cadastra_filmes_default.txt

````

## 📊 COMO GERAR OS GRÁFICOS COM R

### Pré-requisitos:
```bash
- Instale **R**
- Instalar o pacote **ggplot2**
comando apra isntalar o ggplot2: install.packages("ggplot2")
````

#### Executar o script em R

Os gráficos são gerados a partir dos resultados salvos em `results/`.  
Para rodar o script `plot.R`, use o seguinte comando:

```bash
R < plot.R --vanilla ../../results/cadastra_filmes.txt
````

## 👥 Equipe
- **Henrique** - Classe *Filme*
- **Caio & Letícia** - Classe *FilmNow*
- **João & Lucas** - Testes de Experimentação

---

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

---

# Projeto 3 - Python-Open-Source-Algorithms (João Ventura Crispim Neto)
## Apriori Algorithm 
[TheAlgoritms/Python/machine_learning/apriori_algorithm.py](https://github.com/TheAlgorithms/Python/blob/master/machine_learning/apriori_algorithm.py)

Este projeto tem como objetivo otimizar a implementação do **Apriori Algorithm** presente no repositório [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python). O algoritmo é uma técnica clássica de mineração de regras de associação, amplamente utilizada em análise de mercado (*market basket analysis*), cujo propósito é identificar padrões de coocorrência de itens em transações, como por exemplo:

> “Clientes que compram A e B também tendem a comprar C”.

---

## 📌 Deficiência da Implementação Padrão

Na versão original, a função **`prune`** apresentava forte ineficiência devido ao uso recorrente das operações:

* `in` em listas → O(n)
* `count` em listas → O(n)

Essas operações eram executadas repetidamente para cada item de cada candidato, resultando em uma complexidade:

```
O(m · k₂ · n · k₁)
```

O que torna a execução inviável em cenários com grandes volumes de dados.

---

## 🔑 Significado das Variáveis

* **n** → número de elementos no *itemset*.
* **k₁** → tamanho médio das sublistas dentro do *itemset*.
* **m** → número de candidatos gerados pelo algoritmo.
* **k₂** → tamanho médio das sublistas dentro de cada candidato.

---

## 🚀 Solução Proposta

A otimização consistiu em **pré-processar o itemset** utilizando a estrutura `Counter`, com **tuplas como chaves** (estruturas imutáveis em Python).

* Verificação de presença → O(1) amortizado
* Contagem de elementos → O(1) amortizado

### Complexidade Final

* Construção do `Counter`: `O(n · k₁)`
* Processamento dos candidatos: `O(m · k₂²)`
* Uso de memória auxiliar: `O(n · k₁)`

➡️ **Complexidade total:**

```
O(n · k₁ + m · k₂²)
```

---

## 🧪 Como Rodar os Casos de Teste e Gerar os Gráficos

1. Na raiz da pasta **/Python-Open-Source-Algorithms**, execute o script:

   ```bash
   python main.py
   ```

   * O script gera automaticamente casos de teste médios e piores casos.
   * O uso de **Threads** permite executar as funções em paralelo, acelerando a coleta dos resultados.
   * Os resultados são salvos em arquivos `.txt` na pasta **/results**.

2. Para gerar os gráficos de análise, vá até a pasta **/scripts** que está na raiz do repositório e rode o comando:

   ```bash
   - Instale **R**
   - Instalar o pacote **ggplot2**
   - comando apra isntalar o ggplot2: install.packages("ggplot2")
   ```

   ```bash
   R < plot.R --vanilla ../Python-Open-Source-Algorithms/results/pruneOptimized_pior_caso_prune_pior_caso_algoritm_results.txt
   ````

   Issso gerara os gráficos na própria pasta **/scripts** em .pdf.
---

## ✅ Conclusão

Os testes empíricos comprovaram **ganhos expressivos de desempenho**.

* A versão otimizada reduziu significativamente o impacto do crescimento do *itemset*, tornando o algoritmo mais escalável.
* Embora tenha introduzido o uso de memória auxiliar e um termo quadrático em `k₂`, o trade-off foi vantajoso, já que o custo original dependia fortemente de `n · k₁`.

Portanto, a otimização proposta é eficaz e torna o *Apriori Algorithm* mais eficiente e preparado para lidar com grandes volumes de dados.

# Caio - Jogo Android de Xadrez
## Descrição do projeto
Este projeto faz parte da disciplina de Estruturas de Dados, onde cada integrante selecionou um projeto open source com o objetivo principal de demonstrar e implementar otimizações de algoritmos.
Minha contribuição focou no projeto Android Chess (https://github.com/jcarolus/android-chess), um jogo de xadrez para Android, buscando otimizar a forma como os movimentos do jogador eram armazenados e exibidos. Onde inclusive, tive meu PR aceito.

## Alterações realizadas
Originalmente, o projeto armazenava os movimentos do jogo em uma ArrayList<HashMap<String, String>> que é exibida em um menu usando SimpleAdapter. Você pode checar em: (android-chess-versao-inicial/app/src/main/java/jwtc/android/chess/play/PGNDialog.java).
Posso citar que, conforme uma partida de xadrez possui diversas variações, alguns jogos podem se tornar extensos o suficiente para fazer com que essa estrutura se torne ineficiente e com alto custo de memória. Daí nasce a necessidade de altera-la.

De começo, como dito anteriormente, identifiquei essa estrutura como um possível ponto a se melhorar, mas pela falta de experiência com desenvolvimento de jogos em Android, não sabia que Maps eram as únicas estruturas aceitas pelo SimpleAdapter nativo. Dessa forma, com uma pesquisa para me aprofundar no assunto, consegui contornar esse problema implementando: 
### 1°: Uma nova estrutura de dados
Criei a classe movimento, que representa cada movimento realizado na partida, mantendo todos os atributos que eram antes adicionados no HashMap.
### 2°: Adapter personalizado
Essa foi a parte que mais tive trabalho. Como forma de contornar o problema citado anteriormente, precisei implementar um adapter próprio para exibir a lista de movimentos.
Com algumas pesquisas e estudos, consegui construir o MovimentoAdapter que possibilitou essa modificação.
### 3°: Substituição da estrutura de dados
Com a finalização dos passos anteriores, pude substituir a estrutura ArrayList<HashMap<String, String>> por ArrayList<MoveItem>. Além disso, também troquei a instância de SimpleAdapter por MoveItemAdapter.

Você pode encontrar essas alterações acessando o folder: android-chess-otimizado/app/src/main/java/jwtc/android/chess/play/. Lá criei a classe MoveItem.java e o adapter MoveItemAdapter.java. Também alterei a estrutura em si no PGNDialog.java.

## Melhorias no programa
Além de ter tido meu PR aceito pelo autor do programa, gerei alguns gráficos apartir de um benchmark que construi para comprovar a melhoria no uso de memória e no tempo de execução do programa. Você pode verifica-los no arquivo Rplots.pdf, bem como, gerar novamente usando o benchmark e o script em R (plot_benchmark.R) que criei. 
---
