using System.Text.Json;

var path = args[0];
var agg = new SortedDictionary<string, Dictionary<string, int>>();
var total = 0;
foreach (var line in File.ReadLines(path))
{
    if (string.IsNullOrWhiteSpace(line)) continue;
    var parts = line.Split(',');
    var category = parts[1];
    var value = int.Parse(parts[2]);
    var weight = int.Parse(parts[3]);
    var active = int.Parse(parts[4]);
    if (!agg.ContainsKey(category))
    {
        agg[category] = new Dictionary<string, int>
        {
            ["count"] = 0,
            ["value_sum"] = 0,
            ["weight_sum"] = 0,
            ["active_count"] = 0,
        };
    }
    var b = agg[category];
    b["count"] += 1;
    b["value_sum"] += value;
    b["weight_sum"] += weight;
    b["active_count"] += active;
    total += 1;
}
Console.WriteLine(JsonSerializer.Serialize(new { total_records = total, categories = agg }));
