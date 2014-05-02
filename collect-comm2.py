from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
el_per_process = 5000000

def avg(list):
	return float (sum(list) / (len(list)))

part_data=[]
for i in range(0, size):
	if rank == i:
		part_data = [random.randint(0, 99999) for _ in range(el_per_process)]
		part_data_avg = avg(part_data)

data = comm.gather(part_data_avg, root = 0)

if rank == 0:
	print avg(data)

