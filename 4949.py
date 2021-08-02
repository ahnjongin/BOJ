while True:
    stack = []
    count=0
    a=input()
    if a=='.':
        break
    for i in a:
        if i =='(' or i =='[':
            stack.append(i)
        elif i == ')':
            if len(stack)==0 or stack[-1]=='[':
                count=1
                break
            elif stack[-1]=='(':
                stack.pop()
        elif i ==']':
            if len(stack)==0 or stack[-1]=='(':
                count=1
                break
            elif stack[-1]=='[':
                stack.pop()
    if count==0 and len(stack)==0:
        print('yes')
    else:
        print('no')
