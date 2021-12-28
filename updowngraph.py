lis=list(map(int,input().split()))

heights_list=[]
heights_list.append(lis[0])
for i in range(1,len(lis)):
    if(i%2!=0):
        heights_list.append(heights_list[i-1]-lis[i])
    else:
        heights_list.append(heights_list[i-1]+lis[i])


maximum_height=max(heights_list)
minimum_height=min(heights_list)

matrix=[]
for i in range(maximum_height+abs(minimum_height)):
    matrix.append([0]*sum(lis))
row=maximum_height-1
col=0
up=1

for i in range(len(lis)):
    for j in range(lis[i]):
        if(up==1):
            matrix[row][col]=1
            row-=1
            col+=1
        else:
            matrix[row][col]=2
            row+=1
            col+=1
    if(up==1):
            row+=1
            up=0
    else:
        row-=1
        up=1
for i in matrix:
    out=''
    for j in i:
        if(j==0):
            out+=' '
        elif(j==1):
            out+='/'
        else:
            out+='\\'
    print(out)

                
                
                
            
        
    
