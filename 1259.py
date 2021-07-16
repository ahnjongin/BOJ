while(1):
    a= input()
    if a=='0':
        break
    b=a[::-1]
    print ("yes" if a==b else "no")

