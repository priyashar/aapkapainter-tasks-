'''Write a code that prints out individual scores of two players in a game of cricket where score is given as runs per ball in an array. In a game of cricket a person changes strike if he scores an odd number, and keeps strike with him if he scores an even number. No need to consider changing strike after every 6 balls or an over.
Sample Input1: [1,2]
Output1: p1: 1, p2: 2
Sample Input2: [1,2,3,2,1]
Output2: p1: 4, p2: 5
'''


def pf1(i):
  if i==0:
    p1.append(r[0])
  else:
    if(r[i-1]%2==0):
      if p1[i-1]==0:
       p1.append(0) 
      else:
        p1.append(r[i])
    else:
      if p1[i-1]!=0:
        p1.append(0)
      else:
        p1.append(r[i])

def pf2(i):
  if i==0:
    p2.append(0) #[1,2,3,2,1] p1[1,0,0,2,1] p2[0,2,3,0,0]
  elif i==1:
    if(r[i-1]%2!=0):
      p2.append(r[i])
    else:
      p2.append(0)
  else:
    if(r[i-1]%2==0):
      if p2[i-1]==0:
       p2.append(0) 
      else:
        p2.append(r[i])
    else:
      if p2[i-1]!=0:
        p2.append(0)
      else:
        p2.append(r[i])

r=[1,2,3,2,1]
p1=[]
p2=[]
for i in range(0,len(r)):
  pf1(i)
for j in range(0,len(r)):
  pf2(j)
print(p1)
print(p2)
print("score of Player1 is ", sum(p1))
print("score of Player2 is ", sum(p2))