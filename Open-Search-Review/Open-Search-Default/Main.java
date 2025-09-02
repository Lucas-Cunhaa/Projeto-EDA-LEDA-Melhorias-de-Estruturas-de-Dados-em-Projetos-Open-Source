import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static final int LOOPS = 1000;

    public static void main(String[] args) throws  FileNotFoundException, IOException {
        
        try (BufferedReader bf = new BufferedReader(new InputStreamReader(System.in))) {

            String line = "";

            System.out.println("Method Time Sample");

            while ((line = bf.readLine()) != null) {
                String[] sizes = line.split(" ");

                for (String size : sizes) {
                    long time1 = 0;
                    long time2 = 0;
                    // gera uma coleção toda de zero
                    Collection<Double> collection = toDoubleCollection(new double[Integer.parseInt(size)]);

                    for (long i = 0; i < LOOPS; i++) {
                        time1 += (testTimeMethodDefault(collection) / LOOPS);
                        time2 += (testTimeMethodOptimized(collection) / LOOPS);
                    }    

                    System.out.println("METHOD_DEAFAULT-TWO-LOOPS " + time1 + " " + collection.size());

                    System.out.println("METHOD_OPTMIZED-ONE-LOOP " + time2 + " " + collection.size());
                }
            }
        }
    }

    // metodo que recebe array 
    private static double linearWeightedAvgDefault(double[] values) {
        double avg = 0;
        long totalWeight = 1;
        long current = 1;

        for (double v : values) {
            if (Double.isNaN(v) == false) {
                avg += v * current;
                totalWeight += current;
                current += 1;
            }
        }
        return totalWeight == 1 ? Double.NaN : avg / totalWeight;
    }

    // metodo que vai receber a coleção 
    private static double linearWeightedAvgOtimized(Collection<Double> values) {
        double avg = 0;
        long totalWeight = 1;
        long current = 1;

        for (double v : values) {
            if (Double.isNaN(v) == false) {
                avg += v * current;
                totalWeight += current;
                current += 1;
            }
        }
        return totalWeight == 1 ? Double.NaN : avg / totalWeight;
    }

    private static long testTimeMethodDefault(Collection<Double> collection) {
        long start = System.nanoTime();

        linearWeightedAvgDefault(collection.stream().mapToDouble(Double::doubleValue).toArray());

        return System.nanoTime() - start;
    }

    private static long testTimeMethodOptimized(Collection<Double> collection) {
        long start = System.nanoTime();

        linearWeightedAvgOtimized(collection);

        return System.nanoTime() - start;
    }

    private static Collection<Double> toDoubleCollection(double[] array) throws NumberFormatException {
        List<Double> collection = new ArrayList<>();

        for (double n : array) {
            collection.add(n);
        }

        return collection;
    }
}
