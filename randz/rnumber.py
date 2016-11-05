import time,math

def get_seed_rnum():
	t=0
	val=0
	for count in range(1, 4): 
		t=str(time.time())
		val+=int(t[-count])* (10 ** (count-1))
		count+=1
	return math.sqrt(val)/val

def rn_range(a, b):
	seed = get_seed_rnum()
	output = math.floor(seed * b * 10) + a
	if(output > a & output < b): 
		return math.floor(seed * b * 10) + a
	return rn_range(a, b)
		
if __name__ == "__main__":
	import sys
	print(rn_range(int(sys.argv[1]), int(sys.argv[2])))