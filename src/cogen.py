from . import common
from . import const

def cogen(intcodes, vartable):
    asm = []
    asm.append(_gen_header())
    for line in intcodes:
        asm.append(_translate(line, vartable))
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
    asm.append("\tmovl\t%esp, %ebp")
    print(intcode)
    asm.append("\tsubl\t$" + str((const.INT_SIZE * const.MAX_ARGS) + vartable.stack_size(intcode["scope"])))

    return asm

def _gen_funend(intcode, vartable):
    endfunction, fun_name = intcode["code"].split()
    asm = []
    asm.append("\t.size\t" + fun_name + ", -" + fun_name)

def _gen_goto(intcode, vartable):
    pass

def _gen_return(intcode, vartable):
    pass

def _gen_iffalse(intcode, vartable):
    pass

def _gen_equality(intcode, vartable):
    pass

def _gen_label(intcode, vartable):
    pass

def _gen_biop(intcode, vartable):
    pass

def _gen_unary(intcode, vartable):
    pass

def _gen_funcall(intcode, vartable):
    pass
