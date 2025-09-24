import time

def gerar_casos(tamanhos_itemset, num_candidates, tamanho_candidate):
    """
    Gera vários casos de teste para benchmarking com apenas strings.
    
    :param tamanhos_itemset: lista de tamanhos de itemsets, ex: [1000, 2000, 5000]
    :param num_candidates: número de candidatos por caso
    :param tamanho_candidate: tamanho de cada candidato
    :return: lista de dicionários {"itemset": [...], "candidates": [[...], ...]}
    """
    casos = []
    for n in tamanhos_itemset:
        # itemset como strings
        itemset = [str(i) for i in range(n)]
        # candidatos também como strings
        candidates = [[str(i) for i in range(tamanho_candidate)] for _ in range(num_candidates)]
        casos.append({
            "itemset": itemset,
            "candidates": candidates
        })
        
    return casos    
    
def medir_tempo(caso, func, length=None):
    itemset = caso["itemset"]
    candidates = caso["candidates"]
    length = length or (len(candidates[0]) if candidates else 0)
    
    start = time.perf_counter_ns()
    func(itemset, candidates, length)
    end = time.perf_counter_ns()
    
    return end - start