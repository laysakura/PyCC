	.text
.global	f
	.type	f,	@function
f:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$124, %esp
	movl	$1, -4(%ebp)
	movl	$1, -8(%ebp)
	movl	$1, -12(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -16(%ebp)
	movl	-16(%ebp), %eax
	movl	%eax, -16(%ebp)
	movl	-8(%ebp), %eax
	addl	%eax, -16(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -20(%ebp)
	movl	-20(%ebp), %eax
	movl	%eax, -20(%ebp)
	movl	-12(%ebp), %eax
	addl	%eax, -20(%ebp)
	movl	-16(%ebp), %eax
	movl	%eax, -16(%ebp)
	movl	-16(%ebp), %eax
	imull	-20(%ebp), %eax
	movl	%eax, -16(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -24(%ebp)
	movl	-24(%ebp), %eax
	movl	%eax, -24(%ebp)
	movl	-4(%ebp), %eax
	addl	%eax, -24(%ebp)
	movl	-16(%ebp), %eax
	movl	%eax, -16(%ebp)
	movl	-16(%ebp), %eax
	imull	-24(%ebp), %eax
	movl	%eax, -16(%ebp)
	movl	-16(%ebp), %eax
	leave
	ret
	.size	f, .-f
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
