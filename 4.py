def polindrom(a):
    if a==a[::-1]:
        return True
    else:
        return False
    
a=input()
print(polindrom(a))