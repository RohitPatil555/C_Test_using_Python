#include <stdio.h>
#include <test.h>
#include "other_module.h"

int test_2(int x, int y)
{
    int z;
    printf("In test 2\n");
    z = my_env_get("foo");
    return x + y + z;
}