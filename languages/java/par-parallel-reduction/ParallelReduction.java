import java.util.ArrayList;
import java.util.List;

public class ParallelReduction {
    static int transform(int x) { return (x * 7 + 11) % 1000; }
    public static void main(String[] args) throws Exception {
        int itemCount = args.length > 0 ? Integer.parseInt(args[0]) : 200000;
        int workers = 4;
        int chunk = (int)Math.ceil((double)itemCount / workers);
        List<Thread> threads = new ArrayList<>();
        int[] counts = new int[workers];
        int[] sums = new int[workers];
        for (int w = 0; w < workers; w++) {
            final int idx = w;
            final int start = w * chunk;
            final int end = Math.min(start + chunk, itemCount);
            threads.add(new Thread(() -> {
                int c = 0; int s = 0;
                for (int i = start; i < end; i++) { s += transform(i); c++; }
                counts[idx] = c; sums[idx] = s;
            }));
        }
        for (Thread t : threads) t.start();
        for (Thread t : threads) t.join();
        int totalCount = 0; int totalSum = 0;
        for (int i = 0; i < workers; i++) { totalCount += counts[i]; totalSum += sums[i]; }
        System.out.println("{\"item_count\":" + totalCount + ",\"value_sum\":" + totalSum + ",\"workers\":" + workers + "}");
    }
}
