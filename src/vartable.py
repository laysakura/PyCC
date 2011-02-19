from . import const
from . import common

class Vartable:
    def __init__(self):
        self.svlists = []
        # 'svlist' is like this:
        # {"scope": 3, "parent_scope": 2, "child_scopes": [4,6], "vars": [ {"id": ".BANPEI", "stack": 0}, {"id": "v", "stack": -4}, ...] }
        # {"scope": 1, "parent_scope": None, "child_scopes": [3], "vars": [ ... {"id": "arg1", "stack": 8}, {"id": ".BANPEI", "stack": 0} ]}
        # Note that scope with args never has local vars
        # (since function-definition has a single scope)

    def _find_svlist(self, scope):
        def find(svlists):
            if svlists == []:
                return None
            elif svlists[0]["scope"] == scope:
                return svlists[0]
            else:
                return find(svlists[1:])

        return find(self.svlists)

    def _add_var_to(self, svlist, var):
        svlist["vars"].append( {"id": var, "stack": svlist["vars"][len(svlist["vars"]) - 1]["stack"] - const.INT_SIZE} )

    def _add_arg_to(self, svlist, arg):
        svlist["vars"].insert(0, {"id": arg, "stack": svlist["vars"][0]["stack"] + const.INT_SIZE} )

    def new_svlist(self, scope, parent_scope):
        if parent_scope is not None:
            self._find_svlist(parent_scope)["child_scopes"].append(scope)
        # See self._add_var_to() and find why I put '.BANPEI'
        self.svlists.append({"scope": scope, "parent_scope": parent_scope, "child_scopes": [], "vars": [ {"id": ".BANPEI", "stack": const.ARG_OFFSET_FROM_EBP - const.INT_SIZE}, {"id": ".BANPEI", "stack": const.LOCAL_VAR_OFFSET_FROM_EBP + const.INT_SIZE} ]})
        return self.svlists[len(self.svlists) - 1]

    def reg_var(self, scope, parent_scope, var):
        svlist = self._find_svlist(scope)
        if svlist is not None:
            self._add_var_to(svlist, var)
        else:
            new_svlist = self.new_svlist(scope, parent_scope)
            self._add_var_to(new_svlist, var)

    def reg_arg(self, scope, parent_scope, arg):
        svlist = self._find_svlist(scope)
        if svlist is not None:
            self._add_arg_to(svlist, arg)
        else:
            new_svlist = self.new_svlist(scope, parent_scope)
            self._add_var_to(new_svlist, arg)

    def _stack_of(self, var, scope):
        if common.isstack(var):
            return var

        def __stack_of(varlist):
            if varlist == []:
                return None
            elif varlist[0]["id"] == var:
                return varlist[0]["stack"]
            else:
                return __stack_of(varlist[1:])

        if scope is None:
            return None

        svlist = self._find_svlist(scope)
        stack = __stack_of(svlist["vars"])
        if stack is None:
            # search all outer scopes
            return self._stack_of(var, svlist["parent_scope"])

        return str(stack) + "(%ebp)"

    def _register_of(self, var, scope):
        if common.isreg(var):
            return var
        return None

    def place_of(self, var, scope):
        """
        Always returns symbole usable in gas.
        ex:
          * $777
          * -4(%ebp)
          * %eax
        """
        if common.isimm(var):
            return var

        reg = self._register_of(var, scope)
        if reg is not None:
            return reg
        else:
            return self._stack_of(var, scope)

    def stack_size(self, scope):
        if scope is None:
            return 0

        svlist = self._find_svlist(scope)
        size = abs(svlist["vars"][ len(svlist["vars"]) - 1 ]["stack"])

        children = self._find_svlist(scope)["child_scopes"]
        for child in children:
            size += self.stack_size(child)

        return size
