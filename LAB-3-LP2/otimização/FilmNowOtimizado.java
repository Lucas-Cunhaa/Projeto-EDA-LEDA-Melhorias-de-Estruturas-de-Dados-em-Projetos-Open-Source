import java.util.HashMap;

/**
 * Sistema que gerencia filmes e sua lista de filmes favoritos (Hot List).
 * Pode armazenar até 100 filmes e 10 filmes favoritos.
 * 
 * A classe permite adicionar, remover filmes, buscar filmes por posição, 
 * e manipular a lista de favoritos (Hot List).
 * 
 * @author eliane
 */
public class FilmNowOtimizado {
	
    /**
     * HashMap que contém os filmes.
     */
	private HashMap<String, FilmeOtimizado> filmes; 

    /**
     * HashMap que contém os filmes favoritos.
     */
	private HashMap<String, FilmeOtimizado> hotList;

    /**
     * Cria um novo sistema FilmNow.
     * Inicializa as listas de filmes e de filmes favoritos.
     */
	public FilmNowOtimizado() {
		this.filmes = new HashMap<>();
		this.hotList = new HashMap<>();
	}
	
    /**
     * Acessa a lista de filmes armazenados.
     * 
     * @return Um array com todos os filmes.
     */
	public FilmeOtimizado[] getFilmes() {
		return filmes.values().toArray(new FilmeOtimizado[0]);
	}

    /**
     * Acessa a lista de filmes favoritos (Hot List).
     * 
     * @return Um array com os filmes favoritos.
     */
	public FilmeOtimizado[] getHotList() {
		return hotList.values().toArray(new FilmeOtimizado[0]);
	}
	
    /**
     * Acessa os dados de um filme específico na posição fornecida.
     * 
     * @param nome Nome do filme.
     * @return O objeto Filme correspondente à posição.
     */
	public FilmeOtimizado getFilme(String nome) {
		if(existeFilme(nome)) return filmes.get(nome);
        else return null;
	}

    /**
     * Detalha as informações de um filme específico na posição fornecida.
     * 
     * @param nome Nome do filme.
     * @return Uma string com as informações do filme ou uma mensagem de erro.
     */
	public String detalharFilme(String nome) {
		if (!existeFilme(nome)) return "FILME NÃO EXISTE";
		return filmes.get(nome).toString();
		
	}

    /**
     * Cadastra um filme em uma posição específica. Se já houver um filme naquela posição, o anterior é sobrescrito.
     * 
     * @param nome Nome do filme.
     * @param ano Ano de lançamento do filme.
     * @param local Local onde o filme pode ser assistido.
     * @return Uma mensagem indicando o status da operação.
     */
	public String cadastraFilme(String nome, int ano, String local) {
		FilmeOtimizado novoFilme = new FilmeOtimizado(nome, ano, local);
		if (existeFilme(novoFilme.getNome())) return "FILME JA ADICIONADO";
		filmes.put(nome, novoFilme);
		return "FILME ADICIONADO";
	}

    /**
     * Adiciona um filme à Hot List (lista de favoritos).
     * 
     * @param nome Nome do filme que vai ser adicionado.
     * @return Uma mensagem indicando o status da operação.
     * @throws ArrayIndexOutOfBoundsException Se a posição fornecida for inválida.
     */
	public String adicionarHot(String nome) {
		if(existeFilmeHot(nome)) return "FILME JA ADICIONADO!";
		else if(!existeFilme(nome)) return "FILME NAO EXISTENTE!";
		else {
			hotList.put(nome, filmes.get(nome));
			filmes.get(nome).setStatusHot(true);
			return "ADICIONADO À HOTLIST";
			}
		
	} 
	
