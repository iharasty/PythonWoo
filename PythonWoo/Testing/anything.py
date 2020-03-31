import PrimeNumberGen as prime

print("a")

while prime.currMax < 2000000:
    prime.genPrimes(1)

print("b")
sum = 0

for num in prime.setOfPrimes:
    print(num)
    sum += num
    
print(sum)