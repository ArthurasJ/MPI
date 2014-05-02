from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
el_per_process = 5000000	

def avg(list):
	return float (sum(list) / (len(list)))

if rank == 0:
	data = [random.randint(0, 99999) for _ in range(el_per_process * size)]
	chunks = [[] for _ in range(size)]
	for i, chunk in enumerate(data):
		chunks[i % size].append(chunk)
else:
	data = None
	chunks = None

data = comm.scatter(chunks, root = 0)
sub_avg = avg(data)				
data = comm.gather(sub_avg, root = 0)

if rank == 0:
	print avg(data)

