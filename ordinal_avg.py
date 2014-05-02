import random

def avg(list):
	return float (sum(list) / float(len(list)))

print avg([random.randint(0, 99999) for _ in range(20000000)])