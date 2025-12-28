from .cnf import get_cnf 

def cyk_parse(sentence):
    words = sentence.lower().split()
    n = len(words)
    cnf = get_cnf()

    table = [[set() for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for lhs, rules in cnf.items():
            for rhs in rules:
                if len(rhs) == 1 and rhs[0] == words[i]:
                    table[i][i].add(lhs)

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for lhs, rules in cnf.items():
                    for rhs in rules:
                        if len(rhs) == 2:
                            B, C = rhs
                            if B in table[i][k] and C in table[k + 1][j]:
                                table[i][j].add(lhs)

    accepted = "K" in table[0][n - 1]

    return accepted, table, words