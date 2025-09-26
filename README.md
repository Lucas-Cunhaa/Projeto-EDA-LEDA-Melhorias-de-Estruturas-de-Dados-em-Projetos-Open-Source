# Projeto-EDA-LEDA-Melhorias-de-Estruturas-de-Dados-em-Projetos-Open-Source
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

