# Be Quick Or Be Dead 1

You find [https://www.youtube.com/watch?v=CTt1vk9nM9c](https://www.youtube.com/watch?v=CTt1vk9nM9c) when searching for some music, which leads you to the executable in this directory. Can you run it fast enough?

## Solution
The solution to this problem was easy to figure out but I didn't have the right tools to patch the binary. To patch this binary I used [radare2](https://github.com/radareorg/radare2). This binary calculates a `key` which is used to decrypt the flag. However, the application times out before the key reaches the correct value. The algorithm is simple to calcuate the key.

```
int calculate_key() {
  int key = 0;
  do {
    key += 1;
  } while(key != N);
  return key;
```

The solution is to patch the binary by modifying the opcode so that `key = N - 1`. This allows the application to print the flag before the alarm fires and kills the program.


