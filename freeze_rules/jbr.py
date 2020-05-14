from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["com.intellij.ui.ColoredTreeCellRenderer.getTreeCellRendererComponent"],
                   desc("ColoredTreeCellRenderer takes a lot of time computing stringWidth",
                        bug="JBR-2292")),
    ]
    return rules
