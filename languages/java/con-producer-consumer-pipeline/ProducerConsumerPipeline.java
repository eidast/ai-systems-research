import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.atomic.AtomicInteger;

public class ProducerConsumerPipeline {
    static int transform(int x) { return (x * 3 + 7) % 1000; }

    public static void main(String[] args) throws Exception {
        int itemCount = args.length > 0 ? Integer.parseInt(args[0]) : 100000;
        int workers = 4;
        int queueCapacity = 256;
        BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(queueCapacity);
        AtomicInteger totalCount = new AtomicInteger();
        AtomicInteger totalSum = new AtomicInteger();
        Thread[] consumers = new Thread[workers];

        for (int i = 0; i < workers; i++) {
            consumers[i] = new Thread(() -> {
                try {
                    while (true) {
                        int item = queue.take();
                        if (item == -1) break;
                        totalCount.incrementAndGet();
                        totalSum.addAndGet(transform(item));
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
            consumers[i].start();
        }

        for (int i = 0; i < itemCount; i++) queue.put(i);
        for (int i = 0; i < workers; i++) queue.put(-1);
        for (Thread t : consumers) t.join();

        System.out.println("{\"item_count\":" + totalCount.get() + ",\"value_sum\":" + totalSum.get() + ",\"workers\":" + workers + ",\"queue_capacity\":" + queueCapacity + "}");
    }
}
