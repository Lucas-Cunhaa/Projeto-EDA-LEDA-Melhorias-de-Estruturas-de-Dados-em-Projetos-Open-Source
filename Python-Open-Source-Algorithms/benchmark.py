import time
import random
from collections import Counter

def gerar_casos_benchmark(tamanhos_itemset, num_candidates, tamanho_candidate):
    """
    Gera casos de teste para benchmarking: pior caso e caso médio realista baseado em frequências.
    
    :param tamanhos_itemset: lista de tamanhos de itemsets, ex: [1000, 2000, 5000]
    :param num_candidates: número de candidatos por caso
    :param tamanho_candidate: tamanho de cada candidato
    :return: dicionário {"pior_caso": [...], "caso_medio": [...]}
             Cada lista contém dicionários {"itemset": [...], "candidates": [[...], ...]}
    """
    pior_caso = []
    caso_medio = []

    for n in tamanhos_itemset:
        # --- Pior caso ---
        itemset = [str(i) for i in range(n)]
        candidates_pior = [[str(i) for i in range(tamanho_candidate)] for _ in range(num_candidates)]
        pior_caso.append({"itemset": itemset, "candidates": candidates_pior})

        # --- Caso médio realista com frequências ---
        # Criar um "histograma" de frequências de itens: itens iniciais são mais frequentes
        frequencias = Counter({str(i): max(1, n - i) for i in range(n)})  # itens mais próximos de 0 são mais frequentes
        itens = list(frequencias.keys())
        pesos = list(frequencias.values())

        candidates_medio = []
        for _ in range(num_candidates):
            candidate = random.choices(itens, weights=pesos, k=tamanho_candidate)
            
            # Adicionar alguns itens completamente ausentes para realismo
            num_ausentes = max(1, tamanho_candidate // 5)  # 20% ausentes
            ausentes = [str(n + random.randint(1, n*10)) for _ in range(num_ausentes)]
            candidate = candidate[:tamanho_candidate - num_ausentes] + ausentes
            
            random.shuffle(candidate)
            candidates_medio.append(candidate)

        caso_medio.append({"itemset": itemset, "candidates": candidates_medio})

    return {"pior_caso": pior_caso, "caso_medio": caso_medio}  
    
def medir_tempo(caso, func, length=None):
    itemset = caso["itemset"]
    candidates = caso["candidates"]
    length = length or (len(candidates[0]) if candidates else 0)
    
    start = time.perf_counter_ns()
    func(itemset, candidates, length)
    end = time.perf_counter_ns()
    
    return end - start