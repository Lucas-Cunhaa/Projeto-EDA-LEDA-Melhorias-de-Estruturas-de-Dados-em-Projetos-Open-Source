package main.java;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) {
          try {
	            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	            String line = "";
	            // Cabeçalho
	            System.out.println("Method Time Sample");
	            while ((line = reader.readLine()) != null) {
	                String[] tokens = line.split(" ");
                    FilmNow fm = new FilmNow();
	                // medindo tempo de execução 
	                long start = System.nanoTime();
	                
	                // TODO incluir aqui chamada para o método sob análise
	                
	                System.out.println(fm);
	                long end = System.nanoTime();
	                long time = end - start;
	                
	                // saída padrão: método tempo tamanho_da_entrada
	                System.out.println("Cadastra Filmes " + (time) + " " + tokens.length);

	            }
	        } catch (IOException ioe) {}
    }
}
