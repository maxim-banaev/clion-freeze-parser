import pkgutil
import os

import freeze_rules.actions
import freeze_rules.clang
import freeze_rules.editor
import freeze_rules.execution
import freeze_rules.lazyReparse
import freeze_rules.misc
import freeze_rules.plugin
import freeze_rules.resolve
import freeze_rules.symtable


def get_rules():
    rules = []
    for (i, name, _) in pkgutil.iter_modules([os.path.dirname(__file__)]):
        rules += eval(name + '.get_rules()')
    return rules
