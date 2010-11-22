#include <stdio.h>

void prnName(struct stName *mySt)
{
    printf("Number = %d, ", mySt->uiNum);
    printf("Letter = %c.\n", mySt->ucLtr);

    return;
}

int main(int argc, char *argv[])
{
    printf("Hello, world!\n");
    return 0;
}

