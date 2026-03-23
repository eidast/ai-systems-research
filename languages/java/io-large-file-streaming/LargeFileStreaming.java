import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
import java.util.TreeMap;

public class LargeFileStreaming {
    public static void main(String[] args) throws Exception {
        Map<String, int[]> agg = new TreeMap<>();
        int total = 0;
        for (String line : Files.readAllLines(Path.of(args[0]))) {
            if (line.isBlank()) continue;
            String[] parts = line.split(",");
            String category = parts[1];
            int value = Integer.parseInt(parts[2]);
            int weight = Integer.parseInt(parts[3]);
            int active = Integer.parseInt(parts[4]);
            agg.putIfAbsent(category, new int[] {0,0,0,0});
            int[] b = agg.get(category);
            b[0] += 1;
            b[1] += value;
            b[2] += weight;
            b[3] += active;
            total += 1;
        }
        StringBuilder sb = new StringBuilder();
        sb.append("{\"total_records\":").append(total).append(",\"categories\":{");
        boolean first = true;
        for (var entry : agg.entrySet()) {
            if (!first) sb.append(",");
            first = false;
            int[] b = entry.getValue();
            sb.append("\"").append(entry.getKey()).append("\":{")
              .append("\"count\":").append(b[0]).append(",")
              .append("\"value_sum\":").append(b[1]).append(",")
              .append("\"weight_sum\":").append(b[2]).append(",")
              .append("\"active_count\":").append(b[3]).append("}");
        }
        sb.append("}}");
        System.out.println(sb.toString());
    }
}
