'''Write a code that prints out the first occurrence of a duplicate in a given array of integers
Sample Input: [1,2,3,2,1]
Output: 2
'''
x = [1,2,3,2,1]
size = len(x)
Dulicate = []
for i in range(size):
    k = i + 1
    for j in range(k, size):
        if x[i] == x[j] and x[i] not in Dulicate:
            Dulicate.append(x[i])
print(Dulicate)
print(len(Dulicate))