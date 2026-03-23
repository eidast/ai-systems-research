using System.Text.Json;

static int Transform(int x) => (x * 7 + 11) % 1000;
var itemCount = args.Length > 0 ? int.Parse(args[0]) : 200000;
var workers = 4;
var chunk = (int)Math.Ceiling((double)itemCount / workers);
var tasks = Enumerable.Range(0, workers).Select(w => Task.Run(() =>
{
    var start = w * chunk;
    var end = Math.Min(start + chunk, itemCount);
    var count = 0;
    var sum = 0;
    for (var i = start; i < end; i++) { sum += Transform(i); count += 1; }
    return (count, sum);
})).ToArray();
Task.WaitAll(tasks);
var payload = new {
    item_count = tasks.Sum(t => t.Result.count),
    value_sum = tasks.Sum(t => t.Result.sum),
    workers,
};
Console.WriteLine(JsonSerializer.Serialize(payload));
