package src.main.java;
/**
 * Sistema que gerencia filmes e sua lista de filmes favoritos (Hot List).
 * Pode armazenar até 100 filmes e 10 filmes favoritos.
 * 
 * A classe permite adicionar, remover filmes, buscar filmes por posição, 
 * e manipular a lista de favoritos (Hot List).
 * 
 * @author eliane
 */
public class FilmNow {
	
    /**
     * Tamanho máximo da lista de filmes.
     */
	private static final int TAMANHO = 100;

    /**
     * Tamanho máximo da lista de filmes favoritos (Hot List).
     */
	private static final int TAMANHO_HOT_LIST = 10;
	
    /**
     * Lista que contém os filmes.
     */
	private Filme[] filmes; 

    /**
     * Lista que contém os filmes favoritos.
     */
	private Filme[] hotList;

    /**
     * Cria um novo sistema FilmNow.
     * Inicializa as listas de filmes e de filmes favoritos.
     */
	public FilmNow() {
		this.filmes = new Filme[TAMANHO];
		this.hotList = new Filme[TAMANHO_HOT_LIST];
	}
	
    /**
     * Acessa a lista de filmes armazenados.
     * 
     * @return Um array com todos os filmes.
     */
	public Filme[] getFilmes() {
		return this.filmes.clone();
	}

    /**
     * Acessa a lista de filmes favoritos (Hot List).
     * 
     * @return Um array com os filmes favoritos.
     */
	public Filme[] getHotList() {
		return this.hotList.clone();
	}
	
    /**
     * Acessa os dados de um filme específico na posição fornecida.
     * 
     * @param posicao A posição do filme na lista.
     * @return O objeto Filme correspondente à posição.
     * @throws ArrayIndexOutOfBoundsException Se a posição for inválida.
     */
	public Filme getFilme(int posicao) {
		verificarLimites(posicao, filmes);
		return filmes[posicao - 1];
	}

    /**
     * Detalha as informações de um filme específico na posição fornecida.
     * 
     * @param posicao A posição do filme na lista.
     * @return Uma string com as informações do filme ou uma mensagem de erro.
     */
	public String detalharFilme(int posicao) {
		try {
			verificarLimites(posicao, filmes);
			if (filmes[posicao - 1] == null) return "POSIÇÃO INVÁLIDA";
			return filmes[posicao - 1].toString();
		} catch (ArrayIndexOutOfBoundsException e) {
			return e.getMessage();
		}
	}

    /**
     * Cadastra um filme em uma posição específica. Se já houver um filme naquela posição, o anterior é sobrescrito.
     * 
     * @param posicao Posição onde o filme será adicionado.
     * @param nome Nome do filme.
     * @param ano Ano de lançamento do filme.
     * @param local Local onde o filme pode ser assistido.
     * @return Uma mensagem indicando o status da operação.
     * @throws ArrayIndexOutOfBoundsException Se a posição fornecida for inválida.
     */
	public String cadastraFilme(int posicao, String nome, int ano, String local) {
		try {
			verificarLimites(posicao, filmes);
			Filme novoFilme = new Filme(nome, ano, local);
			if (existeFilme(novoFilme, filmes)) return "FILME JA ADICIONADO";
			if (filmes[posicao - 1] != null && filmes[posicao - 1].isStatusHot()) removerHot(filmes[posicao - 1]);
			filmes[posicao - 1] = novoFilme;
			return "FILME ADICIONADO";
		} catch(ArrayIndexOutOfBoundsException e) {
			return e.getMessage();
		}
	}

    /**
     * Adiciona um filme à Hot List (lista de favoritos).
     * 
     * @param posicaoFilme A posição do filme na lista de filmes.
     * @param posicaoHotList A posição na Hot List onde o filme será adicionado.
     * @return Uma mensagem indicando o status da operação.
     * @throws ArrayIndexOutOfBoundsException Se a posição fornecida for inválida.
     */
	public String adicionarHot(int posicaoFilme, int posicaoHotList) {
		try {
			verificarLimites(posicaoHotList, hotList);
			verificarLimites(posicaoFilme, filmes);
			if (existeFilme(filmes[posicaoFilme - 1], hotList)) 
				return "FILME JA ADICIONADO!";
			if (filmes[posicaoFilme - 1] == null) 
				return "FILME NAO EXISTENTE!";
			if (hotList[posicaoHotList - 1] != null) 
				hotList[posicaoHotList - 1].setStatusHot(false);
			hotList[posicaoHotList - 1] = filmes[posicaoFilme - 1];
			hotList[posicaoHotList - 1].setStatusHot(true);
			return "ADICIONADO À HOTLIST NA POSIÇÃO " + posicaoHotList + "!";
		} catch(ArrayIndexOutOfBoundsException e) {
			return e.getMessage();
		}
	} 
	
