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
            yield {"token": "break", "tok_kind": "TOK_BREAK"}
        elif p_continue.match(unread):
            unread = unread[len("continue"): ].strip()
            yield {"token": "continue", "tok_kind": "TOK_CONTINUE"}
        elif p_else.match(unread):
            unread = unread[len("else"): ].strip()
            yield {"token": "else", "tok_kind": "TOK_ELSE"}
        elif p_if.match(unread):
            unread = unread[len("if"): ].strip()
            yield {"token": "if", "tok_kind": "TOK_IF"}
        elif p_int.match(unread):
            unread = unread[len("int"): ].strip()
            yield {"token": "int", "tok_kind": "TOK_INT"}
        elif p_return.match(unread):
            unread = unread[len("return"): ].strip()
            yield {"token": "return", "tok_kind": "TOK_RETURN"}
        elif p_while.match(unread):
            unread = unread[len("while"): ].strip()
            yield {"token": "while", "tok_kind": "TOK_WHILE"}

        # symboles
        elif common.startwith(unread, "("):
            unread = unread[len("("): ].strip()
            yield {"token": "(", "tok_kind": "TOK_LPAREN"}
        elif common.startwith(unread, ")"):
            unread = unread[len(")"): ].strip()
            yield {"token": ")", "tok_kind": "TOK_RPAREN"}
        elif common.startwith(unread, "{"):
            unread = unread[len("{"): ].strip()
            yield {"token": "{", "tok_kind": "TOK_LBRACE"}
        elif common.startwith(unread, "}"):
            unread = unread[len("}"): ].strip()
            yield {"token": "}", "tok_kind": "TOK_RBRACE"}
        elif common.startwith(unread, "*"):
            unread = unread[len("*"): ].strip()
            yield {"token": "*", "tok_kind": "TOK_MUL"}
        elif common.startwith(unread, "+"):
            unread = unread[len("+"): ].strip()
            yield {"token": "+", "tok_kind": "TOK_PLUS"}
        elif common.startwith(unread, "-"):
            unread = unread[len("-"): ].strip()
            yield {"token": "-", "tok_kind": "TOK_MINUS"}
        elif common.startwith(unread, "/"):
            unread = unread[len("/"): ].strip()
            yield {"token": "/", "tok_kind": "TOK_DIV"}
        elif common.startwith(unread, "%"):
            unread = unread[len("%"): ].strip()
            yield {"token": "%", "tok_kind": "TOK_REM"}
        elif common.startwith(unread, "<="):
            unread = unread[len("<="): ].strip()
            yield {"token": "<=", "tok_kind": "TOK_LE"}
        elif common.startwith(unread, ">="):
            unread = unread[len(">="): ].strip()
            yield {"token": ">=", "tok_kind": "TOK_GE"}
        elif common.startwith(unread, "<"):
            unread = unread[len("<"): ].strip()
            yield {"token": "<", "tok_kind": "TOK_LT"}
        elif common.startwith(unread, ">"):
            unread = unread[len(">"): ].strip()
            yield {"token": ">", "tok_kind": "TOK_GT"}
        elif common.startwith(unread, "=="):
            unread = unread[len("=="): ].strip()
            yield {"token": "==", "tok_kind": "TOK_EQ"}
        elif common.startwith(unread, "!="):
            unread = unread[len("!="): ].strip()
            yield {"token": "!=", "tok_kind": "TOK_NEQ"}
        elif common.startwith(unread, "!"):
            unread = unread[len("!"): ].strip()
            yield {"token": "!", "tok_kind": "TOK_BANG"}
        elif common.startwith(unread, ";"):
            unread = unread[len(";"): ].strip()
            yield {"token": ";", "tok_kind": "TOK_SEMICOLON"}
        elif common.startwith(unread, "="):
            unread = unread[len("="): ].strip()
            yield {"token": "=", "tok_kind": "TOK_ASSIGN"}
        elif common.startwith(unread, ","):
            unread = unread[len(","): ].strip()
            yield {"token": ",", "tok_kind": "TOK_COMMA"}

        # int-literal
        elif p_int_literal.match(unread):
            literal = p_int_literal.match(unread).group()
            unread = unread[len(literal): ].strip()
            yield {"token": literal, "tok_kind": "TOK_INT_LITERAL"}

        # id
        elif p_id.match(unread):
            identifier = p_id.match(unread).group()
            unread = unread[len(identifier): ].strip()
            yield {"token": identifier, "tok_kind": "TOK_ID"}

        else:
            yield {"token": "INVALID", "tok_kind": "INVALID"}

def gen_tokens(stdin):
    cur = {}
    for linenum, line in enumerate(stdin):
        for next in _gen_tokens_per_line(line):
            if next["tok_kind"] == "INVALID":
                common.err_exit("[Tokenize Error] L." + str(linenum) + ": Invalid token.\n")
            next["linenum"] = linenum + 1

            if cur == {}:
                # get just first token
                cur = next
                continue

            yield cur, next
            cur = next

    # no tokens left
    yield cur, {"linenum": -1, "token": "[EOF]", "tok_kind": "TOK_EOF"}
