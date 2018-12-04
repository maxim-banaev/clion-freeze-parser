from rules import NormalRule, desc

FileSymbolTablesCache = "symtable.FileSymbolTablesCache"


def get_rules():
    rules = [
        NormalRule([FileSymbolTablesCache,
                    "vfs.newvfs.RefreshSessionImpl"],
                   desc("Freeze on updating a symbol table cache after VFS refresh", bug="CPP-15680")),

        NormalRule([FileSymbolTablesCache,
                    "vfs.VirtualFile.setBinaryContent"],
                   desc("Freeze on updating a symbol table cache after set binary content", bug="CPP-17004")),

        NormalRule([FileSymbolTablesCache,
                    "FileBasedIndexImpl$ChangedFilesCollector.ensureUpToDateAsync"],
                   desc("File symbols cache: ensure up-to-date async")),
    ]
    return rules
