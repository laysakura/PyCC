from . import tokenizer
from . import common

class Parser:
    def __init__(self, tok_generator):
        self.tok_generator = tok_generator
        self.cur_tok = {"linenum": 0, "token": "", "tok_kind": ""}
        self.next_tok = {"linenum": 0, "token": "", "tok_kind": ""}

    def parse(self):
        self._parse_program()

    def _parse_program(self):
        while self.next_tok["tok_kind"] != "TOK_EOF":
            self._parse_function_definition()

    def _parse_function_definition(self):
        def err_exit():
            common.err_exit("[Parse Error] L." + str(self.cur_tok["linenum"])
                            + "  Invalid function definition.\n")

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_INT":
            err_exit()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_ID":
            err_exit()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_LPAREN":
            err_exit()

        self._parse_parameter_list()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_RPAREN":
            err_exit()

        self._parse_compound_statement()

    def _parse_parameter_list(self):
        if self.next_tok["tok_kind"] == "TOK_RPAREN":
            return

        self._parse_parameter()

        while self.next_tok["tok_kind"] == "TOK_COMMA":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            self._parse_parameter()

        if self.next_tok["tok_kind"] != "TOK_RPAREN":
            return

    def _parse_parameter(self):
        def err_exit():
            common.err_exit("[Parse Error] L." + str(self.cur_tok["linenum"])
                            + "  Invalid argument.\n")

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_INT":
            err_exit()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_ID":
            err_exit()

    def _parse_compound_statement(self):
        def err_exit():
            common.err_exit("[Parse Error] L." + str(self.cur_tok["linenum"])
                            + "  Invalid syntacs.\n")

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_LBRACE":
            err_exit()

        while self.next_tok["tok_kind"] == "TOK_INT":
            self._parse_var_declaration()

        while self.next_tok["tok_kind"] != "TOK_RBRACE":
            self._parse_statement()

        self.cur_tok, self.next_tok = next(self.tok_generator) # self.cur_tok must be '}' here

    def _parse_statement(self):
        def err_exit():
            common.err_exit("[Parse Error] L." + str(self.cur_tok["linenum"])
                            + "  Invalid statement.\n")

        self.cur_tok, self.next_tok = next(self.tok_generator)

        if self.cur_tok["tok_kind"] == "TOK_SEMICOLON":
            return

        elif self.cur_tok["tok_kind"] == "TOK_CONTINUE":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            if self.cur_tok["tok_kind"] != "TOK_SEMICOLON":
                err_exit()
            return

        elif self.cur_tok["tok_kind"] == "TOK_BREAK":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            if self.cur_tok["tok_kind"] != "TOK_SEMICOLON":
                err_exit()
            return

        elif self.cur_tok["tok_kind"] == "TOK_RETURN":
            self._parse_expression()
            self.cur_tok, self.next_tok = next(self.tok_generator)
            if self.cur_tok["tok_kind"] != "TOK_SEMICOLON":
                err_exit()
            return

        elif self.cur_tok["tok_kind"] == "TOK_LBRACE":
            self._parse_compound_statement()
            return

        elif self.cur_tok["tok_kind"] == "TOK_IF":
            self._parse_if_statement()
            return

        elif self.cur_tok["tok_kind"] == "TOK_WHILE":
            self._parse_while_statement()
            return

        else:
            self._parse_expression()
            self.cur_tok, self.next_tok = next(self.tok_generator)
            if self.cur_tok["tok_kind"] != "TOK_SEMICOLON":
                err_exit()
            return

    def _parse_var_declaration(self):
        def err_exit():
            common.err_exit("[Parse Error] L." + str(self.cur_tok["linenum"])
                            + "  Invalid variable definition.\n")

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_INT":
            err_exit()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_ID":
            err_exit()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_SEMICOLON":
            err_exit()

    def _parse_if_statement(self):
        def err_exit():
            common.err_exit("[Parse Error] L." + str(self.cur_tok["linenum"])
                            + "  Invalid syntacs.\n")

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_IF":
            err_exit()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_LPARENXS":
            err_exit()

        self._parse_expression()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_RPAREN":
            err_exit()

        self._parse_statement()

        if self.next_tok["tok_kind"] == "TOK_ELSE":
            self.cur_tok, self.next_tok = next(self.tok_generator) # parse 'else'
            self._parse_statement()

    def _parse_while_statement(self):
        def err_exit():
            common.err_exit("[Parse Error] L." + str(self.cur_tok["linenum"])
                            + "  Invalid syntacs.\n")

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_WHILE":
            err_exit()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_LPARENXS":
            err_exit()

        self._parse_expression()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_RPAREN":
            err_exit()

        self._parse_statement()

    def _parse_expression(self):
        self._parse_equality_expression()

        if self.next_tok["tok_kind"] == "TOK_ASSIGN":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            self._parse_expression()

    def _parse_equality_expression(self):
        self._parse_relational_expression()

        while self.next_tok["tok_kind"] == "TOK_EQ" or self.next_tok["tok_kind"] == "TOK_NEQ":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            self._parse_relational_expression()

    def _parse_relational_expression(self):
        self._parse_additive_expression()

        while self.next_tok["tok_kind"] == "TOK_LT" or self.next_tok["tok_kind"] == "TOK_GT" or self.next_tok["tok_kind"] == "TOK_LE" or self.next_tok["tok_kind"] == "TOK_GE":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            self._parse_additive_expression()

    def _parse_additive_expression(self):
        self._parse_multiplicative_expression()

        while self.next_tok["tok_kind"] == "TOK_PLUS" or self.next_tok["tok_kind"] == "TOK_MINUS":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            self._parse_multiplicative_expression()

    def _parse_multiplicative_expression(self):
        self._parse_unary_expression()

        while self.next_tok["tok_kind"] == "TOK_MUL" or self.next_tok["tok_kind"] == "TOK_DIV" or self.next_tok["tok_kind"] == "TOK_REM":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            self._parse_unary_expression()

    def _parse_unary_expression(self):
        def err_exit():
            common.err_exit("[Parse Error] L." + str(self.cur_tok["linenum"])
                            + "  Invalid syntacs.\n")

        if self.next_tok["tok_kind"] == "TOK_INT_LITERAL":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            return

        elif self.next_tok["tok_kind"] == "TOK_ID":
            self.cur_tok, self.next_tok = next(self.tok_generator)

            if self.next_tok["tok_kind"] == "TOK_LPAREN":
                # function call
                self.cur_tok, self.next_tok = next(self.tok_generator)
                self._parse_argument_expression_list()

                self.cur_tok, self.next_tok = next(self.tok_generator)
                if self.cur_tok["tok_kind"] != "TOK_RPAREN":
                    err_exit()

            return

        elif self.next_tok["tok_kind"] == "TOK_LPAREN":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            self._parse_expression()

            self.cur_tok, self.next_tok = next(self.tok_generator)
            if self.cur_tok["tok_kind"] != "TOK_RPAREN":
                err_exit()

            return

        elif self.next_tok["tok_kind"] == "TOK_PLUS" or self.next_tok["tok_kind"] == "TOK_MINUS" or self.next_tok["tok_kind"] == "TOK_BANG":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            self._parse_unary_expression()

        else:
            err_exit()

    def _parse_argument_expression_list(self):
        if self.next_tok["tok_kind"] == "TOK_RPAREN":
            return

        self._parse_expression()

        while self.next_tok["tok_kind"] == "TOK_COMMA":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            self._parse_expression()


def parse(stdin):
    tok_generator = (lambda : tokenizer.gen_tokens(stdin)) ()
    p = Parser(tok_generator)
    p.parse()
