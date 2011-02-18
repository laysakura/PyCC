#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <time.h>
#include <sys/time.h>

#define RDTSC(x) __asm__ __volatile__ ("rdtsc" : "=A" (x))

double get_time(void)
{
  struct timeval tv;
  
  gettimeofday(&tv, NULL);
  return tv.tv_sec + tv.tv_usec * 1e-6;
}

long long get_rdtsc(void)
{
  long long x;
  RDTSC(x);
  return x;
}

int print_int(int d)
{
  printf("%d", d);
  fflush(stdout);
  return 0;
}

int print_char(int d)
{
  printf("%c", d);
  fflush(stdout);
  return 0;
}

int print_space(void)
{
  printf(" ");
  fflush(stdout);
  return 0;
}

int print_line(void)
{
  printf("\n");
  fflush(stdout);
  return 0;
}

int main(int argc, char ** argv)
{
  long long c0, c1;
  int arg[6];
  int i;
  double t0, t1;
  
  for(i = 0; i < 6; i++)
    {
      arg[i] = 0;
    }
  for(i = 1; i < argc && i < 6; i++)
    {
      arg[i - 1] = atoi(argv[i]);
    }
  
  t0 = get_time();
  c0 = get_rdtsc();
  
  c0func(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5]);
  
  c1 = get_rdtsc();
  t1 = get_time();
  
  fprintf(stderr, "time = %.12lf sec\n", t1 - t0);
  fprintf(stderr, "cycles = %lld\n", c1 - c0);
  return 0;
}
