from .grammar import TERMINALS 

def get_cnf():
    CNF = {}

    def add(lhs, rhs):
        if lhs not in CNF: 
            CNF[lhs] = []
        if rhs not in CNF[lhs]: 
            CNF[lhs].append(rhs)

    for w in TERMINALS["KATA_SANDANG"]:
        add("KP", [w])
        
    for w in TERMINALS["KATA_GANTI"]:
        add("KG", [w])
        add("FN", [w])
        
    for w in TERMINALS["KATA_BENDA"]:
        add("KB", [w])
        add("FN", [w])
        
    for w in TERMINALS["KATA_KERJA"]:
        add("KK", [w])
        add("FV", [w])
        
    for w in TERMINALS["KATA_KETERANGAN"]:
        add("KT", [w])
        add("FK", [w])
        
    for w in TERMINALS["KATA_SIFAT"]:
        add("KS", [w])
        add("FA", [w])
        
    for w in TERMINALS["KATA_DEPAN"]:
        add("KD", [w])

    add("FN", ["KP", "KB"])
    add("FN", ["KB", "KG"])
    add("FN", ["KB", "KB"])
    add("FN", ["KB", "FA"])
    
    add("FV", ["KK", "FN"])
    add("FV", ["KT", "FV"])
    add("FV", ["FV", "FP"])

    add("FP", ["KD", "FN"])
    add("FP", ["FP", "FP"])
    add("FP", ["KT", "KD"])
    add("FP", ["FP", "FN"])
    add("FA", ["KT", "KS"])

    add("K", ["FN", "FV"])
    add("K", ["FN", "FA"])
    add("K", ["FN", "FP"])
    add("K", ["K", "FP"])

    return CNF