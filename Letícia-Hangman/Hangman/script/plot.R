# Se o pacote não tiver instalado na máquina.
#install.packages('ggplot2', repos = "http://cran.us.r-project.org")

library('ggplot2')

args <- commandArgs()

data = read.table(args[length(args)], header = T)
ggplot(data, aes(x = Sample, y = Time, colour = Method)) + geom_line()




# library('ggplot2') 

# # Ler arquivo
# data <- read.table("C:/Users/letic/Hangman/results/benchmark3.txt", header = TRUE)

# # Renomear colunas para facilitar o ggplot
# colnames(data) <- c("Method", "Time", "Sample")

# # Criar PDF
# pdf("../results/benchmark3_plot.pdf", width = 8, height = 6)

# # Gerar gráfico
# ggplot(data, aes(x = Sample , y = Time, colour = Method, group = Method)) +
#   geom_line() +
#   geom_point() +
#   labs(
#     title = "Comparação SpacedOut List vs Set",
#     x = "Sample",
#     y = "Tempo por execução (s)"
#   ) +
#   theme_minimal()

# # Fechar PDF
# dev.off()
