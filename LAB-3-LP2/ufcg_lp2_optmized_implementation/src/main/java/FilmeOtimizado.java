package ufcg_lp2_optmized_implementation.src.main.java;

import java.util.Objects;
import java.util.Arrays;
import java.util.HashMap;
import java.util.stream.Collectors;

public class FilmeOtimizado {

/**
 * Classe que representa um filme, com seu nome, ano de lançamento e locais onde pode ser assistido.
 * A classe permite adicionar, remover locais de exibição e controlar o status de "favorito" do filme.
 * 
 * Os filmes podem ter no máximo 5 locais de exibição.
 */
    /**
     * Limite máximo de locais onde um filme pode ser assistido.
     */
    private static final int LIMITELOCAIS = 5;

    /**
     * Nome do filme.
     */
    private String nome;

    /**
     * Ano de lançamento do filme.
     */
    private int ano;

    /**
     * Lista de locais onde o filme pode ser assistido.
     */
    private HashMap<String,Integer> locaisAssistir;
    private int locaisTail;

    /**
     * Status de "favorito" do filme.
     * Se o status for verdadeiro, o filme é marcado como favorito, pois esta na hotList em filmNow.
     */
    private boolean statusHot;

    /**
     * Constrói um objeto Filme com o nome, ano e um local inicial de exibição.
     * 
     * @param nome Nome do filme.
     * @param ano Ano de lançamento do filme.
     * @param localAssistir Local onde o filme pode ser assistido.
     * @throws NullPointerException Se o nome do filme for nulo.
     * @throws IllegalArgumentException Se o nome do filme vazio.
     */
    public FilmeOtimizado(String nome, int ano, String localAssistir) {
    	if (nome == null) 
        	throw new NullPointerException("FILME INVALIDO");
        if (nome.trim().isEmpty()) 
            throw new IllegalArgumentException("FILME INVALIDO");
        else this.nome = nome;
        this.ano = ano;
        this.locaisAssistir = new HashMap<>();
        this.adicionarLocalAssistir(localAssistir);
        this.statusHot = false; // Filme não é favorito por padrão
        this.locaisTail = 0;
    }

    /**
     * Retorna uma representação em formato de string do filme e seus locais de exibição.
     * Se o status do filme for "favorito", o nome do filme será precedido pelo símbolo de fogo (🔥).
     * 
     * @return A representação do filme com seus locais de exibição.
     */
    @Override
    public String toString() {
        if (isStatusHot()) return "🔥 " + nome + ", " + ano + "\n" + toStringLocais();
        return nome + ", " + ano + "\n" + toStringLocais();
    }

    /**
     * Retorna um código de hash para o filme, baseado no nome e ano.
     * 
     * @return O código de hash do filme.
     */
    @Override
    public int hashCode() {
        return Objects.hash(ano, nome);
    }

    /**
     * Compara o filme com outro objeto para verificar se são iguais, considerando nome e ano.
     * 
     * @param obj Objeto a ser comparado.
     * @return True se o filme for igual ao outro objeto, false caso contrário.
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        FilmeOtimizado other = (FilmeOtimizado) obj;
        return ano == other.getAno() && Objects.equals(nome, other.getNome());
    }

    /**
     * Retorna o nome do filme.
     * 
     * @return O nome do filme.
     */
    public String getNome() {
        return nome;
    }

    /**
     * Retorna os locais onde o filme pode ser assistido.
     * 
     * @return Um array com os locais de exibição do filme.
     */
    public String[] getLocalAssistir() {
        return this.locaisAssistir.keySet().toArray(new String[0]);
    }

    /**
     * Remove um local onde o filme pode ser assistido.
     * 
     * @param nomeLocal O nome do local a ser removido.
     * @return True se o local foi removido com sucesso, false caso contrário.
     */
    public boolean removerLocal(String nomeLocal) {
        if (this.quantLocais() <= 1) return false;
        int indice = indiceLocal(nomeLocal);
        if (indice == -1) return false;
        locaisAssistir.remove(nomeLocal);
        return true;
    }

    /**
     * Retorna o índice de um local específico no array de locais de exibição.
     * 
     * @param nomeLocal O nome do local a ser procurado.
     * @return O índice do local, ou -1 se o local não for encontrado.
     */
    private int indiceLocal(String nomeLocal) {
        if (!this.locaisAssistir.containsKey(nomeLocal)){
          return -1;
        }
        return this.locaisAssistir.get(nomeLocal); 
    }

    /**
     * Adiciona um novo local onde o filme pode ser assistido.
     * 
     * @param localAssistir O nome do novo local.
     * @return True se o local foi adicionado com sucesso, false caso contrário.
     * @throws NullPointerException Se o nome do local for nulo.
     * @throws IllegalArgumentException Se o nome do local for vazio.
     */
    public boolean adicionarLocalAssistir(String localAssistir) {
    	if (localAssistir == null) 
        	throw new NullPointerException("FILME INVALIDO");
        if (localAssistir.trim().isEmpty()) 
            throw new IllegalArgumentException("FILME INVALIDO");
        int indice = indicePermiteAdicionar(localAssistir);
        if (indice == -1) return false;
        this.locaisAssistir.put(localAssistir, locaisTail);
        this.locaisTail++;
        return true;
    }

    /**
     * Retorna o índice onde um novo local pode ser adicionado.
     * 
     * @param localAssistir O nome do local a ser adicionado.
     * @return O índice onde o local pode ser inserido, ou -1 se não for possível adicionar mais locais.
     */
    private int indicePermiteAdicionar(String localAssistir) {
        if (this.locaisTail >= LIMITELOCAIS){
          return -1;
        }
        return this.locaisTail;
    }

    /**
     * Retorna a lista de locais onde o filme pode ser assistido, como uma string.
     * 
     * @return Uma string contendo todos os locais onde o filme pode ser assistido, separados por vírgula.
     */
    public String toStringLocais() {
      String[] locaisArray = this.locaisAssistir.keySet().toArray(new String[0]);
        return Arrays.stream(locaisArray).filter(local -> local != null).collect(Collectors.joining(", "));
    }

    /**
     * Retorna o ano de lançamento do filme.
     * 
     * @return O ano de lançamento do filme.
     */
    public int getAno() {
        return ano;
    }

    /**
     * Verifica se o filme é um "favorito".
     * 
     * @return True se o filme for favorito, false caso contrário.
     */
    public boolean isStatusHot() {
        return statusHot;
    }

    /**
     * Define o status do filme como "favorito".
     * 
     * @param statusHot O status do filme, onde true significa que o filme é favorito.
     */
    public void setStatusHot(boolean statusHot) {
        this.statusHot = statusHot;
    }
    
    /**
     * Retorna a quantidade de locais onde o filme pode ser assistido.
     * 
     * @return A quantidade de locais onde o filme pode ser assistido.
     */
    private int quantLocais() {
        return this.locaisTail;
    }
}

