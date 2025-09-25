import java.util.ArrayList;
import java.util.HashMap;

public class benchmark {
    
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

        public static void main(String[] args) {
            int N = 1_000_000;
            benchmarkMemory(N);
            benchmarkRuntime(N, 5);
        }
    
    
        public static long getUsedMemory() {
            Runtime runtime = Runtime.getRuntime();
            return runtime.totalMemory() - runtime.freeMemory();
        }
    
        public static void benchmarkMemory(int N) {
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
            System.out.println("Memória HashMap: " + usedMap / 1e6 + " MB");
            System.out.println("Memória Classe: " + usedClass / 1e6 + " MB");
        }

        public static void benchmarkRuntime(int N, int runs) {
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

                System.out.printf("Run %d | Tempo HashMap: %.2f ms | Tempo Classe: %.2f ms\n",
                    i, (endMap - startMap) / 1e6, (endClass - startClass) / 1e6);
            }
        }
}
