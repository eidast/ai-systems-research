using System;

static int CountPrimes(int limit)
{
    if (limit < 2) return 0;
    var sieve = new bool[limit + 1];
    for (int i = 2; i <= limit; i++) sieve[i] = true;
    for (int p = 2; p * p <= limit; p++)
    {
        if (sieve[p])
        {
            for (int multiple = p * p; multiple <= limit; multiple += p)
            {
                sieve[multiple] = false;
            }
        }
    }
    var count = 0;
    for (int i = 2; i <= limit; i++)
    {
        if (sieve[i]) count++;
    }
    return count;
}

var upper = args.Length > 0 ? int.Parse(args[0]) : 100000;
Console.WriteLine(CountPrimes(upper));
