def is_folder(s):
    if(s.count('.')==0):
        return True
    else:
        return False


def is_file(s):
    if(s.count('.')==0):
        return False
    else:
        return True


def is_code(s):
    if(s.count('.') == 0):
        return False
    else:
        s1=s[s.index("."):len(s)]
        if(s1==".cpp" or s1=='.py'):
            return True
        else:
            return False


def is_image(s):
    if(s.count('.') == 0):
        return False
    else:
        s1=s[s.index("."):len(s)]
        if(s1==".png" or s1=='.jpg'):
            return True
        else:
            return False


def level(s):
    return (s.count('/'))


s=str(input())
print(is_folder(s))
print(is_file(s))
print(is_code(s))
print(is_image(s))
print(level(s))