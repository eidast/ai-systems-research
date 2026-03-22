public class PrimeCount {
    public static int countPrimes(int limit) {
        if (limit < 2) return 0;
        boolean[] sieve = new boolean[limit + 1];
        for (int i = 2; i <= limit; i++) sieve[i] = true;
        for (int p = 2; p * p <= limit; p++) {
            if (sieve[p]) {
                for (int multiple = p * p; multiple <= limit; multiple += p) {
                    sieve[multiple] = false;
                }
            }
        }
        int count = 0;
        for (int i = 2; i <= limit; i++) {
            if (sieve[i]) count++;
        }
        return count;
    }

    public static void main(String[] args) {
        int upper = 100000;
        if (args.length > 0) {
            upper = Integer.parseInt(args[0]);
        }
        System.out.println(countPrimes(upper));
    }
}
