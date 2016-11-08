import math

input_val= [0, 1, 1, 0, 0, 1, 0, 1]

# TODO:: FIX FOR INPUT 1

# val is varriable which should be a positive integer power and count should never
# be assigned when function is called.

# The function return 0 if val is not power of 2 and return binary array of pass 
def get_bool_count(val, count=1):
	if val == 2:
		return count
	if val % 2 != 0:
		return 0
	else:
		count+=1
		return get_bool_count(val/2, count)

def get_binary_table(val, count):
	arr=[0] * count
	for i in range(0, len(arr)):
		arr[i]=[0] * (2**count)
		# table_counter is a helpful variable which helps in counting numbers in binary
		table_counter=0
		switch_val= ( 2 ** (count - i) )/2
		for j in range(0, len(arr[i])):
			if table_counter < switch_val:
				table_counter+=1
				arr[i][j]=0
				continue
			if table_counter == ( 2 ** (count - i) ) - 1:
				table_counter=0
				arr[i][j]=1
				continue
			if table_counter >= switch_val:
				table_counter+=1
				arr[i][j]=1
				continue
	return arr

def get_zheg(input_arr):
	current_power = get_bool_count(len(input_arr))
	bool_table_list= get_binary_table(len(input_arr), current_power)
	output_arr=[0]* (2 ** current_power)

	for i in range(0, len(bool_table_list)):
		curr_arg=2 ** int(((current_power-i+1) / 2)) 
		print(curr_arg)
		print(output_arr[curr_arg])
		output_arr[i+1]=input_arr[curr_arg]
get_zheg(input_val)