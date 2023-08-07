x=int(input())
z=int(input())
y=int(input())
st=int(min(x,z,y))
lst=int(max(x,z,y))
mid=x+z+y-st-lst
print(st ,"<", mid ,"<" ,lst)