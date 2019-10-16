#include <stdio.h>


int main(void) {
  int n;
  scanf("%d", &n);

  int sum = 0;
  while (n > 9) {
    int remainder = n % 10;
    sum += remainder;
    n = (n - remainder) / 10;
  }

  if (n != 0) {
    sum += n;
  }

  printf("%d\n", sum);

  return 0;
}
      
  
