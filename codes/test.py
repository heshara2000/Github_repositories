x=10
y=x
x+=1

if id(x) !=id(y):
    print("x and y do not refer  to the same object")
else:
    print(y)