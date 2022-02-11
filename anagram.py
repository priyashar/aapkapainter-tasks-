''' Write a code that checks if two given strings are anagrams
Sample Input: Mary Army
Output: Yes'''

w1 , w2 = 'Mary' , 'aRmy'

if len(w1)!=len(w2):
  print("they are not anagram")
else:
  if set(w1.lower())==set(w2.lower()):
    print("yes, they are anagram")