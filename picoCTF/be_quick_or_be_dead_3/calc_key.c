#include <stdio.h>


/**
 * This is the pseudocode for the calc function in the binary:
 *
 *    def calc(x):
 *      if x > 4:
 *        x1 = calc(x - 1)
 *        x2 = calc(x - 2)
 *        
 *        y1 = x1 - x2
 *
 *        x3 = calc(x - 3)
 *        x4 = calc(x - 4)
 *
 *        y2 = x3 - x4
 *
 *        y3 = y1 + y2
 *
 *        x5 = calc(x - 5) * 0x1234
 *
 *        return y3 + x5
 *      else:
 *        return (x * x) + 0x2345
 *
 *
 * The calc function below is optimized using DP to get the result faster.
 */
int calc(int x) {
  if (x <= 4) {
    return (x * x) + 0x2345;
  }
  
  int x0 = (0 * 0) + 0x2345;
  int x1 = (1 * 1) + 0x2345;
  int x2 = (2 * 2) + 0x2345;
  int x3 = (3 * 3) + 0x2345;
  int x4 = (4 * 4) + 0x2345;
  
  for (int i = 5; i <= x; i++) {
    int y1 = x4 - x3;
    int y2 = x2 - x1;
    int y3 = y1 + y2;
    int y4 = x0 * 0x1234;
    int next = y3 + y4;

    // shift all for next iteration
    x0 = x1;
    x1 = x2;
    x2 = x3;
    x3 = x4;
    x4 = next;
  }

  return x4;
}


int main() {
  printf("%x\n", calc(0x18f4b));
  return 0;
}
