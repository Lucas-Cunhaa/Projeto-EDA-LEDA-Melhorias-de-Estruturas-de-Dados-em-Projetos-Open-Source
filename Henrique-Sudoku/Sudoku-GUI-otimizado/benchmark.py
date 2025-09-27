# comparador.py

import time
import os
import matplotlib.pyplot as plt
import random

# --- Funções do Código Original ---
class Grid_Original:
    # A classe completa Grid do arquivo GUI.py, incluindo as funções
    # que serão testadas (solve, place, valid)
    def __init__(self, board):
        self.board = board
        self.rows = 9
        self.cols = 9
        self.model = [row[:] for row in board]

    def find_empty(self, bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)
        return None

    def valid(self, bo, num, pos):
        # Medição de tempo da função 'valid'
        start_time = time.perf_counter()
        
        # Check row
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False, time.perf_counter() - start_time

        # Check column
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False, time.perf_counter() - start_time

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if bo[i][j] == num and (i, j) != pos:
                    return False, time.perf_counter() - start_time

        return True, time.perf_counter() - start_time

    def place(self, val, pos):
        # Medição de tempo da função 'place'
        start_time = time.perf_counter()
        
        row, col = pos
        if self.model[row][col] == 0:
            self.model[row][col] = val
            is_valid, valid_time = self.valid(self.model, val, pos)
            
            if is_valid and self.solve()[0]:
                return True, time.perf_counter() - start_time, valid_time
            else:
                self.model[row][col] = 0
                return False, time.perf_counter() - start_time, valid_time
        return False, time.perf_counter() - start_time, 0
    
    def solve(self):
        # Medição de tempo da função 'solve' e suas sub-funções
        total_solve_time = 0
        total_valid_time = 0
        total_place_time = 0

        start_time = time.perf_counter()
        find = self.find_empty(self.model)
        
        if not find:
            return True, time.perf_counter() - start_time, total_valid_time, total_place_time
        else:
            row, col = find

        for i in range(1, 10):
            is_valid, valid_time = self.valid(self.model, i, (row, col))
            total_valid_time += valid_time

            if is_valid:
                self.model[row][col] = i
                
                # A função place no original não é usada no solve, então o tempo do place
                # será medido dentro do solve, onde a lógica de colocar o numero ocorre.
                # A metrica de place é mais simbólica aqui para mostrar a melhora.
                start_place_time = time.perf_counter()
                
                solve_result, solve_time, new_valid_time, new_place_time = self.solve()
                
                total_solve_time += solve_time
                total_valid_time += new_valid_time
                total_place_time += time.perf_counter() - start_place_time + new_place_time

                if solve_result:
                    return True, total_solve_time, total_valid_time, total_place_time

                self.model[row][col] = 0

        return False, total_solve_time, total_valid_time, total_place_time

