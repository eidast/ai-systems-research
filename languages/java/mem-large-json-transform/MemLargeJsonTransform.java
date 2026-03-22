import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MemLargeJsonTransform {
    private static final Pattern OBJECT_PATTERN = Pattern.compile(
        "\\{\\s*\"id\"\\s*:\\s*(\\d+)\\s*,\\s*\"category\"\\s*:\\s*\"([^\"]+)\"\\s*,\\s*\"value\"\\s*:\\s*(\\d+)\\s*,\\s*\"weight\"\\s*:\\s*(\\d+)\\s*,\\s*\"active\"\\s*:\\s*(true|false)\\s*,\\s*\"name\"\\s*:\\s*\"([^\"]+)\"\\s*\\}"
    );

    public static void main(String[] args) throws Exception {
        String raw = Files.readString(Path.of(args[0]));
        Matcher matcher = OBJECT_PATTERN.matcher(raw);
        Map<String, int[]> agg = new TreeMap<>();
        int total = 0;
        while (matcher.find()) {
            String category = matcher.group(2);
            int value = Integer.parseInt(matcher.group(3));
            int weight = Integer.parseInt(matcher.group(4));
            boolean active = Boolean.parseBoolean(matcher.group(5));
            agg.putIfAbsent(category, new int[] {0, 0, 0, 0});
            int[] bucket = agg.get(category);
            bucket[0] += 1;
            bucket[1] += value;
            bucket[2] += weight;
            if (active) bucket[3] += 1;
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
