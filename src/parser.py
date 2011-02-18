from . import tokenizer
from . import common
from . import scope

class Parser:
    def __init__(self, tok_generator):
        self.tok_generator = tok_generator
        self.cur_tok = {"linenum": 0, "token": "", "tok_kind": ""}
        self.next_tok = {"linenum": 0, "token": "", "tok_kind": ""}

        self.tmpvar_generator = (lambda : self._gen_unique_token(".t", "TOK_TMPVAR"))()
        self.label_generator = (lambda : self._gen_unique_token(".L", "TOK_LABEL"))()

        self.last_test_label = {"linenum": -1, "token": "", "tok_kind": "TOK_LABEL"}
        self.last_false_label = {"linenum": -1, "token": "", "tok_kind": "TOK_LABEL"}

        self.intcode = []

        self.scope = scope.Scope()

    def _gen_unique_token(self, prefix, tok_kind):
        n = 0
        while True:
            yield {"linenum": -1, "token": prefix + str(n), "tok_kind": tok_kind}
            n += 1

    def parse(self):
        self._parse_program()
        return self.intcode

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

        self.scope.scopein()

        while self.next_tok["tok_kind"] == "TOK_INT":
            self._parse_var_declaration()

        while self.next_tok["tok_kind"] != "TOK_RBRACE":
            self._parse_statement()

        self.scope.scopeout()

        self.cur_tok, self.next_tok = next(self.tok_generator) # self.cur_tok must be '}' here

    def _parse_statement(self):
        def err_exit():
            common.err_exit("[Parse Error] L." + str(self.cur_tok["linenum"])
                            + "  Invalid statement.\n")

        if self.next_tok["tok_kind"] == "TOK_SEMICOLON":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            return

        elif self.next_tok["tok_kind"] == "TOK_CONTINUE":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            self.cur_tok, self.next_tok = next(self.tok_generator)
            if self.cur_tok["tok_kind"] != "TOK_SEMICOLON":
                err_exit()
            self.intcode.append({"scope": self.scope.curid(), "label": "", "code": "goto " + self.last_test_label["token"]})
            return

        elif self.next_tok["tok_kind"] == "TOK_BREAK":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            self.cur_tok, self.next_tok = next(self.tok_generator)
            if self.cur_tok["tok_kind"] != "TOK_SEMICOLON":
                err_exit()
            self.intcode.append({"scope": self.scope.curid(), "label": "", "code": "goto " + self.last_false_label["token"]})
            return

        elif self.next_tok["tok_kind"] == "TOK_RETURN":
            self.cur_tok, self.next_tok = next(self.tok_generator)

            equality = self._parse_equality()

            self.cur_tok, self.next_tok = next(self.tok_generator)
            if self.cur_tok["tok_kind"] != "TOK_SEMICOLON":
                err_exit()

            self.intcode.append({"scope": self.scope.curid(), "label": "", "code": "return " + equality["token"]})
            return

        elif self.next_tok["tok_kind"] == "TOK_LBRACE":
            self._parse_compound_statement()
            return

        elif self.next_tok["tok_kind"] == "TOK_IF":
            self._parse_if_statement()
            return

        elif self.next_tok["tok_kind"] == "TOK_WHILE":
            self._parse_while_statement()
            return

        else:
            code = self._parse_equality()["token"]
            self.cur_tok, self.next_tok = next(self.tok_generator)
            if self.cur_tok["tok_kind"] != "TOK_SEMICOLON":
                err_exit()

            self.intcode.append({"scope": self.scope.curid(), "label": "", "code": code})
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
        if self.cur_tok["tok_kind"] != "TOK_LPAREN":
            err_exit()

        test = self._parse_equality()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_RPAREN":
            err_exit()

        false_label = next(self.label_generator)
        self.last_false_label = false_label
        self.intcode.append({"scope": self.scope.curid(), "label": "", "code": "if_false " + test["token"] + " goto " + false_label["token"]})

        self._parse_statement()

        if self.next_tok["tok_kind"] == "TOK_ELSE":
            fi_label = next(self.label_generator)
            self.intcode.append({"scope": self.scope.curid(), "label": "", "code": "goto " + fi_label["token"]})
            self.intcode.append({"scope": self.scope.curid(), "label": false_label["token"], "code": ""})

            self.cur_tok, self.next_tok = next(self.tok_generator) # parse 'else'

            self._parse_statement()

            self.intcode.append({"scope": self.scope.curid(), "label": fi_label["token"], "code": ""})

        else:
            self.intcode.append({"scope": self.scope.curid(), "label": false_label["token"], "code": ""})

    def _parse_while_statement(self):
        def err_exit():
            common.err_exit("[Parse Error] L." + str(self.cur_tok["linenum"])
                            + "  Invalid syntacs.\n")

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_WHILE":
            err_exit()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_LPAREN":
            err_exit()

        test = self._parse_equality()

        self.cur_tok, self.next_tok = next(self.tok_generator)
        if self.cur_tok["tok_kind"] != "TOK_RPAREN":
            err_exit()

        test_label = next(self.label_generator)
        false_label = next(self.label_generator)
        self.last_false_label = false_label
        self.last_test_label = test_label
        self.intcode.append({"scope": self.scope.curid(), "label": test_label["token"], "code": ""})
        self.intcode.append({"scope": self.scope.curid(), "label": "", "code": "if_false " + test["token"] + " goto " + false_label["token"]})

        self._parse_statement()

        self.intcode.append({"scope": self.scope.curid(), "label": "", "code": "goto " + test_label["token"]})
        self.intcode.append({"scope": self.scope.curid(), "label": false_label["token"], "code": ""})

    def _parse_equality(self):
        l_rel = self._parse_rel()

        if self.next_tok["tok_kind"] == "TOK_EQ" or self.next_tok["tok_kind"] == "TOK_NEQ":
            # rel (==|!=) rel
            self.cur_tok, self.next_tok = next(self.tok_generator)
            op = self.cur_tok["token"]
            r_rel = self._parse_rel()
            return {"linenum": -1, "token": l_rel["token"] + ' ' + op + ' ' + r_rel["token"], "tok_kind": "TOK_TEST"}

        else:
            # single rel
            return l_rel

    def _parse_rel(self):
        l_expression = self._parse_expression()

        if self.next_tok["tok_kind"] == "TOK_LT" or self.next_tok["tok_kind"] == "TOK_LE" or self.next_tok["tok_kind"] == "TOK_GE" or self.next_tok["tok_kind"] == "TOK_GT" or self.next_tok["tok_kind"] == "TOK_ASSIGN":
            # expression (<|<=|>=|>|=) expression
            self.cur_tok, self.next_tok = next(self.tok_generator)
            op = self.cur_tok["token"]
            r_expression = self._parse_expression()
            return {"linenum": -1, "token": l_expression["token"] + ' ' + op + ' ' + r_expression["token"], "tok_kind": "TOK_TEST"}

        else:
            # single expression
            return l_expression

    def _parse_expression(self):
        term = self._parse_term()

        if self.next_tok["tok_kind"] == "TOK_PLUS" or self.next_tok["tok_kind"] == "TOK_MINUS":
            # term [+-] expression
            self.cur_tok, self.next_tok = next(self.tok_generator)
            op = self.cur_tok["token"]
            expression = self._parse_expression()
            tmpvar = next(self.tmpvar_generator)
            self.intcode.append({"scope": self.scope.curid(), "label": "", "code": tmpvar["token"] + " = " + term["token"] + ' ' + op + ' ' + expression["token"]})
            return tmpvar

        else:
            # term
            return term

    def _parse_term(self):
        unary = self._parse_unary()

        if self.next_tok["tok_kind"] == "TOK_MUL" or self.next_tok["tok_kind"] == "TOK_DIV" or self.next_tok["tok_kind"] == "TOK_REM":
            # unary [*/%] term
            self.cur_tok, self.next_tok = next(self.tok_generator)
            op = self.cur_tok["token"]
            term = self._parse_term()
            tmpvar = next(self.tmpvar_generator)
            self.intcode.append({"scope": self.scope.curid(), "label": "", "code": tmpvar["token"] + " = " + unary["token"] + ' ' + op + ' ' + term["token"]})
            return tmpvar

        else:
            # unary
            return unary

    def _parse_unary(self):
        if self.next_tok["tok_kind"] == "TOK_BANG":
            # ! unary
            self.cur_tok, self.next_tok = next(self.tok_generator)
            unary = self._parse_unary()
            tmpvar = next(self.tmpvar_generator)
            self.intcode.append({"scope": self.scope.curid(), "label": "", "code": tmpvar["token"] + " = ! " + unary["token"]})
            return tmpvar

        elif self.next_tok["tok_kind"] == "TOK_PLUS":
            # + unary
            self.cur_tok, self.next_tok = next(self.tok_generator)
            return self._parse_unary()

        elif self.next_tok["tok_kind"] == "TOK_MINUS":
            # - unary
            self.cur_tok, self.next_tok = next(self.tok_generator)
            unary = self._parse_unary()
            tmpvar = next(self.tmpvar_generator)
            self.intcode.append({"scope": self.scope.curid(), "label": "", "code": tmpvar["token"] + " = - " + unary["token"]})
            return tmpvar

        else:
            # factor
            return self._parse_factor()

    def _parse_factor(self):
        def err_exit():
            common.err_exit("[Parse Error] L." + str(self.cur_tok["linenum"])
                            + "  Invalid syntacs.\n")

        if self.next_tok["tok_kind"] == "TOK_INT_LITERAL":
            # single number
            self.cur_tok, self.next_tok = next(self.tok_generator)
            return self.cur_tok

        elif self.next_tok["tok_kind"] == "TOK_ID":
            # function call or single variable
            self.cur_tok, self.next_tok = next(self.tok_generator)
            identifier = self.cur_tok

            if self.next_tok["tok_kind"] == "TOK_LPAREN":
                # function call
                self.cur_tok, self.next_tok = next(self.tok_generator)
                args = self._parse_argument_expression_list()

                self.cur_tok, self.next_tok = next(self.tok_generator)
                if self.cur_tok["tok_kind"] != "TOK_RPAREN":
                    err_exit()

                # emit intcode for function call
                funcall_code = "call " + identifier["token"]
                for arg in args:
                    funcall_code += ' ' + arg
                self.intcode.append({"scope": self.scope.curid(), "label": "", "code": funcall_code})

                # C functions put retval on %eax register
                return {"linenum": -1, "token": "%eax", "tok_kind": "TOK_REGISTER"}

            else:
                # single variable
                return identifier

        elif self.next_tok["tok_kind"] == "TOK_LPAREN":
            # ( expression )
            self.cur_tok, self.next_tok = next(self.tok_generator)
            reduction = self._parse_expression()

            self.cur_tok, self.next_tok = next(self.tok_generator)
            if self.cur_tok["tok_kind"] != "TOK_RPAREN":
                err_exit()

            return reduction

        else:
            err_exit()

    def _parse_argument_expression_list(self):
        if self.next_tok["tok_kind"] == "TOK_RPAREN":
            return []

        args = [self._parse_expression()["token"]]

        while self.next_tok["tok_kind"] == "TOK_COMMA":
            self.cur_tok, self.next_tok = next(self.tok_generator)
            args.append(self._parse_expression()["token"])

        return args

def parse(stdin):
    tok_generator = (lambda : tokenizer.gen_tokens(stdin)) ()
    p = Parser(tok_generator)
    return p.parse()
