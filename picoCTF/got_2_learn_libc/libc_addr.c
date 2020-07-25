#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){
  // print the puts libc function address and the system libc function address
  const size_t systemPtr = (size_t) system;
  const size_t putPtr = (size_t) puts;
  const size_t offset = systemPtr - putPtr;
  printf("puts:\t\t0x%x\n", puts);
  printf("system:\t\t0x%x\n", system);
  printf("offset:\t\t%d\n", offset);
  printf("new_ptr:\t0x%x\n", putPtr + offset);
  return 0;
}
