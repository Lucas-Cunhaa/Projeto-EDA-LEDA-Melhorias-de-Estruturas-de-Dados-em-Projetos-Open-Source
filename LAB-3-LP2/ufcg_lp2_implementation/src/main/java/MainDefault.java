package ufcg_lp2_implementation.src.main.java;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.io.BufferedReader;

public class MainDefault {
	public static final String NOME_FILME_TESTE = "Filme Teste"; 
	public static final int ANO_FILME_TESTE = 1;
	public static final String NOME_LOCAL_TESTE = "Local Test"; 
    public static final int QUANTIDADE_EXECUCAO_POR_AMOSTRA = 20;
    public static void main(String[] args) {
          try {
	            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	            String line = "";

	            System.out.println("Method Time Sample");
	            while ((line = reader.readLine()) != null) {
	                String[] tokens = line.split(" ");

					for (String tamanho : tokens) {
						for (int i = 0; i <= QUANTIDADE_EXECUCAO_POR_AMOSTRA; i++) {
							if(tamanho.equals("") || tamanho.equals(" ")) break;
							FilmNow fm = new FilmNow(Integer.parseInt(tamanho));

							long start = System.nanoTime();
							fm.cadastraFilme(0, tamanho, 0, line);

							long end = System.nanoTime();
	               			long time = end - start;

							System.out.println("Cadastra-Filmes " + (time) + " " + tamanho);

							fm.removerFilme(0);
						}
					}
	            }
	        } catch (IOException ioe) {}
    }

}


