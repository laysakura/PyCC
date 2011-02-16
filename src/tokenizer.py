import sys
import re
import common

def _gen_tokens_per_line(line):
    p_int_literal = re.compile("[0-9]+")
    p_id = re.compile("[_a-zA-Z][_a-zA-Z0-9]*")
    p_break = re.compile("break(?![_a-zA-Z0-9])")
    p_continue = re.compile("continue(?![_a-zA-Z0-9])")
    p_else = re.compile("else(?![_a-zA-Z0-9])")
    p_if = re.compile("if(?![_a-zA-Z0-9])")
    p_int = re.compile("int(?![_a-zA-Z0-9])")
    p_return = re.compile("return(?![_a-zA-Z0-9])")
    p_while = re.compile("while(?![_a-zA-Z0-9])")

    unread = line.strip()
    while unread != "":
        # keywords
        if p_break.match(unread):
            unread = unread[len("break"): ].strip()
            yield "break", "TOK_BREAK"
        elif p_continue.match(unread):
            unread = unread[len("continue"): ].strip()
            yield "continue", "TOK_CONTINUE"
        elif p_else.match(unread):
            unread = unread[len("else"): ].strip()
            yield "else", "TOK_ELSE"
        elif p_if.match(unread):
            unread = unread[len("if"): ].strip()
            yield "if", "TOK_IF"
        elif p_int.match(unread):
            unread = unread[len("int"): ].strip()
            yield "int", "TOK_INT"
        elif p_return.match(unread):
            unread = unread[len("return"): ].strip()
            yield "return", "TOK_RETURN"
        elif p_while.match(unread):
            unread = unread[len("while"): ].strip()
            yield "while", "TOK_WHILE"

        # symboles
        elif common.startwith(unread, "("):
            unread = unread[len("("): ].strip()
            yield "(", "TOK_LPAREN"
        elif common.startwith(unread, ")"):
            unread = unread[len(")"): ].strip()
            yield ")", "TOK_RPAREN"
        elif common.startwith(unread, "{"):
            unread = unread[len("{"): ].strip()
            yield "{", "TOK_LBRACE"
        elif common.startwith(unread, "}"):
            unread = unread[len("}"): ].strip()
            yield "}", "TOK_RBRACE"
        elif common.startwith(unread, "*"):
            unread = unread[len("*"): ].strip()
            yield "*", "TOK_MUL"
        elif common.startwith(unread, "+"):
            unread = unread[len("+"): ].strip()
            yield "+", "TOK_PLUS"
        elif common.startwith(unread, "-"):
            unread = unread[len("-"): ].strip()
            yield "-", "TOK_MINUS"
        elif common.startwith(unread, "/"):
            unread = unread[len("/"): ].strip()
            yield "/", "TOK_DIV"
        elif common.startwith(unread, "%"):
            unread = unread[len("%"): ].strip()
            yield "%", "TOK_REM"
        elif common.startwith(unread, "<="):
            unread = unread[len("<="): ].strip()
            yield "<=", "TOK_LE"
        elif common.startwith(unread, ">="):
            unread = unread[len(">="): ].strip()
            yield ">=", "TOK_GE"
        elif common.startwith(unread, "<"):
            unread = unread[len("<"): ].strip()
            yield "<", "TOK_LT"
        elif common.startwith(unread, ">"):
            unread = unread[len(">"): ].strip()
            yield ">", "TOK_GT"
        elif common.startwith(unread, "=="):
            unread = unread[len("=="): ].strip()
            yield "==", "TOK_EQ"
        elif common.startwith(unread, "!="):
            unread = unread[len("!="): ].strip()
            yield "!=", "TOK_NEQ"
        elif common.startwith(unread, "!"):
            unread = unread[len("!"): ].strip()
            yield "!", "TOK_BANG"
        elif common.startwith(unread, ";"):
            unread = unread[len(";"): ].strip()
            yield ";", "TOK_SEMICOLON"
        elif common.startwith(unread, "="):
            unread = unread[len("="): ].strip()
            yield "=", "TOK_ASSIGN"
        elif common.startwith(unread, ","):
            unread = unread[len(","): ].strip()
            yield ",", "TOK_COMMA"

        # int-literal
        elif p_int_literal.match(unread):
            literal = p_int_literal.match(unread).group()
            unread = unread[len(literal): ].strip()
            yield literal, "TOK_INT_LITERAL"

        # id
        elif p_id.match(unread):
            identifier = p_id.match(unread).group()
            unread = unread[len(identifier): ].strip()
            yield identifier, "TOK_ID"

        else:
            yield "INVALID", "INVALID"

def gen_tokenes(lines):
    for linenum, line in enumerate(lines):
        for token, tok_kind in _gen_tokens_per_line(line):
            yield linenum + 1, token, tok_kind

def output_for_test(linenum, token, tok_kind):
    if tok_kind == "TOK_INT_LITERAL" or tok_kind == "TOK_ID":
        print(str(linenum) + ":" + tok_kind + " (" + token + ")")
    else:
        print(str(linenum) + ":" + tok_kind)

if __name__ == "__main__":
    program_lines = [line.strip('\n') for line in sys.stdin]
    for linenum, token, tok_kind in gen_tokenes(program_lines):
        if tok_kind == "INVALID":
            sys.stderr.write("[Tokenize Error] L." + str(linenum) + ": Invalid token.\n")
            exit(1)
        output_for_test(linenum, token, tok_kind)
