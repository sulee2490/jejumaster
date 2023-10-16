import random

print("로또 추첨")

lotto = random.sample(range(1,46),7)
a = lotto[0:6]
b = lotto[6:7]

print(a,'+',b)
a.sort()
print(a,'+',b)



