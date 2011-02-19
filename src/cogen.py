from . import common
from . import const

def cogen(intcodes, vartable):
    asm = []
    asm.append(_gen_header())
    for line in intcodes:
        asm.append(_translate(line, vartable))
    asm.append(_gen_footer())
    return common.flatten(asm)

def _translate(intcode, vartable):
    if intcode["code_kind"] == "CODE_FUNDEF":
        return _gen_fundef(intcode, vartable)
    elif intcode["code_kind"] == "CODE_FUNEND":
        return _gen_funend(intcode, vartable)
    elif intcode["code_kind"] == "CODE_GOTO":
        return _gen_goto(intcode, vartable)
    elif intcode["code_kind"] == "CODE_RETURN":
        return _gen_return(intcode, vartable)
    elif intcode["code_kind"] == "CODE_IFFALSE":
        return _gen_iffalse(intcode, vartable)
    elif intcode["code_kind"] == "CODE_EQUALITY":
        return _gen_equality(intcode, vartable)
    elif intcode["code_kind"] == "CODE_LABEL":
        return _gen_label(intcode, vartable)
    elif intcode["code_kind"] == "CODE_BIOP":
        return _gen_biop(intcode, vartable)
    elif intcode["code_kind"] == "CODE_UNARY":
        return _gen_unary(intcode, vartable)
    elif intcode["code_kind"] == "CODE_FUNCALL":
        return _gen_funcall(intcode, vartable)
    else:
        common.err_exit("[Internal Error] Unknown intcode type.\n")

def _movl(_from, to, vartable, scope):
    # in 'movl from, to', if both 'from' and 'to' are stack place,
    # gas raises an error

    if common.isimm(to):
        common.err_exit("[Cogen Error] Cannot assign anything to an immediate.\n")

    _from = vartable.place_of(_from, scope)
    to = vartable.place_of(to, scope)

    asm = []
    if common.isstack(_from) and common.isstack(to):
        asm.append("\tmovl\t" + _from + ", %eax")
        asm.append("\tmovl\t" + "%eax, " + to)
    else:
        asm.append("\tmovl\t" + _from + ", " + to)

    return asm

def _cmpl(lh, rh, vartable, scope):
    # in 'cmpl lh, rh', when:
    # * both 'lh' and 'rh' are stack place
    # * 'rh' is immediate
    # gas raises an error

    lh = vartable.place_of(lh, scope)
    rh = vartable.place_of(rh, scope)

    asm = []
    if common.isimm(lh) and common.isimm(rh):
        asm.append(_movl(rh, "%eax"))
        asm.append("\tcmpl\t" + lh + ", %eax")
    elif (not common.isimm(lh)) and common.isimm(rh):
        asm.append("\tcmpl\t" + rh + ", " + vartable.place_of(lh, scope))
    elif common.isstack(lh) and common.isstack(rh):
        asm.append(_movl(rh, "%eax", vartable, scope))
        asm.append("\tcmpl\t" + lh + ", %eax")
    else:
        asm.append("\tcmpl\t" + vartable.place_of(lh, scope) + ", " + vartable.place_of(rh, scope))

    return asm

def _conditional_jmp(op, label):
    # Note that this function is used for 'iffalse'
    # So, '<' means 'not <' = '>=' and etc...
    asm = []
    if op == "<":
        asm.append("\tjge\t" + label)
    elif op == ">":
        asm.append("\tjle\t" + label)
    elif op == "<=":
        asm.append("\tjg\t" + label)
    elif op == ">":
        asm.append("\tjgl\t" + label)
    elif op == "==":
        asm.append("\tjne\t" + label)
    elif op == "!=":
        asm.append("\tje\t" + label)
    else:
        common.err_exit("[Internal Error] Unexpected operator (cogen._conditional_jmp())\n")

    return asm

def _not(v, vartable, scope):
    v = vartable.place_of(v, scope)
    if common.isimm(v):
        common.err_exit("[Internal Error] argument should not be a number. (cogen_not())\n")

    asm = []
    asm.append("\tnotl\t" + v)
    return asm

