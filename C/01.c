#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void HextoTwo(int num)
{
    int res;
    int i = 0;
    char buf[BUFSIZ][5] = {"0000"};
    char reference[16][5] = {"0000","0001","0010","0011",\
                        "0100","0101","0110","0111",\
                        "1000","1001","1010","1011",\
                        "1100","1101","1110","1111"};

    while(num / 16 !=  0)
    {
        res = num % 16;
        strcpy(buf[i++], reference[res]);
        num = num / 16;
    }

    res = num % 16;
    strcpy(buf[i++], reference[res]);

    while(i > 0)
        printf("%s ", buf[--i]);
}

int main()
{
    int num1 = 0xBEF;// 0xBEF让第二高位的1置零，以及第三高位的1置零，把过程写出来
    num1 &= ~(0x3 << 8);
    HextoTwo(num1);
    printf("\n");
    int num2 = 0xabc;//0xabc让第二高位的0变成1，把过程写出来
    num2 |= (0x1 << 8);
    HextoTwo(num2);
    return EXIT_SUCCESS;
}