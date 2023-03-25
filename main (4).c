#include <stdio.h>

int main(void) {
int n, i, j,aux=0;
  scanf("%d", &n);
  for (i=1;i<=n;i++){
    for(j=1;j<=i;j++){
      aux++;
      printf("%d ", aux);
    }
    printf("\n");
  }
  return 0;
}