    /**
     * Remove um filme da Hot List (lista de favoritos).
     * 
     * @param nome Nome do filme que vai ser removido.
     * @return True se o filme foi removido com sucesso, false caso contrário.
     * @throws ArrayIndexOutOfBoundsException Se a posição fornecida for inválida.
     */
	public boolean removerHot(String nome) {
		if(existeFilmeHot(nome)){
            hotList.remove(nome);
            return true;
        } return false;
		
	}

    /**
     * Remove um filme específico da Hot List (lista de favoritos).
     * 
     * @param filmeRemover O filme a ser removido.
     */
	public void removerHot(FilmeOtimizado filmeRemover) {
		String filme = filmeRemover.getNome();
		if(existeFilmeHot(filme)){
            hotList.remove(filme);
        } 

	}
	
    /**
     * Remove um filme da lista de filmes.
     * 
     * @param nome Nome do filme que vai ser removido.
     * @return Uma mensagem indicando o status da operação.
     */
	public String removerFilme(String nome) {
		if(existeFilmeHot(nome)) removerHot(nome);
		if(existeFilme(nome)) {
			filmes.remove(nome);
			return "FILME REMOVIDO";
		} else {
            return "FILME NAO EXISTE";
        }
			
	}
	
    /**
     * Exibe todos os filmes na lista fornecida.
     * 
     * @param filmes O mapa de filmes a ser exibido.
     * @return Uma string com a lista de filmes formatada.
     */
	public String mostrarFilmes() {
    	String msg = "";
    	int i = 1;
    	for (FilmeOtimizado f : this.filmes.values()) {
       		msg += formataFilme(f.getNome()) + "\n";
        	i++;
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
	public String mostrarFilmes(int ano) {
        String msg = "FILMES COM MESMO ANO: \n\n";
        int i = 1;
        for (FilmeOtimizado f : this.filmes.values()) {
            if (f.getAno() == ano) {
                msg += formataFilme(f.getNome()) + "\n";
                i++;
            }
        }
        return msg.trim();
    }

	
    /**
     * Formata a impressão de um filme.
     * 
     * @param filme O nome do filme a ser formatado.
     * @return A string formatada do filme.
     */
	private String formataFilme(String filme) {
		return " - " + filme;
	}
	
    /**
     * Verifica se um filme já existe em uma lista de filmes.
     * 
     * @param novoFilme O filme a ser verificado.
     * @return True se o filme já existe no mapa, false caso contrário.
     */
	private boolean existeFilme(String nome) {
		return this.filmes.containsKey(nome);
	}
	
	/**
     * Verifica se um filme já existe na hotlist.
     * 
     * @param novoFilme O filme a ser verificado.
     * @return True se o filme já existe no mapa, false caso contrário.
     */
	
	private boolean existeFilmeHot(String nome) {
		return this.hotList.containsKey(nome);
	}
   
}



class TestaFilmNow {
    public static void main(String[] args) {
        // Instancia o sistema
        FilmNowOtimizado fn = new FilmNowOtimizado();

        // Cadastra alguns filmes diretamente no sistema
        fn.cadastraFilme("Matrix", 1999, "HBO");
        fn.cadastraFilme("Interestelar", 2014, "Netflix");
        fn.cadastraFilme("Oppenheimer", 2023, "Prime");

        // Testa mostrar todos os filmes
        System.out.println("==== TODOS OS FILMES ====");
        System.out.println(fn.mostrarFilmes());

        // Testa mostrar filmes de um ano específico
        System.out.println("\n==== FILMES DE 2014 ====");
        System.out.println(fn.mostrarFilmes(2014));

        // Testa filme que não existe
        System.out.println("\n==== FILMES DE 2000 ====");
        System.out.println(fn.mostrarFilmes(2000));

        // Testa detalhar filme existente
        System.out.println("\n==== DETALHAR 'Matrix' ====");
        System.out.println(fn.detalharFilme("Matrix"));

        // Testa detalhar filme inexistente
        System.out.println("\n==== DETALHAR 'Avatar' ====");
        System.out.println(fn.detalharFilme("Avatar"));
    }
}
