from rules import NormalRule, desc


def get_refactoring_rules():
    rules = [
        # Rename refactoring
        NormalRule(["refactoring.rename.OCRenameProcessor.prepareRenaming"],
                   desc("Rename refactoring")),

        NormalRule(["refactoring.rename.OCInplaceRenameHandler.doRename"],
                   desc("Executing inplace rename", bug="CPP-13833")),

        NormalRule(["refactoring.introduce.inplace.AbstractInplaceIntroducer",
                    "OCBaseExpressionInplaceIntroducer.suggestNames"],
                   desc("Suggesting a name during inplace refactoring", bug="CPP-14932")),

        # Inline refactoring
        NormalRule(["refactoring.inline.OCInlineActionHandlerBase.inlineElement"],
                   desc("Inline refactoring")),

        # Extract refactoring
        NormalRule(["refactoring.OCExtractMethodHandler.invoke",
                    "refactoring.OCExtractMethodProcessor.invoke"],
                   desc("Extract method", bug="CPP-11818")),

        # Move refactoring
        NormalRule(["OCSymbolWithQualifiedName.processSameSymbols",
                    "OCAbstractMoveDialog.setMembersChecked"],
                   desc("Move")),

        NormalRule(["refactoring.move.handlers.OCMoveTopLevelRefactoringHandler.showDialog",
                    "refactoring.move.OCDependentMembersCollector.collect"],
                   desc("Move")),

        NormalRule(["refactoring.move.OCMoveProcessor"],
                   desc("Move")),

        NormalRule(["refactoring.move.handlers.OCMoveRefactoringHandler.showDialog"],
                   desc("Push down (Move) members into new class", bug="CPP-14961")),

        NormalRule(["refactoring.move.handlers.OCMoveHandlerDelegate.tryToMove"],
                   desc("Move after editing common header", bug="CPP-14352")),

        # Change signature refactoring
        NormalRule(["refactoring.changeSignature.OCChangeSignatureProcessor.runSynchronously",
                    "refactoring.changeSignature.OCChangeSignatureUsageProcessor.findConflicts"],
                   desc("Change signature: find conflicts", bug="CPP-17417")),

        NormalRule(["refactoring.changeSignature.OCChangeSignatureProcessor.preprocessUsages"],
                   desc("Process usages while change signature", bug="CPP-15485")),
    ]

    return rules


def get_navigation_rules():
    rules = [
        # Navigation
        NormalRule(["navigation.OCGotoDeclarationHandler.getActionText"],
                   desc("Go to declaration action text", bug="CPP-8460", fixed=173)),

        NormalRule(["editor.impl.EditorGutterComponentImpl",
                    "navigation.OCGotoActionSync.navigate"],
                   desc("Clicking on 'Goto associated symbol' line marker might freeze UI", bug="CPP-13876")),

        NormalRule(["navigation.OCSwitchToHeaderOrSourceRelatedProvider.getItems"],
                   desc("Navigating to related symbol ", bug="CPP-7168", fixed=182)),
    ]
    return rules


def get_rules():
    rules = [

        # Generate Action
        NormalRule(["generate.handlers.OCCCppGenerateHandlerBase.invoke"],
                   desc("CPP generate action", bug="CPP-5906")),

        NormalRule(["generate.handlers.OCCCppGenerateHandlerBase.invoke",
                    "generate.handlers.OCClassActionHandlerBase.invoke",
                    "generate.OCGenerateUtil.applyReplacements",
                    "quickfixes.OCImportSymbolFix.fixAllSymbolsRecursively"],
                   desc("CPP generate action", bug="CPP-16915")),

        NormalRule(["generate.actions.OCBaseGenerateTestAction.update",
                    "generate.actions.OCBaseGenerateTestAction.isValidForFile"],
                   desc("Generate test: is valid for", bug="CPP-14396", fixed=191)),

        NormalRule(["generate.OCCppDefinitionsUtil.getOutsidePreferredPosition",
                    "intentions.OCSplitFunctionIntentionAction.invoke"],
                   desc("Generate Definitions is searching for existing functions", bug="CPP-11254", fixed=182)),

        # Quick fixes
        NormalRule(["quickfixes.OCImportSymbolFix.showHint",
                    "symbols.cpp.OCStructSymbol.getKindUppercase"],
                   desc("Auto-import popup can lock the UI", bug="CPP-10663", fixed=181)),

        NormalRule(["quickfixes.OCCreateNewDefinitionIntentionAction.getText"],
                   desc("Create new Definition", bug="CPP-12939")),

        NormalRule(["quickfixes.OCCreateNewDefinitionIntentionAction.isAvailable"],
                   desc("Create new Definition", bug="CPP-12939")),

        NormalRule(["quickfixes.OCCreateNewDefinitionIntentionAction",
                    "generate.OCGenerateUtil.applyReplacements",
                    "quickfixes.OCImportSymbolFix.fixAllSymbolsRecursively"],
                   desc("Generate definition: import fix", bug="CPP-11254", fixed=182)),

        NormalRule(["intentions.OCAddParametersToConstructorIntentionAction.performAction",
                    "generate.OCGenerateUtil.applyReplacements",
                    "quickfixes.OCImportSymbolFix.fixAllSymbolsRecursively"],
                   desc("Add as parameter to constructor: import fix", bug="CPP-16431")),

        NormalRule(["intentions.OCConvertToPropertyIntentionAction.isAvailable"],
                   desc("OCConvertToPropertyIntentionAction.isAvailable", bug="CPP-17687")),

        # Find Usage / Search
        NormalRule(["OCSymbolWithQualifiedNameImpl.processAssociatedSymbols",
                    "actions.FindUsagesAction.actionPerformed"],
                   desc("Find usages search associated targets", bug="CPP-12806")),

        NormalRule(["OCSymbolWithQualifiedNameImpl.getDefinitionSymbol",
                    "actions.FindUsagesAction.actionPerformed"],
                   desc("Find usages search definitions", bug="CPP-14785")),

        NormalRule(["actions.SearchAgainAction.actionPerformed"],
                   desc("Search again", bug="CPP-14288")),

        # Paste Action
        NormalRule(["actions.PasteReferenceProvider.isPasteEnabled",
                    "actions.QualifiedNameProviderUtil.qualifiedNameToElement"],
                   desc("Paste handler resolves in EDT", bug="CPP-12414")),

        NormalRule(["editorActions.PasteHandler.doPaste",
                    "folding.CustomFoldingBuilder.buildFoldRegions",
                    "editor.OCFoldingBuilder.buildLanguageFoldRegions"],
                   desc("Building custom Folding after Paste action in EDT", bug="CPP-15465")),

        ###
        NormalRule(["ui.TextFieldWithPopupHandlerUI"],
                   desc("Deadlock on Search Everywhere", bug="IDEA-196919", fixed=191)),

        NormalRule(["actions.LoadCMakeProjectAction.actionPerformed"],
                   desc("Load CMake project", bug="CPP-14237", fixed=192)),

        NormalRule(["cmake.projectWizard.ImportCMakeProjectAction.actionPerformed"],
                   desc("Import CMake Project", bug="CPP-14495")),

        NormalRule(["com.intellij.codeInsight.completion.CodeCompletionHandlerBase"],
                   desc("Code completion", bug="CPP-14780")),

        NormalRule(["actions.DeleteAction.actionPerformed",
                    "projectView.impl.ProjectViewImpl"],
                   desc("Delete build directory may lead the freeze", bug="CPP-14872")),

    ]
    return rules + get_refactoring_rules() + get_navigation_rules()
