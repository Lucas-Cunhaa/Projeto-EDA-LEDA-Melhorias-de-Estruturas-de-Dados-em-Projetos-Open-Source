import os
import time
from unittest.mock import patch
from hangman import spacedOut as spacedOut_lista      # versão que usa lista
from hangmanOtimizado import spacedOut as spacedOut_set  # versão que usa set

# cria a pasta results se não existir
os.makedirs("results", exist_ok=True)

# palavras de teste
palavras_teste = [
    "python",
    "ufcg",
    "benchmark",
    "proclameiud",
    "fundeiorspa",
    "juntarexico",
    "campolidrue",
]

# chutes programados por palavra simulando até 6 erros, repetindo letras erradas
chutes_por_palavra = {
    "python":       ["a","a","e","e","i","i","o","p","y","t","h","n"],
    "ufcg":         ["a","a","e","e","i","i","o","u","f","c","g"],
    "benchmark":    ["z","z","x","x","q","q","w","w","e","b","n","c","h"],
    "proclameiud":  ["a","a","o","o","e","e","i","i","u","u","p","r","c","l","m","d"],
    "fundeiorspa":  ["z","z","x","x","y","y","a","f","u","n","d","e"],
    "juntarexico":  ["b","b","c","c","d","d","e","e","f","f","g","g","j","u","n","t"],
    "campolidrue":  ["z","z","x","x","y","y","a","c","m","p","o","l"],
}

REPETICOES = 100000

with patch("pygame.display.set_mode"):
    # abre o arquivo para sobrescrever
    with open("results/benchmark3.txt", "w") as f:
        f.write("Method Time(ms) Sample\n\n")

        # ======= Benchmark usando set =======
        f.write("# Benchmark SpacedOut-Set (erros repetidos)\n")
        for idx, palavra in enumerate(palavras_teste, start=1):
            guessed = set()
            for chute in chutes_por_palavra.get(palavra, []):
                start = time.perf_counter()
                for _ in range(REPETICOES):
                    resultado = spacedOut_set(palavra, guessed)
                fim = time.perf_counter()

                tempo_medio = (fim - start) * 1000 / REPETICOES
                f.write(f"SpacedOut-Set {tempo_medio:.8f} Palavra{idx}\n")
                guessed.add(chute.upper())

        f.write("\n")

        # ======= Benchmark usando lista =======
        f.write("# Benchmark SpacedOut-Lista (erros repetidos)\n")
        for idx, palavra in enumerate(palavras_teste, start=1):
            guessed = []
            for chute in chutes_por_palavra.get(palavra, []):
                start = time.perf_counter()
                for _ in range(REPETICOES):
                    resultado = spacedOut_lista(palavra, guessed)
                fim = time.perf_counter()

                tempo_medio = (fim - start) * 1000 / REPETICOES
                f.write(f"SpacedOut-Lista {tempo_medio:.8f} Palavra{idx}\n")
                guessed.append(chute.upper())

print("✅ Benchmark finalizado! Resultados em results/benchmark3.txt")


# #antes da otimizacao
# import os
# import time
# from unittest.mock import patch
# from hangman import spacedOut

# # cria a pasta results se não existir
# os.makedirs("results", exist_ok=True)

# # palavras de teste e chutes programados
# palavras_teste = ["python", "ufcg", "benchmark"]
# chutes = ["a", "a", "a", "a", "p", "y", "t", "h", "o", "n", "u", "f", "c", "g", "b", "e"]

# # número de repetições para cada execução
# REPETICOES = 100000

# # desativa temporariamente a abertura da janela do pygame
# with patch("pygame.display.set_mode"):
#     with open("results/benchmark2.txt", "w") as f:
#         f.write("Method Time(ms) Sample\n")

#         for idx, palavra in enumerate(palavras_teste, start=1):
#             guessed = []
#             for chute in chutes:
#                 start = time.perf_counter()
#                 for _ in range(REPETICOES):
#                     resultado = spacedOut(palavra, guessed)
#                 fim = time.perf_counter()

#                 # tempo médio em milissegundos
#                 tempo_medio = (fim - start) * 1000 / REPETICOES
#                 f.write(f"SpacedOut {tempo_medio:.8f} Palavra{idx}\n")

#                 guessed.append(chute.upper())

# print("✅ Benchmark finalizado! Resultados em results/benchmark.txt")

