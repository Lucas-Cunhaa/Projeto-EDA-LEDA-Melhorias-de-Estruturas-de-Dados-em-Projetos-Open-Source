import matplotlib.pyplot as plt 
import numpy as np 
import re

def parse_file(filename):
    """
    Lê o arquivo e extrai os dados de tempo e amostra
    """
    amostras = []
    tempos_ms = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            # Pula o cabeçalho se existir
            for line in lines:
                if line.strip() and 'Method Time Sample' not in line:
                    # Usa regex para extrair números
                    numbers = re.findall(r'\d+', line)
                    if len(numbers) >= 2:
                        tempo = int(numbers[0])
                        amostra = int(numbers[1])
                        amostras.append(amostra)
                        tempos_ms.append(tempo)
                        
        return amostras, tempos_ms
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado!")
        return [], []
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return [], []

def create_plots(amostras, tempos_ms, method_name):
    """
    Cria os gráficos com os dados
    """
    if not amostras or not tempos_ms:
        print("Nenhum dado para plotar!")
        return
    
    # Convertendo para segundos
    tempos_segundos = [t/1000 for t in tempos_ms]
    
    # Criando figura com subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle(f'Análise de Desempenho - Método: {method_name}', fontsize=16, fontweight='bold')
    
    # Gráfico 1: Linha (ms)
    ax1.plot(amostras, tempos_ms, 'o-', linewidth=2, markersize=8, color='blue', markerfacecolor='white', markeredgewidth=2)
    ax1.set_title('Tempo de Execução vs Tamanho da Amostra')
    ax1.set_xlabel('Tamanho da Amostra (quantidade)')
    ax1.set_ylabel('Tempo (ms)')
    ax1.grid(True, alpha=0.3)
    
    # Adicionar valores nos pontos
    for i, (x, y) in enumerate(zip(amostras, tempos_ms)):
        ax1.annotate(f'{y/1000:.1f}s', (x, y), textcoords="offset points", 
                    xytext=(0,10), ha='center', fontsize=8)
    
    # Gráfico 2: Linha (segundos)
    ax2.plot(amostras, tempos_segundos, 's-', linewidth=2, markersize=8, color='red', markerfacecolor='white', markeredgewidth=2)
    ax2.set_title('Tempo de Execução vs Tamanho da Amostra')
    ax2.set_xlabel('Tamanho da Amostra (quantidade)')
    ax2.set_ylabel('Tempo (segundos)')
    ax2.grid(True, alpha=0.3)
    
    # Gráfico 3: Barras
    bars = ax3.bar([str(a) for a in amostras], tempos_ms, 
                  color=plt.cm.viridis(np.linspace(0, 1, len(amostras))), 
                  alpha=0.7, edgecolor='black')
    ax3.set_title('Tempo por Tamanho de Amostra')
    ax3.set_xlabel('Tamanho da Amostra')
    ax3.set_ylabel('Tempo (ms)')
    
    # Adicionar valores nas barras
    for bar, tempo in zip(bars, tempos_ms):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(tempos_ms)*0.02, 
                f'{tempo/1000:.1f}s', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Gráfico 4: Tendência com regressão
    ax4.scatter(amostras, tempos_ms, color='green', s=100, alpha=0.7, edgecolor='black')
    
    # Linha de tendência
    z = np.polyfit(amostras, tempos_ms, 1)
    p = np.poly1d(z)
    ax4.plot(amostras, p(amostras), "r--", alpha=0.8, linewidth=2,
             label=f'y = {z[0]:.1f}x + {z[1]:.1f}')
    
    ax4.set_title('Tendência do Tempo de Execução')
    ax4.set_xlabel('Tamanho da Amostra')
    ax4.set_ylabel('Tempo (ms)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Análise estatística
    print("=== ANÁLISE ESTATÍSTICA ===")
    print(f"Maior tempo: {max(tempos_ms):,} ms ({max(tempos_segundos):.1f} s)")
    print(f"Menor tempo: {min(tempos_ms):,} ms ({min(tempos_segundos):.1f} s)")
    print(f"Tempo médio: {np.mean(tempos_ms):.1f} ms ({np.mean(tempos_segundos):.1f} s)")
    print(f"Taxa de crescimento: {z[0]:.1f} ms por unidade")
    print(f"Tempo inicial (overhead): {z[1]:.1f} ms")

def main():
    """
    Função principal
    """
    # Nome do arquivo - altere conforme necessário
    filename = "LAB-3-LP2/results/result.txt"
    
    # Lê os dados do arquivo
    print(f"Lendo arquivo: {filename}")
    amostras, tempos_ms = parse_file(filename)
    
    if amostras and tempos_ms:
        print("Dados lidos com sucesso!")
        print(f"Amostras: {amostras}")
        print(f"Tempos (ms): {tempos_ms}")
        
        # Gera os gráficos
        create_plots(amostras, tempos_ms, "Cadastra-Filmes")
    else:
        print("Não foi possível ler os dados do arquivo.")

if __name__ == "__main__":
    main()
