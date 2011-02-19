int f(int arg1, int arg2, int arg3)
{
    int a;
    int b;
    int c;
    a = 4;
    b = 33;
    if (a <= b) {
        a = 333;
        while (1) {
            int x;
            int y;
            int z;
            x = 3;
            y = 4;
            a = 999 * y + x;
            break;
        }
    }
    return 888;
}

int g()
{
    int X;
    int Y;
    Y = -1000;
    X = 3333 +  f(444, Y, 666);
    return !X;
}
