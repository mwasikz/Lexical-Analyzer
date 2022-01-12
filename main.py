keywords = ("abstract", "continue", "for", "new", "switch", "assert", "default", "goto", "package", "synchronized", "boolean", "do", "if", "private", "this", "break", "double", "implements", "protected", "throw", "byte", "else", "import", "public", "throws", "case", "enum", "instanceof", "return", "transient", "catch", "extends", "int", "short", "try", "char", "final", "interface", "static", "void", "class", "finally", "long", "strictfp", "volatile", "const", "float", "native", "super", "while")
mathOps = ("+", "-", "*", "/", "=", "%","+=", "-=", "*=", "/=", "%=","++","--")
logicalOps = ("<", ">", ">=", "<=", "==","&&","||")
others = (",", ";", "(", ")", "{", "}", "[", "]")

keywordsSet = set()
mathOpsSet = set()
logicalOpsSet = set()
othersSet = set()
identifiersSet = set()
numValsList = list()

txtFile = open("test.txt", "r")

def lexicalAnalyzer(sym):
    sym = sym.strip()
    if sym.endswith(others):
        othersSet.add(sym[-1])
        sym = sym[0:-1]

    if sym in keywords:
        keywordsSet.add(sym)
    elif sym in mathOps:
        mathOpsSet.add(sym)
    elif sym in logicalOps:
        logicalOpsSet.add(sym)
    elif sym in others:
        othersSet.add(sym)
    else:
        try:
            sym = int(sym)
            if sym not in numValsList:
                numValsList.append(str(sym))
        except ValueError:
            if "." in sym:
                if sym not in numValsList:
                    numValsList.append(str(sym))
            else:
                identifiersSet.add(sym)

for line in txtFile:
    lineStr = line.strip()
    lineStr = lineStr.split()
    for symbol in lineStr:
        lexicalAnalyzer(symbol)


identifiersSet.remove("")

print("keywords: ", end="")
print(*keywordsSet, sep=", ")

print("Identifiers: ", end="")
print(*identifiersSet, sep=", ")

print("Math Operators: ", end="")
print(*mathOpsSet, sep=", ")

print("Logical Operators: ", end="")
print(*logicalOpsSet, sep=", ")

print("Numerical Values: ", end="")
print(*numValsList, sep=", ")

print("Others: ", end="")
print(*othersSet, sep=" ")
