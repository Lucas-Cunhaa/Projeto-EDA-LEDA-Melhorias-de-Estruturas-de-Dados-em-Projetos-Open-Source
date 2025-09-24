from benchmark import gerar_casos, medir_tempo
from concurrent.futures import ThreadPoolExecutor, as_completed
from prune_algorithms import prune, pruneOptimized

def test_performance(caso, func):
    """
    Returns the average execution time of the function
    """
    time_total = 0
    times_to_run = 1_000
    
    for _ in range(times_to_run):
        time_total += medir_tempo(caso, func) / times_to_run
    
    return {
        "n_itemset": len(caso["itemset"]),
        "time(ns)": f"{time_total:.0f}"
    }


def append_results_to_file(casos, func):
    results = []

    # Executa cada caso em paralelo
    with ThreadPoolExecutor() as executor:
        future_to_case = {executor.submit(test_performance, caso, func): caso for caso in casos}

        for future in as_completed(future_to_case):
            results.append(future.result())
            
    # Salva resultados -> individuais nesse caso
    write_results_to_file([results], [func.__name__])
            
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

    casos = gerar_casos(tamanhos_itemset, num_candidates, tamanho_candidate)
    
    print("iniciando os testes de performance...")
    
    results_optimized = append_results_to_file(casos, pruneOptimized)
    
    print("testes da funcao otimizada finalizada")
    print("inicio do caso de teste default")
    
    results_default = append_results_to_file(casos, prune)
    
    print("imprimindo resultados dos dois testes em um único arquivo....")
    
    write_results_to_file([results_optimized, results_default], [pruneOptimized.__name__, prune.__name__])
    
    print("fim dos testes -> ja estao no diretorio results")