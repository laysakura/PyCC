	.text
.global	f
	.type	f,	@function
f:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$104, %esp
	movl	$23, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	$0, %edx
	movl	$10, %ebx
	idivl	%ebx
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	leave
	ret
	.size	f, .-f
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
