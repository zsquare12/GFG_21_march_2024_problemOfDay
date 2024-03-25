# cook your dish here
T = int(input())
pair = [
    [0,0],
    [2,-2],
    [4,4],
    [6,2]
]
for _ in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  count = 0
  
  for k in range(N):
    x = A[k]

    if x in [i[0] for i in pair]:

        y = [i[1] for i in pair if i[0] == x][0]

        if y in A[k+1:] :
            count += 1
      
  print(count)
      
      