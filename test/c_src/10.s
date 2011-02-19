	.text
.global	f
	.type	f,	@function
f:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$100, %esp
	call	g
	movl	%eax, %eax
	leave
	ret
	.size	f, .-f
.global	g
	.type	g,	@function
g:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$100, %esp
.L0:
	jmp	.L1
	jmp	.L0
.L1:
	movl	$777, %eax
	leave
	ret
	.size	g, .-g
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
