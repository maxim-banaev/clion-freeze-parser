from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["com.intellij.history.integration.LocalHistoryEventDispatcher"],
                   desc("VFS events processing in LocalHistoryEventDispatcher",
                        bug="IDEA-241371")),
    ]
    return rules


