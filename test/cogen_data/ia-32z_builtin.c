int __ia32z_builtin_mult(int x, int y)
{
  int s;
  s = 0;
  if (y < 0) {
    x = -x;
    y = -y;
  }
  while (y != 0) {
    if (y % 2 == 1) s = s + x;
    x = x + x;
    y = y / 2;
  }
  return s;
}

int div_(int y, int x)
{
  if (y < x) return 0;
  else {
    int z;
    int q;
    int r;
    z = x;
    q = 1;
    r = y - x;
    while (r > z) {
      r = r - z;
      z = z + z;
      q = q + q;
    }
    return q + div_(r, x);
  }
}

int __ia32z_builtin_div(int y, int x)
{
  if (x < 0) {
    if (y < 0) return div_(-y, -x);
    else return -div_(y, -x);
  } else {
    if (y < 0) return -div_(-y, x);
    else return div_(y, x);
  }
}

int __ia32z_builtin_rem(int y, int x)
{
  int q;
  q = y / x;
  return y - q * x;
}

