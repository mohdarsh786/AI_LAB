// #include<stdio.h>
// #include<unistd.h>
// int main()
// {
//     fork();
//     fork();
//     fork();
//     printf("Linux\n");
//     return 0;
// }
#include<stdio.h>
#include<unistd.h>
int main()
{
    fork();
    fork();
    fork();
    printf("Linux\n");
    return 0;
}

//write a structure of 4 system calls in a n times.
/*
#include <stdio.h>
#include <unistd.h>
void main() 
{
    int n = 4;
    for (int i = 0; i < n; i++) {
        printf("\nIteration %d:\n", i+1);
        printf("Process ID: %d\n", getpid());
        pid_t pid = fork();
        printf("Fork called. PID: %d\n", pid);
        printf("Parent Process ID: %d\n", getppid());
    }
}
*/