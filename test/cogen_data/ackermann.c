int ack(int m, int n)
{
  if(m == 0)
    return n + 1;
  if(n == 0)
    return ack(m - 1, 1);
  return ack(m - 1, ack(m, n - 1));
}

int c0func(int a, int b, int c, int d, int e, int f)
{
  int i;
  
  i = 0;
  while(i < b)
    {
      print_int(ack(a, i));
      print_line();
      i = i + 1;
    }
  return 0;
}
