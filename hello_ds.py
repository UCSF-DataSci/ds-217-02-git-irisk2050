print("Hello, Data Science!")

# we get (3, 5, 6, 9). The sum of these multiples is 23. 
# Find the sum of all the multiples of 3 or 5 below 1000.

target_num = 100 # we want multiples of 3 and 5 up until this number

mult_sum = sum(i for i in range(target_num) if i % 3 == 0 or i % 5 == 0)

print(f"Sum of multiples of 3 and 5 under below 100: {mult_sum}")