from . import const

class Vartable:
    def __init__(self):
        self.svlists = []
        # 'svlist' is like this:
        # {"scope": 3, "parent_scope": 2, "child_scopes": [4,6], "vars": [ {"id": a, "stack": -4}, ...] }

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

    def new_svlist(self, scope, parent_scope):
        if parent_scope is not None:
            self._find_svlist(parent_scope)["child_scopes"].append(scope)
        # See self._add_var_to() and find why I put '.BANPEI'
        self.svlists.append({"scope": scope, "parent_scope": parent_scope, "child_scopes": [], "vars": [ {"id": ".BANPEI", "stack": const.LOCAL_VAR_OFFSET_FROM_EBP + const.INT_SIZE} ]})
        return self.svlists[len(self.svlists) - 1]

    def reg_var(self, scope, parent_scope, var):
        svlist = self._find_svlist(scope)
        if svlist is not None:
            self._add_var_to(svlist, var)
        else:
            new_svlist = self.new_svlist(scope, parent_scope)
            self._add_var_to(new_svlist, var)

    def stack_of(self, var, scope):
        def _stack_of(varlist):
            if varlist == []:
                return None
            elif varlist[0]["id"] == var:
                return varlist[0]["stack"]
            else:
                return _stack_of(varlist[1:])

        if scope is None:
            return None

        svlist = self._find_svlist(scope)
        stack = _stack_of(svlist["vars"])
        if stack is None:
            # search all outer scopes
            return self.stack_of(var, svlist["parent_scope"])

        return stack

    def stack_size(self, scope):
        if scope is None:
            return 0

        svlist = self._find_svlist(scope)
        size = (len(svlist["vars"]) - 1) * const.INT_SIZE

        children = self._find_svlist(scope)["child_scopes"]
        for child in children:
            size += self.stack_size(child)

        return size
