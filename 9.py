a=input()
if len(a)>3:
    if a[-1]=='g' and a[-2]=='n' and a[-3]=='i':
        print(a+'ly')
    else:
        print(a+'ing')
else:
    print(a)