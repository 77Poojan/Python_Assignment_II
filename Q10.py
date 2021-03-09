def change_case1(str):
    res = [str[0].lower()]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
     
    return ''.join(res)

def change_case2(str):
    res = [str[0].lower()]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('-')
            res.append(c.lower())
        else:
            res.append(c)
     
    return ''.join(res)  
     
str = "ThisIsCamelCased"
c1 = change_case1(str)
c2 = change_case2(str)
print(f'snake case => {c1}')
print(f'kebab case => {c2}')