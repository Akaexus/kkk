
#https://adjule.pl/groups/ogolny/problems/ppr13
#silnia wielokrotna
def sw(n, k):
  if 0<=n and n<k:
    return 1
  elif n>=k:
    return n*sw(n-k, k)
 
for t in range(int(input())):
  n, k = [int(x) for x in input().split()]
  print(sw(n, k))
 
# zosia
#https://adjule.pl/groups/ogolny/problems/ppr12a
nOfBoxes = int(input())
boxes = [int(x) for x in input().split(' ')]
 
numberOfQueries = int(input())
for queryNumber in range(numberOfQueries):
  a, b = [int(x) for x in input().split(' ')]
  print(sum(boxes[a-1:b]))
