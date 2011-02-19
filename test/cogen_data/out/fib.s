	.text
.global	fib
	.type	fib,	@function
fib:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$116, %esp
	movl	8(%ebp), %eax
	cmpl	$2, %eax
	jge	.L0
	movl	$1, %eax
	leave
	ret
	jmp	.L1
.L0:
	movl	8(%ebp), %eax
	movl	%eax, -4(%ebp)
	subl	$1, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, 0(%esp)
	call	fib
	movl	%eax, -8(%ebp)
	movl	8(%ebp), %eax
	movl	%eax, -12(%ebp)
	subl	$2, -12(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, 0(%esp)
	call	fib
	movl	%eax, -16(%ebp)
	movl	-16(%ebp), %eax
	addl	%eax, -8(%ebp)
	movl	-8(%ebp), %eax
	leave
	ret
.L1:
	.size	fib, .-fib
.global	c0func
	.type	c0func,	@function
c0func:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$112, %esp
	movl	8(%ebp), %eax
	movl	%eax, 0(%esp)
	call	fib
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -8(%ebp)
	call	print_line
	movl	%eax, -12(%ebp)
	movl	$0, %eax
	leave
	ret
	.size	c0func, .-c0func
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
