package ufcg_lp2_implementation.src.main.java;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.io.BufferedReader;

public class MainDefault {

    public static void main(String[] args) {
          try {
	            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	            String line = "";

	            System.out.println("Method Time Sample");
	            while ((line = reader.readLine()) != null) {
	                String[] tokens = line.split(" ");
                    FilmNow fm = new FilmNow();

					System.out.println(Arrays.toString(tokens););
	                long start = System.nanoTime();
	                int pos = 98;
					if(Arrays.equals(tokens, new String[0]));
	                System.out.println(fm.cadastraFilme(pos, tokens[0], Integer.parseInt(tokens[1]), tokens[2]));
	                long end = System.nanoTime();
	                long time = end - start;

	                //System.out.println("Cadastra-Filmes " + (time) + " " + tokens.length);
	            }
	        } catch (IOException ioe) {}
    }

}


