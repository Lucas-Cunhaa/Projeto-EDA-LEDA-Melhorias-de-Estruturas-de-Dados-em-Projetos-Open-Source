import os
import time
from unittest.mock import patch
from hangman import spacedOut as spacedOut_lista  


os.makedirs("../results", exist_ok=True)

palavras_teste = [
    "python",
    "ufcg",
    "benchmark",
    "proclameiud",
    "fundeiorspa",
    "juntarexico",
    "campolidrue",
]

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
    
    with open("../results/benchmark.txt", "a") as f:
        f.write("Method Time(ms) Sample\n\n")


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


