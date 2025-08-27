package ufcg_lp2_optmized_implementation.src.main.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static final String NOME_FILME_TESTE = "Filme Teste"; 
	public static final int ANO_FILME_TESTE = 1;
	public static final String NOME_LOCAL_TESTE = "Local Test"; 
    public static final int QUANTIDADE_EXECUCAO_POR_AMOSTRA = 1000;
    public static void main(String[] args) {
          try {
	            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	            String line = "";

	            System.out.println("Method Sample Time");
	            while ((line = reader.readLine()) != null) {
	                String[] tokens = line.split(" ");

					for (String tamanho : tokens) {
						long time = 0;
						FilmNowOtimizado fmOtm = new FilmNowOtimizado();

						for (int i = 0; i <= QUANTIDADE_EXECUCAO_POR_AMOSTRA; i++) {	
							long start = System.nanoTime();
							fmOtm.cadastraFilme(NOME_FILME_TESTE, ANO_FILME_TESTE, NOME_LOCAL_TESTE);

							long end = System.nanoTime();
	               			time += (end - start) / QUANTIDADE_EXECUCAO_POR_AMOSTRA;

							fmOtm.removerFilme(NOME_FILME_TESTE);
						}
						System.out.println("Cadastra-Filmes-OTIMIZADO " + tamanho+  " " + (time));
					}
	            }
	        } catch (IOException ioe) {}
    }
}
