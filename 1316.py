a=int(input())
count=a
for i in range(a):
    word=input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count-=1
            break
print(count)