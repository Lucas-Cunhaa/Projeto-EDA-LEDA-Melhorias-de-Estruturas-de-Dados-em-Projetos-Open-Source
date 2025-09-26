from benchmark import gerar_casos_benchmark, medir_tempo
from concurrent.futures import ThreadPoolExecutor, as_completed
from prune_algorithms import prune, pruneOptimized

def test_performance(caso, func):
    """
    Returns the average execution time of the function
    """
    time_total = 0
    times_to_run = 100
    
    for _ in range(times_to_run):
        time_total += medir_tempo(caso, func) / times_to_run
    
    return {
        "n_itemset": len(caso["itemset"]),
        "time(ns)": f"{time_total:.0f}"
    }


def append_results_to_file(casos, func, test_name):
    results = []

    # Executa cada caso em paralelo
    with ThreadPoolExecutor() as executor:
        future_to_case = {executor.submit(test_performance, caso, func): caso for caso in casos}

        for future in as_completed(future_to_case):
            results.append(future.result())
            
    # Salva resultados -> individuais nesse caso
    write_results_to_file([results], [func.__name__ + test_name])
            
    return results

def write_results_to_file(functions_results: list, functions_names: list):
    file_name = "_".join(name for name in functions_names) 
    
    with open(f"results/{file_name}_algoritm_results.txt", "w") as file:
        file.write("Method Time Sample\n")
        for i in range(len(functions_results)):
            for result in functions_results[i]:
                file.write(f"{functions_names[i]} {result['time(ns)']} {result['n_itemset']}\n")
                
if __name__ == "__main__":
    tamanhos_itemset = [i for i in range(1000, 101_000, 1_000)] # Tamanhos para casos de testes -> numero variável 
    
    num_candidates = 100 # Numero de candidatos em cada caso de teste -> numero fixo
    tamanho_candidate = 10 # Tamanho de cada candidato -> numero fixo

    casos = gerar_casos_benchmark(tamanhos_itemset, num_candidates, tamanho_candidate)
    test_name = "_pior_caso"
    
    print("iniciando os testes do pior caso...")
    
    results_optimized = append_results_to_file(casos["pior_caso"], pruneOptimized, test_name)
    
    print("testes da funcao otimizada finalizada")
    print("inicio do caso de teste default")
    
    results_default = append_results_to_file(casos["pior_caso"], prune, test_name)
    
    print("imprimindo resultados dos dois testes em um único arquivo....")
    
    write_results_to_file([results_optimized, results_default], [pruneOptimized.__name__ + test_name, prune.__name__ + test_name])
    
    test_name = "_caso_medio"
    print("iniciando os testes do caso medio...")
    
    results_optimized_medio = append_results_to_file(casos["caso_medio"], pruneOptimized, test_name)
    
    print("testes da funcao otimizada finalizada")
    print("inicio do caso de teste default")
    
    results_default_medio = append_results_to_file(casos["caso_medio"], prune, test_name)
    
    print("imprimindo resultados dos dois testes em um único arquivo....")
    
    write_results_to_file([results_optimized_medio, results_default_medio], [pruneOptimized.__name__ + test_name, prune.__name__ + test_name])

    print("fim dos testes -> ja estao no diretorio results")