def _neg(v, vartable, scope):
    v = vartable.place_of(v, scope)
    if common.isimm(v):
        common.err_exit("[Internal Error] argument should neg be a number. (cogen_neg())\n")

    asm = []
    asm.append("\tnegl\t" + v)
    return asm

def _gen_header():
    return ["\t.text"]

def _gen_footer():
    footer = []
    footer.append("\t.ident\t\"PyCC by @laysakura\"")
    footer.append("\t.section\t.note.GNU-stack,\"\",@progbits")
    return footer

def _gen_fundef(intcode, vartable):
    function, fun_name = intcode["code"].split()

    asm = []
    asm.append(".global\t" + fun_name)
    asm.append("\t.type\t" + fun_name + ",\t@function")
    asm.append(fun_name + ':')
    asm.append("\tpushl\t%ebp")
    asm.append(_movl("%esp", "%ebp", vartable, intcode["scope"]))
    asm.append("\tsubl\t$" + str((const.INT_SIZE * const.MAX_ARGS) + vartable.stack_size(intcode["scope"])) + ", %esp")

    return asm

def _gen_funend(intcode, vartable):
    endfunction, fun_name = intcode["code"].split()
    asm = []
    asm.append("\t.size\t" + fun_name + ", .-" + fun_name)
    return asm

def _gen_goto(intcode, vartable):
    goto, label = intcode["code"].split()
    asm = []
    asm.append("\tjmp\t" + label)
    return asm

def _gen_return(intcode, vartable):
    asm = []
    _return, retval = intcode["code"].split()
    asm.append(_movl(retval, "%eax", vartable, intcode["scope"]))
    asm.append("\tleave")
    asm.append("\tret")
    return asm

def _gen_iffalse(intcode, vartable):
    iffalse_code = intcode["code"].split()

    asm = []
    if iffalse_code[2] == "goto":
        # 'test' in 'iffalse test goto L_false' is single variable or number
        test = iffalse_code[1]
        test = vartable.place_of(test, intcode["scope"])
        false_label = iffalse_code[3]

        if common.isimm(test):
            if test == "$0":
                asm.append("\tjmp\t" + false_label)
        else:
            asm.append(_cmpl("$0", test, vartable, intcode["scope"]))
            asm.append("\tje\t" + false_label)

    else:
        test_lh, test_op, test_rh = iffalse_code[1], iffalse_code[2], iffalse_code[3]
        false_label = iffalse_code[5]
        asm.append(_cmpl(test_lh, test_rh, vartable, intcode["scope"]))
        asm.append(_conditional_jmp(test_op, false_label))

    return asm

def _gen_equality(intcode, vartable):
    # stray equality expression.
    # ignore unless the operation is assignment
    equality_expr = intcode["code"].split()
    if len(equality_expr) < 3:
        return []

    lh, op, rh = equality_expr[0], equality_expr[1], equality_expr[2]

    if op != '=':
        return []

    asm = []
    asm.append(_movl(rh, lh, vartable, intcode["scope"]))
    return asm

def _gen_label(intcode, vartable):
    asm = []
    asm.append(intcode["label"] + ':')
    return asm

def _gen_biop(intcode, vartable):
    pass

def _gen_unary(intcode, vartable):
    # 'lh = op rh'
    unary_expr = intcode["code"].split()
    lh, op, rh = unary_expr[0], unary_expr[2], unary_expr[3]

    asm = []
    asm.append(_movl(rh, lh, vartable, intcode["scope"]))

    if op == '!':
        asm.append(_not(lh, vartable, intcode["scope"]))
    elif op == '-':
        asm.append(_neg(lh, vartable, intcode["scope"]))

    return asm

def _gen_funcall(intcode, vartable):
    funcall_stmt = iter(intcode["code"].split())
    next(funcall_stmt)          # call
    fun_name = next(funcall_stmt)

    asm = []
    for cnt, arg in enumerate(funcall_stmt):
        asm.append(_movl(arg, str(cnt * const.INT_SIZE) + "(%esp)", vartable, intcode["scope"]))

    asm.append("\tcall\t" + fun_name)
    return asm
