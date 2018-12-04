from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["editor.parameterInfo.OCArgumentListCallPlace.collectCallOptions"],
                   desc("parameter info", bug="CPP-9361", fixed=182)),

        NormalRule(["editor.OCFunctionParameterInfoHandler.updateParameterInfo"],
                   desc("parameter info", bug="CPP-9361", fixed=182)),

        NormalRule(["editor.OCTypedHandlerDelegate.charTyped"],
                   desc("Parsing in typing handlers for colon and hash sign", bug="CPP-11365", fixed=181)),
    ]
    return rules
