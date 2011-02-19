	.text
.global	f
	.type	f,	@function
f:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$100, %esp
	movl	$0, 0(%esp)
	movl	$333, 4(%esp)
	call	e
	movl	%eax, %eax
	leave
	ret
	.size	f, .-f
.global	g
	.type	g,	@function
g:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$104, %esp
	movl	8(%ebp), %eax
	movl	%eax, -4(%ebp)
	negl	-4(%ebp)
	movl	-4(%ebp), %eax
	leave
	ret
	.size	g, .-g
.global	e
	.type	e,	@function
e:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$104, %esp
	cmpl	$0, 8(%ebp)
	je	.L0
	movl	$777, %eax
	leave
	ret
	jmp	.L1
.L0:
	movl	12(%ebp), %eax
	movl	%eax, 0(%esp)
	call	g
	movl	%eax, %eax
	leave
	ret
.L1:
	.size	e, .-e
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
