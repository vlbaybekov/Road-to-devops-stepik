#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    while (1) {
        ptr = (int *)malloc(1000000 * sizeof(int));
        if (ptr == NULL) {
            printf("Out of memory!\n");
            break;
        }
    }
    return 0;
}
