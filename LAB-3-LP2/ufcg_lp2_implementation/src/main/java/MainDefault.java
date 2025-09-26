package ufcg_lp2_implementation.src.main.java;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.io.BufferedReader;

public class MainDefault {
	public static final String NOME_FILME_TESTE = "Filme Teste"; 
	public static final int ANO_FILME_TESTE = 1;
	public static final String NOME_LOCAL_TESTE = "Local Test"; 
    public static final int QUANTIDADE_EXECUCAO_POR_AMOSTRA = 1000;
    public static void main(String[] args) {
          try {
	            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	            String line = "";

	            System.out.println("Method Time Sample");
	            while ((line = reader.readLine()) != null) {
	                String[] tokens = line.split(" ");

					for (String tamanho : tokens) {
						long time = 0;

						if(tamanho.equals("") ||tamanho.equals(" ")) continue;

						FilmNow fm = new FilmNow(Integer.parseInt(tamanho));
						fm.cadastraFilme(1, tamanho, 0, line);

						for (int i = 0; i <= QUANTIDADE_EXECUCAO_POR_AMOSTRA; i++) {	
	               			//time += testCadastraFilmes(fm);
							time += testAddHotFilmes(fm);
						}

						System.out.println("Adicionar-Hot " + (time) + " " + tamanho);
					}
	            }
	        } catch (IOException ioe) {}
    }

	public static long testCadastraFilmes(FilmNow fm) {
		long start = System.nanoTime();
		fm.cadastraFilme(1, NOME_FILME_TESTE, ANO_FILME_TESTE, NOME_LOCAL_TESTE);

		long end = System.nanoTime();

		fm.removerFilme(1);
		

		return (end - start) / QUANTIDADE_EXECUCAO_POR_AMOSTRA;
	}

	public static long testAddHotFilmes(FilmNow fm) {
		long start = System.nanoTime();
		fm.adicionarHot(1, 1);

		long end = System.nanoTime();

		fm.removerHot(1);
		

		return (end - start) / QUANTIDADE_EXECUCAO_POR_AMOSTRA;
	}
}


