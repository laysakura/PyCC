int get_random(int r)
{
  return r * 1103515245 + 12345;
}

int c0func(int a, int b, int c, int d, int e, int f)
{
  int i;
  int r;
  int cnt;
  int x;
  int y;
  int z;
  
  i = 0;
  r = c;
  cnt = 0;
  while(i < a)
    {
      r = get_random(r);
      x = r % b;
      r = get_random(r);
      y = r % b;
      r = get_random(r);
      z = r % b;
      if(x * x + y * y + z * z <= b * b)
        {
          cnt = cnt + 1;
        }
      i = i + 1;
    }
  print_int(cnt * 6 / a);
  print_char(46);
  print_int(cnt * 6 % a);
  print_line();
  return 0;
}
