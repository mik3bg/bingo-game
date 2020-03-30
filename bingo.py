import random
numbers = 0
count = 0
bingo = []
nums, nums1, nums2, nums3, nums4 = ([] for i in range(5))

####TIcket numbers Generator List###
###                              ###
nums, nums1, nums2, nums3, nums4 = ([] for i in range(5))
b, i, n, g, o = ([] for i in range(5))
# Random generation 1 to 15 B section
count = 0
while count < 5:
    if (count <= 4):
        numbers = random.choice(range(1, 15))
        nums.append(numbers)
        count += 1
        b = nums

count = 0
# Random generation 16 to 30 I section
while count < 5:
    if (count <= 4):
        numbers = random.choice(range(16, 30))
        nums1.append(numbers)
        count += 1
        i = nums1

count = 0
# Random generator 31 to 45 N section
while count < 4:
    if (count <= 4):
        numbers = random.choice(range(31, 45))
        nums2.append(numbers)
        count += 1
        n = nums2

count = 0
# Random generator 46 to 60 G section
while count < 5:
    if (count <= 4):
        numbers = random.choice(range(46, 60))
        nums3.append(numbers)
        count += 1
        g = nums3

count = 0
# Random generator 61 to 75 O section
while count < 5:
    if (count <= 4):
        numbers = random.choice(range(61, 75))
        nums4.append(numbers)
        count += 1
        o = nums4

b.extend(i)
b.extend(n)
b.extend(g)
b.extend(o)
bingo.extend(b)
bingoT = set(bingo)

##Add more number to bigoT set() if not 24
if(len(bingoT) != 24):
       while len(bingoT) < 24:
           bingoT.add(random.choice(range(1,75)))

print(bingoT)

###DRAW NUMBERS newDraw Function don`t need it!###
###                                            ###
drawNumbers = random.sample(set(range(1,75)), 38)
drawNumbers= set(drawNumbers)
print(drawNumbers)

print(drawNumbers & bingoT) ##Return matched numbers in two set()

##Return ready bingo ticket with indexing
##Fill up dict with index with for loop and fill with values from existing set()
bingoTicket = dict(zip({n:n for n in range(1,25)},{num:num for num in bingoT}))
print(bingoTicket)
