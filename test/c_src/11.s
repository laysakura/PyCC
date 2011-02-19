	.text
.global	f
	.type	f,	@function
f:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$108, %esp
	movl	$888, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	%eax, -8(%ebp)
	cmpl	$0, -8(%ebp)
	sete	%al
	movzbl	%al, %eax
	movl	%eax, -8(%ebp)
	movl	-8(%ebp), %eax
	leave
	ret
	.size	f, .-f
	.ident	"PyCC by @laysakura"
	.section	.note.GNU-stack,"",@progbits
