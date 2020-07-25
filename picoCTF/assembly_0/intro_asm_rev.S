.intel_syntax noprefix
//.bits 32
.global asm0

// I figured out what this function is doing by
// following the intructions line-by-line, however I've
// modified this file so that it could compile and run
// with a C program.
// This was a good reference https://www.tutorialspoint.com/assembly_programming/assembly_registers.htm
asm0:
	push	ebp
	mov	ebp,esp
	mov	eax,DWORD PTR [ebp+0x8]
	push	ebx	// Added based on https://stackoverflow.com/a/52675141
	mov	ebx,DWORD PTR [ebp+0xc]
	mov	eax,ebx
	pop	ebx	// Added based on https://stackoverflow.com/a/52675141
	mov	esp,ebp
	pop	ebp	
	ret
