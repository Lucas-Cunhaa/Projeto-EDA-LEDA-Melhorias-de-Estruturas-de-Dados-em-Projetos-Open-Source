# Projeto-EDA-LEDA-Melhorias-de-Estruturas-de-Dados-em-Projetos-Open-Source
## Descrição do projeto
Este projeto faz parte da disciplina de Estruturas de Dados, onde cada integrante selecionou um projeto open source com o objetivo principal de demonstrar e implementar otimizações de algoritmos.
Minha contribuição focou no projeto Android Chess, um jogo de xadrez para Android, buscando otimizar a forma como os movimentos do jogador eram armazenados e exibidos. Onde inclusive, tive meu PR aceito.

## Alterações realizadas
Originalmente, o projeto armazenava os movimentos do jogo em uma ArrayList<HashMap<String, String>> que é exibida em um menu usando SimpleAdapter. 
Observação: de começo, identifiquei essa estrutura como um possível ponto a se melhorar, mas pela falta de experiência com desenvolvimento de jogos em Android, não sabia que Maps eram as únicas estruturas aceitas pelo SimpleAdapter que vem por padrão. Dessa forma, com uma pesquisa básica, consegui implementar um adapter próprio para o programa o que possibilitou a substituição dessa estrutura 
