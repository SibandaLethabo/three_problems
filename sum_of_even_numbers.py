def sum_of_even (nums):
    sum = 0
    for num in nums :
        if num % 2 == 0 :
            sum += num 
    return sum

length_list = input("Enter the length of the list:") 
numbers = []
for i in range (int(length_list)):
    num = input(f"Enter num {i + 1}: ")
    numbers.append(int(num))

print(sum_of_even(numbers))