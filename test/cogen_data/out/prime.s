	.text
.global	check_prime
	.type	check_prime,	@function
check_prime:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$116, %esp
	movl	$2, -4(%ebp)
.L0:
	movl	-4(%ebp), %eax
	movl	%eax, -8(%ebp)
	movl	-8(%ebp), %eax
	movl	%eax, -8(%ebp)
	movl	-8(%ebp), %eax
	imull	-4(%ebp), %eax
	movl	%eax, -8(%ebp)
	movl	-8(%ebp), %eax
	cmpl	8(%ebp), %eax
	jg	.L1
	movl	8(%ebp), %eax
	movl	%eax, -12(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -12(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	movl	-4(%ebp), %ebx
	idivl	%ebx
	movl	%edx, -12(%ebp)
	movl	-12(%ebp), %eax
	cmpl	$0, %eax
	jne	.L2
	movl	$0, %eax
	leave
	ret
.L2:
	movl	-4(%ebp), %eax
	movl	%eax, -16(%ebp)
	movl	-16(%ebp), %eax
	movl	%eax, -16(%ebp)
	addl	$1, -16(%ebp)
	movl	-16(%ebp), %eax
	movl	%eax, -4(%ebp)
	jmp	.L0
.L1:
	movl	$1, %eax
	leave
	ret
	.size	check_prime, .-check_prime
.global	count_primes
	.type	count_primes,	@function
count_primes:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$120, %esp
	movl	$2, -4(%ebp)
	movl	$0, -8(%ebp)
.L3:
	movl	-4(%ebp), %eax
	cmpl	8(%ebp), %eax
	jge	.L4
	movl	-8(%ebp), %eax
	movl	%eax, -12(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, 0(%esp)
	call	check_prime
	movl	%eax, -16(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -12(%ebp)
	movl	-16(%ebp), %eax
	addl	%eax, -12(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -8(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -20(%ebp)
	movl	-20(%ebp), %eax
	movl	%eax, -20(%ebp)
	addl	$1, -20(%ebp)
	movl	-20(%ebp), %eax
	movl	%eax, -4(%ebp)
	jmp	.L3
.L4:
	movl	-8(%ebp), %eax
	leave
	ret
	.size	count_primes, .-count_primes
.global	c0func
	.type	c0func,	@function
c0func:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$112, %esp
	movl	8(%ebp), %eax
	movl	%eax, 0(%esp)
	call	count_primes
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
