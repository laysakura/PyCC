	.text
.global	ack
	.type	ack,	@function
ack:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$128, %esp
	movl	8(%ebp), %eax
	cmpl	$0, %eax
	jne	.L0
	movl	12(%ebp), %eax
	movl	%eax, -4(%ebp)
	addl	$1, -4(%ebp)
	movl	-4(%ebp), %eax
	leave
	ret
.L0:
	movl	12(%ebp), %eax
	cmpl	$0, %eax
	jne	.L1
	movl	8(%ebp), %eax
	movl	%eax, -8(%ebp)
	subl	$1, -8(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, 0(%esp)
	movl	$1, 4(%esp)
	call	ack
	movl	%eax, -12(%ebp)
	movl	-12(%ebp), %eax
	leave
	ret
.L1:
	movl	8(%ebp), %eax
	movl	%eax, -16(%ebp)
	subl	$1, -16(%ebp)
	movl	12(%ebp), %eax
	movl	%eax, -20(%ebp)
	subl	$1, -20(%ebp)
	movl	8(%ebp), %eax
	movl	%eax, 0(%esp)
	movl	-20(%ebp), %eax
	movl	%eax, 4(%esp)
	call	ack
	movl	%eax, -24(%ebp)
	movl	-16(%ebp), %eax
	movl	%eax, 0(%esp)
	movl	-24(%ebp), %eax
	movl	%eax, 4(%esp)
	call	ack
	movl	%eax, -28(%ebp)
	movl	-28(%ebp), %eax
	leave
	ret
	.size	ack, .-ack
.global	c0func
	.type	c0func,	@function
c0func:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$120, %esp
	movl	$0, -4(%ebp)
.L2:
	movl	-4(%ebp), %eax
	cmpl	12(%ebp), %eax
	jge	.L3
	movl	8(%ebp), %eax
	movl	%eax, 0(%esp)
	movl	-4(%ebp), %eax
	movl	%eax, 4(%esp)
	call	ack
	movl	%eax, -8(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -12(%ebp)
	call	print_line
	movl	%eax, -16(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -20(%ebp)
	addl	$1, -20(%ebp)
	movl	-20(%ebp), %eax
	movl	%eax, -4(%ebp)
	jmp	.L2
.L3:
	movl	$0, %eax
	leave
	ret
	.size	c0func, .-c0func
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
