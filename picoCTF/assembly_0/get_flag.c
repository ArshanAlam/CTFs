#include <stdio.h>
int asm0(int, int);
int main() {
	int result = asm0(0xd8,0x7a);
	printf("0x%x\n", result);
	return 0;
}
