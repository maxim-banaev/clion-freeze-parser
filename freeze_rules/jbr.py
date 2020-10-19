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

        NormalRule(["sun.font.FontDesignMetrics.stringWidth"],
                   desc("Idea freezes with AppleSystemUIFont when Event Log is opened",
                        bug="IDEA-235635")),

    ]
    return rules
