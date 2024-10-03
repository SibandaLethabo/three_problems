length_list = input("Enter the length of the list:") 
numbers = []
even = []
def reversal():
    for i in range (int(length_list)):
        num = input(f"Enter num {i + 1}: ")
        numbers.append(int(num))

    for num in numbers :
        if num % 2 == 0 :
            even.append(num)
    return even[::-1]
    