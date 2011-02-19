	.text
.global	f
	.type	f,	@function
f:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$108, %esp
	movl	$0, -4(%ebp)
.L0:
	movl	-4(%ebp), %eax
	cmpl	$10, %eax
	jge	.L1
	movl	-4(%ebp), %eax
	movl	%eax, -4(%ebp)
	addl	$1, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -4(%ebp)
	jmp	.L0
.L1:
	movl	-4(%ebp), %eax
	leave
	ret
	.size	f, .-f
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
