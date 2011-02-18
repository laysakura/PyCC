from . import common

class Scope:
    def __init__(self):
        self.scopes = []
        self._curid = None
        self.id_generator = common.gen_unique_id()

    def curid(self):
        return self._curid

    def scopein(self):
        newid = next(self.id_generator)
        self.scopes.append({"parent": self.curid(), "id": newid})
        self._curid = newid

    def scopeout(self):
        self._curid = self._parent_of(self.curid())

    def _parent_of(self, search_id):
        def find(scopes):
            if scopes == []:
                common.err_exit("[Internal Error]  Cannot find scope (Scope._find_scope())\n")
            elif scopes[0]["id"] == search_id:
                parent = scopes[0]["parent"]
                return parent
            else:
                return find(scopes[1:])

        return find(self.scopes)
