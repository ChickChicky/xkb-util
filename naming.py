from subprocess import check_output

lines = check_output(['dumpkeys', '-kilf1']).decode('utf-8').splitlines()

def getnum(v):
    try:
        return int(v, 16)
    except:
        return None

mapping = {}

for line in lines:
    match line.split():
        case [strcode, name] if getnum(strcode) != None:
            mapping[name] = getnum(strcode)
        case [a, 'for', b]:
            if b in mapping:
                mapping[a] = mapping[b]
            #   print('+', b)
            # else:
            #     print('-', b)
        
print(mapping)
            