	.text
.global	get_random
	.type	get_random,	@function
get_random:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$104, %esp
	movl	8(%ebp), %eax
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	imull	$1103515245, %eax
	movl	%eax, -4(%ebp)
	addl	$12345, -4(%ebp)
	movl	-4(%ebp), %eax
	leave
	ret
	.size	get_random, .-get_random
.global	c0func
	.type	c0func,	@function
c0func:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$212, %esp
	movl	$0, -4(%ebp)
	movl	16(%ebp), %eax
	movl	%eax, -8(%ebp)
	movl	$0, -12(%ebp)
.L0:
	movl	-4(%ebp), %eax
	cmpl	8(%ebp), %eax
	jge	.L1
	movl	-8(%ebp), %eax
	movl	%eax, 0(%esp)
	call	get_random
	movl	%eax, -28(%ebp)
	movl	-28(%ebp), %eax
	movl	%eax, -8(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -32(%ebp)
	movl	-32(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	12(%ebp), %ebx
	idivl	%ebx
	movl	%edx, -32(%ebp)
	movl	-32(%ebp), %eax
	movl	%eax, -16(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, 0(%esp)
	call	get_random
	movl	%eax, -36(%ebp)
	movl	-36(%ebp), %eax
	movl	%eax, -8(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -40(%ebp)
	movl	-40(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	12(%ebp), %ebx
	idivl	%ebx
	movl	%edx, -40(%ebp)
	movl	-40(%ebp), %eax
	movl	%eax, -20(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, 0(%esp)
	call	get_random
	movl	%eax, -44(%ebp)
	movl	-44(%ebp), %eax
	movl	%eax, -8(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -48(%ebp)
	movl	-48(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	12(%ebp), %ebx
	idivl	%ebx
	movl	%edx, -48(%ebp)
	movl	-48(%ebp), %eax
	movl	%eax, -24(%ebp)
	movl	-16(%ebp), %eax
	movl	%eax, -52(%ebp)
	movl	-52(%ebp), %eax
	imull	-16(%ebp), %eax
	movl	%eax, -52(%ebp)
	movl	-20(%ebp), %eax
	movl	%eax, -56(%ebp)
	movl	-56(%ebp), %eax
	imull	-20(%ebp), %eax
	movl	%eax, -56(%ebp)
	movl	-56(%ebp), %eax
	addl	%eax, -52(%ebp)
	movl	-24(%ebp), %eax
	movl	%eax, -60(%ebp)
	movl	-60(%ebp), %eax
	imull	-24(%ebp), %eax
	movl	%eax, -60(%ebp)
	movl	-60(%ebp), %eax
	addl	%eax, -52(%ebp)
	movl	12(%ebp), %eax
	movl	%eax, -64(%ebp)
	movl	-64(%ebp), %eax
	imull	12(%ebp), %eax
	movl	%eax, -64(%ebp)
	movl	-52(%ebp), %eax
	cmpl	-64(%ebp), %eax
	jg	.L2
	movl	-12(%ebp), %eax
	movl	%eax, -68(%ebp)
	addl	$1, -68(%ebp)
	movl	-68(%ebp), %eax
	movl	%eax, -12(%ebp)
.L2:
	movl	-4(%ebp), %eax
	movl	%eax, -72(%ebp)
	addl	$1, -72(%ebp)
	movl	-72(%ebp), %eax
	movl	%eax, -4(%ebp)
	jmp	.L0
.L1:
	movl	8(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -76(%ebp)
	call	print_line
	movl	%eax, -80(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -84(%ebp)
	call	print_line
	movl	%eax, -88(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -92(%ebp)
	movl	-92(%ebp), %eax
	imull	$6, %eax
	movl	%eax, -92(%ebp)
	movl	-92(%ebp), %eax
	movl	$0, %edx
	movl	8(%ebp), %ebx
	idivl	%ebx
	movl	%eax, -92(%ebp)
	movl	-92(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -96(%ebp)
	movl	$46, 0(%esp)
	call	print_char
	movl	%eax, -100(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -104(%ebp)
	movl	-104(%ebp), %eax
	imull	$6, %eax
	movl	%eax, -104(%ebp)
	movl	-104(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	8(%ebp), %ebx
	idivl	%ebx
	movl	%edx, -104(%ebp)
	movl	-104(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -108(%ebp)
	call	print_line
	movl	%eax, -112(%ebp)
	movl	$0, %eax
	leave
	ret
	.size	c0func, .-c0func
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
