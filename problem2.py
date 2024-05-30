def filter_even(numbers):
    even_num = [num for num in numbers if num % 2 == 0]
    return even_num

input_string = input("enter a list: ")
input_list = list(map(int, input_string.split()))

output_list = filter_even(input_list)

print("ogl" , input_list)
print("enl" , output_list)