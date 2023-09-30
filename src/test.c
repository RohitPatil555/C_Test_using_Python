#include <stdio.h>
#include "test.h"
#include "other_module.h"

int test_1(int c)
{
    printf("I am in C %d \n", c);
    my_send(c);
    return c + 1;
}