#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    //dynamically allocated memory
    if (argc < 1) {return 1;}
    int *numbers = (int *)malloc((argc - 1) * sizeof(int));
    if (numbers == NULL) {
        printf("Malloc failed");
        return 1;
    }

    //Read elements from command line and convert to integers
    for (int i = 1; i < argc; ++i) {numbers[ i - 1] = atoi(argv[i]);}

    //Threshold and print number
    for (int i = 0; i < argc - 1; ++i) {
        if (numbers[i] > 170) {numbers[i] = 255;} 
        else {numbers[i] = 0;}
        printf("%d ", numbers[i]);
    } printf("\n");

    //free dynamically allocated memory
    free(numbers);
    
    return 0;
}