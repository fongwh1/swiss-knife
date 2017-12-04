#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <fcntl.h>
#include <unistd.h>
 
int main(){
  int i = 10;
  int fd = -1;

  srand(time(NULL));

  while(i--) {
      printf("%d\n", rand()%100);
  }

  if (-1 != (fd = open("empty", O_APPEND))) {
      printf("closing fd \"%d\"\n", fd);
      close(fd);
  }

  return 0;
}