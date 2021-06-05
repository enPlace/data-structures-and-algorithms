def isBalanced(s):
    # Write your code here
    stack = []
    brackets = {"}":"{", "]":"[", ")":"("}
    for i in s: 
        if i in brackets.values(): 
            stack.append(i)
        elif stack: 
            top = stack.pop()
            if brackets[i]!=top:
                return "NO"
        else:
            return "NO"
    return "NO" if stack else "YES" 




print(isBalanced("()")) #YES
print(isBalanced(")("))#NO
print(isBalanced("({[]})"))#YES
print(isBalanced("{]"))#NO
print(isBalanced("}"))#NO
print(isBalanced("()()()()()()()()"))#YES
print(isBalanced("{[({([])})]}"))#YES
print("______________")


print(isBalanced("}[(]}[][)({]([][)}[)[]))({(]}{}]"))#NO