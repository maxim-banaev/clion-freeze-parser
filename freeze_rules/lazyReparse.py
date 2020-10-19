from rules import NormalRule, desc


ENSURE_PARSED = "LazyParseableElement.getFirstChildNode"


def get_rules():
    rules = [
        # Find Usage
        NormalRule(["findUsages.PsiElement2UsageTargetAdapter.isValid",
                    ENSURE_PARSED],
                   desc("Usages View may cause a freeze on update", bug="CPP-8459")),

        NormalRule(["usages.UsageInfo2UsageAdapter.isValid",
                    ENSURE_PARSED],
                   desc("Usages View may cause a freeze on update", bug="CPP-8459")),

        NormalRule(["usages.impl.UsageViewImpl.checkNodeValidity",
                    ENSURE_PARSED],
                   desc("Usages View may cause a freeze on update", bug="CPP-8459")),

        NormalRule(["actions.SearchEverywhereAction",
                    "symbols.OCSymbolBase.canNavigate",
                    ENSURE_PARSED],
                   desc("Search everywhere -> canNavigate -> reparse", bug="CPP-11711", fixed=182)),

        NormalRule(["actions.FindInPathAction.actionPerformed",
                    "find.impl.FindInProjectUtil.setDirectoryName",
                    "symbols.OCSymbolBase.locateDefinition",
                    ENSURE_PARSED],
                   desc("Find in path -> locate definition -> reparse")),

        # Highlighting
        NormalRule(["highlighting.BraceHighlightingHandler.lookForInjectedAndMatchBracesInOtherThread",
                    ENSURE_PARSED],
                   desc("Highlighting matching brackets", bug="IDEA-177314", fixed=173)),

        NormalRule(["highlighting.HighlightUsagesHandlerFactoryBase.createHighlightUsagesHandler",
                    ENSURE_PARSED],
                   desc("Highlight Usages pass -> reparse", bug="CPP-9373", fixed=181)),

        # Folding
        NormalRule(["ComponentStoreImpl.save",
                    "text.TextEditorState.getFoldingState",
                    ENSURE_PARSED],
                   desc("Saving folding state", bug="CPP-10639", fixed=173)),

        NormalRule(["folding.impl.CodeFoldingManagerImpl.writeFoldingState",
                    ENSURE_PARSED],
                   desc("Saving folding state", bug="CPP-10639", fixed=173)),

        NormalRule(["folding.impl.CodeFoldingManagerImpl.saveFoldingState",
                    ENSURE_PARSED],
                   desc("Saving folding state", bug="CPP-10639", fixed=173)),

        NormalRule(["folding.impl.CodeFoldingManagerImpl$1.mouseMoved",
                    ENSURE_PARSED],
                   desc("Folding + mouse moved -> reparse")),

        # Formatting
        NormalRule(["formatting.OCAutoFormatTypedHandler.execute",
                    "PsiUtilBase.getLanguageInEditor",
                    ENSURE_PARSED],
                   desc("Auto format typed handler: get language and reparse", bug="CPP-13581")),

        NormalRule(["symtable.FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged",
                    ENSURE_PARSED],
                   desc("FileSymbolTablesCache$OCCodeBlockModificationListener.treeChanged")),

        # Actions
        NormalRule(["actions.ReformatCodeAction.actionPerformed",
                    ENSURE_PARSED],
                   desc("Document commit while reformat code", bug="CPP-17138")),

        NormalRule(["actions.NextOccurenceAction.go",
                    ENSURE_PARSED],
                   desc("next occurrence -> reparse")),

        NormalRule(["actions.GotoDeclarationAction.update",
                    ENSURE_PARSED],
                   desc("Goto declaration update -> reparse")),

        NormalRule(["editorActions.SelectWordHandler.doExecute",
                    ENSURE_PARSED],
                   desc("Select word/expand selection -> reparse", bug="CPP-11901")),

        NormalRule(["editorActions.PasteHandle",
                    ENSURE_PARSED],
                   desc("Paste function from huge header -> reparse", bug="CPP-14849")),

        NormalRule(["editorActions.CutHandler",
                    ENSURE_PARSED],
                   desc("Cut function from huge header -> reparse", bug="CPP-14849")),

        NormalRule(["actions. BaseRefactoringAction.actionPerformed",
                    ENSURE_PARSED],
                   desc("Replace in path -> reparse", bug="CPP-16170")),

        NormalRule(["editorActions.BackspaceHandler.handleBackspace",
                    ENSURE_PARSED],
                   desc("Delete semicolon in member variable declaration in header file -> reparse", bug="CPP-12901")),

        NormalRule(["CtrlMouseHandler",
                    "getEditorForInjectedLanguageNoCommit",
                    ENSURE_PARSED],
                   desc("CtrlMouseHandler + injected editor", bug="CPP-11610")),

        NormalRule(["filters.FileHyperlinkInfoBase.navigate",
                    ENSURE_PARSED],
                   desc("File hyper links -> reparse", bug="CPP-11601")),

        NormalRule(["MyAutoScrollFromSourceHandler",
                    "SelectInTargetPsiWrapper.selectIn",
                    ENSURE_PARSED],
                   desc("Auto scroll to source -> reparse", bug="CPP-11591")),

        NormalRule(["documentation.QuickDocOnMouseOverManager",
                    ENSURE_PARSED],
                   desc("Quick Documentation on mouse move -> reparse", bug="CPP-12831")),

        NormalRule(["SmartPointerManagerImpl.updatePointerTargetsAfterReparse",
                    ENSURE_PARSED],
                   desc("Document commit while updating smart psi pointers", bug="CPP-13493")),

        NormalRule(["SmartPsiElementPointerImpl.doRestoreElement",
                    ENSURE_PARSED],
                   desc("Lazy parsing while restoring smart psi pointers", bug="CPP-22505")),

        NormalRule(["InjectedLanguageManagerImpl.disposeInvalidEditors",
                    ENSURE_PARSED],
                   desc("InjectedLanguageManagerImpl.disposeInvalidEditors causes reparse in EDT", bug="CPP-17241")),

        NormalRule(["InjectedLanguageUtil.findInjectedPsiNoCommit",
                    ENSURE_PARSED],
                   desc("InjectedLanguageUtil.findInjectedPsiNoCommit causes reparse in EDT", bug="CPP-20445")),

        NormalRule(["InspectionResultsView.showInRightPanel",
                    ENSURE_PARSED],
                   desc("Inspection results view might lead to freezes on click", bug="CPP-13984")),

        NormalRule(["cidr.lang.psi.impl.OCTargetElementUtil.findTargetElement",
                    ENSURE_PARSED],
                   desc("OCTargetElementUtil.findTargetElement causes reparse in EDT", bug="CPP-20447")),

        NormalRule(["vim.group.copy.PutGroup.putTextAndSetCaretPosition",
                    "vim.group.ChangeGroup.autoIndentRange",
                    ENSURE_PARSED],
                   desc("vim: putText -> autoIndentRange -> Lazy reparse in EDT", bug="CPP-20473")),

        NormalRule(["completion.ml.common.RecentPlacesFeatures",
                    ENSURE_PARSED],
                   desc("completion.ml.common.RecentPlacesFeatures -> Lazy reparse in EDT", bug="CPP-22190"))

    ]
    return rules
