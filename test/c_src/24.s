	.text
.global	f
	.type	f,	@function
f:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$104, %esp
	movl	$52471810, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	imull	$6, %eax
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	$100000000, %ebx
	idivl	%ebx
	movl	%edx, -4(%ebp)
	movl	-4(%ebp), %eax
	leave
	ret
	.size	f, .-f
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
