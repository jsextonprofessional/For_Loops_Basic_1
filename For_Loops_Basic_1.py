# 1. Basic - Print all integers from 0 to 150.
for basic in range(1, 151):
    print(basic)
# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for multi in range(5, 1001):
    if multi % 5 == 0:
        print(multi)
# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for dojoway in range(1, 101):
    print(dojoway)
    if dojoway % 10 == 0:
        print("Coding Dojo")
    elif dojoway % 5 == 0:
        print("Coding")
# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
whoa = 0

for odds in range(0, 500000):
    if odds % 2 != 0:
        whoa = whoa + odds
print(whoa)
# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for posi in range(2018, 0, -4):
    print(posi)
# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 3
highNum = 9
mult = 3

for flex in range(lowNum, highNum + 1, mult):
    if flex % mult == 0:
        print(flex)