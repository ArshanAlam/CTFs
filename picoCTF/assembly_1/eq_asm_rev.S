.intel_syntax noprefix
.bits 32
	
.global asm1

# asm1(0x15e) == asm1(350)
asm1:
  # [ebp+0x40]
	push	ebp
	mov	ebp,esp
  # compare 350 with 220
	cmp	DWORD PTR [ebp+0x8],0xdc
  # since 350 > 220, we jump to part_a
	jg 	part_a
	cmp	DWORD PTR [ebp+0x8],0x8
	jne	part_b
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
  # compare 350 with 104
	cmp	DWORD PTR [ebp+0x8],0x68
  # since 350 != 104 23 jump to part_c
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
	cmp	DWORD PTR [ebp+0x8],0xfc
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
  # we move 350 into eax
	mov	eax,DWORD PTR [ebp+0x8]
  # we add 3 to eax to get 353 in decimal
	add	eax,0x3
part_d:
	pop	ebp
  # therefore the result is 353 in decimal or 0x161 in hex
	ret
