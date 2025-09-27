import java.io.FileWriter;
import java.util.ArrayList;
import java.util.HashMap;

public class benchmark {

    static FileWriter csvWriter;
    
    static class MoveItem {
        String nr;
        String move; 
        String annotation;
        int turn;
        
        public MoveItem(String nr, String move, String annotation, int turn) {
            this.nr = nr;
            this.move = move;
            this.annotation = annotation;
            this.turn = turn;
        }   
    }

        public static void main(String[] args) throws Exception {
            csvWriter = new FileWriter("benchmarkresults.csv");
            csvWriter.append("Run,N,Structure,MemoryMB,TimeMS\n");

            int N = 1_000_000;
            benchmarkMemory(N);
            benchmarkRuntime(N, 5);

            csvWriter.flush();
            csvWriter.close();
        }
    
    
        public static long getUsedMemory() {
            Runtime runtime = Runtime.getRuntime();
            return runtime.totalMemory() - runtime.freeMemory();
        }
    
        public static void benchmarkMemory(int N) throws Exception {
            //HashMap insertion
            ArrayList<HashMap<String, String>> mapMoves = new ArrayList<>();
            for(int i = 0; i < N; i++) {
                HashMap<String, String> item = new HashMap<>();
                item.put("nr", "testeNR");
                item.put("move", "testeMove");
                item.put("annotation", "testeAnnotation");
                item.put("turn", Integer.toString(0));
                mapMoves.add(item);
            }
            try {
                System.gc();
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            long usedMap = getUsedMemory();
            
            mapMoves = null;
            //Class insertion 
            ArrayList<MoveItem> objMoves = new ArrayList<>();
            for(int i = 0; i < N; i++) {
                MoveItem item = new MoveItem("testeNR", "testeMove", "testeAnnotation", 0);
                objMoves.add(item);
            }
            try {
                System.gc();
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            long usedClass = getUsedMemory();
            csvWriter.append("0," + N + ",HashMap," + (usedMap / 1e6) + ",\n");
            csvWriter.append("0," + N + ",Classe," + (usedClass / 1e6) + ",\n");
        }

        public static void benchmarkRuntime(int N, int runs) throws Exception {
            for(int i = 0; i <= runs; i++) {
                //Hashmap
                long startMap = System.nanoTime();
                ArrayList<HashMap<String, String>> mapMoves = new ArrayList<>();
                for(int j = 0; j < N; j++) {
                    HashMap<String, String> item = new HashMap<>();
                    item.put("nr", "testeNR");
                    item.put("move", "testeMove");
                    item.put("annotation", "testeAnnotation");
                    item.put("turn", Integer.toString(0));
                    mapMoves.add(item);
                }
                long endMap = System.nanoTime();

                //Classe
                long startClass = System.nanoTime();
                ArrayList<MoveItem> objMoves = new ArrayList<>();
                for(int c = 0; c < N; c++) {
                    MoveItem item = new MoveItem("testeNR", "testeMove", "testeAnnotation", 0);
                    objMoves.add(item);
                }
                long endClass = System.nanoTime();

                csvWriter.append(i + "," + N + ",HashMap,," + ((endMap-startMap)/1e6) + "\n");
                csvWriter.append(i + "," + N + ",Classe,," + ((endClass-startClass)/1e6) + "\n");
            }
        }
}
