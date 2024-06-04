def add_binary(a, b):

    res = ''
    i, rem = 0, 0
    while i < len(a) or i < len(b) or rem:
        val = 0
        if i < len(a) and a[-(i+1)] == '1':
            val += 1
        if i < len(b) and b[-(i+1)] == '1':
            val += 1
        
        val += rem
        rem = val // 2
        res = f'{val % 2}' + res
        i += 1

    return res

add_binary(a = "1010", b = "1011")
add_binary(a = "11", b = "1")