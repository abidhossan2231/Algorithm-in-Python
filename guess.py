from random import randint
count1 = 0
count2 = 0
for x in range(1, 11):
    gn = int(input("\nInput your guessing number between 1 to 10 : "))
    rn = randint(1, 10)

    if gn == rn:
        print("\nYour guessing number is correct. ")
        count1 = count1 + 1

    else:
        print("\nYour guessing number is wrong. And correct number was : ", rn)
        count2 = count2 + 1
print("\n\nTotal correct guess ", count1, " out of 10")
print("\nTotal correct wrong ", count2, " out of 10")