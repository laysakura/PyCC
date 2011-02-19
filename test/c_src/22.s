	.text
.global	f
	.type	f,	@function
f:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$112, %esp
	movl	$1, -4(%ebp)
.L0:
	movl	-4(%ebp), %eax
	movl	%eax, -8(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	$3, %ebx
	idivl	%ebx
	movl	%edx, -8(%ebp)
	movl	-8(%ebp), %eax
	cmpl	$0, %eax
	jne	.L2
	movl	-4(%ebp), %eax
	leave
	ret
.L2:
	movl	-4(%ebp), %eax
	movl	%eax, -12(%ebp)
	addl	$1, -12(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -4(%ebp)
	jmp	.L0
.L1:
	.size	f, .-f
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
