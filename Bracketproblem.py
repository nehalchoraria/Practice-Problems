def wellbracketed(string):
    stack = []
    for i in list(string):
        if i is '(':
            stack.append("(")
        elif i is ')':
                if not stack:                   # This means stack is empty and first element 
                    return False                # is ) which is invalid case.
                elif stack[-1] == "(":
                    stack.pop()
        else:
            pass
    
    if stack:            #if contains some elements
        return False
    else:
        return True

print(wellbracketed("()(as)9d(sasas0)))sasd()"))
print(wellbracketed("()"))