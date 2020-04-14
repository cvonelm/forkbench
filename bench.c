#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    pid_t pid = fork();
    if(!pid)
    {
        printf("Starting: test{{next_num}}\n");
        //sleep(10);
        char * const argv[] = {"test{{next_num}}",NULL};
        char * const envp[] = {NULL};
        execve("{{base}}test{{next_num}}", argv, envp);
        exit(0);
    }
    wait(NULL);
    printf("child test{{next_num}} died!\n");
    sleep(10);
    return 0;
}
