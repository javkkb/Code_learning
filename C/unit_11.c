#include <stdio.h>

int result = 0;  // 定义全局变量 result

void multipleTwo(int number);  // 函数原型

int main(int argc, char *argv[])
{
    multipleTwo(15); // 调用 multipleTwo 函数，使全局变量 result 的值变为原来的两倍

    printf("15 的两倍是 %d\n", result);  // 我们可以调用变量 result

    return 0;
}

void multipleTwo(int number)
{
    result = 2 * number;
}