from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = {'a': 7, 'b': 3.14} #sukuriami fiktyvus duomenys

def send(data, dest, tag):
	comm.send(data, dest = dest, tag = tag)
	print "Pranesimas is proceso %s issiustas i %s procesa kanalu %s" % (rank, dest, tag)

def receive(source, tag):
	data = comm.recv(source = source, tag = tag)
	print "Pranesimas procese %s: gautas is proceso %s kanalu %s" % (rank, source, tag)

def receive_from():
	return ((rank + size) - 1) % size

def send_to():
	return (rank + 1) % size;

send(data, dest = send_to(), tag = 11) #dest - proceso numeris, kuriam siunciame pranesima #tag - "kanalo" numeris
receive(source = receive_from(), tag = 11) #paimame pranesima is 0 proceso, 11 kanalo	
