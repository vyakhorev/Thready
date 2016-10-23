"""
Fields define choices for values (lists / bounds e.t.c.)
"""

class cAbstrView():
    def __init__(self):
        self.var = None

    def get_var(self):
        return self.var

    def set_var(self, var):
        if self.check_var(var):
            self.var = var

    def check_var(self, var):
        return True

class cAbstrListView():
    def __init__(self):
        self.var = None
        self.variants = []

    def get_var(self):
        return self.var

    def set_var(self, var):
        if self.check_var(var):
            self.var = var

    def get_variants(self):
        return self.variants

    def check_var(self, var):
        return True

class cViewTextInput(cAbstrView):
    pass

class cViewNumberInput(cAbstrView):
    pass