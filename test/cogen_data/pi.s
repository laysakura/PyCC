	.text
.global	get_random
	.type	get_random,	@function
get_random:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$108, %esp
	movl	8(%ebp), %eax
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	imull	$1103515245, %eax
	movl	%eax, -4(%ebp)
	movl	$12345, -8(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -4(%ebp)
	movl	-8(%ebp), %eax
	addl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	leave
	ret
	.size	get_random, .-get_random
.global	c0func
	.type	c0func,	@function
c0func:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$312, %esp
	movl	-4(%ebp), %eax
	movl	%eax, -28(%ebp)
	movl	$0, -32(%ebp)
	movl	-32(%ebp), %eax
	movl	%eax, -28(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -36(%ebp)
	movl	16(%ebp), %eax
	movl	%eax, -40(%ebp)
	movl	-40(%ebp), %eax
	movl	%eax, -36(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -44(%ebp)
	movl	$0, -48(%ebp)
	movl	-48(%ebp), %eax
	movl	%eax, -44(%ebp)
.L0:
	movl	-4(%ebp), %eax
	movl	%eax, -52(%ebp)
	movl	8(%ebp), %eax
	movl	%eax, -56(%ebp)
	movl	-52(%ebp), %eax
	cmpl	-56(%ebp), %eax
	jge	.L1
	movl	-8(%ebp), %eax
	movl	%eax, -60(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -64(%ebp)
	movl	-64(%ebp), %eax
	movl	%eax, 0(%esp)
	call	get_random
	movl	%eax, -68(%ebp)
	movl	-68(%ebp), %eax
	movl	%eax, -60(%ebp)
	movl	-16(%ebp), %eax
	movl	%eax, -72(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -76(%ebp)
	movl	-76(%ebp), %eax
	movl	%eax, -76(%ebp)
	movl	-76(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	12(%ebp), %ebx
	idivl	%ebx
	movl	%edx, -76(%ebp)
	movl	-76(%ebp), %eax
	movl	%eax, -72(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -80(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -84(%ebp)
	movl	-84(%ebp), %eax
	movl	%eax, 0(%esp)
	call	get_random
	movl	%eax, -88(%ebp)
	movl	-88(%ebp), %eax
	movl	%eax, -80(%ebp)
	movl	-20(%ebp), %eax
	movl	%eax, -92(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -96(%ebp)
	movl	-96(%ebp), %eax
	movl	%eax, -96(%ebp)
	movl	-96(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	12(%ebp), %ebx
	idivl	%ebx
	movl	%edx, -96(%ebp)
	movl	-96(%ebp), %eax
	movl	%eax, -92(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -100(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -104(%ebp)
	movl	-104(%ebp), %eax
	movl	%eax, 0(%esp)
	call	get_random
	movl	%eax, -108(%ebp)
	movl	-108(%ebp), %eax
	movl	%eax, -100(%ebp)
	movl	-24(%ebp), %eax
	movl	%eax, -112(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -116(%ebp)
	movl	-116(%ebp), %eax
	movl	%eax, -116(%ebp)
	movl	-116(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	12(%ebp), %ebx
	idivl	%ebx
	movl	%edx, -116(%ebp)
	movl	-116(%ebp), %eax
	movl	%eax, -112(%ebp)
	movl	-16(%ebp), %eax
	movl	%eax, -120(%ebp)
	movl	-120(%ebp), %eax
	movl	%eax, -120(%ebp)
	movl	-120(%ebp), %eax
	imull	-16(%ebp), %eax
	movl	%eax, -120(%ebp)
	movl	-20(%ebp), %eax
	movl	%eax, -124(%ebp)
	movl	-124(%ebp), %eax
	movl	%eax, -124(%ebp)
	movl	-124(%ebp), %eax
	imull	-20(%ebp), %eax
	movl	%eax, -124(%ebp)
	movl	-120(%ebp), %eax
	movl	%eax, -120(%ebp)
	movl	-124(%ebp), %eax
	addl	%eax, -120(%ebp)
	movl	-24(%ebp), %eax
	movl	%eax, -128(%ebp)
	movl	-128(%ebp), %eax
	movl	%eax, -128(%ebp)
	movl	-128(%ebp), %eax
	imull	-24(%ebp), %eax
	movl	%eax, -128(%ebp)
	movl	-120(%ebp), %eax
	movl	%eax, -120(%ebp)
	movl	-128(%ebp), %eax
	addl	%eax, -120(%ebp)
	movl	12(%ebp), %eax
	movl	%eax, -132(%ebp)
	movl	-132(%ebp), %eax
	movl	%eax, -132(%ebp)
	movl	-132(%ebp), %eax
	imull	12(%ebp), %eax
	movl	%eax, -132(%ebp)
	movl	-120(%ebp), %eax
	cmpl	-132(%ebp), %eax
	jg	.L2
	movl	-12(%ebp), %eax
	movl	%eax, -136(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -140(%ebp)
	movl	$1, -144(%ebp)
	movl	-140(%ebp), %eax
	movl	%eax, -140(%ebp)
	movl	-144(%ebp), %eax
	addl	%eax, -140(%ebp)
	movl	-140(%ebp), %eax
	movl	%eax, -136(%ebp)
.L2:
	movl	-4(%ebp), %eax
	movl	%eax, -148(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -152(%ebp)
	movl	$1, -156(%ebp)
	movl	-152(%ebp), %eax
	movl	%eax, -152(%ebp)
	movl	-156(%ebp), %eax
	addl	%eax, -152(%ebp)
	movl	-152(%ebp), %eax
	movl	%eax, -148(%ebp)
	jmp	.L0
.L1:
	movl	8(%ebp), %eax
	movl	%eax, -160(%ebp)
	movl	-160(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -164(%ebp)
	call	print_line
	movl	%eax, -168(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -172(%ebp)
	movl	-172(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -176(%ebp)
	call	print_line
	movl	%eax, -180(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -184(%ebp)
	movl	-184(%ebp), %eax
	movl	%eax, -184(%ebp)
	movl	-184(%ebp), %eax
	imull	$6, %eax
	movl	%eax, -184(%ebp)
	movl	-184(%ebp), %eax
	movl	%eax, -184(%ebp)
	movl	-184(%ebp), %eax
	movl	$0, %edx
	movl	8(%ebp), %ebx
	idivl	%ebx
	movl	%eax, -184(%ebp)
	movl	-184(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -188(%ebp)
	movl	$46, -192(%ebp)
	movl	-192(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_char
	movl	%eax, -196(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -200(%ebp)
	movl	-200(%ebp), %eax
	movl	%eax, -200(%ebp)
	movl	-200(%ebp), %eax
	imull	$6, %eax
	movl	%eax, -200(%ebp)
	movl	-200(%ebp), %eax
	movl	%eax, -200(%ebp)
	movl	-200(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	8(%ebp), %ebx
	idivl	%ebx
	movl	%edx, -200(%ebp)
	movl	-200(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -204(%ebp)
	call	print_line
	movl	%eax, -208(%ebp)
	movl	$0, -212(%ebp)
	movl	-212(%ebp), %eax
	leave
	ret
	.size	c0func, .-c0func
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
