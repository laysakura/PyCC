	.file	"test/intapp_tests/fib.c"
	.text
.L0:
.global fib
	.type	fib,	@function
fib:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$44, %esp
	movl	$2, %eax
	cmpl	%eax, 8(%ebp)
	jge	.L5
	movl	$1, %eax
	leave
	ret
.L5:
	movl	8(%ebp), %eax
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	subl	$1, %eax
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, 0(%esp)
.L7:
	call	fib
	movl	%eax, -8(%ebp)
	movl	8(%ebp), %eax
	movl	%eax, -12(%ebp)
	movl	-12(%ebp), %eax
	subl	$2, %eax
	movl	%eax, -12(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, 0(%esp)
.L8:
	call	fib
	movl	%eax, -16(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -20(%ebp)
	movl	-20(%ebp), %eax
	addl	-16(%ebp), %eax
	movl	%eax, -20(%ebp)
	movl	-20(%ebp), %eax
	leave
	ret
.L9:
	.size	fib,	.-fib
.L11:
.global c0func
	.type	c0func,	@function
c0func:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$36, %esp
.L12:
	movl	8(%ebp), %eax
	movl	%eax, 0(%esp)
.L13:
	call	fib
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, 0(%esp)
.L14:
	call	print_int
	movl	%eax, -8(%ebp)
.L15:
	call	print_line
	movl	%eax, -12(%ebp)
	movl	$0, %eax
	leave
	ret
.L16:
	.size	c0func,	.-c0func
	.ident	"SHOCC 1.0.0"
	.section	.note.GNU-stack,"",@progbits
