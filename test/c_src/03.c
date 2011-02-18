int f()
{
    int a;
    int b;
    int c;
    if (1) {
        a = 333;
    }
    a = 444;
    if (b == c) {
        a = 777;
    } else {
        while (1) {
            a = 999;
            break;
        }
    }
}
