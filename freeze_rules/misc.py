from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["PotemkinProgress.runInSwingThread"],
                   desc("Potemkin progress", bug="not a bug")),

        NormalRule(["CidrFilesViewHelper$2.customizeCellRenderer",
                    "OCSearchScope.getExplicitlySpecifiedProjectSourceFiles"],
                   desc("Drawing project tree", bug="CPP-10691", fixed=181)),

        NormalRule(["AbstractTreeStructureBase.getChildElements",
                    "OCHeaderFileTypeDetector.detect"],
                   desc("Project view: file type detector")),

        NormalRule(["Inet4AddressImpl.getLocalHostName"],
                   desc("Slow getLocalHostName", bug="JRE-251", fixed=181)),

        NormalRule(["ClangDaemonFormatProvider.findClangFormatContent",
                    "options.CodeStyle.getSettings"],
                   desc("Freezes in CodeStyle.getSettings", bug="IDEA-218532", fixed=193)),

        NormalRule(["codeStyle.CodeStyleFacadeImpl.getLineIndent"],
                   desc("getLineIndent() leads to symbol building", bug="CPP-10486")),

        NormalRule(["usages.UsageInfo2UsageAdapter.getText",
                    "editor.colors.OCSyntaxHighlighterFactory.getSyntaxHighlighter"],
                   desc("Get Syntax highlighter in Find Usage dialog may lead freeze EDT", bug="CPP-17472")),

        NormalRule(["mac.touchbar.TouchBar"],
                   desc("Touchbar action updates might lead to freezes", bug="CPP-13953")),

    ]
    return rules
