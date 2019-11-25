def to_weird_case(string):
    string = list(string)
    ns = []
    for i in range(len(string)):
        if i%2 == 0:
            ns.append(string[i].upper())
        elif i%2 == 1:
            ns.append(string[i].lower())
    return "".join(ns)
