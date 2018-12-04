from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["clang.format.ClangDaemonFormatProvider.format"],
                   desc("Reformat code via ClangFormat", bug="CPP-16455")),

        NormalRule(["clang.namehint.ClangInlayParameterHintsProvider.getHintInfo"],
                   desc("Get hint info may lead the freeze in EDT", bug="CPP-16494", fixed=192)),

    ]
    return rules
