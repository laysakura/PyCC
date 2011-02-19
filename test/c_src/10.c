int f()
{
    return g();
}

int g()
{
    while(1) {
        break;
    }
    return 777;
}

