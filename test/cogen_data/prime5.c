int c0func(int a, int b, int c, int d, int e, int f)
{
  int i;
  int j;
  int sum;
  int flag;
  int a0;
  int a1;
  int a2;
  int a3;
  int a4;
  
  a0 = 0;
  a1 = 0;
  a2 = 0;
  a3 = 0;
  a4 = 0;
  i = 2;
  while(i < a)
    {
      j = 2;
      sum = 0;
      flag = 0;
      while(j * j <= i)
        {
          if(i % j == 0)
            {
              flag = 1;
              break;
            }
          j = j + 1;
        }
      if(flag == 0)
        {
          a0 = a1;
          a1 = a2;
          a2 = a3;
          a3 = a4;
          a4 = i;
          if(a1 == a0 + 2)
            if(a2 == a0 + 6)
              if(a3 == a0 + 8)
                if(a4 == a0 + 12)
                    {
                      print_int(a0);
                      print_space();
                      print_int(a1);
                      print_space();
                      print_int(a2);
                      print_space();
                      print_int(a3);
                      print_space();
                      print_int(a4);
                      print_line();
                    }
          if(a1 == a0 + 4)
            if(a2 == a0 + 6)
              if(a3 == a0 + 10)
                if(a4 == a0 + 12)
                    {
                      print_int(a0);
                      print_space();
                      print_int(a1);
                      print_space();
                      print_int(a2);
                      print_space();
                      print_int(a3);
                      print_space();
                      print_int(a4);
                      print_line();
                    }
        }
      i = i + 1;
    }
}
