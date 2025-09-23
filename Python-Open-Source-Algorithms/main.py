from collections import Counter
from benchmark import gerar_casos, medir_tempo
from concurrent.futures import ThreadPoolExecutor, as_completed


def prune(itemset: list, candidates: list, length: int) -> list:
    pruned = []
    for candidate in candidates: 
        is_subsequence = True
        for item in candidate: 
            if item not in itemset or itemset.count(item) < length - 1: 
                is_subsequence = False
                break
        if is_subsequence:
            pruned.append(candidate)
    return pruned


def pruneOptimized(itemset: list, candidates: list, length: int) -> list:
    itemset_counter = Counter(itemset) 
    pruned = []
    for candidate in candidates: 
        is_subsequence = True
        for item in candidate: 
            if item not in itemset_counter or itemset_counter[item] < length - 1: 
                is_subsequence = False
                break
        if is_subsequence:
            pruned.append(candidate)
    return pruned


def test_performance(caso, func):
    """
    Returns the average execution time of the function
    """
    time_total = 0
    times_to_run = 1000
    
    for _ in range(times_to_run):
        time_total += medir_tempo(caso, func) / times_to_run
    
    return {
        "n_itemset": len(caso["itemset"]),
        "time(ns)": f"{time_total:.0f}"
    }


def append_results_to_file(casos, func):
    results = []
    func_name = func.__name__

    # Executa cada caso em paralelo
    with ThreadPoolExecutor() as executor:
        future_to_case = {executor.submit(test_performance, caso, func): caso for caso in casos}

        for future in as_completed(future_to_case):
            results.append(future.result())

    # Salva resultados
    with open(f"results/{func_name}_algoritm_results.txt", "w") as file:
        file.write("Method Time Sample\n")
        for result in results:
            file.write(f"{func_name} {result['time(ns)']} {result['n_itemset']}\n")


if __name__ == "__main__":
    tamanhos_itemset = [i for i in range(1000, 101_000, 1_000)]
    
    num_candidates = 200
    tamanho_candidate = 10

    casos = gerar_casos(tamanhos_itemset, num_candidates, tamanho_candidate)
    
    print("iniciando os testes de performance...")
    append_results_to_file(casos, pruneOptimized)
    print("testes da funcao otimizada finalizada")
    print("inicio do caso de teste default")
    append_results_to_file(casos, prune)
    print("fim dos testes -> ja estao no diretorio results")
