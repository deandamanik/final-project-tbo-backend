from .grammar import TERMINALS 

def get_cnf():
    CNF = {}

    def add(lhs, rhs):
        if lhs not in CNF: 
            CNF[lhs] = []
        if rhs not in CNF[lhs]: 
            CNF[lhs].append(rhs)

    for w in TERMINALS["DET"]:     
        add("DET", [w]) 
        
    for w in TERMINALS["PRONOUN"]: 
        add("PRN", [w]); add("NP", [w])
        
    for w in TERMINALS["NOUN"]:    
        add("N", [w]);   add("NP", [w])
        
    for w in TERMINALS["VERB"]:    
        add("V", [w]);   add("VP", [w])
        
    for w in TERMINALS["ADV"]:     
        add("ADV", [w]); add("ADVP", [w])
        
    for w in TERMINALS["ADJ"]:     
        add("ADJ", [w]); add("ADJP", [w])
        
    for w in TERMINALS["PREP"]:    
        add("PREP", [w])

    add("NP", ["DET", "N"])
    add("NP", ["N", "PRN"])
    add("NP", ["N", "N"])
    add("NP", ["N", "ADJP"])
    
    add("VP", ["V", "NP"])
    add("VP", ["ADV", "VP"])
    add("VP", ["VP", "PP"])

    add("PP", ["PREP", "NP"])
    add("ADJP", ["ADV", "ADJ"])

    add("K", ["NP", "VP"])
    add("K", ["NP", "ADJP"])
    add("K", ["NP", "PP"])

    return CNF