    /**
     * Remove um filme da Hot List (lista de favoritos).
     * 
     * @param posicaoHot A posição do filme a ser removido da Hot List.
     * @return True se o filme foi removido com sucesso, false caso contrário.
     * @throws ArrayIndexOutOfBoundsException Se a posição fornecida for inválida.
     */
	public boolean removerHot(int posicaoHot) {
		try {
			verificarLimites(posicaoHot, hotList);
			hotList[posicaoHot - 1] = null;
			return true;
		} catch(ArrayIndexOutOfBoundsException e) { 
			System.err.println(e.getMessage());
			return false;
		}
	}

    /**
     * Remove um filme específico da Hot List (lista de favoritos).
     * 
     * @param filmeRemover O filme a ser removido.
     */
	public void removerHot(Filme filmeRemover) {
		for (int i = 0; i < hotList.length; i++) {
			if (hotList[i] == null) continue;
			if (hotList[i].equals(filmeRemover)) hotList[i] = null;
		}
	}
	
    /**
     * Remove um filme da lista de filmes.
     * 
     * @param posicaoFilme A posição do filme a ser removido.
     * @return Uma mensagem indicando o status da operação.
     * @throws ArrayIndexOutOfBoundsException Se a posição fornecida for inválida.
     */
	public String removerFilme(int posicaoFilme) {
		try {
			verificarLimites(posicaoFilme, filmes);
			if(filmes[posicaoFilme - 1] != null && filmes[posicaoFilme - 1].isStatusHot()) 
				removerHot(filmes[posicaoFilme - 1]);
			filmes[posicaoFilme - 1] = null;
			return "FILME REMOVIDO";
		} catch (ArrayIndexOutOfBoundsException e) {
			return e.getMessage();	
		}
	}
	
    /**
     * Exibe todos os filmes na lista fornecida.
     * 
     * @param filmes A lista de filmes a ser exibida.
     * @return Uma string com a lista de filmes formatada.
     */
	public String mostrarFilmes(Filme[] filmes) {
		String msg = "";
		for (int i = 0; i < filmes.length; i++) {
			if (filmes[i] != null) {
				msg += formataFilme(i + 1, filmes[i].getNome()) + "\n";
			}
		}
		return msg.trim();
	}
	
    /**
     * Exibe todos os filmes que possuem o mesmo nome fornecido.
     * 
     * @param filmes A lista de filmes a ser buscada.
     * @param nomeFilme O nome do filme a ser buscado.
     * @return Uma string com a lista de filmes que correspondem ao nome fornecido.
     */
	public String mostrarFilmes(Filme[] filmes, String nomeFilme) {
		String msg = "FILMES COM MESMO NOME: \n\n";
		for (int i = 0; i < filmes.length; i++) {
			if (filmes[i] != null && filmes[i].getNome().equals(nomeFilme)) {
				msg += formataFilme(i + 1, filmes[i].getNome()) + "\n";
			}
		}
		return msg.trim();
	}
	
    /**
     * Exibe todos os filmes que foram lançados no mesmo ano fornecido.
     * 
     * @param filmes A lista de filmes a ser buscada.
     * @param ano O ano de lançamento a ser buscado.
     * @return Uma string com a lista de filmes que possuem o mesmo ano de lançamento.
     */
	public String mostrarFilmes(Filme[] filmes, int ano) {
		String msg = "FILMES COM MESMO ANO: \n\n";
		for (int i = 0; i < filmes.length; i++) {
			if (filmes[i] != null && filmes[i].getAno() == ano) {
				msg += formataFilme(i + 1, filmes[i].getNome()) + "\n";
			}
		}
		return msg.trim();
	}
	
    /**
     * Formata a impressão de um filme.
     * 
     * @param posicao A posição do filme na lista.
     * @param filme O nome do filme a ser formatado.
     * @return A string formatada do filme.
     */
	private String formataFilme(int posicao, String filme) {
		return posicao + " - " + filme;
	}
	
    /**
     * Verifica se um filme já existe em uma lista de filmes.
     * 
     * @param novoFilme O filme a ser verificado.
     * @param filmes A lista de filmes onde a verificação será realizada.
     * @return True se o filme já existe na lista, false caso contrário.
     */
	private boolean existeFilme(Filme novoFilme, Filme[] filmes) {
		for (Filme filme : filmes) {
			if (filme == null) continue;
			else if (filme.equals(novoFilme)) return true;
		}
		return false;
	}
	
    /**
     * Verifica se a posição fornecida está dentro dos limites válidos para a lista de filmes.
     * 
     * @param posicao A posição a ser verificada.
     * @param filmes A lista de filmes a ser verificada.
     * @throws ArrayIndexOutOfBoundsException Se a posição fornecida for inválida.
     */
	private boolean verificarLimites(int posicao, Filme[] filmes) throws ArrayIndexOutOfBoundsException {
		if (posicao < 1 || posicao > filmes.length) throw new ArrayIndexOutOfBoundsException("POSIÇÃO INVÁLIDA");
		return true;
	}	
}