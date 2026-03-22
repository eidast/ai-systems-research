using System.Text.Json;
using System.Text.Json.Nodes;

var path = args[0];
var data = JsonSerializer.Deserialize<JsonArray>(File.ReadAllText(path))!;
var agg = new SortedDictionary<string, Dictionary<string, int>>();
foreach (var node in data)
{
    var obj = node!.AsObject();
    var category = obj["category"]!.GetValue<string>();
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
    var bucket = agg[category];
    bucket["count"] += 1;
    bucket["value_sum"] += obj["value"]!.GetValue<int>();
    bucket["weight_sum"] += obj["weight"]!.GetValue<int>();
    if (obj["active"]!.GetValue<bool>()) bucket["active_count"] += 1;
}
var output = new Dictionary<string, object>
{
    ["total_records"] = data.Count,
    ["categories"] = agg,
};
Console.WriteLine(JsonSerializer.Serialize(output));
