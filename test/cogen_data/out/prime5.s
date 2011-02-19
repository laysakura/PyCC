	.text
.global	c0func
	.type	c0func,	@function
c0func:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$188, %esp
	movl	$0, -20(%ebp)
	movl	$0, -24(%ebp)
	movl	$0, -28(%ebp)
	movl	$0, -32(%ebp)
	movl	$0, -36(%ebp)
	movl	$2, -4(%ebp)
.L0:
	movl	-4(%ebp), %eax
	cmpl	8(%ebp), %eax
	jge	.L1
	movl	$2, -8(%ebp)
	movl	$0, -12(%ebp)
	movl	$0, -16(%ebp)
.L2:
	movl	-8(%ebp), %eax
	movl	%eax, -40(%ebp)
	movl	-40(%ebp), %eax
	imull	-8(%ebp), %eax
	movl	%eax, -40(%ebp)
	movl	-40(%ebp), %eax
	cmpl	-4(%ebp), %eax
	jg	.L3
	movl	-4(%ebp), %eax
	movl	%eax, -44(%ebp)
	movl	-44(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	-8(%ebp), %ebx
	idivl	%ebx
	movl	%edx, -44(%ebp)
	movl	-44(%ebp), %eax
	cmpl	$0, %eax
	jne	.L4
	movl	$1, -16(%ebp)
	jmp	.L4
.L4:
	movl	-8(%ebp), %eax
	movl	%eax, -48(%ebp)
	addl	$1, -48(%ebp)
	movl	-48(%ebp), %eax
	movl	%eax, -8(%ebp)
	jmp	.L2
.L3:
	movl	-16(%ebp), %eax
	cmpl	$0, %eax
	jne	.L5
	movl	-24(%ebp), %eax
	movl	%eax, -20(%ebp)
	movl	-28(%ebp), %eax
	movl	%eax, -24(%ebp)
	movl	-32(%ebp), %eax
	movl	%eax, -28(%ebp)
	movl	-36(%ebp), %eax
	movl	%eax, -32(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -36(%ebp)
	movl	-20(%ebp), %eax
	movl	%eax, -52(%ebp)
	addl	$2, -52(%ebp)
	movl	-24(%ebp), %eax
	cmpl	-52(%ebp), %eax
	jne	.L6
	movl	-20(%ebp), %eax
	movl	%eax, -56(%ebp)
	addl	$6, -56(%ebp)
	movl	-28(%ebp), %eax
	cmpl	-56(%ebp), %eax
	jne	.L7
	movl	-20(%ebp), %eax
	movl	%eax, -60(%ebp)
	addl	$8, -60(%ebp)
	movl	-32(%ebp), %eax
	cmpl	-60(%ebp), %eax
	jne	.L8
	movl	-20(%ebp), %eax
	movl	%eax, -64(%ebp)
	addl	$12, -64(%ebp)
	movl	-36(%ebp), %eax
	cmpl	-64(%ebp), %eax
	jne	.L9
	movl	-20(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -68(%ebp)
	call	print_space
	movl	%eax, -72(%ebp)
	movl	-24(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -76(%ebp)
	call	print_space
	movl	%eax, -80(%ebp)
	movl	-28(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -84(%ebp)
	call	print_space
	movl	%eax, -88(%ebp)
	movl	-32(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -92(%ebp)
	call	print_space
	movl	%eax, -96(%ebp)
	movl	-36(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -100(%ebp)
	call	print_line
	movl	%eax, -104(%ebp)
.L9:
.L8:
.L7:
.L6:
	movl	-20(%ebp), %eax
	movl	%eax, -108(%ebp)
	addl	$4, -108(%ebp)
	movl	-24(%ebp), %eax
	cmpl	-108(%ebp), %eax
	jne	.L10
	movl	-20(%ebp), %eax
	movl	%eax, -112(%ebp)
	addl	$6, -112(%ebp)
	movl	-28(%ebp), %eax
	cmpl	-112(%ebp), %eax
	jne	.L11
	movl	-20(%ebp), %eax
	movl	%eax, -116(%ebp)
	addl	$10, -116(%ebp)
	movl	-32(%ebp), %eax
	cmpl	-116(%ebp), %eax
	jne	.L12
	movl	-20(%ebp), %eax
	movl	%eax, -120(%ebp)
	addl	$12, -120(%ebp)
	movl	-36(%ebp), %eax
	cmpl	-120(%ebp), %eax
	jne	.L13
	movl	-20(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -124(%ebp)
	call	print_space
	movl	%eax, -128(%ebp)
	movl	-24(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -132(%ebp)
	call	print_space
	movl	%eax, -136(%ebp)
	movl	-28(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -140(%ebp)
	call	print_space
	movl	%eax, -144(%ebp)
	movl	-32(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -148(%ebp)
	call	print_space
	movl	%eax, -152(%ebp)
	movl	-36(%ebp), %eax
	movl	%eax, 0(%esp)
	call	print_int
	movl	%eax, -156(%ebp)
	call	print_line
	movl	%eax, -160(%ebp)
.L13:
.L12:
.L11:
.L10:
.L5:
	movl	-4(%ebp), %eax
	movl	%eax, -164(%ebp)
	addl	$1, -164(%ebp)
	movl	-164(%ebp), %eax
	movl	%eax, -4(%ebp)
	jmp	.L0
.L1:
	.size	c0func, .-c0func
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
