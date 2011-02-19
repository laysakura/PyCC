int f()
{
    return e(0, 333);
}

int g(int a)
{
    return -a;
}

int e(int x, int y)
{
    int cnt;

    if (x) {
        return 777;
    }
    else
        return g(y);
}

