	.text
.global	f
	.type	f,	@function
f:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$112, %esp
	movl	$23, -4(%ebp)
	movl	$5, -8(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -12(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	-8(%ebp), %ebx
	idivl	%ebx
	movl	%edx, -12(%ebp)
	movl	-12(%ebp), %eax
	leave
	ret
	.size	f, .-f
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
