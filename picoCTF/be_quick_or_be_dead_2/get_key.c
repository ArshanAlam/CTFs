#include <stdint.h>
#include <stdio.h>

const int SEED = 1015;

int fib(const int n) {
  int prev = 0;
  int next = 1;

  for (int i = 2; i <= n; i++) {
    int tmp = prev + next;
    prev = next;
    next = tmp;
  }

  return next;
}

int main() {
  printf("%x\n", fib(SEED));
  return 0;
}
