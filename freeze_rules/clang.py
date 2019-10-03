from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["clang.format.ClangDaemonFormatProvider.format"],
                   desc("Reformat code via ClangFormat", bug="CPP-16455")),

        NormalRule(["clang.formatClangDaemonFormatProvider.findClangFormatContent",
                    "CompletableFuture.get"],
                   desc("ClangFormat: findClangFormatContent", bug="CPP-15717", fixed=193)),

        NormalRule(["clang.ClangDaemonFormatProvider.format",
                    "editor.impl.DocumentImpl.doGetText"],
                   desc("ClangFormat: slow Document.getText")),

        NormalRule(["clang.namehint.ClangInlayParameterHintsProvider.getHintInfo"],
                   desc("Get hint info may lead the freeze in EDT", bug="CPP-16494", fixed=192)),

        NormalRule(["codeInsight.hints.PopupActionsKt.hasDisabledOptionHintInfo",
                    "clang.namehint.ClangInlayParameterHintsProvider.getNamehints",
                    "clang.ClangUtils.waitForClangFuture"],
                   desc("clangd: slow 'has namehints' check", bug="CPP-17243")),
    ]
    return rules
