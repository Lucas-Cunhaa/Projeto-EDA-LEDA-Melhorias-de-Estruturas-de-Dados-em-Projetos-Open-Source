
library(ggplot2)

df <- read.csv("benchmarkresults.csv")

# --- Gráfico de Tempo de Execução ---
ggplot(df, aes(x=Run, y=TimeMS, color=Structure, group=Structure)) +
  geom_line() +
  geom_point() +
  labs(title="Tempo de Execução - HashMap vs Classe",
       x="Execução",
       y="Tempo (ms)") +
  theme_minimal()

# --- Gráfico de Uso de Memória ---
df_mem <- subset(df, Run == 0)  # memória só medida uma vez
ggplot(df_mem, aes(x=Structure, y=MemoryMB, fill=Structure)) +
  geom_bar(stat="identity", position="dodge") +
  labs(title="Uso de Memória - HashMap vs Classe",
       x="Estrutura",
       y="Memória (MB)") +
  theme_minimal()