def is_palindrone(s):
    n = len(s) - 1
    i, j = 0, n
    letters = (r"abcdefghijklmnopqurstuvwxyz1234567890")

    while i < j:

        print(s[i], end='')
        while s[i].lower() not in letters:
            i += 1
            print(s[min(i, n)], end='')
            if i > n:
                return True
        print(s[j], end='')
        while s[j].lower() not in letters:
            j -= 1
            print(s[max(j, 0)], end='')
            if j < 0:
                return True

        if s[i].lower() != s[j].lower():
            return False
        
        i += 1
        j -= 1

        print('\n', end='')

    return True
            

print(is_palindrone(s = r"H8Co9Y8` FhB0MZ?cFd !? H?!YD'Pz7w?Ntiz86,LaEm't!H9 r!? 9q'.sWKS  !iA\".3Y1Gj8ev5S :.` ;7k.;.C?4 811s2K :e` s 'D?u7::::7u?D' s `e: K2;118 4?C.;.k7; `.: S5ve8jG1Y3.\"Ai!  SKW;.'q9 ?!r 9H!t'mEaL,68zitN?w7zP'DY!?H ?! dFc?ZM0BhF `8Y9oC8H"))
print(is_palindrone(s = ".G?j!:;;:Gj?!."))
print(is_palindrone(s = "A man, a plan, a canal: Panama"))