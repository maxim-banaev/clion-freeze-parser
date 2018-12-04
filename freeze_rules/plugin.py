from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["FindPopupPanel",
                    "TextMateHighlightingLexer.parseLine"],
                   desc("TextMate line parser leads the freeze in Find Panel", bug="CPP-17116"))
    ]

    return rules

