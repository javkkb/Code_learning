#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main (int argc, char** argv)
{
    int mysteryNumber = 0, guessNumber = 0;
    const int MAX = 100, MIN = 1;
    // 生成随机数
    srand(time(NULL));
    mysteryNumber = (rand() % (MAX - MIN + 1)) + MIN;
    /* 程序的循环部分， 如果用户没猜中数字，就一直进行循环 */
    do
    {
        // 请求用户输入所猜数字
        printf("这个数字是什么 ? ");
        scanf("%d", &guessNumber);
        // 比较用户输入的数字和神秘数字
        if (mysteryNumber > guessNumber)
            printf("猜小了 !\n\n");
        else if (mysteryNumber < guessNumber)
            printf("猜大了 !\n\n");
        else
            printf ("太棒了，你猜到了这个神秘数字 !!\n\n");
    } while (guessNumber != mysteryNumber);

    return 0;
}
/*
*****************
作者：程序员联盟
链接：https://juejin.im/post/5ecdbe4ee51d45788d1cb890
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*****************
*/