int fib(int n)
{
  if (n < 2) {
    return 1;
  } else {
    return fib(n - 1) + fib(n - 2);
  }
}

int c0func(int a, int b, int c, int d, int e, int f)
{
  print_int(fib(a));
  print_line();
  return 0;
}
