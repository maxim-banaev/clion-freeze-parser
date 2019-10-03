from rules import NormalRule, desc


def get_rules():
    rules = [
        NormalRule(["execution.sanitizers.SanitizersConfigurationExtension.attachToProcess"],
                   desc("IDE lockup when Use visual representation for Sanitizer", bug="CPP-16010")),



        NormalRule(["execution.debugger.evaluation.CidrValue.computeSourcePosition"],
                   desc("Freezes in CidrValue.computeSourcePosition", bug="CPP-16842")),

        NormalRule(["execution.debugger.breakpoints.CidrWatchpointHandler.cleanup"],
                   desc("Stopping a debug session", bug="CPP-11330", fixed=181)),

        NormalRule(["execution.debugger.OCEvaluator"],
                   desc("Evaluating variables during debugging might lead to freezes", bug="CPP-13122", fixed=193)),

        NormalRule(["execution.debugger.OCDebuggerTypesHelper"],
                   desc("Evaluating variables during debugging might lead to freezes", bug="CPP-13122", fixed=193)),


        NormalRule(["execution.testing.CidrTestWithScopeElementsFramework.getTestLinks"],
                   desc("Searching for unit tests", bug="CPP-11735", fixed=183)),

        NormalRule(["execution.testing.CidrTestRunConfigurationProducer.isConfigurationFromContext"],
                   desc("Calculating run configuration for Google Test", bug="CPP-9359", fixed=183)),

        NormalRule(["execution.testing.CidrRunConfigurationSettingsEditor$MyComboBox.fireSelectedItemChanged",
                    "execution.testing.google.CidrGoogleTestRunConfigurationData"],
                   desc("Google test run configuration editor", bug="CPP-11409", fixed=183)),

        NormalRule(["execution.testing.CidrTestListUpdater"],
                   desc("Initial tests scanning in big projects", bug="CPP-14242")),

        NormalRule(["execution.testing.google.CidrGoogleTestRunConfigurationData.checkData"],
                   desc("Initial tests scanning in big projects", bug="CPP-14242")),

        NormalRule(["LineMarkerInfo.getLineMarkerTooltip",
                    "execution.testing.CidrTestRunConfigurationProducer.setupConfigurationFromContext"],
                   desc("Test line marker: tooltip")),
    ]
    return rules
