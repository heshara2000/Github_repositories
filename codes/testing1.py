heights = [4, 2, 3, 1]

x=heights.reverse()
   #[5,3,2,4]
temp=x[0]  #1
for i in range (x):
   
    if x[i] < x[i+1]:   #5<3,3<2, 2<4
        temp.append(i+1)  #1,3,4
    else:
        continue
print (temp)