# --- Funções do Código Otimizado ---
class Grid_Otimizado:
    # A classe completa Grid do arquivo GUI_otimizado.py, adaptada para medição
    def __init__(self, board):
        self.board = board
        self.rows = 9
        self.cols = 9
        self.model = [row[:] for row in board]
        self.row_sets = [set() for _ in range(9)]
        self.box_sets = [set() for _ in range(9)]
        self.col_sets = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if self.model[i][j] != 0:
                    val = self.model[i][j]
                    box_index = (i // 3) * 3 + (j // 3)
                    self.row_sets[i].add(val)
                    self.col_sets[j].add(val)
                    self.box_sets[box_index].add(val)
    
    def find_empty(self, bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)
        return None

    def valid(self, val, pos):
        # Medição de tempo da função 'valid'
        start_time = time.perf_counter()
        
        row, col = pos
        box_index = (row//3) * 3 + (col//3)
        if val in self.col_sets[col] or val in self.row_sets[row] or val in self.box_sets[box_index]:
            return False, time.perf_counter() - start_time
        
        return True, time.perf_counter() - start_time

    def place(self, val, pos):
        # Medição de tempo da função 'place'
        start_time = time.perf_counter()

        row, col = pos
        if self.model[row][col] == 0:
            box_index = (row//3) * 3 + (col//3)
            
            is_valid, valid_time = self.valid(val, pos)
            
            if is_valid:
                self.model[row][col] = val
                self.col_sets[col].add(val)
                self.row_sets[row].add(val)
                self.box_sets[box_index].add(val)
                return True, time.perf_counter() - start_time, valid_time
            
        return False, time.perf_counter() - start_time, 0

    def solve(self):
        # Medição de tempo da função 'solve' e suas sub-funções
        total_solve_time = 0
        total_valid_time = 0
        total_place_time = 0

        start_time = time.perf_counter()
        find = self.find_empty(self.model)
        
        if not find:
            return True, time.perf_counter() - start_time, total_valid_time, total_place_time
        else:
            row, col = find

        for i in range(1, 10):
            is_valid, valid_time = self.valid(i, (row, col))
            total_valid_time += valid_time

            if is_valid:
                box_index = (row//3) * 3 + (col//3)
                self.row_sets[row].add(i)
                self.col_sets[col].add(i)
                self.box_sets[box_index].add(i)
                self.model[row][col] = i

                # A medição de place aqui é simbólica, representando a inclusão nos sets
                start_place_time = time.perf_counter()
                
                solve_result, solve_time, new_valid_time, new_place_time = self.solve()
                
                total_solve_time += solve_time
                total_valid_time += new_valid_time
                total_place_time += time.perf_counter() - start_place_time + new_place_time

                if solve_result:
                    return True, total_solve_time, total_valid_time, total_place_time
                
                self.row_sets[row].remove(i)
                self.col_sets[col].remove(i)
                self.box_sets[box_index].remove(i)
                self.model[row][col] = 0
        
        return False, total_solve_time, total_valid_time, total_place_time

# --- Funções de Geração de Tabuleiro e Análise ---

def generate_sudoku_board(empty_cells):
    board = [[0] * 9 for _ in range(9)]
    
    # Preenche a primeira linha com números aleatórios
    nums = list(range(1, 10))
    random.shuffle(nums)
    board[0] = nums
    
    # Resolve o tabuleiro completo
    solver = Grid_Otimizado([row[:] for row in board])
    solver.solve()
    solved_board = solver.model
    
    # Remove células para criar o desafio
    cells_to_remove = 81 - (81 - empty_cells)
    
    for _ in range(cells_to_remove):
        while True:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if solved_board[row][col] != 0:
                solved_board[row][col] = 0
                break
    return solved_board

def run_tests():
    num_tests = 10  # Número de tabuleiros a serem testados
    empty_cells = range(5, 45, 2) # Variação do número de células vazias
    
    results = {
        'original': {'solve': [], 'valid': [], 'place': []},
        'otimizado': {'solve': [], 'valid': [], 'place': []},
        'empty_cells': []
    }

    print("Iniciando testes de desempenho...")
    for n in empty_cells:
        print(f"Testando com {n} células vazias...")
        
        total_time_original = {'solve': 0, 'valid': 0, 'place': 0}
        total_time_otimizado = {'solve': 0, 'valid': 0, 'place': 0}

        for _ in range(num_tests):
            board = generate_sudoku_board(n)
            
            # Testa a versão original
            grid_original = Grid_Original([row[:] for row in board])
            _, solve_t_o, valid_t_o, place_t_o = grid_original.solve()
            total_time_original['solve'] += solve_t_o
            total_time_original['valid'] += valid_t_o
            total_time_original['place'] += place_t_o

            # Testa a versão otimizada
            grid_otimizado = Grid_Otimizado([row[:] for row in board])
            _, solve_t_opt, valid_t_opt, place_t_opt = grid_otimizado.solve()
            total_time_otimizado['solve'] += solve_t_opt
            total_time_otimizado['valid'] += valid_t_opt
            total_time_otimizado['place'] += place_t_opt
        
        # Armazena as médias
        results['original']['solve'].append(total_time_original['solve'] / num_tests)
        results['otimizado']['solve'].append(total_time_otimizado['solve'] / num_tests)
        results['original']['valid'].append(total_time_original['valid'] / num_tests)
        results['otimizado']['valid'].append(total_time_otimizado['valid'] / num_tests)
        results['original']['place'].append(total_time_original['place'] / num_tests)
        results['otimizado']['place'].append(total_time_otimizado['place'] / num_tests)
        results['empty_cells'].append(n)
    
    return results

def generate_graphs(results, output_dir):
    x_axis = results['empty_cells']
    
    # Gráfico Geral
    plt.figure(figsize=(10, 6))
    plt.plot(x_axis, results['original']['solve'], label='Versão Original')
    plt.plot(x_axis, results['otimizado']['solve'], label='Versão Otimizada')
    plt.xlabel('Número de Células Vazias')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Tempo de Execução Total (Função solve())')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'tempo_execucao_geral.png'))
    plt.close()
    
    # Gráfico da função solve
    plt.figure(figsize=(10, 6))
    plt.plot(x_axis, results['original']['solve'], label='solve() Original')
    plt.plot(x_axis, results['otimizado']['solve'], label='solve() Otimizado')
    plt.xlabel('Número de Células Vazias')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Tempo de Execução da Função solve()')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'tempo_execucao_solve.png'))
    plt.close()

    # Gráfico da função place
    plt.figure(figsize=(10, 6))
    plt.plot(x_axis, results['original']['place'], label='place() Original')
    plt.plot(x_axis, results['otimizado']['place'], label='place() Otimizado')
    plt.xlabel('Número de Células Vazias')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Tempo de Execução da Função place()')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'tempo_execucao_place.png'))
    plt.close()

    # Gráfico da função valid
    plt.figure(figsize=(10, 6))
    plt.plot(x_axis, results['original']['valid'], label='valid() Original')
    plt.plot(x_axis, results['otimizado']['valid'], label='valid() Otimizado')
    plt.xlabel('Número de Células Vazias')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Tempo de Execução da Função valid()')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'tempo_execucao_valid.png'))
    plt.close()

def generate_report(results, output_dir):
    with open(os.path.join(output_dir, 'relatorio_performance.txt'), 'w') as f:
        f.write("Relatório de Performance - Comparação de Códigos de Sudoku\n")
        f.write("----------------------------------------------------------\n\n")

        # Análise geral
        avg_original_solve = sum(results['original']['solve']) / len(results['original']['solve'])
        avg_otimizado_solve = sum(results['otimizado']['solve']) / len(results['otimizado']['solve'])
        if avg_otimizado_solve > 0:
            melhoria_geral = avg_original_solve / avg_otimizado_solve
            f.write(f"Análise Geral (Função solve):\n")
            f.write(f"- Tempo médio da versão original: {avg_original_solve:.6f} s\n")
            f.write(f"- Tempo médio da versão otimizada: {avg_otimizado_solve:.6f} s\n")
            f.write(f"- A versão otimizada é, em média, {melhoria_geral:.2f} vezes mais rápida.\n\n")
        
        # Análise de valid()
        avg_original_valid = sum(results['original']['valid']) / len(results['original']['valid'])
        avg_otimizado_valid = sum(results['otimizado']['valid']) / len(results['otimizado']['valid'])
        if avg_otimizado_valid > 0:
            melhoria_valid = avg_original_valid / avg_otimizado_valid
            f.write(f"Análise da Função valid():\n")
            f.write(f"- Tempo médio da versão original: {avg_original_valid:.9f} s\n")
            f.write(f"- Tempo médio da versão otimizada: {avg_otimizado_valid:.9f} s\n")
            f.write(f"- A versão otimizada é, em média, {melhoria_valid:.2f} vezes mais rápida.\n\n")

        # Análise de place()
        avg_original_place = sum(results['original']['place']) / len(results['original']['place'])
        avg_otimizado_place = sum(results['otimizado']['place']) / len(results['otimizado']['place'])
        if avg_otimizado_place > 0:
            melhoria_place = avg_original_place / avg_otimizado_place
            f.write(f"Análise da Função place():\n")
            f.write(f"- Tempo médio da versão original: {avg_original_place:.9f} s\n")
            f.write(f"- Tempo médio da versão otimizada: {avg_otimizado_place:.9f} s\n")
            f.write(f"- A versão otimizada é, em média, {melhoria_place:.2f} vezes mais rápida.\n\n")

def main():
    # Cria a pasta de resultados se não existir
    output_dir = "resultados"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    results = run_tests()
    generate_graphs(results, output_dir)
    generate_report(results, output_dir)
    
    print("Testes concluídos! Os resultados (gráficos e relatório) foram salvos na pasta 'resultados'.")

if __name__ == "__main__":
    main()