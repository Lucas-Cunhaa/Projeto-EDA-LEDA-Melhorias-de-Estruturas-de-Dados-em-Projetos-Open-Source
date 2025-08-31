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
````

#### Executar o script em R

Os gráficos são gerados a partir dos resultados salvos em `results/`.  
Para rodar o script `plot.R`, use o seguinte comando:

```bash
R < plot.R --vanilla ../../results/cadastra_filmes.txt

````bash
# Exemplo de opções:

(1) results/cadastra_filmes.txt -> teste do método Cadastra Filme antes da otimização {O(n)}
(2) results/cadastra_filmes_otimizado.txt -> teste do método Cadastra Filme depois da otimização {O(1)}
.
.
.
# basta escolher uma opção e ele gerará gráficos do número de caso de entrada de dados e seus tempos de execução
````




## BÔNUS: 📊 COMO GERAR OS GRÁFICOS COM PYTHON

### Pré-requisitos:
```
# Instale as dependências Python necessárias
pip install matplotlib
pip install chardet

# rode o main.py que esta na raiz do reposítorio
python main.py

```
### Entendendo como gerar o gráfico dos dados nos arquivos .txt:

```
# Exemplo de opções:

(1) resultCadastraFilmesBeforeOptimization.txt -> teste do méthodo Cadastra Filme antes da otimização {O(n)}
(2) resultCadastraFilmesAfterOptimization.txt -> teste do méthodo Cadastra Filme depois da otimização {O(1)}
.
.
.
# basta escolher uma opção e ele gerará gráficos do número de caso de entrada de dados e seus tempos de execução
```

```
## 👥 Equipe
- **Henrique** - Classe *Filme*
- **Caio & Letícia** - Classe *FilmNow*
- **João & Lucas** - Testes de Experimentação
```



