def isBalanced(s):
    # Write your code here
    stack = []
    brackets = {"}":"{", "]":"[", ")":"("}

    for i in s: 
        if i in brackets.values(): 
            #if left-side bracket, add to the stack
            stack.append(i)

        elif stack:
            #check if items in stack, compare last item to key:value  
            top = stack.pop()
            if brackets[i]!=top:
                return "NO"
        else: 
            #means that there is nothing in the stack, but there are still 
            #right-side brackets
            return "NO"
    return "NO" if stack else "YES"
            #if something is in the stack, invalid, else YES




print(isBalanced("()")) #YES
print(isBalanced(")("))#NO
print(isBalanced("({[]})"))#YES
print(isBalanced("{]"))#NO
print(isBalanced("}"))#NO
print(isBalanced("()()()()()()()()"))#YES
print(isBalanced("{[({([])})]}"))#YES
print("______________")


print(isBalanced("}[(]}[][)({]([][)}[)[]))({(]}{}]"))#NO