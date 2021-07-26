n=int(input())
member=[]

for i in range(n):
    age, name = map(str,input().split())
    age=int(age)
    member.append((age,name))

member.sort(key=lambda x:x[0])

for i in member:
    print(i[0],i[1])

#파이썬은 기본적으로 stable정렬을 하기 때문에
# 같은 숫자인 경우에 먼저온 순서로 자동정렬