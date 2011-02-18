int check_prime(int n)
{
  int d;
  d = 2;
  while (d * d <= n) {
    if (n % d == 0) return 0;
    d = d + 1;
  }
  return 1;
}

int count_primes(int n)
{
  int x;
  int c;
  x = 2;
  c = 0;
  while (x < n) {
    c = c + check_prime(x);
    x = x + 1;
  }
  return c;
}

int c0func(int a, int b, int c, int d, int e, int f)
{
  print_int(count_primes(a));
  print_line();
  return 0;
}
