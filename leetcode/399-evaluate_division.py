def calcEquation(equations, values, queries):

    map_path = {}
    for (eq, val) in zip(equations, values):
        if eq[0] not in map_path:
            map_path[eq[0]] = {}
        map_path[eq[0]][eq[1]] = val
        if eq[1] not in map_path:
            map_path[eq[1]] = {}
        map_path[eq[1]][eq[0]] = 1/val

    res = []
    for query in queries:
        start, end = query
        if (start not in map_path) or (end not in map_path):
            res.append(-1)
            continue
        stack_loc, stack_val = [start], [1]
        i = 0
        while i < len(stack_loc) and stack_loc[i] != end:
            # val could be a list
            loc, prev = stack_loc[i], stack_val[i]
            for next, val in map_path[loc].items():
                if next in stack_loc:
                    continue
                stack_loc.append(next)
                stack_val.append(val*prev)
            i += 1
        
        if end in stack_loc:
            res.append(stack_val[stack_loc.index(end)])
        else:
            res.append(-1)

    return res


calcEquation(
    equations = [["a","b"],["b","c"]], 
    values = [2.0,3.0], 
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
)


calcEquation(
    equations = [["a","b"],["b","c"],["bc","cd"]], 
    values = [1.5,2.5,5.0], 
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
)


calcEquation(
    equations = [["a","b"]], 
    values = [0.5], 
    queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
)