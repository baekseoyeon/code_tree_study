num_str = input()
num_list = num_str.split()
num_list[0],num_list[1] =num_list[1],num_list[0]

print(num_list[0],num_list[1])