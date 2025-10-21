def negate_literal(literal):
    return literal[1:] if literal.startswith('~') else '~' + literal

def resolve(ci, cj):
    resolvents = []
    for di in ci:
        for dj in cj:
            if di == negate_literal(dj):
                new_clause = list(set(ci + cj))
                new_clause.remove(di)
                new_clause.remove(dj)
                resolvents.append(sorted(set(new_clause)))
    return resolvents

def resolution(kb, query):
    kb = [sorted(set(clause)) for clause in kb]
    query_negated = [negate_literal(lit) for lit in query]
    kb.append(query_negated)
    print(f"Initial KB (with negated query): {kb}\n")

    new = set()
    while True:
        n = len(kb)
        pairs = [(kb[i], kb[j]) for i in range(n) for j in range(i + 1, n)]
        generated_any = False
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            for resolvent in resolvents:
                if not resolvent:
                    print(f"Resolved {ci} and {cj} to get empty clause []")
                    return True
                resolvent_tuple = tuple(sorted(resolvent))
                if resolvent_tuple not in new:
                    print(f"Resolved {ci} and {cj} to get {resolvent}")
                    new.add(resolvent_tuple)
                    generated_any = True
        if not generated_any:
            print("No more resolvents. Query is NOT entailed.")
            return False
        for clause in new:
            if list(clause) not in kb:
                kb.append(list(clause))

# Example usage
kb = [
    ['P', 'Q'],
    ['~P', 'R'],
    ['~Q', 'R']
]
query = ['R']
result = resolution(kb, query)
print("\nFinal Result: Is the query entailed?", result)
