# plot.R
library('ggplot2')

# Pegar argumentos da linha de comando
args <- commandArgs(trailingOnly = TRUE)

# Primeiro argumento: nome do PDF
pdf_file <- args[1]

# Último argumento: arquivo de dados
data_file <- args[length(args)]

# Ler os dados
data <- read.table(data_file, header = TRUE)

# Abrir PDF (gera o arquivo)
pdf(file = pdf_file, width = 8, height = 6)

# Criar o gráfico
ggplot(data, aes(x = Sample, y = Time, colour = Method)) +
  geom_line() +
  theme_minimal()

# Fechar PDF
dev.off()  # salva e fecha o PDF

