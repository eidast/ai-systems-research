using System.Collections.Concurrent;
using System.Text.Json;

static int Transform(int x) => (x * 3 + 7) % 1000;

var itemCount = args.Length > 0 ? int.Parse(args[0]) : 100000;
var workers = 4;
var queueCapacity = 256;
var queue = new BlockingCollection<int>(queueCapacity);
var results = new ConcurrentBag<(int Count, int Sum)>();

var tasks = Enumerable.Range(0, workers).Select(_ => Task.Run(() =>
{
    var count = 0;
    var sum = 0;
    foreach (var item in queue.GetConsumingEnumerable())
    {
        count++;
        sum += Transform(item);
    }
    results.Add((count, sum));
})).ToArray();

for (var i = 0; i < itemCount; i++) queue.Add(i);
queue.CompleteAdding();
Task.WaitAll(tasks);

var payload = new {
    item_count = results.Sum(x => x.Count),
    value_sum = results.Sum(x => x.Sum),
    workers,
    queue_capacity = queueCapacity,
};
Console.WriteLine(JsonSerializer.Serialize(payload));
