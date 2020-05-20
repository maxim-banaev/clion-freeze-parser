from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["com.intellij.ui.ColoredTreeCellRenderer.getTreeCellRendererComponent"],
                   desc("ColoredTreeCellRenderer takes a lot of time computing stringWidth",
                        bug="JBR-2292")),

        NormalRule(["X11.XDecoratedPeer.getLocationOnScreen",
                    "java.awt.Component.getLocationOnScreen_NoTreeLock"],
                   desc("XDecoratedPeer.getLocationOnScreen may leed freeze",
                        bug="JBR-1820")),

    ]
    return rules
