a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
count = 0
for i in range (a,b+1):
    if i % 3 == 0:
        count += 1
print(f"The count of numbers divisible by 3 is: {count}")