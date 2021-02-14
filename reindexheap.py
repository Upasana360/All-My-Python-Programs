c = 0
N = int(input())
arr=list(map(int, input().split()[:N]))
ARR= [0] * N
#print(ARR)

for i in range(0,N):
    for j in range(0,N):
        if(arr[i]-arr[j]<0):
            c = c+1
            print(c) 
            
    ARR[c] = arr[i]
    c = c * 0
    print(ARR)
    
print(ARR)