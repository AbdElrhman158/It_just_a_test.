user_input=input()
vowel=[ 'a' , 'e' , 'ı' , 'i' , 'o' , 'ö' , 'u' , 'ü' ]
y='y'
if user_input==y :
    print("maybe")
elif user_input in vowel :
    print("accept")
else :
    print("refuse")