	.text
.global	f
	.type	f,	@function
f:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$108, %esp
	movl	$10000001, -4(%ebp)
.L0:
	movl	$3, -8(%ebp)
	movl	-8(%ebp), %eax
	imull	$3, %eax
	movl	%eax, -8(%ebp)
	movl	-8(%ebp), %eax
	cmpl	-4(%ebp), , %eax
	jg	.L1
	movl	$0, %eax
	leave
	ret
	jmp	.L0
.L1:
	movl	$333, %eax
	leave
	ret
	.size	f, .-f
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
