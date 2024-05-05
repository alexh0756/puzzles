def simplifyPath(path):

    abs_path = '/'
    i, j = 0, 0

    if path[-1] != '/':
        path += '/'

    while i < len(path) and j < len(path):
        if path[j] == '/':
            if path[i:j] in ('', '.'):
                pass
            elif path[i:j] == '..':
                a = max(len(abs_path) - 2, 0)
                while abs_path[a] != '/':
                    a -= 1
                abs_path = abs_path[:a+1]
            else:
                abs_path += path[i:j] + '/'

            i, j = j, j

        if path[i] == '/':
            i += 1
        j += 1
    

    return abs_path

print(simplifyPath(path="/home/"))
print(simplifyPath(path="/home//foo/"))
print(simplifyPath(path="/home/user/Documents/../Pictures"))
print(simplifyPath(path="/../"))
print(simplifyPath(path="/.../a/../b/c/../d/./"))